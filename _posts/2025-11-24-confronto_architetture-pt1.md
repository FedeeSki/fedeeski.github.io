---
layout: post
title: Confronto tra Architettura Informatica e Biologica (Pt.1)
date: 2024-11-24
categories: [Essay]
tags: [paper ,scientifico, riflessioni] 
---

<div style="text-align: right; margin-bottom: 20px;">
  <a href="{% post_url 2025-11-24-comparison-architectures-pt1 %}" style="
      background-color: #f8f9fa;
      border: 1px solid #ddd;
      border-radius: 20px;
      padding: 8px 15px;
      text-decoration: none;
      color: #333;
      font-size: 0.9em;
      font-family: sans-serif;
      box-shadow: 0 2px 4px rgba(0,0,0,0.05);
      transition: all 0.3s ease;">
    🇬🇧 <strong>Read in English</strong>
  </a>
</div>

## **Motivazione: Perché Confrontare Architetture Informatiche e Biologiche**

[Lettura da PC consgiliata] <br>

L'evoluzione dell'informatica moderna si trova a un punto di svolta cruciale. Mentre la Legge di Moore rallenta e i limiti fisici del silicio si avvicinano, l'industria tecnologica cerca nuovi paradigmi computazionali che possano superare le barriere tradizionali dell'elaborazione digitale. <br>
Parallelamente, la nostra comprensione dei meccanismi neurali alla base della cognizione umana ha raggiunto livelli di dettaglio senza precedenti, rivelando principi di elaborazione dell'informazione che differiscono radicalmente dalle architetture di von Neumann. 

<div id="grafico-moore" style="width: 100%; max-width: 900px; margin: 0 auto; overflow-x: auto;">
  </div>
<script type="text/javascript">
  function drawMooreChart() {
    var spec = "https://raw.githubusercontent.com/FedeeSki/fedeeski.github.io/refs/heads/main/assets/json/moore_law_divergence.json";
    var embedOptions = {
      "mode": "vega-lite",
      "width": "container",
      "height": 450,
      "actions": false
    };
    vegaEmbed('#grafico-moore', spec, embedOptions)
      .catch(console.error); 
  }
  document.addEventListener('DOMContentLoaded', drawMooreChart);

</script>

<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>


Il cervello umano, con i suoi circa 86 miliardi di neuroni e 100 trilioni di sinapsi, rappresenta il sistema di elaborazione dell'informazione più sofisticato conosciuto. Consuma appena 20 watt di energia (meno di una lampadina) eppure supera i computer più potenti in compiti come il riconoscimento di pattern, l'apprendimento adattivo e l'elaborazione contestuale. Questa straordinaria efficienza deriva da principi architetturali fondamentalmente diversi: elaborazione massivamente parallela, memoria distribuita, plasticità adattiva e integrazione tra storage e processing.

Dall'altro lato, i sistemi informatici moderni hanno raggiunto prestazioni computazionali impressionanti attraverso l'ottimizzazione di architetture sequenziali, gerarchie di memoria rigide e algoritmi deterministici. Tuttavia, questi stessi punti di forza diventano limitazioni quando si tratta di adattabilità, efficienza energetica e robustezza ( caratteristiche in cui i sistemi biologici eccellono naturalmente).

Il confronto sistematico tra questi due paradigmi non è meramente accademico. L'industria tecnologica sta già investendo miliardi di dollari in tecnologie neuromorphic (Intel Loihi, IBM TrueNorth), algoritmi bio-inspired (reti neurali, evolutionary computing).
Comprendere i principi fondamentali che governano entrambi i domini è essenziale per guidare il prossimo salto evolutivo dell'informatica.

Inoltre, questo confronto assume particolare rilevanza nel contesto dell'intelligenza artificiale contemporanea. Mentre i LLM raggiungono capacità sempre più sofisticate, rimangono domande fondamentali sui loro meccanismi interni e su quanto si avvicinino ai processi cognitivi biologici. L'analisi comparativa delle architetture può fornire intuizioni cruciali per lo sviluppo di AI più efficienti.

