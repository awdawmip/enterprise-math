# R5: Complete four-dimensional Blackwell coupling polytope and exact atlas-escape gap

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / INDEPENDENT_REVIEW_PENDING / NOT_ADMITTED.

## Exact science and provenance

Continue [PR #1856](https://github.com/awdawmip/enterprise-math/pull/1856) at immutable commit `5af6934e25289a6a229747b859b9c4baf507f22a`, with its seven LR nodes, FULL_HIST physical mass map, fixed source X, seedless target Y, 16-edge atlas S, dual vector and 13-edge feasible coupling P. The predecessor dual certificate is in [PR #1855](https://github.com/awdawmip/enterprise-math/pull/1855). Frozen science/task pins remain GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Current normative rules were read independently.

All results below concern **this one exact marginal pair and every feasible nonnegative Blackwell coupling** for it. They do not claim a uniform all-physical-strategies 14-edge bound. The static likelihood-ratio/coupling model is typed as an auxiliary statistical observer, not the native six-dimensional X6 spatial basis.

Source and seedless target physical flows:

```
X = (999/1000,1/6,999/1000,1/20,29/240,11/160,1/120)
Y = (1,2002911/10904720,26095487/40892700,442758619/6542832000,
     11037627/68154500,394502727/2180944000,2002911/109047200)
r = (1/10,1/2,3/4,1,5/4,3/2,19/10)
```

With `nu=M(X)`, `mu=M(Y)`, an edge `E_(i,j)` carries source index j to target index i; 21 equations are seven row sums `mu_i`, seven column sums `nu_j`, and seven LR moments `r_j nu_j`. The `g=b` source has `nu_4=0`; extremal columns 0 and 6 only carry `(0,0)` and `(6,6)`, leaving 30 candidate edges. The target has `mu_1=0`.

## Theorem 1 — exact universal 17-edge support restriction

Define
```
Phi(mu,nu) = (23/5)(mu_0-nu_0)+3(mu_1-nu_1)
             +2(mu_2-nu_2)+(mu_3-nu_3).
```
Evaluate this linear functional on each edge's 21-vector `a_(i,j)`: **all 30 prices `Phi(a_(i,j))` are nonnegative**, and on these fixed marginals `Phi(mu,nu)=0`. Since `E>=0`, every positive-price edge must have zero mass. The additional zero target mass `mu_1=0` removes all edges entering row 1. Exactly the following 17 edges remain:
```
Z = {(0,0),(0,1),(2,1),(3,1),(4,1),
     (0,2),(2,2),(3,2),(4,2),
     (0,3),(2,3),(3,3),(4,3),
     (4,5),(5,5),(6,5),(6,6)}.
```
Each edge in Z is *potentially* positive: Theorem 2 supplies a single feasible coupling strictly positive on all 17. This support restriction is exact for **all** nonnegative couplings, regardless of the atlas-escape objective.

## Theorem 2 — complete four-dimensional affine parametrization

Let P be the predecessor's exact 13-positive-edge coupling, fully reproduced in `VERIFY.py`. Put
```
q1 = E_(2,1),  q2 = E_(3,1),  q3 = E_(3,2),  q4 = E_(2,3).
E(q) = P + q1 V1 + q2 V2 + q3 V3 + q4 V4.
```
Each `Vk` has coefficient +1 at its new q edge and the following compensating coefficients on P's support:

| Kernel direction | Compensating edge coefficients |
| --- | --- |
| V1 | (0,1):-10/23, (4,1):-13/23, (0,2):+10/23, (2,2):-1, (4,2):+13/23 |
| V2 | (0,1):-5/23, (4,1):-18/23, (0,3):+5/23, (3,3):-1, (4,3):+18/23 |
| V3 | (0,2):-5/23, (4,2):-18/23, (0,3):+5/23, (3,3):-1, (4,3):+18/23 |
| V4 | (0,2):+10/23, (2,2):-1, (4,2):+13/23, (0,3):-10/23, (4,3):-13/23 |

Exact rational rank of the 21×13 P-edge columns is 13; rank of all 21×17 Z columns is also 13. Each `Vk` is an explicit kernel vector; the four are independent because their coordinates on the four newly named edges form the identity. Therefore **every equality solution supported on Z** has one and only one such q representation.

The *entire* nonnegative coupling polytope is exactly
```
Q = {q in R^4 : q1,q2,q3,q4 >= 0,
     P_e + sum_k qk Vk,e >= 0  for every P-support edge e}.
```
This is an exact finite rational H-representation. The point `q=(1/1000000,1/1000000,1/1000000,1/1000000)` makes all **17** edge weights at least `1/1000000`. All 21 equations hold exactly. Thus `dim(Q)=4`, and the full 17-edge support is physically feasible for these marginals.

## Theorem 3 — exact cost gap and complete optimal face

Reuse the exact predecessor dual, whose value on these margins is
```
c = 225713944957/3385915560000.
```
The dual reduced costs on the four new edges are respectively `0,28/23,5/23,13/23`; all P-support edges are dual-tight. Hence for **every feasible coupling** of this marginal pair:
```
epsilon_S(E(q)) = c + (28/23)*q2 + (5/23)*q3 + (13/23)*q4.
```
Because `q2,q3,q4>=0`, the exact minimizers are and only are `q2=q3=q4=0`; the remaining edge nonnegativity inequalities are equivalent to
```
0 <= q1 <= 3997/390000.
```
The two endpoints have 13 positive edges; strict interior points have 14. The all-17-positive rational witness at `qk=1/1000000` has cost **exactly `c+1/500000`**. This identifies one zero-cost coupling residual coordinate `q1` and three strictly cost-bearing residual coordinates.

## Product with the full physical observation fiber

The predecessor's observer kernel `K=(-49400/295513,-49400/295513,-49400/295513,-33345/591026,132145/295513,-33345/591026,1)` leaves the seven source masses and two stop times unchanged for
```
-295513/49400000 <= h <= 295513/36054360.
```
Consequently the exact Cartesian product of that complete **one-dimensional physical-flow fiber** and the complete **four-dimensional coupling polytope Q** is a five-dimensional legal *physical-flow × coupling* family with fixed observer and fixed seedless target. The fiber and coupling residual coordinates remain separately typed.

## Verification, boundary and next discriminating step

`VERIFY.py` (Python standard library `Fraction`) repeats all fixed masses, physical capacity and stop-time checks, all 30 Phi edge prices, the exact Phi saturation, support elimination, both ranks, all four null directions, all 21 coupling equations, the strict 17-edge witness, all reduced costs and gap equation, and the original optimal segment and physical fiber. `EXACT_OUTPUT.txt` records the actual execution output. Universal conclusions follow from exact linear equalities and nonnegativity.

**Next:** construct lawful physical marginal perturbations across the zero-Phi face and derive the corresponding variable-support 14-edge charts. The live all-physical 14-vs-15-edge question remains open. This proof is an author-side checkpoint pending independent review; no formal Task CLAIM, Result or admission is asserted.
