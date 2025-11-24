---
layout: post
title: Comparison Between Computer and Biological Architectures (Pt.1)
date: 2024-11-24
categories: [Essay]
tags: [paper ,scientific, reflections] 
---

<div style="text-align: right; margin-bottom: 20px;">
  <a href="{% post_url 2025-11-24-confronto_architetture-pt1 %}" style="
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
    🇮🇹 <strong>Leggi in Italiano</strong>
  </a>
</div>


## **Motivation: Why Compare Computer and Biological Architectures**

[PC reading recommended] <br>

The evolution of modern computing is at a crucial turning point. As Moore’s Law slows down and the physical limits of silicon approach, the technology industry is searching for new computational paradigms capable of overcoming the traditional constraints of digital processing. <br>
In parallel, our understanding of the neural mechanisms underlying human cognition has reached unprecedented levels of detail, revealing principles of information processing radically different from **Von Neumann** architectures.

<div id="grafico-moore" style="width: 100%; max-width: 900px; margin: 0 auto; overflow-x: auto;">
  </div>
<script>
  
  // Questa è la funzione che useremo
  function drawMooreChart() {
    // Il percorso del file JSON (che ora sappiamo essere corretto)
    var spec = "https://raw.githubusercontent.com/FedeeSki/fedeeski.github.io/refs/heads/main/assets/json/moore_law_divergence.json";
    var embedOptions = {
      "mode": "vega-lite",
      "width": "container",
      "height": 450,
      "actions": false
    };

    // Chiama vegaEmbed sull'ID del div
    vegaEmbed('#grafico-moore', spec, embedOptions)
      .catch(console.error); // Invia eventuali errori alla console
  }

  // Esegui quando il DOM è pronto
  document.addEventListener('DOMContentLoaded', drawMooreChart);

</script>

<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>


The human brain, with its approximately 86 billion neurons and 100 trillion synapses, represents the most sophisticated information-processing system known. It consumes only about 20 watts (less than a light bulb), yet it surpasses the most powerful computers in tasks such as pattern recognition, adaptive learning, and contextual reasoning. This extraordinary efficiency derives from fundamentally different architectural principles: massively parallel processing, distributed memory, adaptive plasticity, and tight integration between storage and computation.

Conversely, modern computer systems have achieved remarkable computational performance through the optimization of sequential architectures, rigid memory hierarchies, and deterministic algorithms. However, these strengths become limitations when adaptability, energy efficiency, and robustness are required—domains in which biological systems naturally excel.

A systematic comparison between these two paradigms is not merely academic. The technology industry is already investing billions of dollars in **neuromorphic** hardware (Intel Loihi, IBM TrueNorth) and **bio-inspired algorithms** (neural networks, evolutionary computing). Understanding the foundational principles governing both domains is essential to guide the next evolutionary leap in computing.

This comparison is particularly relevant in the context of contemporary Artificial Intelligence. While LLMs achieve increasingly sophisticated capabilities, fundamental questions remain about their internal mechanisms and their proximity to biological cognitive processes. Comparative analysis of system architectures can provide critical insight for more efficient AI.

From an engineering perspective, this study aims to identify transferable principles capable of informing the design of embedded, real-time, and safety-critical systems—areas where energy efficiency, adaptability, and fault tolerance are essential requirements. Aerospace and defense industries, for example, increasingly demand systems that combine high computational performance with biologically inspired characteristics: continuous learning, fault robustness, and operation in uncertain environments.

This work therefore aims to build a bridge between computational neuroscience and systems engineering.

To concretely understand the differences between these two worlds, it is useful to examine their foundational architectures: the classic **Von Neumann** model, which has guided computing for more than 70 years.

## **The Classical Paradigm: Von Neumann**

<figure style="margin: 2rem 0; text-align: center;">
  
  <img src="{{ '/assets/imgs/Disegno1VN.svg' | relative_url }}" 
       alt="Diagram of Classical Von Neumann Architecture with CPU, RAM and BUS"
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  
</figure>

Here is how we imagine a computer in theory: a clean and modular system. The CPU acts as the brain, dividing work between the Control Unit (which directs the flow) and the ALU (which performs calculations). RAM serves as an orderly warehouse. Data travels between RAM and CPU through the **System Bus**, a digital highway that on paper seems free and smooth. This geometric separation enabled the digital revolution, but it hides an invisible energy cost that we will soon explore.

#### **Physical Reality: The Memory Wall**

<figure style="margin: 2rem 0; text-align: center;">
  
  <img src="{{ '/assets/imgs/Disegno2VN.svg' | relative_url }}" 
       alt="Von Neumann bottleneck scheme"
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  
</figure>

