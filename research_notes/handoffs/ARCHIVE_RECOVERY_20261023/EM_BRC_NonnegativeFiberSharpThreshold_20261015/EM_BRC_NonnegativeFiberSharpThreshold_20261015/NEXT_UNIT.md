# Next research unit — first cross-direction nonnegative layer

Study the external affine-incidence integer observation model at p=5, N=8=2p−2 (the exact first mass with cross-direction moves in the unrestricted graph).

Proved at all p>=5:
1. For N<p, residual Y(F) mod p uniquely determines the full state.
2. At N=p, the zero-residue fiber comprises p²−1 isolated p-delta condensates; the other nonsingleton fibers are p+1 parallel-line cliques.
3. All fully line-covered F=1_L+H with 0<=r=N−p<=p−2 have residual fiber and nonnegative connected component exactly {1_M+H : M parallel L} of size p−1.
4. For p<=N<2p−2, *all* edges are these same-direction cliques; all other states are isolated.
5. Cross-direction edges begin sharply at N=2p−2 and are never incident to a line-covered state at that threshold.

Explicit next question: at p=5,N=8, take all ordered nonparallel port pairs (j,k), define the exact minimal cross-direction edge F=(B_k−B_j)^−, G=(B_k−B_j)^+. Deduplicate their endpoints, classify connected components of the cross-edge-only subgraph, and compare full mod-5 observation residues. Does any non-atomic state of this first cross layer have same residue as a different non-reachable cross-edge component? Give a finite complete certificate on the set of cross-edge endpoints (not necessarily all C(31,8) nonnegative states), with exact population and no stale owner claims.

Proof input: X=F_5²\{0}; each B_j=1_j−1_{K_j}, YB=5I; cross neg-part mass=8; all pointwise mass is nonnegative integer. The local archive contains verify_threshold.py, check_mass_plus_one.py, check_movable_regime.py, certificates, and formal proof.

Authorship/authority boundary: UNREVIEWED author's external toy-model calculations only; P000 native X6 untouched, no formal Researcher CLAIM/Result/Driver review. GitHub Source write safety-blocked; do not treat a branch or empty Drive document as published evidence.
