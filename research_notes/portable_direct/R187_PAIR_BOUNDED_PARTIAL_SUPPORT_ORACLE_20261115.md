# R187 — Pair-bounded latest-source queries under unknown support

Date: 2026-11-15. Scientific status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**. Independent portable research, with no claim of formal Task ownership, Source PROGRESS, Result, Review or Foundation admission.

## Provenance and exact model

Frozen scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Direct dependencies: [R185](https://github.com/awdawmip/enterprise-math/blob/09f4c0c6eebf51a6cc15778b9101ccbe097004c1/research_notes/portable_direct/R185_CARDINALITY_PROMISED_SOURCE_QUERY_COMPLEXITY_20261115.md) and [R186](https://github.com/awdawmip/enterprise-math/blob/09f4c0c6eebf51a6cc15778b9101ccbe097004c1/research_notes/portable_direct/R186_PAIR_ONLY_SOURCE_QUERY_SORTING_GAP_20261115.md). Rules: EM main@0e020615068df74e84d323325c1364029cc49641; global knowledge main@09f54b2ee9387bf3ca7d7ddf07eba04fcb0d53c9.

Fix k named sources T={0,...,k-1}. The original population consists of complete typed X6 atoms carrying six-axis signed path order, branch identity, provenance, multiplicity and positive-rational BRC weights. This *source-only* observer maps a whole history to s=(s1,...,sr), the distinct observed sources ordered by increasing last-occurrence time. This is the R182/R185 delete-then-append quotient for whole-history concatenation, with 0<=r<=k. For nonempty U subset T, q_U(s) is the rightmost s_i in U, or NONE. Unit-cost adaptive queries may use singleton or pair subsets (1<=|U|<=2), and must reconstruct the entire s without a promise about r. The original X6/BRC carrier is retained for any richer observer: this theorem certifies only this source-only quotient and concatenation language.

Let Q2(k) be the deterministic minimax query count under unknown support, and Cpair(k) the optimal comparison-sorting minimax for k known-present items (R186).

## Theorem A: an adaptively chosen singleton of the oldest source is necessary

For every k>=1, **on every full-support input s=(s1,...,sk), every correct unknown-support algorithm must query the singleton {s1}**. This holds even if all other queries may have unbounded subset size as long as they contain at least two names.

Proof. Compare s to s'=(s2,...,sk), with only the oldest name removed. For any subset U of at least two names, if s1 is absent from U the oracle answers agree; if s1 belongs to U, some other present name in U occurs later and the answers still agree. Every other singleton also gives the same answer on both inputs. Consequently an adaptive transcript cannot distinguish s from s' until it queries {s1}. As both require different outputs, that query is necessary. For k=1 use the full and empty histories. QED.

Thus pair-only adaptive querying cannot exactly recover unknown support, even with arbitrarily many queries. R184's singleton necessity is now also an adaptive-transcript obstruction.

## Theorem B: exact universal bounds and sharp growth order

For every integer k>=1,

**Cpair(k)+1 <= Q2(k) <= M(k)+k**,

where M(k)=k*ceil(log2 k)-2^ceil(log2 k)+1, with M(1)=0, is the standard top-down mergesort worst-case comparison bound. Hence Q2(k)=Theta(k log k) as k tends to infinity.

Lower bound. Restrict a correct unknown-support algorithm to full-support permutations. Singleton answers are then fixed and supply no relative-order information. Erasing those unary nodes gives an ordinary pair-comparison sorting decision tree, some path of which uses at least Cpair(k) pair queries. Theorem A forces at least one singleton query on that same full-support path, so its total is at least Cpair(k)+1.

Upper bound. For a pair x,y, the returned name is the later *present* member. NONE means both names are absent. This comparison defines a total preorder: all absent names tie at its oldest end, followed by all present names in their exact chronological last-occurrence order. Stable mergesort therefore produces a1,...,ak, with the absent names in a prefix, using at most M(k) pair queries. Ask singleton {a1}. If present, the entire list is the answer. If absent, check consecutive pairs (a_i,a_{i+1}) from the beginning until the first non-NONE. Exactly those adjacent comparisons lying wholly in the absent prefix give NONE; one plus their number is the absent prefix length. Drop that prefix and return the rest. At most k-1 further pairs and one singleton suffice. The known-support sorting lower bound Cpair(k)=Omega(k log k) and this construction establish the stated Theta result. QED.

The query-unit model deliberately excludes input conversion, full-carrier construction, source-ID bit length, native BRC evaluation cost and output serialization. This is a query-complexity theorem, not a runtime speedup claim.

## Theorem C: exact law for one unknown occurring source and bounded aperture

Fix k>=1 and b>=1. If exactly one of the k names occurs, with its identity unknown, and queries satisfy |U|<=b, then the deterministic minimax cost is

**Q_b(k | r=1) = ceil((k-1)/b)**.

Upper bound: query successive disjoint blocks of at most b candidates, removing an entire block on NONE. A non-NONE answer identifies the unique source. When one candidate remains, its membership is forced by the cardinality promise. Lower bound: an adversary answers NONE while at least two candidates remain; t such responses eliminate at most bt names. If bt<k-1, at least two singleton histories remain consistent with the whole transcript. Thus at least ceil((k-1)/b) queries are needed in the worst case. QED.

For b=2 this is ceil((k-1)/2). For k=1 zero queries suffice under the one-present-source promise.

## Exact finite decision-tree validation

For k=1..4, enumerate every partial permutation (including empty) and every allowable singleton/pair query. The exact Bellman recurrence on a candidate belief B is D(B)=0 when |B|=1, otherwise 1+minimum over splitting queries of the maximum D of their nonempty response groups. Every group is a strict subset, so exhaustive memoized recursion terminates and proves its finite minimax value.

| k | partial states | exact Q2(k) | Cpair(k)+1 |
|---:|---:|---:|---:|
| 1 | 2 | 1 | 1 |
| 2 | 5 | 2 | 2 |
| 3 | 16 | 4 | 4 |
| 4 | 65 | 6 | 6 |

The equality Q2(k)=Cpair(k)+1 is proven by enumeration only for k<=4; it is **open for arbitrary k** here. The verifier separately checks the k=4 known-cardinality-promise minimax values for r=0,1,2,3,4 as 0,2,3,5,5; exhaustively recovers 16,071 partial source orders across k=1..7 by mergesort plus a single membership query; and checks the one-source block law for all 1<=b<=k<=8. All arithmetic is exact integer computation. Use Python standard library: python R187_bounded_source_oracle_check.py > R187_verification.json. The repository JSON is a compact persisted summary of the same validated cases.

## BRC/X6 interpretation and next scientific questions

The full branch, signed native X6 path, multiplicity, positive rational BRC mass and joint-provenance structure have richer queries than q_U. R187 only permits collapsing *source history* under the declared source-only observation and whole-history concatenation; it does not identify all branches with equal source-order images.

Next: test whether Q2(k)=Cpair(k)+1 holds for every k, finding an optimal-tree lift or a finite counterexample; then connect a source selector to actual src/enterprise_math/brc_transport.py while retaining all typed branch/path observables and measuring real total bit cost.

Historical researcher EM-DIRECT-BF4AD7 / SID MCP-46f202db13e64ad6b4c8860e06908245 / Activity RA-7A118452894D2600AE7DE5A2 are provenance only, not authentication of current possession or formal CLAIM. Independent Review remains NOT_REVIEWED.