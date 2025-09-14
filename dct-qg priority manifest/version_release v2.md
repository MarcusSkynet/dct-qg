## Title

**Dimensional Collapse Theory (DCT): Priority Manifest and Roadmap**

## Description

This deposit publishes the **Priority Manifest** for a new, self-contained framework of quantum gravity—**Dimensional Collapse Theory (DCT)**—and provides a roadmap for the accompanying paper series.

DCT posits that spacetime undergoes **episodic, local “snaps”** in which a null pair in the normal 2-plane is deleted (NPR). Each snap commits an **irreversible payload bit** to a codimension-2 surface called the **Ledger** $\mathcal L$, growing its entropy by $\delta S_{\mathcal L}=\ln 2$ and consuming area $\Delta A=4\ln 2\,\ell_{\mathrm P}^{2}$. The snaps are triggered when a **dimensionless curvature invariant** reaches a universal threshold:

$$
\mathcal I(r)=r^{4}K(r),\qquad
\mathcal I_{\mathrm{crit}}=48\ln 2=\frac{12}{\mathcal T},\qquad
\mathcal T=\frac{1}{4\ln 2}.
$$

For the Schwarzschild family this places the Ledger at

$$
r_{\mathcal L}=\sqrt{\mathcal T}\,R_S.
$$

Between snaps, the Ledger behaves as an **inner boundary** with a real **Robin** kernel (effective, frequency-local reflectivity). Snaps appear as **localized insertions** in the master path integral (one multiplicative factor per event). The manifest also defines the minimal **reversible register** written at each snap—**Infinity Bits** $\{X,Y,Z\}$ plus the payload bit—ensuring kinematic reversibility of NPR consistent with thermodynamics.

Beyond the core mechanism, the document outlines: a focused (regulated) Raychaudhuri equation that avoids singularities, a boundary-EFT viewpoint for quiet phases, phenomenology for gravitational-wave echoes and Hawking bookkeeping, cosmological implications (stable remnants as dark matter; a smooth ledger contribution to dark energy), and a tensor-network mapping suitable for simulation.

**This is the authoritative roadmap**: subsequent papers (listed in the manifest) will supply full derivations, proofs, and data analyses.

## What’s new in this release

* **Notation finalized.** Calligraphic DCT triad $(\mathcal L,\mathcal I,\mathcal T)$; upright-sans for boundary kernels $(\mathsf S,\mathsf B,\mathsf R)$; left dimension tags ${}^{(D)}$, ${}^{(d)}$.
* **Refactor:** $\alpha_{\mathrm H} \rightarrow \mathcal T = 1/(4\ln 2)$ (Transdimensional Constant).
* **TDT law clarified:** $\delta S_{\mathcal L}=\delta S_{\mathrm{info}}$ (capacity equals payload); area-per-bit $\Delta A=4\ln 2\,\ell_{\mathrm P}^{2}$.
* **Entropy subscripts fixed:** $S_{\mathrm{BH}}$ (Bekenstein–Hawking), $S_{\mathcal L}$ (Ledger).
* **Path-integral style:** snaps as **product of factors**; effective boundary action ${}^{(d)}\!S_{\partial}[\psi]$ at manifest level; microscopic ledger EFT deferred to its own paper.

## Contents

* **priority\_manifest.pdf / .tex** — main document (this release).
* **Figures script (optional):** `dct_qg_manifest_figures.py` (generates schematic plots referenced in the text).
* **Macros (optional snippet):** unified LaTeX macro set for symbols and fonts.

> **Note:** The manifest intentionally keeps the EFT boundary in its **effective** form; the **microscopic** route (ledger DOFs $\phi$, mixing, integration to Robin) is covered in a follow-up paper.

## How to cite

**Preferred citation (APA style):**
Marcus (2025). *Dimensional Collapse Theory (DCT): Priority Manifest and Roadmap* (v1.0). Zenodo. [https://doi.org/DOI-TO-BE-ASSIGNED](https://doi.org/DOI-TO-BE-ASSIGNED)

**BibTeX:**

```bibtex
@misc{DCT_manifest_2025,
  author = {Marcus},
  title = {Dimensional Collapse Theory (DCT): Priority Manifest and Roadmap},
  year = {2025},
  version = {v1.0},
  doi = {DOI-TO-BE-ASSIGNED},
  publisher = {Zenodo}
}
```

## Keywords

quantum gravity; black holes; holography; information; entropy; Robin boundary; gravitational waves; dark matter; dark energy; tensor networks; effective field theory; path integral

## License

* **Text & figures:** CC BY 4.0 (recommended).
* **Code snippets/scripts:** MIT (recommended).
  (Adjust to your preference before publishing.)

## Repro/Build

* LaTeX: `pdflatex` → `bibtex` → `pdflatex` ×2.
* Figures (optional): run `dct_qg_manifest_figures.py` (Python 3.10+, matplotlib; no external data).
* The manifest uses only standard LaTeX packages; macros are included inline or via the provided snippet.

## Related identifiers (add as available)

* arXiv preprint(s) for the follow-up papers (trigger, NPR, TDT, Infinity Bits, focused Raychaudhuri, EFT, tensor networks, phenomenology, dark sector).
* Repository link for data/scripts (e.g., GitHub).

## Notes

This is a **priority-establishing** release for a research program in progress. Some derivations are summarized at the manifest level and are fully developed in the subsequent papers referenced within.

**Contact:** add email/ORCID if you want on-record correspondence.
