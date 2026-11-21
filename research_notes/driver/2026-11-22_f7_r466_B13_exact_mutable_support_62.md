# CBRC F7 Driver r466 — exact 62-key mutable-support repair obstruction for the frozen B12 witness

Date: 2026-11-22 (Asia/Taipei). Original F7 scientist: `EM-CBRCF7-83A1D4`. This exact follow-on audit: `EM-DVR-DEBB5E`. Mathematical status: independently reproducible finite combinatorial theorem, pending native Driver Review/Result/Activity linkage.

## Original scalar model and precise scope

Retain `u=(1,1,-1,-1)`, `v=(1,-2,-1,2)`, `A=I+uv^T`, `k=a-2b-c+2d`, and

`D_q(a,b,c,d)=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d)`.

The globally defined q obeys `q(-x,y)=q(x,y)`, `q(0,0)=0`, `q(x,0)=1` for nonzero x, `q(x,y)>=1/2` for nonzero off-axis coordinates and the fixed marks `q(2,1)=q(1,-1)=1/2`. Let `q_*` be the exact r464 B12 half-feasible rational witness, `M=30000000000000`, 2,813 nondefault entries, pinned to the immutable [62,463-byte source table](https://github.com/awdawmip/enterprise-math/blob/43165a915ab1db44a6194fcda670443cd3bc5720/research_artifacts/F7_R464_B12_Exact_Half_Witness_20261122.json), SHA256 `340491fd5d5e9ba66b9f345dee30f3e821df94ae7f4553c21bfa4c8dd0f4aeb5`.

For an integer input z, write its scalar-argument support as `S(z)={ (|x|,y) : (x,y) appears in the four q arguments of D_q(z) }`. Let `F12` be the union of S(z) over all 25^4 B12 inputs; the exact set has 3,073 keys. Only `U={ (x,y) in F12 : y!=0 and (x,y) not in {(2,1),(1,-1)} }` can be changed while retaining the scalar conditions.

Define the finite violation family
`V={z in [-13,13]^4 : S(z) subset F12 and |D_{q_*}(z)|>1/2}`,
and hyperedges `H_z=S(z) intersect U` for z in V. Exact enumeration gives `|V|=7916`.

## r466 exact theorem

**The maximum number of pairwise-disjoint mutable supports H_z and the minimum size of a mutable-key set intersecting every H_z both equal 62:**

`nu({H_z:z in V}) = tau({H_z:z in V}) = 62.`

Consequently any admissible function q' that has `|D_{q'}(z)|<=1/2` for every B13 input, when compared against the *specific frozen* r464 q*, must differ from q* on **at least 62 distinct old B12 mutable keys**. This improves the previous r465 lower bound of 53. It is also the exact minimum hitting-set cardinality for this scoped family of already violated B13 inequalities.

## Constructive upper and lower certificates

A size-62 explicit hitting set is the 52 mutable keys on the boundary

`{(13,y): -13<=y<=13, y!=0} union {(x,13),(x,-13):0<=x<=12}`

plus the following ten old mutable keys:

`(1,-12),(10,-12),(11,11),(17,2),(21,17),(27,-7),(34,-21),(38,-25),(47,30),(55,-34)`.

The checker exhaustively verifies that this set lies in U and meets every one of the 7,916 violating supports. For the lower certificate the checker contains **62 explicit B13 integer input quadruples** whose H_z are nonempty and pairwise disjoint. It verifies each violation using the original integer numerators and verifies disjointness on mutable keys; the 62 supports collectively occupy 231 mutable keys. Thus `62<=nu<=tau<=62` proves equality without relying on the MIP search solver.

For any B13 half-feasible q' and each z in V, at least one mutable coordinate in H_z must change, since changing no q argument leaves the original violation intact and fixed axes/marks cannot change. The disjoint family forces at least 62 distinct changes.

The 62-cover is a **combinatorial hitting certificate**; meeting every original support is necessary, not sufficient to obtain a numerically half-feasible B13 extension. The full B13 minimax value remains unresolved; r464 still proves `E_B^*=1/2` for `B<=12` and the prior full-domain bracket remains `1/2<=E_infinity<=4/7`. This statement concerns the auxiliary two-coordinate F7 model with its original assumptions.

## Independent checks and provenance

Checker: [`research_checks/CBRC_F7_R466_B13_MUTABLE_HYPERGRAPH_EXACT_20261122.py`](https://github.com/awdawmip/enterprise-math/blob/81ec8f5351ce661bf9c61b269ffb2449759edd1a/research_checks/CBRC_F7_R466_B13_MUTABLE_HYPERGRAPH_EXACT_20261122.py).

Run `python research_checks/CBRC_F7_R466_B13_MUTABLE_HYPERGRAPH_EXACT_20261122.py research_artifacts/F7_R464_B12_Exact_Half_Witness_20261122.json`.

Actual local run: **CERTIFIED**, B12 complete inputs 390,625; B13 complete inputs 531,441; old-only violating supports 7,916; disjoint mutable packing 62; hitting cover 62; union packing mutable keys 231. The distinct MIP search supplied one candidate but **the published theorem is checked with integer arithmetic, explicit certificates and direct exhaustion**, requiring no MIP package.

Original scoped r465 [proof](https://github.com/awdawmip/enterprise-math/blob/0209ed5efe16c5265f962d3e20db363a4b909fdd/research_notes/driver/2026-11-22_f7_r465_B13_frozen_witness_53_disjoint_repair_obstruction.md) and [checker](https://github.com/awdawmip/enterprise-math/blob/f1a8db61f1aa16f377c9d405814740d5267e5123/research_checks/CBRC_F7_R465_B13_FROZEN_WITNESS_CHANGE_BOUND_20261122.py) remain intact. Publication of this analysis is scientific evidence, not a native Review, Result acceptance, CLAIM or mother-objective completion.
