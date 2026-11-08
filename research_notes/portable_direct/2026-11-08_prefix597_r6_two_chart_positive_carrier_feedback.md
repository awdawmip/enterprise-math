# PREFIX-597-R6 — Exact two-chart positive carrier and observable-feedback root policies

Date: 2026-11-08 (Asia/Shanghai). Scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Researcher: `EM-DIRECT-B900FB / TASK_RESEARCH`; native activity: `RA-CC93244CAE5F854895CE2C8E`.
Status: `AUTHOR_DERIVED / ABSTRACT_EXACT_CHECKED / NATIVE_PREMISE_REUSED / UNREVIEWED / NOT_ADMITTED`.

## Exact inputs and scientific scope

The original X6 BRC native dynamics has 96 ports, six labeled actions, and nine allowed roots `0, ±e1, ±e2, ±e3, ±e4`. Retain the **specified** triple reward observer

$$
T=192K-5R_1+R_2-5R_3+R_4+4R_5+4R_6,\quad P_0=R_1+R_2,\quad P_1=R_3+R_4.
$$

This is an observer of six native spatial axes, not a three-dimensional native space. The declared output is the *entire ordered triple-reward history* and, where stated, the final 34-class state. It hides original action labels and starting port.

Immutable scientific premises read at Enterprise Math `main@cd054e38a53ff762130da3e96d9e66ec9e197fcb`:

1. PREFIX-595: `research_notes/portable_direct/2026-11-08_prefix595_r6_four_port_native_34state_quotient.md` (Git blob `70fbec6c80959db684b6026c7dec0c132c06571b`). An exact 34-class nonnegative strong Markov quotient for the triple, and an exact equality between the raw-seven-reward + original-next-port one-step counting measures from original starts (6,29) versus (7,28), and (30,29) versus (31,28), separately for all nine roots. Its native certificate previously verified 864 strong-lumping comparisons and 18 raw kernel identities.
2. PREFIX-596: `research_notes/portable_direct/2026-11-08_prefix596_r6_native_observer_polytope_34_vertices.md` (Git blob `363ddfce9a7cb459064428cd41829a054e8403f8`). The universal triple-law behavior polytope has exactly 34 extreme points, affine dimension 32, and a unique four-point affine dependence.

Denote four behavior vertices by `A=[6,30], B=[29], C=[7,31], D=[28]`, the other 30 by `E_1,...,E_30`. The only affine circuit is

$$
v_A+v_B=v_C+v_D. \tag{1}
$$

Let `c=e_A+e_B-e_C-e_D` be the signed **coefficient difference** (not a negative BRC branch probability). Let `O(p)=Σ_X p_X v_X` for any 34-component nonnegative initial-class mass vector `p`, normalized or unnormalized.

## Theorem A — complete face lattice

The behavior polytope is affinely equivalent to a **30-fold pyramid over a parallelogram**, with precisely **34 vertices, dimension 32, and 34 facets** (dimension 31). Each facet is either the join of all 30 apex vertices with an edge of the parallelogram (4 choices), or a base facet missing one of the 30 apex vertices (30 choices).

**Proof.** The 33 vertices `A,C,D,E_1,...,E_30` are affinely independent, since the only dependence among all 34 has nonzero coefficient on `B`. Send them by an affine isomorphism to `0,e1,e2,e3,...,e32`. Equation (1) forces `B=e1+e2`. Thus `A,B,C,D` form a parallelogram, and each of the 30 further vertices is an independent pyramid apex. The usual pyramid facet correspondence gives `4+30=34`. QED.

## Theorem B — all mixture fibers and exact two-chart normal form

For nonnegative initial masses `p,q` of equal total mass:

$$
O(p)=O(q)\iff q=p+t c,\qquad -\min(p_A,p_B)\le t\le\min(p_C,p_D). \tag{2}
$$

Define

$$
N(p)=p-\min(p_A,p_B)c. \tag{3}
$$

Then `N(p)` is nonnegative, has exactly the same total mass and all universal triple observations as `p`, is idempotent, and is **the unique normalized representative of its observable equivalence fiber** satisfying `min(N(p)_A,N(p)_B)=0`.

The resulting canonical positive domain is precisely the union of two 32-dimensional simplices,
$$
\operatorname{conv}(V\setminus\{A\})\ \cup\ \operatorname{conv}(V\setminus\{B\}). \tag{4}
$$
each with 33 affinely independent vertices, intersecting in their shared 31-dimensional simplex on `V\{A,B}`. Thus one **chart bit** plus at most **33 nonnegative barycentric slots** (32 independent normalized coefficients) encodes every admissible initial mixture exactly. This is a **switching nonlinear coordinate representation**, not a 33-state fixed positive Markov model.

