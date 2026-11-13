# PREFIX-624 — Exact rank bifurcation of the original X6-BRC one-step endpoint and tagged-action observers

**Date:** 2026-11-09 (Asia/Shanghai). **Status:** author-side exact proof and reproducible rational-arithmetic evidence; independent mathematical Driver review pending.

**Scientific pin:** `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. The original native STAR phase/action enumerator is reused from [PREFIX-623](https://github.com/awdawmip/enterprise-math/pull/1864) at immutable commit `0ccdeea6c7b5ab9d1ac833990ce6eb40d4db18a6`. Current behavioral rules were read separately at Source `main@a3ead6603a0aeeafb552fb98f60b296587125edb` and account knowledge `main@7f3bb303e607416b611c1e69819e5eb38da5157d`. P000, X6/Heartbeat typing, original six weights and the frozen scientific operator are unchanged.

## Exact observer and scope

The population is an arbitrary **nonnegative original 96-port predecessor state** (r\in\mathbb R_{\ge0}^{96}); this is a linear-algebraic enlargement beyond PREFIX-623's restricted four-point reachable family. Its original 48 STAR phases are enumerated from
```
(1,3,6), (1,4,5), (2,3,5), (2,4,6)
```
with six original axis weights `(1,1,1,1,0,0)`, special source phase $G=4$, and 576 action labels `(i,j,u,v)` determined by the native `neighbors(i)` relation. The only gate-dependent action is (j=4,u=v=1), with weight $z\ge0$; every other action carries its original destination-axis weight. This is the native positive BRC action algebra, not a classical surrogate evolution.

Write (A(z)\in\mathbb R_{\ge0}^{96\times96}) for the destination-summed original transition. Write (J(z):\mathbb R^{96}\to\mathbb R^{576}) for the full **source-identified labelled action-flow** operator:
$$
 (J(z)r)_{i,j,u,v}=w_{i,j,u,v}(z)\,r_{2j+v}.
$$
Summing the labelled action coordinates by destination gives (A(z)r). All ranks below are over exact rational/real linear spaces; $z\ge0$ is an exact rational or real gate.

## Theorem 624.1 — a rank drop exactly at the symmetric gate

For the original 96-port BRC transition:
$$
\boxed{
 \operatorname{rank}A(z)=
 \begin{cases}32,&z=1,\\33,&z\ge0,\ z\ne1.\end{cases}
}
$$
The 48 native source phases split into **32 live** and **16 silent** phases; the original 32 silent phases have both source-bit columns zero. The live source-phase indices, in the original zero-based phase order, are
```
[0,2,4,6,8,9,10,11,12,14,16,18,20,21,22,23,
 24,26,28,30,32,33,34,35,36,38,40,42,44,45,46,47].
```
For every live phase except $j=4$, the two columns (A(z)e_{2j},A(z)e_{2j+1}) are identical for every $z\ge0$. For the gate $z=1$ this equality holds at $j=4$ too. Therefore the upper rank bounds are 33 and 32 respectively.

**Complete exact lower-rank certificate.** For the 32 even source-port columns `C32=[2*j for j in live_phases]`, the 32 native destination rows
```
R32=[0,2,4,6,8,10,12,14,24,26,28,30,32,34,36,38,
     48,50,52,54,56,58,60,62,72,74,76,78,80,82,84,86]
```
give
$$
 \det A(1)[R32,C32]=6561=3^8.
$$
Add the special odd source port 9: `C33=C32+[9]`. The 33 rows
```
R33=[0,2,4,6,7,8,10,12,14,24,26,28,30,32,34,36,38,
     48,50,52,54,56,58,60,62,72,74,76,78,80,82,84,86]
