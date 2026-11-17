# R5 — A planar winding certificate for exact FULL/LR real-image equality after two nonfrozen likelihood-ratio collisions

Date: 2026-10-30 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

Frozen source inputs: GLOBAL_KNOWLEDGE_V1 main@ab3cf46f589428d453a2cb91d93cdc37711e4a8d; Enterprise Math main@063316aba2aa706f9e890e791585a8cfab68d6bf. Exact predecessor is research_notes/brc_r5_dynamic_double_collision_20261030_t0140/RESEARCH.md at immutable commit a7fa2349505549b82f32a4d7035b88bad6cda637. P000/ACTIVE worldview and portable protocol remain unchanged. These are auxiliary finite dual-law probability models, not native X6 or empirical physics claims. At this run, the service reported research_authority_granted=false, UPSTREAM_CODE_REVIEW_REQUIRED, and active owner lookup returned CONTROL_QUOTA. This author-side PR evidence is not a Source claim, Result, or independent review.

## Research question and result

Keep the prior nonfrozen two-stage nature tree: two positive origins, time-2 collision of A1/B1 at L=1, time-3 collision of A11/B11 at L=2, and optional stops at times 1,2,3 (forced stop at 4). Can terminal errors be chosen strictly positive so the signed FULL/LR support gap disappears while real-image membership is still checked rather than assumed?

Yes: an explicit *source/likelihood-ratio-dependent* family of terminal Bernoulli rates yields **identical FULL and seedless-LR convex hulls, and identical actual real four-observer images**. This demonstrates exact hull equality is attainable after two genuine nonfrozen collisions, but this rate family cannot solve the mother problem's unequal-image requirement.

## General lemma — hypercube-edge winding surjectivity

Let F:[0,1]^n → R² be continuous and separately affine in every coordinate. Let P be the convex hull of its 2^n binary-corner images, and assume P is a nondegenerate convex polygon. For each boundary edge E of P let G_E be the subgraph of the binary hypercube induced by all corners v with F(v)∈E, with edges between Hamming-distance-one corners. If every G_E is connected, then

F([0,1]^n) = P.

**Proof.** Repeated affine interpolation gives exactly

F(x)=∑_{v∈{0,1}^n} F(v) ∏_{i=1}^n [x_i if v_i=1 else (1−x_i)].

The weights are nonnegative and sum to one, hence F(cube)⊆P. Choose one binary preimage for each polygon vertex; it also lies in the corner set of both neighboring edges. For each consecutive polygon vertex pair, graph connectivity supplies a hypercube-edge walk joining those representatives with every visited corner mapped to that polygon edge. On a domain hypercube edge F is affine, so its image is a straight segment inside the same polygon edge. Concatenate these walks around the polygon. The resulting closed loop in the cube maps to a curve running around the entire polygon boundary once, possibly with harmless backtracking; its winding number about every interior point is 1. Every loop in a cube is contractible. If any interior point y of P were missing from F(cube), this would contract its boundary winding-one image loop in R²\{y}, which is impossible by homotopy invariance of the winding number. Continuity also covers each whole polygon edge. Thus P⊆F(cube). QED.

The hypothesis is sufficient, not necessary; arbitrary multi-affine planar images need not be convex. Relevant established background is multi-affine corner interpolation and the winding-number/degree invariant, for which see https://en.wikipedia.org/wiki/Multilinear_polynomial and https://en.wikipedia.org/wiki/Degree_of_a_continuous_mapping. No novelty-priority claim is made for the general topology.

## Two-law change-of-measure gauge (exact BRC positive mass reuse)

At a stopped history h let L(h)=P(h)/Q(h)>0. Every stopped history cylinder has positive Q/P path mass and preserved source provenance. For any bounded stop time τ and scalar g(t),

E_P[g(τ)/L_τ] = E_Q[g(τ)],
E_Q[g(τ)L_τ] = E_P[g(τ)].

To prove it, partition into disjoint stopped history cylinders and substitute P(h)=L(h)Q(h) term by term. This is true for all real FULL or seedless-LR behavioral policies, including 0/1 hazards and unreachable branches. It is a probabilistic observer identity rather than a physical amplitude or native-heartbeat operator.

Define strictly positive P-law and Q-law terminal error Bernoulli rates at time t and history h by

p_t(h)=1/5 + t/20 + (t+1)/(100 L(h)),
q_t(h)=2/5 − t/30 + (t+2)L(h)/200.

At forced time 4 there is no new random event: L_4 equals the leaf LR at time 3. For all nodes 1≤t≤4 and 5/18≤L≤15/4; therefore 0<p_t≤29/50<1 and 0<q_t≤41/80<1, with each kernel genuinely depending on LR at fixed time. The three optional stopping stages affect (T_P,T_Q), hence affect the original observation vector.

