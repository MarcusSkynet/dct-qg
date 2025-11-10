# DCT Notation and Conventions

This document provides a canonical reference for the notation, conventions, and terminology used throughout the Dimensional Collapse Theory (DCT) framework. It is intended as a guide for anyone exploring the papers and code in this repository.

## 1. Foundational Conventions

### Units and Physical Constants

Unless otherwise stated, we adopt **natural units** where the speed of light ($c$), the reduced Planck constant ($\hbar$), and the Boltzmann constant ($k_B$) are set to unity:
$$
c = \hbar = k_B = 1
$$
In these units, physical quantities are expressed in terms of Planck units. Newton's gravitational constant $G$ is related to the Planck length $\ell_{\mathrm{P}}$ by $G = \ell_{\mathrm{P}}^2$. We keep $G$ and $\ell_{\mathrm{P}}$ explicit in key formulas for clarity.

### Metric Signature

We use the **mostly-plus** metric signature $(-, +, +, +)$ in four dimensions and $(-, +, \dots, +)$ in a general $D$-dimensional spacetime.

### Dimensional Tagging

To avoid ambiguity, geometric objects are explicitly labeled with their dimensionality via a left superscript.
-   ${}^{(D)}X$: A quantity $X$ in the full $D$-dimensional spacetime (e.g., ${}^{(D)}R_{ABCD}$).
-   ${}^{(d)}X$: A quantity $X$ on the $d$-dimensional Ledger surface, where $d := D-2$ (e.g., ${}^{(d)}h_{ab}$).
-   ${}^{(2)}X$: A quantity related to the 2-dimensional normal plane.

Spacetime indices are denoted by uppercase Latin letters ($A, B, \dots$), while indices tangent to the Ledger are denoted by lowercase Latin letters ($a, b, \dots$).

## 2. Core Concepts and Definitions

### The DCT Triad ($\mathcal{L}, \mathcal{I}, \mathcal{T}$)

The core of DCT is built upon a triad of foundational concepts: the Ledger surface ($\mathcal{L}$), a universal curvature invariant ($\mathcal{I}$), and the Transdimensional Constant ($\mathcal{T}$).

-   **The Ledger ($\mathcal{L}$):** The Ledger is a physical, co-dimension 2 surface located inside the black hole's event horizon. It acts as a holographic screen where information is irreversibly recorded during "snap" events. Between snaps, it serves as a lossless, perfectly reflecting inner boundary.

-   **The Curvature Invariant ($\mathcal{I}$):** A "snap" is triggered when a local, dimensionless curvature measure reaches a universal threshold. For spherically symmetric spacetimes, this invariant is defined using the Kretschmann scalar ($K = R_{ABCD}R^{ABCD}$):
    $$
    \mathcal{I}(r) \equiv r^4 K(r)
    $$
    The snap occurs precisely when $\mathcal{I}$ hits the critical value $\mathcal{I}_{\mathrm{crit}}$.

-   **The Transdimensional Constant ($\mathcal{T}$):** This is a fundamental, dimensionless constant derived from first principles within the theory, which links geometry to information. Its value is:
    $$
    \mathcal{T} = \frac{1}{4\ln 2} \approx 0.3606
    $$
    This constant sets the universal snap threshold, $\mathcal{I}_{\mathrm{crit}} = 12 / \mathcal{T} = 48\ln 2$, and determines the Ledger's location. For a Schwarzschild black hole of radius $R_S$, the Ledger is found at:
    $$
    r_{\mathcal{L}} = \sqrt{\mathcal{T}}\,R_S \approx 0.6006\,R_S
    $$

### Thermodynamics and Information

DCT makes a clear distinction between thermodynamic entropy and information entropy, linking them only at snap events.

-   **Entropy Units:** All entropies are measured in **nats**. The conversion to bits is: $1 \text{ bit} = \ln 2 \text{ nats}$.

-   **Entropy Types:**
    -   **Thermodynamic Entropy ($S_{\mathrm{th}}$):** The Clausius entropy that appears in thermodynamic laws ($\delta Q = T\,dS_{\mathrm{th}}$) and area laws. The Bekenstein-Hawking entropy ($S_{\mathrm{BH}}$) and Ledger entropy ($S_{\mathcal{L}}$) are both types of $S_{\mathrm{th}}$.
    -   **Information Entropy ($S_{\mathrm{info}}$):** The Shannon or von Neumann entropy of a state or payload.

