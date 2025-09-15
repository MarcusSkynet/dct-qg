# An IR complete framework for Quantum Gravity in D-dimensions

**Author:** Marek Hubka  
**Version:** 0.1 (September 2025)  

[https://doi.org/DOI-TO-BE-ASSIGNED](https://doi.org/DOI-TO-BE-ASSIGNED)
![License](https://img.shields.io/badge/docs-CC--BY--NC--ND%204.0-lightgrey.svg)

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
| 0. Manifest | ✅ Released | /manifest/priority_manifest.pdf |
| 1. Trigger  | ⏳ Draft    | (coming soon) |
| 2. NPR      | ⏳ Draft    | (coming soon) |
| 3. TDT      | ⏳ Draft    | (coming soon) |
| 4. Infinity Bits | ⏳ Draft | (coming soon) |
| 5. Focused Raychaudhuri | ⏳ Draft | (coming soon) |
| 6. EFT/Master Eq. | ⏳ Draft | (coming soon) |
| 7. Tensor Networks | ⏳ Draft | (coming soon) |
| 8. Phenomenology | ⏳ Draft | (coming soon) |
| 9. DM Remnants | ⏳ Draft | (coming soon) |
| 10. DE Ledger | ⏳ Draft | (coming soon) |
| 11. Radion | ⏳ Draft | (coming soon) |
| 12. UV Roadmap | ⏳ Draft | (coming soon) |
| 13. Kill Tests | ⏳ Draft | (coming soon) |

---

## Read me first

* **House symbols:** $\mathcal L$ (Ledger), $\mathcal I$ (dimensionless invariant), $\mathcal T=1/(4\ln 2)$ (Transdimensional Constant).

* **Snap law (TDT):** capacity matches payload $\delta S_{\mathcal L}=\delta S_{\mathrm{info}}$; one bit costs $\Delta A=4\ln 2\,\ell_{\mathrm P}^{2}$.

* **Trigger:** $\mathcal I(r)=r^{4}K(r)$ and $\mathcal I_{\mathrm{crit}}=48\ln 2$.

* **Placement (Schwarzschild):** $r_{\mathcal L}=\sqrt{\mathcal T}\,R_S$.

If those four lines make sense, you’re already 80% of the way there.

---

## Roadmap (14 items)

**0. Priority Manifest (the “series bible”)**

- What it is: the bird’s-eye view and references for everything below.
- Deliverable: one PDF to cite while the rest lands.
- Why start here: you’ll know where each piece fits before diving.

**1. The Universal Trigger (Foundation)**
- Title: *A Universal Curvature Trigger for Spacetime Dimensional Collapse*
- What it answers: why the snap happens **exactly** at $\mathcal I=\mathcal I_{\mathrm{crit}}$; why $r_{\mathcal L}=\sqrt{\mathcal T}\,R_S$.
- Takeaway figure: $\mathcal I(r)$ crossing $48\ln 2$.

**2. Null-Pair Removal (Geometric Mechanism)**
- Title: *NPR: Deleting One Null Pair Cleanly*
- What it answers: what “deleting” means mathematically (the projector), what survives, what doesn’t.
- One-liner: kinematics in one page; proofs in appendices.

**3. Transdimensional Thermodynamics (TDT)**
- Title: *Capacity, Payload, and the Area Tick*
- What it answers: why $\delta S_{\mathcal L}=\delta S_{\mathrm{info}}$ and $\Delta A=4\ln 2\,\ell_{\mathrm P}^{2}$.
- Punchline: “no record without area.”

**4. Infinity Bits (Reversible Register)**
- Title: *$\{X,Y,Z\}$ + branch: the minimal reversible write*
- What it answers: why **four** bits; why three are geometric metadata; how reversibility survives.

**5. Focused Raychaudhuri (Finite Focusing)**
- Title: *How Thermo Tames Caustics*
- What it answers: the Raychaudhuri equation with the snap term; how singularities don’t form; recovery of classical focusing when you turn the knob back.

**6. Ledger EFT \& Master Equation (IR QG EFT)**
- Title: *Quiet Phases as Boundary Physics*
- What it answers: between snaps, the Ledger is a **Robin** boundary; in the master equation, snaps are **episodic** CP–TP kicks.
- For implementers: use effective ${}^{(d)}\!S_{\partial}[\psi]$ now; microscopic ledger DOFs later.

**7. Tensor Networks for Snaps**
- Title: *HaPPY-style Encoding of Infinity Bits*
- What it answers: how to tile and route $\{X,Y,Z,\text{branch}\}$; what’s actually simulated; where Qiskit plugs in.
- Repo hook: `notebooks/tensor_network_demo.ipynb` (see Quickstart).

**8. Phenomenology (Echoes \& Hawking Bookkeeping)**
- Title: *From the Ledger to the Telescope*
- What it answers: echo time delays, phases, reflectivity $\mathsf R(\omega)$; modified Hawking flux.
- Deliverable: templates + knobs to fit GW data.

**9. Dark Sector I (Remnants as Dark Matter)**
- Title: *Stabilized Remnants and the Mass Function*
- What it answers: why evaporation stalls; relic abundance windows; constraints.

**10. Dark Sector II (Cosmological Ledger as DE)**
- Title: *A Smooth Component from Boundary Thermo*
- What it answers: effective $w \approx -1$ with small drift; what to look for in data.

**11. Radion/ Fifth Force**
- Title: *Why It’s There in $D>4$ and Why You Don’t See It in 4D*
- What it answers: sequestering by mass and boundary conditions; lab constraints; astrophysical knobs.

**12. UV-Completion Roadmap**
- Title: *Two Paths to the Mountain Top*
- What it answers: discrete ladder vs. continuous interpolation; what data/theory would decide.

**13. Kill Tests (Falsification Suite)**
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
/manifest/            priority/manifest.tex + pdf
/papers/              
    p01_trigger/      
    p02_npr/
    p03_tdt/
    p04_infinity_bits/
    p05_focused_raychaudhuri/
    p06_eft_master_eq/
    p07_tensor_networks/
    p08_phenomenology/
    p09_dark_matter/
    p10_dark_energy/
    p11_radion/
    p12_uv_roadmap/
    p13_kill_tests/
    common/           notation conventions
LICENSE               The CC BY 4.0 License
README.md             this file

```

Symbols: $\mathcal L,\mathcal I,\mathcal T$ (anchors), upright-sans $\mathsf S,\mathsf B,\mathsf R$ (boundary response), left tags ${}^{(D)},{}^{(d)}$ when bulk + ledger appear together. Entropy subscripts $S_{\mathcal L}, S_{\mathrm{BH}}$. Actions $S_{\mathrm{EH}}, S_{\mathrm{matter}}, S_{\partial}, S_{\mathrm{snap}}$ with arguments.

---

## What to test (per paper)

* **P1:** check $\mathcal I$ threshold on Schwarzschild/Kerr slices; verify $r_{\mathcal L}=\sqrt{\mathcal T}\,R_S$.

* **P2:** verify projector properties (idempotent, trace $=D-2$, boost-invariance).

* **P3:** one-bit area tick $4\ln 2\,\ell_{\mathrm P}^{2}$.

* **P4:** four-bit necessity (thermo + reversibility).

* **P5:** recovery of classical Raychaudhuri when the snap term is tuned off.

* **P6:** Robin kernels $\Rightarrow$ reflectivity $\mathsf R(\omega)$.

* **P7:** encode/decode paths; stability under noise.

* **P8:** echo delays \& phases vs. ringdown fits.

* **P9–10:** parameter windows that pass cosmology bounds.

* **P11:** 4D sequestering of the radion.

* **P12–13:** try to falsify the framework (please).

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
  doi          = {DOI-TO-BE-ASSIGNED},
  url          = {https://doi.org/10.5281/zenodo.16152610}
}
```

---

## FAQ

* **Why four bits at a snap?** One irreversible payload bit, three reversible geometric bits to unambiguously unwind NPR.

* **Why this invariant?** $\mathcal I=L^{4}K$ removes mass-scaling and gives a clean, universal threshold $\mathcal I_{\mathrm{crit}}$.

* **Where’s the Lagrangian?** In quiet phases, it’s a **boundary** story: $(\partial_n+\mathsf S)\psi|_{\mathcal L}=0$.

* **How do snaps show up in the path integral?** As a **product of factors**, one per event—additive in the action, multiplicative in the weight.