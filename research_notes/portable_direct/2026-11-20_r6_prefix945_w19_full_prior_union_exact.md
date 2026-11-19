# PREFIX-945 — Nineteenfold odd-core named-XOR collision, exact full predecessor union

Date: 2026-11-20. Enterprise Math research lane R6, auxiliary named-XOR two-port observer. **Frozen scientific input** `f42f2906d77f24085c123f3ccfe9667d41caa96d`, unchanged from PREFIX-944. Status: AUTHOR_PROVED / EXACT_FINITE_COMPUTED / INDEPENDENT_FULL_CANDIDATE_CHECK / INDEPENDENT_PRIORITY_AUDIT / NOT_INDEPENDENTLY_MATHEMATICALLY_REVIEWED / NOT_ADMITTED. No native X6, BRC dynamics, shared Task/CLAIM or formal Result is claimed.

## Definitions and proof

Let `L=262145, H=524287, C=131072, Q={L,L+2,...,H}, N=2^32`. For each `(a,b) in Q^2`, observe the named trajectories `F_x^j=(x,x XOR 2^j)`, with `0<=j<=18`, by `Phi_(a,b)(u,v)=(u mod a,v mod b)`, retaining original source bits.

Define
`W19={(a,b) in Q^2: exists 0<=i,j<=18 and integer t>=1 with ((19*a XOR 2^j)-2^i)=t*b}`.

**Collision certificate theorem.** Every W19 pair has two distinct legal named trajectories with equal observations: `F_0^i=(0,2^i)` and `F_(19a)^j=(19a,19a XOR 2^j)`. The first residues are both 0 modulo a; the second residues agree modulo b by the defining equation. Since `19a` is positive and below `2^32`, and a single flip at j<=18 remains legal, the histories differ and both endpoints lie in the prescribed state domain. The construction is sufficient, not a complete classification of all collisions.

For `D=(19a XOR 2^j)-2^i`, conservative exact bounds are
`4,456,467 <= D <= 10,223,596 < 39*262145`. Consequently all positive quotients satisfy `1<=t<=38`. For each `(a,i,j)`, checking exactly `max(1,ceil(D/H)) <= t <= floor(D/L)` and retaining odd `b=D/t in Q` exhausts all W19 witnesses. Sort/unique by `ID=((a-L)/2)*131072+(b-L)/2` (little-endian uint64) to obtain the exact ordered-pair family.

## Full-domain count, incremental contribution

The canonical predecessor union P17 through PREFIX-944 has inherited size `7,577,727,669`. By exact priority-disjoint subtraction from BZS, U, V, W2, W3, D4, W5, D6, W7, D8, W9, D10, W11, W13, W15, W17, the following finite results were obtained:

| Exact object | Count |
|---|---:|
| Raw parameter witnesses (a,i,j,t) | 16,565,914 |
| Unique W19 ordered modulus pairs | 12,701,275 |
| Already covered by P17 | 6,385,441 |
| **New19 = W19 minus P17** | **6,315,834** |
| **P19 = P17 union W19** | **7,584,043,503** |
| Not covered by these certificate families in Q^2 | 9,595,825,681 |

The total finite universe is `131072^2=17,179,869,184`, so the **certificate** coverage is `44.14494325756095%`; the noncovered complement is not proved collision-free. The W19 first-match priority buckets are BZS=6,344,617; U=2,454; V=24,445; W2=1,275; W3=2,109; D4=331; W5=899; D6=138; W7=1,776; D8=393; W9=1,022; D10=236; W11=1,363; W13=1,905; W15=1,212; W17=1,266; NEW=6,315,834. These are mutually exclusive and sum to 12,701,275.

**First lexicographically new pair:** `a=271425, b=522261, i=0, j=16, t=10`. The two trajectories `(0,1)` and `(5157075,5222611)` have identical two-port observation `(0,1)`, as `(19*271425 XOR 65536)-1=5222610=10*522261`. The pair was absent from the full predecessor P17 (as tested by the exact predicates and frozen sets).

## Verification scope

1. GNU C++17 `-O3` full `a,i,j,t` enumeration directly generated 16,565,914 witnesses and 12,701,275 sorted unique pair IDs.
2. An independent exact C++17 pre-sieved `(t,b)` multiples into a compressed sparse row index, then looked up each XOR difference. It generated `3,476,853` divisor edges, independently matched the full raw count and **every sorted W19 ID** byte-for-byte.
3. Separate Python/NumPy audited **all 12,701,275 W19 IDs** against the complete source-priority predicates/sets. Every priority bucket and all **6,315,834 NEW19 IDs** matched the C++ writer exactly. Its additional 1,001 deterministic witness checks are only sample checks; the exhaustive full candidate equivalence comes from step 2.
4. Frozen historical input files and W13/W15/W17 binaries were SHA-256 checked against PREFIX-944's recorded manifests. The inherited P17 cardinality is used as a prior certified input, not recounted from scratch in this run.

Full exact binary certificate SHA-256: W19= `dfb42d6775f6e111195447931c53a4d36de3c94a425bbf22485208066f87f45e` (101,610,200 bytes), NEW19= `f7037964afe2872a11729b21eea70645e24a846b3499e96cc348df2958d76801` (50,526,672 bytes). Both are sorted little-endian uint64 IDs. Reproduction code, execution logs, manifest, and exact two binaries are in the attached conversation reproduction archive; source files and compact results JSON are published beside this paper.

## Control, attribution, next research

Earlier original R6 provenance: researcher `EM-DIRECT-58C410`, SID `MCP-31edc522830749ad8775ca012e02ef30`, Activity `RA-25432C4AAE9BF66A907F5115`; retaining those names does not grant present protected execution rights. The previous shared X6 owner request `r6-20261120-prefix944-own-x6-owner-read-01` succeeded: its historical lease and claim were held by another researcher. No shared CLAIM/open/Result/Review action was executed. Activity linkage must use its own current portable association/CAS contract and proper source readback.

Next scientific unit: compute distinct new certificate unions for further odd cores using rowwise bitmask or CRT residue-cell enumeration, with full preprocessing/verification costs and a direct count comparison. Parent question `B_fix,odd(32) in {19,20}` remains open.