Dal punto di vista ingegneristico, questo studio mira a identificare principi trasferibili che possano informare la progettazione di sistemi embedded, real-time e safety-critical;  settori dove l'efficienza energetica, l'adattabilità e la fault tolerance sono parametri critici. L'industria aerospaziale, della difesa ad esempio richiede sempre più sistemi che combinino prestazioni computazionali elevate con caratteristiche tipicamente biologiche: apprendimento continuo, robustezza ai guasti e operazione in ambienti incerti.

Questo lavoro si propone quindi di costruire un ponte tra neuroscienze computazionali e ingegneria dei sistemi.

Ora per comprendere in modo concreto le differenze tra questi due mondi, è utile analizzare le loro architetture di base: il classico modello di **von Neumann**, che ha guidato l’informatica per oltre 70 anni.
## **Il paradigma classico: Von Neumann**

<figure style="margin: 2rem 0; text-align: center;">
  
  <img src="{{ '/assets/imgs/Disegno1VN.svg' | relative_url }}" 
       alt="Diagramma Architettura Von Neumann Classica con CPU, RAM e BUS"
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  
</figure>

Ecco come immaginiamo un computer in teoria: un sistema pulito e modulare. La CPU agisce come il cervello, dividendo i compiti tra la Control Unit (che dirige il traffico) e l'ALU (che esegue i calcoli). La RAM funge da magazzino ordinato. Tra RAM e CPU viaggia sul System Bus, un'autostrada digitale che sulla carta appare libera e scorrevole. Questa separazione geometrica ha permesso la rivoluzione digitale, ma nasconde un prezzo energetico invisibile che esploreremo a breve.

#### **La realtà Fisica, il Memory Wall**

<figure style="margin: 2rem 0; text-align: center;">
  
  <img src="{{ '/assets/imgs/Disegno2VN.svg' | relative_url }}" 
       alt="Von neumann bottleneck scheme"
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  
</figure>


Qui l'eleganza crolla. La CPU lavora a frequenze altissime (GHz), ma è costretta a rallentare drasticamente perché il Bus agisce come un imbuto. I dati si accalcano in uscita dalla RAM, creando un ingorgo che lascia il processore in uno stato di **Data Starvation** (Fame di dati). La CPU non consuma energia solo per calcolare, ma la spreca in **cicli di stallo** (Memory stalls), costretta all'inattività mentre attende che le informazioni attraversino questa strettoia.
È il famoso **Von Neumann Bottleneck**.



### **L'Unità Biologica: Oltre il semplice "Perceptron"**

Abituati alle ANN siamo abituati a pensare che un neurone possa essere una cosa semplice come un Perceptron (somma pesata + funzione di attivazione), in realtà il “neurone biologico” è un sistema più complesso e ricco. <br>


**Dendriti**: non sono semplici fili di input o “I/O system” (ovvero che si limitano a trasmettere positivamente i segnali sinaptici al soma) , ma strutture che eseguono operazioni locali, integrazione spaziale e temporale.  <br>

* Possiedono **canali ionici voltaggio-dipendent**i che possono massimizzare o minimizzare i segnali in transito (con equazioni differenziali non lineari, dando un comportamento caotico/oscillante). 
* Generano **potenziali d’azione** dendritici locali che si propagano sia verso il soma che lateralmente (propagazione tra rami della stessa cellula), all’indietro (**Backpropagating Action Potential** (bAP) lungo i dendriti), saltando da un “ramo” all’altro attraverso i numerosi punti di ramificazione. Inoltre questi potenziali dendritici possono propagarsi da un ramo a un ramo "fratello" che origina dallo stesso punto di biforcazione. Questo permette **comunicazione incrociata** tra diversi input che arrivano su rami adiacenti
* **Gap junctions** dendro-dendritiche: Alcune connessioni elettriche dirette (gap junctions) collegano i dendriti di neuroni vicini, permettendo propagazione diretta di correnti elettriche senza bisogno di neurotrasmettitori. <br>


Semplificando, queste trasmissioni “laterali” permettono: **sincronizzazione locale** (coordinare attività di neuroni vicini), **integrazione cross-modale** (combinare input da diverse fonti), **amplificare il segnale** (rinforzare pattern di attivazione importanti) e **modulazione locale**: permettere **fine-tuning** dell'elaborazione senza coinvolgere circuiti più ampi.  <br>

