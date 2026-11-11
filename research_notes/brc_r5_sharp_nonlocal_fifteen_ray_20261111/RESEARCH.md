# R5 — an exact sharp fifteen-atom ordering on a maximal feasible hidden-fiber ray

Date: 2026-11-11 (Asia/Shanghai). Scope: **frozen P/Q–BRC Blackwell auxiliary transport fiber**, not native X6 dynamics. Status: author-side exact arithmetic and finite certificate; independent review/Source Result pending.

## Input, source and observer

Frozen scientific provenance remains GLOBAL `a01383f825ef9d43b4b754254303298c64041568` and Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Continue the previously verified R5 [PR #2098](https://github.com/awdawmip/enterprise-math/pull/2098), immutable evidence commit `550a28515d92c0da1a89b0edcb060f113240ca27`, rather than rebasing mathematical inputs. The code below reproduces its exact full-support initial transmission by listing all 28 fractions and tests the same frozen observation vector against the earlier endpoint `C`.

There are targets `0..6`, source ports `j ∈ {1,2,3,5}`, likelihood numerators `R=(2,10,15,20,25,30,38)`, and 28 dynamic nonnegative masses `E(i,j)`. The full observer includes seven target-sum constraints, four source totals and four source first-moment constraints (15 displayed equalities of rank 13). The omitted two singleton arcs are fixed by the frozen model. All named ports and exact target labels are retained. The operation `H_j(v)` adds `v` at source 3 and `-v` at compensator `j ∈ {1,2,5}`; the three-target vector `v` has `Σv=ΣR_iv_i=0`. One elementary operation changes one compensator port and source 3, touching three target labels.

## Theorem 1 — global interior connectivity with a quantitative finite word bound

Let `X,Y` be **strictly positive** 28-vector transmissions in the same exact observer fiber, with identical complete source-3 rows. Then there is a finite **strictly positive** intermediate-state path from `X` to `Y` using only the specified elementary six-arc atoms. A fully explicit algorithm and bound depend only on their 28 exact coordinates.

For `i=1..5` define `h_i` by `h_i(0)=R_i-R_6`, `h_i(i)=36`, `h_i(6)=R_0-R_i`, zero elsewhere. These five vectors form a basis of the five-dimensional `K={w:Σw=ΣR_iw_i=0}`. Put `d_j(i)=Y(i,j)-X(i,j)`. Then the 15 ordered moves
`M_(j,i)=(d_j(i)/36)(+h_i at j, -h_i at 3)`
sum exactly to `Y-X`: the sum of the three port-local vectors is zero by target conservation and the unchanged source-3 row.

Set `D=Y-X`, `B=max_k Σ_(j,i)|M_(j,i)[k]|`, and `m=min_k{X[k],Y[k]}>0`. Choose
`N_safe=max(1,ceil(2 B/m))`. Subdivide the straight segment into `N_safe` equal intervals, applying all 15 moves scaled by `1/N_safe` on every interval. A visited point equals
`X+(r/N_safe)D+(1/N_safe)Σ_(ℓ≤t)M_ℓ`.
Its every coordinate is at least `m-B/N_safe≥m/2>0`, and every atom lies in the exact observer kernel. Thus the algorithm uses at most `15 N_safe` legal steps (omit zero moves).

For an arbitrarily chosen **fixed order** `M_1,...,M_15`, this repeated-equal-subdivision method has a **sharper exact necessary-and-sufficient** positive-step criterion. Let `P_t=Σ_(ℓ≤t) M_ℓ`. Define
`T=max(0,{-P_t[k]/X[k]: D[k]≥0, P_t[k]<0},{(D[k]-P_t[k])/Y[k]: D[k]<0, P_t[k]<D[k]})`.
Then the **smallest integer subdivision count making every intermediate coordinate strictly positive** is `N_strict=max(1,floor(T)+1)`. Indeed, over `r=0,...,N-1`, the coordinate minimum occurs at `r=0` when `D[k]≥0`, and at `r=N-1` when `D[k]<0`. The two displayed ratio families are exactly the resulting strict positivity inequalities. This establishes a verifiable upper-bound algorithm across the entire full-support hidden fiber without assuming a global 15-step theorem.

## Theorem 2 — an entire maximal endpoint ray has exact legal distance fifteen

Take exactly the positive `X` listed in `VERIFY_R5_SHARP_RAY.py`, which the verifier checks against the frozen `C` observation. For compensator ports `j=1,2,5`, prescribe their five coordinates (target labels 1..5) as
`c_1=(12,8,1,13,8)`, `c_2=(3,13,7,4,2)`, `c_5=(-15,-21,-8,-17,-10)`.
They sum componentwise to zero. Define
`D=Σ_(j∈{1,2,5},i=1..5) (c_j[i]/36) (+h_i at j,-h_i at 3)`.
Then `AD=0`, `D(.,3)=0`, and `D≠0`. The **complete maximal feasible nonnegative endpoint ray** is
`Y(ε)=X+εD`, `0≤ε≤ε_max=9/115400000`.
The endpoint is strictly positive for `0≤ε<ε_max`, reaches its first zero coordinate at `ε_max`, and is infeasible for every larger `ε`.

The original lexicographic port-major order `(1,1)..(1,5),(2,1)..(2,5),(5,1)..(5,5)` loses intermediate nonnegativity at
`ε_sorted=155682221/377131868400000000 < ε_max`.
A different **fixed explicit permutation of precisely the same 15 atoms** is feasible all the way to `ε_max`:
```
(2,2), (1,2), (1,3), (2,3), (2,5),
(5,4), (1,4), (5,5), (2,4), (1,5),
(5,1), (2,1), (5,3), (1,1), (5,2).
```
The exact verifier checks all 16 states at `ε_max` are nonnegative and in the same observer fiber. Every prefix is affine in `ε` and starts at a strictly positive `X`; hence each intermediate state is **strictly positive** for all `0≤ε<ε_max`. It is nonnegative at the boundary.

**Sharpness:** For each port, the indicated coefficient vector does not belong to the span of any four of the 35 three-target atom directions. The executable finite-field certificate enumerates all `C(35,4)=52360` subsets, obtaining 46,198 rank-four sets, 6,162 lower-rank sets and 3,468 distinct hyperplane normals over prime `p=2147483647`. Every normal has nonzero modular dot product with each of the three coefficient vectors. Because all 4×4 minors of the integer atom dictionary have absolute value at most `4!36^4<p`, modular rank four is equivalent to rational rank four. A nonzero modular dot product proves rational non-membership. Any algebraic atom decomposition must therefore use at least five atoms **at each of the three distinct compensator ports**. Positive scaling by `ε` preserves that lower bound. The above 15-step legal path achieves it:

**For every real `0<ε≤9/115400000`, the exact legal elementary-atom distance `d_BRC(X,Y(ε))=15`.**

This proves a nonlocal, full endpoint ray of sharp fifteen-step transfers, including a boundary endpoint. It also gives a concrete instance where operation **ordering**, rather than adding residual atoms, restores positivity across the entire feasible ray.

## Evidence, limitations and next mathematical unit

Run `python3 VERIFY_R5_SHARP_RAY.py`; `EXACT_OUTPUT.txt` contains the captured actual output. Verification uses Python standard-library exact `Fraction` and finite integer/modular computations, no tolerance or non-frozen observer. The single explicit permutation was found through bounded heuristic search, but its *proof and certificate are exact* and independent of that search procedure.

Theorem 1 proves finite legal connectivity for arbitrary strictly positive hidden-fiber endpoint pairs with an explicit endpoint-dependent length bound. Theorem 2 proves exact 15-step length along the stated maximal ray. **Unresolved:** whether every positive endpoint pair in this fiber always admits some legal 15-step atom permutation/decomposition, or there exists a pair whose minimum exceeds 15. An immediately executable next unit is to search endpoint directions whose available five-atom bases force incompatible source-3 prefix margins; use rational LP/MILP or exact Farkas certificates to distinguish a true >15 lower bound from failure of a chosen ordering.

Owner/authority: authored as independent R5 continuation. No other task's active CLAIM changed, and no P000/native X6 theorem, formal Source Result or independent review is asserted.
