# Direct Farey-to-affine emission and rational-cluster exact risk law

Date: 2026-11-09. Researcher-ID: EM-DIRECT-68490A. Native activity: RA-B54D08A1FB8BB5E22D6A64C7.
Mode: independent author-side TASK_RESEARCH; no shared CLAIM or independent review.
Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Immediate predecessors: r14 Farey thresholds and r16 maximal affine codec, PR #1777@937715a5d8f52bf585d1f06d2d989ac3b0a4872e.
Observer: auxiliary irrational circle-cut Bayes risk, not a native X6 physical dynamics claim. The carrier retains phase indices, historical arc labels and type-specific gap provenance.

## Definitions

Let 0<theta<1 be irrational, t_i={i theta}, m>=2, n>=m. The m distinct phase cuts partition the unit circle into historical arcs I. For the n cuts, M(I;n) is the longest refined subarc fully inside I. The finite-future whole-block Bayes risk for the uniform initial-phase observer is

    R_theta(m,n-m)=1-sum_(historical arcs I) M(I;n).

For the frozen S23/AV observer, theta=79*alpha-46 and m=128, with strict certified enclosure

    262204504569236716045286/10^24 < theta
       < 262204504569236716045287/10^24.

The 160-term rational logarithm series and its remainder certify the enclosure, as in predecessor r14.

## Theorem A: direct event-to-affine emitter (any irrational theta)

Suppose an exact Farey event oracle yields a consecutive partition [m,N] into candidate-constant risk cells [s_j,e_j] with exact integer coefficient pair V_j=(A_j,B_j) such that R_theta(m,n-m)=A_j+B_j theta throughout each cell. Candidate boundaries may be spurious (adjacent V equal). No assumption about a minimal constant block table is made.

Maintain current horizon h and current coefficient value V(h), plus at most one pending affine record. Initially h=m and V(m)=(0,0). For each cell [s,e] after the initial cell, emit the singleton increment

    D(s)=V(s)-V(s-1)=(A_j-A_previous,B_j-B_previous),

and, when e>s, emit one zero-increment interval [s+1,e]. For the initial cell, emit zeros for [m+1,e]. Merge adjacent increment intervals with equal exact pairs D=(dA,dB); on a new pair flush the pending record. A maximal run over increment positions [l,r] is stored as

    (n0,n1,A0,B0,dA,dB)
     =(l-1,r, V(l-1)[0], V(l-1)[1],dA,dB).

For every integer n0<=n<=n1, its reconstructed risk is

    R_theta(m,n-m) = [A0+(n-n0)dA]+[B0+(n-n0)dB]*theta.

**Proof.** On the first index of each constant-risk cell, the difference is exactly the new coefficient pair minus the previous pair. All later differences within that cell vanish. These intervals partition all indices m+1,...,N, including spurious event boundaries. Consecutive equal differences telescope to the displayed formula. Because theta is irrational, distinct integer affine coefficient pairs cannot coincide as values; thus each output run is the unique maximal constant-increment interval and no pair of adjacent runs can be merged. The algorithm needs one pending six-integer record and the current coefficient pair: O(1) additional working space, exclusive of the Farey oracle, its arc rank/select index and the output file. It makes O(T+J) integer-pair operations after the oracle has supplied T event cells and produces J runs. QED.

The 2026-11-09 executable implements this theorem *while traversing* Farey epochs, without materializing any constant-risk block table. Its finite S23/AV verifier still preindexes up to 2,000,128 phase memberships in O(N) memory. The theorem separately allows an exact floor-sum rank/select oracle in place of that index, and it is meaningful only with that oracle's bit and query costs counted.

## Theorem B: rational-cluster one-run family

Let q>=1, 0<=p<q, gcd(p,q)=1 (gcd(0,1)=1). Let theta=p/q+epsilon be irrational with epsilon>0 and theta<1. Let m>=q be a multiple of q, and N>=m. Assume

    (N+q)*epsilon < 1/q.

Then for **every integer n in [m,N]**,

    R_theta(m,n-m) = q*(n-m)*epsilon = (n-m)*(q*theta-p).

Thus the entire horizon range is represented by the single exact affine record

    (m,N,0,0,-p,q).

