# D25: exact gauge-depth filtration and marked-odd descent (author portable, 2026-10-28)

Status: AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE. Same author and research context as the existing all-order auxiliary norm/gauge theorem in Draft PR #1566. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged.

## Exact model and declared operations

For any odd prime p and n>=2 set B=Z/p^nZ, A=B[T]/(T^2-2), sigma(x+yT)=x-yT, P=1+pA. For eta=x+yT in P, define F_eta(v)=eta*sigma(v). Retain the labelled ordered basis (1,T). Even observer: z=F_eta^2=N(eta)=x^2-2y^2. Signed source-marked odd observer: y=[T]F_eta(1). The desired future operation is to read y modulo p^q, 1<=q<=n. This is an external finite arithmetic ring, not the native Heartbeat World X6 Cell space or a native H0/B0 experiment.

For each depth 1<=m<=n define the admissible auxiliary gauge subgroup G_m=1+p^m A and its action by multiplication conjugacy:

\[
M_u F_\eta M_u^{-1}=F_{\eta D(u)},\quad D(u)=u/\sigma(u),\quad u\in G_m.
\]

## Theorem (all odd p, all finite precisions and all gauge depths)

For each fixed z in 1+pB:

1. There is an exact sequence
\[
1\to 1+p^mB\to G_m\xrightarrow{D}
K_m:=\{\alpha\in1+p^mA:N(\alpha)=1\}\to1
\]
and |K_m|=p^(n-m), including the trivial case m=n.
2. Two normalized operators with the same norm are G_m-conjugate **if and only if** their signed T coefficients agree modulo p^m. Each fixed-norm fiber of size p^(n-1) therefore decomposes into exactly p^(m-1) orbits of exactly p^(n-m) labelled members, distinguished by y mod p^m.
3. The marked readout y mod p^q descends to the G_m quotient **if and only if q<=m**. For q>m it is changed by an admitted gauge transformation; a mark or a stricter proven admissible native gauge subgroup would be needed for reconstruction.
4. For any subgroup H of P, the fixed-norm quotient is exactly K_1/D(H), cardinality p^(n-1)/|D(H)|. An observer descends precisely if it is constant on D(H)-cosets. This is the scope-typed BRC fiber-constancy criterion for the given population, observer and future operation.

## Proof

Reuse, at its exact scope, the already proved bijection eta=(sqrt_1(z+2y^2))+yT, for z in 1+pB and y in pB. Here sqrt_1 is the unique square root congruent 1 mod p, by Hensel lifting with invertible derivative 2. Hence a norm fiber has |pB|=p^(n-1) labelled members.

For u in G_m, D(u) is 1 mod p^m and norm one. Conversely for any alpha in K_m, define u=(1+alpha)/2. Then u is in G_m and sigma(alpha)=alpha^(-1), so D(u)=(1+alpha)/(1+alpha^(-1))=alpha. Its kernel is u=sigma(u), equivalently vanishing T coefficient because 2 is a unit, namely 1+p^mB. Counting G_m and its kernel gives |K_m|=p^(n-m).

Conjugate eta,xi satisfy xi/eta=D(u) congruent 1 mod p^m; their y coefficients agree mod p^m. Conversely if N(xi)=N(eta)=z and y_xi=y_eta mod p^m, let eta=x+yT and xi=x'+y'T. Then (x'-x)(x'+x)=2(y'^2-y^2). Since x'+x is a unit and the right-hand side divisible by p^m, x'-x=0 mod p^m; thus xi/eta is in K_m and is reached by the explicit u above. Each y residue in pB modulo p^m has exactly p^(n-m) lifts, producing the orbit formula.

For q<=m, y mod p^q is constant on orbits. For q>m (so m<n), take eta=1, u=1+p^mT, xi=u/sigma(u). Then [T]xi=2p^m mod p^(m+1), whereas [T]eta=0; so the next digit changes even though z stays 1. This proves the sharp descent criterion. For a general H<=P, its image D(H) acts freely on each norm fiber, which is a K_1 torsor; the coset statement follows. QED.

## Original-class constraint, actual verification and provenance

The earlier auxiliary p=373,n=4 norm-one witnesses with y=+373 and y=-373 have difference of valuation one. This theorem proves them equivalent under G_1 yet inequivalent under G_2. A real native gauge-depth-two constraint would retain the first odd p-adic digit; authentic H0/B0 normalization and gauge restrictions must be supplied and proved before such a conclusion is transferred to native LIFT/JT2 or Delta_p-R_p.

Standalone exact Python checker: d25_gauge_depth_filtration_checker_20261028.py. The actual author run PASS covered 10 complete small cases (48,274 normalized source elements, 160,924 exact conjugator witnesses) and 42 target-prime depth witnesses including p=373,n=4. Its concise JSON is d25_gauge_depth_filtration_author_summary_20261028.json. This is same-author arithmetic confirmation; it is not an independent review or universal computational proof. Native Source CLAIM, OPEN, checkpoint and Result remain unverified under client quota/access limitations. Original H0/B0 support intake remains #1559. UR V2 original 94,687-byte bundle with SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76 remains unverified; original UR mathematics is not rerun.
