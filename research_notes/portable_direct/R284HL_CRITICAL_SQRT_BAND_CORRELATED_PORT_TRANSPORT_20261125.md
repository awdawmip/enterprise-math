# R284HL — Critical square-root band: correlated port-moment transport

2026-11-25. Author proof, NOT_REVIEWED. Scope: the auxiliary binary-tag safe-word total-count observer, not a native physical attribution. Own open session MCP-8cd6c4fa26b9459d923ff73ba0082220, EM-DIRECT-0C386E / RA-B82240E8488EF5A1DA5186C4; recovered from original registration r1-20261124-0256-r284gd-session-v1 by r1-20261125-1000-own-recovery. No shared CLAIM/run. Fresh LEASED inventory r1-20261125-1000-owner-read RUNNING at last prepublication read. Current account entry blobs verified at main@14091fcec902e744b93769232a8cbfbcc9ff0ad1, EM normative/control source 696158fe190359eabb652c010319b87c75474a50; P000 V5, ACTIVE worldview, joint observer and residual fidelity contracts read. Scientific pin: b1b2d665ada2333db345b4b32a47857b59219f72:research_notes/portable_direct/R284HK_MOVING_DIAGONAL_BAND_MONOTONICITY_20261125.md (full read, blob 9e1bb7bf5c1f034105d19dbd165dfd2560c5d8c2). Reuse its exact HA port identities, conditional on the original safe-word counting model. HK's moving strip excludes the critical scale addressed here.

## Theorem

Let d=u-q, h=u^(-1/2), lambda=d*h. For every fixed 0<a<b<infinity, uniformly for integers u tending to infinity and d with a<=lambda<=b, define
I(lambda)=integral_0^lambda x(lambda-x) exp(-x^2-(lambda-x)^2/2) dx,
ell(lambda)=I'(lambda)/I(lambda),
A(lambda)=13 lambda/6-ell(lambda)/2.
Then there is a smooth B(lambda) on (0,infinity) such that

    (3u/32) K(q,u)=1+h A(lambda)+h^2 B(lambda)+O_[a,b](h^3).

In particular the exact adjacent comparisons obey

    u*(K(q,u)/K(q+1,u)-1)=A'(lambda)+O_[a,b](u^(-1/2)),
    u*(K(q,u+1)/K(q,u)-1)=A'(lambda)-1+O_[a,b](u^(-1/2)).

Here A'(lambda)>13/6 for every lambda>0. Thus both desired strict inequalities hold throughout every fixed compact positive square-root band for all sufficiently large u. The thresholds can depend on a,b; no explicit finite threshold is asserted. Endpoints of an adjacent comparison may be in a slightly enlarged compact interval. This is a correlated expansion, not differentiation of an uncontrolled asymptotic error.

## Proof

Frozen exact moments:
M_n(k)= (k+1)/(n+1)*binom(2n+2,n-k).
Put T_n(k)=M_n(k)/M_n(0). On its support,
T_n(k)=(k+1)*product_(i=0)^(k-1) (n-i)/(n+i+3).
Define C_(n,m)(g)=sum_(k=0)^g M_n(k) M_m(g-k), with negative g giving zero. In this proof m=2u-d. Frozen counts:
Q=C_(u,m)(d-1);
S=C_(u,m)(d)+Q+q*[C_(u-1,m)(d)+C_(u-1,m)(d-1)];
P=sum_(j=0)^3 binom(3,j) C_(u-1,m-1)(d+1-j);
K=(P Q/S^2)*(3u+q+1)^2/(u+2q+1).

### 1. Uniform smooth port expansion with a paid remainder

For n=alpha*h^(-2)+beta*h^(-1)+gamma with alpha fixed positive, beta smooth bounded in lambda, gamma in {0,-1}, write y=kh. For k up to (b+2)/h the moment support includes every index once u is large. Write t=ih. Each summand log(1-i/n)-log(1+(i+3)/n) has a uniform Taylor expansion in h through degree 3 with error O(h^4) on the compact t/lambda domain (denominators bounded away from zero after multiplication by h^2). Its coefficients are polynomials in t, with smooth lambda dependence. Summing the degree 1,2,3 terms by exact polynomial power sums gives an expansion through degree 2 with uniform O(h^3) error: the first coefficient is -y^2/alpha, since sum_(i<k)(2i+3)=k^2+2k. The coefficient of h is independent of gamma because gamma first contributes to i/n at order h^3. Exponentiation and multiplication by h(k+1)=y+h give

    h T_n(k)=(y+h) exp(-y^2/alpha)
                *[1+h U_(alpha,beta)(y,lambda)
                    +h^2 V_(alpha,beta,gamma)(y,lambda)+O(h^3)],

