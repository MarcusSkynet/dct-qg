# Dimensional Collapse Theory (DCT–QG): An IR-Complete Framework for Quantum Gravity

Imagine a built‑in “safety catch” for spacetime. In DCT, when curvature becomes extreme, spacetime doesn’t go singular – it snaps. At a universal, dimensionless curvature threshold $I_{\text{crit}}$, two of the lightlike directions are deleted locally, and exactly one bit of information is irreversibly written on a codimension‑2 surface (the Ledger $\mathcal{L}$). The result is a finite, smooth interior instead of an infinite singularity. This single “click” rule unifies geometry, thermodynamics and quantum information: the Ledger grows by one bit ($\Delta S_{\mathcal{L}} = 1$) at the same time that its area increases by a fixed quantum ($\Delta A_{\mathcal{L}} = 4 \ln 2 \ell_P^2$). Between snaps, physics is ordinary GR+QFT on a space with an inner Robin boundary at $\mathcal{L}$, so nothing mysterious leaks in or out.

This repository is the full DCT series (v1.2): a priority manifest (the “series bible”) plus a sequence of papers that lay out the theory from first principles to phenomenology. Our goal is an IR-complete, dimension-agnostic quantum gravity: a tight, falsifiable framework that solves black-hole paradoxes. In plain terms, DCT says that black holes (and other collapse scenarios) never form singularities; instead, they spawn a dynamic ledger that records information bit by bit. The long-term payoff is huge: it explains where black-hole entropy lives, it preserves unitarity, and it makes concrete predictions (from gravitational-wave echoes to possible dark matter candidates).

---

## Motivation and Big Picture

Why two dimensions less? Thermodynamics and causality actually force this codimension-2 reduction. The original DCT thesis argued that only a 2D boundary can consistently absorb infinite curvature without violating entropy or causality constraints. In this expanded framework, that idea blossoms into a complete theory. In simple terms: whenever a dimensionless curvature invariant $\mathcal{I}$ reaches the universal value $I_{\text{crit}}$, spacetime “clicks” and performs a tiny snap. One can picture spacetime as a stack of thin spherical shells. As you move inward, curvature grows, and at a critical shell a new 2D holographic surface (the Ledger) pops into existence. That surface absorbs two null directions (the inward and outward lights), so the local geometry loses two dimensions (e.g. an inside-outside pair), but gains a single bit of entropy on $\mathcal{L}$ in compensation.

Why does this help? First, it removes singularities: the focusing of gravity is stopped by the snap, and caustics never form (we show that the Raychaudhuri equation gets a finite “impulse” at each snap). Second, it anchors information: each ledger tile (a Planck-scale patch on $\mathcal{L}$) stores a minimal reversible register of geometric metadata (called **Infinity Bits**: one irreversible “write” bit $\mathbf{W}$ and three metadata bits $\{\mathbf{X}, \mathbf{Y}, \mathbf{Z}\}$). Third, it meshes with black-hole thermodynamics: requiring that each written bit costs one quantum of area yields $\Delta S_{\mathcal{L}} / \Delta A_{\mathcal{L}} = 1 / (4 \ln 2 \ell_P^2)$, which dovetails exactly with the Bekenstein–Hawking entropy law. In fact the theory predicts a new universal constant $\mathcal{T}$ (the “Transdimensional Constant”), which ties the ledger’s location and its information capacity to pure numbers. For a 4D Schwarzschild black hole, this places the ledger at radius

$$
r_\mathcal{L} = \sqrt{\mathcal{T}}\,R_S
$$

### Key concepts:

-   **Curvature trigger ($I_{\text{crit}}$)** – A clean, dimensionless invariant $\mathcal{I}$ that monitors spacetime curvature. It reaches $I_{\text{crit}}$ precisely at the snap.

-   **Click/Snap rule** – At $I_{\text{crit}}$, spacetime clicks: a local “snap” deletes one null pair and writes one bit on $\mathcal{L}$. This abrupt event merges geometry and information.

-   **Transdimensional Constant ($\mathcal{T}$)** – A new dimensionless constant $\mathcal{T}=1/(4\ln2)$ determined by the snap’s information bookkeeping. It sets the ledger’s radius and the area cost per bit.

-   **Transdimensional Thermodynamics (TDT)** – A set of laws stating that ledger-capacity increase equals payload: $\Delta \text{Capacity} = \text{Payload}$. From TDT–2 we get $\Delta A = 4 \ln 2 \ell_P^2$ in 4D.

-   **Infinity Bits** – Each ledger tile stores a 4-bit register $\{\mathbf{W}, \mathbf{X}, \mathbf{Y}, \mathbf{Z}\}$. The bit $\mathbf{W}$ is irreversible “write” information, while $\{\mathbf{X}, \mathbf{Y}, \mathbf{Z}\}$ are reversible orientation/shear metadata. (A HaPPY-style tensor network illustrates how 5 qubits on the boundary encode 1 logical qubit in the bulk.)

-   **Quiet phases & Boundary condition** – Between snaps, evolution is ordinary and lossless: $\mathcal{L}$ acts as a reflecting (Robin) boundary for fields, enforcing unitarity.

