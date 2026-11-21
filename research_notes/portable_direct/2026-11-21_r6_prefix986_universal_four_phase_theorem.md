# PREFIX-986 — Universal four-phase eight-step cycle and sharp finite bound

Date: 2026-11-21 Asia/Shanghai
Status: AUTHOR_FINITE_EXHAUSTIVE_CERTIFICATE / EXACT_INTEGER_CHECKED / INDEPENDENT_SMALL_WIDTH_CROSSCHECK / NOT_REVIEWED
Continuation: PREFIX-985 (at most one branching phase).
Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json
Scope: auxiliary signed-source bit-flip observer, not native X6/BRC dynamics.

## Model and universal theorem

Fix p >= 3. Nonzero residuals are those c with a named source (i,j,s) satisfying c=2^i-s*2^j, 0<=i<p, 1<=j<p, s in {+1,-1}. Let w=(c0,c1,c2,c3) be a fixed ordered word of four such nonzero residuals. A move at phase q from an odd p-bit integer x may use a named source for cq if bit_j(x)=(1-s)/2; it sends (q,x) to ((q+1) mod 4, x XOR 2^j). Keep named-source multiplicity, sign and order when counting paths.

**Theorem 986.1 (all widths, all four nonzero residuals).** For every p>=3 and every w:

1. An infinite valid named-source path exists if and only if an eight-move phase-aligned return exists. A four-move return is a special case. A period of more than two complete four-stage words is never required to witness *existence* of an infinite path.
2. If there is no infinite path, then every legal path from any phase and any odd input has length at most **18 moves**.
3. The bound 18 is attained by a genuine p=6 residual word and hence is sharp for the uniform theorem.

This closes both questions left open by PREFIX-984 for the auxiliary observer.

## Proof by a finite exact quotient

For a residual c, aggregate its legal named sources by nonzero port j. Store a bit mask M_c(j): 1 for sign + (input bit 0), 2 for sign - (input bit 1), 3 for both. From the exact source equation, the ordered list of nonzero-port masks for each nonzero c is one of

(1), (2), (1,2), (2,2), (2,3).

These are the five classes established in PREFIX-983 Lemma 983.2. The two slots of a double-port class are distinct. Additionally, in every actual (2,3) class, the mask-3 port j has its mask-2 companion at j+1. In particular **the same mask-3 port occurring in different phases always has the same mask-2 companion**. This latter necessary constraint is retained in our quotient.

There are at most eight port slots across four phases. Encode each overlap pattern by the restricted-growth sequence of its port labels in slot order: the first label is 0, and each later label is an existing label or the next unused integer. Reject equality of the two ports within a double-port phase. Reject any pattern in which two (2,3) phases share a mask-3 port but have different mask-2 companions. Every actual residual word maps to one of the retained classes; the retained set may contain extra nonrealizable classes, making the certificate a sufficient overapproximation.

For a retained class with m<=8 ports, form G on states (q,b) in Z/4 x {0,1}^m, with an edge labelled by a slot (j,M) when M contains bit b_j; the successor is ((q+1) mod 4, b XOR 2^j). Its size is at most 4*2^8=1024. Since unused input bits never change and do not control legality, a real-word path projects to such a path, and every abstract path in a *realized* overlap class lifts to genuine named sources after fixing the untouched bits. Graph quotient here preserves Boolean existence and longest path; it is **not** an equivalence of signed-path multiplicities or positive BRC masses.

For each graph the checker performs:
- exact Kahn elimination to detect a directed cycle and, if acyclic, compute its maximum directed path length over all phases;
- one whole-word relation T on the phase-zero bit states, checking T(x) contains x (4-move return), and T^2(x) contains x (8-move return).

Every directed cycle contains phase-zero vertices because phase advances by one modulo four; therefore testing T and T^2 at phase zero is sufficient. The entire enumeration yields:

