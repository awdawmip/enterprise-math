# PREFIX-467 — Exact horizon-minimal joint BRC history codec in the native X6 ab-gate

Date: 2026-11-03 (Asia/Shanghai). Scientific provenance: continuation of PREFIX-466 at EM commit e3311755b3b12aee1f9bc4392e898593d453bfe8. Scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d. Status: author-side analytic derivation and exact-integer executable checks; independent review/admission pending. Native task owner and native researcher identity were not verified.

## Exact object and observer

Use P000's affine native X6 chart with the restricted signed step alphabet consisting of x=+E1 and the ten symbols ±E2,...,±E6. Denote a=+E2, b=+E3, c=+E4. All non-x steps are allowed. At the empty word the first x is allowed. At later positions, x is allowed exactly when the last two steps are a,b in that order. Time is the separately typed word order, rather than an extra spatial coordinate.

Use the explicit positive integer weights from PREFIX-466: x and all negative directions have weight 1; positive a,b,c,+E5,+E6 have weights 6,12,18,24,36. For an ordered legal word u of length n, retain (i) its native endpoint (the +E1 step count s and the other five signed chart displacements y), (ii) its exact individual product weight W, and (iii) an integer multiplicity when words are aggregated. An H-future observer lists the exact endpoint/product-weight/multiplicity histogram after every legal extension of each length h with 0 ≤ h ≤ H. An unavailable extension contributes no word. The observer is defined on individual histories, with multiplicity summed when certified-equivalent histories are coalesced.

Retain the existing exact BRC valuation coordinates A,C from PREFIX-463/465 and the five signed net coordinates y. The base key f(u)=(s,y1,...,y5,A,C) determines W exactly. In particular, with p=(n-s-Σ|yj|)/2 and ρ=(6,12,18,24,36),
W(u)=6^p 2^A 3^C ∏ ρj^max(yj,0).
At fixed n and endpoint, A,C are uniquely determined by W, by uniqueness of prime factorization. This is an internal signed X6 chart, not a final nonnegative cell-address serialization.

Let q(u)∈{0,1,2} record the relevant suffix: 2 if the word ends in ab, 1 if it ends in a but not ab, and 0 otherwise. The exceptional empty start is assigned q=2 because it has the same legal next-step behavior and all subsequent transitions as an ab-ending word. For fixed n and base f let Q_n(f) be the set of q states realized by a legal word. Define B_n = number of distinct base keys, F_n = sum_f |Q_n(f)|, and U_n = number of base keys with q=2 and another q.

## Theorem 1: complete minimal finite-horizon history quotient

For every n ≥ 0 and every integer horizon H ≥ 0, two legal length-n histories have equal present and all ≤H future endpoint/product-weight histograms exactly when:

* H=0: their base f keys agree.
* H=1: their base f keys agree and either both have q=2 or both have q∈{0,1}.
* H≥2: their base f keys and their q states agree.

Consequently the number N(n,H) of observer-equivalence classes is exactly
N(n,0)=B_n,
N(n,1)=B_n+U_n,
N(n,H)=F_n for all H≥2.

Proof. The current endpoint and product weight recover f at fixed n. The deterministic transition from (f,q) upon appending one of the eleven step symbols, including signed-pair closing and integer valuation updates, proves sufficiency of the complete q for arbitrary future length. For H=0 no extension is observed. For H=1, q=0 and q=1 both disallow immediate x and admit precisely the same ten non-x letters, whose endpoint/product-weight changes depend only on f. The q=2 class admits immediate x, producing a readout with one extra +E1 step; neither q=0 nor q=1 can produce this in one step. For H≥2, q=0 and q=1 are separated by the length-two extension bx: q=1 can append b then x, while q=0 cannot append any x within two steps. Its resulting +E1 count therefore distinguishes the exact endpoint histogram. The immediate-x distinction also separates q=2 from the other two states. The all-≤H observer includes these witnesses for each H≥2. Thus all displayed partitions are both sufficient and necessary. QED.

## Theorem 2: exact count of one-step-relevant gate fibers

For every integer n≥2,
U_n = B_(n-2).
There are exactly B_(n-2)-1 base fibers containing all three q states. Exactly one q=2-containing fiber has only {q=1,q=2}; its base is (s=0,y1=n-1,y2=1,y3=y4=y5=0,A=C=0).

Proof. Every q=2 word of length n ends in ab, so it is v ab with legal prefix v of length n-2. Appending ab to a base f(v) is deterministic, and injective on base keys: reverse the +b and +a signed net changes and recover their corresponding pair-valuation increments from the recovered prior signed coordinates. Hence the q=2 fibers are in bijection with the B_(n-2) prefix bases. For each v, v ba is also legal and has the same step multiset, hence the same base key, while its final suffix state is q=1. Thus every q=2 fiber is mixed and U_n=B_(n-2).

If v consists solely of a's, the total step multiset in v ab consists of n-1 a's and a single b. Every ordering ends either in a (q=1) or in ab (q=2), so q=0 is absent. Its base is exactly the stated exceptional key, and no different word can have this base due to the fixed length, endpoint and no cancellations.

