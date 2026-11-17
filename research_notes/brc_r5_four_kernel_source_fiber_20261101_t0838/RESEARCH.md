# R5 — Complete four-kernel source-fiber obstruction for genuine time–likelihood-ratio decisions

**2026-11-01, Asia/Shanghai. Scientific status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.** This is an auxiliary stochastic stopping theorem; it is neither a native X6 theorem nor an accepted solution to the unrestricted four-observer mother question.

## Source pins and lineage

- Frozen GLOBAL_KNOWLEDGE_V1 main: ba9440e1981ad1bd8092bb02224f83b0f338f07e. ACTIVE worldview and the original P000_REALITY_FOUNDATION.json were read at that exact commit; P000 Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc.
- Frozen Enterprise Math main: ce7279d4cafc8d7ddb4a65d75c33e8c40849428c. The applicable AGENTS, P000, portable research protocol and scheduled research operations were read.
- Verified scientific predecessor: PR #1663, commit 96b1587e1d14aadf252b9538fbeb5ef0ef9d305f, research_notes/brc_r5_timeaware_two_law_complete_20261101_t0740/. That model forced P(low|i) = Q(low|i)/2; the present model removes this coupling and permits all four positive binary conditional kernel parameters independently.
- Contributor: this run's own portable author reasoning and exact computation. No earlier session identity, CLAIM, Result or independent reviewer authority has been adopted.

## Full probability and information model

Sources i in {A,B} have prior P(i)=Q(i)=1/2. The two measures P and Q are normalized probability laws on complete source/signal/action/terminal paths. At integer time 1, a stop declares hypothesis P; continuation leads to time-2 source-conditioned signal low/high, with independently chosen strictly positive parameters

    Q(low|A)=a_A,  Q(low|B)=a_B,
    P(low|A)=b_A,  P(low|B)=b_B,
    (a_A,a_B,b_A,b_B) in (0,1)^4.

The high probabilities under each measure are their respective complements. Time-2 low: stop declares P at time 2, continue declares Q at time 3. Time-2 high: stop declares Q at time 2, continue declares P at time 3. Every time-3 decision is terminal.

FULL knows the source i, signal and time. The seedless LR policy knows exactly (integer time, dP/dQ for that reached history); time1 has key (1,1), time2 low_i has (2,b_i/a_i), and time2 high_i has (2,(1-b_i)/(1-a_i)). Whenever any such keys coincide, LR must share one stop probability at all associated histories. Each behavioral action is freshly sampled when its reached decision node is visited, with no persistent seed. A sample path visits time1 and at most one time2 node, so no key can be revisited within a path. Therefore the observer map is multi-affine in distinct policy parameters; every deterministic corner suffices to generate the corresponding *convex hull*, not necessarily the real behavioral image itself. FULL has 64 deterministic strategies; LR has 2^(1+k) where k is the number of distinct time2 LR keys, hence 2 through 32.

Retain exact positive source-, signal-, decision-port- and time-labelled BRC probability masses under BOTH P and Q until the declared observer projection; no source averaging is done before proving a valid quotient. This is a typed BRC path-flow use, not signed amplitude, spatial X6 dynamics or an extra native coordinate dimension.

The genuine four observables are

    O=(e_P,e_Q,T_P,T_Q),
    e_P=P(declare Q), e_Q=Q(declare P),
    T_P=E_P[terminal time], T_Q=E_Q[terminal time].

The letters P/Q in "declare P/Q" are hypothesis labels.

## Main theorem: ALL REAL FOUR-KERNEL PARAMETERS

For every a_A,a_B,b_A,b_B in (0,1), put theta_Q=(a_A+a_B)/2 and theta_P=(b_A+b_B)/2. Denote FULL and LR real-policy observation images by F,L.

**(I) Exact dual signed Bellman support identities valid for every possible time2 LR key collision:**

    C_Q(O)=T_Q+(1+theta_Q)e_Q
    min over L C_Q = 2+theta_Q
    min over F C_Q = 2+theta_Q-|a_A-a_B|/4

    C_P(O)=T_P-(1+theta_P)e_P
    min over L C_P = 1
    min over F C_P = 1-|b_A-b_B|/4.

Hence unequal Q source kernels force a strict convex-hull support gap |a_A-a_B|/4; unequal P source kernels force a gap |b_A-b_B|/4. The corresponding FULL witness to the entire LR hull has L-infinity distance at least |a_A-a_B|/[4(2+theta_Q)] or |b_A-b_B|/[4(2+theta_P)], respectively. The two inequalities may concern different FULL policies.

