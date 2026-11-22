# CBRC F7 r475 — global minimax attainment and exact finite-box convergence

Date: 2026-11-22 (Asia/Taipei). Provenance: the same original RESEARCH_DRIVER logical lane `EM-DVR-DEBB5E`. The CBRC F7 frozen Result, Task and original scientist `EM-CBRCF7-83A1D4` retain their existing attribution and independent-review status. This note is a new Driver-authored mathematical subunit, **not** a native accepted Result or review.

## Exact model and quantifiers

Let `A` be the class of **globally defined** real-valued `q: Z² -> R` satisfying all the original F7 scalar conditions:
- `q(-x,y)=q(x,y)` for every integer pair;
- `q(0,0)=0`, `q(x,0)=1` for every nonzero integer `x`;
- `q(x,y)>=1/2` whenever `y!=0`;
- `q(2,1)=q(-1,-1)=1/2`.

With `k=a-2b-c+2d`, define
```text
D_q(a,b,c,d) = q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d).
E_B(q) = max {|D_q(z)| : z in [-B,B]^4 intersect Z^4},  B=1,2,...
E_inf(q) = sup {|D_q(z)| : z in Z^4}.
e_B = inf_{q in A} E_B(q),  m = inf_{q in A} E_inf(q).
```
Every infimum above uses the **same global admissible class** `A`; a finite-box witness is not permitted to weaken scalar constraints outside its box. The baseline `q_0(x,y)=0` at the origin, `1` on the nonzero horizontal axis, and `1/2` otherwise belongs to `A` and has bounded defect (in fact `E_inf(q_0)=1`, as already verified in r471). Thus `0<=e_B<=m<=1`.

## Lemma 1 — pointwise coercivity from a finite-box defect bound

For any `q in A`, any `(x,y) in Z²` with `y!=0`, set
```text
r=x-y, u=x-2y, p=(x,y), Tp=(x-3y,-y).
M_p=max(|x|,|y|,|x-3y|).
H_p=1_{r!=0}+1_{u!=0} in {1,2}.
```
The exact axis-pair input `z_p=(x,y,x-3y,-y)` has `k=u-r=-y`, so its two transformed points are `(r,0)` and `(u,0)`:
```text
D_q(z_p) = H_p-q(p)-q(Tp).
```
Consequently, whenever `B>=M_p` and `E_B(q)<=epsilon`,
```text
H_p-epsilon <= q(p)+q(Tp) <= H_p+epsilon,
1/2 <= q(p) <= H_p+epsilon-1/2.
```
In particular, `q(x,y)<=3/2+epsilon` off axis, and the sharper `q(x,y)<=1/2+epsilon` applies on either nonzero line `x=y` or `x=2y`. For a **global** defect bound `E_inf(q)<=epsilon`, these bounds hold simultaneously for every off-axis point. Their proof uses only the original axis values and off-axis floor, not any added regularity, decay or upper-bound axiom.

## Theorem 2 — exact exhaustion and attainment

**For the original F7 admissible class,**
```text
e_1 <= e_2 <= ...,
m = lim_{B -> infinity} e_B = sup_{B>=1} e_B,
there exists q_opt in A such that E_inf(q_opt)=m.
```
Moreover the sequence of finite-box near-minimizers can be chosen with a pointwise convergent subsequence whose limit is a global minimizer.

**Proof.** Monotonicity of `E_B(q)` for each q implies monotonicity of `e_B`; the fixed baseline yields a finite upper bound, so `L=lim_B e_B` exists and `L<=m`.

For every `B>=1` select `q_B in A` satisfying `E_B(q_B)<=e_B+1/B` (the definition of the infimum suffices; finite-box attainment is not assumed). Fix any coordinate `p=(x,y)`. If `y=0`, its value in every `q_B` is fixed. If `y!=0`, Lemma 1 supplies, for all `B>=M_p`, the bounds
```text
1/2 <= q_B(p) <= 3/2+e_B+1/B <= 5/2+1/B.
```
Thus **each fixed coordinate** has an eventually bounded real sequence. Since `Z²` is countable, successive subsequence extraction and the diagonal argument produce integers `B_j -> infinity` such that `q_{B_j}(p)` converges for every lattice point p. Call the pointwise limit `q_*`.

All original scalar constraints defining `A` are pointwise equalities or closed inequalities, so the limit `q_*` is still in `A`. For a fixed quadruple `z`, eventually `z in [-B_j,B_j]^4`. The four evaluated lattice points in `D_{q_{B_j}}(z)` are fixed, so
```text
|D_{q_*}(z)| = lim_j |D_{q_{B_j}}(z)|
             <= lim_j (e_{B_j}+1/B_j)=L.
```
Taking the supremum over all fixed z gives `E_inf(q_*)<=L`. By definition, `m<=E_inf(q_*)`; combined with `L<=m`, this forces
```text
E_inf(q_*) = m = L.
```
Hence the global minimum is attained and finite-box optimal values converge to it. QED.

## Exact compactness corollary — any strict obstruction is finite

For every real threshold `alpha`,
```text
(no global q in A satisfies E_inf(q)<=alpha)
  <=> m>alpha
  <=> exists a finite integer B with e_B>alpha.
```
Equivalently, if **every** finite B admits an admissible `q_B` with `E_B(q_B)<=alpha`, then there exists a single globally admissible `q` with `E_inf(q)<=alpha`. For alpha=1/2, exact feasibility in all finite boxes would therefore prove the original full-lattice half-error conjecture; a strict global gap above 1/2 must have an exact finite-box witness.

This is an existence/completeness theorem, not an effective bound on which B witnesses a strict gap, and not a claim that the open half-error threshold has been decided. The known exact finite range through B14 and the inherited bracket `1/2<=m<=4/7` remain unchanged.

## Validation and significance

The axis-pair identity is a direct integer substitution; a fresh baseline check evaluated 2,401 inputs on `[-3,3]^4`, found maximum defect 1, and cross-checked all 420 off-axis coordinates in `[-10,10]^2` against their exact axis-pair defect identity. These checks corroborate the formula; the theorem is proved by the exact identity plus the countable diagonal argument, rather than finite experimentation.

Unlike a compact-support construction, this result provides a precise global/finite relationship for the original unbounded, unconstrained-off-axis-upper problem. The automatic pointwise bounds supply the missing compactness; no artificial upper-value restriction or change of original F7 predicates is inserted.

Dependencies and authorship:
- r471 axis-pair and fiber identity: `enterprise-math@013c38ab95d45a1c5fc6f3e583d6e62e688395f7:research_notes/driver/2026-11-22_f7_r471_exact_fiber_swap_global_quarter_audit.md`.
- r472 quadratic density: `enterprise-math@def0b48fe6aa9025f747c1899fcd2ea0d21553ae:research_notes/driver/2026-11-22_f7_r472_axis_pair_quadratic_tail_density.md`.
- r474 constrained kernel (independent structural branch): `enterprise-math@6009333d847ea2b78fd4386610ded14b9f8a1d3d:research_notes/driver/2026-11-22_f7_r474_exact_linear_constraint_gauge_classification.md`.

New proved mathematical subunit: 1. Native Review admitted: 0; Native Result admitted: 0; formal Task completed: 0; parent objective completed: 0. No claim, author reassignment, safety bypass or scheduler change.
