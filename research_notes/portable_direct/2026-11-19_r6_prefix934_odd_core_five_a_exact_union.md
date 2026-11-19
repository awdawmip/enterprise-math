# PREFIX-934 — Odd-core k=5 named-XOR collision census and 2-adic source-bit reduction

**Date:** 2026-11-19 (Asia/Shanghai). **Research:** 进取数论研究6, independent auxiliary observer. **Scientific input (frozen):** `f42f2906d77f24085c123f3ccfe9667d41caa96d`. **Predecessor:** PREFIX-933, `748ec1d1015c28554c3e85454faac77f36da701c`. **Author/source:** original Researcher-ID `EM-DIRECT-58C410`, original SID `MCP-31edc522830749ad8775ca012e02ef30`; these identify the already recorded research origin, not an X6 CLAIM. **Status:** AUTHOR_PROVED / TWO_DIFFERENT_EXACT_ENUMERATION_IMPLEMENTATIONS_AGREE / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Definitions and exact universe

Let `N=2^32`, `Q={262145,262147,...,524287}`, and `|Q|=131072`. An ordered modulus pair `(a,b)` belongs to `Q^2`. The population consists of **named** traces `Z_x=(x,x)` and `F_x^i=(x,x XOR 2^i)`; labels, start and bit index distinguish traces. The auxiliary two-port readout is `Phi_(a,b)(u,v)=(u mod a,v mod b)`. Every `x` and endpoint in this note belongs to `[0,N)`; neither an X6 native equivalence nor a new three-dimensional-slice theorem is asserted by this auxiliary calculation.

For k=5, define W5 to be all ordered pairs in Q^2 for which there are i,j in [0,18] and a positive integer t satisfying

    (5*a XOR 2^j) - 2^i = t*b.

All 5a are below N. If the displayed equality holds, `F_0^i=(0,2^i)` and `F_(5a)^j=(5a,5a XOR 2^j)` are different named traces and have equal readouts: the first residues are zero, and the endpoint difference is tb. This is an explicit, finite, source-labeled collision certificate.

## Theorem A — exact k=5 quotient completeness

For `a∈Q` and `0≤i,j≤18`, `5a≥1,310,725`, `5a XOR 2^j≤5*524287+262144=2,883,579`, and `2^i≥1`. Consequently `0<D=(5a XOR 2^j)-2^i≤2,883,578<11*262145`. For any odd `b∈Q`, the equality `D=t*b` therefore forces `1≤t≤10`. Exhausting `a∈Q, i,j∈[0,18],t∈[1,10]` and retaining only `b=D/t∈Q` is an exhaustive enumeration of W5. Integers are exact; there is no numeric tolerance or probabilistic sampling.

## Theorem B — general 2-adic source-bit reduction

Let `k=2^r*m` with r≥1, m odd, and let `a,b` be odd positive integers. Whenever `i,j≥r`,

    (k*a XOR 2^j) - 2^i
        = 2^r * ((m*a XOR 2^(j-r))-2^(i-r)),

so `b | (k*a XOR 2^j)-2^i` **if and only if**
`b | (m*a XOR 2^(j-r))-2^(i-r)`. This follows by factoring the low r zero bits of ka and the coprimality gcd(b,2)=1. The interior (i,j≥r) of the k certificate is a subset of the lower-bit odd-core m certificate, provided the latter uses the corresponding source-bit interval and valid endpoints. Only min(i,j)<r can contribute new pairs relative to the full odd-core m family.

Moreover, for `min(i,j)<r`, write `D=(ka XOR 2^j)-2^i`, assumed nonzero. If i≠j, then `v_2(D)=min(i,j)`. If i=j<r, then `D=ka` and `v_2(D)=r` for odd a,m. Since b is odd, any `D=t*b` forces the same valuation for t. **Proof:** when j<r, the XOR at bit j adds `2^j` to ka. Other terms with indices ≥r are multiples of `2^r`; if i≠j below r, the lower of `2^i,2^j` has the unique lowest set bit. If i=j below r, the two added/subtracted bits cancel, leaving ka. This gives an exact parity/2-adic filter for future even-multiple searches. It does not assert that odd-core k=5 is reducible to earlier even-k counts.

## Theorem C — exact W5 census and disjoint incremental coverage

