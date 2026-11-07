# R5: Three LR keys, origin-preserving four-moment observation and an exact equal-hull/different-image example

Date: 2026-10-29 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED. This is an **author-side portable mathematical result**, not a Source CLAIM or an independently accepted theorem.

## Target and scope

The R5 mother problem remains: an absorbing finite strictly positive dual-measure stopping experiment, with precisely the four observers (e_P,e_Q,T_P,T_Q), such that FULL history and seedless likelihood-ratio (LR) policy images have equal convex hulls but different *actual* real-behaviour images. Previous source at enterprise-math commit c04b177790428bfc01e982084e10ebfd12caa4b4 excludes one source-sensitive double merger and proves rigidity in a specified two-key envelope.

Here we prove an adjacent but **distinct** full counterexample with three decision keys and the four *joint moments* (E[B1],E[B2],E[B3],E[B1B2B3]). These are not the original stopping observers; the actions below are nonabsorbing binary reports. The result therefore establishes an exact BRC provenance/moment interface and a next-step test, not a solution of the stopping mother problem.

Pinned sources: GLOBAL_KNOWLEDGE_V1 main@16d23aa8d6f1b8079f1b183a5e27e81398c4010f; Enterprise Math main@f646634cd1a6c4f9f659180bf15a743b02871864. Canonical global entries, P000, ACTIVE worldview, source joint-observer preservation, positive weighted BRC and portable research protocols were read. P000 is unchanged.

## Model and exact LR collision

First nature draws an observed provenance label S in {A,B} with P(S=A)=P(S=B)=Q(S=A)=Q(S=B)=1/2. At each time j=1,2,3 the policy chooses binary action Bj; there is no absorption. FULL remembers S and earlier actions. Seedless LR can condition only on (j,r_j), with fresh behavioural coins and no carried random seed. Last, at t=4, nature produces independent Bernoulli Z with strictly positive kernels P(Z=1)=2/3, P(Z=0)=1/3 and Q(Z=1)=1/3, Q(Z=0)=2/3. The ordered (S,Z) exogenous atom weights A0,A1,B0,B1 are (1/6,1/3,1/6,1/3) under P, (1/3,1/6,1/3,1/6) under Q. All exogenous kernels and weights are strictly positive. Zero action probabilities under deterministic policy are not zero *nature* kernels.

Up through the three decisions, P and Q coincide on the source and every preterminal action history: the same policy factors occur under both measures and cancel in likelihood ratios. Thus r_j=1 on every reachable positive history, and all origins/action histories collide at the same LR key for each time j. At terminal Z the LR may become 2 or 1/2, but no further decision occurs.

The declared four-dimensional observer is M(pi)=(E_Q B1,E_Q B2,E_Q B3,E_Q(B1B2B3)). P gives the same preterminal moments. The fourth coordinate is a genuine three-way *joint* observer; collapsing the three Bernoulli marginals loses it. This is a finite BRC origin/word-mass model, not native X6 dynamics.

## Theorem 1 — exact all-signed hull equality

Let V_b=(b1,b2,b3,b1b2b3) for b in {0,1}^3, and let H=conv{V_b}. For a seedless LR behavioural policy, write its three independent probabilities as x,y,z in [0,1]. Since the only LR key at each time is (j,1), the three fresh coins yield

M_LR = {F(x,y,z): (x,y,z) in [0,1]^3},   F(x,y,z)=(x,y,z,xyz).

Every F(x,y,z) is a convex mixture of the eight V_b using the nonnegative Bernoulli product weights ∏_j x_j^bj (1−x_j)^(1−bj). Every V_b is reached by one deterministic LR policy. Therefore conv(M_LR)=H.

Every FULL policy, including source- and history-dependent behavioural policies, induces a probability distribution lambda_b over the eight action words; M_FULL is its linear image Σ_b lambda_b V_b, hence is contained in H. Conversely any distribution on the three-bit words is implemented by a perfect-history behavioural strategy using the ordinary probability chain rule: choose B1 according to its marginal, then B2 conditioned on B1, then B3 conditioned on B1,B2 (unreached histories are arbitrary). Therefore **M_FULL=H**. Thus

conv(M_FULL) = conv(M_LR) = H,

and for *every real signed w in R^4*, min_FULL w·M = min_LR w·M = min_b w·V_b, with analogous equality for maxima. No finite scan of directions is needed.

This also gives a rational two-vertex certificate for each of the 64 deterministic source-conditioned policies: if origin A chooses action word a and B chooses b, the observer is (V_a+V_b)/2. Every such FULL vector is explicitly in H.

## Theorem 2 — complete exact FULL polytope

H is precisely the set of (x,y,z,t) satisfying

0≤x,y,z≤1,    0≤t≤min(x,y,z),    t≥x+y+z−2.

Necessity follows from indicator inequalities 0≤B1B2B3≤Bj and B1B2B3≥B1+B2+B3−2.

