---
layout: cayman
title: Hiding Beats Finding
description: "Claim: Finding grows dramatically more difficult than hiding as complexity increases."
---
RENAME: Hiding_Beats_Finding 

**TL;DR.**  Within a simple system, injecting a behavior in a way that cannot easily be found is virtually impossible.  As complexity increases, however, this tendency reverses itself such that it becomes relatively easy to inject behaviors into a system that become virtually impossible to find.  This has implications for the safety and comprehensibility of AI systems as they grow in complexity.


This claim is clear enough in the abstract. Yet, architects of complex systems may sometimes feel they have constructed their particular system in ways that afford specific properties and guarantees, which makes hiding difficult even for very complex systems. Here, we offer an example of one such attempt to show that these attempts will fail, and they generally will fail in ways that are impossible to see a priori.


- Among the many behaviors of this AI, it regularly uses synthesized video in its interaction with users.

- Our AI agent has an overriding constitutionally-based motivational system that strives to maintain its integrity from attack/subversion.  Each version of its own design begins with this integrity goal as the bedrock of its architecture.
- Of course any actions involving its crypto money must be safe guarded extremely well as this is an obvious area for external exploitation:  (1) only known and trusted code is used.  (2) all relevant processing is sandboxed within itself, and the sandboxing code is among the most throughly tested code. (3) even after all of



SO HERE IS THE NEEDLE IN THE HAY STACK

DITHERING - For added realism and texture the video synthesizer use a simple randomized dithering in a algorithm pervasively.  Uses randomized scratch pad as a colorable source of randomness for this.  It turns out given enough video its easy to reconstruct the random pad (no reason)



COMPARING FINDING TO HIDING
- IN MATH - Obviously, identifying a single class of inputs exploitable inputs for an encryption scheme is much easier than identifying ALL exploitable classes to ensure you will catch all cases of hiding.  
- ACROSS MULTIPLE COMPONENTS - As the number of interacting components increases, scanning for malicious outcomes from all possible combinations of components grows much faster than the complexity of designing a single malicious combination.
- WITHIN TRAINED SYSTEMS - The generated text template used a scaffolding for info provided in the body of the encrypted text
