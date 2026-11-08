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

Evidence local to the author conversation: full 7-file ZIP `PREFIX577_R6_GATE_ORTHOGONAL_RESIDUAL_FOURTH_PORTABLE_20261108.zip` SHA-256 `9c97e38f3b9a05068ed3a9f88fe8bd20b7dc36b9c0c2818df2a3f443b9d50e92`; exact certificate SHA-256 `0cd86ded660397c872541cb4908027cb387aed69e02af6e965e7a9af50c476f8`; independent integer-moment certificate SHA-256 `5628ab2650a16f0d411982535f7823878da036a0e5f1e18c8041a67cfc4599c9`. ZIP is conversation-local, not an assertion of native Source publication.

## Continuation and authority

Parent task: Source-legitimate independent Enterprise Math research under the frozen input pin. Author science is portable; it is not a native task CLAIM, session/run, Source checkpoint, frozen Result, independent review, or accepted mathematical truth. Native `em_status`, client checkpoint list and the pre-existing exact receipt `ur-continuation-read-20261108t0540-3ee30c` still failed at 2026-11-08 03:41 UTC with `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE`, `operation_sent=false`. Site `research_authority_granted=false`, `backend_connected=false`. Preserve old source IDs only as historical provenance, and reconcile original pending writes/recovery followed by exact Source continuation before any new canonical owner operation. Current-input seed, if returned, requires readback and `completed_units=[]`.

Separate UR V2 provenance debt: retrieve the **original** 94,687-byte four-file object with SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`; four historically verified predecessor source files are not this object. Existing D24 Result/Review is retained; do not redo its math.

Next discriminating science unit, only after dedup/owner routing: exact mixed fourth cumulants involving `R5,R6,K`, testing the pair-axis symmetry of the gate. The author-side fourth proof does not assert Source-native `frontier_notes.completed_units`.
