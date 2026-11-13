# Stage284-B — two-route shared BRC port: exact incompatibility gap and joint moment hull

**Deliverable:** portable author-side algebraic proof, exact rational example and independently executed ordered-history replay. **Status:** `PORTABLE_AUTHOR_PROOF / EXACT_FINITE_REPLAY / UNREVIEWED / NOT_ADMITTED`. Not a canonical research CLAIM, Source Result, independently reviewed theorem, P000 native Cell dynamical conclusion, or external physical law.

**Fixed scientific read inputs:** `GLOBAL_KNOWLEDGE_V1 main@4b3659222a1886c4643af5bdc6a867c745d65043`; `awdawmip/enterprise-math main@8168b9667b766ce95c681e67628de6af10fdec3b`; predecessor Stage283-B scientific commit `39c9c9c313743e0befca7e380b8864ac5f620e2b`, itself based on Stage282-B. Project P000, ACTIVE `HEARTBEAT_WORLD_NATIVE_X6_TIME`, joint-observer preservation and `docs/PORTABLE_RESEARCH_PROTOCOL.md` were read. The precise scientific question is the Stage283-B packet's two-fiber compatibility problem. Stage278-A Bellman next-face remains a separate open problem.

## 1. Exact model, full ordered population and scope

Let sources `i∈{P,Q}` have equal first-symbol masses `Pr_i(R=0)=Pr_i(R=1)=1/2`. Conditioned on first symbol `r`, draw a second observed symbol `S∈{0,1}` with

- `Pr_P(S=0|R=0)=1/4` and `Pr_P(S=0|R=1)=3/4`;
- `Pr_Q(S=0|R=0)=1/3` and `Pr_Q(S=0|R=1)=2/3`.

The four joint ordered-prefix masses `(R,S)=(00,01,10,11)` are exactly `(1/8,3/8,3/8,1/8)` under `P` and `(1/6,1/3,1/3,1/6)` under `Q`. Every source-prefix weight is strictly positive. The second observation is source-dependent and depends on the first, so the transition kernels are genuinely non-IID. Preserve all four ordered prefix identities and their source tags, even though the *declared downstream* controller only uses `R`.

After observing the prefix, the controller visits the **same** source-blind, route-blind binary port with continuation parameter `y∈[0,1]` at a first gate `Y1`. Stopping yields terminal `A`. On continuation, a fresh Bernoulli draw with *the same conditional parameter y* occurs at `Y2`: stopping there yields `B`, continuing yields `C`. The two random draws are independent conditional on the fixed parameter, but the parameter is tied by a **single controller setting** across both visits and both routes `R=0,1` (and both sources). A source-independent ex ante draw of a global controller setting, when specifically allowed, is a mixture of such fixed shared-port policies, not separate settings chosen after the observed route.

The complete ordered terminal history consists of a prefix `(r,s)` followed by one of three action words `Y1=0`, `(Y1,Y2)=(1,0)` and `(Y1,Y2)=(1,1)`. There are precisely `4×3=12` nonnegative terminal branches for each source (zero weights may occur at policy boundary `y=0` or `1`); each source's terminal weights sum exactly to `1`. For each fixed route `r`, the source reach mass is `w_{i,r}=1/2`, and the ordered `A,B,C` route masses are

`(w_{i,r}(1-y), w_{i,r} y(1-y), w_{i,r} y²)`.

The bounded scalar terminal observer is `F=1` exactly on `(R=0, terminal=B)` or `(R=1,terminal=C)` and `0` otherwise. The optimization target is `max E_i[F]`, or equivalently `min L_i=1−E_i[F]`, for either source; the same formulas hold for both. All results concern this finite external positive-weight BRC decision network with its declared horizon and operator scope, not a general history-dependent controller or a physical/quantum process.

## 2. The true shared-port optimum (global, all real settings)

At route `0`, the observer has terminal mass `w_0 y(1-y)`; at route `1`, it has mass `w_1 y²`, with `w_0=w_1=1/2`. Therefore

`E_i[F]=(1/2)y(1-y)+(1/2)y²=y/2`.

For every real `0≤y≤1`, `E_i[F]≤1/2`, with equality **if and only if `y=1`**. Thus the exact true continuous optimal reward and complementary loss are respectively

`R_true=1/2`, `L_true=1/2`.

Any source-independent random mixture of global shared-port policies has reward `E[Y]/2≤1/2`, so randomizing globally does not improve this affine-observer optimum. This calculation is a continuous-domain algebraic proof, not a conclusion from a grid.

## 3. Invalid independent-route conic relaxation and a strict gap

The Stage283-B two-visit moment lift for one route of fixed reach mass `w>0` is `z=w y`, `v=w y²`. Its true fixed-policy image obeys `0≤v≤z≤w` and `wv=z²`; its **exact convex hull** is

`K_w = { (z,v): 0≤v≤z≤w, z²≤wv }`.

The tempting factor-by-route quotient keeps only `(z_r,v_r)∈K_{w_r}` separately for each route, allowing different route-normalized moments. For our terminal observer its resulting objective is

`R_relax=(z_0−v_0)+v_1`.