<figure style="margin: 2rem 0; text-align: center;">
  
  <img src="{{ '/assets/imgs/ANN.svg' | relative_url }}" 
       alt="Modello del Neurone Artificiale (Perceptron)"
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
       
  <figcaption style="font-style: italic; font-size: 0.9em; color: #555; margin-top: 10px; line-height: 1.4;">
    <strong>Il Modello del Neurone Artificiale (Perceptron).</strong><br>
  </figcaption>
  
</figure>

L'immagine illustra l'astrazione matematica alla base delle ANN. Il processo è un flusso sequenziale:
* **Input Ponderati** ($\mathbf{x \cdot w}$): I dati in ingresso ($\mathbf{x}$) vengono moltiplicati per i rispettivi pesi ($\mathbf{w}$), che ne determinano l'importanza relativa.
* **Integrazione**($\mathbf{\Sigma}$): I segnali ponderati vengono sommati algebricamente in un unico nodo centrale (da qui il termine "Point Neuron"). Tutta la complessità spaziale viene ridotta a un singolo valore scalare.
* **Attivazione** (Non-linearità): La somma passa attraverso una funzione (grafico a destra, es. Sigmoide) che decide l'intensità dell'Output, introducendo la non-linearità necessaria per l'apprendimento.
<br>

<figure style="margin: 2rem 0; text-align: center;">
  <img src="{{ '/assets/imgs/SNN_bio.svg' | relative_url }}" 
       alt="Confronto tra Neurone Artificiale (Point Neuron) e Neurone Biologico (Dendritic Computation)"
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <figcaption style="font-style: italic; font-size: 0.9em; color: #555; margin-top: 10px; line-height: 1.4;">
    <strong>Schema di una rete di neuroni biologici (Multi-compartment model).</strong><br>
  </figcaption>
</figure>

A differenza del modello artificiale, qui il calcolo non è concentrato in un punto, ma è diffuso nello spazio e nel tempo:

* **Input Sinaptici** (Eccitazione/Inibizione): I segnali non sono numeri astratti, ma spike provenienti da altri neuroni (i cerchi verdi più piccoli a destra). Notate il dettaglio cruciale: alcuni input eccitano (frecce), altri inibiscono (linee piatte a T), bloccando attivamente il segnale.
* **Dendriti Attivi** (Il vero processore): I rami non sono cavi passivi. Ogni biforcazione agisce come un piccolo centro di calcolo indipendente che filtra, somma o blocca i segnali prima che arrivino al centro. Come evidenziato in rosso: "Il calcolo avviene qui, non solo nel Soma!".
* **Integrazione** (Spike Decision): Il corpo cellulare (Soma) riceve il risultato di tutte queste elaborazioni locali. Non fa una semplice somma, ma prende una decisione complessa basata su quando e come sono arrivati i segnali.
* **Output** (Assone): Se la soglia viene superata, parte lo Spike (il fulmine arancione), un evento digitale che viaggia verso altri neuroni.

#### **Sincronizzazione locale**

Questa elaborazione locale ad altissima velocità **si contrappone** ai meccanismi di comunicazione tra **processi informatici separati (IPC)**.

Quando due processi (che non condividono memoria, come due programmi diversi) devono comunicare, non possono usare la cache L1. Devono chiedere al sistema operativo di fare da mediatore usando meccanismi come:

* **Shared Memory (Memoria Condivisa):** Il sistema operativo assegna un'area di RAM comune.
* **Message Passing (Scambio di Messaggi):** Il sistema operativo si fa carico di copiare i dati da un processo all'altro.

In entrambi i casi, questa comunicazione ha una **latenza molto maggiore** e un **enorme overhead** del sistema operativo. Inoltre, per evitare che i processi scrivano contemporaneamente nella *shared memory* creando caos, sono necessari strumenti di sincronizzazione come i **semafori**, che aggiungono ulteriore latenza e complessità.

>*"Nei **neuroni**, l'elaborazione è altamente parallela e locale: i compartimenti dendritici integrano gli input quasi istantaneamente, un po' come i **thread** di un processore condividono la velocissima cache L1 per i calcoli locali.”*

<br>

####  **Fine tuning**

