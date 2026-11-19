# PREFIX-943 — 17-fold odd-core named XOR collision: exact disjoint union

Date: 2026-11-19. Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Predecessor: `PREFIX-941/942`, signed-bit CRT/floor-sum with k=13,15 and prior exact union 7,571,259,796.
Scope: **auxiliary** named XOR two-port observer, not native X6. Status: `AUTHOR_PROVED / EXACT_FINITE_COMPUTED / INDEPENDENT_FULL_SET_MATCH / INDEPENDENT_NEW_NONOVERLAP_AUDIT / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED`.

## Definition and theorem

Let `N=2^32`, `Q={262145,262147,...,524287}` (131,072 strictly 19-bit odd moduli). A named history is `F_x^j=(x,x XOR 2^j)`, `0<=j<=18`. An ordered pair `(a,b) in Q^2` observes `Phi_(a,b)(u,v)=(u mod a,v mod b)`.

Define `W17` as the pairs where some `0<=i,j<=18` and integer `t>=1` satisfy

```
(17*a XOR 2^j)-2^i=t*b.                         (1)
```

**Theorem.** Every pair in W17 has two distinct legal named histories `F_0^i` and `F_(17a)^j` with the same observation.

Proof: their starts are both 0 modulo a, and (1) makes the endpoints congruent modulo b. Distinct starts give distinct histories. The maximum nonzero start is `17*524287=8912879` and the endpoint differs by a flip at most `2^18`, so all endpoints lie below `2^32`. QED.

For all possible witnesses, `0<D=(17a XOR 2^j)-2^i<=17*524287+2^18-1=9175022`. Hence any solution has `1<=t<=floor(9175022/262145)=34`. This conservative positive quotient window is complete.

## Exact CRT cell count used for independent checking

The signed-bit law is `x XOR 2^j=x+s*2^j` with `s=1-2*bit_j(x)`. Fix i,j,t,s and set `c=s*2^j-2^i`. The endpoint equation with b odd is equivalent to `17a == t-c (mod 2t)`, together with `tL<=17a+c<=tU` and a odd. Let `d=gcd(17,2t)`; if d does not divide t-c, the cell is empty. Otherwise solve uniquely for a residue `a0 (mod M)`, `M=2t/d`, by `(17/d)*a0 == (t-c)/d (mod M)`. The modulus M is even; a0 must be odd. Its allowable progression `a=a0+Mh` is the intersection of `[L,U]` and `[ceil((tL-c)/17),floor((tU-c)/17)]`. Filter by `bit_j(17a)=(1-s)/2`.

The exact indicator identity `bit_j(z)=floor(z/2^j)-2floor(z/2^(j+1))` turns this filter into two Euclidean floor sums over a progression, with no full-a scan for the raw count. This is the theorem already established in PREFIX-941/942, now used as a separately executed check for k=17.

## New k=17 exact finite result

| Measure | Count |
|---|---:|
| Raw (a,i,j,t) witnesses | **19,318,164** |
| Distinct ordered W17 pairs | **15,136,736** |
| New pairs after priority-disjoint removal of older families | **6,467,873** |
| Predecessor certified union | 7,571,259,796 |
| **Current certified union** | **7,577,727,669** |
| **Not covered by these explicit certificates** | **9,602,141,515** |

The universe is `131072^2=17179869184`. The complement is not classified as injective.

| Prior certificate, first match wins | W17 pairs |
|---|---:|
| B/Z/S | 7,440,349 |
| U | 3,992 |
| V | 30,326 |
| W2 | 1,000,035 |
| W3 | 185,410 |
| D4 | 306 |
| W5 | 1,647 |
| D6 | 169 |
| W7 | 788 |
| D8 | 472 |
| W9 | 886 |
| D10 | 357 |
| W11 | 1,438 |
| W13 | 1,358 |
| W15 | 1,330 |
| **NEW17** | **6,467,873** |

These 16 disjoint classes sum to 15,136,736.

First lexicographic new witness:
```
(a,b)=(272019,521095), (i,j,t)=(2,16,9).
17a=4624323, (17a XOR 65536)=4689859.
4689859-4=4689855=9*521095.
Phi_(a,b)(0,4)=Phi_(a,b)(4624323,4689859)=(0,4).
```

## Evidence / verification scope

Two differently organized **complete** integer C++17 enumerators ran: direct scalar XOR `a,j,i,t`, and signed-bit CRT arithmetic progressions `i,j,t,s,h`. Both produced the same 19,318,164 raw witnesses in every one of 34 t-buckets and byte-identical 121,093,888-byte sorted `W17.bin`. Its SHA-256 is
`c13cd4a065ec200fe542f4a5a3dfc7525f90efe2d885f08cea67265b52a9900d`.

An independent Python Euclidean floor-sum counter also reproduced all 34 k17 raw buckets; it exactly reproduces previously published k11, k13, k15 raw buckets and ran 15,288 separately brute-checked local signed cells.

Old set inputs U,W2,W3,D4,W5,D6,W7,D8,W9,D10 came from the frozen PREFIX939 archive, SHA-256 verified. W11, W13, W15 were reconstructed from that frozen input and their published mathematical definitions, and their SHA-256 matched the previously published hashes (e.g. W15 `03f20dd609d1ceb997ee6fa25c0ecef34fc1626cf869ecd69dac340747fc4b03`). The original 13 predecessor families retain their exact sources.

The priority-disjoint C++17 set scan produced 6,467,873 `NEW17` pairs, sorted file size 51,742,984 bytes, SHA-256
`c8bdff39be9c81ba491cd03ba8f1be7af46800f5b88c71f3a884ab43146b36f0`.
An **independent full-set NumPy audit** verified that every NEW17 member avoids all 13 previous sorted sets and both B/Z/S and V closed predicates: zero overlaps in all tests. It did not independently calculate the positive priority partition; that positive count comes from the verified C++17 merge.

Companion texts: `PREFIX943_R6_K17_EXACT_RESULTS.json`, `PREFIX943_R6_SEVENTEEN_A_EXACT_CPP.cpp`, `PREFIX943_R6_K17_INDEPENDENT_CRT_ENUM.cpp`, `PREFIX943_R6_SIGNED_BIT_CRT_COUNTS.py`, and local full binary reproducibility archive in the originating conversation.

## Control / next

This independently published portable science preserves original R6 source attribution: `EM-DIRECT-58C410`, SID `MCP-31edc522830749ad8775ca012e02ef30`, Activity `RA-25432C4AAE9BF66A907F5115`. Historical record IDs are provenance, not live CLAIM/capability evidence. Shared X6 owner was read separately and no shared task was claimed.

The next exact question is whether distinct-pair union cardinalities can be counted through **intersections of source-labeled CRT progressions** rather than giant sorted binary sets. Keep overlap multiplicity and source-port provenance before any lossy BRC or coordinate readout. Formal review, Source CLI audit, project admission and native six-dimensional transfer remain open, each on its own authority path. Mother question `B_fix,odd(32) in {19,20}` remains open.
