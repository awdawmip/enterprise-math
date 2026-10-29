# Stage285-B — exact upstream-dependent BRC joint-moment hull and correlation obstruction

**Author deliverable:** self-contained algebraic proof, fully ordered source-tagged finite-path counterexample, exact executable Fraction replay. **Status:** `PORTABLE_AUTHOR_PROOF / EXACT_FINITE_REPLAY / UNREVIEWED / NOT_ADMITTED`. No native CLAIM, Source Result, independent Driver admission, Lean checker, six-dimensional Cell dynamics, or physical calibration is asserted.

**Pinned inputs actually read (2026-10-29):** `GLOBAL_KNOWLEDGE_V1 main@ebc95a36c61f05438c3294b5dd4c1e2011f51f70` (canonical `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, ACTIVE worldview and triggered mathematical/BRC policies); `enterprise-math main@e3148a75734182faea1e2822c84bd782b43005bb` (AGENTS, P000, joint observer, heartbeat X6, and portable protocol); predecessor Stage284-B `3fb3545eaa820982ffd3360b4e60965c472a7f92`, exact next packet `NEXT_TASK_PACKET_285B.md`. The old Stage278-A N=12 Bellman new-face task remains separate.

## 1. Completely specified positive-rational source population and causal ports

Two sources `i=P,Q` emit an ordered pair `(R,S)`. The initial distribution and conditional second-symbol probability are

| source | Pr(R=0) | Pr(S=0 \| R=0) | Pr(S=0 \| R=1) | Pr(RS=00,01,10,11) |
|---|---|---|---|---|
| P | 1/4 | 1/4 | 3/4 | (1/16, 3/16, 9/16, 3/16) |
| Q | 1/3 | 1/3 | 2/3 | (1/9, 2/9, 4/9, 2/9) |

All primitive source probabilities are strictly positive and source-dependent, and the distribution of `S` depends on `R`: this is genuinely non-IID. Before either observed source symbol, a **source-blind upstream action** `U~Bernoulli(x)` is drawn, independent of the source law conditional on the fixed controller setting `0<=x<=1`. After drawing `R,S`, expose downstream route `T=R XOR U`. The source-blind, route-blind shared port `Y` is visited twice; each visit independently continues with the **same fixed** probability `0<=y<=1`. Stopping immediately yields terminal `A`, continuing then stopping yields `B`, and continuing both times yields `C`. Ordered action words are `(Y1=0)`, `(Y1=1,Y2=0)`, `(Y1=1,Y2=1)` respectively. The complete path identity is `(source,U,R,S,T,action word,terminal)`; there are `2*2*2*3=24` leaves per source (boundary leaves may have zero probability). All branch mass is positive rational whenever `0<x,y<1`.

Let `p_i(r,s)=Pr_i(R=r,S=s)` be the rational table above and `a_P=1/4`, `a_Q=1/3`, `b_i=1-2a_i` (`b_P=1/2`, `b_Q=1/3`). For a **fixed deterministic global controller setting** `(x,y)∈[0,1]^2`, the ordered leaves with `u∈{0,1}` have the exact mass `p_i(r,s) [x if u=1 else 1-x]` multiplied by `(1-y, y(1-y), y²)` for terminal `A,B,C`. There is no negative/signed cancellation; branch provenance is retained.

The route-0 reach mass is the affine expression

`w_i,0(x)=a_i(1-x)+(1-a_i)x=a_i+b_i x>0`, and `w_i,1(x)=1-a_i-b_i x>0`

for **all** `x∈[0,1]`. These two weights are source-dependent, exactly the upstream-sensitive occupancy requested by Stage285-B. The source-law draws remain positive at controller endpoint settings even when some action branches vanish.

The allowed primary observer class is any bounded function of the *complete ordered terminal path* above, including source label only as an external evaluation index. The finite horizon ends at the second `Y` visit; the observer cannot inspect a latent ex ante setting itself or impose future visits. A narrower explicit binary observer used for a counterexample is `F=1` precisely when `(T=0,terminal=B)` or `(T=1,terminal=C)`, and `F=0` otherwise.

**Three policy classes are distinct:** (a) one fixed shared `(x,y)`; (b) source-independent **ex ante** random mixture of complete settings `(X,Y)`, held fixed during each path, with U and the two Y Bernoulli draws independent conditional on the chosen setting; (c) fresh route/history-adapted changes to y. Only (a) and (b) are studied here; (c) is not included in their maxima or convex hull.

## 2. Exact convex hull for correlated upstream/downstream ex ante mixtures

**Theorem 285.1 (binary-split truncated moment hull).** Let

`Phi(x,y)=(x,y,y²,xy,xy²)` for `0<=x,y<=1`,

and denote a candidate vector by `(u,m1,m2,c1,c2)`. The exact convex hull of all `Phi(x,y)` is the set of vectors satisfying `0<=u<=1` and both **joint mass-and-moment block** conditions

```
(a_0,b_0,d_0)=(1-u, m1-c1, m2-c2),
(a_1,b_1,d_1)=(u, c1, c2),
0 <= d_k <= b_k <= a_k,       b_k^2 <= a_k*d_k,  k=0,1.
```

In fact every feasible point is realized by an ex ante distribution supported on at most **four** fixed deterministic global settings `(x,y)` with `x∈{0,1}`. If the moments are rational, all atom weights and y-settings can be chosen rational.

*Necessity.* Under any ex ante distribution of `(X,Y)`, distribute each setting `(x,y)` to two endpoint settings `(0,y)` and `(1,y)` with weights `1-x` and `x`. This preserves each of `E[X]`, `E[Y]`, `E[Y²]`, `E[XY]`, `E[XY²]` (because the five monomials are affine in x). For each endpoint `k=0,1`, the resulting nonnegative subprobability measure of Y has mass `a_k`, first moment `b_k` and second moment `d_k`. The pointwise inequalities `0<=Y²<=Y<=1` yield `0<=d_k<=b_k<=a_k`; weighted Cauchy–Schwarz yields `b_k²<=a_k d_k`, including the zero-mass case.

*Sufficiency and explicit rational witness.* Suppose the displayed inequalities hold. For each `k`, if `a_k=0` then `b_k=d_k=0` and no atom is needed. If `a_k>0` but `b_k=0`, `d_k=0` and place all mass `a_k` at `(x=k,y=0)`. Otherwise `b_k>0`, the inequalities force `d_k>0`; set

`v_k=d_k/b_k ∈(0,1]`, `alpha_k=b_k²/d_k ∈(0,a_k]`.

Place mass `alpha_k` at `(k,v_k)` and mass `a_k-alpha_k` at `(k,0)` (omit zero-weight atoms). This produces precisely `a_k`, `alpha_k*v_k=b_k` and `alpha_k*v_k²=d_k`. Across both values of k, the weights sum to one and the five desired coordinates match exactly. All construction operations preserve rationality. Hence the inequalities characterize the **entire real convex hull**, not just a finite sampled subset. `□`

This is a **joint** moment cone and not Stage284-B's direct product with independent route moments: upstream X-Y correlation enters through `c1,c2`. The two blocks are subprobability measures conditioned on the actual upstream action outcome; their masses **sum to one**, rather than representing independently chosen route policies.

## 3. All ordered terminal paths factor through precisely stated sufficient moments

**Theorem 285.2 (observer-preserving BRC quotient, fixed horizon).** In the model of §1, for any ex ante mixed global policy `(X,Y)`, the full source-tagged probability of **every** ordered terminal path `(U,R,S,T,action word,terminal)` is an affine function of the five moments from Theorem 285.1. Consequently any bounded terminal observer on these complete paths has exactly the same expectation for any two ex ante mixtures with the same five moments, simultaneously under P and Q. This is an exact finite-horizon/source-typed factorization and preserves path identity, not just aggregate route mass.

*Proof.* Conditional on a fixed `(x,y)` and source-prefix `(r,s)`, the upstream action is Bernoulli(x). After mixing, write

```
for U=0:   mass(A,B,C) = p_i(r,s)*(a0-b0, b0-d0, d0),
for U=1:   mass(A,B,C) = p_i(r,s)*(a1-b1, b1-d1, d1),
T = R XOR U,
```

where `(a_k,b_k,d_k)` are the two moment blocks. These are exactly the expectations of `(1-X)*[(1-Y),Y(1-Y),Y²]` and `X*[(1-Y),Y(1-Y),Y²]`. Their nonnegativity follows from the cone. Every path is represented with its full U,R,S,word and T label; multiplying by any bounded observer and summing yields the claimed factorization. This is stronger than preserving four aggregate summary observables, but it only covers this declared finite-horizon policy class. A reader of the hidden ex ante setting, a third Y visit or an adaptive reconfiguration need not factor through the same five coordinates. `□`

For reference, after aggregating R,S and U by final route, set `w0=a_i+b_i u`, `z0=a_i m1+b_i c1`, `v0=a_i m2+b_i c2` and `w1=1-w0`, `z1=m1-z0`, `v1=m2-v0`. Route terminal masses `(A,B,C)` are exactly `(w_t-z_t,z_t-v_t,v_t)` for `t=0,1`. The declared bounded observer has

`E_i[F]=z0-v0+v1 = a_i*m1+(1-2a_i)*m2+b_i*(c1-2*c2)`.

This identity holds for all real ex ante mixtures, not only rational grid values.

## 4. Exact strict non-factorization and constrained optimization gap

Take the following two *source-blind ex ante mixtures of entire global settings*:

```
A: (X,Y)=(0,0) or (1,1), each with mass 1/2;
B: (X,Y)=(0,1) or (1,0), each with mass 1/2.
```

Both have the **same** upstream mean and downstream marginal two moments `u=m1=m2=1/2`, but

`A: c1=c2=1/2`, whereas `B: c1=c2=0`.

Thus both have exactly the same source-specific *mean route reach masses* `w_i,0(u)`, as well as the same marginal tied-port moments; nevertheless their ordered terminal laws and even the binary observer differ. From the exact formula:

| source | `E_i[F]` under A | `E_i[F]` under B | discrepancy B − A |
|---|---:|---:|---:|
| P | 1/8 | 3/8 | 1/4 |
| Q | 1/6 | 1/3 | 1/6 |

In the **constrained moment slice** `u=m1=m2=1/2`, the equality `E[Y-Y²]=0` forces `Y∈{0,1}` under every ex ante mixture. Thus `c1=c2=t` and the exact joint table of X's endpoint Bernoulli replacement with Y admits precisely `0<=t<=1/2`; the explicit four-point table

`Pr(0,0)=t`, `Pr(0,1)=1/2-t`, `Pr(1,0)=1/2-t`, `Pr(1,1)=t`

realizes every such t. Inserting this into the full expression gives **global continuous-domain optima over the entire constrained mixed-policy class**

`E_P[F]=3/8-t/2 <= 3/8`, `E_Q[F]=1/3-t/3 <= 1/3`,

both attained at `t=0` (mixture B). By contrast, a proposed **product-moment factorization** based only on means, i.e. imposing `c1=u*m1=1/4` and `c2=u*m2=1/4`, gives `E_P[F]=E_Q[F]=1/4`. Its exact constrained objective gaps are **1/8 under P** and **1/12 under Q**. The product relation here is **not a valid relaxation** of the correlated mixed-policy class: it incorrectly excludes legitimate source-blind, globally correlated policy mixtures. The proof exhibits the missing BRC cross-occupancy residual explicitly; no independent route setting or adaptive y was smuggled into the witness.

Neither the theorem nor the example asserts that five moments are minimal for every specific observer, nor does it claim an unconstrained optimal reward gap. It proves their exact sufficiency for the specified entire ordered-horizon observer class and the insufficiency of the smaller triple `(u,m1,m2)` for that class.

## 5. Exact replay, prior art boundary, future scope and native status

`REPRO_STAGE285B.py` is a standalone Python standard-library `fractions.Fraction` program. It performs 9×9 parameter grid checks for both sources (`162` source-policy pairs; `3888` individually tracked ordered terminal leaves), verifying exact source normalization, affine route mass formulas and the observer formula; checks both ex ante mixtures and 17 exact rational couplings at the constrained optimum; and reconstructs a nontrivial rational five-moment vector with the explicit four-atom map, verifying **identical full 24-leaf laws** for both sources. Its actual stdout is `REPRO_STAGE285B_EXECUTED_STDOUT.txt`, ending `STAGE285B_CAUSAL_SPLIT_MOMENT_HULL_EXACT_PASS`.

The **general real-parameter statements** follow from §§2–4's algebra and measure-splitting construction; finite grids test concrete witnesses and code logic, not the universal theorem. The first-two-moment cone is a special elementary case of the classical *truncated Hausdorff moment problem*. As contextual prior art (abstract/metadata only inspected, not used as a substitute for proof): P. J. di Dio and K. Schmüdgen, *The multidimensional truncated Moment Problem: Carathéodory Numbers*, arXiv:1703.01494 (2017), https://arxiv.org/abs/1703.01494; and D. D. Ang, R. Gorenflo, D. D. Trong, *A Multi-Dimensional Hausdorff Moment Problem: Regularization by Finite Moments*, Z. Anal. Anwend. 18 (1999), doi:10.4171/ZAA/866. **No claim of general novelty or comprehensive external duplication search is made.** The concrete source-tagged BRC quotient and exact conditional correlated-mixture witness are author-side scoped calculations.

P000/ACTIVE Heartbeat X6 remain unchanged: six native spatial axes with three-dimensional research slices, independent time, native 120° right-angle semantics, signed relative X6 displacements and a registered six-nonnegative-field address codec for final addresses. The external model here introduces no Cell transition, registered address, typed heartbeat update, three-axis slice embedding, or relation-preserving mapping; thus no transfer to native X6 physics or native BRC–Shor arithmetic is asserted. The positive weighted path algebra in this external toy DAG uses no phase or signed cancellation. A native translation would first require all those type, path, port, observer and future-operation certificates and would be subject to the BRC-only computation contract in its proper scope.

**Next separate research unit:** Stage286-B, extend from two tied port visits to three and prove or falsify sufficiency of the five-coordinate quotient. A concrete rational two-mixture witness is provided in the next packet. Keep Stage278-A N=12 Bellman adjacent-face and native X6 correspondence as separate open units.
