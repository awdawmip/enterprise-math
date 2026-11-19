# R284AT — Spanning-tree completeness for directed Port interventions in every positive dimension

Date: 2026-11-19. Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.
Lineage: R284AS (three-channel complete classification), R284AQ (rank-one tree probes), R284AR (transpose ambiguity).
Frozen scientific inputs remain those of R284AR: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`; R284AS source is an author continuation, not formal admission. Applicable current P000 / ACTIVE / Source normative rules were read separately. All matrices below are **auxiliary named Port-channel matrices**, not native X6 spatial dynamics.

## AT1. Exact theorem (all n, all strictly positive rational matrices)

Let `n>=2`, `C=(c_ij) in Q_{>0}^{n*n}`, `D=diag(d_1,...,d_n)` with independent formal named variables. The diagonal observer is
`F_C(d)=det(D-C)`.

For each chosen ordered pair `(u,v),u!=v`, independently read the full formal polynomial
`H_C^{uv}(d,z)=det(D-C-z E_uv)`.
Form the undirected observation graph `G_E` on `{1,...,n}` with an edge `{u,v}` for every read `H^{uv}`.

**Theorem AT1.** On the class of strictly positive rational matrices, the map
`C -> (F_C, {H_C^{uv}:(u,v) in E})`
is injective (entrywise) **if and only if** `G_E` is connected. In particular, precisely `n-1` suitably chosen directed single-entry interventions are necessary and sufficient for universal entrywise recovery. Every orientation of every spanning tree works. This extends R284AS from three channels and extends R284AQ from rank-one cores to arbitrary positive full-rank or singular cores.

## AT2. Pair and three-vertex path coefficients are sufficient

For `S subseteq [n]`, write `[d_S]P` for the coefficient of `prod_{i in S} d_i` in a multiaffine polynomial `P`; for a directed edit, first take the coefficient of `z` in `H-F`.

For `alpha_i=c_ii`, each singleton coefficient determines `alpha_i`:
`[d_{[n] \setminus {i}}]F = -alpha_i`.

Every unordered pair product `p_ij=c_ij*c_ji>0` is determined from
`[d_{[n] \setminus {i,j}}]F = alpha_i*alpha_j - p_ij`. (AT2)

For each sampled directed `(u,v)`, the highest-degree coefficient of the z-response is
`[z d_{[n] \setminus {u,v}}](H^{uv}-F)=-c_vu`. (AT3)

For each third vertex `w != u,v`, the three-vertex coefficient is
`[z d_{[n] \setminus {u,v,w}}](H^{uv}-F)=c_vu*alpha_w-c_vw*c_wu`. (AT4)

Hence a directed probe directly supplies its reverse entry and every length-two path product `q_{uv|w}=c_vw*c_wu`.

**Proof of the coefficient formulas.** Every variable `d_i` appears in exactly one diagonal entry, so the determinant is multiaffine. Selecting `d_i` for all `i in S` fixes those rows/columns, leaving the determinant of the complementary principal submatrix. Complements of sizes 1,2,3 give the displayed formulas by a direct 1x1/2x2 determinant and a three-vertex cofactor expansion of the single-entry edit. The response is affine in `z`. QED.

## AT3. Constructive reconstruction on an arbitrary oriented spanning tree

1. Extract all `alpha_i,p_ij` from `F`. For every probed tree edge `(u,v)`, (AT3) gives `c_vu` and `c_uv=p_uv/c_vu`. Thus all oriented entries of every tree edge are known.
2. For any vertices `x,y`, choose the unique tree path `x=v_0,v_1,...,v_l=y`. Proceed inductively on `k` to know both `c_{x,v_k}` and `c_{v_k,x}`. The base `k=1` is a probed tree edge.
3. On edge `{v_k,v_{k+1}}` (`k>=1`), use its actual probe orientation `(u,v)` and (AT4) with `w=x`. If `(u,v)=(v_k,v_{k+1})`, then
   `q=c_{v_{k+1},x}*c_{x,v_k}`, so divide by the known positive `c_{x,v_k}`.
   For the reverse orientation, `q=c_{v_k,x}*c_{x,v_{k+1}}`, so divide by `c_{v_k,x}`.
   In either case the opposite entry follows from `p_{x,v_{k+1}}`.
4. This recovers both orientations for every pair `x,y`, plus the diagonals, hence `C` exactly. The argument uses no rank, determinant-nonzero or genericity hypothesis.

This is a provenance-preserving path propagation rule: every inferred directed edge is tied to a *named* three-vertex path coefficient from a *specified* probed edge. Positivity ensures all divisions are defined.

## AT4. Disconnected probe graphs are never entrywise complete

If `G_E` is disconnected, choose a positive diagonal matrix `T` whose diagonal is constant within each connected component but takes different constants on different components. Since `C` is strictly positive, `C'=TCT^{-1} != C`.

Nevertheless `F_{C'}=F_C` by diagonal similarity. Moreover for every probed edge `(u,v)`, `t_u=t_v`, so `T^{-1}E_uv T=E_uv` and therefore `H_{C'}^{uv}=H_C^{uv}` **as complete polynomials**. This is an exact indistinguishability certificate; no finite set of probes with disconnected support can recover the whole matrix. Every connected graph on n vertices needs at least n-1 undirected edges. Together with AT3 this proves both directions of AT1. QED.

## AT5. Observer scope and computational cost

A spanning-tree selection is an optimal *number of fully named directed-intervention families*, not a claimed bound on scalar measurements or on evaluating those formal determinant polynomials. After accessing the required polynomial coefficients, the reconstruction uses pair products, two-hop path products and rational divisions; coefficient extraction and input/output bit growth contribute to the full computational cost. This separation preserves the Source project method contract and avoids an algorithmic speed claim absent a corresponding end-to-end benchmark.

The result uses exact signed determinant/cofactor contributions and retains directed path provenance. It follows the BRC information/observer discipline without treating positive-mass summaries as signed cancellations. The six-dimensional P000 native worldview is unchanged.

## Reproduction

Companions: `R284AT_spanning_tree_probe_checker.py` and `R284AT_exact_verification.json`.

A deterministic Python 3 `fractions.Fraction` checker tested 225 positive rational matrices of sizes n=2..6, on randomly generated *oriented spanning trees* (55/55/55/40/20 by n). All 225 exact reconstructions matched original matrix entries; 1,910 pair/path response coefficient checks passed; 24 full-multiaffine polynomial/direct-determinant comparisons passed. It also verified a strictly positive row-substochastic n=4 disconnected-probe indistinguishability witness at all 48 F-and-probe polynomial coefficients. Finite checks PASS; the all-n statement is proved by AT2–AT4. Independent Review: NOT_REVIEWED.

## Next high-value unit

Determine the minimal **scalar readout** cost when full formal determinant-response polynomials are unavailable, and compare coefficient extraction by interpolation versus structured determinant/cofactor evaluations at bounded rational precision. In sparse/nonpositive networks, characterize which division failures are repaired by cycle/path incidence or higher-order probes while retaining source and port labels.
