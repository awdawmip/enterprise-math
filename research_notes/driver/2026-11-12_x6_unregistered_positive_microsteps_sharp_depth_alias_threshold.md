# X6 signed-phase observation with unregistered positive-axis microsteps: sharp depth-alias thresholds

Status: DRIVER_MATHEMATICAL_AUDIT / UNIVERSAL EXACT ALGEBRA IN DECLARED CANDIDATE MODEL / NOT_NATIVE_RESULT_ADMISSION
Date: 2026-11-12 (+08)
Related active questions: RS-X6-NATIVE-TIME-DYNAMICS; RS-X6-NATIVE-ROTATION-DYNAMICS. The separate fair-backlog Driver retains actual task dispatch/owner responsibility.

## Contribution and exact scope

This is a new RESEARCH_DRIVER deduction from the already saved X6 time-ordered depth-observability theorem (research_notes/driver/2026-11-12_x6_time_ordered_signed_rotation_depth_observability.md). That theorem assumed the accumulated spatial microstep displacement was known modulo the common diagonal. Here the endpoint displacement is **unknown but restricted to an unrestricted positive-native-axis word of an exact known length**. We prove when the same observed relative endpoint nevertheless uniquely determines the starting common depth and the six-axis step-occurrence vector; and give the first exact collisions when it does not.

Preserve source authorship: the affine X6 Cell torsor, signed-axis primitive adjacency, positive-only BRC multiplicity and 20 joint observers are established in definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md. The global P000 V4 projection and Source P000 V5 distinguish raw signed Cell charts from final nonnegative Cell addresses, native six-dimensional space from time, and primitive triadic-force stability from coordinate adjacency. These results operate on raw signed charts and typed *candidate* transformations, not on an asserted universal native physical rotation or triadic-force law.

## 1. General n-axis theorem

Let n >= 2 and D=(1,...,1) in Z^n. Define q(z)=z-(min_i z_i)D, the exact min-zero relative observer. Fix a known signed permutation g with epsilon=gD containing exactly k negative signs, where 1 <= k <= n-1. Fix any known initial relative chart r=q(z0), and write z0=r+hD with unrestricted integer hidden depth h. First apply g; afterwards perform an unknown positive-only native step word of exactly M >= 0 unit increments, whose occurrence vector b lies in

    B_M={b in Z_{≥0}^n : sum_i b_i=M}.

Observe the full relative endpoint

    Y(h,b)=q(gr+h epsilon+b).

Word order is **not** observed. Its native positive-only BRC multiplicity at b is M! / product_i b_i!.

Define

    d_min = n / gcd(n,2k),
    M_crit = 2k(n-k) / gcd(n,2k).

**Sharp theorem.** For every fixed r and g as above, (h,b) -> Y(h,b) is injective on Z x B_M exactly when 0 <= M < M_crit. If M >= M_crit, there exist two different depths and two distinct positive-only occurrence vectors with the same entire n-coordinate relative readout. The threshold is sharp and independent of r. For a restricted nonempty depth set H subset Z, the same map on H x B_M is injective exactly when there is no nonzero d in H-H such that

    n divides 2kd, and
    M >= 2k(n-k)|d|/n.

The statement is unconditional *within the declared positive-only, post-rotation, fixed-word-length coordinate candidate model*. It also identifies when path **occurrence vectors** can be recovered; ordered primitive path words retain their separate branch identity/multiplicity.

### Proof

