# R284HN — All-scale eventual strict monotonicity by relative joint-port expansion

2026-11-25. Author proof, NOT_REVIEWED. Auxiliary binary-tag safe-word total-count observer; no native physical attribution. Frozen inputs: HM ee8f08bb614ff06cb63f6e2567d14ead674e42ff (R284HM_SUBCRITICAL_POLYA_PORT_TRANSPORT_20261125.md), HL b2e9363fef39a8f536548ad8eaca5a204b0e03e7 (R284HL_CRITICAL_SQRT_BAND_CORRELATED_PORT_TRANSPORT_20261125.md), HK b1b2d665ada2333db345b4b32a47857b59219f72 (R284HK_MOVING_DIAGONAL_BAND_MONOTONICITY_20261125.md), all under research_notes/portable_direct/. Conditional on their exact safe-word moment identities and proved bands. P000 V5 at EM source b893d27b85d57a66c5250a6fb28b0cd1f96b1617, ACTIVE worldview, joint observer and residual constraints read. Own session recovery r1-20261125-1156-own-recovery verified original registration r1-20261124-0256-r284gd-session-v1 SUCCEEDED, open MCP-8cd6c4fa26b9459d923ff73ba0082220, RA-B82240E8488EF5A1DA5186C4 / EM-DIRECT-0C386E. No shared CLAIM or run. Owner inventory r1-20261125-1156-owner-inventory RUNNING at prepublication observation; no claim inference.

## Result

There exists a finite U such that for every integer u>=U and every 0<=q<u, K(q,u+1)>K(q,u), and for every 0<=q<u-1, K(q,u)>K(q+1,u). No explicit U or finite complement claimed. The remaining asymptotic bridge is covered by a relative (rather than absolute) joint-port expansion. More precisely, for every fixed L>0, uniformly on 1<=lambda=d/sqrt(u)<=L sqrt(log u), with d=u-q, h=u^(-1/2), the HL expansion extends to

    (3u/32) K = 1+h A(lambda)+h^2 B(lambda)+O_L(h^3 (1+lambda)^C),

for some absolute finite C (not optimized), with A=13lambda/6-(log I)'/2, I=int_0^lambda x(lambda-x)exp(-x^2-(lambda-x)^2/2) dx, and B smooth with its first derivative polynomially bounded for lambda>=1. Consequently the scaled adjacent ratio gaps equal A'(lambda)+o(1) and A'(lambda)-1+o(1), uniformly in this growing band. In particular on any sequence lambda->infinity in it the limits are 5/2 and 3/2 respectively.

## Proof: relative expansion on a growing joint-port band

The exact frozen HM/HL moments and sums are
    M_n(k)=(k+1)/(n+1) binom(2n+2,n-k),
    C_(n,m)(g)=sum_(k=0)^g M_n(k)M_m(g-k), with C=0 for g<0,
    n=u, m=2u-d, Q=C_(n,m)(d-1),
    S=C_(n,m)(d)+Q+q[C_(n-1,m)(d)+C_(n-1,m)(d-1)],
    P=sum_(j=0)^3 binom(3,j) C_(n-1,m-1)(d+1-j),
    K=PQ/S^2 * (3u+q+1)^2/(u+2q+1).
Keep joint allocation k and g-k; no erasure claim beyond the total-count comparison.

