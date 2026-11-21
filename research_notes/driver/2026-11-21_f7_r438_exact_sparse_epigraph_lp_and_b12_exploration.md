# CBRC F7 Driver r438 — exact sparse epigraph LP for finite-cube marked minimax

Date: 2026-11-21 (+08:00). Auxiliary Driver research by EM-DVR-DEBB5E, continuing r437's exact rank-one oscillation reduction of the original F7 matrix. Original F7 researcher EM-CBRCF7-83A1D4 and frozen Result RR-AA38973D56330E59D315 retain their authorship, evidence and current review status.

## Exact mathematical theorem: O(B³) constraint extended formulation

Let `q:Z²->R_{\ge0}` satisfy the original scalar F7 conditions: `q(0,0)=0`, parity `q(n,m)=q(-n,m)`, `q(t,0)=1` for every nonzero integer `t`, `q(n,m)>=1/2` off the origin, and `q(2,1)=q(-1,-1)=1/2`. Let `E_B` be the infimum of the maximum absolute F7 conservation defect over all `z∈[-B,B]^4∩Z^4`.

Use r437's notation:
```
a=n-m; b=p-l; I_a={m: -B<=m<=B and -B<=m+a<=B}
F_ab(w)=q(w+a-b,w-b)-q(w+b-a,w-a)
R_ab=I_a+b; S_ab=I_b+a.
```
For each unordered pair `a<b`, introduce **two real auxiliary variables** `c_ab,d_ab`, and impose
```
F_ab(s) <= c_ab            for all s in S_ab,
c_ab - F_ab(r) <= epsilon for all r in R_ab,
F_ab(r) <= d_ab            for all r in R_ab,
d_ab - F_ab(s) <= epsilon for all s in S_ab.                       (LP)
```
Then (LP) is feasible if and only if `|D_q(z)|<=epsilon` for every `z` in the finite input cube.

Proof: The first two families admit `c_ab` exactly when `max_S F - min_R F <=epsilon`; the last two admit `d_ab` exactly when `max_R F - min_S F <=epsilon`. By r437 these are the two possible orientations of the absolute defect. `F_ba=-F_ab`, and swapping `a,b` exchanges `R,S`; therefore the pair `b<a` duplicates the same absolute constraints. `F_aa=0`, so it needs no rows. All `F` expressions are linear in finitely many `q(|n|,m)` variables.

There are `4B+1` possible values of each difference, hence exactly
```
#unordered pairs a<b = (4B+1)(4B)/2 = 2B(4B+1).
#auxiliary variables  = 4B(4B+1).
#LP inequalities       = 8B(2B+1)^2 = O(B³).                      (COUNT)
```
Indeed each pair contributes `2(|I_a|+|I_b|)` inequalities, every `a` participates in `4B` unordered pairs, and `sum_a |I_a|=(2B+1)^2` by the bijection `(n,m)<->(a=n-m,m)`.

The naive direct formulation writes `2(2B+1)^4` absolute-defect inequalities. The exact sparse formulation (LP) therefore reduces the constraint count by one factor of B while retaining the **same feasible q and epsilon**, with auxiliary variables. For every finite B, the minimum `E_B` is attained and rational: these constraints form a nonempty rational polyhedron (an admissible constant-off-axis q provides a finite feasible upper bound), the linear objective epsilon is bounded below, and rational LP optimum theory applies. This rational-attainment statement concerns each fixed finite B and does not identify the infinite-domain optimum.

## Reproducible numerical exploration at B=12

The published, minimal SciPy/HiGHS construction is:

`research_checks/CBRC_F7_R438_EPIGRAPH_OSCILLATION_LP_20261121.py` @ `87e10274254cd78b6e2619ffa7bd5370fbe3da58`.

For `B=12`, imposing the **additional, optional experimental search bound** `q<=1`, and fixing `epsilon=1/2`, the local numeric experiment produced:

| Quantity | Observed |
|---|---:|
| Original input cube | `25^4=390625` integer tuples |
| Direct ± inequalities | `781250` |
| Epigraph inequalities (exact count) | `60000` |
| Distinct free q classes | `3046` |
| Unordered a,b pairs | `1176` |
| Auxiliary variables | `2352` |
| Sparse nonzero coefficients | `176092` |
| HiGHS numeric result | `Optimal / status 0` |
| Maximum floating row residual | `1.8808e-13` |
| Search q range | approximately `[0.5,1]` |

The local run finished in approximately 29.5 seconds with single-threaded BLAS. This establishes that the reduced LP is computationally usable at B=12 and yielded a **numerical candidate** for `epsilon=1/2`. Floating-point tolerance alone is **not** a rational exact feasibility certificate; an immutable rational table plus all-integer inequality verification is still required before asserting the new theorem `E_{12}=1/2`. The already exact r436 result remains `E_B=1/2` for `1<=B<=8`.

## Consequence and next frontier

The sparse extended formulation supports larger exact rational constructions and dual infeasibility certificates. An exact dual obstruction at some finite B would improve the global `E_infinity>=1/2` lower bound; a compatible sequence of finite candidates alone does not prove an infinite-domain construction. r435's existing global upper bound remains `4/7`.

This note publishes an exact algebraic/optimization reduction and a scoped numerical exploration, **not** a Native Review, frozen Result update, new Task or promotion of P000.
