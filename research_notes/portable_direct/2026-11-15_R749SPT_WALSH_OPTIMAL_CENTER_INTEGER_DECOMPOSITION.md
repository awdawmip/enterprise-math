# R749SPT — Regular unimodular triangulation and integer decomposition of Walsh minimax centers

**Date:** 2026-11-15. **Status:** AUTHOR_EXACT_NOT_REVIEWED. **Frozen scientific input:** \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. **Predecessors:** R749SPR (PR #2457, commit \`7e876e05511b861a72cc1f03b5a880faba71a3b5\`) and R749SPS (PR #2461, commit \`d1eb596c0ba74ea351ab08b23b4fe1832c56680b\`). Scope is the *auxiliary signed 16-atom Walsh* source model, retaining full signed atoms and source total-variation observers.

## Exact object and question

Define \(\chi_m(k)=(-1)^{\mathrm{popcount}(k\mathbin{\&}m)}\) and
\[
p(t,s,h,u,v,w,z)[k]=\frac{1+t\chi_3(k)+s\chi_{12}(k)+h\chi_{15}(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16},\quad k=0,\ldots,15.
\]
At \((t,s)=(1/10,1/2)\), R749SPR proved that the complete calibrated optimal-center set is \(q_X=p(1/10,1/2,H/10,U/10,V/10,0,0)\) for \(X=(H,U,V)\in K\), where
\[
\begin{array}{ll}
-H-U-V\ge-2,&-H-U+V\ge-2,\\
-H+U-V\ge-2,&-H+U+V\ge-2,\\
H-U-V\ge-2,&H-U+V\ge-4,\\
H+U-V\ge-4,&H+U+V\ge-2.
\end{array}
\]
Every such center has exact minimax TV risk \(9/20\). R749SPS proved \(L_K(n)=(46n^3+33n^2+17n+3)/3\), \(L_K(1)=33\), \(L_K(2)=179\), normalized volume 92.

**New question:** Is each grid-\(n\) exactly optimal center an *exact average* of first-grid optimal centers, at every integer precision \(n\), rather than merely approximated by them?

## Theorem (integer decomposition property; all n)

For every integer \(n\ge1\) and every \(X\in nK\cap\mathbb Z^3\), there exist \(X_1,\ldots,X_n\in K\cap\mathbb Z^3\) such that
\[
\boxed{X=\sum_{j=1}^nX_j,\qquad q_{X/n}=\frac1n\sum_{j=1}^nq_{X_j}.}
\]
Thus the **33 first-grid calibrated minimax centers** form a universal finite alphabet for every positive precision level. In fact, \(K\) admits a **regular unimodular triangulation of exactly 92 tetrahedra**, each of normalized lattice volume one.

### Exact regular-lifting certificate

List all 33 points of \(P=K\cap\mathbb Z^3\) in lexicographic order. Lift each \(p_i=(H_i,U_i,V_i)\) to \((p_i,z_i)\in\mathbb Z^4\), setting
\[
z_i=1000(H_i^2+U_i^2+V_i^2)+j_i
\]
with lexicographic offsets
\[
(j_i)=(16,13,25,9,30,11,9,5,24,22,22,17,21,8,3,29,0,7,12,26,23,13,8,27,16,25,10,20,27,21,30,23,12).
\]

The accompanying executable standard-library certificate exhausts \(\binom{33}{4}=40,920\) quadruples, using integer determinants and Cramer's rule for the exact affine supporting heights. Exactly 34,580 quadruples have nonzero spatial determinant. **Precisely 92** quadruples define lower supporting facets; every one has exactly four tight lifted points and spatial determinant \(\pm1\). A separate exact face-incidence audit finds 44 boundary triangular faces and 162 interior triangular faces; boundary triangles lie in one of the eight true \(K\) facet planes, and coning the boundary mesh to the strict interior origin gives total normalized volume **92**. Thus the supporting lower tetrahedra constitute a complete regular simplicial subdivision of \(K\), and every simplex is unimodular.

The lower-hull construction gives nonoverlap and coverage by standard convex-polytope geometry: all lower supporting facets of the finite lifted hull are exhausted; each is simplicial, and their projections partition \(\operatorname{conv}P=K\). The independent boundary/cone volume check verifies the same normalized volume. All finite arithmetic is exact integer arithmetic; no floating-point geometric predicate is used.

### Proof of all-precision decomposition

For any \(X\in nK\cap\mathbb Z^3\), choose a unimodular tetrahedron containing \(X/n\), with vertices \(v_0,v_1,v_2,v_3\in P\). Write \(X/n=\sum_{i=0}^3\lambda_iv_i\) with \(\lambda_i\ge0\), \(\sum\lambda_i=1\). The integer matrix whose columns are \(v_1-v_0,v_2-v_0,v_3-v_0\) has determinant \(\pm1\), hence an **integer inverse**. Consequently
\[
(n\lambda_1,n\lambda_2,n\lambda_3)^{\mathsf T}
=A^{-1}(X-nv_0)\in\mathbb Z^3,
\quad n\lambda_0=n-\sum_{i=1}^3n\lambda_i\in\mathbb Z_{\ge0}.
\]
Take \(n\lambda_i\) copies of \(v_i\); the resulting \(n\) lattice points sum exactly to \(X\). Since the probability-law map \(X\mapsto q_X\) is affine, the same decomposition is a convex average of minimax-optimal probability laws and remains exactly minimax-optimal. This establishes the theorem for *every* positive integer \(n\).

## BRC-style branch provenance and level-two counting

The positive-rational **branch carrier** is the multiset of labeled first-grid optimal centers; the affine probability-average is an observer that can merge different origin multisets. The signed Walsh atom representation is retained separately, so positive branch mass is never treated as an encoding of arbitrary signed cancellation.

At \(n=2\), exhaustive integer enumeration gives \(\binom{34}{2}=561\) unordered two-source multisets, but exactly **179** distinct averaged optimal centers, covering all \(2K\cap\mathbb Z^3\). The largest observer fiber contains **13** multisets. An exact fiber collision is
\[
(-2,-1,1)+(-2,1,-1)=(-2,0,0)+(-2,0,0)=(-4,0,0).
\]
Two provenance-distinct branch populations yield the same projected optimal center. Further, an alphabet of \(a\) first-grid types produces at most \(a(a+1)/2\) unordered pairs, so any first-grid alphabet covering all 179 second-grid optimal centers must have **at least 19** types; in particular the 11 extreme vertices alone do not suffice. The 33-type construction is sufficient, not claimed minimal.

## Evidence, scope and next question

Execute \`python3 R749SPT_WALSH_OPTIMAL_CENTER_UNIMODULAR_CERT.py\`; \`R749SPT_WALSH_OPTIMAL_CENTER_UNIMODULAR_RESULTS.json\` is the complete saved PASS output. It verifies the finite lift exactly and gives reproducible level-two fibers. The **universal** integer-decomposition conclusion uses the unimodular-simplex proof, not numerical extrapolation from finitely many \(n\). The minimax-optimality interpretation uses the predecessor R749SPR theorem, itself author-checked and awaiting independent mathematical review.

**Open frontier:** identify the first parametric source/event wall of this \(K\) as \((t,s)\) moves, determine which nearby optimal-center polytopes admit a comparable integer or rational unimodular subdivision, and study higher-\(n\) branch-provenance multiplicities. A native X6/V29/V39 preserved-source and port map remains a separately typed bridge question. No additional native execution authority is claimed here.