---
layout: post
title: Confronto tra Architettura Informatica e Biologica (Pt.2)
date: 2024-11-24
categories: [Essay]
tags: [paper ,scientifico, riflessioni] 
---

## **Random Acces Memory (RAM) e Memoria di lavoro biologica : Capacità e Limiti**




### **RAM: Le celle di memoria** 

La capacità della RAM si misura in **byte** limitata solo dalla tecnologia fisica. 


La RAM è organizzata in celle (o locazioni) ognuna capace di mantenere una quantità fissa di dati, ad esempio 1 byte, ogni cella quindi ha un indirizzo univoco, che funziona (semplificando molto) come il numero civico di una casa.
Nella RAM in un sistema a 64 bit, un indirizzo fisico può variare in base all’architettura specifica e alla quantità di RAM, ma è sempre rappresentato da un valore di 64 bit (numero che richiede 64 cifre binarie) come “0x1234567890ABCDEF” che rappresenta come già detto un’ubicazione specifica all’interno della memoria fisica del computer. Per puro esempio fittizio, “via Roma” potrebbe diventare “0x56696120526F6D61”. 

>*“Questo è un indirizzo testuale perché i suoi bit codificano una parola leggibile.* <br>
*Un indirizzo di RAM è invece solo un numero, che il computer usa come coordinate interne.”*

Un’altro esempio utile può essere contare le celle: <br>


Supponiamo di avere 4 GB (4.294.967.296 byte) di RAM, disposti come parole a 64 bit. <br>
Poiché ogni parola (word) è di 8 byte, ci saranno **4.294.967.296 byte / 8 byte per parola = 536,9 milioni di parole** da 64 bit.  
Ci saranno un totale di 4.294.967.296 byte x 8 = 34.359.738.368 bit. <br>
Ognuno di questi **bit** è memorizzato in una **"cella di storage"** fisica. Queste celle di storage sono implementate con strutture diverse (ad esempio **6T**, cioè 6 transistor per **bit**, o **1T1C**, cioè 1 transistor + 1 condensatore per **bit**), a seconda che sia SRAM o DRAM.

Questa distinzione fisica spiega perché le cache (SRAM, 6T) sono molto più veloci,  mentre la RAM di sistema (DRAM, 1T1C) è più densa ed economica ma deve essere periodicamente rinfrescata.".

**{ fare immagini confronto DRAM e SRAM }**



#### **Bus di indirizzi** 

La CPU invia l’indirizzo della cella da usare attraverso il bus di indirizzi (un insieme di linee elettriche o meglio conduttori che trasportano segnali 0 e 1 tra CPU e RAM). Se il bus di indirizzi ha $\mathbf{n}$ linee, si possono distinguere $\mathbf{2^n}$ indirizzi diversi.

Es: 32 linee = $\mathbf{2^32}$ = **4GB** di spazio utilizzabile.


#### **Bus dati**

Una volta scelta la “casa” i dati passano attraverso il bus dati, dopo la CPU fa operazioni di lettura e scrittura sulla cella in $\mathbf{O(1)}$ costante per ogni locazione.



>*"L'architettura di Von Neumann si fonda sul verdetto assoluto di Parmenide: **Essere** (1) o **Non Essere** (0). <br> Un unico, semplice principio per un universo digitale. <br> L'architettura neuromorfica, al contrario, pianta un giardino di infinite seeds biologiche, dove il calcolo non è un verdetto, ma un **ecosistema in divenire.**"*

---

### **Memoria Biologica, Capacità: 7±2 vs 4±1?**

#### **(Teoria di Miller ) Perchè Miller aveva Torto?** 

Miller (1956) contava chunks già consolidati, non items puri, per esempio “UNI-PAR-INF” sembrano 3 chunks (unità di informazione), ma sono 9 lettere che hai già imparato, in poche parole confondeva *capacità di storage* con *capacità di chunking*.

##### **(Teoria di Cowan) Focus attention**

