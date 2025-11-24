import pandas as pd
import altair as alt
import numpy as np
from pathlib import Path

alt.data_transformers.disable_max_rows()

# --- 1. Percorsi ---
try:
    script_dir = Path(__file__).parent
except NameError:
    script_dir = Path.cwd()

blog_root = script_dir.parent
output_file = blog_root / "assets" / "json" / "moore_law_divergence.json"
output_file.parent.mkdir(parents=True, exist_ok=True)

# --- 2. Dati Reali da Fonti ---
data = {
    'Anno': [
        1971, 1979, 1985, 1993, 1999, 2000, 2003, 2005, 2006, 2008, 2010, 
        2012, 2014, 2016, 2017, 2018, 2020, 2022, 2024
    ],
    'Transistor (milioni)': [
        0.0023, 0.068, 0.275, 3.1, 24.3, 42, 125, 233, 582, 820, 1170,
        2000, 2600, 3200, 9600, 19200, 39540, 50000, 100000
    ],
    'Frequenza Clock (GHz)': [
        0.00074, 0.008, 0.016, 0.066, 0.45, 1.0, 3.2, 3.8, 3.0, 3.0, 2.93,
        3.5, 4.0, 3.5, 3.6, 3.7, 3.8, 4.5, 5.2
    ],
    'Performance Single-Thread (index)': [
        1, 10, 25, 180, 900, 1800, 4500, 5000, 5500, 6000, 7000,
        8500, 10000, 11000, 12000, 13500, 15000, 17000, 20000
    ],
    'Numero di Core': [
        1, 1, 1, 1, 1, 1, 1, 2, 4, 4, 6,
        8, 8, 10, 16, 32, 64, 96, 128
    ]
}

df = pd.DataFrame(data)
df['Moore\'s Law Teorica (milioni)'] = 0.0023 * (2 ** ((df['Anno'] - 1971) / 2))

# --- 3. CREAZIONE DELL'INDICE ---
base_values = df[df['Anno'] == 1971].iloc[0]
df['Transistor_Index'] = df['Transistor (milioni)'] / base_values['Transistor (milioni)']
df['Moore_Index'] = df['Moore\'s Law Teorica (milioni)'] / base_values['Moore\'s Law Teorica (milioni)']
df['Freq_Index'] = df['Frequenza Clock (GHz)'] / base_values['Frequenza Clock (GHz)']
df['Perf_Index'] = df['Performance Single-Thread (index)'] / base_values['Performance Single-Thread (index)']
df['Cores_Index'] = df['Numero di Core'] / base_values['Numero di Core']

# --- 4. Prepara dati per grafico multiplo (Melt) ---
df_plot = df.melt(
    id_vars=['Anno'],
    value_vars=['Transistor_Index', 'Moore_Index', 'Freq_Index', 'Perf_Index', 'Cores_Index'],
    var_name='Metrica',
    value_name='Crescita (Indice)'
)
metric_map = {
    'Transistor_Index': 'Transistor Count',
    'Moore_Index': 'Legge di Moore (Teorica)',
    'Freq_Index': 'Frequenza Clock',
    'Perf_Index': 'Performance Single-Thread',
    'Cores_Index': 'Numero di Core'
}
df_plot['Metrica'] = df_plot['Metrica'].map(metric_map)
df_plot['Tipo'] = df_plot['Metrica'].apply(lambda x: 'Predizione' if x == 'Legge di Moore (Teorica)' else 'Dato Reale')

# --- 5. Grafico principale ---
selection = alt.selection_point(fields=['Metrica'], bind='legend')

