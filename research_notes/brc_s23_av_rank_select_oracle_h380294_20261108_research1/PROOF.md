# S23/AV: certified rank/select and exact adjacency without triangular threshold enumeration

Date: 2026-11-08, Asia/Shanghai. Author-side exact theorem and executable finite verification; independent review pending.

Frozen science: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Parent frontier: `research_notes/brc_s23_av_stream_gap_class_h7000_20261108_r1/`, commit `6c3fe28b7bf03a98f08feb5ee4a6897272867ff4` (H=7000 exhaustive streamed certificate).
BRC type: observer keeps the joint label-1/label-4 counts, with label 3 furnishing unit-likelihood padding. The claim concerns the two-point likelihood-sign auxiliary observer, not a mother-model/X6 bridge.

## Theorem: non-enumerative exact order-statistics on 1 <= H <= 380294

Let `r = log(7)/log(10/7)`. The triangular threshold set at integer horizon H is
`T_H = {t(v,j)=r*v-j: v,j>=0, v+j<=H}`, with `M=(H+1)(H+2)/2` distinct values.

Put
`P=2074774`, `D=380295`, `Q=10^26`,
`LO=545569623581288298975349314`, `HI=LO+1`.
For every integer `1<=H<=380294`:

**(A) Exact rational ordering.** For any two triangle coordinates `(v,j)`, `(v',j')`,
`t(v,j) < t(v',j')` if and only if
`P*v-D*j < P*v'-D*j'`.
The integer keys `K(v,j)=P*v-D*j` are pairwise distinct in this domain.

**(B) Exact rank/count in logarithmic arithmetic operations.** For any integer key m, the number of triangular points whose key is <m can be evaluated with two integer binary searches and one Euclidean floor sum, without enumerating the M points. Let
`j_min(v)=floor((P*v-m)/D)+1`;
`A=min{v in [0,H+1]: j_min(v)>0}`;
`B=min{v in [0,H+1]: j_min(v)>H-v}`.
The predicates are monotone; where the sentinel H+1 is needed it denotes the first position after all real rows. Set `n=B-A` and
`FS(n,D,P,b)=sum(i=0..n-1) floor((P*i+b)/D)`, with `FS(0,...)=0`. Then
```
C_H(m) = A*(H+1) - A*(A-1)//2
       + n*H - n*(A+B-1)//2
       - FS(n,D,P,P*A-m).
```
This is exactly `#{(v,j):v,j>=0,v+j<=H,K(v,j)<m}`. Its evaluation uses `O(log H+log D)` Euclidean/integer operations.

**(C) Exact select, predecessor and successor.** All keys belong to `[-D*H,P*H]` and are distinct. Given a zero-based rank s, binary search for the least integer m with `C_H(m)>s`; the key of the rank-s threshold is `m-1`. Recover coordinates using
`v=((m-1)*inverse(P modulo D)) modulo D`,
`j=(P*v-(m-1))/D`.
Since `H<D`, this recovers the unique point. One selection takes `O(log((P+D)H)*(log H+log D))` integer/Euclidean operations; successive threshold and adjacency queries are available without sorting the M thresholds. Bit complexity depends on the bit lengths of H,P,D and the rational certificate.

### Proof of (A)

The 45-term rational `atanh` series with explicit upper remainder bounds (recomputed in `VERIFY_ORACLE.py`) proves
`LO/Q < r < HI/Q`. Furthermore `gcd(P,D)=1` and direct integer multiplication verifies
```
380294 * max(abs(LO*D-P*Q), abs(HI*D-P*Q)) < Q.
```
Hence for every `1<=H<=380294`, `|r-P/D| < 1/(D*H)`. For any nonzero integer `d` with `|d|<=H`, the noninteger rational `P*d/D` has distance at least `1/D` from every integer. The perturbation `|(r-P/D)*d|` is strictly smaller than `1/D`, so `r*d-b` and `P*d/D-b` have the same strict sign for every integer b. For `d=0`, the sign is exactly the sign of `-b`. Apply this to the differences `d=v-v'` and `b=j-j'`. Key injectivity follows because equality of keys requires `D|(v-v')`, whereas `|v-v'|<=H<D`; then both coordinate differences vanish. This also proves the real threshold order without a floating-point sort.

### Proof of (B) and (C)

For a fixed v, `P*v-D*j<m` is equivalent to `j>=j_min(v)`, so the number in that row is `clamp(H-v-floor((P*v-m)/D),0,H-v+1)`. As v grows, `j_min(v)` is nondecreasing and `H-v` decreases: full rows form a prefix, zero rows a suffix, and intermediate rows are exactly `A<=v<B`. Sum the full-row arithmetic progression and the intermediate expression. Their floors form the stated Euclidean floor sum. The binary search for select works because `C_H` is nondecreasing and jumps by exactly one at the integer after each unique key. The modular inverse reconstructs the unique triangle point. This proves all formulas and complexity bounds.

## Exact finite validation (reproducible)

`VERIFY_ORACLE.py` independently recomputes the 45-term logarithm enclosure, confirms the maximal declared horizon, and compares every rank, select and successor against a brute integer-key sort for H=1,2,3,10,80,150 (16,? values in the largest individual test: 11,476). It also runs 250 seeded rank/select/next-roundtrips at each of H=7000, H=100000, H=380294, without constructing their complete threshold sets.

Exact sizes:
```
H=7000:   M=24,510,501
H=100000: M=5,000,150,001
H=380294: M=72,312,333,660
```
Certified adjacent examples at H=380294: at zero-based rank 30,000, `(87,380150)->(19,379779)`, displacement `(-68,-371)`; at rank 10,000,000, `(1194,375449)->(1273,375880)`, displacement `(79,431)`. In both cases the rank difference is exactly one, a complete integer adjacency certificate for those pairs.

Actual output and executable source reside in the same directory. These tests corroborate the finite exact algorithm; the theorem for all H in the stated range follows from the above symbolic argument and the rigorous rational enclosure.

## Scientific value and next question

The previous full stream at H=7000 processed 24,510,501 thresholds in `O(H^2 log H)` ordering operations. The new oracle answers an arbitrary threshold's exact rank and immediate neighbor using logarithmically many arithmetic operations and `O(1)` additional machine-integer objects, even at H=380294 where the triangle contains over 72 billion thresholds. It is a new query primitive, not a claim of full enumeration of all gap classes at the larger horizon.

Next: use this oracle to inspect the `v+j=H` frontier and construct a verified incremental class/extremal witness update; then establish or refute `N(H)<=2455069` on a larger exact range. Retain `N(510)=2455069` and the H=7000 endpoint proof as inherited author-side dependencies; new claims about the first jump of N still require their own complete coverage certificate.

Control: GitHub read/write as `awdawmip`; native Researcher-ID, owner and CLAIM not verified because the native status/task API returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE`, `operation_sent=false` on 2026-11-08. This is an author-side mathematical proof, not an accepted Result or independent review.