**(II) If a_A=a_B=a and b_A=b_B=b with a different from b**, then FULL and LR have *exactly the same real-behavior four-observer images*, and their common affine rank is exactly 3. In this case the time2 low and high LR keys are distinct and source-independent.

**(III) If a_A=a_B=b_A=b_B=alpha**, then the time2 likelihood keys coincide (both equal 1). FULL/LR convex hulls differ strictly. LR's affine rank is precisely 2 when alpha differs from 2/3, and precisely 1 at alpha=2/3.

**Complete classification:** conv(F)=conv(L) if and only if (a_A,b_A)=(a_B,b_B)=(a,b) with a different from b. Whenever convex hulls are equal, the LR affine rank is 3. Thus this ENTIRE open four-dimensional family has no instance with both full LR rank 4 and equal four-observer convex hulls. This is a model-specific no-go; the unrestricted original mother question is open.

## Proof of I — explicit two-law source-fiber support

Minimize C_Q under Q. On low at time2, the two costs are 3+theta_Q (stop: declare P, time 2 plus error penalty) and 3 (continue: declare Q at time 3), so continue is optimal. On high, the costs are 2 (stop: declare Q at time 2) and 4+theta_Q (continue: declare P at time 3), so stop is optimal. Both inequalities are strict for all theta_Q in (0,1). Thus if source i with prior Q mass 1/2 continues at time1, its total Q cost is (3 a_i + 2(1-a_i))/2 = 1 + a_i/2. Stopping at time1 costs (2+theta_Q)/2 = 1+theta_Q/2. FULL chooses by source:

    min_F C_Q
       = 2 + [min(a_A,theta_Q)+min(a_B,theta_Q)]/2
       = 2+theta_Q-|a_A-a_B|/4.

For LR, time1 action is *common* to the two sources, irrespective of any downstream key collisions. Even allowing an artificially enlarged LR class to distinguish all time2 source signals, the cost is bounded below by min(2+theta_Q,2+(a_A+a_B)/2)=2+theta_Q. The genuine LR strategy stop at time1 for both sources attains that bound. Therefore min_L C_Q=2+theta_Q.

Minimize C_P under P. On low, costs are 2 (stop) and 2-theta_P (continue, error P(declare Q)); on high, costs are 1-theta_P (stop, error P(declare Q)) and 3 (continue). Thus, for every source, low must continue and high must stop for a Bellman minimum. If source i continues at time1, its P cost is [b_i(2-theta_P)+(1-b_i)(1-theta_P)]/2=(1-theta_P+b_i)/2. A time1 stop costs 1/2. FULL hence has

    min_F C_P
       = [min(1,1-theta_P+b_A)+min(1,1-theta_P+b_B)]/2
       = 1-|b_A-b_B|/4.

The relaxed common-time1 LR minimum is min(1,1-theta_P+(b_A+b_B)/2)=1. Again the genuine LR stop-at-time1 policy attains 1, proving min_L C_P=1.

A linear functional has the same extrema on an image and its convex hull. For witness w minimizing C_Q in F and v in conv(L), C_Q(v)-C_Q(w) >= |a_A-a_B|/4. Since the coefficient l1 norm of C_Q is 2+theta_Q, this yields ||v-w||_infty >= |a_A-a_B|/[4(2+theta_Q)]. The same argument for C_P with coefficient norm 2+theta_P gives the corresponding b-based inequality. Both are exact all-real statements and do not depend on rational interpolation.

## Proof of II — exact real behavioral aggregation and rank

With common source kernels (a,b), FULL chooses six behavioral probabilities p_A,p_B,l_A,h_A,l_B,h_B in [0,1]. Let s=(1-p_A)+(1-p_B). Define p=(p_A+p_B)/2; for s>0, define

    l=[(1-p_A)l_A+(1-p_B)l_B]/s,
    h=[(1-p_A)h_A+(1-p_B)h_B]/s.

For s=0, define l=h=0. Clearly p,l,h all lie in [0,1]. The law-independent survival weights work under BOTH P and Q because the two source priors are both 1/2 and the conditional P and Q kernels do not depend on source. The LR behavioral policy with time1 p, low l, high h exactly replicates *all* P and Q source-aggregated terminal decision/time masses. This yields F subset of L, and L subset of F by strategy inclusion, so F=L as actual real images.

Let f_l=(1-p)l and f_h=(1-p)h. Their feasible set is the convex polytope

    0<=p<=1,  0<=f_l<=1-p,  0<=f_h<=1-p.

