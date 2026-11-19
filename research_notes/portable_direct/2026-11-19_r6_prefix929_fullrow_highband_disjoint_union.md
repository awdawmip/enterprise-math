# PREFIX-929 — Exact global intersection of verified complete rows, their time reversals, and the 32-bit mixed collision family

Date: 2026-11-19. Lane: 进取数论研究6. Classification: AUTHOR_PROVED / EXACT_FINITE_COMPUTED / TWO_INDEPENDENT_IMPLEMENTATIONS_AGREE / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. This is the **auxiliary provenance-aware named-XOR two-port observer**, not a theorem of native X6 dynamics. Keep P000, six-axis/three-dimensional-slice semantics and source labels unchanged.

## Exact universe and reused certificates

Let `N=2^32`, `Q={262145,262147,...,524287}`, `n=|Q|=131072`. Named traces are `Z_x=(x,x)` and `F_x^i=(x,x XOR 2^i)`, `0<=x<N`, `0<=i<32`, retaining type/start/bit labels. The observer is `Phi_(a,b)(u,v)=(u mod a,v mod b)`.

Reuse PREFIX-928's proved and computationally checked *oriented-pair* collision set `K=B union Z union S union U`, where B is two-sided bucket-capacity overflow, Z is `lcm(a,b)<N`, S is same-start signed-power alias at the second port, and U is the 32-source-bit family outside B/Z/S generated over 64 special second-port moduli and their transposes. The already verified exact size is

`|K|=7,467,804,449; |U|=5,295,478`.

The sorted oriented-pair IDs in the user's previously produced PREFIX-928 reproducibility bundle encode `id=((a-262145)/2)*131072+(b-262145)/2` in little-endian uint64 order, with 42,363,824 bytes and SHA-256 `15534b09fa696b5cbeba46f7f644d75c2c3f99b719a88071150fa91357f22bad`. The original source C++ generators and result JSON are published at `awdawmip/enterprise-math@e31b888733e1ed8acd0322a46a4ee45375532ec8`. The present calculation reuses this frozen U; it does not reclassify U as an already-reviewed theorem.

## Theorem 1: time-reversal transfer of verified row collisions

For a named trace `(x,y)` of type Z or F^i, its reversal `(y,x)` has the **same** named type and, for F, the same bit identity because `y=x XOR 2^i` implies `x=y XOR 2^i`. Thus two distinct named traces colliding at moduli `(a,b)` reverse to two distinct named traces colliding at moduli `(b,a)`. No other model transfer is used.

Define `D` to be the 91 odd strict-19-bit second moduli from PREFIX-922 satisfying (i) `2^d mod b` avoids `+1,-1` for `1<=d<=31`, and (ii) it attains one of those residues for some `32<=d<=52`. PREFIX-922's complete direct-witness search and independent audit certified every `Q × {b}` for `b∈D`. Reuse the 11 other complete rows of PREFIX-923:

`E={262145,321651,440667,440669,524273,524275,524277,524279,524281,524283,524285}`.

Also include the full `b=440665` row (PREFIX-920) and the full `b=524287` row (PREFIX-921; 7 minimizers have same-start collisions). These 91+11+2 rows are disjoint, so `L=D union E union {440665,524287}` has **104** members and all pairs in

`C={(a,b)∈Q²: a∈L or b∈L}`

have a valid named collision. Exact cardinality: `|C|=2*104*131072-104²=27,252,160`.

## Theorem 2: an additional highband certificate with time reversal

PREFIX-923 directly audited an independent finite family

`H={(a,b_t): a∈Ahi={500001,500003,...,524287}, b_t=262145+2*((77081*t+12345) mod 131072), 0<=t<1024}`,

with `|Ahi|=12144`, 1024 distinct b_t, each such pair having a legal named collision. By Theorem 1, `H^op={(b,a):(a,b)∈H}` also consists entirely of valid collision pairs.

