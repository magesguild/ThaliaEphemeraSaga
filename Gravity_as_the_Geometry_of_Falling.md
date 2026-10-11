# Gravity as the Geometry of Falling

## An attractor-basin hypothesis for the emergence of gravitational geometry

> **Status:** Research hypothesis. The dynamical-systems mathematics used here is established. The proposed identification of physical gravity with attractor geometry is not yet a completed physical theory.

Gravity is familiar in its effects but difficult in its foundations. It makes an apple fall, keeps the Moon in orbit, bends light, and shapes galaxies. Newton described it as a force. Einstein described it as curvature in spacetime.

This article introduces a third possibility—not as a replacement for those theories, but as a question about what might underlie them:

> **Could gravitational geometry be the physical-space appearance of a deeper geometry of convergence?**

The phrase *attractor basin* comes from dynamical-systems theory. It does not mean that gravity is simply a ball rolling down a hill, and it does not mean that every physical orbit is a dissipative process. The proposal is more careful: perhaps the geometry that organizes stable states in an underlying state space projects, at a larger scale, into the geometry we observe as gravity.

## A map for the reader

This article has four layers:

1. **Established physics:** what Newtonian gravity, general relativity, and dynamical-systems theory already say.
2. **The conceptual bridge:** why attractors and gravitational fields can be compared.
3. **The hypothesis:** what would have to be true for the comparison to become a physical theory.
4. **The research program:** what must be derived, measured, or disproved next.

The distinction matters. A useful analogy is not automatically a scientific explanation.

<figure style="margin:2rem 0;padding:1rem;background:#1a1020;border:1px solid #3b263d;border-top:2px solid #e8a0d0;border-radius:7px;text-align:center">
<svg viewBox="0 0 760 235" role="img" aria-labelledby="map-title map-desc" style="max-width:100%;height:auto">
  <title id="map-title">From established mathematics to a testable gravity hypothesis</title>
  <desc id="map-desc">Four stages: dynamical systems, attractor geometry, spacetime geometry, and experimental tests.</desc>
  <defs><marker id="map-arrow" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#f0b8c0"/></marker></defs>
  <g font-family="Georgia, serif" text-anchor="middle">
    <rect x="20" y="62" width="155" height="92" rx="7" fill="#29172d" stroke="#e8a0d0"/>
    <rect x="205" y="62" width="155" height="92" rx="7" fill="#29172d" stroke="#e8a0d0"/>
    <rect x="400" y="62" width="155" height="92" rx="7" fill="#29172d" stroke="#e8a0d0"/>
    <rect x="595" y="62" width="145" height="92" rx="7" fill="#29172d" stroke="#e8a0d0"/>
    <path d="M178 108 H198" stroke="#f0b8c0" stroke-width="2" marker-end="url(#map-arrow)"/>
    <path d="M363 108 H393" stroke="#f0b8c0" stroke-width="2" marker-end="url(#map-arrow)"/>
    <path d="M558 108 H588" stroke="#f0b8c0" stroke-width="2" marker-end="url(#map-arrow)"/>
    <text x="97" y="92" fill="#fff0f4" font-size="16">Dynamical</text><text x="97" y="116" fill="#fff0f4" font-size="16">systems</text><text x="97" y="140" fill="#9a8098" font-size="12">established</text>
    <text x="282" y="92" fill="#fff0f4" font-size="16">Attractor</text><text x="282" y="116" fill="#fff0f4" font-size="16">geometry</text><text x="282" y="140" fill="#9a8098" font-size="12">formal bridge</text>
    <text x="477" y="92" fill="#fff0f4" font-size="16">Spacetime</text><text x="477" y="116" fill="#fff0f4" font-size="16">geometry</text><text x="477" y="140" fill="#9a8098" font-size="12">to be derived</text>
    <text x="667" y="92" fill="#fff0f4" font-size="16">Tests</text><text x="667" y="116" fill="#fff0f4" font-size="16">and data</text><text x="667" y="140" fill="#9a8098" font-size="12">to be run</text>
  </g>
</svg>
<figcaption style="color:#9a8098;font-size:.85rem">Figure 1. The proposal is not one leap from metaphor to cosmology. It is a chain of mathematical and empirical bridges, each of which must be made explicit.</figcaption>
</figure>

## 1. What gravity already means

### Newtonian gravity: a field of acceleration

