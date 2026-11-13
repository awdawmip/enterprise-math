# R695 — Exact contextual-return tomography on the full convex hull of E* directional BRC kernels

Date: 2026-11-10 (Asia/Shanghai). Status: AUTHOR-DERIVED / EXACT-COMPUTATION-CHECKED / UNREVIEWED / NOT ADMITTED.
Mother task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`; immutable publication `TP2-8B7E13C5904A2D6F1142`; formal owner at 2026-11-10 20:10 CST: `taskbook/unassigned`, `READY / NEEDS_DISPATCH`. No formal CLAIM is asserted.

## Provenance and bounded model

Science remains pinned to the task publication's `a72226e2430ffa4786321ac86e7f0c599d5f0389`, with no change to P000. The concrete labelled E* X6 returning-square BRC direction kernels are read from immutable R692C commit `3dacca5010104893d96301af4d61608d5a5a0879`, path `research_notes/portable_direct/R692C_ESTAR_MASK_RETURN_EXACT.js`, Git blob `0c6d51f99eac5903a30770c8c393c972a68d93ad`. R694 (commit `e26cce89ed74826642b1b8b990b7252d90cc3086`) proved a two-return probe separates **the finite 15-subset menu** at each root phase; this note studies every nonnegative rational *mixture* of the four direction kernels at each fixed phase.

Let the four original 15-path group counting kernels be (n_{a,j}(g)), (j=0,1,2,3), root phase (a\in\{0,1,2\}), (g\in S_3). For any rational coefficients (α_j\ge 0), not all zero, the explicitly labelled positive-BRC mixture is
[
 μ_{a,α}(g)=\frac{\sum_j α_j n_{a,j}(g)}{15\sum_j α_j}.
]
The macros preserve the chosen Cell, update the (S_3) frame, and carry four original direction-source tags before taking this declared group observer. The future continuation is chosen externally and independently of the first-macro source. The scalar observation after a fixed continuation law (ν) is the exact positive BRC return pairing
[
B_ν(μ)=(μ*ν)(e)=\sum_{g\in S_3}μ(g)ν(g^{-1}).
]
This is algebraic tomography of that observer; the port/source tags must remain available for later native operations until their quotient is separately certified.

Denote (e=012,,t=021,,c=120,,c^{-1}=c^2=201). Write (ν_{a,m}) for the uniform direction-mask `m` continuation, where singleton mask `1` selects (j=0) and mask `4` selects (j=2).

## Theorem R695-A — Globally exact reconstruction throughout the rational mixture families

For every (α\in\mathbb{Q}_{\ge0}^4\setminus\{0\}), each of the following observer signatures uniquely determines the **entire** first-step group law (μ_{a,α}).

**Phase 0.** Every allowed mixture has (μ(e)=2/5). Put (x=μ(t)), (y=μ(c)), (z=μ(c^2)=3/5-x-y), and measure
[
 A=B_{ν_{0,1}}(μ),quad B=B_{ν_{0,4}}(μ).
]
The two immutable continuation kernels give
[
 A=4/25+3x/5,qquad B=4/25+x/5+2y/5.
]
Consequently
[
 x=\tfrac53(A-4/25),quad
 y=\tfrac52(B-4/25-x/5),quad z=3/5-x-y.
]
The measurement Jacobian on the affine coordinates ((x,y)) has determinant (6/25\ne0).

**Phase 1.** Every allowed mixture is supported on ({e,c,c^2}). Put (r=μ(e)) and (B=B_{ν_{1,1}}(μ)). Because (ν_{1,1}=(6e+6c+3c^2)/15),
[
 B=2/5-μ(c)/5.
]
Thus (μ(e)=r,quadμ(c)=2-5B,quadμ(c^2)=5B-1-r).

**Phase 2.** Every allowed mixture is supported on ({e,t}). The one-step return (r=μ(e)) already reconstructs (μ(t)=1-r).

The proof is exact substitution into the four original 15-path kernels. The reconstruction is valid for any rational nonnegative mixture coefficients, including boundary faces and zero coefficients. The identities also hold for real convex coefficients as algebraic statements.

## Theorem R695-B — Minimum scalar return-observation counts

The three mixture polytopes have affine dimensions (2,2,1), respectively. For phase 0 this follows from the independent differences of directional vertices (j=1,2) relative to (j=0); for phase 1 the same two differences are independent; for phase 2 all vertices lie on the segment supported by (e,t).

For any fixed suffix sequence of independently chosen future group kernels, the return probability remains a **single affine-linear functional** of the unknown first kernel (μ), by BRC convolution associativity and linearity. A family of (k<d) fixed nonadaptive scalar return experiments therefore has a nonzero kernel on a (d)-dimensional affine hull, and two nearby interior mixtures have identical measurements. Hence at least (d) such scalar observations are required to reconstruct every point of the family. Theorem A attains this lower bound.

Explicit minimal designs: phase 0 needs **two** two-macro return probes (masks 1 and 4), since one-step return is constant; phase 1 needs **one** one-step return and **one** two-macro probe (mask 1); phase 2 needs **one** one-step return. These are lower bounds within fixed, nonadaptive, scalar return-probability observations and complete first-kernel recovery.

## R695-C — Exact witness separating finite-menu injectivity from continuum injectivity

R694 showed that mask 3 by itself distinguishes 13 **discrete** distinct laws in phase 0. Now take
[
μ=ν_{0,2}=(2e+2t+c)/5,quad
μ'=\tfrac38ν_{0,1}+\tfrac58ν_{0,4}
       =2e/5+7t/20+c^2/4.
]
Here (ν_{0,2}) denotes discrete mask `2` (direction (j=1)); mask `4` denotes direction (j=2). These laws are different, but
[
μ(e)=μ'(e)=2/5,qquad
B_{ν_{0,3}}(μ)=B_{ν_{0,3}}(μ')=9/25.
]
The continuation-mask-1 return separates them by exactly (3/100). This witnesses the need for a second probe when continuously mixing direction sources, even though one probe was sufficient on the finite mask menu.

## Executed exact checker and next problem

The attached `R695_CONTINUOUS_PROBE_TOMOGRAPHY.py` uses original R692C integers and Python standard-library `Fraction`; it checked all 45 discrete masks, all 675 within-phase ordered discrete pairs, and all 1,482 nonnegative integer coefficient quadruples with total mass (1\le\sum_j\alpha_j\le8) across the three phases (494 per phase), plus the exact continuum-fiber witness. Output: `R695_ALL_EXACT_ASSERTIONS_PASS`. These finite computations independently verify the program's reconstruction formulas; Theorems A/B hold on the full declared coefficient families by their algebraic proofs.

Applied BRC interface: labelled positive path-count kernels and exact group convolution, with source and observer scope explicit. Reuse status: `REUSE_APPLIED` R692C original kernels; `COMPOSE_APPLIED` R694 contextual pairing. This is a model-internal author proof, not an independent review or native Result/Working Truth admission.

Next independent unit: reconstruct the **reachable** test-observation row span under actual pinned X6 Link/Port, V29 PASS/TRANSFER and V39 update permissions. Determine whether legal suffix event streams realize two independent phase-0 contextual probes, one phase-1 probe, and the phase-2 return observer; if fewer are reachable, compute a minimal port/source repair coordinate. Keep the mother task's primitive triad Cell/path law, rotation covariance, and genuine V29/V39 semantics open.