-   **"No Record Without Area" Principle:** Information can only be irreversibly recorded on the Ledger if accompanied by an increase in the Ledger's area. For each irreversible **payload bit** ($W$) written to the Ledger, the area increases by a discrete quantum:
    $$
    \Delta \mathcal{A}_{\mathcal{L}} = 4\ln 2\,\ell_{\mathrm{P}}^2
    $$

> #### Entropy Conventions and Relations in Detail
>
> -   **Definitions:** The thermodynamic entropies of the horizon and Ledger are defined by their respective areas:
>     $$
     S_{\mathrm{BH}} \equiv S_{\mathrm{th}}|_{\mathrm{H}} = \frac{A_H}{4G_D} \qquad \text{and} \qquad S_{\mathcal{L}} \equiv S_{\mathrm{th}}|_{\mathcal{L}} = \frac{A_{\mathcal{L}}}{4G_D}
     $$
>
> -   **Placement Law:** The area and entropy ratios are fixed by $\mathcal{T}$:
>     $$
     \frac{A_{\mathcal{L}}}{A_H} = \mathcal{T} \quad \implies \quad \frac{S_{\mathcal{L}}}{S_{\mathrm{BH}}} = \mathcal{T}
     $$
>
> -   **Snap (Write) Rule:** At the instant of a snap, the increase in the Ledger's thermodynamic capacity equals the information content of the payload being written:
>     $$
     \Delta S_{\mathcal{L}} = \Delta S_{\mathrm{info}} = \ln 2 \quad (\text{for one bit})
     $$
>     This is a *matching constraint*, not a general identity.
>
> -   **Cumulative Payload:** Assuming no information is erased, the total thermodynamic entropy of the Ledger tracks the total information written to it over time:
>     $$
     S_{\mathcal{L}}(t) = S_{\mathrm{info}}^{\mathrm{written}}(t) \quad \implies \quad S_{\mathrm{BH}}(t) = \frac{1}{\mathcal{T}} S_{\mathrm{info}}^{\mathrm{written}}(t)
     $$

### Mechanism and Dynamics (Snaps and NPR)

Snaps are realized geometrically through **Null-Pair Removal (NPR)**.

-   **NPR Projector:** At a snap, a 2-plane spanned by a pair of null vectors ($n_+^A, n_-^A$) is deleted from the spacetime. This is implemented by a projector $P$ which annihilates any component along these null directions. With the normalization $n_+ \cdot n_- = -1$, the projector is:
    $$
    P^A{}_B = \delta^A{}_B + n_+^A n_{-\,B} + n_-^A n_{+\,B}
    $$
    This operator is idempotent ($P^2=P$) and boost-invariant. It projects any tensor onto the $d$-dimensional tangent space of the Ledger.

-   **Dynamics:**
    -   **Between Snaps (Quiet Phase):** The Ledger acts as a lossless, perfectly reflecting inner boundary. Fields evolve unitarily according to a **real-Robin** boundary condition ($|\mathsf{R}|=1$). No information or energy crosses $\mathcal{L}$.
    -   **At a Snap:** The exterior quantum state is updated by a local, completely-positive, trace-preserving (CP-TP) map, and one irreversible payload bit is written to the Ledger.

### Infinity Bits ($W, X, Y, Z$)

Each snap event is characterized by a 4-bit register stored on a Ledger tile.
-   **Payload Bit ($W$):** The single **irreversible** bit of information ("write" bit) recorded during the snap. This is the only bit that contributes to the increase in the Ledger's entropy and area.
-   **Metadata Bits ($X, Y, Z$):** Three **reversible** bits that encode geometric metadata about the snap, such as the orientation and shear alignment of the deleted null plane. Changes to these bits do not cost area or entropy.

## 3. Dictionary of Symbols and Terms

### DCT-Specific Terminology