Here the elegance collapses. The CPU runs at extremely high frequencies (GHz), but is forced to drastically slow down because the Bus acts as a bottleneck. Data piles up when leaving RAM, creating a traffic jam that leaves the processor in a state of **Data Starvation**. The CPU does not only consume energy when computing—energy is wasted during **memory stall cycles**, forced into inactivity while waiting for data to pass through this narrow gateway.  
This is the well-known **Von Neumann Bottleneck**.


### **The Biological Unit: Beyond the Simple “Perceptron”**

Accustomed to ANN models, we tend to think of a neuron as something as simple as a perceptron (weighted sum + activation function). In reality, the *biological neuron* is a much richer and more complex system. <br>

**Dendrites** are not simple input wires or an “I/O system” that merely forwards signals positively to the soma. They are structures that perform local operations and spatial-temporal integration. <br>

* They contain **voltage-gated ion channels** that can amplify or attenuate passing signals (using nonlinear differential equations, producing chaotic/oscillatory behavior).
* They generate local **dendritic action potentials** that propagate both toward the soma and laterally (**Backpropagating Action Potentials** (bAP)), jumping between branches through dense arborization. These dendritic potentials may even spread from one branch to a “sibling” branch emerging at the same bifurcation, enabling **cross-communication** between inputs arriving on adjacent dendritic regions.
* **Dendro-dendritic gap junctions**: Some direct electrical connections allow current to pass between dendrites of neighboring neurons without neurotransmitters.

In simplified terms, this lateral transmission enables: **local synchronization**, **cross-modal integration**, **signal amplification**, and **local modulation**, permitting **fine-tuning** without involving broader circuits. <br>

<figure style="margin: 2rem 0; text-align: center;">
  
  <img src="{{ '/assets/imgs/ANN.svg' | relative_url }}" 
       alt="Artificial Neuron Model (Perceptron)"
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
       
  <figcaption style="font-style: italic; font-size: 0.9em; color: #555; margin-top: 10px; line-height: 1.4;">
    <strong>The Artificial Neuron Model (Perceptron).</strong><br>
  </figcaption>
  
</figure>

The image illustrates the mathematical abstraction underlying ANNs. The process is a sequential flow:

* **Weighted Inputs** ($\mathbf{x \cdot w}$): Incoming data ($\mathbf{x}$) are multiplied by weights ($\mathbf{w}$), determining their relative importance.
* **Integration** ($\mathbf{\Sigma}$): Weighted signals are algebraically summed into a single central node (hence “Point Neuron”). All spatial complexity is reduced to a scalar value.
* **Activation** (Non-linearity): The sum passes through a function (right-hand plot, e.g., Sigmoid) which determines output intensity.

<br>

<figure style="margin: 2rem 0; text-align: center;">
  <img src="{{ '/assets/imgs/SNN_bio.svg' | relative_url }}" 
       alt="Comparison between Artificial Neuron (Point Neuron) and Biological Neuron (Dendritic Computation)"
       style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <figcaption style="font-style: italic; font-size: 0.9em; color: #555; margin-top: 10px; line-height: 1.4;">
    <strong>Diagram of a biological neural network (Multi-compartment model).</strong><br>
  </figcaption>
</figure>

Unlike an artificial neuron, here computation is not concentrated in a single point, but distributed across space and time:

* **Synaptic Inputs** (Excitatory/Inhibitory): Signals are not abstract numbers, but spikes from other neurons (small green circles). Note the key detail: some inputs excite (arrows), others inhibit (T-shaped bars), actively blocking signals.
* **Active Dendrites** (The real processor): Branches are not passive wires. Each bifurcation is an independent computational unit that filters, sums, or blocks signals before they reach the soma. Highlighted in red: *“Computation happens here, not only in the soma!”*
* **Integration** (Spike Decision): The soma receives the results of all local computations and makes a complex temporal decision about firing.
* **Output** (Axon): When threshold is exceeded, the neuron fires an output spike (orange lightning) to others.

#### **Local Synchronization**

This extremely fast and local form of computation **contrasts strongly** with communication between **independent computer processes (IPC)**.

When two processes that do not share memory must communicate, they cannot use L1 cache. They must request OS-mediated mechanisms such as:

* **Shared Memory**
* **Message Passing**

Both incur **high latency**, **OS overhead**, and require synchronization primitives like **semaphores**, adding delay and complexity.

>*“In neurons, computation is highly parallel and local: dendritic compartments integrate inputs almost instantaneously, much like processor threads sharing the ultra-fast L1 cache.”*

<br>

#### **Fine Tuning**

Fine Tuning in ANN is **global**:

```python
# The entire gradient must propagate across the WHOLE network 
for layer in network: 
    layer.weights += learning_rate * global_gradient[layer]
```

**Global Backpropagation**: each weight depends on the final loss and requires a full **forward + backward pass**, computationally expensive: **O(n)** parameters.  
**Lock-step learning**: the entire network must freeze for updates.

For dendrites, Fine Tuning is **ultralocal**:

```c
// Biological pseudocode
if (pre_synaptic_activity && post_synaptic_activity){
      strengthen_synapse_locally();  // Only this synapse!
}

if (pre_synaptic_activity && NO_post_synaptic_activity){
      weaken_synapse_locally();
}
```

This touches the core of the **Credit Assignment Problem**.  
**Backpropagation** solves it exactly but is **biologically implausible**.  
The brain instead uses a **local temporal-correlation heuristic (STDP)**, far faster and more efficient.

---

### **Hebbian Plasticity: “Neurons that fire together, wire together”**

The **Hebbian rule** is the paradigm of **local plasticity**. Each synapse autonomously decides whether to strengthen or weaken based solely on local pre- and post-synaptic activity.  
If two neurons fire nearly simultaneously, their connection strengthens.

A crucial extension is **spike-timing-dependent plasticity (STDP)**:  
If the presynaptic neuron fires slightly **before** the postsynaptic one (≈ 20 ms), the synapse is potentiated (**LTP**).  
If it fires **after**, it is weakened (**LTD**).

<figure style="margin: 2rem 0; text-align: center;">
  <img src="{{ '/assets/imgs/STDP.svg' | relative_url }}" 
       alt="Spike-Timing Dependent Plasticity (STDP) Graph"
       style="max-width: 80%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
  <figcaption style="font-style: italic; font-size: 0.9em; color: #555; margin-top: 10px; line-height: 1.4;">
    <strong>The Time Rule (STDP).</strong><br>
  </figcaption>
</figure>

---

### **Homeostatic Balance**

Alongside Hebbian strengthening, each dendrite maintains a target activation level.  
**Homeostatic plasticity** stabilizes excitability to prevent runaway activation, ensuring long-term stability without global supervision.

---

## **The Distributed Architecture: The Ordered Chaos of Neurons**

<figure style="margin: 2rem 0; text-align: center;">

<img src="{{ '/assets/imgs/DisegnoSNN.svg' | relative_url }}" 
     alt="Neuromorphic Architecture Diagram" 
     style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">

</figure>

In the biological (and neuromorphic) paradigm, the tyranny of the **System Bus** is abolished.

There is **no central controller**. Instead of a single congested highway, we have an **asynchronous mesh network (NoC)**.  
The radical change is **co-location**: memory is no longer stored externally (RAM) but **embedded within the connections themselves** (synaptic weights). When a spike arrives, it is processed instantly where the data already resides.

This eliminates the **Memory Wall** at its root: **computation moves to the data**.  
The result is **massively parallel**, **event-driven** processing, consuming energy only **where and when** needed—no wasteful global clock.

To understand this revolution, consider the three key replacements for classical logic:

* **Spike Encoders (Input)** — real-world signals become spike trains; information lies in timing.
* **Neuron Core "Integrate & Fire"** — autonomous units retaining state and firing only on demand.
* **Spike Decoders / Readout** — decisions emerge probabilistically through temporal accumulation (**Rate Coding** / **Time-to-First-Spike**).

---

## **Toward Convergence**

These principles suggest promising directions for **neuromorphic AI**:  
More **scalable**, **energy-efficient**, and **resilient** systems capable of online learning without massive datasets or centralized training.

Neuromorphic platforms (**Loihi**, **TrueNorth**, **SpiNNaker**) attempt to approximate this complexity:

* **Co-located memory** (digital synapses / memristors)
* **Event-driven spikes**
* **On-chip plasticity** (hardware STDP)

Yet none fully implement rich dendritic computation, ion-channel diversity, or biochemical multi-scale plasticity.

Integrating **Hebbian-style rules** and **homeostatic mechanisms** could move machines closer to the flexibility and adaptability of the human brain.

The secret of brain efficiency (those famous **20 watts**) lies here:  
Computers spend energy **fetching** data, whereas neurons **wait** for data to arrive and process it **locally**.

We have seen how the brain computes and how it avoids traffic congestion.  
But a processor—biological or digital—is useless without structured memory. Where does the brain store memories? How does it truly learn? <br>
In **Part 2 (of 3)** of this extended article, we will analyze how the brain transforms *chaos* into knowledge, surpassing the rigidity of RAM to form **semantic and associative memory**.

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