Cowan (2001), ha fatto esperimenti con stimoli non verbalizzabili (toni puri, colori non nominabili), senza chunking possibile crolla a circa 4 items. Quindi propose come **4** il vero limite del "**Focus of attention**".

Ma cosa è un **chunk** veramente? E’ un’unità di informazione significativa e organizzata nella memoria di lavoro, non è definito dalla quantità fisica di dati, ma dal significato psicologico.

<u><strong>Definizione</strong></u>: “Qualsiasi configurazione di stimoli che è diventata familiare e significativa attraverso **l'esperienza**, e che viene trattata come una singola unità dalla memoria di lavoro."

Esempio con sequenza di lettere:

**Non-chunks, lettere random:**

“**X A Z P L R Y**” sono 7 elementi separati ogni lettera occupa uno slot di *Working memory*, carica di **WM: 7 chunks**.

**Chunks, lettere familiari:** 

“**GATTO FIORE SEDIA**” sono 12 lettere, ma solo 3 parole (3 chunks), ogni parola è un’unità familiare, carico di **WM: 3 chunks**.


#### **Amplificazione della capacità**

La WM ha circa 4 slot ma, ogni slot può contenere 1 chunk (semplice o complesso):

<figure style="margin: 2rem 0; text-align: center;">
  
  <img src="{{ '/assets/imgs/NvsE.svg' | relative_url }}" 
       alt="Diagramma Architettura Neuromorfica"
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <figcaption style="font-style: italic; font-size: 1em; color: #555; margin-top: 10px; line-height: 1.4;">
    <strong>“Non nasciamo con i chunks, vengono costruiti con l’esperienza”</strong><br>
  </figcaption>
</figure>


### **Come nascono i chunks? Esposizione ripetuta ad un pattern:**

Prima di tutto si cominciano a formare grazie all’esposizione ripetuta ad un **pattern:**

#### 1) **Meccanismi neuronali dell’esposizione, Encoding iniziale: formazione della traccia:**

<figure style="margin: 2rem 0; text-align: center;">
  
  <img src="{{ '/assets/imgs/MeccanismiNDE.svg' | relative_url }}" 
       alt="MeccanismiNDE"
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</figure>

<figure style="margin: 2rem 0; text-align: center;">
  
  <img src="{{ '/assets/imgs/Corteccia.jpg' | relative_url }}" 
       alt="Corteccia"
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</figure>

Nello **Stato iniziale**, ci sono **3 elementi separati**, codificati in neuroni distinti: <br> 
{Neurone A: “**U**” }; {Neurone B: “**N**” }; {Neurone C: “**I**” }.

Non c’è nessuna connessione forte tra loro



#### 2) **Ripetizione e rafforzamento sinaptico**

Principio Hebbiano base: **“Cells that wire together, fire together”**. \
Dopo esposizioni ripetute (10-100+ volte):


```python
# Pseudocodice neurale
for esposizione in range(ripetizioni):
    attiva(neurone_U)
    attiva(neurone_N)  # Immediatamente dopo
    attiva(neurone_I)  # Immediatamente dopo
    
    # Hebbian learning
    if neurone_U.attivo AND neurone_N.attivo:
        rinforza_sinapsi(U -> N)
    
    if neurone_N.attivo AND neurone_I.attivo:
        rinforza_sinapsi(N -> I)

# Dopo questo ciclo for, si formano connessioni forti. 

```

#### 3) **Long term potentiation (LTP), meccanismo molecolare**

Questo meccanismo (approfondendolo molto poco) parte con la **coincidenza temporale** (dai 20-100 ms), tra neuroni pre e post sinaptici.<br> Poi si attivano i recettori **NMDA**, a seguire si una un ingresso massiccio di $\mathbf{Ca^{2+}}$ nel neurone post sinaptico, in questo modo viene stimolato fortemente.  <br>
Questo calcio che entra nel neurone, **attiva** delle proteine speciali chiamate **chinasi**, queste funzionano come degli “**interruttori molecolari**” che attivano altri processi nella cellula modificando altre proteine esistenti o attivando la sintesi di nuove. <br> In pratica traducono il segnale elettrico in **cambiamenti biochimici duraturi**. Questo fenomeno delle chinasi è chiamato “**Cascata di chinasi**”.