Two separately implemented finite algorithms agree: scalar C++17 enumerates `(a,j,i,t)` with native integer modulo and sorts `uint64_t` pair IDs; NumPy vectorizes all `a` and `i` for fixed `(j,t)`, constructs an independent Boolean predicate, sorts/deduplicates, and reconstructs all older certificate sets for membership. Both obtain **the same byte-identical ordered list**.

Raw parameter witnesses by t:

| t | raw |
|---|---:|
| 1 | 0 |
| 2 | 0 |
| 3 | 3,154,354 |
| 4 | 720,907 |
| 5 | 10,290,908 |
| 6 | 620,423 |
| 7 | 3,516,421 |
| 8 | 229,368 |
| 9 | 841,751 |
| 10 | 0 |

Total raw 19,374,132; distinct ordered pairs **15,406,809**. Their sorted little-endian uint64 IDs, `((a-262145)/2)*131072+(b-262145)/2`, occupy 123,254,472 bytes and have SHA-256 `ed2ff4c1961e29a619ccb404e834150028b4a689d5816ae03b2fa41fbc49de95`.

Classify each distinct W5 pair once, **in priority order** against the preexisting PREFIX-933 union:

| Class | Priority-disjoint count |
|---|---:|
| B/Z/S (two-sided capacity or zero-trace or known same-start predicate) | 7,548,662 |
| U (PREFIX-928 32-bit mixed), after B/Z/S | 3,229 |
| V (104 complete rows and 1,024 highband reflected stripe), after above | 33,831 |
| W2 (two-a zero-origin), after above | 1,405,996 |
| W3 (three-a zero-origin), after above | 214,543 |
| D4 (four-a boundary), after above | 142 |
| **new outside all previous classes** | **6,200,406** |

The numbers add to 15,406,809. Consequently the previous certified union `7,531,649,800` increases exactly to **7,537,850,206** out of `17,179,869,184` ordered pairs; the remaining **9,642,018,978** pairs are not covered by these named certificate families. The increment is relative to the stated B/Z/S/U/V/W2/W3/D4 union; this has not been deduplicated against every historical named XOR certificate elsewhere in the project.

The lexicographically first new pair is `(a,b)=(278817,508375)`, witnessed by `i=5,j=17,t=3`. The two traces are

    F_0^5=(0,32)
    F_(5a)^17=(1394085,1525157)

and the endpoint difference `1525157-32=1525125=3*508375`. First endpoint observations are both zero modulo 278817; second observations are both 32 modulo 508375.

## Reproducibility and source pins

The calculation uses the sorted `U` from PREFIX-928 (5,295,478 IDs, SHA-256 `15534b09fa696b5cbeba46f7f644d75c2c3f99b719a88071150fa91357f22bad`), the complete W2 and W3 sets from the PREFIX-932 code (30,211,412 and 19,413,088 IDs), and the sorted D4 from PREFIX-933 (1,793,182 IDs, SHA-256 `d66d467d5c48d62f6bdb2cdf02a081830eba4a32f28447b10d8c425350bdb664`). They are defined by exact frozen formulas at those committed source versions, not recomputed as new theorems. Existing C++ program `PREFIX932_R6_TRIPLE_A_EXACT_CPP.cpp` regenerated W2/W3, including its exact prior result assertions. The independent vectorized implementation reconstructed the B/Z/S and V flag predicates rather than importing scalar classification.

New-only sorted IDs occupy 49,603,248 bytes and have SHA-256 `d3857354c1016485dcf365d7769e84c2f1e6c9a27f7a3d9aa6d57a7258f81377`. Both implementations produce the same W5 and new-only byte arrays. Local executed source files and machine-readable results are shipped alongside this paper. Comparison was computationally independent in algorithmic layout; mathematical independent reviewer approval remains pending.

**Next discriminating unit:** k=6. By Theorem B, all its i,j≥1 certificates reduce exactly to existing k=3. Only the one-low-bit boundary (i=0 or j=0) needs new enumeration. Deduplicate that against this PREFIX-934 union by actual ordered IDs, preserving future source-bit provenance. Additional k≥7 odd cores remain unexamined.

**Research provenance:** independent auxiliary work within the existing Researcher-ID, without a current shared X6 CLAIM, formal Result, freeze or acceptance. P000/ACTIVE six-axis worldview and residual/provenance preservation are unchanged.
