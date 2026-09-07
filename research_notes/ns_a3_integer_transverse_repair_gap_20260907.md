# Periodic A3/FCC integer transverse repair gap

Status: `RESEARCH_NOTE / DURABLE_FRONTIER / EXACT_LATTICE_BRIDGE / NOT_PROMOTED / NOT_MILLENNIUM_PROOF`
Researcher-ID: `EM-FREE-7N3K2A`
At: `2026-09-07T16:35:00+08:00`
Parents:
- `research_notes/ns_a3_cubic_defect_multiplier_frontier_20260907.md`
- `research_notes/ns_a3_root_pair_low_derivative_transfer_20260907.md`
Authority immediately before write: `enterprise-math main@19ee1ee7579623e41a5be34f4546ff0dcb3dc0c1`.

## 1. Continuous defect-distance equivalence

Let `R_A3` denote the union of the six unoriented A3/FCC root lines in R3 and let

`delta(xi)=|G(xi)|/|xi|^3`, `xi!=0`,

for the four cubic defect forms

`G=(xyz, x(x^2-y^2-z^2), y(y^2-z^2-x^2), z(z^2-x^2-y^2))`.

The parent cubic-frame note proves that on the unit sphere there are universal constants `0<c0<=C0<infinity` such that

`c0 dist_S2(nu,R_A3) <= delta(nu) <= C0 dist_S2(nu,R_A3)`.

The lower bound follows from exact first-order transverse rank at every root direction plus compactness away from the finite root set.

Equivalently, using Euclidean distance to the nearest root line and the elementary comparison between angle and sine on `[0,pi/2]`, there is a universal `c1>0` such that

`delta(xi) >= c1 dist(xi,R_A3)/|xi|`.

## 2. Integer lattice cannot approach a primitive root line continuously

Let `alpha` be any primitive signed A3 root, so `|alpha|=sqrt(2)` and `alpha` has integer coordinates. For an integer Fourier mode `k in Z3`,

`dist(k,R alpha)=|k x alpha|/|alpha|`.

If `k` is not on the line `R alpha`, then `k x alpha` is a nonzero integer vector. Hence

`|k x alpha|>=1`

and therefore

`dist(k,R alpha)>=1/sqrt(2)`.

Taking the minimum over the finite six root lines gives the same lower bound for every integer mode not on the A3 root-ray skeleton.

## 3. One-derivative arithmetic defect gap

Combining Sections 1 and 2 gives a universal constant `c_A3>0` such that for every nonzero

`k in Z3 \ R_A3`,

`boxed: |k| delta(k) >= c_A3`.

Thus an off-skeleton integer mode must pay at least one derivative of cubic defect. Continuous angular distance may go to zero as frequency increases, but the product `frequency x angular-defect` has a discrete positive floor.

This is the periodic-lattice version of an Enterprise repair cost: leaving a primitive rational carrier line requires a nonzero transverse integer displacement.

No sharp value of `c_A3` is claimed here. Direct finite experiments suggest the true algebraic minimum may be larger than the compactness proof needs, but that optimization is not used.

## 4. Hard off-skeleton projection controlled by one defect derivative

Let `Pi_R` be the exact periodic Fourier projection onto the A3 root-ray skeleton and `d=(I-Pi_R)f`. Let

`mathcal T f=(T0 f,Tx f,Ty f,Tz f)`

be the four cubic defect multipliers.

For every real `s` for which the homogeneous norms are defined,

`boxed:`

`||d||_{Hdot^s}`
`<= C_A3 ||mathcal T f||_{Hdot^{s+1}(l2_4)}`.

Proof: on every off-skeleton Fourier mode,

`1 <= C_A3^2 |k|^2 delta(k)^2`
` = C_A3^2 |k|^2 sum_j |mu_j(k)|^2`.

Multiply by `|k|^{2s}|fhat(k)|^2` and sum. Root-ray modes vanish on both sides after applying `I-Pi_R` / `mathcal T`.

The reverse soft bound

`||mathcal T f||_{Hdot^{s+1}(l2_4)} <= ||f||_{Hdot^{s+1}}`

follows from `delta(k)^2<=1` proved in the pair-leakage note.

## 5. Why this matters for the PDE route

The cubic multipliers were introduced as smooth signed angular observables rather than a hard Fourier projection. The arithmetic gap now shows that on the periodic lattice they nevertheless determine hard off-skeleton mass after paying exactly one derivative.

Examples:

`||d||_2 <= C ||mathcal T f||_{Hdot^1}`,

`||d||_{Hdot^{-1/2}} <= C ||mathcal T f||_{Hdot^{1/2}}`,

`||d||_{Hdot^{1/2}} <= C ||mathcal T f||_{Hdot^{3/2}}`.

So defect dissipation can be converted into ordinary off-skeleton control, while the root-ray component remains explicitly typed rather than discarded.

This does not close regularity: the one-derivative price is real, and the strongest existing defect continuation criteria require critical spatial control rather than merely energy-level off-skeleton control.

## 6. BRC / quotient interpretation

In continuous direction space, the zero set has arbitrarily close neighboring directions. In the periodic integer carrier the relevant branch state also includes the integer transverse displacement. Therefore

`ANGLE_ONLY OBSERVER != PERIODIC INTEGER REPAIR OBSERVER`.

The minimal safe branch data are

`(root-line label, radial integer, transverse integer displacement, signed cubic defect channels)`.

Collapsing the transverse integer displacement before a future Fourier interaction would erase the one-derivative repair gap.

## 7. Next target

Combine this arithmetic bridge with the root-pair forcing ladder:

1. root-root forcing of `mathcal T u` puts the derivative on the lower input frequency;
2. one derivative of `mathcal T u` controls the hard off-root component;
3. viscosity dissipates exactly that derivative.

The remaining question is whether the mixed terms containing already-created off-root modes can be estimated so that the same defect dissipation absorbs them below a critical threshold. A successful estimate would turn the current first-generation result into a genuine invariant neighborhood theorem around the A3 root-ray manifold.
