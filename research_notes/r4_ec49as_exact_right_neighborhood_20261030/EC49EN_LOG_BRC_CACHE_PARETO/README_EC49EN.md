# EC49EN — Exact logarithmic BRC cache count and observer-storage Pareto projection

**Date:** 2026-11-02. **Lineage:** EC49EI fixed-positive-count rank dichotomy, EC49EJ cross-horizon aliases and EC49EM native-prefix optimum. **Classification:** author-side analytic theorem / exact finite check PASS / portable Draft PR / unreviewed / not admitted.

## Problem and preserved native scope

Use ordered signed-X6 primitive operations: a=(-1,-1), b=(-2,-2), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2). A future word contains h of these operations and returns native displacement +2E1. Nine genuine history states are N0,N1,N2,A0,A2,B0,B1,AB0,BA0; the five first-A/B observer buckets are N,A,B,AB,BA.

At every integer horizon h=2,...,H choose a nonempty set of genuine return words of length h. All selected words at that h have identical complete six-axis native positive-step vector p, and their nine-history terminal indicator matrix has rational rank 9. Distinct horizons may choose distinct p. Retain all word identities, ordered native paths, first-event labels and joint-observer provenance.

For two independent strictly positive BRC channels the future multiplier pair is (X_p,Y_p)=(product x_i^p_i, product y_i^p_i). Cache keys here are **distinct formal exponent vectors p**, equivalent to distinct symbolic monomial pairs over algebraically independent positive indeterminates; accidental coincidences after numerical weight substitution are a different equivalence. Let M(H) be the minimum number of distinct p keys across horizons. Let S(H) count distinct cached 9-history x 5-bucket binary observation-transfer blocks (one per distinct transfer signature), separately from word/provenance records and prefix edges. Let M_4(H) minimize M under S=4.

## Exact theorem (all integer H>=2)

    M(H) = ceil(log2(H+1)) - 1;
    min S(H) = 4;
    M_4(H) = ceil(log2 H).

The complete nondominated (M,S) projection is:
- If H=2^j (integer j>=1), a single point (j,4).
- If 2^j < H < 2^(j+1), precisely (j,6) and (j+1,4).

These values concern symbolic positive-BRC multiplier reuse and observer-transfer table storage. A separately optimized native-prefix cost E is another resource.

## Exact lower bound for M

By EC49EJ, any returning p-fiber has p=(p1,p2,e,0,0,0), e>=1, p1>=2e, p2>=0. Set m=min(p1-2e,p2), A=p1+p2-1-m and B=p1+p2-1. Its operation horizons are the consecutive integers [A,B]. EC49EI establishes full rank exactly when m>=1 (at q>0 four required signatures, at q=0 two F/G signatures). Since p1>=2e+m and p2>=m, A>=2e+m-1>=m+1, so B=A+m<=2A-1.

Given k count fibers covering consecutive h=2..H, let R0=1 be the last continuously covered horizon before any selection. An additional fiber containing the next uncovered integer R+1 cannot end beyond 2R+1. Hence R_k<=2R_(k-1)+1, so R_k<=2^(k+1)-1. Thus k>=ceil(log2(H+1))-1. This bound covers *all* allowed p, e and word orders.

## Exact lower bound for M_4 and transfer storage

The unique h=2 rank-nine fiber uses words ce,de,ec,ed and requires four distinct transfer signatures. A rank-nine q=0 fiber, with q=#c+#d, requires both F and G signatures (first f and first g), which are distinct from those four; therefore any schedule using q=0 at any horizon needs S>=6. In a schedule with S=4 every fiber must use q>=1. For a fixed p this omits its largest horizon B, leaving [A,B-1] and B-1<=2A-2. A new such interval containing next uncovered R+1 ends at most 2R. Therefore R_k<=2^k and k>=ceil(log2 H). This also proves S_min>=4; the constructions below attain S=4.

## Constructive upper bounds (actual signed native paths)

