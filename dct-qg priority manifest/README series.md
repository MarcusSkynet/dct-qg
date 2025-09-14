# Dimensional Collapse Theory (DCT) — the Series

**Short version:** spacetime has a **click**. When a simple, dimensionless curvature gauge crosses a universal threshold, a tiny, local **snap** deletes one null pair, commits **one payload bit** to a codimension-2 surface—the **Ledger** $\mathcal L$—and life goes on. No singularities, thermodynamics in charge, quantum mechanics respected.

This repo is the **compilation**: one manifest that plants the flag, plus **13 papers** that do the heavy lifting—geometry, thermodynamics, EFT, phenomenology, cosmology, simulations, and stress tests.

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

* **Build PDFs:** `pdflatex → bibtex → pdflatex ×2` in each `papers/pXX/*` folder.

* **Figures:** `python scripts/dct/qg/manifest/figures.py` (no external data).

* **Tensor-network demo:**

    * Python ≥ 3.10, `qiskit` (or `qiskit-aer`) installed.

    * Open `notebooks/tensor/network/demo.ipynb`.

    * Run cells to see a 6-qubit node, boundary routing, and simple echo toy.

* **EFT notebook hooks:** placeholders are in `notebooks/echo/templates.ipynb` (you plug in your kernel $\mathsf S$ or $\mathsf B$).

---

## Repo layout (suggested)

```
/manifest/            priority/manifest.tex + pdf
/papers/
    p01/trigger/     (alpha/T, placement)
    p02/npr/
    p03/tdt/
    p04/infinity/bits/
    p05/focused/raychaudhuri/
    p06/eft/master/eq/
    p07/tensor/networks/
    p08/phenomenology/
    p09/dark/matter/
    p10/dark/energy/
    p11/radion/
    p12/uv/roadmap/
    p13/kill/tests/
    common/           macros, figures, bibliography
/scripts/             figure builders, small tools
/notebooks/           qiskit demos, echo templates

```

**Macros:** we ship `dct/macros.sty`. Symbols: $\mathcal L,\mathcal I,\mathcal T$ (anchors), upright-sans $\mathsf S,\mathsf B,\mathsf R$ (boundary response), left tags ${}^{(D)},{}^{(d)}$ when bulk + ledger appear together. Entropy subscripts $S_{\mathcal L}, S_{\mathrm{BH}}$. Actions $S_{\mathrm{EH}}, S_{\mathrm{matter}}, S_{\partial}, S_{\mathrm{snap}}$ with arguments.

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

## License

* Text \& figures: CC BY 4.0

* Code \& notebooks: MIT

---

## How to cite

* **Series:** cite the manifest + specific paper(s) you use.

* **Example (APA):** Marcus (2025). *Dimensional Collapse Theory (DCT): Priority Manifest and Roadmap*. Zenodo. DOI-TBA.

BibTeX:

```bibtex

@misc{DCT/manifest/2025,
    author = {Marcus},
    title = {Dimensional Collapse Theory (DCT): Priority Manifest and Roadmap},
    year = {2025},
    version = {v1.0},
    doi = {DOI-TO-BE-ASSIGNED},
    publisher = {Zenodo}
}

```

---

## FAQ (one screen)

* **Why four bits at a snap?** One irreversible payload bit, three reversible geometric bits to unambiguously unwind NPR.

* **Why this invariant?** $\mathcal I=r^{4}K$ removes mass-scaling and gives a clean, universal threshold $\mathcal I_{\mathrm{crit}}$.

* **Where’s the Lagrangian?** In quiet phases, it’s a **boundary** story: $(\partial_n+\mathsf S)\psi|_{\mathcal L}=0$.

* **How do snaps show up in the path integral?** As a **product of factors**, one per event—additive in the action, multiplicative in the weight.