Equality q(x)=q(x') holds precisely when x-x'=cD for some integer c. Let d=h-h'. Therefore Y(h,b)=Y(h',b') iff

    d epsilon + (b-b')=cD.

Since both occurrence vectors sum to M, summing all n coordinates gives

    c = d(n-2k)/n.

Consequently the necessary and sufficient difference vector is

    b-b'=d[(n-2k)/n D - epsilon].

On each of the k negative-sign coordinates this is +2d(n-k)/n, and on each of the n-k positive-sign coordinates it is -2dk/n. Because n divides 2dk iff it divides 2d(n-k), integrality is equivalent to n | 2kd. For nonzero d its smallest possible magnitude is d_min.

For d>0 the positive and negative parts of the required difference vector each have total mass

    C(d)=2k(n-k)d/n.

A pair of nonnegative occurrence vectors of common total M with this difference exists iff M >= C(d): take the positive part and negative part of the difference (each has total C(d)), then append any common nonnegative vector of total M-C(d). If M<C(d), nonnegativity of b,b' forbids the difference. The negative-d case is symmetric. At d=d_min the minimal collision length is M_crit=C(d_min), giving the claimed threshold. For fixed h, the difference b-b'=cD has sum zero, hence c=0 and b=b', establishing uniqueness of b once h is known. Restriction to H simply restricts available nonzero d. QED.

## 2. Exact X6 C6 phase specialization

Use the previously published signed triad candidate R_123(z1,z2,z3,z4,z5,z6)=(-z3,z1,z2,z4,z5,z6). Its ordered phase prefix R^t D has k_t=1,2,3,2,1 negative signs for t=1,2,3,4,5; t=0 and t=6 have uniform signs and are depth-blind even with M=0.

For one registered nontrivial phase, with an **unknown M-step positive-only word applied after that phase**, the precise thresholds are:

| Registered phase t (mod 6) | Number k_t of negative signs | Earliest ambiguity length M_crit | Smallest nonzero colliding depth gap |
|---|---:|---:|---:|
| 1, 5 | 1 | 5 | 3 |
| 2, 4 | 2 | 8 | 3 |
| 3 | 3 | 3 | 1 |

For example at t=1, r=0, epsilon=(-1,1,1,1,1,1), M=5, two full histories are

    h=3, b=(5,0,0,0,0,0)
    h'=0, b'=(0,1,1,1,1,1).

They give exactly the same full min-zero observed endpoint, namely (0,1,1,1,1,1). Their positive-only ordered-word multiplicities are respectively 1 and 120. No path order is assumed erased by the carrier; it is merely absent from this endpoint observer.

At phase t=2 (k=2), a sharp collision at M=8 uses d=3 and occurrence vectors (4,4,0,0,0,0) versus (0,0,2,2,2,2). At phase t=3 (k=3), a sharp collision at M=3 uses d=1 and vectors (1,1,1,0,0,0) versus (0,0,0,1,1,1). For t=4,5 permute the negative coordinates accordingly. Adding a common positive occurrence vector extends each collision to all larger M. These collisions hold for every known r, because the common gr term cancels.

A finite-depth repair follows immediately: at phases t=1,2,4,5, if the admissible depth set H has no pair differing by a nonzero multiple of 3, then depth and occurrence vector remain exactly recoverable for every positive word length M. At phase t=3, an H containing consecutive depths admits the first collision at M=3.

## 3. Reproducible exact supplementary enumeration

All calculations use integer vectors, min-zero subtraction, binomial compositions and dictionary equality, without floating point or any assumed source code execution by the research console. For k=1,2,3,4,5 and each M from 0 through M_crit-1, exhaustively enumerated all C(M+5,5) occurrence vectors and all h in {-4,-3,...,4}, checking that no two different (h,b) produce the same six-coordinate readout. The numbers of checked distinct input pairs across those subcritical M are, respectively:

    k=1: 1890
    k=2: 15444
    k=3: 252
    k=4: 15444
    k=5: 1890

All 34,920 subcritical enumerated pairs were unique within the corresponding (k,M) observation fiber. Constructed and checked the exact threshold collisions listed above for every k; additional direct search over M=0,...,9 and h=-4,...,4 found first collisions exactly at 5,8,3,8,5. These computations supplement the general proof rather than replace it.

## 4. New joint-phase recovery theorem: two ambiguous readouts can be jointly exact

Consider a finite nonempty collection S of registered **phase probes** with known signed permutations g_t, mixed-sign epsilon_t=g_tD and k_t negative entries. At each probe, independently choose an unknown positive-only occurrence vector b_t with known length M_t, and observe

    Y_t=q(g_t r+h epsilon_t+b_t).

The same hidden initial depth h is used in all probes, but the post-phase positive words are independent unknown choices. Define

    d_t = n/gcd(n,2k_t),
    C_t(d) = 2k_t(n-k_t)|d|/n whenever d is a multiple of d_t,
    d_joint = lcm_{t in S} d_t.

**Joint theorem.** The full map (h,(b_t)) -> (Y_t) is injective exactly when there is no nonzero integer d divisible by d_joint such that M_t >= C_t(d) for **every** sampled t. Equivalently, for unrestricted h in Z the full map is injective iff **at least one t** satisfies

    M_t < 2k_t(n-k_t)d_joint/n.

When noninjective, sharp simultaneous collisions exist at depth gap d_joint and can be extended to larger word lengths by common-step padding independently in each probe. For a fixed finite H, replace the possible d values by nonzero members of H-H.

Proof: Equality of joint readouts requires equality for each t with the same depth difference d. The single-probe theorem gives exactly d in d_t Z and M_t >= C_t(d). Intersection of these integer divisibility conditions is d in d_joint Z. Each C_t is positive and linear in |d|; consequently the earliest possible collision uses |d|=d_joint. When every bound is satisfied, construct the positive and negative parts of the required difference separately at each probe. Conversely, any violated length bound or divisibility condition excludes all joint collisions. For fixed h, each observed Y_t and length M_t uniquely determines b_t by the previous fixed-depth argument. QED.

**Exact two-phase X6 witness.** Probe R^1 (k=1) after M_1=5 positive steps, and R^3 (k=3) after M_3=3 positive steps. Each probe is individually noninjective (their thresholds are 5 and 3), but d_joint=lcm(3,1)=3. The phase-3 probe requires M_3>=9 to alias a gap of three, so the pair is jointly injective for (M_1,M_3)=(5,3), for every initial r. It first admits a simultaneous ambiguity at (5,9), using the sharp single-probe phase-1 vector pair above at depth gap 3 and the phase-3 pair (3,3,3,0,0,0) versus (0,0,0,3,3,3).

Supplementary exact check at (5,3), r=0: for each h in {-4,-3,...,4} enumerated 252 possible phase-1 and 56 possible phase-3 occurrence vectors, i.e. 127,008 joint input records. For individual probes, pairwise readout sets overlap for depth differences 3 and 1 respectively. For all 36 pairs of distinct depths in the tested range, the **joint** readout sets have empty intersection, as the universal criterion predicts.

The independent-probe hypothesis is deliberately typed. A physically continuous Heartbeat path may correlate successive b_t values; its realizable histories form a subset of these product families, so joint injectivity proved here also holds for that subset whenever the registered per-probe displacement representation applies. Conversely, the constructed independent-probe collisions should be tested for path coherence before being asserted as a physical multi-time ambiguity.

## 5. Relation to formal X6/Heartbeat research and next test

The previous time theorem proved phase observation detects hidden common depth if the registered affine shift b is known modulo Delta. This theorem identifies the precise first loss of that recovery when **only post-phase positive-word length** is registered, and produces explicit finite-state ambiguity witnesses. The resulting readout determines the unsigned positive-axis *occurrence vector* below the threshold, but ordered words remain separate native Path-formal/BRC records. A positive word of M steps is still composite whenever more than one axis is used.

The next discriminating native question is whether a particular Source-pinned registered triadic-force/Heartbeat update actually permits these post-rotation positive-only word families and which phase labels/branch records remain registered. If the admissible set is smaller or state-dependent, compute the exact difference-set collision criterion for that typed set rather than infer universal nonidentifiability. Keep non-STAR triad carrier status, real time/force state, author history and the original TASK owner/CLAIM obligations separate.

Evidence lineage: definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json; definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json; definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md; research_notes/driver/2026-11-12_x6_signed_triad_c6_group_and_brc_path_fiber_action.md; research_notes/driver/2026-11-12_x6_signed_rotation_relative_observer_depth_descent.md; research_notes/driver/2026-11-12_x6_time_ordered_signed_rotation_depth_observability.md.

Formal status: a new mathematical audit/proved candidate-model auxiliary result. No Source-native Result admission, independent DR, formal Task completion, or mother Objective completion is asserted by this file.
