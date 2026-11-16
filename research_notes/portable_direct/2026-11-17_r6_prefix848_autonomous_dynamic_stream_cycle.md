# PREFIX-848 - Autonomous changing-source CRT: a finite-state cycle theorem

**Status:** AUTHOR_PROVED / EXACT_FINITE_EXHAUSTION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
**Frozen science:** `f42f2906d77f24085c123f3ccfe9667d41caa96d` unchanged.
**Dependencies:** PREFIX-846 constant-source sliding-window CRT; PREFIX-847 one-coordinate update fibers and the last-heartbeat local lower bound.
**Observer scope:** integer-encoded named positive BRC Q-only source weights. The observer is not a native X6 Cell/Link/Port event.

## Problem

Let S={0,...,W-1}^p be the named source-digit state space, N=W^p and U(x)=sum_i x_i W^i. One heartbeat transition is permitted when x=y or x,y differ in exactly one named coordinate (an arbitrary new value for that coordinate). An otherwise unrestricted stream x_1,x_2,... follows these transitions. At heartbeat t a predetermined schedule transmits

  Y_t(x_t)=c_t(S_0+U(x_t)) mod m_t,
  c_t=a^floor(t/2)b^floor((t-1)/2), C=ab,

with known offset S_0 and integer m_t in [1,2^B]. The receiver retains only the last w observations and the public time/modulus schedule. It must decode the **last/current state x_t** for every trajectory and every t>=w. It has no externally supplied previous exact source tuple, no retained earlier decoded state and no separate update-event report. Moduli are chosen independently of hidden states.

## Theorem 848.1 - Exact graph-cycle criterion for permanent streaming recovery

For fixed finite p,W,w,C,B define the late-time modulus alphabet

  A(B,C)={m in {1,...,2^B}:gcd(m,C)=1}.

For a length-w modulus word z=(m_1,...,m_w) over A, call z *good* when the map

  (x_1,...,x_w) |-> (U(x_1) mod m_1,...,U(x_w) mod m_w)

determines x_w uniquely over **all** Hamming-one trajectories of length w. This is an endpoint-decoding property; two trajectories may have identical reports if and only if their last states coincide.

Build a directed graph G(B) whose vertices are (w-1)-tuples of members of A (for w=1 use the unique empty tuple). Each good word z supplies an edge from its first w-1 moduli to its last w-1 moduli.

**Claim:** an observation-independent bounded-width schedule recovers every trajectory from each sliding w-window for all heartbeats if and only if G(B) contains a directed cycle. Consequently the exact permanent optimal port bit width is

  B_dyn(p,W,w,C)=min{B>=0:G(B) has a directed cycle}.       (848.1)

**Proof.** If a directed cycle exists, concatenate the successive edge words into a periodic modulus sequence. Every sliding w-word is good. All chosen moduli are coprime with C and therefore with every c_t, so the observed gain-scaled residues can be normalized (time and S_0 are public) and agree in their endpoint distinguishability with the definition of a good word. This gives exact decoding for every window. Conversely suppose a bounded-width raw modulus sequence works indefinitely. Because 2^B bounds the available moduli, there is a uniform late time after which every c_t contains all prime powers at primes dividing C which occur in any possible m_t<=2^B. Hence the effective modulus m_t/gcd(m_t,c_t) equals the C-coprime part of m_t, lies in A(B,C), and yields precisely the same observation equality fibers as the raw port. Every sufficiently late length-w effective-modulus word must be good; otherwise two admissible length-w trajectories with distinct endpoints would have identical reports. The infinite sequence of overlapping (w-1)-tuples is a directed walk in finite G(B). A finite directed graph admitting an infinite walk must contain a directed cycle. QED.

The theorem provides a finite, complete decision procedure for each fixed p,W,w,C,B. It keeps temporal change and source identities explicit and does not identify different trajectory histories merely because they end at the same packed scalar value.

## Finite exact solutions for the binary-weight named-source system

The attached verifier exhaustively resolves p=2,3,4, W=2, window w=2,3 and operation-product C=1,2,6 (18 cases). For each B from zero until the first directed cycle, it enumerates all C-coprime moduli <=2^B; all length-w modulus words; all admissible named-source trajectories; and the complete endpoint-recovery condition. Each below-optimum B produces an acyclic graph, giving an exact finite impossibility certificate for every potentially nonperiodic schedule. Each optimum B has an explicit periodic cycle, supplying a constructive all-time schedule.

The results are:

| p | w | C=1 | C=2 | C=6 |
|---:|---:|---:|---:|---:|
| 2 | 2 | 2 | 3 | 3 |
| 2 | 3 | 2 | 3 | 3 |
| 3 | 2 | 3 | 4 | 4 |
| 3 | 3 | 3 | 4 | 4 |
| 4 | 2 | 4 | 5 | 5 |
| 4 | 3 | 4 | 5 | 5 |

These are minimum maximum per-heartbeat **bit widths**, not numbers of ports. In this exact finite domain and with arbitrary one-coordinate updates every heartbeat, enlarging the memory from two to three reports does not reduce the optimum.

In contrast to the known-baseline update decoder of PREFIX-847, the autonomous decoder must also resolve the uncertain baseline. For example p=3,W=2,C=2 admits a 3-bit supplied-baseline update port q=7 under PREFIX-847, whereas the autonomous two-/three-window problem requires 4 bits here. A witness periodic modulus schedule can use 9 alone; the stored certificates list further possible cycles.

## Verification / boundaries

`PREFIX848_R6_AUTONOMOUS_STREAM_CHECK.js` implements exact finite state and modulus enumeration in integer arithmetic. The results JSON stores for all 18 cases: every attempted B, candidate alphabet cardinality, number of tested length-w words, number of good words, whether the full overlap graph has a cycle, and a concrete optimum witness period. Each finite trajectory is exactly enumerated from the discrete named-coordinate Hamming update relation; there is no floating-point approximating of outcomes. The graph-cycle theorem is a separate universal combinatorial proof, while the table's parameter domain is finite.

The source model remains a typed BRC scalar observer with fixed W and prescribed coordinate-update relation. It does not assert that arbitrary X6-native events realize these transitions, nor that a scalar port is sufficient for future signed path/provenance observations. P000 X6 and joint observer preservation remain unchanged.

**Next:** seek a general lower bound or a structured schedule that separates B_dyn from the full single-heartbeat width for larger p,W,w; quantify the extra memory required to synchronize a source-changing stream after a missed/ambiguous observation; then test whether an actually authorized native event interface supplies the source update labels needed for PREFIX-847's conditional local-code economy.

**Reproduce:** `node PREFIX848_R6_AUTONOMOUS_STREAM_CHECK.js > PREFIX848_R6_AUTONOMOUS_STREAM_RESULTS.json`.