For sufficiency, if t=1 then x=y=z=1 and the point is V_111. If 0≤t<1, assign mass t to 111 and put a_j=(x_j−t)/(1−t) for the remaining distribution. The inequalities yield 0≤a_j≤1 and Σa_j≤2. The truncated cube {a in [0,1]^3 : Σa_j≤2} has exactly the seven integral corners other than 111: if two coordinates were fractional they could be oppositely perturbed on the active sum face; if only one were fractional while the sum were the integer 2, integrality of the other two would force it integral. Hence a is a convex mixture of words with ≤2 ones. Add the 111 mass t. For rational inputs, this construction admits rational weights. QED.

## Theorem 3 — explicit nonmembership and exact distance

Let FULL choose word 000 deterministically on source A and 111 deterministically on source B. Both origins have positive mass 1/2. It yields

C=(1/2,1/2,1/2,1/2)=(V_000+V_111)/2 in M_FULL.

Any LR policy matching its first three coordinates has x=y=z=1/2, hence fourth coordinate xyz=1/8≠1/2. Equivalently the **nonlinear polynomial image certificate** R(x,y,z,t)=t−xyz vanishes on every real LR observer but R(C)=3/8.

More strongly, write δ* for the unique root in [0,1/2] of (1/2+δ)^3=1/2−δ. Monotonicity and exact rational signs give 1/6<δ*<3/16. If an LR point were at L∞ distance δ from C, its first three coordinates would be at most 1/2+δ and fourth at least 1/2−δ, so δ≥δ*. Equality is attained with x=y=z=1/2+δ* and xyz=1/2−δ*. Consequently

dist_infinity(C, M_LR)=δ*≈0.182327803828 > 1/6.

This is equality of **all linear supports** with strict difference of actual real behavioural images. Both claims hold for every real policy probability in the stated model. The joint moment is necessary to see the residual.

## Theorem 4 — reusable Jacobian criterion, and stopping-chain boundary

For an at-most-k-key seedless LR policy whose polynomial observer map F:[0,1]^k→R^d has k<d, the LR image has zero d-dimensional Lebesgue measure: a Lipschitz image of O(n^k) subcubes of radius O(1/n) has total d-volume O(n^(k−d))→0. If d independent FULL behavioural parameters have a nonsingular d×d Jacobian at an interior point, the inverse function theorem makes the FULL image contain a nonempty open d-dimensional subset. Thus the actual images differ. **If separately one proves all-signed hull equality**, this gives a complete observer-image/hull separation test without general quantifier elimination.

Here FULL can use independent source-specific triples a,b with G(a,b)=(F(a)+F(b))/2. At a=(1/4,1/4,1/4), b=(3/4,3/4,3/4), the 4×4 Jacobian submatrix using parameters (a1,a2,a3,b1) has rows

(1/2,0,0,1/2);
(0,1/2,0,0);
(0,0,1/2,0);
(1/32,1/32,1/32,9/32).

Its exact determinant is 1/32>0. FULL already has four-dimensional interior within this source-conditioned subclass; LR remains a 3D polynomial graph.

**Boundary for the actual stopping target.** In an absorbing no-bypass *single chain* of three LR stop/continue keys K1→K2→K3, the earliest deterministic stop (K1, K2, K3 or never) determines the only effective deterministic policy outcome. Therefore the LR polytope has at most four distinct deterministic observer vectors and affine dimension at most three. If its FULL and LR hulls agree, the 4D-volume/Jacobian test cannot apply. This does *not* prove their actual sets coincide inside that 3D hull. To apply the rank test to four stopping observers requires sufficient bypass/reachability interaction to produce at least five affinely independent LR vertices.

## Verification and exact scientific boundary

The standalone Python Fraction code VERIFY.py was executed; EXACT_OUTPUT.txt contains the actual output PASS_EXACT_R5_THREE_KEY_SOURCE_MOMENT_HULL. It checks: all four positive exogenous P/Q atoms and normalization; 8 deterministic LR and 64 source-conditioned FULL policies; 625 signed test directions in {-2,-1,0,1,2}^4 (regression only); exact source witness, R(C)=3/8; Jacobian determinant 1/32; and the rational distance-root bracket. The all-real theorems are derived above, not inferred from 625 directions.

BRC resolution: REUSE_APPLIED (typed positive origin/word masses and provenance-retaining joint observer); no native BRC/X6 solver was run. Source ownership query returned CONTROL_QUOTA; native CLAIM/Result/independent Driver review are not established. Not assessed: literature novelty, exact original stopping-observer realization, native geometry/physical transfer, formal Lean check.

**Next unit:** Build a true strictly positive P/Q **absorbing stopping** tree with at least three simultaneously consequential time/LR keys and origin/bypass interaction. Enumerate all deterministic LR and FULL vectors of (e_P,e_Q,T_P,T_Q). First certify every FULL vertex is an exact rational convex combination of LR vertices (or return one exact Farkas separator), including all signed directions. On success use the Jacobian rank criterion or an exact polynomial/semialgebraic image witness. Preserve source/path BRC masses and do not substitute the present four moments for the target observers.
