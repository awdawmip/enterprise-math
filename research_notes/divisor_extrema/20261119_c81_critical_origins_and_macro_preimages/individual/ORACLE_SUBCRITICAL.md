# Individually chosen grid origins below the ordinary precision threshold

For one arrangement, an origin succeeds if the two rounded readings of that arrangement are unique in the full catalogue rounded at that same origin. The origin may be chosen individually for each target arrangement. Let O_c be the fraction of arrangements admitting at least one successful origin. Write
\[
 z=b/c,\qquad H=c^{3/4}2^{-p},\qquad m=\min(1,cH).
\]
The physical normalized readings of C78 are denoted by U_c and W_c. Each rounding cell in these coordinates has side H. An additive translation on either axis has no effect on O_c.

**Theorem.** Suppose \(1\le b\le c,\quad z\to0,\quad cm^3\to\infty,\quad m^2/z\to\infty\). Then \(O_c\to0\). In particular, for adjacent stocks this holds if \(p-\tfrac{25}{12}\log_2 c\to-\infty\). For \(\liminf b/c^{1/3}>0\), including stock doubling, it holds throughout the ordinary subcritical range \(p-p_*(c,b)\to-\infty\). The intervening adjacent-stock range up to the ordinary \(9/4\) coefficient remains unresolved by this theorem.

## Regular charts

We use the established spectral regularity in C78, “Nearby stock precision”, LOCAL_ADJACENT.md, in its opening regularity statement and its regular-domain covering argument. On compact interior sets the adjacent divided-difference map \(F_c=(U_c,P_c)\), where \(P_c=(W_c-U_c)/z\), tends in \(C^1\) to its limiting map \((U,P)\), and \(U_c\to U\) in \(C^2\). The Jacobian determinant of the limiting map and the Hessian determinant of U are nonzero except on a set of planar measure zero. Restrict to a sufficiently small regular chart and a compact subchart with a positive collar inside it. After swapping source coordinate names if needed, \(|U_x|\) is bounded below. Set \(a_c=\partial_yU_c/\partial_x U_c\). The gradient of its limit is
\[
 \nabla a=D^2U\,(-U_y,U_x)^T/U_x^2,
\]
which is nonzero. One derivative of \(a_c\) consequently has fixed sign and absolute value bounded below throughout a small rectangular chart. Its values lie in a bounded interval. Fubini along that derivative gives \( |\{Y:a_c(Y)\in E\}|\le C|E|\) for any measurable set E there. The chart may be enlarged slightly while retaining these bounds, shrinking the compact subchart first. There is a branch of \(F_c^{-1}\) on a uniform neighborhood of the image of this compact subchart with uniformly bounded first derivatives and Jacobian determinant bounded above and below. These assertions follow by shrinking about a regular point until \(DF_c\) differs uniformly from a fixed invertible matrix by a sufficiently small amount. Compact regular subcharts of this type cover all but arbitrarily small area of the source triangle. One may use finitely many closed rectangles with piecewise smooth boundaries, so their lattice densities tend to their planar densities.

## Four signed targets

