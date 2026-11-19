# R284AV — Distance-graded optimal witness scheduling within the R284AU scalar Port reconstruction

Date: 2026-11-19. Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.
Direct source lineage: R284AT → R284AU → R284AV. Keep the historical frozen input pin from R284AT: R284AR @ 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Current behavioral rules, P000 and ACTIVE Heartbeat World are read separately. Auxiliary Port channel matrices do not constitute standalone native six-axis geometry.

## AV1. Improved theorem

Adopt precisely the bounded-height scalar oracle and positivity hypotheses of R284AU: n≥2, C=A/b, b,M positive known integers, A_ij integer in [1,M], named exact determinant queries
    O_C(d,z;u,v)=det(diag(d)-C-zE_uv),
with one arbitrary oriented spanning tree of available edited edges. The common integer probe scale
    L=2n!(M+1)^n+2
is the same as R284AU; each diagonal entry is either 0 or L/b and every edit z is 0 or 1/b.

**Theorem AV1.** For every n and every orientation of every spanning tree, one can reconstruct C entrywise from at most
    Q_AV(n)=n+binom(n,2)+(n-1)+2[binom(n,2)-(n-1)]
           =3 binom(n,2)+1 = (3n²-3n+2)/2
individual exact scalar determinant readouts. The procedure preserves polynomial-bit query sizes, exact signed cofactors, named vertices, paths and edit directions. All rational output postprocessing has polynomial bit complexity in n, log M and log b.

Compared with the previously proven universal R284AU bound
    Q_AU(n)=n+binom(n,2)+(n-1)+2(n-1)(n-2),
the new bound saves exactly
    Q_AU(n)-Q_AV(n)=(n-1)(n-2)
calls (for n≥2), without changing the oracle, required prior information or allowed edit families.

This is an upper bound on exact measurements, not a lower bound on all possible adaptive scalar observers. In the direct uncached implementation described below, the numerical bound is attained on the positive cases tested; a cache of shared unedited triple coefficients can further reduce measurements on particular instances/schedules.

## AV2. Grade-by-tree-distance reconstruction proof

The exact high-base coefficient extraction lemma and its bit bounds are established in R284AU and retained unchanged: each selected principal or edited cofactor coefficient of one-, two- or three-channel type is extracted using one scalar determinant evaluation at scale L.

First obtain all diagonal entries α_i=A_ii from n singleton coefficients. Obtain every unordered edge product p_ij=A_ij A_ji from binom(n,2) unedited pair coefficients. Each directed tree edge (u,v) receives one edited pair coefficient, revealing A_vu; then A_uv=p_uv/A_vu. Thus the entire oriented tree is recovered in both directions after
    Q_base=n+binom(n,2)+(n-1)
scalar calls.

There are precisely
    N=binom(n,2)-(n-1)=(n-1)(n-2)/2
unordered NON-TREE vertex pairs.

For each such pair {x,y}, choose x<y and the unique tree path
    x=v_0,v_1,…,v_ℓ=y
with ℓ≥2. Let a=v_(ℓ-1) be the penultimate vertex. Process non-tree pairs by nondecreasing ℓ. By induction, A_xa and A_ax were already reconstructed because the tree distance between x and a is ℓ−1<ℓ.

The edge {a,y} belongs to the tree, and its actual edit orientation is either (u,v)=(a,y) or (u,v)=(y,a). Extract exactly two scalar coefficients for T={x,a,y}: the unedited leading principal coefficient ℓ_T(0) and the same coefficient ℓ_T(1) with the tree's E_uv edit. R284AT's exact three-vertex cofactor formula gives
    q_(u,v)|x=A_vx A_xu
              =A_vu α_x−[ℓ_T(1)−ℓ_T(0)].

In the orientation (u,v)=(a,y), this equals A_yx A_xa, so A_yx=q/A_xa and A_xy=p_xy/A_yx. In the orientation (u,v)=(y,a), it equals A_ax A_xy, so A_xy=q/A_ax and A_yx=p_xy/A_xy. All denominators are nonzero by strict positivity. This closes the distance induction and reconstructs both orientations of EVERY previously unknown pair. Exactly ONE two-coefficient witness is needed for each unordered non-tree pair; no iteration over all third vertices for each tree edge is required.

Total scalar calls:
    Q_base+2N
      =n+binom(n,2)+(n-1)+2[binom(n,2)-(n-1)]
      =3 binom(n,2)+1.
All coefficient targets have complement sizes n−1, n−2 or n−3, and use the SAME high-base bound B and L. The bit-complexity statement follows from R284AU's coefficient-bound and exact fraction-free determinant analysis. QED.

## AV3. Representation and scope

This proof makes explicit the role of graph distance as a control/observation scheduling coordinate. Its graded induction is NOT an assumption about physical distance in P000's native X6 space. The tree is a named graph of permissible directed Port interventions; each scalar observation retains the signed determinant, edit orientation and exact two-hop path provenance. Under this declared future operation scope, no extra BRC mass compression or norm projection is performed. The 6D spatial P000 basis and separate time semantics remain unchanged.

The bound is robust to matrix singularity and rank deficiency under strict positivity. The sparse counterexample in R284AU still applies when positive support fails.

## AV4. Exact independent replay

The companion standard-library checker R284AV_distance_graded_scalar_port_checker.py imports only the R284AU_scalar_port_checker.py exact Bareiss determinant and high-base coefficient oracle, and independently implements the new sorted-distance reconstruction schedule.

It was executed locally on 234 pseudorandom positive integer matrices of dimensions 2..8 with seed 28420261120, and 8 additional all-ones oriented star/path boundary tests. Every one of the 242 full reconstructed matrices matched entrywise. Across them the checker recorded 6,938 exact integer scalar-oracle calls, 835 observed tree edits and 1,397 non-tree-pair cofactor witness recoveries. The largest single-case call count was 85, exactly Q_AV(8), compared with R284AU's universal bound Q_AU(8)=127. Maximum tested tree distance was 7. The full deterministic JSON record is R284AV_exact_verification.json.

These finite tests validate implementation coverage; the all-n quantifier is supported by the above direct induction. Independent mathematical Review and formal machine proof remain NOT_REVIEWED.

## AV5. Next scientific question

Can non-tree pair cyclic triple coefficients be multiplexed or reused to reduce the worst-case exact scalar count below 3 binom(n,2)+1 without exponential input/output precision, while retaining the known rational height class? Test noisy finite-resolution observability and necessary direction conditions when some weights vanish. Assess any claimed improvement across scalar query length, determinant evaluation, witness recovery and validation, rather than count alone.