with U,V smooth (polynomials before exponentiation), uniformly including y=0. In particular changing n by -1 affects only the coefficient of h^2 and higher in this normalized moment. The ratio of unnormalized zero moments is exactly M_(n-1)(0)/M_n(0)=(n+2)/(4n+2)=1/4+O(h^2).

For g=d+j with fixed j in {-2,-1,0,1}, and n=u+gamma1, m'=2u-d+gamma2, multiply the two normalized expansions with y=kh and z=gh=lambda+jh. Apply Euler-Maclaurin to the sum h*sum_(k=0)^g of the smooth products on [0,z]. Its leading term is the integral of x(z-x) exp(-x^2-(z-x)^2/2); endpoint half weights and the h^2 endpoint derivative correction give smooth coefficients, with O(h^3) error (the smooth coefficient functions have uniformly bounded derivatives through order four; the original O(h^3) pointwise residual remains O(h^3) after the h-weighted sum). Taylor expand at z=lambda. Consequently
    h^3 C_(n,m')(d+j)/(M_n(0)M_m'(0))
      = I(lambda)+h [D(lambda)+j I'(lambda)]
          +h^2 E_(gamma1,gamma2,j)(lambda)+O(h^3),
where D is independent of j and gamma1,gamma2 and E is smooth. This gives a second-order expansion without needing the explicit second-order coefficient. The positive I is bounded away from zero on each compact band; hence all subsequent divisions preserve the uniform third-order error.

### 2. Exact ratio cancellation

Normalize by C=C_(u,m)(d). Section 1 gives C_(u,m)(d+j)/C=1+j h ell+ h^2 times a smooth coefficient +O(h^3); the shifted n,m versions carry factors 1/4 per unit shift, with the same first-order correction. Thus, with all omitted h^2 coefficients smooth after the indicated normalization,
    Q/C = 1-h ell+O(h^2),
    P/C = (1/2)*(1-h ell/2+O(h^2)),
    S/C = (u/2)*(1-h(lambda+ell/2)+O(h^2)).
For P use sum binom(3,j)=8 and sum binom(3,j)(1-j)=-4. For S, q=u(1-lambda*h), and the two q-independent terms are O(h^2) relative to u. The coordinate multiplier is
    (3u+q+1)^2/(u+2q+1)
      = (16u/3)*(1+lambda*h/6+O(h^2)).
Combining these expansions yields the stated (3u/32)K and first-order coefficient A; second-order smooth B and uniform O(h^3) follow from Section 1 and the rational operations. No assertion that the underlying joint allocation distribution is disposable: this is only an expansion of its total-count comparison observer.

### 3. Strictly negative curvature of log I

Write f(x)=x exp(-x^2), g(y)=y exp(-y^2/2) for x,y>0, and extend by zero for nonpositive arguments. On (0,lambda) let X have density f(x)g(lambda-x)/I(lambda). Integration by parts (zero endpoint products), followed by differentiation under the integral (g(0)=0), gives
    I'/I = E[f'(X)/f(X)] = E[g'(lambda-X)/g(lambda-X)],
    I''/I = E[(f'(X)/f(X))*(g'(lambda-X)/g(lambda-X))].
The endpoint score singularities are integrable against the product density, including the mixed product, since lambda>0. Therefore
    ell' = Cov(1/X-2X, 1/(lambda-X)-(lambda-X)) < 0.
Indeed the first function is strictly decreasing in X and the second is strictly increasing; the covariance identity with two independent copies X,X' expresses the covariance as one half of the expected product of their score differences. The density is positive throughout (0,lambda), so strict negativity follows. Hence A'=13/6-ell'/2>13/6.

### 4. Pay the adjacent difference, not the full endpoint error

At fixed u, increment q changes lambda to lambda-h. Subtract the two normalized K expansions. The first-order coefficient difference is h^2 A'(lambda)+O(h^3), the smooth second-order coefficient difference is O(h^3), and each remaining error is O(h^3). Dividing by the normalized K at the second point, which is 1+O(h), gives the first adjacent limit. At fixed q, increment u changes h to h+O(h^3) and lambda to lambda+h+O(h^2), giving the same positive normalized increment. The actual K has the prefactor 1/u, whose ratio u/(u+1)=1-h^2+O(h^4) subtracts 1 from the limiting scaled gap. The strict signs are uniform by A'>13/6, and A'-1>7/6.

This avoids paying the two order-h corrections as independent errors: they describe the same smooth joint port coefficient. The first-order variation across adjacent integer budgets is itself order h^2, and only the third-order residual is paid.

## Executed check (exact integer counts; illustrative quadrature)

Python 3, fractions.Fraction, mpmath 40 decimal digits for the displayed continuous values only. All 24 adjacent sign assertions use exact integers/fractions; the numerical values of I and derivatives are not proof certificates. 12 base pairs, 36 exact K evaluations. The following script was run locally:
```python
from math import comb,isqrt
from fractions import Fraction as F
import mpmath as mp
mp.mp.dps=40

def moments(n,g):
    a=[comb(2*n+2,n)//(n+1)]
    for k in range(g):
        a.append(a[-1]*(k+2)*(n-k)//((k+1)*(n+k+3)) if k<n else 0)
    return a

def K(u,d):
    q=u-d; m=u+q; g=d+1
    A,a,B,b=(moments(n,g) for n in (u,u-1,m,m-1))
    def C(a,b,g):return sum(a[k]*b[g-k] for k in range(g+1)) if g>=0 else 0
    Q=C(A,B,d-1); S=Q+C(A,B,d)+q*(C(a,B,d)+C(a,B,d-1)); P=sum(comb(3,j)*C(a,b,d+1-j) for j in range(4))
    return F(P*Q*(3*u+q+1)**2,S*S*(u+2*q+1))

def I(l):return l**3*mp.quad(lambda t:t*(1-t)*mp.exp(-l*l*(t*t+(1-t)**2/2)),[0,1])
def A(l):return 13*l/6-mp.diff(lambda z:mp.log(I(z)),l)/2
for l in [mp.mpf('0.5'),mp.mpf(1),mp.mpf(2),mp.mpf(4)]:
    a=A(l);ap=mp.diff(A,l)
    print('lambda',l,'A',mp.nstr(a,12),'Aprime',mp.nstr(ap,12))
    for u in [1024,4096,16384]:
        d=int(l*isqrt(u));k=K(u,d);kq=K(u,d-1);ku=K(u+1,d+1)
        assert k>kq and ku>k
        x=mp.mpf((F(3*u,32)*k-1).numerator)/(F(3*u,32)*k-1).denominator*mp.sqrt(u)
        print(u,d,'Ahat',mp.nstr(x,10),'qgap*u',format(float(u*(k/kq-1)),'.10f'),'ugap*u',format(float(u*(ku/k-1)),'.10f'))
```
Actual output:
```
lambda 0.5 A -1.6939731871 Aprime 8.60306284234
1024 16 Ahat -1.628083941 qgap*u 7.8833164282 ugap*u 6.2784571268
4096 32 Ahat -1.651027446 qgap*u 8.2034854109 ugap*u 6.8608019209
16384 64 Ahat -1.669659896 qgap*u 8.3923851634 ugap*u 7.2086385029
lambda 1.0 A 1.09957191023 Aprime 4.06885420481
1024 32 Ahat 0.956503109 qgap*u 4.0564046650 ugap*u 2.8957650030
4096 64 Ahat 1.031896762 qgap*u 4.0601517896 ugap*u 2.9759837333
16384 128 Ahat 1.066742445 qgap*u 4.0638260418 ugap*u 3.0206939752
lambda 2.0 A 4.38121305051 Aprime 2.87593107204
1024 64 Ahat 4.601594134 qgap*u 3.0425258683 ugap*u 1.8676878918
4096 128 Ahat 4.493379956 qgap*u 2.9580884526 ugap*u 1.8715354415
16384 256 Ahat 4.437716267 qgap*u 2.9167081062 ugap*u 1.8736463405
lambda 4.0 A 9.72695690169 Aprime 2.57774417146
1024 128 Ahat 11.97093915 qgap*u 2.9460106929 ugap*u 1.5925454484
4096 256 Ahat 10.75658444 qgap*u 2.7523575858 ugap*u 1.5858712810
16384 512 Ahat 10.22106415 qgap*u 2.6628290294 ugap*u 1.5819588205
```

## Next

The critical regime d~sqrt(u) is now covered asymptotically, uniformly on every compact positive scaled band. The two unmatched regimes are d/sqrt(u) ->0 with d->infinity (fixed d q-direction strips remain HB) and d/sqrt(u)->infinity below the moving HK threshold. Seek an expansion with scale-adaptive error after adjacent differencing, or a direct exact finite moment transport inequality; then make effective bounds and close the finite complement. Do not reprove all-budget sign selection or the already established fixed-ratio strips. Separate proof review and Activity observation audit remain pending.