**Proof.** For 0<=i<N, write i=qk+r, 0<=r<q. Since i*epsilon<1/q, the phase is {i theta}={r p/q}+i epsilon, with no wrap inside its base cluster. Because p is coprime to q, the q base fractions {r p/q} are precisely 0,1/q,...,(q-1)/q, permuted. Clusters stay disjoint and ordered. Within each cluster, successive indices differ by q, hence consecutive phases are exactly q epsilon apart.

For the first m=q h cuts each cluster contains exactly h points. Their historical arcs comprise m-q short arcs of length q epsilon and q long arcs running to the next cluster. Every later cut with index i>=m extends the right end of its original cluster; it lies in that cluster's original long historical arc, and no historical short arc is refined.

At any n<=N, the clockwise gap from the current last point in one cluster to the first point of the next has length at least 1/q-(n-1)epsilon > q epsilon by the stated inequality. Therefore it is the longest n-cut subarc of its historical long arc; all other subarcs therein have length q epsilon. Exactly n-q of all n circular gaps are intra-cluster and have length q epsilon. Summing the q long gaps gives 1-(n-q)q epsilon. Consequently

    sum_I M(I;n)=(m-q)q epsilon + 1-(n-q)q epsilon
                 =1-q(n-m)epsilon.

Subtracting from 1 proves the formula and its single-record encoding. QED.

This family extends the predecessor's m=128, q=2 near-half example to every reduced rational p/q and every m divisible by q. It supplies a certified bypass for a long nearly rational Farey-epoch walk and exact risk values at arbitrary n within the displayed inequality. A proof for m not divisible by q and a general multi-epoch bypass remain open.

## Executed finite certificates (actual Python/Fraction)

The direct Farey stream ran with strict rational endpoints for the frozen m=128, N=2,000,128 model. It visited 29 Farey epochs, 6,577 internal candidate thresholds and 6,606 risk-cell evaluations; emitted exactly 102 affine runs, 52 with positive increments, with 13 distinct increment pairs. Terminal risk pair was (-21156991,80688896). The output was byte-identical to the prior r16 2M full affine table (3,677 bytes, SHA-256 26707bc77d7b7267495df34045f1c5111a2d21cb7c8222e83e65775897b013e1). It never built a constant-risk block list.

Independent strict two-endpoint Fraction enumerations verified the rational-cluster theorem for (p,q,m,N)=(1,2,128,380),(1,3,33,322),(2,3,30,333),(2,5,40,240),(3,7,28,210),(0,1,17,200). Both rational enclosures of theta=p/q+sqrt(2)/10^8 passed for **every n** in those six ranges: 2,830 exact endpoint assertions. A contrasting outside-hypothesis case p/q=1/3, epsilon=sqrt(2)/25, m=6, n=12 has extrapolated q(n-m)epsilon>1, while actual risk stays in [0,1].

A separate non-S23 check at theta=sqrt(2)-1, m=17, N=3017 produced 36 direct affine runs with 20 strict-endpoint direct-partition checks; the near-half theta=1/2+sqrt(2)/10^8, m=128, N=5128 case produced exactly one run, with 20 more direct checks. These are finite executable checks of the general event algorithm, in addition to the proof.

Scripts: VERIFY_DIRECT_AFFINE.py, VERIFY_RATIONAL_CLUSTER.py, VERIFY_INDEPENDENT_SLOPES.py. Real stdout: RUN_EVIDENCE.txt, RUN_CLUSTER.txt, RUN_SLOPES.txt. Local output DIRECT_AFFINE_RUNS_2M.tsv uses the exact r16 bytes; the repository's prior r16 TSV can be regenerated by its verifier.

## Full cost and future-residual accounting

The direct streaming combiner costs O(T+J) coefficient operations and O(1) extra working memory *given* a certified event oracle. The run itself uses O(N) arc-membership preprocessing, O(N log m) index work and O(T*m log N) risk-winner work. Exact Fraction arithmetic has larger bit costs depending on the rational enclosure. For rational clusters satisfying Theorem B, the output (m,N,0,0,-p,q) is an exact O(1)-arithmetic representation once p,q,epsilon and the inequality are certified; constructing and certifying these inputs is not free.

A six-integer scalar-risk record preserves R at every declared horizon, but not the phase-labelled arc/port trace needed by other observers. Preserve its underlying Farey labels or the rational-cluster (p,q,m,N,epsilon) descriptor for future operations outside scalar risk evaluation.

Source status: original author-side proof and finite calculations, independent mathematical review pending; no shared CLAIM, native X6 transfer or theorem admission asserted.