**Proof.** The difference between equal-mass representations of equal behaviors is an affine dependence; by uniqueness of (1), it is `t c`. The four coordinates give the interval in (2). Choosing its left endpoint gives (3). If `q=p+t c` is nonnegative, then `min(q_A,q_B)=min(p_A,p_B)+t`, so `N(q)=N(p)`. Idempotence follows. Deleting either `A` or `B` eliminates the unique affine dependence and leaves 33 affinely independent points. Every `N(p)` has at least one of these two coefficients zero, and conversely every point in either simplex is canonical. QED.

## Theorem C — the sole ambiguity is killed at one native step

For each allowed root `r` and emitted *triple reward increment* `rho=(ΔT,ΔP0,ΔP1)`, let `K[r,rho]` be the 34-by-34 nonnegative reward-labeled transition matrix of the exact PREFIX-595 strong quotient. Then

$$
cK[r,\rho]=0,\qquad pK[r,\rho]=N(p)K[r,\rho]. \tag{5}
$$

for **every** `r,rho` and nonnegative `p`. The joint distribution of the next triple reward and the next 34-class state is identical for two initial distributions in the same observer fiber, *already after one step*.

**Proof.** PREFIX-595 establishes equality of the original-port integer counting measures for all raw-seven-reward + exact-next-port outcomes after summing starts `6+29` versus `7+28`, for each root. Push forward each equality to triple rewards and next 34-class. Strong lumpability makes each class transition well-defined and implies row `A` + row `B` = row `C` + row `D` separately for each emitted `rho`. Divide native action counts by six. This is exactly the first identity (5); (3) gives the second. QED.

**Scope.** The strong 34-class quotient and its adaptive propagation here preserve only the declared triple reward language. The separate stronger original-port equality for the *specific two original-port mixtures* covers full seven rewards and original next port but does not establish full-seven strong lumpability for every 34-class pure state. Original action labels discriminate the special starts at depth one (PREFIX-595), so they are not included in the asserted quotient.

## Corollary — feedback-controlled nine-root sequences

The earlier universal law treated externally predetermined nine-root schedules. Equation (5) also permits **observable-feedback policies**: the root at time `n` can be a measurable function of previously observed triple reward increments and exogenous randomness independent of the hidden initial port, with the same random seed coupling. Under any such policy, two mixtures related by `t c` produce identical full ordered triple-reward histories for every horizon `n>=0` and identical joint laws of the history with the final 34-class state for every `n>=1`. At `n=0`, the initial class law can remain different.

**Proof.** Condition on the exogenous seed. At the first step the policies select the same root, and (5) shows equality for each emitted `rho` even jointly with next class. Induct on observed history: the conditional next-class vectors and selected roots agree at each stage. Integrate over the seed. QED.

An exact update for each reward-history mass `m[h]` is `m[h+rho] += N(N(m[h]) @ K[r(h),rho])`. Retain reward-history branches or an independently certified downstream observer. The normalizer needs only one `min` and four coefficient updates, but total transition, emission-support and bit-complexity costs remain to be measured; no blanket algorithmic speedup is claimed.

## Verification and future use

The attached standard-library `PREFIX597_R6_two_chart_positive_carrier_certificate.py` locally returned `ALL_ABSTRACT_CHECKS_PASS`: exact 34-vertex/33-rank canonical model, unique circuit, two charts, 115 rational mixture tests including fiber endpoints, and synthetic labeled nonnegative transition tests satisfying `cK=0`. This verifies the **abstract implications**, not a fresh native BRC kernel execution. The native premises rely on the separately published author-checked PREFIX-595 certificate and frozen PREFIX-565 kernel; independent native re-execution remains open.

BRC reuse: `REUSE_APPLIED` to native PREFIX-565 exact edge and PREFIX-595/PREFIX-596 author proofs. Observer safe only for stated output and feedback language; P000 V5, X6, joint provenance and original six-axis data remain unchanged. Result is author-level, not a formal CLAIM/Result/Review or Working Truth.

**Next smallest scientific unit (PREFIX-598-R6).** Find a direct phase/branch/action pairing for the four-port equation, uniformly across the nine roots, and account for the four nonzero primitive-action-label witness terms. A parallel route tests minimum dimension for unrestricted positive hidden-state realizations and exact rational bit growth of 34-state, 33-signed, and two-chart forward readout.
