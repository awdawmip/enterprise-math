# PREFIX-939 — Exact k=10 low-bit boundary and general 2-adic quotient localization

Date: 2026-11-19. Research line: auxiliary fixed-19-bit odd-modulus **named XOR two-port observer**; frozen scientific input `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Reuses PREFIX-938 complete prior union `7,552,031,686`. Author analysis and exact finite computation; **not independently mathematically reviewed or admitted**. Historical Researcher `EM-DIRECT-58C410`, original SID `MCP-31edc522830749ad8775ca012e02ef30`; Source Activity `RA-25432C4AAE9BF66A907F5115`. This auxiliary arithmetic is not a native X6 model.

## Exact collision model and theorem

Let `Q={262145,262147,...,524287}`, `|Q|=131072`, `N=2^32`. For each legal endpoint pair `F_x^j=(x,x XOR 2^j)`, the observer is `Phi_(a,b)(u,v)=(u mod a, v mod b)`, with named source bit and start retained as provenance. For `(a,b) in Q^2`, define `W10` by existence of `0<=i,j<=18` and positive `t` satisfying

    D10=(10a XOR 2^j)-2^i=t b.

Then `F_0^i` and `F_(10a)^j` are distinct legal histories with the same observer value. Both endpoints are below `N`, starts are congruent modulo `a`, and the terminal difference is `t b`.

## General 2-adic reduction and valuation lemma (new reusable result)

Let `k=2^r m` with `r>=1`, `m` odd, and `a,b` odd, with the two named endpoints legal. Put `x=2^r ma`, `D=(x XOR 2^j)-2^i`; `v2` is the 2-adic valuation of a nonzero integer.

* If `i,j>=r`, then `D=2^r((ma XOR 2^(j-r))-2^(i-r))`, so `b|D` iff `b|((ma XOR 2^(j-r))-2^(i-r))`. The entire internal-bit collision family reduces exactly to the odd-core `W_m` with shifted source labels, retaining their original provenance.
* If `i<r<=j`, `v2(D)=i`. If `j<r<=i`, `v2(D)=j`.
* If `i,j<r`, then `v2(D)=min(i,j)` when `i!=j`, and `D=2^r ma`, `v2(D)=r`, when `i=j`.
* As `b` is odd, whenever `D=t b!=0`, `v2(t)=v2(D)`. These are lossless exact quotient filters. For `i=j<r`, `b|D` is equivalent to `b|ma` and implies `lcm(a,b)|ma<N`; this subfamily is already covered by earlier B/Z/S lcm certificates.

Proof: for `j<r`, bit `j` of `2^r ma` is zero and XOR adds `2^j`; for `j>=r`, XOR factors out `2^r`. Compare the lowest nonzero 2-power in the resulting two or three terms. Multiplication/division by `2^r` does not alter divisibility by odd `b`. For `i=j<r`, the two inserted/subtracted bits cancel. The lcm implication follows because any common multiple of `a,b` divides `ma`, and `ma<N`. No even-modulus inference is used.

For `k=10=2*5`, all `i,j>=1` witnesses were already included in the fully enumerated `W5`; only `i=0` or `j=0` need new enumeration (37 of 361 source-bit combinations). The `i=j=0` subfamily adds no new pairs. All remaining boundary witnesses have odd `t`.

## Exhaustive finite census

`10a` lies between `2,621,450` and `5,242,870`. Consequently `2,097,162<=D<=5,505,013`; since `21*262145=5,505,045`, `1<=t<=20` exhausts possible positive quotients. A conservative implementation also tests `t=21` (zero hits).

Two independent enumerators used different orders: C++17 scalar `a,j,i,t`; Python/NumPy vectorized `j,i,t` over all `a`. Both generated identical full sorted sets and SHA-256 digests and separately reproduced the entire priority-disjoint membership partition, with exact integer operations throughout.

| Item | Exact count |
|---|---:|
| Raw low-bit-boundary witnesses | 1,776,380 |
| Of these, `i=j=0` | 153,958 |
| Unique ordered `W10_boundary` pairs | 1,736,455 |
| Already B/Z/S | 933,937 |
| Additional U / V | 372 / 3,001 |
| Additional W2 / W3 / D4 / W5 | 18,562 / 475 / 16 / 138 |
| Additional D6 / W7 / D8 / W9 | 9 / 437 / 2 / 118 |
| **New relative to PREFIX-938** | **779,388** |
| **Cumulative union** | **7,552,811,074** |
| **Not covered by these certificates in `Q^2`** | **9,627,058,110** |

This priority partition is disjoint; the categories sum exactly to 1,736,455. It counts certificates, not proven injectivity of the complement.

First lexicographic genuinely new witness: `(a,b)=(314573,454071)`, `i=0,j=15,t=7`. Since `10a=3145730` and `(10a XOR 32768)=3178498`, `3178498-1=3178497=7*454071`. Hence `F_0^0=(0,1)` and `F_3145730^15=(3145730,3178498)` have observer value `(0,1)` while preserving their distinct named histories.

## Reproduction, hashes, scope

Pair ID is `((a-262145)/2)*131072+((b-262145)/2)`; files are strictly increasing little-endian uint64 IDs.

* Full boundary set: 1,736,455 IDs, 13,891,640 bytes, SHA-256 `afc6f12c3f7fb662f6934d1e4493cd16400c800309ff292388b60798a24e3827`.
* New-only set: 779,388 IDs, 6,235,104 bytes, SHA-256 `97c9c9288f9a162ba2d3b2f2827fc9cd03f5334a98db4275c5361a605275301d`.

Prior exact sorted inputs: `PREFIX928_R6_SORTED_PAIR_IDS.bin`, `W2.bin`, `W3.bin`, `D4_sorted_cpp.bin`, `W5.bin`, `D6.bin`, `W7.bin`, `D8.bin`, `W9.bin`, with the preceding bytes supplied by the verified PREFIX-936/937 and PREFIX-938 reproduction bundles. Earlier families B/Z/S and V are recomputed from the explicit closed predicates in the independent sources. C++ and NumPy outputs and the original set are retained in the full local reproducibility bundle. Reproducing the partition requires the pinned original input bytes; no substitute or newly rounded data are accepted.

This is an exact result about this explicit auxiliary observer and finite domain, not an X6 native-space proof. It does not settle `B_fix,odd(32) in {19,20}`.

## Next scientific question

Derive a uniform odd-core transfer rule for `k=2^r m` including the new boundary quotient valuations, compare with the previous completed W-family union, and evaluate `k=11` (or a non-enumerative congruence sieve) for additional true set coverage. Keep shared X6 owner/CLAIM and mathematical review/admission separately typed.