Every observer coordinate is affine in these three aggregates, so rank is at most three. The three columns of observer variation in (e_P,e_Q,T_P) are

    [ -b,  -b,  1-b ]
    [  a,   a, -(1-a)]
    [ -2,  -b, -(1-b)].

Their determinant is (a-b)(2-b), nonzero for 0<a,b<1 and a different from b. Thus LR affine rank is exactly 3, and the aggregate behavioral image is convex.

## Proof of III — collision of low/high when P=Q

When all four kernels equal alpha, the two laws agree on the entire sample path space; both time2 LR keys are (2,1). Thus LR has a common time1 stop parameter p and a single time2 stop parameter q across *both* low and high signals. Every LR real policy satisfies

    e_P=(1-p)[alpha(1-q)+(1-alpha)q],  e_Q=1-e_P,
    T_P=T_Q=1+(1-p)(2-q).

Put m=min(alpha,1-alpha)>0. Then e_P >= m(1-p), whereas T_P <= 1+2(1-p), so every LR policy satisfies the signed *linear* support inequality

    T_P-(2/m)e_P <= 1.

As this is linear, it also holds throughout conv(L). But a valid deterministic FULL strategy continues at time1, stops at time2 on low, continues at time2 on high. It has e_P=0 and T_P=3-alpha>1, violating the LR inequality strictly. Therefore the convex hulls are different, including at the equal-P/Q parameter.

Since e_Q=1-e_P and T_Q=T_P, the LR affine rank is that of the 2-coordinate (e_P,T_P) image. The LR convex hull has exactly the three distinct candidates (0,1), (alpha,3), (1-alpha,2) for (p,q) deterministic corners, the other fourth corner repeating (0,1). The determinant of the two difference rows is 3alpha-2. It is nonzero except at alpha=2/3, giving affine rank 2 away from that point and rank 1 there.

The three cases cover the entire open real parameter cube, completing the classification.

## Exact executed verifier and concrete four-dimensional example

The accompanying VERIFY.py was actually executed using Python standard-library fractions.Fraction and its literal result is saved as EXACT_OUTPUT.txt. It exhaustively enumerates 64 deterministic FULL policies and 2–32 LR deterministic policies for each of 81 rational quadruples from the fully independent 3^4 grid, including 57 cases with genuine LR time2 key collisions, and checks both Bellman support identities and probability/time bounds. It also executes 46,875 exact real-policy source-aggregation checks on three distinct common P/Q kernel pairs, three rank minors, and four equal-law rank/bifurcation checks. The finite coverage corroborates the preceding fully analytic proof, not a substitute for its all-real quantification.

A strictly positive witness with rank4 uses (a_A,a_B,b_A,b_B)=(1/4,1/2,1/8,1/3). Its time2 LR keys are 1/2,7/6,2/3,4/3, distinct. LR has 32 deterministic policies and a 4x4 difference determinant exactly 1/2048. One legal FULL policy continues source A and stops source B at time1, continues low A, and stops high A, giving

    O_FULL=(1/2,1/2,25/16,13/8),
    C_Q support gap=1/16,
    C_P support gap=5/96.

The FULL witness realizes the Q support minimum and lies at L-infinity distance at least 1/38 from the entire LR hull. The P gap may use another FULL witness. All arithmetic is exact; no floating point or numerical optimality inference appears.

## Control boundary and next research unit

Native gateway em_status at this run returned research_authority_granted=false, executor_binding_configured=false, and 5/5 native active job quota. A read-only canonical active-owner/task query returned CONTROL_QUOTA, so active Owner could not be confirmed. This write is author-side portable evidence, not a formal CLAIM, frozen Result, independent Driver review or admission. The P000 and ACTIVE worldview remain unchanged, and no native X6 embedding or relation-preservation claim is made. The gateway's older global source pin is not silently equated with the above verified new GitHub GLOBAL_KNOWLEDGE_V1 snapshot.

Continue with a two-merger genuine time/LR stopping model (or a new independent time1 signal), explicitly preserving the BRC source/port ledger, calculating exact LR key fibers, multi-affinity, LR rank and FULL-vs-LR *all-signed* hull relationship. Require exact primal Caratheodory membership certificates or rational separating hyperplanes; if and only if four-dimensional hull equality is proved, investigate certified real-behavior LR nonmembership. Any native transfer requires explicit X6, third slice coordinate, observer and relation preservation.

**Author argument:** complete within the stated auxiliary model; **independent proof review/formal check:** pending; **canonical state-machine admission:** pending. No credential, new shared permission, invented session, or P000 mutation.