-   **Area Tick:** The minimal quantum of area ($\Delta \mathcal{A}_{\mathcal{L}} = 4\ln 2\,\ell_{\mathrm{P}}^2$) that the Ledger gains when one irreversible payload bit is written.
-   **Capacity:** The thermodynamic entropy of the Ledger ($S_{\mathcal{L}} = A_{\mathcal{L}}/(4G)$), representing its maximum information storage ability.
-   **Ledger:** A physical, co-dimension 2 surface inside a black hole that acts as a holographic memory, replacing the classical singularity.
-   **Null-Pair Removal (NPR):** The geometric mechanism of a snap, where a 2-plane spanned by two null vectors is deleted from the spacetime tangent space.
-   **Payload Bit ($W$):** The single bit of irreversible "write" information recorded on the Ledger during a snap.
-   **Real-Robin Boundary:** A type of boundary condition ($|\mathsf{R}|=1$) that ensures perfect reflection and unitary evolution. It describes the behavior of the Ledger between snaps.
-   **Snap:** A discrete, quantized event where spacetime locally loses two dimensions and records one bit of information on the Ledger, triggered when curvature reaches $\mathcal{I}_{\mathrm{crit}}$.
-   **Transdimensional Constant ($\mathcal{T}$):** The fundamental constant $1/(4\ln 2)$ that sets the ratio of the Ledger's area to the event horizon's area.
-   **Transdimensional Thermodynamics (TDT):** The set of laws governing the thermodynamic behavior of the Ledger, centered on the "capacity equals payload" principle at snaps.

### Symbol Glossary

| Symbol | Name / Meaning |
| :--- | :--- |
| **Foundational** | |
| $\mathcal{L}$ | The Ledger surface|
| $\mathcal{I}$ | The dimensionless curvature invariant ($r^4K(r)$)|
| $\mathcal{I}_{\mathrm{crit}}$ | Critical value of $\mathcal{I}$ that triggers a snap ($48\ln 2$)|
| $\mathcal{T}$ | The Transdimensional Constant ($1/(4\ln 2)$)|
| $\mathcal{J}$ | The "snap instrument" (a CP-TP map for the state update)|
| $\ell_{\mathrm{P}}$ | Planck length ($\sqrt{G\hbar/c^3}$)|
| $\ell_{\mathrm{P}}^2$ | Planck area ($G\hbar/c^3$)|
| $A_{\mathrm{P}}$ | Planck area (D-dim) (${G_D\hbar/c^3} $)|
| $W$ | The irreversible payload or "write" bit|
| $X, Y, Z$ | The reversible metadata (Infinity) bits|
| **Thermodynamics** | |
| $S_{\mathrm{th}}$ | Thermodynamic (Clausius/Gibbs) entropy|
| $S_{\mathrm{info}}$ | Information (Shannon/von Neumann) entropy|
| $S_{\mathrm{BH}}$ | Bekenstein-Hawking entropy of the event horizon ($A_H/4G$)|
| $S_{\mathcal{L}}$ | Thermodynamic entropy of the Ledger ($A_{\mathcal{L}}/4G$)|
| **General Relativity** | |
| $g_{AB}$ | The spacetime metric tensor|
| $h_{ab}$ | The induced metric on the Ledger|
| $R_{ABCD}$ | The Riemann curvature tensor|
| $K$ | The Kretschmann scalar ($R_{ABCD}R^{ABCD}$)|
| $\theta$ | Expansion scalar of a null congruence|
| $n_+, n_-$ | A pair of null vectors normal to the Ledger|
| $P^A{}_B$ | The Null-Pair Removal (NPR) projector|
| $R_S$ | The Schwarzschild radius ($2GM/c^2$)|
| $A_H, A_{\mathcal{L}}$ | Area of the event horizon and the Ledger, respectively|
| **Boundary Dynamics** | |
| $\mathsf{B}$ | The Robin boundary operator/parameter|
| $\mathsf{R}$ | The reflection coefficient (with $|\mathsf{R}|=1$ for a real-Robin boundary)|
| **Phenomenology** | |
| $\tau$ | Time delay of gravitational-wave echoes|
| $\varphi$ | Phase angle or phase shift|
| $M_{\mathrm{rem}}$ | Mass of a stable black hole remnant|
| $\omega_{\mathrm{gap}}$ | Minimum frequency (mass gap) for particle emission|
| $w_{\mathcal{L}}$ | Equation-of-state parameter for the Ledger as a dark energy fluid|