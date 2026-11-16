# PREFIX-846 — Sliding-window CRT recovery and prime-power normal form for time-multiplexed BRC provenance

**Status:** AUTHOR_PROVED / EXACT_FINITE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
**Frozen scientific input:** \`f42f2906d77f24085c123f3ccfe9667d41caa96d\` (unchanged).
**Dependencies:** PREFIX-840 named-source scalar; PREFIX-842 permanent coprime modulus; PREFIX-843 modular fibers; PREFIX-844 joint CRT fibers; PREFIX-845 stateless k-port minimax.
**Research scope:** Positive-integer named-source Q-only BRC observation, not an asserted native X6 Cell/Link/Port event. Retain signed provenance, joint relationships and future-operation residuals at their original layers; the modular map is applied only to the declared U-observer.

## Setup and new question

For p named positive integer source weights 1<=w_i<=W and N=W^p, encode the named weight tuple by U in {0,...,N-1}, with the fixed known integer offset S. For fixed positive BRC operation weights a,b, put

  c_t=a^floor(t/2) b^floor((t-1)/2) (t>=1), and C=ab.

At heartbeat t a predetermined, observation-independent readout schedule chooses one modulus m_t>=1 and reports

  Y_t(U)=c_t(S+U) mod m_t.

There is only one active raw modular port per heartbeat, with at most B bits, so m_t<=2^B. The receiver may preserve the most recent w reports, but must decode the constant initial U from **each** sliding block of w successive reports, without using older decoded U or any auxiliary repair coordinate. The report time and chosen modulus are known. This is a scope-typed observer memory, not physical time or a native X6 event correspondence.

Let B_stream(N,C,w) be the least such maximum per-heartbeat width over all predetermined modulus schedules, possibly nonperiodic, that work for every t>=1. Let B_w(N,C) be the PREFIX-845 minimax width of w simultaneous fixed stateless modular ports.

## Theorem 846.1 — Exact fiber of any nonuniform time window

For arbitrary positive integers m_t,...,m_{t+w-1}, define

  d_s=m_s/gcd(m_s,c_s), and L_{t,w}=lcm(d_t,...,d_{t+w-1}).

For all U,V in {0,...,N-1},

  (Y_t(U),...,Y_{t+w-1}(U))=(Y_t(V),...,Y_{t+w-1}(V))
  iff U=V mod L_{t,w}.

Consequently the window is injective iff L_{t,w}>=N, and its maximum fiber has size ceil(N/L_{t,w}). Given the reports, each congruence is invertible after dividing by gcd(m_s,c_s); generalized CRT recovers U modulo L_{t,w}. The minimum supplementary fixed-length repair budget is ceil(log2(ceil(N/L_{t,w}))) bits, achieved by retaining floor(U/L_{t,w}) if an auxiliary coordinate is permitted.

**Proof.** Each report equality is m_s | c_s(U-V), equivalent to d_s | (U-V). Their conjunction is equivalent to divisibility by the lcm. Values U in an interval of length N have distinct residues modulo L iff L>=N. The fibers and quotient repair follow by Euclidean division, including L=1. For actual reconstruction, write g_s=gcd(m_s,c_s), c_s'=c_s/g_s, d_s=m_s/g_s. Because the observed residue is divisible by g_s, divide it and multiply by (c_s')^(-1) modulo d_s (when d_s=1 the congruence is trivial); subtract known S and merge consistent congruences by generalized CRT. QED.

## Theorem 846.2 — Exact bit-width/latency equivalence

For every N>=1, C>=1, w>=1,

  **B_stream(N,C,w) = B_w(N,C)**.

In particular, the PREFIX-845 construction yields

  ceil((log2 N)/w) <= B_stream(N,C,w)
  <= ceil(log2(ceil(N^(1/w))+w*rad(C*(w-1)!))).

For fixed C,w, B_stream=(log2 N)/w+O_{C,w}(1) as N grows.

**Proof (achievability).** Take a finite optimal bank of w C-coprime moduli m_1,...,m_w, each at most 2^B, with lcm>=N (PREFIX-845 theorem 845.1). Repeat these w moduli periodically, one per heartbeat. Every consecutive w-heartbeat window contains each modulus exactly once. Since gcd(m_j,C)=1 and every c_t has only primes dividing C, gcd(m_j,c_t)=1. Thus L_{t,w}=lcm(m_1,...,m_w)>=N in all windows by theorem 846.1.

**Proof (converse, including arbitrary nonperiodic predetermined schedules).** Assume a schedule with m_t<=2^B and injectivity in every window. For fixed B, there is an integer T_B such that for all t>=T_B and all m<=2^B, gcd(m,c_t) removes every prime-power factor of m supported on primes dividing C: for each prime l|C, v_l(c_t) grows without bound. Thus for t>=T_B,

  m_t/gcd(m_t,c_t)=(m_t)_perp(C),

the largest factor of m_t coprime to C. Pick any w-window beginning after T_B. By injectivity, the lcm of its w C-coprime effective moduli is >=N. Each effective modulus is <=2^B, and hence is a feasible PREFIX-845 w-port bank. Therefore B>=B_w(N,C). The same argument covers C=1 with T_B=1. QED.

This equality is for a **w-heartbeat decoding latency/window** and at most one active port per heartbeat. The receiver holds w report residues, potentially wB raw bits. A single isolated heartbeat generally cannot decode U at this width. No transmission, storage, or native causal-cost improvement beyond this declared width/latency tradeoff is asserted.

## Theorem 846.3 — Prime-power-disjoint normal form for exact minimax certificates

Fix B,C,k and let Q=2^B. Define P_{Q,C} to be all prime powers l^e in [2,Q] whose prime l does not divide C. For the maximum possible effective lcm over at most k C-coprime moduli m_j<=Q, it is sufficient and necessary to select **at most one power per prime**, distribute selected prime powers into k bins, and require each bin's integer product <=Q. The maximum lcm equals the maximum product of all selected prime powers across feasible bins.

**Proof.** Factor any feasible bank m_j. For each prime l appearing in its lcm, retain only the highest power l^e across all ports and assign that power to a port that already contained l^e. Multiplying retained assigned prime powers in any given port produces a divisor of the original m_j, so its product remains <=Q. Each prime is used once and the overall product equals the original lcm. Conversely, the bin products are valid C-coprime moduli <=Q; being made of distinct prime supports across bins, their lcm equals their product. QED.

This yields an independent finite feasibility method: generate allowable prime powers, branch on omitting a prime or assigning one of its powers to a bin, use bin-product bounds and symmetry reduction, and test whether the total chosen product reaches N. It also makes the **composite** modular interaction/carrier explicit rather than replacing its observer contribution by an unsupported prime-only projection.

## Concrete witness and finite exact checks

For C=2, N=64, w=3, choose the periodic modulus cycle (3,5,7). Every 3-heartbeat block has effective lcm 105>=64, so the maximum per-heartbeat register width is 3 bits. At width 2 the odd positive choices <=4 are only 1 and 3, with attainable lcm at most 3; hence 3 bits is exact. The active port reports one residue per heartbeat; the receiver needs the three most recent residues.

A Python arbitrary-precision integer verifier checks:
- Theorem 846.1's equivalence, including noncoprime moduli and unequal heartbeat gains: 13,824 parameter windows and 2,336,256 pairwise observation comparisons, a,b in 1..3; three moduli in 1..8; start times 1,2,4; U,V in 0..12; S=7.
- 27 finite optimal widths, over C in {2,6,30}, N in {4,16,64}, window w in {1,2,3}, via exhaustive unordered port enumeration; 297 sliding-window exact distinctness tests for each finite optimal schedule.
- Independent prime-power-bin enumeration checks 24 reachable width instances (optimum and all smaller widths for these); all agree with direct bank enumeration.

Result: \`ALL_EXACT_ASSERTIONS_PASSED\`. Programs use exact arbitrary-precision Python integers for modular arithmetic and lcm. The prime-list generator uses a trial divisor bound on the small finite domain <=32; the general proofs are arithmetic, not inferences from this finite experiment.

Reproduce with \`python PREFIX846_R6_STREAMING_CRT_CHECK.py > PREFIX846_R6_STREAMING_CRT_RESULTS.json\`.

## Connection and unfinished questions

This is a precise theorem about a frozen BRC-derived scalar **observer** with named source U fixed across the decoding window. A source-changing stream requires an explicit transition law and may invalidate the window recovery; future operations on signed branches or X6-native Cell/Link/Port relations require their own observer-safe bridge, including event order and provenance.

Next: (1) characterize the minimal memory/width frontier for a slowly changing U_t with a bounded number of source updates per w heartbeats; (2) find a compact *finite* prime-power-bin certificate for B_k(N,C), especially larger k; (3) test admissible X6-native event observables without collapsing signed provenance or global-depth residual; (4) preserve q>=5 nonnegative Q carrier work as an independent problem.