For every other v choose its rightmost non-a symbol t and write v=v' t a^j with j≥0; v' is a legal prefix. If t=b, the reordered word v' a^(j+1) b b is legal and ends in bb; if t is a non-x symbol other than a,b, the word v' a^(j+1) b t is legal and ends in t; if t=x, the word v' a^(j+1) b x is legal because the appended x follows ab. Each reordered word has the same multiset, endpoint and exact product weight as v ab and has q=0. Thus every nonexceptional q=2 fiber contains all three states. QED.

In particular for n≥2, N(n,1)=B_n+B_(n-2), an exact arbitrary-length identity requiring no finite enumeration.

## Theorem 3: exact minimum fixed-width dense codec at a fixed prefix length

Fix n,H and the declared observer. Enumerate reachable length-n base keys in lexicographic order, refining each into exactly the H-equivalence classes from Theorem 1. Their consecutive ranks 0,...,N(n,H)-1 form an invertible codec; inverse decoding is table lookup (or indexed enumeration). Since the classes are pairwise observer-distinguishable, any fixed-width injective binary code on this exact finite population needs at least ceil(log2 N(n,H)) bits, which the rank code attains.

The theorem counts the history-sensitive key, with n and the grammar known externally. Integer path multiplicities remain exact values attached to these keys. Constructing or storing the dictionary, recovering W, and transmitting endpoint/n are additional resource costs. The associated dynamic programming counts all reachable keys and multiplicities by exact integer addition, with at most eleven transition attempts per occupied state per layer, plus exact-integer bit costs.

## Executed certificate

The accompanying ECMAScript BigInt source independently enumerates all ordered legal words of lengths n=0...5, reconstructing signed endpoint, pair counts, A,C and product weight from the raw word; it compares each histogram to the state-quotient transition recurrence. It extends the exact compressed recurrence through n=8, tests the PREFIX-466 unweighted and weighted rational-series recurrences at each layer, enumerates H=0,1,2 dense rank keys, roundtrips the rank mapping, and verifies the mixed-gate fiber formulas and exceptional-base characterization for n=2...8.

Key exact results:

| n | B_n | N(n,1) | F_n | bits H=0 / H=1 / H≥2 | 3 B_n bound |
|---:|---:|---:|---:|---:|---:|
| 2 | 65 | 66 | 74 | 7 / 7 / 7 | 195 |
| 3 | 275 | 286 | 348 | 9 / 9 / 9 | 825 |
| 4 | 933 | 998 | 1270 | 10 / 10 / 11 | 2799 |
| 5 | 2694 | 2969 | 3899 | 12 / 12 / 12 | 8082 |
| 6 | 6869 | 7802 | 10493 | 13 / 13 / 14 | 20607 |
| 7 | 15863 | 18557 | 25423 | 14 / 15 / 15 | 47589 |
| 8 | 33797 | 40666 | 56526 | 16 / 16 / 16 | 101391 |

For n=8 the exact recurrence aggregates 110,650,630 legal ordered words and total positive weighted mass 10,940,358,735,514,950. All assertions passed. The separate independent Python standard-library check reproduced the same row counts, mass and direct brute histograms through n=5; it is retained in the current handoff. No floating-point rank or equality check was used.

These are exact model-internal positive-weight BRC observations; their quotient retains the declared endpoint/product-weight/count observer and append language. It does not discard raw source provenance for any different future operation. No native physical time or signed phase evolution is asserted.

## Concrete next unit — PREFIX-468

Compute B_n by a symbolic language-weight/image method, ideally a rational or diagonally-extracted multivariate generating function, rather than forward state enumeration. Test whether the exact one-step formula N(n,1)=B_n+B_(n-2) permits a finite recurrence or a structure theorem for B_n. Independently apply the history-equivalence repair criterion to a new pattern gate with overlapping suffixes and document how its observer-minimal quotient differs from the unweighted automaton. The separate any-degree X6 moment-rank conjecture from PREFIX-459/460 remains open.

## Source, identity, governance

Project source: P000, ACTIVE Heartbeat X6, joint observer preservation and residual-fidelity constraints, and PREFIX-466 author-side result at commit e3311755b3b12aee1f9bc4392e898593d453bfe8. Scientific source frozen at f42f2906d77f24085c123f3ccfe9667d41caa96d. The cited P000/world/joint file blob SHAs at the frozen pin match current main: bcc2590d3168a28f72e8b9f0f9b1f76faadcd488, 94a02d067be2b039ca4c0f7ffedb5ebde8430e08 and 3923890d77a02d84b772f789e6912dd14f220d14. Behavioral rules follow current applicable main, independently of the scientific freeze.

Real GitHub login: awdawmip, Enterprise Math push/admin. Native task list returned CONTROL_QUOTA; native RESEARCHER session start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false, so this author-side source publication is not a formal CLAIM, Result/Review or Admission. Distinct competing owners were not displaced.
