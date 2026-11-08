# BRC-X6: complete face lattice of the 38-vertex signed native-policy polytope

**AUTHOR_EXACT_ENUMERATION / UNREVIEWED / NOT_ADMITTED.** Portable mathematics from the TASK_RESEARCH lane, 2026-11-09. Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Original 96 ports, 576 labeled actions, full `(next-port,R1,...,R6,K)` signed atom observer and nine frozen roots. Four source ports are `(6,7,28,29)` with signs `(+,-,-,+)`. Original kernel SHA-256: `d2b84a22928e8160315e8578ea99a62f91b8688462d2b6451a71eef871df88b0`.

## Reused exact parent facts

The native action-balance network flow polytope `P={x∈R^24: x>=0, four source-row sums=1, all signed original joint output-atom balances=0}` is 12-dimensional and has exactly 38 preserving deterministic 0/1 vertices. Its 18 distinct facets are original coordinate-zero faces. These are reused from the earlier author publications: [38 vertices](https://github.com/awdawmip/enterprise-math/blob/7886a552ff372fee6d68dada88d1219d9916016e/research_notes/portable_direct/2026-11-09_prefix577_r6_signed_first_step_integral_flow_complete_38_vertices_author_portable.md) and [18 facets/434 edges](https://github.com/awdawmip/enterprise-math/blob/f5582f8b5124b6a43d43bb96742e64357b8b5129/research_notes/portable_direct/2026-11-09_prefix577_r6_signed_policy_polytope_18_facets_434_edges_author_portable.md). This result credits those predecessors and computes the entire previously unclassified face lattice.

## New exact complete f-vector

Enumerating every intersection of the 18 distinct coordinate facets yields **46,204 faces including the empty face and P**, or **46,202 proper nonempty faces**. The number of nonempty faces of each dimension is:

| dimension | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| count | 38 | 434 | 2054 | 5458 | 9325 | 10957 | 9156 | 5511 | 2381 | 723 | 147 | 18 | 1 |

The alternating sum of the proper nonempty boundary face counts is zero, matching the Euler characteristic of the boundary 11-sphere of a 12-dimensional polytope. The 38 vertices, 434 edges and 18 facets independently match the preceding exact results.

**Complete enumeration proof.** For each original source/action coordinate `e` take the 38-bit mask `F_e={j:(v_j)_e=0}`. There are 24 coordinate masks but only 18 distinct masks. For a bounded `{x>=0:Ax=b}` polytope, every face is obtained by setting some defining nonnegativity inequalities to equality. Thus the set of all intersections of the 18 masks, including the intersection over the empty family and the empty vertex mask, is exactly the complete face lattice. Exhaustive deduplication gives 46,204 masks. An independent 2^18 subset enumeration and a separate incremental intersection closure using all 24 original coordinates give identical face-mask sets.

For each nonempty face mask `S`, `dim(F_S)=rank_Q((1,v_j):j∈S)-1`. The full augmented original 25×38 0/1 matrix has rank 13. Its projection onto leading `1` and these twelve zero-based original action coordinate indices is already rank 13:

`(0,1,2,3,4,6,7,10,12,13,14,16)`.

Hence the 13-row projected matrix is injective on every face's affine span. Any nonzero determinant minor up to 13×13 in this 0/1 matrix is bounded by `ceil(13^(13/2))=17,403,308` (Hadamard). Consequently its rank modulo prime `1,000,000,007` is **exactly its rational rank**. The resulting ordered ledger with one line per nonempty face `{face-vertex-bitmask:010x}:{dimension}\n` has SHA-256:

`2a4fa0cbebd8828b3f05cae6cbd3804be5bd8b74b808ca96e87a6aa1f4433786`.

Independent replication checked all 262,144 facet subsets and compared **79 full 25-coordinate exact rational ranks** (including all 18 facets) with the recorded dimensions. All agreed. Full author-portable scripts, the frozen native kernel, detailed certificate and complete 46,203-line face ledger accompany the source turn's research ZIP.

## New coordinate-private minimal-support theorem

For a face `F` with exactly `k` deterministic vertices, call vertex `v` coordinate-private when an original source/action label `e` has `v[e]=1` and `w[e]=0` for every other vertex `w` in `F`.

**Theorem.** If *every* vertex of `F` is coordinate-private, then **every rational or real point in the relative interior of F has minimal preserving pure-policy convex support exactly k**.

**Proof.** Coordinates zero on F remain zero under every nonnegative convex mixture, so any vertex in a representation of a point of F must itself lie in F. The point has positive value at each of the `k` original private coordinates. Each such value can be supplied by only the corresponding vertex of F. Thus every one of the `k` vertices is mandatory. Conversely, every relative-interior point admits a strictly positive convex combination of all the face's vertices, giving k terms. Original signed atom and action/port provenance is retained.

The exhaustive face lattice gives the numbers of faces all of whose vertices have original private coordinates, classified by their number k of vertices:

`k=1:38; 2:434; 3:1924; 4:3838; 5:3784; 6:2132; 7:696; 8:120; 9:8; k>=10:0.`

Thus there are **eight distinct nine-vertex private-coordinate faces**. The maximum k for this exact *certificate type* is nine; known 10–13-term optimal witnesses from earlier author work remain valid through their separate base-expansion certificates.

One such private-coordinate nine-vertex face has original zero-coordinate indices `(2,6,8,10,11)` and these exact preserving four-action tuples:

```
(0,1,2,3) (1,1,3,3) (3,3,0,0)
(3,3,1,1) (3,3,2,2) (3,3,4,4)
(3,3,5,5) (4,1,0,3) (5,1,1,3)
```

Respective private original `(source-row,action)` labels are

`(0,0),(0,1),(3,0),(3,1),(3,2),(2,4),(2,5),(0,4),(0,5)`.

Their equal-weight barycenter has denominator **9** and minimum preserving convex support **9**, directly proved by these nine original coordinate witnesses. This refines the certificate for the earlier nine-vertex simplex example, without redoing its valid mathematics.

## Reproduction and actual status

The two source-turn Python verifiers enumerate the 38 native pure policies from the frozen original kernel across all nine roots. The main script enumerates all faces, computes exact dimensions with the bounded-modular certificate, and writes `FULL_FACE_LATTICE_CERTIFICATE.json` and `FULL_FACE_LATTICE_MASKS.txt`. An independent script enumerates 18-facet subsets and checks 79 exact full-coordinate rational ranks. These are **author-side** checks, not Source-native experiments, independent Driver reviews, or admissions.

The original D25 H0/B0, Frobenius and CM experiment remain under their existing canonical ownership. Source control was not modified: the current gateway returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE / operation_sent=false` for native status and recovery; no claim/open/checkpoint was attempted. The original four-file UR V2 package (94,687 bytes, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`) remains an exact pending recovery target; no replacement is presented as original.

**Next research:** certify exact sparse-decomposition infeasibility for generic rational policies on faces without private-coordinate certificates, especially the known 10–13 support cases. Resume original Source work only after current canonical session/CLAIM/continuation readback.