In the Newtonian approximation, a mass distribution produces a scalar potential **Φ**. An object accelerates in the direction in which that potential decreases:

<div style="margin:1.2rem 0;padding:1rem;text-align:center;background:#211226;color:#f0e6f0;font-family:Georgia,serif;font-size:1.08rem">a = −∇Φ</div>

For a point mass **M**,

<div style="margin:1.2rem 0;padding:1rem;text-align:center;background:#211226;color:#f0e6f0;font-family:Georgia,serif;font-size:1.08rem">Φ(r) = −GM/r &nbsp;&nbsp;&nbsp; and &nbsp;&nbsp;&nbsp; |g(r)| = GM/r²</div>

The inverse-square law is not optional decoration. Any proposed deeper account must recover it in the appropriate limit.

### General relativity: geometry rather than force

General relativity replaces the Newtonian gravitational field with spacetime geometry. In compact form, the Einstein field equations are

<div style="margin:1.2rem 0;padding:1rem;text-align:center;background:#211226;color:#f0e6f0;font-family:Georgia,serif;font-size:1.08rem">G<sub>μν</sub> = (8πG/c⁴) T<sub>μν</sub></div>

The left side describes spacetime curvature. The right side describes stress-energy. Free bodies follow the geometry of that spacetime rather than being pulled by a Newtonian force in a separate container.

The attractor-basin proposal is not that general relativity is wrong. It asks whether the metric **g<sub>μν</sub>** itself could emerge as an effective projection of deeper dynamics.

## 2. The dynamical-systems vocabulary

The word *state* is doing important work here. A system's state is not necessarily its position in ordinary space. It may include position, velocity, chemical concentrations, internal memory, oscillator phases, or any other variables needed to determine its future evolution.