I **recettori AMPA** sono i recettori che ricevono il segnale eccitatorio dal neurone presinaptico. Dopo la cascata di chinasi, la cellula post-sinaptica aggiunge più recettori AMPA sulla propria membrana. Quindi la sinapsi diventa più **sensibile**, ogni futuro segnale produrrà un risultato più forte. <br>

> *es: “Come aggiungere più antenne sul tetto, il segnale si riceve meglio”.*

A seguire, la crescita di nuove **spine dendritiche**, ovvero piccole protuberanze dei dendriti dove avvengono le sinapsi, con la stimolazione ripetuta la cellula può formare nuove spine o ingrossare quelle esistenti. <br>
Questo significa che si creano nuove connessioni fisiche o si rafforzano quelle vecchie tra neuroni.  


**Vari tempi del processo:**

**0-1 min: Early-LTP** (fosforilazione recettori esistenti) <br>
**1-3 ore: Late-LTP** (sintesi proteica, crescita spine) <br>
**Vari giorni: Consolidamento strutturale** (rimodellamento sinaptico) <br>

---

### **Riconoscimento del pattern come unità: da elementi a Gestalt**

La transizione da elementi a Gestalt descrive il passaggio dal percepire singoli elementi isolati (punti, linee, suoni, dati) al percepire una **forma organizzata e coerente**, cioè una Gestalt (termine tedesco che significa “forma”, “configurazione”, “insieme strutturato”).


#### **Chunking percettivo:**

Il cervello raggruppa elementi separati in **unità significative** più grandi e coerenti.


>“*Il sistema visivo non elabora ogni punto o linea singolarmente,ma li combina in **blocchi strutturati**  “chunk”  che rappresentano forme, oggetti o pattern"*

<br>

##### Esperimento classico: Chase & Simon (1973) 