```
give the exact **symbolic** determinant
$$
 \boxed{\det A(z)[R33,C33]=6561(z-1)}.
$$
For this minor, only source column 9 depends on (z), so the determinant is affine in (z). The exact integer determinants at $z=0$ and $z=1$ are respectively (-6561) and (0), proving the displayed identity for every (z). A separate exact check at $z=2$ returns (6561). Together with the upper bounds, this proves the rank formula. In particular (A(1)-A(0)) has rank 1 and precisely three nonzero entries.

## Theorem 624.2 — exact labelled-flow rank and sharp linear repair dimension

For every $z\ge0$,
$$
 \boxed{\operatorname{rank}J(z)=64}.
$$
Indeed, each of the 64 bit ports belonging to a live phase has at least one strictly positive outgoing original typed action, even at $z=0$. Each labelled action has **one explicitly identified source port**. Consequently the 64 nonzero columns of (J(z)) have disjoint labelled-coordinate supports and are linearly independent; the other 32 columns are zero.

Given only the complete **current** 96-port endpoint (y=A(z)r) and the gate (z), to reconstruct **all 576** labelled action flows of an arbitrary nonnegative predecessor (r), the minimal number of additional **linear scalar predecessor observations** is
$$
\boxed{
 k_{\rm extra}(z)=\operatorname{rank}J(z)-\operatorname{rank}A(z)
 =\begin{cases}32,&z=1,\\31,&z\ge0,\ z\ne1.\end{cases}
}
$$
**Lower bound:** The 64-dimensional live source-port space contains an interior of the nonnegative cone. On it (J(z)) is injective while (A(z)) has rank 32 or 33. Any (m)-coordinate additional linear observation can raise joint rank by at most (m). Thus (m\ge64-\operatorname{rank}A(z)); sufficiently small positive perturbations of any kernel vector also give distinct nonnegative witnesses.

**Constructive upper bound:** For $z=1$, read the 32 odd source-bit coordinates `r[2*j+1]` for every live phase (j). Subtract their known contributions from the 32 destination rows R32; the invertible 32×32 submatrix reconstructs all 32 even live coordinates. For $z\ne1$, read the 31 odd source-bit coordinates for live (j\ne4). Subtract their contributions from R33; the invertible 33×33 submatrix reconstructs all 32 live even coordinates **and** special odd port 9. In both cases, all 64 live predecessor ports are recovered, so the 576 labelled flows follow exactly. Silent predecessor ports do not enter any action flow and need no reconstruction.

This is a **linear-supplement observer theorem** on the full 96-port nonnegative input domain, for a declared one-step labelled-flow query. PREFIX-623's one-scalar repair pertains to its much narrower two-step-reachable four-point-probe family **when the predecessor phase observer is already supplied**. Both statements hold in their respective domains.

## Reproducibility and checks

Companion script `PREFIX624_native_action_rank_checker.py` reconstructs the original STAR graph, 576 native typed actions and exact 96×96 transition matrices. Its SymPy exact integer/rational assertions verify the two determinant certificates and the third $z=2$ determinant, the rank-1 gate perturbation, all silent/live source columns, labelled-action positivity at (z=0,1,2,7/3), and the rank formula. It additionally reconstructs all 576 labelled flows from endpoint-plus-minimal-odd-port observations for **12 positive rational predecessor inputs** (four gates × three independently specified input vectors). All assertions passed; raw details and minor row/column sets appear in the companion results JSON. The universal claims follow from the exact symbolic argument and rank certificates rather than the 12 tests.

## Next smallest research unit

Use the actual restricted post-two-step X6 four-point accessible family to calculate the rank of the **two-consecutive-ancestor** tagged-history observer, conditioning precisely on which ancestral phase vectors, gates and intermediate ports are already provided. Derive a minimum repair-coordinate count that preserves this larger path query; compare it with the present full-domain 31/32 and earlier restricted-domain one-scalar results. Preserve tagged provenance until a scope-typed observer factorization is proved.

**Control provenance:** author-side science, not a formal CLAIM, native Result or mathematical acceptance; Owner/session inquiries are separate from the durable manuscript. No change to P000 or protected worldview.