Let `V=C union H union H^op`. Use these four **pairwise-disjoint** enumeration pieces:
1. complete second-port rows `b∈L`, all `a∈Q`;
2. transposed complete rows `a∈L`, `b∈Q\L`;
3. highband forward `(a,b)∈H\C`;
4. highband reversal `(a,b)∈H^op\(C union H)`.

Piece 4 omits a reversed candidate if it was already in piece 3, equivalently when its first modulus `a` also belongs to Ahi and its second modulus `b` belongs to the seed set T.

**Exact full-domain counts and exclusion:**

| Disjoint piece | Domain | Already in B/Z/S | Already in U | Net new over K |
|---|---:|---:|---:|---:|
| 104 complete second-port rows | 13,631,488 | 6,203,042 | 1,678 | 7,426,768 |
| Their transposed columns excluding overlap | 13,620,672 | 6,071,390 | 1,709 | 7,547,573 |
| Highband H outside complete stripes | 12,404,898 | 810,190 | 0 | 11,594,708 |
| Reverse highband outside prior pieces | 12,396,617 | 810,051 | 0 | 11,586,566 |
| **Total** | **52,053,675** | **13,894,673** | **3,387** | **38,155,615** |

The disjointness of B/Z/S versus U is independently verified for all 5,295,478 U-member IDs. Hence

`|V\K|=52,053,675-13,894,673-3,387=38,155,615`.

The final exact certified union and its **certificate complement** are

`|K union V|=7,467,804,449+38,155,615=7,505,960,064`,
`|Q²\(K union V)|=17,179,869,184-7,505,960,064=9,673,909,120`.

The complement is **not** an injectivity certificate: it has not yet been globally intersected with every older generic two-flip certificate.

## Independent computations, arithmetic and evidence boundary

Two actually executed implementations yielded all four exact counts above:

- `PREFIX929_R6_ROW_STRIPE_UNION_NUMPY.py`: integer NumPy vectorization, `np.gcd` and `np.searchsorted` against the SHA-256-checked, sorted PREFIX-928 binary U set. Classifies the four disjoint pieces directly, evaluating `B=(b<33*ceil(N/a)) or (a<33*ceil(N/b))`, `Z=(a/gcd(a,b))*b<N`, and `S=(b in the exactly 24 signed-power-alias moduli)`.
- `PREFIX929_R6_DISJOINT_CERTIFICATE_UNION_CPP.cpp`: C++17 independently loops over the four mathematical domain partitions, computes B/Z/S directly, and **streams** all 5,295,478 ordered U IDs in one pass. It verifies strict ordering, range and U's complete disjointness from B/Z/S. It subtracts exactly the U members belonging to V, never performs per-pair binary search.

Both implementations returned the exact same four-way counts, total 52,053,675, old B/Z/S overlap 13,894,673, U overlap 3,387, increment 38,155,615, and new union 7,505,960,064. No floating-point results, sampling or randomization are involved. The U input binary is not duplicated in the repository; reproducible source and digest are fixed above. Prior papers' direct-witness verifications establish the existence of collisions for the imported full-row and highband families; this paper's exact new contribution is **the union and overlap computation plus the time-reversal transfer proof**.

## Next discriminating task

Intersect the resulting certificate complement with *other* published generic two-flip and residual mixed-collision pair sets, or generate an additional disjoint oriented-pair family; preserve provenance and actual named witnesses. The mother question `B_fix,odd(32) in {19,20}` and any native X6 typed transfer remain open. The present work claims neither a shared-X6 CLAIM nor formal Result/Review admission.

Author's control provenance: continuation of research6, original session `MCP-31edc522830749ad8775ca012e02ef30`, registered Researcher `EM-DIRECT-58C410`, Activity `RA-25432C4AAE9BF66A907F5115`, session-start receipt `r6-20261119-prefix928-own-session-start-01` terminal `SUCCEEDED`; registration is independent of a canonical shared-task CLAIM.
