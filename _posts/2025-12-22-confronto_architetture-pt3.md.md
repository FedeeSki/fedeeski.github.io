---
layout: post
title: Confronto tra Architettura Informatica e Biologica (Pt.3)
date: 2025-12-21
categories: [Essay]
tags: [paper ,scientifico, riflessioni] 
---

## **Attention mechanism nei transformer: dalle basi all’evoluzione neuromorfica**

<figure style="margin: 2rem 0; text-align: center;">
  
  <img src="{{ '/assets/imgs/transformer.webp' | relative_url }}" 
       alt="Attention mechanism transformer"
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</figure>

L'Attention Mechanism è un componente architetturale che permette a un modello di deep learning di "concentrarsi" selettivamente su diverse parti dell'input quando produce un output. <br> Per esempio immaginate di leggere una frase lunga e complessa: il vostro cervello non le dà uguale peso, ma si **focalizza** sulle parole chiave per coglierne il significato. L’attention fa esattamente questo.

Nei **Transformer** (il modello introdotto nel paper <a href="https://arxiv.org/abs/1706.03762" target="_blank" >
  <strong>"Attention Is All You Need"</strong>
</a> di Vaswani nel 2017), questo meccanismo non è solo un componente, ma è l'architettura fondamentale che sostituisce le ricorrenze (RNN/LSTM), permettendo un calcolo molto parallelo e una modellazione più efficace delle dipendenze a lunga distanza. <br>

### **Come funziona l’attention SDPA (Scaled Dot-Product Attention)?**

L’idea di base è semplice ma potente. Il modello elabora una sequenza di input (come la frase nell'immagine) scomponendola in unità elementari chiamate token, indicati con ”$\mathbf{t}$” (es. $\mathbf{t_1}$ è "Bill", $\mathbf{t_6}$ è "Theatre"). Per ogni token, l’attention calcola quanto è rilevante rispetto a tutti gli altri token della sequenza.

<figure style="margin: 2rem 0; text-align: center;">
  
  <img src="{{ '/assets/imgs/Vector-Values.webp' | relative_url }}" 
       alt="Vector values"
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</figure>


**1)** **Query**, **Key**, **Value** $\mathbf{(Q, K, V)}$: Ogni token $\mathbf{t}$ (rappresentato dal vettore x) viene proiettato tramite matrici di peso $\mathbf{(W^q , W^k , W^v)}$ in tre spazi diversi:
1. Query (**Q**): rappresenta "cosa sto cercando" per il token corrente.
2. Key (**K**): rappresenta "cosa posso offrire" come etichetta per essere trovato.
3. Value (**V**): rappresenta "l’informazione effettiva" (il contenuto) che verrà trasferita.

**2)** Calcolo dei punteggi ("**Scores**"): Per misurare la "similarità" o "rilevanza", si calcola il prodotto scalare tra le Query e le Keys.
Matematicamente, è necessario trasporre la matrice delle Keys ($\mathbf{K^T}$) affinché le dimensioni siano allineate per il prodotto matriciale (riga per colonna). <br> Questo permette di confrontare simultaneamente ogni Query con tutte le Keys, generando una matrice quadrata di punteggi.
**Punteggi** = $\mathbf{Q \cdot K^T}$.

**3)** **Scalatura e Softmax**: I punteggi vengono prima ridimensionati (divisi per $\mathbf{\sqrt{d_k}}$ ) e poi passati attraverso una funzione Softmax. <br>
La **Softmax** è una funzione matematica che trasforma numeri arbitrari (anche negativi) in una distribuzione di probabilità: schiaccia i valori bassi verso lo **0** ed esalta i valori alti, facendo sì che la somma totale sia esattamente **1**. <br> In pratica, converte i punteggi grezzi in "percentuali di attenzione".

**Attention_Weights** = $\mathbf{softmax( (Q \cdot K^T) / \sqrt{dimensione_K} )}$.

**4)** **Output**: L'output per un dato token è la somma pesata di tutti i Values, pesata dalle percentuali appena calcolate. <br> **Output** = $\mathbf{\text{Attention_Weights} \cdot V}$.

>*In pratica se la parola “**gatto**” ha un **alto peso di attenzione** con la parola “**miagola**”, l’output “**gatto**” **conterrà** una forte componente di **informazione** di “**miagola**”.*