For O=(e_P,e_Q,T_P,T_Q), the identities above yield for every real policy

e_P = 21/100 + T_P/20 + T_Q/100,
e_Q = 41/100 + T_P/200 − T_Q/30.

Consequently O=A(T_P,T_Q), where the injective affine map A:R²→R⁴ is

A(u,v)=(21/100+u/20+v/100, 41/100+u/200−v/30, u, v).

The four original observer coordinates are retained, with explicit rank-two specialization. This construction never discards path/source labels before the exact measure-change audit.

## Fixed positive nonfrozen nature tree

Roots: P(A)=1/3, P(B)=2/3; Q(A)=2/3, Q(B)=1/3. For Y=1, the (P,Q) conditional probabilities are (1/2,1/4) at A and (1/4,1/2) at B. For Z=1, the (P,Q) conditional probabilities at A1, B1, A0, B0 are respectively

(1/2,1/4), (2/3,1/3), (1/2,2/5), (1/2,3/5).

All complementary event probabilities are strictly positive. L(A1)=L(B1)=1 at time 2; L(A11)=L(B11)=2 at time 3; all remaining keys and explicit P/Q masses are computed in VERIFY.py. The colliding A1/B1 second-stage conditionals differ, making the continuation information genuinely source-sensitive.

There are 14 binary FULL decision keys (two roots, four Y histories, eight Z histories), versus 12 unique (time,exact LR) seedless-LR decision keys. Each potential path visits each decision key at most once, making the time observation F=(T_P,T_Q) separately affine in all real stop hazards. Its convex hull is exactly the hull of 2^14 or 2^12 deterministic corner images.

The accompanying standalone Python Fraction verifier **actually enumerates all 16,384 FULL corners and all 4,096 LR corners**, including unreachable choices. They produce 572 and 272 distinct two-law time pairs respectively. Both exact convex hulls are the same nondegenerate 13-vertex polygon P. For each consecutive boundary edge, the exact graph of all LR optimal binary corners is connected, with cardinalities, in cyclic polygon order:

[1152, 80, 24, 8, 5, 2, 2, 5, 8, 20, 80, 128, 1088].

VERIFY.py explicitly confirms for each of the 13 edges (i) all 16,384 FULL corners satisfy its rational support inequality; (ii) LR optimal corners attain both endpoints; (iii) BFS with single-bit flips reaches every optimal corner. The full polygon vertex list and every rational edge threshold are in EXACT_OUTPUT.txt. These finite assertions are exact rational checks, not direction sampling.

Applying the winding lemma to the real LR time-observer map gives O^time_LR=P, the *entire real time-pair image*. Since every real FULL time pair belongs to the common deterministic convex hull P and FULL includes all LR policies, O^time_FULL=P as well. Applying the same injective affine A gives the rigorous real-image identity

O_FULL = O_LR = A(P),

so in particular conv(O_FULL)=conv(O_LR) in R⁴ **for all real behavioral stop probabilities**, including zero/one and zero-reach cases. Thus this explicitly nonfrozen, doubly colliding, strictly positive example passes the all-signed hull equality test, but the entire images also coincide: it is a controlled *no-go baseline* rather than the mother target. The image has affine dimension 2 and no claim of four-dimensional interior is made.

## Execution, validation scope, next concrete question

VERIFY.py depends only on Python standard-library fractions.Fraction and itertools. It checks strictly positive/normalized nature kernels, both exact LR collisions, 20,480 deterministic policies, law-specific Bernoulli rates in (0,1), affine four-observer identities by direct path summation, common 13-vertex hull, 13 exact signed support facets and each complete optimal-corner graph. ACTUAL stdout in EXACT_OUTPUT.txt ends PASS_EXACT_R5_DOUBLE_COLLISION_WINDING_IMAGE_EQUALITY. The continuum claim follows from two proved algebraic/topological lemmas and these exact exhaustive finite checks. The model-dependent finite certificate is not a universal theorem for all trees; project-native X6 transfer, Source admission, independent review and originality checking remain separate obligations.

**Next**: preserve the nature tree and modify terminal errors with small strictly positive rational history-specific perturbations that distinguish sources *inside* the colliding LR fibers. Before using semialgebraic nonmembership, require exact full four-dimensional hull equality by checking every FULL deterministic observer against LR hull using rational ≤5-vertex combinations or Farkas certificates. Any strict signed gap rejects that perturbation. For hull-equal nonplanar candidates, analyze exposed-face LR binary-corner connected components and their exact attainable intervals. Disconnectedness alone is not nonmembership; verify an actual component-range gap or perform certified real quantifier elimination, including boundary and unreachable policies.
