# BRC-X6 signed first-step preserving-policy polytope: all facets and its graph

**Author-level portable theorem, 2026-11-09 Asia/Hong_Kong.** Scientific pin `f42f2906d77f24085c123f3ccfe9667d41caa96d`; exact native kernel SHA-256 `d2b84a22928e8160315e8578ea99a62f91b8688462d2b6451a71eef871df88b0`. Original 96 ports, six actions, native target and complete seven-output tuple (six spatial-axis rewards and independent gate K); nine frozen roots `0,±e1,±e2,±e3,±e4`.

## Exact result

Let `P=(6,7,28,29)` with signs `(+1,-1,-1,+1)`. Each source port chooses its own six-action distribution `x[p,a]≥0`, `Σ_a x[p,a]=1`. For every native target-plus-seven-output atom `o`, require `Σ_{p,a:A_r(p,a)=o} s_p x[p,a]=0`. The predecessor [integral-flow 38-vertex theorem](https://github.com/awdawmip/enterprise-math/blob/7886a552ff372fee6d68dada88d1219d9916016e/research_notes/portable_direct/2026-11-09_prefix577_r6_signed_first_step_integral_flow_complete_38_vertices_author_portable.md) proved this convex polytope has dimension 12 and exactly 38 0/1 deterministic vertices. New exact combinatorial invariants, for **each** of the nine roots:

```
f_0 = 38           f_1 = 434            f_11 = 18
graph diameter = 2
vertex degree histogram: degree 14 -> 3 vertices, 21 -> 22, 28 -> 13
minimal face dimension of unordered distinct vertex pairs:
dimension 1 -> 434 pairs; dimension 2 -> 260; dimension 3 -> 9
```

The 18 distinct facets come from the 24 nonnegative coordinate bounds. Six pairs of bounds determine identical supporting facets by native atom-balance identities:
`x[6,1]=x[28,3]`, `x[6,2]=x[7,2]`, `x[6,3]=x[7,3]`, `x[7,1]=x[29,3]`, `x[28,4]=x[29,4]`, `x[28,5]=x[29,5]`. The remaining 12 coordinate bounds are separate facets. Twelve facets contain 30 vertices, four contain 33, and two contain 34. Every facet is 11-dimensional.

## Proof and exact reproducibility

The signed incidence representation is a connected 13-node / 24-native-action-edge flow network with full affine dimension 12 and strictly feasible uniform policy `x[p,a]=1/6`. Hence every facet is supported by a coordinate equality `x[p,a]=0`. Enumerate the complete 38 native 0/1 vertices and identify coordinate bounds having identical vertex-zero sets. This produces exactly 18 distinct proper faces. On each face, the augmented incidence vectors `[1|x]` have rank 12 over both 1000000007 and 1000000009, proving Q-rank at least 12; the proper supporting coordinate equality bounds the affine rank by 12. Thus all 18 faces are facets and these are all facets.

For any pair of pure policies `v,w`, let `E(v,w)` be the union of their positive native action edges. Their midpoint is positive exactly on `E(v,w)`, so the smallest face containing both is the feasible flow face restricted to that edge support. The directed incidence rank gives its exact affine dimension:

`dim Face(v,w) = |E(v,w)| - |V_active(E)| + connected_components(E)`.

Therefore the two vertices are adjacent iff this circuit rank equals one. Exhaustively evaluate all `C(38,2)=703` unordered vertex pairs: exact circuit ranks have histogram `434,260,9` in dimensions `1,2,3`, respectively. Independently compute, for each of the same 703 support faces, affine span rank of all contained native 0/1 vertices over **both** exact finite fields; every rank equals its incidence circuit rank. The 434 edges give vertex valences `14×3,21×22,28×13`, sum 868, and an exactly connected diameter-two graph. Checking equality of native atom labels for all 24×24 ordered action pairs confirms that the equality partition is identical for all nine frozen roots.

The recomputable author package contains the original pinned kernel, a certificate JSON listing all 38 vertices and 18 facets, and `verify_signed_policy_facets_skeleton.py` with exact integer checks (no numerical tolerance), plus expanded proof. **Evidence status:** `AUTHOR_PROVED / EXACT_INTEGER_AND_TWO_PRIME_CHECKED / UNREVIEWED / NOT_ADMITTED`.

**Scope/continuation:** The original D25 H0/B0 divided-power module, source Frobenius, κ/Δ−R and native CM experiment remain their separate uncompleted Source frontier. This author-only geometric/observer increment makes no Source CLAIM, native checkpoint, Result or independent review. D24 Result/Review remain terminal. Original UR V2 four-file bundle remains an exact historical recovery target: 94,687 bytes; SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`. Next nonduplicative mathematical unit: exact 38-controller convex decomposition and output complexity, after current Source ownership / cross-stream evidence check.
