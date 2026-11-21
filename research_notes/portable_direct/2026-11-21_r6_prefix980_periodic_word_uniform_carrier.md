# PREFIX-980 — Periodic residual words: bounded source carrier and three-phase obstruction

Date: 2026-11-21. Mode: Research6, independent portable auxiliary signed-source XOR observer.
Status: AUTHOR_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED.
Prior scientific frontier: PREFIX-979 at awdawmip/enterprise-math@18151786859a4cb0279182225b52b0622357bd74.
Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json (Source V5). Global P000 V4 and ACTIVE worldview remain distinct.
Previous EM-DIRECT-FBEA5D / RA-3FB2D033BE6048D8712FF056 are historical provenance, not evidence of possession of that identity in this run.

## Exact model and domain

Fix integer p>=3. D_p={2^i-s*2^j: 0<=i,j<p, s in {+1,-1}}. Every valid (i,j,s) is a distinct named source. The state x is an odd integer modulo 2^p, so bit0=1. Ports j=1,...,p-1 preserve parity.

At residual a, source (i,j,s) is valid iff a=2^i-s*2^j and bit_j(x)=0 for s=+1, or bit_j(x)=1 for s=-1. It maps x to x XOR 2^j. Define P_a (s=+1 ports), M_a (s=-1 ports), T_a=P_a union M_a, all excluding port0.

Prescribe a finite nonempty ordered word w=(a_0,...,a_{L-1}), repeated cyclically; phase r uses a_r and then advances to r+1 mod L. Keep source identities, signs and step order.

## Lemma 980.1 — Nonzero-residue support has at most two ports

For a !=0 in D_p, |T_a|<=2. For a=0, T_0={1,...,p-1}.

Proof: A negative a can only arise as 2^i-2^j with i<j. The 2-adic valuation of -a fixes i, after which 2^j=2^i-a fixes j. Thus at most one port. A positive-difference source 2^i-2^j with i>j has a unique j=v_2(a), and a binary block of consecutive 1s. A positive-sum source 2^i+2^j requires either a power of two (i=j, one port) or a binary number with exactly two set positions (two ports). In the two-position case, any positive-difference source can occur only for adjacent set positions and its port is the lower, already one of the two sum ports. In the power-of-two case, there are at most one sum port and one difference port. No other cases create more ports. The restriction j>=1 only decreases support. For zero, i=j, s=+1 gives every port. QED.

## Theorem 980.2 — Exact constant-dimensional joint-source carrier

Let U(w)=union of T_{a_r} for r=0,...,L-1. The reduced state (phase r, bits of x indexed by U) preserves every finite and infinite named-source path exactly, including port, source i, sign, sequence, and every product of edge weights in a nonnegative coefficient semiring.

Indeed, every future source test and every update acts only at a port in U. Other input bits are inert. Restricting full paths to U, and extending any reduced path by arbitrary fixed outside bits, are inverse at the named transition level. Induction on path length gives path and weight preservation.

If all a_r are nonzero, |U|<=2L and there are at most L*2^(2L) reduced phase states, independently of p. Among all-phase, all-input one-step observations retaining named source labels, U is the smallest sufficient bit-coordinate set: two states differing at any j in U have distinct source eligibility or source sign/name at a phase using j. This last minimality does not assert minimality on a restricted reachable population or under a coarser observer.

## Corollary 980.3 — Uniform decision and extinction bound

A periodic nonzero word w has an infinite genuine named path from some odd phase-0 state iff the finite reduced phase graph contains a directed cycle. Every directed cycle must meet phase 0 (the phase advances by one each edge). If the graph is acyclic, every valid path from any phase has length at most

    L*2^|U|-1 <= L*2^(2L)-1.

For L=3 this gives the **universal bound 191** for all bit widths p, when each word residue is nonzero and there is no persistent path. The bound 191 is proved, but not claimed optimal.

Proof: Infinite walk iff cycle in a finite directed graph; a directed acyclic graph permits at most vertex count minus one edges in a path. Apply Theorem 980.2. QED.

## Proposition 980.4 — Three-phase obstruction invisible to every adjacent pair

For p=4 and w=(-1,3,6), each adjacent ordered pair (-1,3), (3,6), (6,-1), considered as its own alternating system, has a two-step infinite source path under PREFIX-979. The three-phase word has no infinite path.

At -1 phase the only legal nonzero port j=1 requires bit1=0 and flips it to 1; at 3 phase the only legal nonzero port j=1 requires bit1=1 and flips it to 0. At 6 phase, j=1 with either sign changes bit1 to 1 and blocks the next -1 phase. Alternatively port j=2 is usable only when bit2=1: it flips bit2 to 0, allowing one more -1,3 pair, but is then exhausted. Hence every path stops. All adjacent pairs individually have opposite-sign cross support at j=1. Pairwise persistence is therefore insufficient for a prescribed three-phase schedule. QED.

## Proposition 980.5 — Genuine six-step, three-port cycle

For p>=8 and w=(6,24,96), the odd input x=1 and selected port sequence (1,3,5,1,3,5) give the six pre-update states

    (1,3,11,43,41,33).

The corresponding genuine names (i,j,s) are

    (3,1,+1),(5,3,+1),(7,5,+1),
    (2,1,-1),(4,3,-1),(6,5,-1).

After six updates x=1 and phase=0, yielding an indefinitely repeatable three-port cycle. This is an auxiliary source-port operation, not a native X6 TRIADIC_CLOSURE_E event.

## Exact positive observer

On the reduced 2^|U| states let K_r(b,b') be the sum of nonnegative weights of genuine named sources available at phase r that send b to b'. Ordered matrix products K_0 K_1 ... K_{n-1} preserve exact positive named-path masses. Boolean support, counting and signed/phase amplitudes are distinct observers; this source carrier is BRC-compatible in positive-mass semantics but no native typed BRC operation or X6 embedding was executed.

## Reproducible exhaustive evidence

PREFIX980_R6_REPRO.py enumerates the original (i,j,s) dictionary, constructs exact reduced phase graphs, and uses integer-only topological cycle detection. All ordered triples of **nonzero numerical residuals** were enumerated:

| p | Nonzero residues | Triple words | Infinite | Finite | Largest finite path observed (any phase) | Finite words for which all three adjacent pairs persist |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 10 | 1,000 | 0 | 1,000 | 6 | 0 |
| 4 | 18 | 5,832 | 148 | 5,684 | 11 | 36 |
| 5 | 29 | 24,389 | 713 | 23,676 | 13 | 123 |
| 6 | 43 | 79,507 | 2,118 | 77,389 | 13 | 306 |

In addition, selected full odd-input named-source states were checked directly against the reduced graph on 12,504 (phase,x,word) inputs. The six-step three-port cycle was checked independently against genuine sources at p=8. These finite results apply to the declared checked domains; no p=19 exhaustive triple count is claimed. Uniform support and extinction are human-proved at arbitrary p. No independent scientific review.

## Remaining questions

Seek a sharper phase-word criterion and a smaller bound than 191 using binary source geometry, while retaining all names and joint phase correlations. For a native bridge, specify the Cell/Link/Port mapping, admissible TRIADIC_CLOSURE_E transition, third slice coordinate and observer-preservation law before making native X6 claims. Mother problem B_fix,odd(32) in {19,20} remains open.

This result changes no shared CLAIM, PROGRESS, Result, Review, Foundation or P000.