Immaginiamo di processare il **token** “$\mathbf{t_8}$” ("Watch"). La sua **Query** cercherà concetti compatibili. <br> Probabilmente calcolerà un punteggio molto alto (grazie alla Softmax) con il **token** “$\mathbf{t_{11}}$” ("Movie"), perché "guardare" e "film" sono semanticamente legati. <br> Di conseguenza, l'**output** per "Watch" assorbirà gran parte del **Value** di "Movie", arricchendosi del contesto necessario per capire cosa si sta guardando.


### **Il Problema Fondamentale: Attention è "Anti-Neuromorfica"**

L'architettura dei Transformer, sebbene rivoluzionaria, è intrinsecamente poco adatta ai chip neuromorfici per diversi motivi:

**Complessità computazionale**: La complessità computazionale dell'algoritmo Scaled Dot-Product Attention è dominata dalla moltiplicazione delle matrici **Q** (Query) e $\mathbf{K^T}$ (Key trasposta), risultando in una complessità temporale di $\mathbf{O(N^2 \cdot \text{dimensione_modello})}$. <br>
Questa dipendenza quadratica dalla lunghezza della sequenza (**N**) rappresenta il principale **collo di bottiglia** computazionale e di memoria nei modelli Transformer.
La dipendenza quadratica dalla lunghezza della sequenza (**N**) significa che il costo computazionale e la memoria richiesta per memorizzare la matrice dei punteggi di attenzione ([$\mathbf{N \\times N}$]) aumentano drasticamente all'aumentare di (**N**). 


**Softmax come Bottleneck**: La funzione softmax è un'operazione **non-lineare e non-locale**, per calcolare il valore di un singolo elemento, è necessario conoscere tutti gli altri elementi della sequenza (per poi fare la normalizzazione). <br> Questo richiede una comunicazione globale e sincronizzazione, che è costosa e inefficiente su architetture neuromorfiche distribuite e asincrone. 

**Calcolo Denso e operazioni matriciali**: L'operazione $\mathbf{Q \cdot K^T}$ è un calcolo molto denso e con un'alta intensità di memoria. <br>
Richiede l'accesso a tutti gli elementi della sequenza per calcolare tutti i punteggi. Questo va contro il principio neuromorfico dell'elaborazione event-driven, dove solo i neuroni che ricevono uno spike (segnale) si attivano, risparmiando energia.

**Alto Footprint di Memoria**: La matrice dei pesi di attenzione [$\mathbf{N \\times N}$] ha una complessità quadratica $\mathbf{O(n^2)}$. Per sequenze lunghe (es. documenti, video), questa matrice diventa enormemente grande, saturando la memoria on-chip e **limitando** l'efficienza.

>*Riassumendo:  l'attention standard è un algoritmo "**globalmente sincronizzato**" e "**memory-bound**", mentre il calcolo neuromorfico è "**localmente asincrono**" e "**compute-bound**".*

### **Architetture Neuromorfiche per l'Attention: la Prossima Frontiera**

La ricerca sta esplorando modi per "neuromorfizzare" gli Attention mechanism. Ecco gli approcci più promettenti:

#### a) **Spiking Transformer (es. SpikeFormer)**

L'idea è di sostituire gli attivatori continui (ReLU, Softmax, etc.) con neuroni a spiking (SNN, basati su eventi discreti).

Mentre nei Transformer classici il calcolo è "denso" (si moltiplicano matrici piene di numeri), qui gli input $\mathbf{(Q, K, V)}$ vengono codificati in sequenze temporali di spike. <br>
L'attenzione diventa così un'operazione sparsa ed event-driven: il punteggio di attenzione non è il risultato di una moltiplicazione massiva, ma **emerge** dalla **co-attivazione temporale** (quando due neuroni sparano insieme). 

Tuttavia, calcolare una vera Softmax (che richiede la normalizzazione globale sommando tutti gli elementi) è computazionalmente complesso con soli spike locali. <br>
Pertanto, questi modelli approssimano l'attenzione normalizzata utilizzando meccanismi di **inibizione laterale**: i neuroni "competono" tra loro, sopprimendo l'attività dei vicini meno stimolati. Questo processo simula una selezione **Winner-Take-All** (WTA), accettando una lieve perdita di precisione aritmetica in cambio di una drastica riduzione dei calcoli.