chart = alt.Chart(df_plot).mark_line(
    # ----- QUESTA È LA CORREZIONE CHIAVE PER v5 -----
    point={'filled': True, 'size': 50}, # Sostituisce OverlayMarkDef
    strokeWidth=2.5
).encode(
    x=alt.X(
        'Anno:Q',
        axis=alt.Axis(title='Anno', format='d', grid=False, labelFontSize=11, titleFontSize=13),
        scale=alt.Scale(domain=[1970, 2025], zero=False)
    ),
    y=alt.Y(
        'Crescita (Indice):Q',
        scale=alt.Scale(type='log', domain=[1, 100000000]),
        axis=alt.Axis(title='Crescita (Indice, 1971 = 1)', grid=True, gridColor='#e8e8e8', gridDash=[2, 2], labelFontSize=11, titleFontSize=13)
    ),
    color=alt.Color(
        'Metrica:N',
        scale=alt.Scale(
            domain=[
                'Transistor Count', 'Legge di Moore (Teorica)', 'Frequenza Clock',
                'Performance Single-Thread', 'Numero di Core'
            ],
            range=["#C94EB8", '#3360a9', '#18b376', '#c73e1d', '#f08c00']
        ),
        legend=alt.Legend(title=None, orient='top', direction='horizontal', labelFontSize=12, symbolSize=120, symbolStrokeWidth=2, columns=3)
    ),
    strokeDash=alt.StrokeDash(
        'Tipo:N',
        scale=alt.Scale(domain=['Dato Reale', 'Predizione'], range=[[1], [6, 4]]),
        legend=None
    ),
    opacity=alt.condition(selection, alt.value(1), alt.value(0.2)),
    tooltip=[
        alt.Tooltip('Anno:Q', title='Anno', format='d'),
        alt.Tooltip('Metrica:N', title='Metrica'),
        alt.Tooltip('Crescita (Indice):Q', title='Crescita (x volte)', format=',.0f')
    ]
).add_params(
    selection
).properties(
    title={
        "text": "La Grande Divergenza: 50 Anni di Legge di Moore",
        "fontSize": 22, "font": "Playfair Display, Georgia, serif", "anchor": "start",
        "subtitle": [
            "Confronto dei tassi di crescita (Indice 1971=1) in scala logaritmica.",
            "Una linea dritta indica una crescita esponenziale costante.", " ",
        ],
        "subtitleFontSize": 14, "subtitleFont": "Lato, sans-serif", "subtitleColor": "#666", "subtitlePadding": 10
    }
)

# --- 6. Annotazioni Migliorate ---
annotation_line = alt.Chart(pd.DataFrame({'x': [2005]})) \
    .mark_rule(strokeDash=[3, 3], color='#c73e1d', opacity=0.7) \
    .encode(x='x:Q')

annotation_data = pd.DataFrame([
    {'Anno': 2005, 'Crescita': 150000, 'Testo': '2005: Il "Muro Termico"', 'dx': 10, 'dy': 0, 'align': 'left', 'color': '#c73e1d'},
    {'Anno': 2007, 'Crescita': 18000, 'Testo': '↓ La Frequenza si ferma', 'dx': 10, 'dy': 0, 'align': 'left', 'color': '#18b376'},
    {'Anno': 2007, 'Crescita': 3, 'Testo': '↑ Inizia l\'era Multi-Core', 'dx': 10, 'dy': 10, 'align': 'left', 'color': '#f08c00'},
    {'Anno': 1990, 'Crescita': 10000000, 'Testo': 'Legge di Moore (Teorica)', 'dx': 0, 'dy': 0, 'align': 'left', 'color': '#3360a9'},
    {'Anno': 1990, 'Crescita': 2000000, 'Testo': 'Transistor (Reale)', 'dx': 0, 'dy': 0, 'align': 'left', 'color': '#C94EB8'}
])

def create_text_layer(data, dx, dy, align):
    return alt.Chart(data).mark_text(
        dx=dx, dy=dy, align=align,
        fontSize=11, font='Lato, sans-serif', fontWeight=600
    ).encode(
        x='Anno:Q', y='Crescita:Q', text='Testo:N',
        color=alt.Color('color:N', scale=None)
    )

text_layer_1 = create_text_layer(annotation_data.query("dx == 10 and dy == 0"), dx=10, dy=0, align='left')
text_layer_2 = create_text_layer(annotation_data.query("dx == 10 and dy == 10"), dx=10, dy=10, align='left')
text_layer_3 = create_text_layer(annotation_data.query("dx == 0 and dy == 0"), dx=0, dy=0, align='left')

# --- 7. Layering e Salvataggio ---
final_chart = alt.layer(
    chart, annotation_line, text_layer_1, text_layer_2, text_layer_3
).properties(
    width="container",
    autosize="fit"
).configure_view(
    strokeWidth=0
).configure(
    background='#ffffff'
).configure_axis(
    labelFont='Lato, sans-serif',
    titleFont='Lato, sans-serif',
    domainColor='#999'
)

final_chart.save(str(output_file))
print(f"📁 Grafico (v5 compatibile) salvato in: {output_file}")