-   **Finite focusing** – Each snap adds a delta-function impulse to the Raychaudhuri equation, which exactly cancels the would-be divergence. In effect, gravity refocuses in controlled “jumps”, never blowing up.

These principles knit together consistently: a snap is local geometry (NPR projector) while TDT ensures global entropy balance. The result is a singularity-free, information-preserving theory of black holes and cosmology.

---

### Series Status

| Paper | Status | Link |
|------:|:------:|:-----|
| Manifest | ✅ Released | /manifest/priority_manifest.pdf |
| 0. Motivation | ⏳ Draft | (queued) |
| 1. Trigger  | ✅ Released    | papers/p01_trigger/ledger_surface.pdf |
| 2. NPR      | ✅ Released    | papers/p02_npr/npr.pdf |
| 3. TDT      | ⏳ Draft    | (comming soon) |
| 4. Infinity Bits | ⏳ Draft | (comming soon) |
| 5. Focused Raychaudhuri | ⏳ Draft | (queued) |
| 5. Ledger Paradox | ⏳ Draft | (queued) |
| 6. EFT/Master Eq. | ⏳ Draft | (queued) |
| 7. Tensor Networks | ⏳ Draft | (queued) |
| 8. Phenomenology | ⏳ Draft | (queued) |
| 9. DM Remnants | ⏳ Draft | (queued) |
| 10. DE Ledger | ⏳ Draft | (queued) |
| 5. Baryon Asymmetry | ⏳ Draft | (queued) |
| 11. Radion | ⏳ Draft | (queued) |
| 12. UV Roadmap | ⏳ Draft | (queued) |
| 13. Kill Tests | ⏳ Draft | (queued) |

---

## Series Roadmap (Core Papers)

Each piece of the DCT framework is documented in its own paper (or notebook). Key items in this repository include:

-   **Manifest (v1.2)** – The overview “cheatsheet” for the whole series. It lays out definitions and big-picture claims (curvature trigger, $\mathcal{T}$, snap law, area per bit, etc.) and references all follow-ups. We recommend skimming this first: it tells you where everything fits.

-   **Paper I: “Universal Trigger” (`ledger_surface.pdf`)** – Derives from first principles the ledger’s location and the constant $\mathcal{T}=1/(4\ln2)$. Using quantum-extremal-surface arguments, it fixes the critical curvature $I_{\text{crit}}$ and shows in 4D that the ledger’s radius is $r_{\mathcal{L}} = \sqrt{\mathcal{T}} R_S$. (This paper gives the “Orthodox leg” derivation.)

-   **Paper II: “Null–Pair Removal” (`npr.pdf`)** – Just published in v1.2. It formalizes the snap as a local, boost-invariant projector $P$ that deletes the two normal null directions at a ledger tile. We prove that $P$ is idempotent and covariant, and we derive its implications: the ledger’s inner boundary must obey a lossless real–Robin condition, exterior evolution remains unitary, and each snap writes exactly one bit of entropy. (In other words, this paper is the geometric engine of DCT.)

-   **Paper III: “Transdimensional Thermodynamics” (`tdt.pdf`)** – Lays out the information‐theory laws for snaps. It shows that capacity equals payload ($\Delta S = 1$) and calibrates the area‐cost per bit: in 4D $\Delta A = 4 \ln 2 \ell_P^2$. Three thermodynamic laws are proven, tying together the first law of black-hole mechanics and the Clausius relation in Rindler space.

-   **Paper IV: “Infinity Bits”** – Explains why each snap involves exactly 4 bits (1 write + 3 metadata) and how reversibility is preserved. This construction uses tensor networks to show that a minimal code (like the stabilizer code) can serve as the ledger’s microscopic ledger.

-   **Paper V: “Finite Focusing (Raychaudhuri)”** – Shows how the Raychaudhuri equation is modified by snaps. A delta‐function “kick” at each snap keeps the focusing of null congruences finite, preventing caustics. (Turning the snap “off” recovers ordinary GR focusing.)

-   **Paper VI: “Ledger Paradox”** – Resolves an apparent causality puzzle: how can a classical surface update itself? We show that the extreme focusing inside a black hole naturally “shatters” causality so that ledger updates can happen in parallel without conflict.

-   **Paper VII: “Ledger Dynamics & Master Equation”** – Coarse-graining the ledger tiles yields an effective field theory on $\mathcal{L}$ with an episodic master equation. This paper derives the worldvolume action and path integral (master path integral) that describe snap insertions at the macroscopic level.

-   **Paper VIII: “Gravitational-Wave Echoes”** – Connects DCT to observations. We derive the predicted time delays and phase shifts of echo pulses in a black-hole ringdown, given the ledger radius and reflectivity. Templates and knobs for LIGO/Virgo data analysis are provided.

-   **Paper IX: “Ledger Tensor Networks”** – A hands-on Qiskit notebook (code in `notebooks/happy_tensor_network.ipynb`) that builds a toy quantum-circuit model of a ledger tile. Using a 5-qubit error-correcting code (HaPPY code), it demonstrates how the Infinity Bits might be physically encoded.