**Vantaggi**: Risparmio energetico grazie alla natura event-driven (si consuma energia solo quando c'è uno spike) e alle operazioni di addizione che sostituiscono le moltiplicazioni.

**Sfida**: Il training è complesso (richiede surrogate gradients poiché gli spike non sono differenziabili) e la gestione del compromesso tra la precisione dell'approssimazione e l'efficienza energetica.


#### b) **Memristor & In-Memory Computing per l'Attention**

I Memristor (Memristore in italiano, unione di memoria e resistore ) sono innovativi componenti elettronici che costituiscono il quarto elemento fondamentale dei circuiti, unendo in un unico dispositivo le funzioni di **memoria** e **logica**. La loro resistenza elettrica non è volatile e può essere variata in modo controllato, permettendo al dispositivo di "**ricordare**" la carica elettrica che lo ha attraversato.

##### **L'architettura Crossbar Array**

Per sfruttare al massimo le loro proprietà, i memristor sono organizzati in **Crossbar Array** (matrici a barre incrociate). Si tratta di una griglia bidimensionale in cui i memristor sono posizionati ad ogni intersezione tra righe (Word Lines) e colonne (Bit Lines). Questa struttura è cruciale perché permette una densità di integrazione estremamente elevata e supporta il calcolo parallelo massivo.

<figure style="margin: 2rem 0; text-align: center;">
  
  <img src="{{ '/assets/imgs/crossbar_arrays1.webp' | relative_url }}" 
       alt="Crossbar arrays scheme"
       style="max-width: 80%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</figure>

L'applicazione più promettente di questa tecnologia è l'accelerazione dei carichi di lavoro di AI, in particolare quelli basati su Neural Network e Attention mechanism (tipico dei modelli Transformer come GPT).

1. **Memoria dei Pesi** nelle reti neurali, le matrici dei pesi (come le proiezioni **Q, K, V** usate nel calcolo dell'Attention) rappresentano le sinapsi del modello. Queste matrici vengono memorizzate fisicamente nella crossbar: ogni singolo memristor memorizza un "peso" specifico attraverso il suo stato di resistenza. 

2. **Calcolo In-Memory** (AIMC) Il vantaggio chiave è che la costosa operazione di moltiplicazione matrice-vettore (ad esempio, $\mathbf{Q \cdot K^T}$), che è il cuore del calcolo AI, viene eseguita direttamente nella memoria (calcolo in-memory).  <br>
Questo avviene in modo analogico, sfruttando le leggi fondamentali della fisica: <br>
**Moltiplicazione**: L'operazione è realizzata per **Legge di Ohm** ($\mathbf{I = V \cdot G}$, dove **G** è la conduttanza, l'inverso della resistenza). La tensione **V** (l'input) viene moltiplicata per la conduttanza **G** (il peso memorizzato).  <br>
**Somma**: L'accumulo dei risultati avviene per **Legge di Kirchhoff** sulle correnti (KCL), che stabilisce che le correnti generate si sommano automaticamente lungo le colonne (Bit Lines).Tale calcolo avviene in un **singolo** passo fisico.


**Vantaggi**: Superamento del **Memory-Wall**, questa architettura **elimina** il bottleneck di Von Neumann (o memory-wall), ovvero il collo di bottiglia creato dal continuo spostamento dei dati tra processore e memoria. <br>
Il calcolo più intensivo viene eseguito **In-Memory**, i sistemi memristive offrono un consumo energetico drasticamente inferiore rispetto alle GPU, con stime che raggiungono o superano tre ordini di grandezza (**1000x**) in termini di efficienza per l'operazione fondamentale di moltiplicazione matrice-vettore. <br>
Paper: (<a href="https://www.labs.hpe.com/techreports/2016/HPE-2016-23.pdf" target="_blank" >
  <strong>Dot-Product Engine for Neuromorphic Computing: Programming
1T1M Crossbar to Accelerate Matrix-Vector Multiplication</strong>
</a>) <br>

**Riduzione del Consumo** per LLM: Uno studio su un'architettura memristive per la diffusione di LLM ha mostrato una riduzione significativa del **69%** del consumo energetico e una riduzione di **68x** nel prodotto area-ritardo, rispetto ai moderni sistemi TPU/GPU. <br>
Paper: (<a href="https://www.researchgate.net/publication/340891075_Compute-in-Memory_with_Emerging_Nonvolatile-Memories_Challenges_and_Prospects" target="_blank" >
  <strong>Compute-in-Memory with Emerging Nonvolatile-Memories: Challenges and Prospects</strong>
</a>) <br>



**Sfida**: **Rumore ("drift" della conduttanza) e Precisione.** <br>
Il calcolo analogico è sensibile al rumore elettrico e alla variabilità dei dispositivi. Questo è un **problema critico** perché i Transformer classici richiedono un'alta precisione numerica che l'analogico fatica a garantire.

Per far funzionare il sistema è quindi necessaria la **Quantizzazione** (Quantization-aware training), ovvero una tecnica avanzata di ottimizzazione del modello che prepara una Neural Network per il deployment con una **precisione numerica inferiore**. <br> Tuttavia, questo limite diventa un punto di forza grazie all'abbinamento con le reti a spiking: la robustezza al rumore degli SNN aiuta a compensare la natura imprecisa dell'hardware analogico, rendendo la combinazione sostenibile.

#### c) Event-Driven Attention su hardware come Loihi 2 o SpiNNaker 2

Questi chip sono progettati per eseguire efficientemente reti a spiking. La sfida è **mappare** **l'algoritmo di attention** sul loro **paradigma** di calcolo basato su **eventi**.

Si progetta un circuito neurale a spiking che implementa il comportamento dell'attention. <br>
Ad esempio, popolazioni di neuroni competono tramite meccanismi di inibizione laterale per implementare una forma di "**softmax winner-take-all**". I pesi di attenzione non sono una matrice esplicita, ma sono rappresentati dall'attività dinamica della rete.

**Vantaggio**: **Massima efficienza energetica** su hardware neuromorfico nativo.

**Sfida**: È un **cambio di paradigma radicale**. La progettazione è molto più **ispirata alla biologia** e meno diretta della semplice implementazione di un algoritmo. Richiede una ri-formulazione completa del problema.

<figure style="margin: 2rem 0; text-align: center;">
  
  <img src="{{ '/assets/imgs/hw_neuromorfico.webp' | relative_url }}" 
       alt="Es. hw neuromorfico"
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</figure>

L'immagine illustra il concetto di integrazione su piccola scala di un circuito neurale a spiking completo. <br> Dimostra come un'architettura compatta, che include **neuroni**, **sinapsi** e **input/output** (assoni), venga accoppiata con l'elettronica standard (CPLD, USB) per creare un sistema funzionante di calcolo neuromorfico.

La **densità di integrazione è notevole**, con **256** neuroni e oltre **260.000** sinapsi racchiusi in soli **6mm** quadrati. (Questi dati, numeri sono per uso didattico, non mi riferisco a nessuna Architettura specifica).


Il **singolo** neurone artificiale (come unità funzionale, inclusa la sua memoria sinaptica) occupa uno spazio allocato di circa **23.400 micrometri quadrati**. <br>
Si tenga presente che questa area è **gigantesca** rispetto al singolo transistor (l'elemento base del chip), la cui dimensione sui chip moderni è misurata in nanometri. <br> La dimensione qui riflette la complessità di integrare calcolo e memoria nello stesso punto (architettura non-Von Neumann).

All'interno di un **core neurosinaptico** non c'è una CPU generica. Ogni singolo neurone è un'unità di elaborazione altamente specializzata ottimizzata per eseguire in parallelo la simulazione **Integrate-and-Fire** (sommare gli input, confrontare con la soglia, generare uno spike). <br> Questo porta a un'**enorme efficienza specifica**, a **scapito della generalità**.

**Costo**: Il costo di questi chip è **elevato** non per il materiale, ma per la loro natura di **HW R&D** (ricerca e sviluppo) prodotto in volumi limitati, accessibile solo con collaborazioni. Il vero valore è l'**efficienza energetica** che offrono, riducendo drasticamente il costo operativo a lungo termine (es. in applicazioni Edge AI).


## **Evolutionary algorithms** & **Swarm intelligence**

<figure style="margin: 2rem 0; text-align: center;">
  
  <img src="{{ '/assets/imgs/Gemini_metafora.webp' | relative_url }}" 
       alt="Metafora dei picchi e nebbia, EA"
       style="max-width: 70%; height: auto; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</figure>

Immaginiamo un vasto e complesso **paesaggio di ottimizzazione**, una **topografia di valli** **profonde** (soluzioni sub-ottimali) e **picchi** elevati (soluzioni ottimali). <br> L’obiettivo è trovare il picco più alto, ma la **nebbia** è fitta e non è possibile vedere oltre il nostro naso.

Nell'immagine, questo paesaggio si manifesta in cime rocciose avvolte nella foschia notturna, con la vetta centrale “divina”: **l'Ottimo Globale**.

**L'algoritmo greedy** è rappresentato dalla figura solitaria e scura in primo piano, che, con la sua visione limitata, può solo muoversi verso il miglioramento locale immediato, finendo per restare bloccata sul picco minore che sta scalando (**un massimo locale**).

Al contrario, gli **Algoritmi Evolutivi** (EA) dispiegano un'intera popolazione di soluzioni candidate, visibili come le numerose figure luminose distribuite su tutto il paesaggio. <br>
Questa esplorazione parallela del “**search space**” permette agli EA di superare la “nebbia” della cecità locale, aumentando drasticamente la probabilità che alcuni individui convergano verso la vera **soluzione ottimale**, guidati dai principi di selezione e mutazione.

L'**approccio tradizionale** (algoritmi greedy o basati sul calcolo del gradiente) funziona bene solo se il problema è **convesso** (cioè ha un solo picco). <br>
Nel caso di problemi non convessi (la norma in applicazioni reali), la "nebbia" che rappresenta la cecità locale impedisce di vedere l'Ottimo Globale da lontano, puntando a salire solo sulla collina più vicina (un Massimo Locale). <br>
Basandoci solo sull'informazione locale (un passo avanti), c'è un alto rischio di rimanere intrappolati su un picco sub-ottimale, credendo di aver raggiunto la vetta del mondo, mentre la vera soluzione ottimale è nascosta da qualche parte, oltre la nebbia.

### **Crossover & Mutation (skipping “the fog”)**

Gli operatori genetici permettono di "saltare" da una parte all'altra del paesaggio senza seguire il percorso graduale.

* Il **Crossover** combina informazioni da due picchi diversi, creando un figlio che potrebbe trovarsi in una regione totalmente nuova e migliore.

* La **Mutazione** agisce come una spinta casuale che fa cadere un individuo giù da un massimo locale in cui si era bloccato, permettendogli di ricominciare a salire su una nuova e più promettente collina.

In sintesi, la "nebbia" stabilisce la posta in gioco (stakes) del problema: è un ambiente di ricerca complesso, in cui l'obiettivo degli EA è quello di implementare una strategia di ricerca **stocastica e robusta** in grado di navigare e, infine, "**dissipare la nebbia**" attorno al **vero** **ottimo globale**.

### **Genetic Algorithm nell’informatica & Neuromorphic computing**

<figure style="margin: 2rem 0; text-align: center;">
  
  <img src="{{ '/assets/imgs/Ackley.gif' | relative_url }}" 
       alt="Differential Evolution"
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <figcaption style="font-style: italic; font-size: 1em; color: #555; margin-top: 10px; line-height: 1.4;">
    <strong>Differential Evolution</strong><br>
  </figcaption>
</figure>

I GA sono la forma più nota di EA e seguono un ciclo evolutivo ben definito :

* **Rappresentazione**: Ogni soluzione è codificata come un "**cromosoma**" (solitamente una stringa binaria o di numeri reali).

* **Fitness**: Una funzione di **fitness** valuta quanto è "buona" una soluzione per il problema in esame.

* **Selezione**: I cromosomi con maggiore fitness vengono scelti per la riproduzione, mimando la "survival of the fittest".

* **Crossover e Mutazione**: (descritti nel paragrafo sopra).

I GA eccellono nella risoluzione di problemi **NP-hard** e in scenari dove lo spazio di ricerca è molto vasto e la funzione di fitness è complessa o non differenziabile. Per questo sono strumenti ideali per l'ottimizzazione combinatoria, che richiede di trovare la migliore sequenza o combinazione (il 'cromosoma') in un ampio spazio di soluzioni discrete. 

Alcuni esempi di problemi NP-hard dove i GA sono molto utili:

**Travelling Salesman Problem (TSP)**: Trovare il percorso più breve che visita una serie di città e ritorna al punto di partenza. La difficoltà risiede nella ricerca della migliore permutazione delle città. Nei GA, il cromosoma è tipicamente codificato come una sequenza ordinata di indici delle città.

**Knapsack Problem** (Problema dello Zaino): Decidere quali oggetti inserire in uno zaino per massimizzare il valore totale senza superare un limite di peso. Nei GA, la soluzione è rappresentata da un vettore binario (il cromosoma), dove ogni posizione corrisponde a un oggetto, e il valore '1' indica l'inclusione dell'oggetto e '0' la sua esclusione.

Per comprendere appieno come gli Algoritmi Evolutivi possano offrire soluzioni ottimali per le SNN e le architetture neuromorfiche, è opportuno un preambolo sulla Swarm Intelligence.

### Swarm Intelligence (SI)

<style>
  .image-container {
    display: flex;
    flex-direction: column; /* Default per mobile: una sotto l'altra */
    gap: 20px;
    justify-content: center;
    align-items: center;
    margin: 2rem 0;
  }

  .image-wrapper {
    width: 80%; /* Su mobile prendono tutta la larghezza */
  }

  .responsive-img {
    width: 100%;
    height: auto;
    border: 1px solid #000000ff;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    display: block;
  }

  /* Quando lo schermo è più grande di 768px (PC/Tablet) */
  @media (min-width: 768px) {
    .image-container {
      flex-direction: row; /* Su PC: una di fianco all'altra */
      align-items: flex-start;
    }
    .image-wrapper {
      flex: 1;
      max-width: 50%; /* Per sicurezza lasciamo un piccolo margine */
    }
  }
</style>

<figure>
  <div class="image-container">
    <div class="image-wrapper">
      <img src="{{ '/assets/imgs/si_birds.webp' | relative_url }}" 
           alt="Ackley Function" 
           class="responsive-img">
    </div>
    <div class="image-wrapper">
      <img src="{{ '/assets/imgs/si_ants.webp' | relative_url }}" 
           alt="Second Function" 
           class="responsive-img">
    </div>
  </div>
</figure>

La Swarm Intelligence (**SI**) è una filosofia di calcolo che si ispira al comportamento collettivo **decentralizzato** degli insetti sociali (come formiche, api) o di altri gruppi animali (stormi di uccelli, banchi di pesci).
In breve:
Lo sciame è composto da una miriade di **agenti individuali** che seguono regole di comportamento estremamente semplici e locali.

**Interazione Locale**: Gli agenti interagiscono solo con i loro vicini immediati o con l'ambiente circostante (ad esempio, depositando o sentendo i feromoni). <br>
**Comportamento Emergente**: Dalle interazioni locali non coordinate sorge un comportamento globale complesso e coerente, che risolve problemi come la ricerca del cibo o la costruzione di nidi.

>Il risultato è un sistema **autorganizzato** e **decentralizzato** che presenta un'elevata robustezza e scalabilità.

### **Implicazioni nel Neuromorphic Computing (NC)**

La somiglianza tra SI e NC è strutturale e profonda:

* **Decentralizzazione**: Il cervello non ha un processore centrale (CPU) che orchestra tutto. La cognizione è il risultato dell'interazione distribuita di miliardi di neuroni. Questo rispecchia perfettamente la struttura degli algoritmi di SI, dove non esiste un'entità di controllo centrale.

* **Elaborazione Locale**: Nel cervello, ogni neurone esegue operazioni semplici (somma segnali, decisioni binarie di firing). Similmente, in SI, ogni agente esegue semplici regole locali (muoversi verso il vicino migliore).

* **Emergenza**: Sia la coscienza nel cervello che la soluzione ottimale nello sciame sono **proprietà emergenti** che non possono essere attribuite a nessuna singola unità.

Ora per dire l’ultima cosa della quale vorrei parlare bisogna fondere tutto quello della quale abbiamo parlato…

#### **“Spiking Transformer” Evolutivo e Ibrido**

Per spiegare questo concetto, adattiamo il Transformer al linguaggio biologico (SNN), utilizzando l’Evolution (GA) e lo Swarm (SI) non come semplici sostituti della Backpropagation, ma come "Architetti" e "Ottimizzatori globali".

#### La Sinfonia **GA + SI + Surrogate Gradients**

Questa è una **visione teorica** o un'architettura "allo stato dell'arte della ricerca", non uno standard consolidato. Sarebbe l'approccio ibrido ideale verso cui tendiamo.

La Backpropagation classica non funziona direttamente sugli spike (eventi discreti on/off). Tuttavia, affidare l'intero addestramento di miliardi di pesi solo a GA e SI sarebbe **computazionalmente proibitivo** (problema della dimensionalità). <br>
L'approccio vincente è ibrido: usiamo i Surrogate Gradients (che approssimano la derivata degli spike) per l'addestramento massivo dei pesi, mentre GA e SI risolvono i problemi strutturali e di configurazione che il gradiente non può affrontare.

##### **Genetic Algorithm (L'Architetto Topologico)**

Il GA viene usato per la Neural Architecture Search (NAS), ovvero per progettare la "forma" della rete:

* **Codifica**: Il DNA digitale definisce quanti neuroni usare, la densità delle sinapsi e i ritardi assonali.

* **Fitness Function**: Premia l'accuratezza, ma penalizza i consumi. Cerca la massima efficienza energetica (less spike = less energy).

Si ottiene infine una “topologia di rete ottimizzata”, eliminando a monte le connessioni inutili tramite il "pruning evolutivo" (potatura), rendendo la rete sparsa e leggera prima ancora di iniziare l'addestramento profondo.

##### **Swarm Intelligence (Ottimizzazione degli Iperparametri)**

Mentre i Surrogate Gradients aggiustano i pesi sinaptici, la Swarm Intelligence (es. PSO) lavora a un livello superiore o di rifinitura (fine-tuning):

* **Il ruolo dello swarm**: Invece di cercare miliardi di pesi singoli, le particelle cercano la combinazione ottimale di iperparametri globali (es. la soglia di voltaggio per lo spike, le costanti di tempo di decadimento dei neuroni).

Questi parametri sono cruciali per la stabilità degli SNN e sono difficili da impostare col solo gradiente. La SI, non richiedendo derivate, esplora lo spazio di ricerca in modo robusto, evitando che la rete si blocchi in minimi locali (soluzioni sub-ottimali).

---

#### **Un'Allegoria della Mente: “Teatro Emergente”**

Immaginiamo la mente non come una macchina programmata, ma come un vasto palcoscenico immerso in un buio profondo, governato da una economia termodinamica. 

Questo teatro, il nostro SNN, rifiuta lo spreco di un’illuminazione costante e artificiale; qui la realtà esiste solo nell'istante in cui accade. Il buio rappresenta la sparsità, il silenzio necessario affinché l’informazione abbia valore: le luci si accendono solo per la frazione di un millisecondo, in lampi discreti che squarciano l'oscurità solo dove un attore sta agendo, rispecchiando la natura frammentata e fisica dell'impulso neurale.

Dietro le quinte di questo teatro agisce una forza, l’Algoritmo Genetico, che incarna la **Filogenesi** e il tempo dell'evoluzione. A questa entità non interessa il successo di una singola battuta, ma la sopravvivenza della “compagnia”. Essa lavora come un architetto silenzioso che, generazione dopo generazione, scolpisce la struttura stessa del teatro e seleziona i vincoli biologici degli attori, scartando le architetture fragili per consegnare al presente un hardware capace di sostenere la complessità.

Una volta che il sipario si alza, entra in gioco la Swarm Intelligence, che rappresenta l'**Ontogenesi** e l'adattamento rapido dell'individuo. Qui assistiamo alla "morte del regista": non esiste alcuna voce divina, nessuna Backpropagation che urla ordini dall'alto conoscendo già il finale dell'opera. Gli attori-neuroni sono ciechi al disegno globale; sanno solo che devono trovare un’armonia immediata con chi sta loro accanto. <br>
L'intelligenza, dunque, non viene calata dall'alto, ma emerge dal basso attraverso l'autorganizzazione: è uno sciame di pensieri che, muovendosi tra i vincoli strutturali imposti dall'evoluzione e i lampi di luce dell'esperienza presente, improvvisa una performance coerente, trasformando il caos locale in ordine globale.



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