<figure style="margin: 2rem 0; text-align: center;">
  
  <img src="{{ '/assets/imgs/Chase&Simon.svg' | relative_url }}" 
       alt="MeccanismiNDE"
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</figure>
[Link al paper in questione](https://andymatuschak.org/prompts/Chase1973.pdf)

#### **Statistical learning**

Il cervello non apprende solo in modo esplicito ( con regole o istruzioni ), ma anche in modo **statistico** e **implicito**, osservando quanto spesso certi eventi si verificano e in che ordine.

<u><strong>Stream continuo</strong></u>: "pukopaldogolabupuko..."

<u><strong>Dopo 2 minuti di esposizione</strong></u>: Neonati riconoscono "puko", "paldo", "golabu" come unità

Hanno estratto probabilità transizionali.


#### **Monitoraggio delle co-occorrenze**

Ogni volta che due stimoli (A e B) si presentano **vicini nel tempo o nello spazio**, il cervello registra la loro **co-occorrenza**, cioè il fatto che tendono ad apparire insieme. <br>
Con l’esperienza, questa informazione diventa **una misura di probabilità condizionata**, del tipo:  $\mathbf{P(B|A)}$ = probabilità che B segua A.

Se questa probabilità è **alta (vicina a 1)**, il cervello interpreta A e B come **unità funzionalmente legate**, quindi come unica entità percettiva e cognitiva. <br> La prevedibilità fa da “**collante**” neurale, le connessioni sinaptiche tra A e B vengono rafforzate.
Questo meccanismo avviene sia nei livelli sensoriali, sia nei livelli concettuali.

##### Le strutture neurali coinvolte sono:

* **Gangli basali** per apprendimento sequenziale e statistico, per imparare pattern temporali, per filtrare le sequenze che hanno alta coerenza temporale e alta ricompensa predetta. La **dopamina** è fondamentale per segnalare la precisione della predizione.

* **Cervelletto** per il timing cognitivo, affina la precisione cognitiva e temporale del chunking.

* **Corteccia prefrontale ventromediale** tecnicamente vmPFC, coinvolta nell’integrazione del valore e della probabilità, ovvero se una sequenza o un pattern è affidabile, prevedibile o vantaggioso, la vmPFC ne rafforza la traccia mnemonica.



### **Error-driven learning (Rescorla-Wagner)**

```python
# Pseudo codice

for ogni esposizione: 
  # prevedo che A porterà a B
  predizione = modello_interno("A")
    
  osservazione = realtà # B accade o no?
  error = osservazione - predizione  # quanto mi sono sbagliato
  if error > soglia:
      aggiorna_modello() # Rinforza A->B 
  else: 
      # Predizione corretta -> chunk consolidato 
      chunk_strength += 1

```

Questo pseudo codice sarebbe la versione “**computazionale**” del modello di Rescorla-Wagner (1972), che ha fatto da base teorica per tutto il **RL** (Reinforced learning) moderno (inclusa la backpropagation, in un certo senso). <br> Quest’ultimo si è poi rivelato una descrizione molto accurata di come i neuroni apprendono in generale.

#### Ruolo della **Dopamina**:

Nel cervello questo “**prediction error**” non è astratto, è una vera grandezza neurochimica, quando un evento positivo o negativo accade: <br>

Se il risultato è **migliore** del previsto => **scarica di dopamina (+)**; <br>
Se il risultato è **peggiore** del previsto => **scarica (-)**; <br>
Se è **come previsto** => **dopamina costante**;

Quindi la dopamina rappresenta ($\mathbf{osservazione - predizione}$), esattamente come l'`error` nel codice sopracitato.
 
Un confronto molto interessante può essere il seguente, senza andare troppo nel dettaglio:

<figure style="margin: 2rem 0; text-align: center;">
  
  <img src="{{ '/assets/imgs/TabellaAspetti.svg' | relative_url }}" 
       alt="Tabella Aspetti Informatica e Biologia"
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</figure>

**Il fatto interessante è che il cervello non impara “per ricompensa” nel senso stretto, ma per *riduzione dell’errore di predizione*, proprio come fanno i modelli moderni di Machine Learning**

Quando l’errore è **0**, significa che: <br> 
Il modello interno è ben **allineato con la realtà**, l’**associazione è stabile**, e l’informazione può essere compressa in un **chunk efficiente** (minor sorpresa porta a minor entropia che porta a miglior codifica).


> **“L’apprendimento non serve a conoscere il mondo, ma a ridurre la sorpresa di fronte ad esso.”**

<br>

--- 

### **Consolidamento nella memoria a lungo termine**

Un riflessione abbastanza riassuntiva, ma tecnica dei meccanismi principali di *consolidamento biologico*, con punti rilevamenti per la progettazione di sistemi neuromorfici e architetturali.


#### **Panorama Sintetico:**

Il consolidamento è il processo dove i chunk labili (instabili), vengono trasformati in rappresentazioni stabili e resistenti all’oblio. <br>
* **Consolidamento sinaptico**: minuti o ore. Cambiamenti locali nelle sinapsi (*potenziamento/depotenziamento*).
* **Consolidamento sistemico**: giorni o settimane (anche mesi). 
Riorganizzazione e trasferimento delle rappresentazioni tra *strutture* (es. tra ippocampo e corteccia).
* **Consolidamento strutturale/epigenetico**: settimane o anni. 
*Formazione o crescita delle spine dendritiche* (della quale abbiamo parlato qualche paragrafo fa durante la LTP) cambiamenti trascrizionali che stabilizzano a lungo termine.


### **Consolidamento sistematico & Replay**

Complementary learning system (***CLS*** ), teoria che spiega perché il cervello usa 2 sistemi: <br>
* **Ippocampo**: apprendimento rapido, indicizzazione di episodi, alta plasticità.
* **Corteccia**: apprendimento lento, integrando le informazioni in strutture semantiche stabili.

#### Replay offline:

Durante il riposo (slow wave NREM, anche detto deep sleep), l’ippocampo rigioca sequenze durante la veglia leggera e il sonno NREM  coordinate con oscillazioni corticali (modelli ritmici di attività neuronale). Questo replay guida il trasferimento e l’integrazione delle tracce nella corteccia, **riducendo la dipendenza dall’ippocampo**.

#### Assimilazione in schemi:

Il consolidamento non è una semplice copia, è una “**ristrutturazione**”, le nuove tracce vengono integrate nei network corticali esistenti (generalizzazione) o restano episodiche se non integrate.


### **Stabilità vs Plasticità**

Consolidare richiede **stabilizzare sinapsi**, ma il cervello deve pur sempre mantenere la capacità di apprendere (plasticità). 

Esistono **meccanismi omeostatici** (scaling sinaptico, metaplastica) che regolano la soglia di plasticità e prevengono saturazione.

**Reconsolidation**: il recupero di una memoria può renderla nuovamente labile; una seconda finestra di plasticità permette aggiornamenti o cancellazioni mirate.



### **Gating & Correlatori neurochimici**

I **neuromodulatori** come la dopamina, modulano se e quando consolidare, **segnali di valore** e **stati comportamentali** (attenzione, sorpresa) aprono *“windows”* di consolidamento. <br> Questo meccanismo di **gating** evita di consolidare tutto indiscriminatamente, solo ciò che ha valore ed è prevedibile tende ad essere stabilizzato.

---

## **Implicazioni per la computazione neuromorfica**

**Von Neumann**: consolidamento è una copia **esplicita**, (RAM -> Storage). Operazione deterministica, separata e spesso sincronizzata. <br>
**Biologia / Neuromorfica**: consolidamento è una **trasformazione adattiva e distribuita**, le memoria vengono ristimate e riorganizzate integrandole. <br> Dunque è un processo continuo, regolato localmente, modulato globlamente, e sostenuto da offline replay.

### Aspetti più importanti da emulare:

#### **Doppio canale di apprendimento**:

Memorie temporanee in strutture ad alta plasticità + trasferimento graduale a storage NVM (memristive arrays o weight banks non volatili). [Approfondimento](https://www.nature.com/articles/s41563-019-0291-x)

<figure style="margin: 2rem 0; text-align: center;">
  <img src="{{ '/assets/imgs/SNN_syn.webp' | relative_url }}" 
       alt="SNN synapses"
       style="max-width: 80%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</figure>

#### **Replay offline**:

Meccanismi di riattivazione sequenziale (on-chip or scheduled) per consolidare pesi a lungo termine (analogo a experience replay / distillation in ML).

<figure style="margin: 2rem 0; text-align: center;">
  <img src="{{ '/assets/imgs/' | relative_url }}" 
       alt="Replay offline"
       style="max-width: 80%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</figure>

#### **Two-timescale plasticity**:

Modelli che combinano tracce veloci (contatori temporali) con tracce lente (stabilizzazione, retention flags).

#### **Synaptic tagging emulation**:

Flag locali che indicano “ready to stabilize”. Solo le sinapsi taggate possono acquisire proteine/aggiornamenti globali.

<figure style="margin: 2rem 0; text-align: center;">
  <img src="{{ '/assets/imgs/' | relative_url }}" 
       alt="Synaptic tagging emulation"
       style="max-width: 80%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</figure>

Questo diagramma illustra come una **stimolazione debole** (che induce "Early-LTP") imposta un "tag" (etichetta) locale sulla sinapsi. Successivamente, una **stimolazione forte** (in un'altra sinapsi o nel corpo cellulare) genera proteine di plasticità (l'aggiornamento globale). <br> Queste proteine viaggiano in tutta la cellula, ma solo la sinapsi precedentemente "taggata" può catturarle, convertendo così la sua traccia temporanea in un potenziamento stabile e a lungo termine ("Late-LTP")


#### **Gating neuromodulatorio**:

Segnali globali (dopamine like) che avviano o sopprimono la consolidazione, utile per risparmio energetico e selettività. 


#### **Algoritmo R-STDP <br> (Reward-Modulated Spike-Timing-Dependent Plasticity)**:

Lo STDP standard è la regola di apprendimento "hebbiana" per neuroni a spiking: se un neurone pre-sinaptico spara poco prima di uno post-sinaptico, la sinapsi si rinforza (Long-Term Potentiation). <br> Se spara dopo, si indebolisce (Long-Term Depression).

```python
# Parametri globali

dopamine_trace = 0  # Traccia del neuromodulatore globale
learning_rate_base = 0.01  # Tasso di apprendimento base
decay_rate = 0.95  # Decadimento della traccia della dopamina

# Per ogni sinapsi (i -> j) nella rete
for synapse in network.synapses:
    # 1. Calcola il cambiamento sinaptico standard con STDP
    stdp_delta = calculate_stdp(synapse.pre_spikes, synapse.post_spikes)
    
    # 2. Modula il cambiamento con il segnale di ricompensa globale
    # La dopamina può scalare l'ampiezza dell'update
    effective_learning_rate = learning_rate_base * dopamine_trace
    
    # 3. Applica l'update modulato alla sinapsi
    synapse.weight += effective_learning_rate * stdp_delta
    
    # Oppure => la dopamina può abilitare/disabilitare l'update
    # if dopamine_trace > threshold:
    #     synapse.weight += learning_rate_base * stdp_delta

# 4. Aggiorna il segnale neuromodulatorio globale (es. semplificato)
# Questo segnale viene calcolato altrove, da un modulo di "critico" o da un input esterno
dopamine_trace = dopamine_trace * decay_rate + external_reward_signal

```

**R-STDP** è molto utile per il risparmio energetico: la plasticità sinaptica, che è un processo ad alto costo computazionale, avviene solo quando **dopamine_trace** è alto. In assenza di segnali rilevanti, i pesi sono "*congelati*". <br>
Inoltre per la sua **selettività**: solo i percorsi neurali **attivi subito prima** del segnale di ricompensa vengono consolidati. I percorsi irrilevanti non vengono modificati.


Negli **HW neuromorfici** (come i chip di Intel Loihi o IBM TrueNorth), questi algoritmi non sono software che gira su una CPU, ma sono implementati direttamente nel circuito (**embedded** nel HW):

* **Segnale di Broadcast**: Un singolo segnale (una linea di tensione) può essere diffuso attraverso il chip per rappresentare: `dopamine_trace` o `ach_level`.


* **Circuiti Modulati**: I blocchi che calcolano l'update dei pesi sinaptici o la soglia di attivazione hanno un ingresso aggiuntivo per questo segnale di broadcast. Un **moltiplicatore analogico** può facilmente implementare: <br>
`effective_learning_rate = learning_rate_base * dopamine_trace` .

* **Memorie Locali**: Ogni sinapsi o neurone ha i suoi parametri locali (peso, soglia base), che vengono modificati in modo "context-dependent" dal segnale globale.


>Il **gating neuromodulatorio** fornisce un meccanismo **elegante** e **biologicamente plausibile** per conferire alle reti neuromorfiche proprietà di adattamento, efficienza e robustezza che sono essenziali per operare in ambienti **reali**, **non strutturati** e con **risorse limitate**.


Inserire finale e conclusioni per la Pt.3



<script type="text/javascript">
  window.MathJax = {
    tex: {
      inlineMath: [['$', '$'], ['\\(', '\\)']],
      displayMath: [['$$', '$$'], ['\\[', '\\]']],
      processEscapes: true
    },
    svg: {
      fontCache: 'global'
    }
  };
</script>
<script type="text/javascript" id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js">
</script>