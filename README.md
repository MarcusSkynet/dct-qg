# An IR complete framework for Quantum Gravity in n-dimensions

**Author:** Marek Hubka  
**Version:** 1.0 (September 2025)  

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17136168.svg)](https://doi.org/10.5281/zenodo.17136168)
![License](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)

**Short version:** spacetime has a **click**. When a simple, dimensionless curvature gauge crosses a universal threshold, a tiny, local **snap** deletes one null pair, commits **one payload bit** to a codimension-2 surface—the **Ledger** $\mathcal L$—and life goes on. No singularities, thermodynamics in charge, quantum mechanics respected.

This repository is the **compilation**: one manifest that plants the flag, plus **13 papers** that do the heavy lifting—geometry, thermodynamics, EFT, phenomenology, cosmology, simulations, and stress tests.

---

### Relation to the Original [DCT Thesis](https://github.com/MarcusSkynet/dct)

This series is not appearing out of thin air. It builds directly on the original **Dimensional Collapse Theory (DCT)** thesis, where the core idea was first formulated: that spacetime can undergo dimensional reduction once a universal curvature threshold is crossed.  

What you’re reading here **supersedes** that early version. The original thesis introduced the premise and sketched the central mechanism. This series keeps those insights but expands them into a **complete, systematic framework**, with clear derivations, consistency checks, and phenomenological consequences.  

Think of the thesis as the seed and this series as the full-grown tree.

---

### Series Status

| Paper | Status | Link |
|------:|:------:|:-----|
| Manifest | ✅ Released | /manifest/priority_manifest.pdf |
| 0. Motivation | ⏳ Draft | (queued) |
| 1. Trigger  | ✅ Released    | papers/p01_trigger/interior_surface_of_bh.pdf |
| 2. NPR      | ⏳ Draft    | (coming soon) |
| 3. TDT      | ⏳ Draft    | (queued) |
| 4. Infinity Bits | ⏳ Draft | (queued) |
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

## Read me first

* **House symbols:** $\mathcal L$ (Ledger), $\mathcal I$ (dimensionless invariant), $\mathcal T=1/(4\ln 2)$ (Transdimensional Constant).

* **Snap law (TDT):** capacity matches payload $\delta S_{\mathcal L}=\delta S_{\mathrm{info}}$ and one bit costs $\Delta A=4\ln 2 \ell_{\mathrm P}^{2}$.

* **Trigger:** $\mathcal I=L^{4}K$ and $\mathcal I_{\mathrm{crit}}=48\ln 2$.

* **Placement (Schwarzschild):** $r_{\mathcal L}=\sqrt{\mathcal T}R_S$.

If those four lines make sense, you’re already 80% of the way there.

---

## Roadmap (17 items)

**Priority Manifest (the “series bible”)**

- What it is: the bird’s-eye view and references for everything below.
- Deliverable: one PDF to cite while the rest lands.
- Why start here: you’ll know where each piece fits before diving.

**0. Motivation (The "Why")**
- Title: *On the Necessity of Codimension-Two Reduction*
- What it answers: Why is the `D -> D-2` axiom the most logical choice?
- Takeaway: Argues from first principles (thermodynamics, causality, geometry) that a codimension-two boundary is the uniquely elegant solution to the singularity problem.

**1. The Universal Trigger (Foundation)**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17289422.svg)](https://doi.org/10.5281/zenodo.17289422)
- Title: *The Universal Interior Surface of Black Holes and the Derivation of the Transdimensional Constant*
- What it answers: why the snap happens **exactly** at $\mathcal I=\mathcal I_{\mathrm{crit}}$ and why $r_{\mathcal L}=\sqrt{\mathcal T} R_S$.
- Takeaway figure: $\mathcal I(r)$ crossing $48\ln 2$.

**2. Null-Pair Removal (Geometric Mechanism)**
- Title: *NPR: Deleting One Null Pair Cleanly*
- What it answers: what “deleting” means mathematically (the projector), what survives, what doesn’t.
- One-liner: kinematics in one page; proofs in appendices.

**3. Transdimensional Thermodynamics (TDT)**
- Title: *Capacity, Payload, and the Area Tick*
- What it answers: why $\delta S_{\mathcal L}=\delta S_{\mathrm{info}}$ and $\Delta \mathcal{A}=4\ln 2 \ell_{\mathrm P}^{2}$.
- Punchline: “no record without area.”

**4. Infinity Bits (Reversible Register)**
- Title: *The Minimal Reversible Write: $\{X,Y,Z\} + b_r$*
- What it answers: why **four** bits; why three are geometric metadata; how reversibility survives.

**5. Finite Focusing (Singularity Resolution)**
- Title: *How TDT Tames the Raychaudhuri Equation*
- What it answers: the Raychaudhuri equation with the snap term; how caustics don’t form; recovery of classical focusing when you turn the knob back.

**6. The Ledger Paradox (Causal Consistency)**
- Title: *Resolving Causality on a Classical Spacetime Boundary*
- What it answers: How can an extended, classical surface inside a black hole update its state without violating causality?
- Punchline: The intense focusing of the BH interior creates a "shattered causality" that naturally allows for parallel, causally independent updates.

**7. Ledger Dynamics & Master Equation (The Engine)**
- Title: *Quiet Phases and Impulsive Snaps: The Master Equation*
- What it answers: between snaps, the Ledger is a **Robin** boundary; at snaps, the state gets a **CP–TP kick**.
- For implementers: use effective ${}^{(d)} S_{\partial}[\psi]$ now; microscopic ledger DOFs later.

**8. Gravitational-Wave Echoes (Phenomenology)**
- Title: *From the Ledger to the Telescope*
- What it answers: echo time delays, phases, reflectivity $\mathsf R(\omega)$.
- Deliverable: templates + knobs to fit GW data.

**9. Ledger Coding (Microscopic Model)**
- Title: *HaPPY-style Encoding of the Infinity Bits*
- What it answers: how to tile the ledger with quantum error-correcting codes; where Qiskit plugs in.
- Repo hook: `notebooks/happy_tensor_network.ipynb` (see Quickstart).

**10. Dark Sector I (Remnants as Dark Matter)**
- Title: *Stabilized Remnants and the Mass Function*
- What it answers: why evaporation stalls; relic abundance windows; constraints.

**11. Dark Sector II (Cosmological Ledger as DE)**
- Title: *A Smooth Component from Boundary Thermo*
- What it answers: effective $w \approx -1$ with small drift; what to look for in data.

**12. Baryon Asymmetry (Cosmological Origin)**
- Title: *A Gravitational Origin of the Baryon Asymmetry*
- What it answers: How can the universe have more matter than antimatter?
- Punchline: The "handedness" of a geometric snap (encoded in the Infinity Bits) provides a natural source of CP-violation, satisfying the Sakharov conditions.

**13. Radion & Fifth Force (Consistency Check)**
- Title: *Why It’s There in* $D>4$ *and Why You Don’t See It in 4D*
- What it answers: sequestering by mass and boundary conditions; lab constraints; astrophysical knobs.

**14. The Measurement Problem (Foundations)**
- Title: *Objective Snaps and the "No Record Without Area" Principle*
- What it answers: What *is* a quantum measurement?
- Punchline: A physical event (a snap) that costs a quantum of area on the ledger.

**15. UV-Completion Roadmap**
- Title: *Two Paths to the Mountain Top*
- What it answers: discrete ladder vs. continuous interpolation; what data/theory would decide.

**16. Kill Tests (Falsification Suite)**
- Title: *How to Break DCT (Please Try)*
- What it answers: decisive predictions to shoot at—echo phases, late-time tails, remnant spectra, cosmology fits.

---

## Quickstart (humans)

1. **Skim the manifest** (10–15 min).

2. Read **Papers 1–5** in order (trigger → NPR → TDT → Infinity Bits → focusing).

3. Jump to your taste: **EFT/ME** if you like formalism; **Phenomenology** if you like data; **Tensor Networks** if you like simulations; **Dark Sector** if you like cosmology.

---

## Quickstart (machines)

**The Theory:**
To build all papers from source: `pdflatex -> bibtex -> pdflatex ×2` in each `papers/pXX_*` folder.

**The Software (coming soon):**

*   **Tools Library:** The main Python package for DCT-QG calculations.
    *   **[Go to `qgledger` Repository &raquo;](https://github.com/YourUsername/qgledger)**

*   **Tensor Network Demo:** A hands-on Qiskit notebook demonstrating the microscopic ledger.
    *   **[Go to `Quantum-Ledger-Qiskit` Repository &raquo;](https://github.com/YourUsername/Quantum-Ledger-Qiskit)**

*   **Echo Search Pipeline:** A Jupyter notebook and tools to search for echoes in LIGO data.
    *   **[Go to `Echo-Search-Pipeline` Repository &raquo;](https://github.com/YourUsername/Echo-Search-Pipeline)**

---

## Repo layout

```
/manifest/            - priority/manifest.tex + pdf
/papers/              - individual papers (tex + pdf)
    p00_motivation/
    p01_trigger/      
    p02_npr/
    p03_tdt/
    p04_infinity_bits/
    p05_focused_raychaudhuri/
    p06_ledger_paradox/
    p07_eft_master_eq/
    p08_tensor_networks/
    p09_phenomenology/
    p10_dark_matter/
    p11_dark_energy/
    p12_baryon_asymmetry/
    p13_radion/
    p14_uv_roadmap/
    p15_kill_tests/
common/               - notation conventions and universal preamble
bibliography/         - reference bibliography
LICENSE               - The CC BY 4.0 License
README.md             - this file

```

Symbols: 
- $\mathcal L,\mathcal I,\mathcal T$ (anchors),
- upright-sans $\mathsf S,\mathsf B,\mathsf R$ (boundary response),
- left tags ${}^{(D)}(\cdot),{}^{(d)}(\cdot)$ when bulk + ledger appear together.
- Entropy subscripts $S_{\mathcal L}, S_{\mathrm{BH}}$.
- Actions $S_{\mathrm{EH}}, S_{\mathrm{matter}}, S_{\partial}, S_{\mathrm{snap}}$ with arguments.

---

## What to test

* **1:** check $\mathcal I$ threshold on Schwarzschild/Kerr slices; verify $r_{\mathcal L}=\sqrt{\mathcal T} R_S$.

* **2:** verify projector properties (idempotent, trace $=D-2$, boost-invariance).

* **3:** one-bit area tick $4\ln 2 \ell_{\mathrm P}^{2}$.

* **4:** four-bit necessity (thermo + reversibility).

* **5:** recovery of classical Raychaudhuri when the snap term is tuned off.

* **6:** Robin kernels $\Rightarrow$ reflectivity $\mathsf R(\omega)$.

* **7:** encode/decode paths; stability under noise.

* **8:** echo delays \& phases vs. ringdown fits.

* **9–10:** parameter windows that pass cosmology bounds.

* **11:** 4D sequestering of the radion.

* **12–13:** try to falsify the framework (please).

---

## How to cite

* **Series:** cite the manifest + specific paper(s) you use.

BibTeX:

```bibtex
@misc{Hubka2025,
  author       = {Marek Hubka},
  title        = {An IR complete framework for Quantum Gravity in D-dimensions},
  year         = {2025},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.17136167}
}
```

---

## FAQ

* **Why four bits at a snap?** One irreversible payload bit, three reversible geometric bits to unambiguously unwind NPR.

* **Why this invariant?** $\mathcal I=L^{4}K$ removes mass-scaling and gives a clean, universal threshold $\mathcal I_{\mathrm{crit}}$.

* **Where’s the Lagrangian?** In quiet phases, it’s a **boundary** story: $(\partial_n+\mathsf S)\psi|_{\mathcal L}=0$.

* **How do snaps show up in the path integral?** As a **product of factors**, one per event—additive in the action, multiplicative in the weight.