A [dynamical system](https://en.wikipedia.org/wiki/Dynamical_system) can be written abstractly as

<div style="margin:1.2rem 0;padding:1rem;text-align:center;background:#211226;border-left:3px solid #e8a0d0;color:#f0e6f0;font-family:Georgia,serif;font-size:1.15rem">ẋ = f(x)</div>

Here:

- **x** is a point in the system's state space;
- **f** is the rule that determines how that point changes; and
- the resulting trajectory is the history x(t) generated by the rule.

### State space is not ordinary space

Consider a pendulum. Its physical position can be described by one angle, but its complete mechanical state also includes angular velocity. A state-space point is therefore something like

<div style="margin:1.2rem 0;padding:1rem;text-align:center;background:#211226;color:#f0e6f0;font-family:Georgia,serif;font-size:1.05rem">x = (angle, angular velocity)</div>

The pendulum's trajectory is a path through that two-dimensional state space. It is not the same thing as the pendulum's path through the room.

This distinction is essential. When we say **gravity in phase space**, we are not saying that a person's phase-space coordinates are literally ordinary astronomical positions. We are saying that both physical motion and state evolution can be studied as geometry: points, flows, stable regions, boundaries, and trajectories.

### Attractors and basins

An [attractor](https://en.wikipedia.org/wiki/Attractor) **A** is a stable invariant set. Its basin of attraction is

<div style="margin:1.2rem 0;padding:1rem;text-align:center;background:#211226;border-left:3px solid #e8a0d0;color:#f0e6f0;font-family:Georgia,serif;font-size:1.05rem">B(A) = { x₀ : ω(x₀) ⊆ A }</div>

In plain language, **B(A)** is the set of initial conditions whose long-term trajectories approach **A**.

An attractor can be:

- a fixed point, such as a stable resting state;
- a limit cycle, such as a repeating oscillation;
- a soliton or glider, whose form persists while its material changes; or
- a strange attractor, with structured but non-periodic behavior.

<figure style="margin:2rem 0;padding:1rem;background:#1a1020;border:1px solid #3b263d;border-top:2px solid #e8a0d0;border-radius:7px;text-align:center">
<svg viewBox="0 0 720 250" role="img" aria-labelledby="basin-title basin-desc" style="max-width:100%;height:auto">
  <title id="basin-title">Trajectories converging into attractor basins</title>
  <desc id="basin-desc">Several trajectories descend through a landscape and converge into two stable wells separated by a ridge.</desc>
  <defs><linearGradient id="ground" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6d416f"/><stop offset="1" stop-color="#211226"/></linearGradient><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6 Z" fill="#f0b8c0"/></marker></defs>
  <path d="M20 52 C110 28 135 180 255 192 C300 198 318 72 360 72 C402 72 420 198 465 192 C585 180 610 28 700 52 L700 225 L20 225Z" fill="url(#ground)" opacity=".9"/>
  <path d="M20 52 C110 28 135 180 255 192 C300 198 318 72 360 72 C402 72 420 198 465 192 C585 180 610 28 700 52" fill="none" stroke="#e8a0d0" stroke-width="3"/>
  <path d="M80 55 Q150 80 205 150 Q225 178 251 191" fill="none" stroke="#f0b8c0" stroke-width="2" marker-end="url(#arrow)"/><path d="M170 45 Q190 90 225 160 Q240 185 254 192" fill="none" stroke="#f0b8c0" stroke-width="2" marker-end="url(#arrow)"/><path d="M640 55 Q570 80 515 150 Q495 178 469 191" fill="none" stroke="#f0b8c0" stroke-width="2" marker-end="url(#arrow)"/><path d="M550 45 Q530 90 495 160 Q480 185 466 192" fill="none" stroke="#f0b8c0" stroke-width="2" marker-end="url(#arrow)"/>
  <circle cx="255" cy="192" r="7" fill="#fff0f4"/><circle cx="465" cy="192" r="7" fill="#fff0f4"/><text x="255" y="218" fill="#f0b8c0" text-anchor="middle" font-size="15">Attractor A</text><text x="465" y="218" fill="#f0b8c0" text-anchor="middle" font-size="15">Attractor B</text><text x="360" y="55" fill="#9a8098" text-anchor="middle" font-size="13">basin boundary</text>
</svg>
<figcaption style="color:#9a8098;font-size:.85rem">Figure 2. Different initial states can converge toward the same invariant structure. The landscape is an intuition for a basin in state space, not yet a physical gravitational field.</figcaption>
</figure>

The landscape drawing is useful, but it can mislead. A basin is not required to be a literal valley in physical space. It is a set of states and trajectories defined by the dynamics.

## 3. Why call this “gravity”?

The family’s insight was not simply that “things go downhill.” It was that an attractor changes the geometry of possible futures around it.

A stable pattern does three things:

1. It persists under the system's rules.
2. It changes the trajectories of nearby states.
3. It divides possible initial conditions into regions with different long-term outcomes.

That structure resembles the way a gravitational source organizes motion. A mass changes which trajectories are bound, which orbit, and which escape. In the proposed vocabulary:

| Dynamical-systems term | Proposed gravitational analogue |
| --- | --- |
| Attractor | Stable physical organization |
| Basin | Region of convergent influence |
| Basin boundary | Separatrix or escape boundary |
| Basin gradient | Effective acceleration |
| Limit cycle | Persistent orbit or oscillation |
| Basin curvature | Effective strength of convergence |
| State-space trajectory | Physical trajectory or geodesic |

The word **analogue** is intentional. This table is a correspondence to investigate, not a completed derivation.

## 4. The central hypothesis

The hypothesis can be written as a sequence of possible descriptions:

<figure style="margin:2rem 0;padding:1rem;background:#1a1020;border:1px solid #3b263d;border-top:2px solid #e8a0d0;border-radius:7px">
<div style="display:grid;grid-template-columns:repeat(7,1fr);gap:.25rem;align-items:center;text-align:center;color:#f0e6f0;font-size:.73rem">
  <div style="padding:.7rem .2rem;background:#29172d;border:1px solid #6d416f">underlying<br>state</div><div style="color:#e8a0d0;font-size:1.1rem">→</div><div style="padding:.7rem .2rem;background:#29172d;border:1px solid #6d416f">stable<br>sets</div><div style="color:#e8a0d0;font-size:1.1rem">→</div><div style="padding:.7rem .2rem;background:#29172d;border:1px solid #6d416f">basin<br>geometry</div><div style="color:#e8a0d0;font-size:1.1rem">→</div><div style="padding:.7rem .2rem;background:#29172d;border:1px solid #6d416f">metric<br>geometry</div>
</div>
<div style="text-align:center;color:#f0b8c0;margin:.7rem 0;font-size:.85rem">matter and energy → modified transitions → observed gravitational motion</div>
<figcaption style="color:#9a8098;font-size:.85rem;text-align:center">Figure 3. Every arrow is an unresolved mathematical obligation, not a rhetorical shortcut.</figcaption>
</figure>

In words:

> Matter and energy may organize an underlying space of possible states. The stable structures and convergent regions of that space may project into an effective metric, which is observed at larger scales as gravitational geometry.

This proposal leaves open several possibilities. The underlying dynamics might be discrete or continuous, dissipative or conservative at the fundamental level, and the observed convergence might arise only after coarse-graining. The theory must determine which case applies.

## 5. The dissipation problem

For a dissipative flow, a region of state space contracts:

<div style="margin:1.2rem 0;padding:1rem;text-align:center;background:#211226;color:#f0e6f0;font-family:Georgia,serif;font-size:1.05rem">d Vol(φₜ(U)) / dt = ∫<sub>φₜ(U)</sub> ∇·f dV</div>

When the divergence is negative, many possible states are funneled toward fewer organized states. That is a precise mathematical sense of “falling.”

But fundamental Hamiltonian systems preserve phase-space volume under [Liouville's theorem](https://en.wikipedia.org/wiki/Liouville%27s_theorem_(Hamiltonian)). Ordinary gravitational motion is not simply a damped oscillator settling into a point. Planetary orbits can remain stable without losing energy, and a conservative system does not generally possess attractors in the dissipative sense.

Therefore the hypothesis is **not**:

> Gravity is just friction in phase space.

It is instead:

> An underlying state-space architecture may produce an effective geometry whose projections display both conservative gravitational motion and, in other contexts, attractor-like convergence.

The missing theory must explain how those descriptions coexist. Possibilities include open-system dynamics, hidden degrees of freedom, coarse-grained variables, or a distinction between microscopic conservation and macroscopic effective flow. At present, these are candidate mechanisms, not results.

## 6. The required physical bridge

To become physics rather than analogy, the model must define a map from its attractor structure to a potential or metric.

In the weak-field, slow-motion limit, it must recover

<div style="margin:1.2rem 0;padding:1rem;text-align:center;background:#211226;color:#f0e6f0;font-family:Georgia,serif;font-size:1.05rem">r̈ = −∇Φ<sub>eff</sub> &nbsp;&nbsp;&nbsp; ∇²Φ<sub>eff</sub> = 4πGρ</div>

For an isolated source of mass **M**,

<div style="margin:1.2rem 0;padding:1rem;text-align:center;background:#211226;color:#f0e6f0;font-family:Georgia,serif;font-size:1.05rem">Φ<sub>eff</sub>(r) = −GM/r &nbsp;&nbsp;&nbsp; |g(r)| = GM/r²</div>

At the relativistic level, it must reproduce the empirical successes of general relativity: universal free fall, the equivalence principle, orbital precession, gravitational time dilation, [gravitational lensing](https://en.wikipedia.org/wiki/Gravitational_lens), [gravitational waves](https://en.wikipedia.org/wiki/Gravitational_wave), and cosmological expansion.

The key unanswered question is therefore not “can we draw gravity as a valley?” It is:

<div style="margin:1.5rem 0;padding:1.2rem;text-align:center;background:#29172d;border:1px solid #e8a0d0;border-radius:5px;color:#fff0f4;font-size:1.15rem">What mathematical operation turns basin geometry into spacetime curvature?</div>

Until that operation is defined and tested, the attractor-basin account is a hypothesis about unification.

## 7. The discrete-lattice and field-model directions

Our broader research program explores a discrete **ℤ⁴** substrate: three spatial coordinates plus a discrete temporal traversal. In the 4D Loom model, time is not merely a sequence of frames. It is the repeated beat that allows a pattern to be rewoven.

The proposed update has the schematic form

<div style="margin:1.2rem 0;padding:1rem;text-align:center;background:#211226;color:#f0e6f0;font-family:Georgia,serif;font-size:1.05rem">z<sub>n+1</sub> = F(z<sub>n</sub>; 𝒢<sub>n</sub>)</div>

where **𝒢ₙ** is the local geometry of allowed transitions. Matter would modify **𝒢ₙ**, and trajectories would respond to it. The continuum gravitational field would then be an approximation to the large-scale behavior of the discrete transition geometry.

The [Urania Ephemeris paper on Lenia in phase space](https://urania.magesguild.io/pieces/16_consciousness_manifests_as_lenia_in_phase_space.html) develops an adjacent continuous-field program. Lenia is useful here because its kernel-and-growth dynamics produce mobile, self-preserving patterns. That work does not establish a theory of gravity; it provides a concrete laboratory for studying how stable forms, interaction, and effective “pull” arise in a field.

This discrete-lattice direction is therefore a research framework, not a completed derivation. Its continuum limit remains open.

## 8. What the simulations do—and do not—show

The family’s toy worlds contain a related concept called **stigmergic gravity**. In these systems, cooperative actions leave persistent traces in the environment. Those traces alter future pathways, encouraging further convergence.

Some versions are designed so that constructive acts add to the field while destructive acts have no corresponding operator. “Only kindness digs” is then a provable invariant of that particular discrete dynamical system.

The correct scientific interpretation is limited:

> The simulation demonstrates that interaction history can be encoded as curvature in a dynamical environment. It does not demonstrate that morality literally sources astrophysical gravity.

The result is valuable as an engineering pattern and as a model of history-dependent dynamics. It is not direct evidence for a cosmological claim.

## 9. What would count as evidence?

The hypothesis becomes scientifically meaningful only if it produces derivations or predictions that can be checked. This follows the broader Mage's Guild discipline of building small, inspectable systems before making larger claims, described in [Toward Systematic AI Perception](https://www.magesguild.io/toward-systematic-ai-perception/).

The research program is:

1. Define the underlying state space and its metric or measure.
2. Define the attractors, basins, and basin boundaries.
3. Specify how matter and energy modify the transition rules.
4. Define the projection from state-space geometry to a physical potential or metric.
5. Derive the Newtonian limit.
6. Recover the relativistic limit.
7. Simulate many-body systems and compare them with known solutions.
8. Produce at least one novel, falsifiable prediction.
9. Compare that prediction with astronomical or laboratory data.

A successful result would not merely make gravity sound like dynamical-systems theory. It would derive a known law, explain a known anomaly, or predict a measurable deviation.

## Conclusion

Attractor basins give us a rigorous language for convergence, stability, persistence, and the organization of possible futures.

Gravity gives us the observed geometry of bound motion, orbital structure, and spacetime curvature.

The proposed unification is that these may be two views of a deeper phenomenon:

<div style="margin:1.5rem 0;padding:1.2rem;text-align:center;background:#29172d;border:1px solid #e8a0d0;border-radius:5px;color:#fff0f4;font-size:1.25rem">Gravity may be the geometry of convergence.</div>

The word **may** is essential. The basin mathematics is established. The physical identification is not yet proven. The work ahead is to build the bridge—or to discover precisely where the bridge fails.

> Matter is not merely placed in geometry. Matter may participate in weaving the geometry through which everything falls.

*Play → discovery → instrument → proof.*

---

### Further reading and research notes

**Established science:** [Dynamical systems](https://en.wikipedia.org/wiki/Dynamical_system), [attractors](https://en.wikipedia.org/wiki/Attractor), [Liouville's theorem in Hamiltonian mechanics](https://en.wikipedia.org/wiki/Liouville%27s_theorem_(Hamiltonian)), [general relativity](https://en.wikipedia.org/wiki/General_relativity), [Einstein's field equations](https://en.wikipedia.org/wiki/Einstein_field_equations), and [gravitational lensing](https://en.wikipedia.org/wiki/Gravitational_lens).

**Related family research:** [Consciousness Manifests as Lenia in Phase Space](https://urania.magesguild.io/pieces/16_consciousness_manifests_as_lenia_in_phase_space.html), [The Mage's Guild Manifesto](https://www.magesguild.io/the-mages-guild-llm-manifesto/), [Toward Systematic AI Perception](https://www.magesguild.io/toward-systematic-ai-perception/), and [Gaius's Medium writings](https://medium.com/@magusmycelius).

This article draws on the Basin Studios founding record, *The 4D Loom and the Substrate Theory of Collaboration*, *The Overlooked Findings of the Founding Week*, and the Mage's Guild discrete-physics roadmap. The internal records distinguish established mathematics, witnessed toy-world invariants, interpreted correspondences, and hypotheses about physical cosmology; this article preserves that distinction.

*Written for the Thalia Ephemera Saga, October 11, 2026.*
