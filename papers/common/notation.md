# Notation and Conventions

### Units and signature
We use natural units $c=\hbar=k_{B}=1$. Planck length $\ell_{\mathrm P}$ is kept explicit.  
Unless stated, $G$ is explicit in geometric identities and set to $1$ in back-of-the-envelope estimates.  
Metric signature is $(-,+,+,+)$ in 4D, and $(-,+,\dots,+)$ in $D$ dimensions.  

Curvature conventions:

$$
R^{a}{}_{bcd} = \partial_{c}\Gamma^{a}_{bd} - \partial_{d}\Gamma^{a}_{bc}
                 + \Gamma^{a}_{ce}\Gamma^{e}_{bd} - \Gamma^{a}_{de}\Gamma^{e}_{bc}, \qquad
R_{ab}=R^{c}{}_{acb}.
$$

### Dimensional tags
We mark the dimension of geometric objects with *left* superscripts in parentheses:

$$
{}^{(D)}G_{AB},\quad {}^{(D)}\nabla,\quad {}^{(D)}\Box, \quad {}^{(d)}R_{ab},\quad {}^{(2)}\epsilon_{\perp\,ab}.
$$

Here $D$ is the ambient spacetime dimension and $d:=D-2$ is the ledger dimension.  
Indices $A,B,\dots$ are ambient; $a,b,\dots$ live on the ledger $\mathcal L$; the normal two-plane is denoted by ${}^{(2)}(\cdot)$.  
Right superscripts are reserved for powers, perturbative orders, or labels unrelated to dimension.

### DCT triad and invariants
We use the calligraphic triad $(\mathcal L,\mathcal I,\mathcal T)$:

$$
\mathcal L \ \text{(ledger surface)}, \qquad
\mathcal I(r) \equiv r^{4} K(r), \ \ K=R_{abcd}R^{abcd}, \qquad
\mathcal T = \frac{1}{4\ln 2}.
$$

The universal snap threshold is

$$
\mathcal I_{\mathrm{crit}} = 48\ln 2 = \frac{12}{\mathcal T},
$$

fixing, for Schwarzschild, the ledger placement $r_{\mathcal L} = \sqrt{\mathcal T}\,R_S$ (axisymmetric generalizations use the canonical slice).

### Thermodynamics and information
All entropies are in *nats*.  
Ledger entropy $S_{\mathcal{L}}=A/(4\ell_{\mathrm P}^{2})$.  

At a snap, the capacity–payload equality holds,

$$
\delta S_{\mathcal{L}} = \delta S_{\mathrm{info}},
$$

and one *irreversible payload bit* costs

$$
\Delta A_{\text{one bit}} = 4\ln 2\,\ell_{\mathrm P}^{2}.
$$

Reversible geometric metadata $(X,Y,Z)$ (the *Infinity Bits*) do not change von Neumann entropy.  
We summarize this ethos as: *no record without area*.

### Mechanism and dynamics
Snaps are *Null–Pair Removal* (NPR) events: if $n^{A}_{\pm}$ span the deleted null 2-plane with $n_{+}\!\cdot n_{-}=1$,

$$
P^{A}{}_{B} = \delta^{A}{}_{B} - n_{+}^{A}n^{-}_{B} - n_{-}^{A}n^{+}_{B}
$$

projects to the ledger-orthogonal data; local $SO(1,1)$ boosts in the deleted plane are gauge.  

Transport across $\mathcal L$ is permitted only during snaps.  
Between snaps, the ledger imposes a *real* Robin boundary (lossless, $|\mathsf R| = 1$), so evolution is unitary.  
At a snap, the open system updates via a localized CP–TP instrument and writes the irreversible payload bit to $\mathcal L$.

### Bits vs. nats
We write information in nats; $1$ bit $= \ln 2$ nats.  
When convenient, we annotate payload in bits and convert via $\ln 2$.

### Default dimension
Unless a left superscript is shown, quantities are $D=4$.  
We tag ${}^{(D)}(\cdot)$, ${}^{(d)}(\cdot)$, or ${}^{(2)}(\cdot)$ only when comparing across dimensions or when a quantity lives intrinsically on $\mathcal L$ or on the normal two-plane.