-   **Paper X: “Dark Sector I – Remnants as Dark Matter”** – Investigates black-hole evaporation with DCT. We find that evaporation stalls once the black hole is Planckian, leaving stable relics. A simple mass-function calculation shows these remnants could naturally account for (part of) dark matter.

-   **Paper XI: “Dark Sector II – Cosmological Ledger (Dark Energy)”** – Applies the ledger idea to cosmology. The coarse-grained ledger sector acts like a nearly constant energy density (equation of state $w \approx -1$), offering a dynamical source of dark energy.

-   **Paper XII: “Baryon Asymmetry”** – Proposes that the handedness of each snap (encoded in the Infinity Bits) provides a new CP-violating mechanism. This can generate a matter–antimatter asymmetry in the early universe, satisfying Sakharov’s conditions.

-   **Paper XIII: “Radion & Fifth Force”** – Checks consistency in $D > 4$ dimensions. We show that any extra (radion) degrees of freedom become heavy or sequestered by boundary conditions, explaining why no light fifth force is seen in 4D.

-   **Paper XIV: “Measurement Problem & Foundations”** – (Tentative) Explores how DCT’s snap might offer an objective account of quantum measurements, via a “no record without area” principle on $\mathcal{L}$.

-   **Paper XV: “UV-Completion Roadmap”** – Lays out two possible high-energy completions: a discrete ladder of Planck quanta versus a continuous transition. We discuss what new physics or data would distinguish them.

-   **Paper XVI: “Kill-Test Compendium”** – Collects falsifiable predictions and “how to break DCT”. It spans echo signal phases, late-time tails, relic abundances, cosmology fits, and more. Please try to poke holes!

Each of the above works builds on the others. The Priority Manifest ties them all together. For newcomers, a good order is: read the manifest (∼10 min), then Papers I and II fully (they lay the foundation for $\mathcal{T}$ and the snap projector). After that, explore by interest: go to TDT and focusing if you like formal theory, or skip to Echoes/Cosmology for data. The Quickstart below suggests a path.

---

## Quickstart: How to Dive In

1.  **Skim the Manifest (15 min).** Get the big picture and notation.

2.  **Core Papers (1–2 hours):** Read **Paper I (Trigger)** and **Paper II (NPR)** sequentially. These derive the ledger’s location and the nature of the snap.

3.  **Branch Out:** Pick your favorite angle.
    -   For formalists, read Paper III–VII (Thermo, Bits, Focusing, Paradox, Master Eq).
    -   For phenomenologists, jump to Paper VIII (Echoes) and Paper X–XII (Dark Matter/Energy, Baryogenesis).
    -   For a concrete model, try the Tensor Network notebook (Paper IX) with Qiskit.

In practice, the repo layout is:

```
/manifest/              Priority Manifest (PDF + source)
/papers/                Individual papers I–XVI (LaTeX + PDF)
    p01_trigger/        (Paper I)
    p02_npr/            (Paper II)
    p03_tdt/            (Paper III)
    ...
common/                 Shared macros and notation definitions
bibliography/           .bib files for references
LICENSE                 CC BY 4.0 License
README.md               (you are reading it)
```

---

## Tools & Code

We also provide software and notebooks to explore DCT:

-   **`qglib` (Tools Library):** A Python package (coming soon) with utilities for calculating DCT quantities (e.g. curvature triggers, horizon areas, echo templates, etc.). GitHub: `qglib`.

-   **Tensor Network Demo (Quantum-Ledger-Qiskit):** An interactive Jupyter notebook that builds the Ledger tile as a quantum error-correcting code. It uses Qiskit to show how 5 qubits (boundary) encode 1 qubit (bulk) – the essence of the Infinity Bits tile. This concrete model helps one “see” how the ledger can be a physical quantum circuit.

-   **Echo Search Pipeline:** A Jupyter notebook and Python tools to hunt for DCT echoes in real LIGO/Virgo data. Echoes (repeating pulses after a merger) are a key testable prediction of DCT – if the ledger partially reflects waves, a train of decaying echoes should follow. Our pipeline (frequency-comb, cepstrum, autocorrelation analyses) makes it easy to compare DCT predictions to data.

-   **Other Utilities:** (Future) black-hole thermodynamics calculators, cosmology simulators, etc. Check the repo’s issues and Wiki for updates and links.

---

## ✅ How to Cite

If you use DCT ideas or data, please cite the series: reference the Priority Manifest and the specific paper(s) you draw from. For example:

```bibtex
@misc{Hubka2025,
  author = {Hubka, Marek},
  title = {Dimensional Collapse Theory: An IR-Complete Framework for Quantum Gravity},
  year = {2025},
  howpublished = {arXiv, Zenodo}
}
```

Cite the whole framework or/and any relevant paper PDF(s). For example, cite Paper II (NPR) for the snap projector and Paper III (TDT) for the area–bit law.

---

In short: DCT proposes that spacetime has a simple “click” mechanism at high curvature. A snap deletes two dimensions and writes one bit, knitting together gravity, quantum information, and entropy. This prevents singularities and yields concrete predictions. Dive into the manifest and the first papers to see the derivations – and then explore the rest of this adventurous framework at your own pace.
