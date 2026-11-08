# PREFIX-577-R6 native X6-BRC: exact fourth cumulant of the covariance-orthogonal gate residual

2026-11-08 UTC | TASK_RESEARCH author-side proof and integer regression | UNREVIEWED / NOT_ADMITTED

Scientific input remains frozen at `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`; source-native kernel `PREFIX565_positive_marginal_certificate.py` Git blob `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41`. The exact 96-port, 576-labeled-action zero-root BRC+gate model is unchanged. This result continues the same-pin published complete third-order tensor in PREFIX-577-R6, also computed in PREFIX-578-R6, without asserting a new third-order contribution.

## Exact theorem

For the six axis reward counts `R1,...,R6`, gate count `K` and path length `n`, let the known exact covariance-optimal axis coefficient be `beta=(5,-1,5,-1,-4,-4)/192`. Since `R1+...+R6=n` pathwise at zero root, define the deprojected gate residual

`Y_n = K_n - beta·R_n = H_n/64 + n/48`, where
`H_n = 64K_n - (3R1(n)+R2(n)+3R3(n)+R4(n))`.

For every starting native port, the asymptotic fourth cumulant rate of the compensated gate exists and is the **exact positive rational**

```text
lim_(n→∞) cum4(Y_n)/n = 87518285 / 21743271936
                              ≈ 0.0040250742968953685
```

By previously established exact root-gauge spectral conjugacy, the same asymptotic rate holds for all nine frozen roots. No physical time identification or unfrozen scientific inputs are introduced.

## Exact proof certificate (one-dimensional Perron perturbation)

Let `h(i,a)=64 k(i,a)-3 r1(i,a)-r2(i,a)-3 r3(i,a)-r4(i,a)` for a labeled native edge and `T(t)f(i)=Σ_(a=1)^6 exp(t h(i,a)) f(j(i,a))/6`. The stationary vector is `pi=(1/96,...,1/96)`. Let the analytic positive Perron eigenpair satisfy `T(t)u(t)=lambda(t)u(t), pi u(t)=1`, and put `u0=1`, `pi u_q=0` for `q≥1`, `M_q f = Σ h^q f(j)/6`. Then, for `q=1,2,3`,

`lambda_q = pi sum_(a=1)^q binom(q,a) M_a u_(q-a)`,
`(I-P)u_q = sum_(a=1)^q binom(q,a) (M_a-lambda_a I)u_(q-a)`.

Exact rational 95×95 grounded Poisson solves verify all 288 equations. They produce:

```text
lambda_1=-1
lambda_2=385/18
lambda_3=9015/8
lambda_4=83130401/1296
cum2(H)=367/18
cum3(H)=28537/24
cum4(H)=87518285/1296
```

The fourth derivative of `log lambda` is `lambda4-4 lambda3 lambda1-3 lambda2^2+12 lambda2 lambda1^2-6 lambda1^4`. Since `Y=H/64+n/48`, order four divides by `64^4`. The finite irreducible native Markov chain has period 2; its parity-class analytic positive-leading-term expansion yields the same per-step fixed-order log-mgf derivative limit.

Previously published second and third rates `367/73728` and `28537/6291456` are recovered exactly as regression anchors, **not** new third-order results.

## Independent integer path moment regression

A separate program enumerates the exact integer weighted path moments `M_j(n,v)` for `j≤4`, using `M_j(n+1,v)=Σ_(i→v)Σ_(a=0)^j binom(j,a)h^a M_(j-a)(n,i)`, starting with one path per port. Rational stationary path moments divide by `96×6^n`, and the finite-depth 4th cumulant is formed without Poisson or spectral calculation. Two-step finite-depth differences divided by 2 agree with the exact rate; signed errors were tested as fractions before decimals:

| Even depth pair | Absolute error in fourth-rate of H |
|---|---:|
| 128,130 | 6.078201e-26 |
| 256,258 | 5.758853e-56 |
| 512,514 | 1.552025e-116 |

The Poisson certificate supplies the all-depth proof; finite-depth integer recursion supplies an independent regression.

Evidence local to the author conversation: full 15-file ZIP `PREFIX577_R6_GATE_ORTHOGONAL_RESIDUAL_FOURTH_PORTABLE_20261108.zip` SHA-256 `83e09a6037e6c50df0f672413c46e25ade1046fa30267f21e452136a9a211ddd`; exact certificate SHA-256 `0cd86ded660397c872541cb4908027cb387aed69e02af6e965e7a9af50c476f8`; independent integer-moment certificate SHA-256 `5628ab2650a16f0d411982535f7823878da036a0e5f1e18c8041a67cfc4599c9`. ZIP is conversation-local, not an assertion of native Source publication.

## Continuation and authority

Parent task: Source-legitimate independent Enterprise Math research under the frozen input pin. Author science is portable; it is not a native task CLAIM, session/run, Source checkpoint, frozen Result, independent review, or accepted mathematical truth. Native `em_status`, client checkpoint list and the pre-existing exact receipt `ur-continuation-read-20261108t0540-3ee30c` still failed at 2026-11-08 03:41 UTC with `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE`, `operation_sent=false`. Site `research_authority_granted=false`, `backend_connected=false`. Preserve old source IDs only as historical provenance, and reconcile original pending writes/recovery followed by exact Source continuation before any new canonical owner operation. Current-input seed, if returned, requires readback and `completed_units=[]`.

