# R749SUD — Exact two-port grid count, sharp saturation, and high-resolution volume

Date: 2026-11-18 (Asia/Shanghai). Evidence: AUTHOR_EXACT_NOT_REVIEWED. Independent portable continuation of R749SUC, [PR #2679](https://github.com/awdawmip/enterprise-math/pull/2679), source commit 376e0f41891050ac521295849bb52ccbdd2a9eea. Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389, definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md, WBRC-T30–T32. P000 is unchanged. No shared CLAIM or physical X6 event license is asserted.

## Model and previously established input

Let W be any rational 2-by-2 entrywise nonnegative matrix with spectral radius less than 1, with two *labeled* ports. For all four ordered port pairs, each resettable experiment adds an edge j/K (j=1,...,M), with integers 1<=M<K, and reads the stable/unstable bit; equality at spectral criticality is unstable. N(2,K,M) is the number of jointly realizable full four-pair response vectors.

The R749SUC theorem at the cited immutable source gives the exact star criterion for S=(I-W)^(-1)=[[A,B],[C,D]]:

A,D>=1, B,C>=0, and AD-BC>=max(A,D).

For any entry s>=0, its observed bin is h(s)=#{j=1,...,M : js>=K}. For off-diagonal h=0 the lower endpoint is 0; for 1<=h<=M the lower endpoint is K/(M-h+1). For diagonal 0<=i<M the *open* upper endpoint is U_i=K/(M-i); bin M is unbounded. R749SUC proves that when both diagonal bins are finite the joint bins are realizable iff L_b L_c < U_i U_j-max(U_i,U_j); when either diagonal bin is unbounded all off-diagonal bins can be realized. This manuscript uses that constructive exact theorem, without importing any changed scientific input.

## Theorem A. Exact integer floor formula, O(M^3) arithmetic

For every pair of integers 1<=M<K,

\[
\boxed{N(2,K,M)=(2M+1)(2M^2+2M+1)+
 \sum_{u,v,a=1}^{M}\max\left(0,M-\left\lfloor
 \frac{Kuv}{a(K-\max(u,v))}\right\rfloor\right).}
\]

Proof. There are (2M+1)(M+1)^2 choices for which at least one diagonal bin equals M, with all (M+1)^2 off-diagonal choices feasible. For the remaining M^2 finite diagonal pairs, the off-diagonal combinations with at least one zero bin contribute 2M+1 choices per pair: their lower product is 0, while U_i,U_j>1. For the positive off-diagonal bins substitute u=M-i, v=M-j, a=M-b+1, d=M-c+1, all 1,...,M. The strict corner condition is

\[
\frac{K^2}{ad}<\frac{K^2}{uv}-\frac K{\min(u,v)}
\quad\Longleftrightarrow\quad
(K-\max(u,v))ad>Kuv.
\]

For fixed u,v,a, admissible d in 1,...,M must satisfy d>Kuv/[a(K-max(u,v))]. Their number is max(0,M-floor(Kuv/[a(K-max(u,v))])). Summing and combining the first two contributions gives (2M+1)((M+1)^2+M^2)=(2M+1)(2M^2+2M+1). All operations are integer arithmetic; there are M^3 summands. QED.

## Theorem B. Sharp first saturation K and multiplicative energy

Define E_M=#{(a,d,u,v) in {1,...,M}^4: ad=uv}. Then

\[
\boxed{N_\infty(M)=(2M+1)(2M^2+2M+1)+\frac{M^4-E_M}{2},}
\]

where N(2,K,M) is nondecreasing in K>M and becomes identically N_infty(M) starting at the following **sharp integer**:

\[
\boxed{K_*(1)=2,\qquad K_*(2)=5,\qquad K_*(M)=M(M-1)^2+1\ (M\ge3).}
\]

Further,

\[
\boxed{E_M=M^2+2\sum_{h=2}^M\varphi(h)\lfloor M/h\rfloor^2.}
\]

Proof. The positive-bin condition in Theorem A is K(ad-uv)>max(u,v)ad. If ad<=uv it never holds; if ad>uv it holds exactly when

\[
K>\Theta(u,v,a,d)=\frac{\max(u,v)ad}{ad-uv}.
\]

Thus monotonicity holds and the plateau includes exactly those ordered quadruples with ad>uv. Swapping (a,d) and (u,v) exchanges > and <, leaving E_M ties; this proves the class count. To count ties, reduce a/u=v/d=r/s with gcd(r,s)=1. The two positive multipliers are each at most floor(M/max(r,s)); for max(r,s)=h there are 1 such coprime pair if h=1 and 2 phi(h) if h>=2. This proves the energy identity.

For M>=3, if ad<=(M-1)^2, then Theta<=M(M-1)^2 because ad-uv>=1. If ad>(M-1)^2 then the two factors <=M force ad to be M^2 or M(M-1). If ad=M^2, the largest strictly smaller product uv is at most M(M-1), whence Theta<=M^2. If ad=M(M-1), the largest strictly smaller product uv is at most (M-1)^2, giving Theta<=M^2. Since M^2<=M(M-1)^2 for M>=3, no threshold exceeds M(M-1)^2. Equality is attained by (a,d,u,v)=(M-1,M-1,M,M-2): ad-uv=1. Hence the first integer K satisfying all strict inequalities is K=M(M-1)^2+1, and the integer immediately below is missing at least that class. At M=2 the largest threshold is 4, attained by (a,d,u,v)=(2,2,2,1); M=1 is saturated at its first legal K=2. QED.

The totient identity and the standard elementary asymptotic sum phi(h)/h^2=(6/pi^2)log M+O(1) imply E_M=(12/pi^2)M^2 log M+O(M^2). Consequently

\[
\boxed{N_\infty(M)=\tfrac12M^4+4M^3-\frac6{\pi^2}M^2\log M+O(M^2).}
\]

The analytic asymptotic follows by expanding phi(h)=h sum_{d|h}mu(d)/d and using sum mu(d)/d^2=6/pi^2. This classical number-theoretic identity is used only for the asymptotic; Theorems A and B are fully integer exact.

## Theorem C. Simultaneously growing grid: exact leading volume

Put kappa=K/M>1 and define g(0)=1, g(t)=1-t+t log(t) for 0<t<1, and g(t)=0 for t>=1. The value g(t) equals the area of {(p,q) in (0,1)^2: pq>t}. Define

\[
V(\kappa)=\int_0^1\int_0^1 g\left(
\frac{\kappa xy}{\kappa-\max(x,y)}\right)\,dx\,dy.
\]

Then for every integer K>M>=1,

\[
\boxed{N(2,K,M)=M^4V(K/M)+O(M^3),}
\]

with an absolute error constant uniform over K>M. If K/M tends to a finite kappa>1 then N(2,K,M)/M^4 tends to V(kappa). V(kappa) is strictly increasing, 0<V(kappa)<1/2 for finite kappa>1, and tends to 1/2 as kappa tends to infinity.

Proof. In the positive-bin comparison write x=u/M, y=v/M, p=a/M, q=d/M. Its exact inequality becomes pq>kappa xy/(kappa-max(x,y)). For fixed x,y this is a coordinatewise monotone upper set in p,q, so comparing the M-by-M grid count with M^2 times its area has O(M) boundary-cell error, uniformly in the threshold. Summing over u,v contributes O(M^3) total error. The area integrand is bounded between 0 and 1 and nonincreasing in x and y; its two-dimensional right-grid Riemann sum differs from its integral by O(1/M) with a universal constant, via telescoping monotone one-dimensional slice bounds. This adds O(M^3). The polynomial contribution from Theorem A is also O(M^3). Strict monotonicity follows because its threshold decreases with kappa on a positive-measure open region, and g is strictly decreasing on (0,1). The limiting threshold is xy; for four independent uniform coordinates, the two products pq and xy are iid and have no ties, so their probability of > is 1/2. QED.

For quadrature set x0=(sqrt(1+4 kappa^2)-1)/(2 kappa) and a(x)=kappa x/(kappa-x). The two-dimensional volume reduces exactly to

\[
V(\kappa)=2\int_0^{x_0}\left(x-\frac34 a(x)x^2+
\frac12a(x)x^2\log(a(x)x)\right)dx
+\frac12\left(\log(1/x_0)-\frac{1-x_0}{\kappa}\right).
\]

Independent floating-point quadrature references, *not proofs*: V(1.25)≈0.323878703253, V(2)≈0.396956699250, V(4)≈0.451633920151. Exact count N(2,320,160)=275605156 (ratio 0.420540093994).

## Exact test evidence, scope and next question

The accompanying standalone dependency-free certificate counts signatures twice: Theorem A's O(M^3) integer formula versus R749SUC's original four-bin inequalities. It checked 252 (K,M) pairs for M=1,...,7; saturation and sharp boundary witnesses for M=1,...,10; all checks PASS. Representative values: N(2,4,3)=190, N(2,12,3)=206 and N(2,13,3)=208=plateau; N(2,36,4)=479 and N(2,37,4)=481=plateau. Full finite data appear in the machine results file. The arbitrary-domain theorems rely on the above proofs, not finite extrapolation. Author checked; not independently reviewed or formalized.

WBRC-T31 positive-rational visible Port feedback and stable hidden Schur collapse supply the mathematical observer interface. Source order, native six-spatial-axis Cell address, triadic closure, independent time, resources and physical event licensing in P000 are kept separate. New scientific directions are the finer transition for K growing in the M^2 to M^3 regimes, and an explicitly permitted causal, source-preserving native Cell/Link/Port lift.