For every point of `K_{w_0}`, `z_0−v_0≤z_0−z_0²/w_0 = w_0/4−(z_0−w_0/2)²/w_0≤w_0/4=1/8`. Independently `v_1≤z_1≤w_1=1/2`. Therefore `R_relax≤5/8`. It is **attained** by the two separate route policies `y_0=1/2`, `y_1=1`, corresponding to `(z_0,v_0)=(1/4,1/8)` and `(z_1,v_1)=(1/2,1/2)`. These points each satisfy the stronger local equality `w_r v_r=z_r²`; nonetheless they cannot come from any single global y.

Thus the independent-route conic bound is sharp as a *relaxed* optimization, but false for the actual tied controller:

`R_relax=5/8 > R_true=1/2`, with exact gap `1/8`.

Equivalently for the terminal loss, `L_relax=3/8 < L_true=1/2` by `1/8`. Neither high-precision approximations nor a finite grid nor a locally feasible controller can remove that obstruction: the missing information is **cross-route identity of the same causal port**, not the accuracy of the two local BRC moment cones.

## 4. Exact joint convex hull of a globally shared repeatedly sampled port

**Theorem (finite fixed-occupancy fibers).** Fix any finite nonempty family of source-tagged route identities `j∈J`, each with constant `w_j>0` independent of the downstream global port parameter `y∈[0,1]`. Assume each route uses the *same* two-visit Bernoulli parameter y, independently redrawn conditional on y, and records the two positive moment coordinates `z_j=w_j y` and `v_j=w_j y²`. The convex hull of all simultaneous fixed-port vectors `(z_j,v_j)_{j∈J}` is exactly the image of the moment set

`M = { (m1,m2): 0≤m1≤1, m1²≤m2≤m1 }`

under the shared map `z_j=w_j m1`, `v_j=w_j m2` for every `j∈J`.

**Necessity.** Take any finite convex combination of globally shared port policies, with port settings `y_k∈[0,1]` and weights `α_k≥0`, `Σα_k=1`. Its moments `m1=Σα_k y_k`, `m2=Σα_k y_k²` satisfy `0≤m1≤1`, `m2≤m1` because `y_k²≤y_k` and `m2≥m1²` by weighted Cauchy–Schwarz/Jensen. For every route the mixture masses are *simultaneously* `z_j=w_jm1` and `v_j=w_jm2`, because its upstream reach mass is fixed and the randomization precedes the route. No route-specific `m1_j` or `m2_j` may be independently chosen.

**Constructive sufficiency.** For `m1=0`, the inequalities force `m2=0`, achieved by the single setting y=0. For `m1>0`, one has `m2≥m1²>0`. Put

`u=m2/m1 ∈ [0,1]`, `α=m1²/m2∈(0,1]`.

Choose one global setting `Y=u` with probability α and the global setting `Y=0` otherwise. Then `E[Y]=αu=m1` and `E[Y²]=αu²=m2`. Use this single ex ante mixture *jointly* on all routes; all coordinates become exactly `z_j=w_jm1`, `v_j=w_jm2`. This uses no more than two deterministic global policy settings and proves the full finite-dimensional hull including all boundary cases. ∎

**Causal/observer meaning.** The cross-route repair is the collection of equalities `z_j/w_j=m1`, `v_j/w_j=m2` for all j plus one shared second-moment inequality `m1²≤m2≤m1`. These are indispensable for an exact jointly lifted **moment domain** under ex ante mixtures, although a particular scalar observer can sometimes be certified with fewer equalities. For one fixed (unmixed) port setting, the sharper identity `m2=m1²` is also necessary. Even the full joint moment hull does not automatically preserve future observers of ordered actions, source-specific conditional path states, or operators that can inspect the ex ante latent mixture label; those require a separately declared observer/operation preservation certificate. Positive mass and repeated action sequence are BRC branch identities; no signed/phase cancellation is inferred.

## 5. Exact replay, provenance and proof scope

`REPRO_STAGE284B.py` is a standalone standard-library `fractions.Fraction` script. It enumerates all 12 ordered terminal paths under each positive rational source, for 17 choices `y=k/16`, `k=0,…,16`, crosschecks source mass = 1, precise BRC route `A,B,C` mass triples and `E_i[F]=y/2` (`17×2=34` source-policy crosschecks). It also verifies the independent-route rational maximizers, local conic equalities, strict `1/8` gap and a shared-moment mixture example. The actual stdout is saved verbatim as `REPRO_STAGE284B_EXECUTED_STDOUT.txt` and ends `STAGE284B_SHARED_PORT_CONIC_COMPATIBILITY_EXACT_PASS`.

The continuum inequalities, strict relaxation gap and constructive joint convex-hull identity above are **proved algebraically**; the finite grid is a non-exhaustive crosscheck of the general real-parameter theorems. There is no Lean or third-party independent proof check and no native canonical acceptance. All computations are exact rational arithmetic, with no float/log/phase readout.

The inputs are an external control network, not a six-dimensional Cell world. Native P000/ACTIVE Heartbeat X6 transfer would first require a registered lossless six-nonnegative-field address codec, chosen spatial cell/three-axis slice semantics, separately typed time, native ordered-axis steps, declared source/branch/port transition mapping, declared future operators and full relation/observer preservation. No such bridge is asserted. P000 and protected worldview are unchanged.

**Next:** Stage285-B — allow upstream source/route reach weights `w_{i,r}(x)` to depend on an earlier controller action, while preserving a global tied port `y`; classify the joint causal mixed-moment hull or give an exact rational non-factorization/strict gap, with full ordered paths and independent Fraction replay. Keep Stage278-A Bellman next-face as a separate open line.
