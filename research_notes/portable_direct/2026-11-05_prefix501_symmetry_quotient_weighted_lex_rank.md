# PREFIX-501 — Symmetry quotient and compact weighted-prefix index for dense BRC–KMP–source ranks

Date: 2026-11-05 (Asia/Shanghai). Researcher-ID: EM-DIRECT-A348C4. Native activity: RA-803898F4C7F1A2B7C649652A.
Mode: independent author-side TASK_RESEARCH continuation; no formal task CLAIM, Result, Review or admission.
Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED(n=0..9) / UNREVIEWED / NOT_ADMITTED.
Scientific input pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d (unchanged).
Normative source read separately: global canonical main@76dc1f9b364870b822eae1794ef1e07a87f183e2, Enterprise Math continuation and portable protocol at main@593fbfc92da4662c1e77ae42264fab0ef12e9d65, including P000/ACTIVE worldview and observer-preservation rule.
Predecessors: PREFIX-496 dense joint rank, PREFIX-497 five-color Parikh reduction, PREFIX-499 suffix support, PREFIX-500 modulus-12 support oracle.

## Precise observer and goal

The model is the selected signed five-axis path subfamily inside native X6 (sixth spatial axis occupancy fixed at zero). Alphabet: a,A,b,B,c,C,d,D,e,E. For a path of length n, retain signed five-axis displacement y, exact BRC cancellation observations V=p_b+2p_d+p_e and W=p_c+p_e (p_i=min(number positive i, number negative i)), terminal KMP state q for g in {aab,aba}, and absorbing first-source tag t in {N,B,C}. A future operation appends a native signed direction. The result is a certified compression of this specified observer, not a claim of full path, field, time, or physical-state recovery.

PREFIX-496 ranked the dense reachable states by lexicographic (y_a,y_b,y_c,y_d,y_e,W,V,q,t); PREFIX-500 computes the actual control support C_g(n,y,V,W) with a constant number of integer arithmetic operations for fixed g. The missing operation was weighted prefix summation without materializing every signed base fiber.

## Theorem 1 — exact sign/orbit invariance of controller support