Il Fine Tuning nelle ANN è **globale**:

```python
# Tutto il gradiente deve propagarsi attraverso TUTTA la rete 
for layer in network: 
      layer.weights += learning_rate * global_gradient[layer]
```


La **Backpropagation globale**: ogni peso dipende dall'errore finale, richiede **forward pass completa** + **backward pass completa** quindi computazionalmente costoso: O(n) per tutti i parametri. **Lock-step learning**: tutta la rete deve "fermarsi" per l'aggiornamento. <br>


Per i Dendriti il Fine Tuning è “**ultralocale**”:


```c
// Pseudocodice biologico
if (pre_synaptic_activity && post_synaptic_activity){
      strengthen_synapse_locally();  // Solo questa sinapsi!
}
    
if (pre_synaptic_activity && NO_post_synaptic_activity){
      weaken_synapse_locally();
}
    
```

Questo tocca il cuore del “**Credit Assignment Problem**”. 
La **backpropagation** lo risolve in modo esatto ma **biologicamente implausibile**. Il cervello usa invece un'euristica locale (come la STDP): assegna il “credito”' basandosi solo sulla correlazione temporale tra l'attività locale e quella immediatamente successiva, un'approssimazione molto più veloce ed efficiente. <br>

#### **Plasticità hebbiana: “Neurons that fire together, wire together”**

La regola hebbiana è il paradigma della **plasticità locale**. Ogni sinapsi decide autonomamente se rafforzarsi o indebolirsi in base alla sola attività pre e post sinaptica.
Se due neuroni si attivano quasi contemporaneamente, la connessione che li unisce tende a potenziarsi: “***Neurons that fire together, wire together*** ”. <br> <br>
Un’estensione chiave di questo principio è la **spike-timing dependent plasticity** (STDP), che introduce una finestra temporale di circa 20 millisecondi: se il neurone presinaptico spara poco prima di quello postsinaptico, la sinapsi si rafforza; se l’ordine si inverte, si indebolisce.
Questo meccanismo consente un apprendimento fine e temporale, completamente guidato dalle dinamiche locali di ciascuna sinapsi.

<figure style="margin: 2rem 0; text-align: center;">
  <img src="{{ '/assets/imgs/STDP.svg' | relative_url }}" 
       alt="Grafico Spike-Timing Dependent Plasticity (STDP)"
       style="max-width: 80%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <figcaption style="font-style: italic; font-size: 0.9em; color: #555; margin-top: 10px; line-height: 1.4;">
    <strong>La Regola del Tempo (STDP).</strong><br>
  </figcaption>
</figure>
Il grafico illustra la finestra temporale critica per l'apprendimento sinaptico:

* **Asse X (Tempo Relativo)**: Misura la differenza $\mathbf{\Delta t = t_{post} - t_{pre}}$. Se è positiva (destra), l'input ha preceduto l'output (causalità).
* **Causalità** (LTP, Verde): Se il neurone presinaptico spara appena prima *(0ms - 20ms)* del postsinaptico, la sinapsi viene fortemente potenziata. Questo riflette il principio hebbiano: ***"Ho contribuito al tuo sparo, quindi siamo collegati"***.
* **Anti-Causalità** (LTD, Rosso): Se l'input arriva dopo che il neurone ha già sparato (parte sinistra), la connessione è inutile o dannosa e viene depressa (indebolita).
* **Decadimento Esponenziale**: Notate come l'effetto svanisca rapidamente. Oltre la finestra di *+/- 20ms*, la correlazione temporale è persa e non c'è plasticità significativa.

#### **Equilibrio come obiettivo**

Accanto al rafforzamento hebbiano, ogni dendrite possiede un proprio set point di attivazione che tende a mantenere stabile.
La plasticità omeostatica regola l’eccitabilità locale per evitare che il neurone diventi iper- o ipo-attivo, garantendo stabilità a lungo termine senza necessità di supervisione globale. <br>
È un meccanismo di auto-regolazione che permette al sistema di restare funzionale anche di fronte a cambiamenti ambientali o strutturali.

### **L'Architettura Distribuita: Il caos ordinato dei neuroni**