For any integer a>=2 use p_a=(a+1,a-1,1,0,0,0). For a<=h<=2a-1 set q=2a-1-h and u=v=h-a. When q>=1, choose precisely four words:

    e c^q f^u g^v
    e d^q f^u g^v
    c e c^(q-1) f^u g^v
    d e d^(q-1) f^u g^v

They realize the four rank-nine transfer signatures 0A,0B,1A,2B with a unimodular nine-column minor (EC49EI/EM). When q=0, u=v=a-1>=1; choose two words:

    f e g f^(u-1) g^(v-1)
    g e f f^(u-1) g^(v-1)

These realize the full-rank F/G pair. Each constructed word has h operations, displacement +2E1, native length 4a and positive vector p_a, so both positive BRC multipliers are shared within the fiber.

For M(H), take a=2,4,8,... and cover intervals [2,3], [4,7], [8,15], etc., attaining ceil(log2(H+1))-1 keys with S<=6. For S=4, take a=2,3,5,9,17,... (a=2^j+1, j>=0) and cover only [a,2a-2], i.e. [2,2], [3,4], [5,8], etc. These have q>=1 throughout and attain ceil(log2 H) keys with S=4. At h=2 and 3, the M-minimal schedule has the identical BRC vector (3,1,1,0,0,0), but distinct operation words and distinct seam transfers. The exact lower and upper bounds prove the Pareto projection.

## Executed computational evidence

The committed JavaScript checker replays actual signed native operations against all nine history-state transfers, verifies displacement, positive exponent counts, rational full rank by GF(2) rank-nine witnesses, 1,024 positive-fiber interval inequalities, all symbolic key counts and shared-prefix trie costs for H=2,3,4,5,7,8,9,10,15,16,20,31,32. A GF(2) rank 9 witness certifies Q-rank 9 of the integer indicator matrix. This checker was executed directly before publication to generate EC49EN_EXECUTED.json.

Two separate Python standard-library checks also executed locally, both PASS: a genuine 10-step signed-X6 historical-path simulator and independent complete integer-fiber/bitmask set-cover DP for H=2..12 (22 exact finite minima). Their local archival sources and full outputs are available as the run's supplemental evidence package. The all-H result is the interval proof above; neither finite checker is extrapolated.

Illustrative native-prefix costs of *these* witnesses, not conditional prefix optima:

| H | M-minimal (M,S,E) | S=4 witness (M,S,E) | globally smallest E from EC49EM |
|---:|:---:|:---:|---:|
| 3 | (1,6,42) | (2,4,44) | 36 |
| 5 | (2,6,88) | (3,4,90) | 50 |
| 8 | (3,6,198) | (3,4,174) | 62 |
| 9 | (3,6,212) | (4,4,238) | 66 |
| 15 | (3,6,542) | (4,4,542) | 90 |

E counts distinct ordered native primitive prefix edges. The corresponding native-prefix optimum is 4H+30 for H>=5 (EC49EM). Word labels and provenance are preserved in either factor/cache scheme.

## Version, exact scope and open continuation

**Frozen science pins:** GLOBAL_KNOWLEDGE_V1 773d538180bfb49e24cffeb35c3ee75eb0628e2e; Enterprise Math fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. **Current behavioral main reads (2026-11-02):** global b8d30a685a039fd57929eea36fb8c21a2610396b; Enterprise Math cf36e583135f99d9ef9c1dc8d956063fc43a8ca0. P000 and ACTIVE Heartbeat World remain unchanged. Use only typed positive-weight BRC monomial arithmetic here; retain branch order and full observer state. No phase/signed cancellation, physical time evolution or quantum speedup is inferred.

**Authority:** GitHub identity awdawmip, repository writable; Source-native researcher session denied STATIC_READONLY_SCOPE_DENIED (operation_sent=false); active-owner read CONTROL_QUOTA. This is author-side preserved research; it is not a native CLAIM/Result or independent Driver acceptance.

**Next EC49EO:** exact three-resource Pareto optimization (E,M,S), beginning H=3,4,5; obtain real signed-X6 witnesses plus finite optimality certificates for E conditioned separately on M=M_min(H) and S=4.