Let u=y_a, v=y_b, c=|y_c|, and s=|y_d|+|y_e|. For every n>=0, integers u,v, c,s>=0, V,W>=0 and every two five-axis displacements y and y' with the same (u,v,c,s),

    C_g(n,y,V,W) = C_g(n,y',V,W) =: K_g(n,u,v,c,s,V,W).

This includes sign changes of y_c and arbitrary redistributions of total absolute displacement s between axes d and e. Equality means equal *sets of realizable (q,t) pairs*, not merely equal cardinalities. Empty sets are included.

Proof. Write each direction's positive/negative occupation as p_i+max(±y_i,0). Given n, V, W and y, with m=(n-sum |y_i|)/2, choose p_d=d, p_e=e and solve

    p_a=m-V-W+d+e, p_b=V-2d-e, p_c=W-e.

All conditions p_i>=0 depend on y only through n, u, v, |y_c| and |y_d|+|y_e|. The five-color Parikh reduction of PREFIX-497 groups letters into (a,b,B,c/C,A/d/D/e/E), with counts

    k_a=p_a+max(u,0)
    k_b=p_b+max(v,0), k_B=p_b+max(-v,0)
    k_c=2p_c+c
    k_x=p_a+max(-u,0)+2(d+e)+s.

Thus the collection of attainable five-color count vectors is identical on every claimed class. The fixed KMP–first-source controller depends solely on five-color words. For any available count vector, every five-color word can be lifted to each corresponding ten-direction occupation vector by assigning the x letters and c/C letters to their prescribed original multiplicities; all words in one color have identical controller transitions. Therefore the attainable (q,t) sets agree. No native information outside the declared observer is identified. QED.

## Corollary 1 — exact orbit-weighted count for the full joint fiber

Let k_g(n,u,v,c,s,V,W)=|K_g(n,u,v,c,s,V,W)| and S_g(n) be the total number of distinct full (y,V,W,q,t) observations. Put rho(0)=1, rho(c)=2 for c>0, tau(0)=1, tau(s)=4s for s>0. Then

    S_g(n) = sum_{u,v,c,s,V,W} rho(c)*tau(s)*k_g(n,u,v,c,s,V,W).

Proof. The signed y_c options have multiplicity rho(c). The integer solutions (y_d,y_e) to |y_d|+|y_e|=s number tau(s): four axis endpoints plus 4(s-1) interior signed assignments when s>=1. Every such displacement supports exactly k_g controllers by Theorem 1. The decomposition is disjoint and exhaustive. QED.

## Theorem 2 — O(n^6)-word dense weighted lexicographic rank/index

For each fixed n>=0 and gate g in {aab,aba}, there is an *explicit* precomputed exact index supporting:

- dense rank of any realizable (y,V,W,q,t) by O(1) integer lookups/arithmetic;
- inverse rank of any integer j in [0,S_g(n)) using O(log(n+2)) integer comparisons/lookups;
- append-and-re-rank of one native direction using an inverse rank at n, the exact BRC/controller step, then a rank at n+1.

The index uses O((n+1)^6) integer words and O((n+1)^6 log(n+2)) bits; precomputing it takes O((n+1)^6) constant-arithmetic-oracle calls plus O((n+1)^6) integer operations. These are fixed-n bounds. For all lengths 0<=n<=N, separate tables occupy O((N+1)^7 log(N+2)) bits.

Construction. Enumerate the feasible six-parameter quotient domain (u,v,c,s,W,V); compute K_g using the exact PREFIX-500 oracle, and store each constant-size sorted controller set and weight k. Build a weighted V-choice prefix row for each (u,v,c,s,W), then a W-choice row for each (u,v,c,s). Define A_g(u,v,c,s)=sum_{W,V} k_g. For each signed prefix (u,v,y_c,y_d), the weight for next signed y_e is A_g(u,v,|y_c|,|y_d|+|y_e|). Form its sorted nonzero y_e-choice row with integer cumulative offsets. Sum these rows upwards to form y_d-choice rows, then y_c-choice rows, y_b-choice rows and the y_a root. Store row lists, nonnegative block weights and cumulative starts. Every row uses disjoint ordered blocks; its parent total is exactly the sum of its child totals. The rows have at most O(n^5) signed-coordinate entries, and W/V quotient rows have at most O(n^6) entries.

To rank, follow the seven successive choices (y_a,y_b,y_c,y_d,y_e,W,V), adding their prefix offsets; add the zero-based ordinal of (q,t) in K_g. To invert, search each row's monotonically increasing prefix starts, subtract the selected offset, and after seven levels select the residual controller ordinal. This is a disjoint interval bijection onto 0,...,S_g(n)-1. Every choice row has at most O(n+1) possibilities, giving O(log(n+2)) comparisons for seven binary searches. Count integers have O(log(n+2)) bits because S_g(n) is polynomially bounded by the existing base-fiber coefficient bound and at most 11 controllers per fiber. This proves the stated space and word-operation bounds. QED.

The representation's optimal fixed-length payload width remains ceil(log2 S_g(n)) bits as in PREFIX-496. Auxiliary index space is a *shared preprocessing cost*, not included in per-state payload width. With conventional bit-cost accounting, ranking is O(log(n+2)) bit operations and inverse ranking O(log^2(n+2)) elementary bit comparisons; initial index construction is O(n^6 log n) bit work under the already proved constant-arithmetic PREFIX-500 kernel.

## Exact computational certificate and scope

Published source: research_notes/portable_direct/prefix501_symmetric_prefix_certificate.py; exact execution: research_notes/portable_direct/PREFIX501_EXACT_EXECUTION.json.
Command: python3 prefix501_symmetric_prefix_certificate.py 9. Environment: Python 3 standard library, exact unbounded integers, set/dict/sort and bisect; no floating point or probabilistic errors.

The checker independently propagates all ten native signed directions, updating y, V, W, the gate KMP state and first-source tag. For *each* n=0..9 and each gate it constructs the full state set, tests every quotient class for identical controller supports, constructs the weighted-prefix row index, compares its rank with independently sorting all full states, and verifies inverse rank for every j and state. It also verifies the orbit-weighted total identity. The integer program exits normally with status ALL_CHECKS_PASS.

| n | base BRC fibers | aab full states | aba full states | quotient keys per gate | index row entries (y+W+V) |
|---:|---:|---:|---:|---:|---:|
| 4 | 712 | 1,218 | 1,219 | 192 | 1,319 |
| 8 | 22,275 | 60,590 | 60,550 | 3,117 | 17,409 |
| 9 | 43,054 | 127,403 | 127,298 | 5,320 | 28,324 |

Index row-entry counts exclude the K controller-set payloads and runtime hash-table implementation overhead. The measured Python checker uses direct native state enumeration *only to validate* the new index; the mathematical precomputation route uses the PREFIX-500 constant-arithmetic support oracle for each quotient key, not native enumeration.

Original executed source SHA-256: 21f265e396e61f6fe6605fcc3fd12eb4dd57b0855b87b6bee292449901d4b98a.
Original complete JSON execution SHA-256: 2756e99aa102770af11b78a715ce4a3d8e39b66bde209f574a5bc200e7bc068c.
These exact file bytes are included in this Git publication. Finite execution validates the implementation on n<=9; the all-n statements follow from the proofs above and the stated PREFIX-500 oracle theorem.

## BRC interface, tool reuse, limits, next discriminating unit

Applied previously proved exact BRC cancellation update for V,W and its source-controller quotient (REUSE_APPLIED). Composed the existing PREFIX-496 dense rank with PREFIX-497 five-color Parikh occupancy and PREFIX-500 support oracle (COMPOSE_APPLIED). Relevant current inventory includes T0_BRC and T7_FINITE_SYMMETRY_EQUIVARIANCE; this result is a specialized proven compression, not a claimed new general BRC or symmetry tool family. The signed-source information stays visible through K and the controller ordinal. This work performs no classical pi, trigonometric, matrix-exponential, or physical residual attribution.

Next PREFIX-502: reduce auxiliary storage below O(n^6 log n) bits while keeping exact lex rank/unrank, by deriving a piecewise polynomial/rational weighted-prefix sum on the six quotient coordinates, or test whether on-demand prefix counting via fixed-dimensional Presburger/Barvinok machinery yields a better concrete preprocessing/query tradeoff. Measure entire preprocessing, rank and append cost under the same observation contract. Also examine minimal sufficient online updates when shared per-length indices are unavailable.

Formal task RS-X6-NATIVE-ROTATION-DYNAMICS was queried as READY / NEEDS_DISPATCH, owner unassigned, at native control snapshot 2026-11-04T22:57:10.783194Z; this independent author-side continuation does not establish its CLAIM or change its native rotation-dynamics objective.