| Double-port phases | Retained RGS configurations | Cyclic | Four-move return | Cyclic without eight-move return | Maximum acyclic path |
|---:|---:|---:|---:|---:|---:|
| 0 | 240 | 14 | 14 | 0 | 6 |
| 1 | 3,552 | 364 | 364 | 0 | 7 |
| 2 | 24,216 | 4,084 | 4,024 | 0 | 11 |
| 3 | 84,200 | 21,700 | 20,320 | 0 | 14 |
| 4 | 122,558 | 45,786 | 40,373 | 0 | 18 |
| **Total** | **234,766** | **71,948** | **65,095** | **0** | **18** |

Every retained configuration is exhaustively checked, with all bit assignments and all phases, in the attached C++17 exact-integer enumerator. All 71,948 cyclic cases have an eight-move phase-aligned closed path; all 162,818 acyclic cases have maximum path length <=18. For arbitrary p, extra unused coordinates form static spectator factors, so the two graph statements transfer to every actual word. This proves (1) and (2) conditional only on the explicit finite computational certificate.

This is a **computer-assisted exhaustive proof**, not an independent formal checker verdict. To falsify the claimed universal conclusion it suffices to find a missed residual mask type, a realizable overlap pattern excluded by the enumerator, a graph computation error, or a valid longer/cyclic counterexample. Reproducible source and checks are provided below.

## Sharp witness from actual signed sources

Let p=6, w=(6,24,8,40), x0=63. The following **18 actual legal moves** use ports

1,3,3,5,1,3,3,3,1,4,3,3,1,3,2,3,1,3

and yield the integer sequence

63,61,53,61,29,31,23,31,23,21,5,13,5,7,15,11,3,1,9.

The named (i,j,s) sources in order are:

(2,1,-1), (4,3,-1), (4,3,+1), (3,5,-1), (3,1,+1), (4,3,-1), (4,3,+1), (5,3,-1), (2,1,-1), (3,4,-1), (4,3,+1), (5,3,-1), (3,1,+1), (5,3,+1), (2,2,-1), (5,3,-1), (2,1,-1), (5,3,+1).

For each step substitute the source into c=2^i-s*2^j and verify the current bit. An independent full four-phase graph inspection for this word detects no cycle and finds a maximum of precisely 18 edges. Thus 18 is sharp, not just an abstract upper bound.

## Reproduction, independence and provenance

Files:
- PREFIX986_R6_FOUR_PHASE_UNIFORM.cpp: exhausts all 5^4 local-mask choices, all RGS port overlaps, each quotient graph, cycle/8-return property, and acyclic maximum. Use g++ -std=c++17 -O3 and run with no arguments for the grand totals or 0..4 for a branching-phase stratum.
- PREFIX986_R6_INDEPENDENT_CHECK.py: separately constructs all original signed-source triples at p=3,4; uses a phase-zero period-graph cycle test independent of the C++ four-layer Kahn graph and checks the exact p=6 sharp witness by recursive DP. Run with python3.
- PREFIX986_R6_EXACT_RESULTS.json: exact outputs from these two runs and witness.

The independent actual-residual crosscheck gives 6,561 p=3 words with 960 cyclic and 65,536 p=4 words with 9,957 cyclic, zero mismatches between cycles and eight-step returns. These agree with PREFIX-984. The prior p=3..7 actual dictionary census is reused, not recomputed in this turn.

Scientific status: AUTHOR_FINITE_EXHAUSTIVE_CERTIFICATE / EXACT_INTEGER_CHECKED / NOT_REVIEWED. Frozen P000 and ACTIVE six-dimensional X6 worldview are unchanged. No typed native BRC/Cell/Link/Port update bridge is claimed. In particular the Boolean cycle witness does not preserve named-path multiplicity or positive branch mass without an explicit source lift.

Historical predecessor provenance: EM-DIRECT-FBEA5D, RA-3FB2D033BE6048D8712FF056, Source session MCP-45ad6d29cd534c1aad25595a72e3c532. These historical identifiers are not a claim of fresh current protected execution authority.

## Next scientific question

Find a genuinely source-preserving *weighted* finite carrier for the four-phase theorem: characterize the smallest joint state sufficient to compute signed-source multiplicities and nonnegative BRC weights under arbitrary repeated words, and establish a typed mapping (if available) to native X6 operations. The mother problem B_fix,odd(32) in {19,20} remains open.