Fix signs \((e_1,e_2)\in\{-1,1\}^2\) and a positive constant \(\kappa<1/10\), small enough for all the local operations below. Put \(t=\kappa m/c\). For a source X in the subchart take
\[
 Y=F_c^{-1}\big(F_c(X)+(e_1t,(e_2-e_1)t/z)\big).
\]
The larger translation is at most \(2\kappa\), since \(t/z=\kappa m/b\). Thus Y remains in the enlarged chart including a collar. In physical readings \((U_c,W_c)\) the displacement is exactly \((e_1t,e_2t)\). In particular opposite signs are covered. On the subchart with a collar, \(X\mapsto Y\) is one-to-one, Lipschitz with a uniform bound, and its inverse Jacobian determinant is uniformly bounded. The scalar function \(a_c(Y(X))\) is uniformly Lipschitz, and preimages of measurable sets of slopes E have area at most \(C'|E|\) by the change of variables above.

Choose integers R so that
\[
 1/m=o(R),\qquad R=o(\sqrt{cm}),\qquad R=o(m/z).
\]
Such R exist since \(m\sqrt{cm}=\sqrt{cm^3}\to\infty\) and \(m^2/z\to\infty\). Fix a large chart-dependent constant K. Inside a fixed bounded interval containing all slopes, exclude the rationals' neighborhoods
\[
 \bigcup_{1\le q\le K/m}\ \bigcup_{a\in\mathbb Z}
 \{\beta:|\beta-a/q|\le 1/(qR)\}.
\]
Include only neighborhoods meeting the bounded interval (or a fixed enlargement). Their total length is \(O_K(1/(mR))\), and their number is \(O_K(m^{-2})\). At a lattice source with exceptional slope, its grid square of side 1/c has slopes within \(O(1/c)\) of this union. The source-square interiors are disjoint. The bounded-density estimate applied to the enlarged union bounds the fraction of exceptional sources by \(O_K((mR)^{-1}+(cm^2)^{-1})=o(1)\). The subchart collar absorbs the boundary grid squares.

For any unexcluded slope \(\beta=a_c(Y)\), Dirichlet approximation gives a reduced \(a/q\) with \(K/m<q\le R\) and \(|\beta-a/q|\le1/(qR)\). Since \(ja/q\bmod1\), \(0\le j<q\), is the complete equally-spaced grid, \(j\beta\bmod1\) comes within \(1/(2q)+1/R\le m/(2K)+o(m)\) of every point of the circle. Write \(u=\{cY_x\}\), \(v=\{cY_y\}\). It follows that there are \(0\le j<R\) and an integer \(n=O(R)\) with
\[
 |(n-u)+\beta(j-v)|\le m/(2K)+o(m).
\]
Set \(Z=c^{-1}(\lfloor cY_x\rfloor+n,\lfloor cY_y\rfloor+j)\). Since \(R/c\to0\), this is a genuine catalogue point in the enlarged interior chart. Taylor's formula gives
\[
 c|U_c(Z)-U_c(Y)|\le \|\partial_xU_c\|_\infty(m/(2K)+o(m))+O(R^2/c)<\kappa m/3
\]
for sufficiently large fixed K and large c. Also
\[
 c|(W_c(Z)-W_c(Y))-(U_c(Z)-U_c(Y))|\le O(zR)=o(m)
\]
by the uniform gradient bound on \(P_c\). Hence both physical displacements from X have the prescribed strict signs and magnitude at most \(3t/2<H/2\).

After excluding the union of the four negligible exceptional source sets, there is a distinct competitor in each open quadrant, with both coordinate displacements below H/2 in magnitude. In any cell containing X there is an axis direction with at least H/2 of available room on each axis. Use the competitor in the resulting quadrant. The strict bounds cover origins on cell boundaries under the half-open floor convention. Exhausting the regular interior completes the proof.

## Specializations

For \(b=1\) and \(p-\tfrac{25}{12}\log_2 c\to-\infty\), one has \(m c^{1/3}\to\infty\), whence both conditions hold. For \(c^{1/3}\le b=o(c)\), ordinary subcriticality gives \(cH/\sqrt z=2^{p_*-p}\to\infty\). Since also \(1/\sqrt z\to\infty\), \(m/\sqrt z\to\infty\); finally \(cm^3=(m/\sqrt z)^3 b^{3/2}/\sqrt c\to\infty\).

## Stock spacings with a positive limiting ratio

It remains to justify the above corollary on a subsequence with \(z\to z_0>0\). Here \(cH/\sqrt z=2^{p_*-p}\to\infty\) implies \(cH\to\infty\). The finite two-coordinate map \((U_c,W_c)\) converges in \(C^1\) on compact interior regular sign charts to the two corresponding spectra. To see that its limiting Jacobian vanishes only on a null set, use the original spectrum formula of C80, OPTIMAL_ENDPOINT_CUTS.md, with \(s=(1+z_0)^{-15/4}<1\), \(A=4x^{15/4}\), \(D=4(y/x)^{9/4}\). These are locally smooth coordinates on the open triangle. Unfold the absolute values on a sign chart, allowing fixed signs for the two chosen spectra. Near \(0<A<1,\ D\downarrow0\), the continued spectra, up to these signs, satisfy
\[
 U=f(A)D^{14/3}(1+O(D)),\qquad W/U=s^4(1-sA)/(1-A)+O(D),
\]
where \(f(A)\ne0\) and the expansions after factoring out the displayed power are analytic in A,D. Hence with \(R=W/U\), \(R_A=s^4(1-s)/(1-A)^2+O(D)\) up to sign, \(R_D=O(1)\), \(U_A=O(U)\), and \(U_D\sim(14/3)U/D\). Thus \(\det d(U,W)=U\det d(U,R)\ne0\) there. The signed functions U,W analytically continue through their zero lines on the positive quadrant with the same rational spectrum formula, so \(\det d(U,W)\) is nonidentically zero for each continued sign chart. The zero lines, boundary and analytic Jacobian zero set have area zero.

At any regular point choose a compact inverse chart with a collar as before. In the physical two readings shift the target in each prescribed sign pair by \(t=\kappa\min(H,1)\), ensuring the target remains in the chart. Round each coordinate of its preimage to the nearest catalogue lattice coordinate. Bounded first derivatives give \(O(1/c)=o(t)\) true error in either reading. Thus off the discarded set, for large c each of the four open quadrants contains a competitor at coordinate distances below H/2. A subsequence argument combining \(z_0=0\) and \(z_0>0\) yields the stated full-spacing corollary whenever \(\liminf b/c^{1/3}>0\).

## Permanent uniqueness above the ordinary threshold

Write \(R_c(p)\) for the fraction unique under every offset simultaneously. For any finite catalogue, a point pair is capable of occupying one cell of physical side h precisely if its coordinate spacings are less than h in both axes. For one axis, an interval of length strictly less than h joining the two readings cannot meet both boundary lattices \(2h\mathbb Z\) and \(h+2h\mathbb Z\) between the two readings. Thus at least one of the two prescribed grids of side 2h keeps them together. Choose such a grid on each axis independently. With \(\mathcal T=\{0,1/2\}^2\) the four shifts in units of the larger mesh,
\[
 1-R_c(p)\le\sum_{a\in\mathcal T}(1-V_c(p-1,a)).
\]
By the C78 ordinary threshold and \(R_c(p)\le V_c(p,a)\) for any a, equivalently \(R_c(p)\to1\) if and only if \(p-p_*(c,b)\to+\infty\), for every spacing \(1\le b\le c\). The comparison is needed only on sequences with large p in its sufficient direction. This observation does not require uniform quantitative rates in the C78 theorem.