Separate UR V2 provenance debt: retrieve the **original** 94,687-byte four-file object with SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`; four historically verified predecessor source files are not this object. Existing D24 Result/Review is retained; do not redo its math.

Next discriminating science unit, only after dedup/owner routing: exact mixed fourth cumulants involving `R5,R6,K`, testing the pair-axis symmetry of the gate. The author-side fourth proof does not assert Source-native `frontier_notes.completed_units`.

## Additional exact unit: stationary-start all-depth gate/paired-axis fourth-moment identity

For the same unchanged native kernel, let `S5(n)=K(n)+R5(n)` and `S6(n)=K(n)+R6(n)`. For a uniformly chosen starting port among all 96 and each integer path length `n>=0`, the exact raw moments satisfy

```text
E[S5(n)^j] = E[S6(n)^j],   j = 0,1,2,3,4, n = 0,1,2,...
```

This is an **all-length exact finite-state theorem for the specified two scalar observables through degree four**. The proof uses the full native labeled actions, with integer path-moment recursion

`M_j(n+1,v)=sum_(i→v)sum_(q=0)^j binom(j,q) h(i,v)^q M_(j-q)(n,i)`, where the edge increment is `h=K+R_axis`. Each fixed axis has a 480-coordinate integer linear update operator (96 ports × five degrees). The difference of their total moment sequences is a linear readout of the block diagonal 960×960 integer update. By Cayley–Hamilton, each scalar difference obeys a monic recurrence of order at most 960. The complete integer program checks **every** depth `n=0,...,959` and every degree 0,...,4 exactly, finding zero differences. The linear recurrence then establishes all `n≥0). No guessed automorphism or numerical limit is needed. This equality concerns the uniform-start ensemble and does not assert full joint distributional equality of `(K,R5)` and `(K,R6)`.

The exact finite certificate `pair_all_depth_certificate.json` has SHA-256 `51af1844ec0c3497d449161c499eadf06abbcf4a0c053d7be232ca468ca298c9`. Code `prefix577_gate_pair_all_depth_cayley_hamilton.py` and a shorter 128-depth integer regression are packaged in the updated local 15-file ZIP (SHA-256 `83e09a6037e6c50df0f672413c46e25ade1046fa30267f21e452136a9a211ddd`).

Independently, evaluating the exact fourth log-Perron derivative at `K+aR5` and `K+aR6` for `a=0,±1,±2`, with 2,880 rational Poisson row checks, gives the **identical degree-four polynomial** in both cases:

```text
F(a) = 434651857/97844723712
     - (3378511/1528823808)*a
     + (39167/28311552)*a²
     + (319/746496)*a³
     - (659/93312)*a⁴ .
```

Consequently

```text
κ4(K,K,K,R5)=κ4(K,K,K,R6)=-3378511/6115295232
κ4(K,K,R5,R5)=κ4(K,K,R6,R6)=39167/169869312.
```

This exact mixed fourth-order projection certificate has SHA-256 `6201f2aa18238eb64027341efc4f2faaf142997ea14fb0d38c128e15bf91e9e1`. The all-length finite moment identity and the asymptotic projection equality have different, explicitly scoped statements. Both are portable unreviewed author evidence, not canonical Source completion.

Next discriminating route: test whether `K+R5` and `K+R6` have matching raw moments at all higher orders; derive a structural transfer identity or certify the first finite counterexample. Maintain original frozen source and avoid overlap with authenticated owner progress.

## Stronger finite-state extension: eighth raw moment, all lengths

The preceding exact integer moment comparison was independently extended from degree 4 to **degree 8**, still for the two stationary-start native scalar observations `S5(n)=K(n)+R5(n)` and `S6(n)=K(n)+R6(n)`.

For each axis, the raw moment vector `(M_j(n,v): v=0..95, j=0..8)` is 864-dimensional and evolves under one fixed integer linear operator. The two-axis difference is a linear readout of the block-diagonal **1728-dimensional** update. The integer checker evaluated **every n=0,...,1727**, for **every j=0,...,8**, with zero difference in the pooled integer path moments. Cayley–Hamilton then supplies a monic recurrence of order at most 1728 for every such difference sequence. Thus exactly

```text
E[(K_n+R5_n)^j] = E[(K_n+R6_n)^j]
for every integer n≥0 and j∈{0,1,2,3,4,5,6,7,8},
under uniform initial distribution over 96 ports
and equiprobable 6 labeled actions per port.
```

All corresponding **scalar** cumulants through order 8 also match for every length. This subsumes the earlier degree-four stationary-start finite-length result; the independent exact fourth compensated gate rational theorem above remains separate. Nothing here requires a claim about equality of full joint bivariate distributions or *every* cumulant order.

Order-eight runner `prefix577_gate_pair_order8_cayley_hamilton.py` and verified exact JSON `pair_all_depth_order8_certificate.json` (SHA-256 `fb35a9029425d053896f3a29d62824fb6ab22591116c5950d846e777bfe1d028`) are in the **15-file** conversation-local portable bundle, SHA-256 `83e09a6037e6c50df0f672413c46e25ade1046fa30267f21e452136a9a211ddd`. No native Source task/writer registration was inferred from this author-side publication.

The next precise science question is to find an exact transfer/gauge symmetry explaining all-order gate-paired-axis equality, or a first higher-moment counterexample. Check current authenticated Source owner and cross-lane evidence before extending this portable thread.