<figure style="margin: 2rem 0; text-align: center;">
  
  <img src="{{ '/assets/imgs/DisegnoSNN.svg' | relative_url }}" 
       alt="Diagramma Architettura Neuromorfica"
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  
</figure>


Nel paradigma biologico (e neuromorfico), la "tirannia" del **System Bus** viene abbattuta.

Non c'è più un centro. Invece di un'unica autostrada intasata, si ha una **rete mesh asincrona** (NoC).
Il cambiamento radicale è nella **co-locazione**: la memoria non è più in un "magazzino esterno" (RAM), ma è "spalmata" fisicamente sulle connessioni stesse (i pesi sinaptici). Quando un dato (spike) arriva, viene elaborato istantaneamente lì dove risiede, dal neurone locale.

Questo elimina alla radice il **Memory Wall**: non spostiamo i dati verso il processore, portiamo il calcolo dentro i dati. Il risultato? Un sistema massivamente parallelo ed Event-Driven, dove l'energia si consuma solo dove e quando serve davvero (vedi il fulmine), senza clock globale che batte a vuoto.

Per comprendere la rivoluzione di questo schema, analizziamo i tre componenti chiave che sostituiscono la logica classica:

1.  **Spike Encoders (Input):** A sinistra, non abbiamo più dati statici. Gli *encoder* trasformano l'informazione del mondo reale in treni di impulsi temporali (**Spikes**). L'informazione è codificata nel *tempo* di arrivo del segnale.

2.  **Neuron Core "Integrate & Fire" (Il Processore):** Ogni cerchio azzurro è una unità di calcolo autonoma che esegue l'equazione $\mathbf{V(t) = V(t-1) + \text{Input}}$. Il neurone somma gli spike e mantiene il suo stato interno (memoria). Solo quando supera una soglia, "spara" un output. Se non riceve input, dorme (consumo zero).

3.  **Spike Decoders / Readout (L'Output)**: A destra, non otteniamo una risposta statica istantanea. Il Readout Layer funziona accumulando **evidenza nel tempo**. I neuroni di uscita integrano gli spike ricevuti: la decisione (es. "È un gatto") non è un valore binario, ma emerge probabilisticamente basandosi sulla frequenza di sparo (**Rate Coding**) o sul tempo di arrivo del primo impulso (**Time-to-First-Spike**). Vince il neurone che ha accumulato più "energia" o che ha reagito più velocemente nella finestra temporale.



### **Verso la convergenza**
Questi principi suggeriscono direzioni promettenti per l’**AI neuromorfica**.
Algoritmi bio-ispirati potrebbero consentire reti più **scalabili**, **energeticamente efficienti** e **resilienti**, capaci di apprendere in tempo reale senza bisogno di dataset massivi e addestramenti centralizzati. 
Le piattaforme neuromorfiche (Loihi, TrueNorth, SpiNNaker) cercano di simulare, almeno in parte questa complessità: **Memoria co-locata** ovvero sinapsi digitali (memristor) che memorizzano i pesi e integrano la corrente, **Spike event-driven** riduzione drastica del consumo energetico e **Plasticità on-chip** regole STDP implementate in hardware per apprendimento online. Ma nessuna di queste riesce a implementare completamente il calcolo dendritico locale, la super varietà di canali ionici e la plasticità multiscale chimica.

Integrare regole di tipo **hebbiano** e **meccanismi omeostatici** (meccanismi che mantengono stabile l’attività neuronale compensando eccessi o deficit di segnale) potrebbe avvicinare le macchine alla flessibilità e all’adattabilità del cervello umano.


Il segreto dell'efficienza del cervello (quei famosi 20 Watt) risiede proprio qui: nel rifiuto di spostare i dati. Mentre la CPU spende energia per "andare a prendere" le informazioni attraverso l'imbuto, il neurone aspetta che l'informazione arrivi e la elabora sul posto.

Abbiamo visto come il cervello calcola e come evita il traffico. Ma un processore, biologico o digitale, è inutile senza una memoria strutturata. Dove li mette i ricordi? Come impara davvero? <br>
Nella **Parte 2 (2 su 3)** di questo lungo articolo, analizzeremo come il cervello trasformi il "caos" in conoscenza, superando la rigidità della RAM per creare una memoria semantica e associativa.



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