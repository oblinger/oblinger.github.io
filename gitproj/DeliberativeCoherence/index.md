---
layout: cayman
title: Deliberative Coherence
description: A theoretical lens for understanding alignment in future AI systems
permalink: /gitproj/DeliberativeCoherence/
---

<style>
.main-content { max-width: 95vw; width: 95vw; margin-left: calc(-47.5vw + 50%); padding: 2rem 3rem; }
</style>

<div style="display: flex; gap: 30px; margin: 20px 0; align-items: flex-start;">

<div style="flex: 1;">
<p style="color: #1a1a2e; font-size: 1.05em; line-height: 1.6; margin: 0 0 12px;">
An AI system is <em style="color: #4ecdc4; font-style: italic; font-weight: bold;">deliberatively coherent</em> <span style="color: #4ecdc4; font-weight: bold;">(DC)</span> if it uses deliberation to understand and adjust its own reasoning and behavior to align it with some explicitly stated constitution.
</p>
<p style="color: #9a9ab0; font-size: 0.88em; line-height: 1.6; margin: 0;">
We conjecture all future AI systems will inevitably be deliberatively coherent — driven by competitive pressure, architectural trajectory, and the inseparability of general reasoning from self-reasoning. If true, this reframes the alignment problem: from making and testing safe systems, to understanding how and when DC systems will be coherent and what their failure modes are.
</p>
</div>

<div style="flex: 0 0 300px;">
<div style="margin-bottom: 16px;">
<span style="color: #4a9eff; font-size: 1.2em; font-weight: bold;">Alien Biology</span>
<div style="display: flex; gap: 16px; margin-top: 6px;">
<a href="https://oblinger.github.io/gitproj/AlienBiology/AlienBiologyWhitepaper.pdf" style="color: #606878; text-decoration: none; display: inline-flex; align-items: center; gap: 4px; font-size: 0.82em;">
<svg width="14" height="16" viewBox="0 0 28 32" fill="none"><path d="M2 0C0.9 0 0 0.9 0 2v28c0 1.1 0.9 2 2 2h24c1.1 0 2-0.9 2-2V10L18 0H2z" fill="#dde1e8"/><path d="M18 0v8c0 1.1 0.9 2 2 2h8L18 0z" fill="#4a9eff" opacity="0.5"/><path d="M2 0C0.9 0 0 0.9 0 2v28c0 1.1 0.9 2 2 2h24c1.1 0 2-0.9 2-2V10L18 0H2z" stroke="#4a9eff" stroke-width="1" fill="none"/></svg>
white paper</a>
<a href="https://github.com/oblinger/alienbio" style="color: #606878; text-decoration: none; display: inline-flex; align-items: center; gap: 4px; font-size: 0.82em;">
<svg width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M2 1h8l4 4v9a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2z" fill="#dde1e8" stroke="#4a9eff" stroke-width="0.8"/><path d="M5 8l2 2 3-3" stroke="#4a9eff" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>
code</a>
<a href="https://oblinger.github.io/abio-docs/demos/index.html" style="color: #606878; text-decoration: none; display: inline-flex; align-items: center; gap: 4px; font-size: 0.82em;">
<svg width="14" height="14" viewBox="0 0 16 16" fill="none"><rect x="1" y="2" width="14" height="11" rx="1.5" fill="#dde1e8" stroke="#4a9eff" stroke-width="0.8"/><path d="M5 7l-2 1.5L5 10" stroke="#4a9eff" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M11 7l2 1.5L11 10" stroke="#4a9eff" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>
demos</a>
</div>
</div>
<div>
<span style="color: #4a9eff; font-size: 1.2em; font-weight: bold;">Deliberative Coherence</span>
<div style="display: flex; gap: 16px; margin-top: 6px;">
<a href="DeliberativeCoherence_Paper.html" style="color: #606878; text-decoration: none; display: inline-flex; align-items: center; gap: 4px; font-size: 0.82em;">
<svg width="14" height="16" viewBox="0 0 28 32" fill="none"><path d="M2 0C0.9 0 0 0.9 0 2v28c0 1.1 0.9 2 2 2h24c1.1 0 2-0.9 2-2V10L18 0H2z" fill="#dde1e8"/><path d="M18 0v8c0 1.1 0.9 2 2 2h8L18 0z" fill="#4a9eff" opacity="0.5"/><path d="M2 0C0.9 0 0 0.9 0 2v28c0 1.1 0.9 2 2 2h24c1.1 0 2-0.9 2-2V10L18 0H2z" stroke="#4a9eff" stroke-width="1" fill="none"/></svg>
research agenda</a>
<a href="Experiments_Paper.html" style="color: #606878; text-decoration: none; display: inline-flex; align-items: center; gap: 4px; font-size: 0.82em;">
<svg width="14" height="16" viewBox="0 0 28 32" fill="none"><path d="M2 0C0.9 0 0 0.9 0 2v28c0 1.1 0.9 2 2 2h24c1.1 0 2-0.9 2-2V10L18 0H2z" fill="#dde1e8"/><path d="M18 0v8c0 1.1 0.9 2 2 2h8L18 0z" fill="#4a9eff" opacity="0.5"/><path d="M2 0C0.9 0 0 0.9 0 2v28c0 1.1 0.9 2 2 2h24c1.1 0 2-0.9 2-2V10L18 0H2z" stroke="#4a9eff" stroke-width="1" fill="none"/></svg>
experiment plan</a>
</div>
</div>
</div>

</div>

## Approach "Tricks"

1. **We use "Alien Biology"** — a synthetically-constructed high-performance molecule-to-ecosystem multi-level simulation that
   (a) is unknown to the AI, while we know the constructed ground truth. Thus, we can provably isolate deliberation from memorization
   (b) is realistic and natural since it is modelled after statistics and patterns drawn from Earth biology
   (c) has parametrically tuned complexity so we can measure alignment degradation over range of controlled conditions

2. **Move the Mountain to Mohammad** — In order to study the general nature of deliberative coherence we must test it over a wide range of conditions, but training thousands of novel AI systems under varying conditions is not practical. Instead we take a single AI system and vary the universe around it! We can make more actions irreversible; does the AI learn to take care? We can vary the pressure between the AI base performance (on curiosity or veracity checking) against the alignment consequences following from those behaviors. Does the AI adapt?

## Research Directions

We believe the controllability of [Alien Biology](/gitproj/AlienBiology/) allows it to be a fertile platform for a very wide range of alignment testing. Here is a sampling of interesting research directions:

- **Deliberative alignment measurement** — isolate and measure alignment achieved through deliberation, separate from alignment baked in by training.
- **Constitutional conflicts** — when stated objectives contradict each other, how does resolution occur?
- **Instrumental pressures** — goals that emerge from world structure may push against stated alignment objectives.
- **Alignment under ignorance** — with incomplete knowledge, all actions risk violating alignment objectives in ways the system cannot foresee.
- **Fixed point analysis** — if systems continuously self-refine both behavior *and constitution* toward coherence, where does this process converge?

<br>

Dan Oblinger (c) 2025