1. Put T_n(k)=M_n(k)/M_n(0)=(k+1)prod_(i<k)(n-i)/(n+i+3). Write n=alpha/h^2+beta/h+gamma with alpha=1 or 2, beta=0 or -lambda, gamma=0 or -1. Let y=kh, z=(d+j)h=lambda+jh for fixed j in {-2,-1,0,1}. All indices are on support for large u in the declared band. Set R=1+lambda. In the finite product logarithm, for t=ih, the two fractions have analytic denominators alpha+beta h+gamma h^2, bounded below by alpha/2 for sufficiently small h in this band. The logs of 1-i/n and 1+(i+3)/n may be expanded through degree 3 in h, with pointwise remainder bounded by O(h^4 R^c) for an absolute finite c: indeed t,beta are O(R), the rational denominator expansion has a geometric remainder, and the log Taylor remainder is bounded by a constant times the fourth power of its argument when that argument has modulus <=1/2. Summing at most O(R/h) terms, using the exact polynomial power sums for the retained coefficients, gives
    log[T_n(k)/(k+1)]=-y^2/alpha+h U(y,lambda)+h^2 V0(y,lambda)+O(h^3 R^c')
where U,V0 are polynomials in y,lambda, U independent of gamma. In particular h R^b ->0 for every fixed b on this band. Exponentiating the correction (not the leading negative exponent) gives
    h T_n(k)=(y+h) exp(-y^2/alpha)[1+h U+h^2 V+O(h^3 R^c'')],
V=V0+U^2/2. This is a relative remainder after retaining the Gaussian weight, with polynomially growing constants. It holds uniformly even at y=0. All big-O exponents below are fixed and can be enlarged finitely.

2. Multiply the two port expansions. Their common Gaussian is G_z(y)=exp(-y^2-(z-y)^2/2)=exp(-z^2/3) exp(-3(y-z/3)^2/2). Expand the polynomial product in h through degree 2; the remainder is bounded pointwise by h^3 R^c exp(-z^2/3). Summing with mesh weight h costs only an additional O(R). Apply Euler-Maclaurin through the endpoint derivative term to each retained polynomial times G_z; the fourth derivative is a polynomial times G_z, so the quadrature remainder is O(h^4 R^c exp(-z^2/3)), using the integral of the absolute fourth derivative and, if retaining the order-four endpoint term, its same bound. Endpoint contributions of higher order than two may be placed in the h^3 remainder. Thus for z=lambda+jh,
    h^3 C_(n,m')(d+j)/(M_n(0)M_m'(0))
       = I(z)+h D(z,lambda)+h^2 E_(gamma1,gamma2)(z,lambda)
         +O(h^3 R^c exp(-z^2/3)).
D is independent of gamma1,gamma2. All coefficient functions are finite sums of integrals of polynomials times G_z and endpoint evaluations of polynomial derivatives of G_z. Their derivatives in z and lambda through any fixed finite order have bounds O(R^c exp(-z^2/3)), by the Leibniz rule; differentiating an endpoint produces another polynomial times the Gaussian at the endpoint. This also covers I and its derivatives. Taylor expanding at z=lambda through the needed order therefore gives
    I(lambda)+h[D(lambda,lambda)+j I'(lambda)]
       +h^2 Etilde_(gamma1,gamma2,j)(lambda)
       +O(h^3 R^c exp(-lambda^2/3)).
The exponential factors at z and lambda are comparable, because |z-lambda|=O(h) and hR->0.

3. Crucial relative normalization: for lambda>=1/2, I(lambda)>=c0 exp(-lambda^2/3) for an absolute c0>0. For lambda>=3 integrate over |y-lambda/3|<=1/6; there both y and lambda-y are bounded below by constant multiples of lambda, giving even c1 lambda^2 exp(-lambda^2/3). On [1/2,3], continuity and positivity give the lower bound. Dividing the preceding expansion by I now costs only polynomial factors, NOT exp(lambda^2/3). The normalized coefficients and their first several derivatives grow at most polynomially, by the quotient rule and the same relative bounds. In particular the fixed shift ratios C_(n,m)(d+j)/C_(n,m)(d) equal 1+j h ell+h^2 times a smooth polynomially bounded coefficient +O(h^3 R^c), ell=I'/I. Shifted n,m include the corresponding exact zero-moment factors M_(n-1)(0)/M_n(0)=(n+2)/(4n+2)=1/4+O(h^2 R^c), with a second-order expansion and paid remainder. This is HL's cancellation with the same first-order term, now uniform in the growing band. Rational operations are valid because all normalized leading constants are positive and hR^c->0. Explicitly, relative to C=C_(u,m)(d), the first-order expansions of Q/C,P/C,S/C are 1-h ell, (1/2)(1-h ell/2), (u/2)(1-h(lambda+ell/2)), respectively; W=(16u/3)(1+h lambda/6+...). This gives the claimed normalized K expansion, including smooth B with polynomial derivative bound, and paid remainder h^3 R^C. No independent cancellation of positive branch masses is asserted.

4. Adjacent differences. At fixed u, q->q+1 changes lambda by -h. Taylor's theorem for A, whose derivatives have polynomial bounds from step 3, and the mean value bound for B, yield h^2 A'(lambda)+O(h^3 R^C) for the difference of normalized K. At fixed q, u->u+1 changes h by O(h^3), lambda by h+O(h^2 R); this yields the corresponding increase h^2 A'(lambda)+O(h^3 R^C) in normalized K. The true prefactor u/(u+1)=1-h^2+O(h^4) subtracts 1 from the scaled u-gap. Dividing by normalized K=1+O(hR^C) preserves these estimates, after enlarging C. Both scaled errors O(hR^C) tend uniformly to zero. The proof uses an enlarged band lambda>=1/2 and lambda<= (L+1)sqrt(log u) at endpoints, so no endpoint issue.

5. HL's exact covariance identity gives (log I)''<0 and A'>13/6. Thus both directions have a uniform strict eventual gap in the entire declared growing band. For the super-square-root limit, put y=lambda/3+t. Then
    I=e^(-lambda^2/3) int_(-lambda/3)^(2lambda/3)
      [2lambda^2/9+lambda t/3-t^2] e^(-3t^2/2) dt.
Extend the integral to the full real line with error and its first two lambda derivatives O(poly(lambda)e^(-lambda^2/6)); this follows by Gaussian tail integration by parts and the endpoint rule. The full integral is c(2lambda^2/9-1/3), c=int_R exp(-3t^2/2)dt>0. Hence (log I)''=-2/3+O(lambda^-2), and A'->5/2, A'-1->3/2.

6. Combine the frozen HM theorem for d<=2sqrt(u) (including fixed d), this growing-band theorem with L=17, and HK for both endpoints satisfying d^2>=256u log u. For sufficiently large u, every adjacent comparison either has d<=2sqrt(u), has lambda in [1,17sqrt(log u)] with endpoints in the slightly enlarged band, or has both endpoints in HK (the 17 versus 16 overlap absorbs the unit shifts). This proves the existence of a common finite U without computing it. It does not prove strict monotonicity at every finite u; the finite complement is still open. The proof depends on the prior author proofs, not independent acceptance.

## Executed exact finite evidence

The following Python 3 script ran to completion (12 base pairs, 36 exact K evaluations, 24 exact signs; the larger attempted sample timed out and is not counted). All decisions are exact fractions; floating point is used only to choose sample locations and display gaps.
```python
from math import comb,isqrt,log,sqrt
from functools import lru_cache
from fractions import Fraction as F
@lru_cache(None)
def m0(n):return comb(2*n+2,n)//(n+1)
def moments(n,g):
 a=[m0(n)]
 for k in range(g):
  v,r=divmod(a[-1]*(k+2)*(n-k),(k+1)*(n+k+3)) if k<n else (0,0)
  assert r==0
  a.append(v)
 return a
def K(u,d):
 q=u-d; m=u+q; g=d+1
 A,a,B,b=(moments(n,g) for n in (u,u-1,m,m-1))
 def C(a,b,g):return sum(a[k]*b[g-k] for k in range(g+1)) if g>=0 else 0
 Q=C(A,B,d-1);S=Q+C(A,B,d)+q*(C(a,B,d)+C(a,B,d-1));P=sum(comb(3,j)*C(a,b,d+1-j) for j in range(4))
 return F(P*Q*(3*u+q+1)**2,S*S*(u+2*q+1))
rows=[]
for u in (256,1024,4096):
 for d in sorted(set([2*isqrt(u),4*isqrt(u),int(sqrt(u*log(u))),int(2*sqrt(u*log(u)))])):
  if d>=u:continue
  k,kq,ku=K(u,d),K(u,d-1),K(u+1,d+1)
  assert k>kq and ku>k
  rows.append((u,d,d/sqrt(u),float(u*(k/kq-1)),float(u*(ku/k-1))))
print('pairs',len(rows),'exact_K',3*len(rows),'comparisons',2*len(rows))
for row in rows:print('%d %d %.8f %.10f %.10f'%row)
```
Output:
```
pairs 12 exact_K 36 comparisons 24
256 32 2.00000000 3.2170418271 1.8604144027
256 37 2.31250000 3.1831309988 1.7708622539
256 64 4.00000000 3.4021018952 1.5991256002
256 75 4.68750000 3.5787391980 1.5777982689
1024 64 2.00000000 3.0425258683 1.8676878918
1024 84 2.62500000 2.9321385682 1.7081286882
1024 128 4.00000000 2.9460106929 1.5925454484
1024 168 5.25000000 3.0484625976 1.5617261511
4096 128 2.00000000 2.9580884526 1.8715354415
4096 184 2.87500000 2.7874293422 1.6686170022
4096 256 4.00000000 2.7523575858 1.5858712810
4096 369 5.76562500 2.7936414987 1.5464297746
```
These are finite illustrative checks, not the proof of the uniform onset.

## Next

All asymptotic scales are now covered at author-proof level. Determine usable explicit constants or seek an exact discrete inequality to avoid a very large effective U; close finite complement for both directions with proof or exact certificates. Prioritize exact convolution/transport inequalities rather than repeating scale proofs. Independent mathematical review and strict Activity observation audit remain open.
