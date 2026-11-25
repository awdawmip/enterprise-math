# R284HU — Exact full-K boundary correction and two threshold-free fixed-omission strips

2026-11-25. Author proof with exact symbolic coefficient certificates and exact integer checks; NOT_REVIEWED. Auxiliary binary-tag safe-word total-count observer, not native physical attribution. Frozen inputs: HT d9a5329739c288770a164382c7b8b1992d886c65:research_notes/portable_direct/R284HT_TERMINAL_PORT_EXACT_REDUCTION_20261125.md (signed-extension formula); HO 35dc10f164c6a93ea5d65c4b5285304188fae549:research_notes/portable_direct/R284HO_EXACT_FIXED_DEFICIT_POLYNOMIAL_STRIPS_20261125.md (full K). Account entry blobs verified at main 08900309e6d8fd0aabd2e4885d8c70282ebd506e. Current P000 V5, ACTIVE worldview, joint-preservation and portable protocol read. Own session recovery r1-20261125-1855-own-recovery confirms original RESEARCHER session open and original registration SUCCEEDED; no CLAIM or execution authority inferred from recovery. Owner inventory r1-20261125-1855-owner-read SUCCEEDED: as_of 2026-11-25T10:56:25.791203Z, no LEASED entries, source 6f27a670c11f9791099deb87d1d9066b7b268d2d. Independent continuation, no shared task state mutation.

## Results

For integers u>=1, 0<=q<u, set n=u, m=u+q, d=u-q. Use M_n(k)=(k+1)/(n+1) binom(2n+2,n-k), extended by zero off 0<=k<=n. Put C_ab(g)=sum_k M_a(k)M_b(g-k). The original HO quantities are Q=C_nm(d-1), S=Q+C_nm(d)+q R, R=C_(n-1,m)(d)+C_(n-1,m)(d-1), and P=sum_{j=0}^3 binom(3,j) C_(n-1,m-1)(d+1-j). Then K=P Q (3u+q+1)^2/[S^2(u+2q+1)].

1. Exact full-K boundary correction: P=R+E, E=M_(m-1)(0)[M_(n-1)(d)+M_(n-1)(d+1)]. Consequently the four direct convolution terms in P can be eliminated in favor of R and an explicit nonnegative boundary term. This holds on the entire valid integer domain, including q=0 (where E=0). It reduces the literal expression from eight convolution evaluations to four when q>0, without asserting a bit-complexity improvement. Only the stated total-count observer is compressed; labeled joint branches remain defined by the original sums.
2. For every integer u>=1, K(0,u+1)>K(0,u). For every integer u>=2, K(0,u)>K(1,u) and K(1,u+1)>K(1,u). These are unbounded, threshold-free fixed-omission strips, complementary to HO's fixed-deficit strips. No conclusion about q>=2 comparisons yet.
3. General fixed-q reduction: for any fixed nonnegative integer q, K(q,u) is a rational expression quadratic over quadratic in h_u=binom(2u,u)/binom(4u+4,u+1), with coefficients rational in u. Thus adjacent fixed-q comparisons reduce to polynomial signs on a bounded residual coordinate, with an explicit exact transport for h_u. This is a method for further strips, not a proof that all certificates succeed.

## Proof of the boundary correction

Let F_a(z)=sum_{k=0}^a M_a(k) z^k. The exact binomial difference M_a(k)=binom(2a+1,a-k)-binom(2a+1,a-k-1), with out-of-range binomials zero, gives by two Pascal steps
M_a(k)=M_(a-1)(k-1)+2M_(a-1)(k)+M_(a-1)(k+1) for k>=0, a>=1; the formal value at k=-1 of the binomial difference is zero. Therefore
(1+z)^2 F_(a-1)(z)=z F_a(z)+M_(a-1)(0).
Now P=[z^(d+1)] (1+z)^3 F_(n-1)F_(m-1).
Substitute the identity for m to obtain
P=[z^d](1+z)F_(n-1)F_m+M_(m-1)(0)[z^(d+1)](1+z)F_(n-1)=R+E.
No asymptotic expansion or independent-endpoint error payment is required.

## Exact fixed-q residual coordinate

Write B=binom(4u+4,u+1), H=binom(2u,u), h=H/B. For capacities a=u+alpha, b=u+beta and convolution index g=u+gamma, with fixed integer shifts, HT gives a signed term R_ab(g)=binom(S,j)[4(g+2)^2-S]/[S(S-1)], S=2(a+b+2), j=a+b-g. The quotient R_ab(g)/B is rational in u by factorial ratios with fixed shifts. The omitted terms in the signed extension, when the first class count J=N+i, N=a+1, i>=1, are
-binomial(2N,N+i) binomial(2M,j-N-i) (1-(N+i)/N)(1-(j-N-i)/M), M=b+1,
and the symmetric terms with classes swapped. The first sum has i<=beta-gamma-1, the second i<=alpha-gamma-1; empty sums are zero. In the valid domain the two negative-factor tails are disjoint, by j<=N+M-2. The fixed shifts give binomial(2N,N+i)/H rational in u by factorial ratios; binomial(2M,j-N-i) is a polynomial in u of fixed degree. These identities hold for integer u in the domain, interpreting forbidden binomial coefficients as zero and any removable rational singularity by the original count. In the particular shifts used in Q,C,R, E, all relevant small-index binomial products have fixed length. Hence Q/B,C/B,R/B,E/B are affine in h and K is quadratic/quadratic. For E, M_(n-1)(d), M_(n-1)(d+1) have fixed bottom indices q-1,q-2 and the other factor M_(m-1)(0) is H times a rational factor. The q=0 boundary is identically zero. The h-coordinate retains the exact signed truncation correction, rather than dropping it.

The exact h transport and elementary bound are
h_(u+1)/h_u = 3(u+2)(2u+1)(3u+4)(3u+5)/[4(u+1)(2u+3)(4u+5)(4u+7)],
0<h_u<=1/(2u+4)<=1/(u+1),
since among subsets counted by B there are H(2u+4) choosing u elements from the first 2u and one from the rest.

## The two strips

For q=0, all Q,C,R needed are in HT's exact terminal range: C_(u,u) at g=u-1,u; C_(u-1,u) at g=u-1,u. After division by B they equal
Q/B=u/(4u+3),
C/B=(u^2+3u+3)/[(3u+4)(4u+3)],
P/B=R/B=(2u^2+4u+3)/[4(2u+1)(4u+3)].
Substitution yields the closed form
K(0,u)=u(3u+1)^2(3u+4)^2(2u^2+4u+3)/[4(u+1)^3(2u+1)(4u+3)^2].

For q=1, u>=2, the four normalized quantities (denoted Q,C,R,E in the following display only) are
Q=2(4hu^2+26hu+12h+2u^2-2u-3)/[(u+2)(u+3)],
C=2(6hu^2+11hu+4h+2u^3+4u^2+u-1)/[(u+1)(u+2)(3u+4)],
R=(2hu^2+9hu+4h+u^2-1)/[(u+1)(u+2)],
E=2h(2u+1)/[(u+1)(u+2)].
These follow from the signed formula and its finite omitted terms above: for Q the first tail i=1,2 and second i=1; for C first tail i=1 only; for R the two summands have first tail i=1 and i=1,2 respectively, with no second tail. E follows directly from M_(u-1)(u-1)=1. Thus N1=(R+E)Q(3u+2)^2, D1=(Q+C+R)^2(u+3), K(1,u)=N1/D1. All actual denominators are positive by original counts. Let N0,D0 be numerator and denominator of the q=0 closed form. The signs of the three comparisons are those of K0(u+1)-K0(u), N0 D1-D0 N1, and N1(u+1,h*ratio)D1(u,h)-D1(u+1,h*ratio)N1(u,h).

Exact symbolic certificate: factor each rational comparison and clear its positive denominator. For the first comparison use u=1+x, x>=0. For the second use u=2+x, h=z in [0,1]. For the third use u=2+x, h=z/(u+1), z in [0,1], and multiply by (u+1)^degree_h. For a degree L polynomial sum_i a_i(u) z^i, its Bernstein coefficients on [0,1] are b_k=sum_{i<=k} a_i binom(k,i)/binom(L,i), since z^i=sum_{k=i}^L binom(k,i)/binom(L,i) binom(L,k) z^k(1-z)^(L-k). All coefficients of each b_k(x+start) are strictly positive in the executed symbolic check. Thus each comparison is strictly positive on the stated entire domain, including endpoints. This is an exact finite symbolic certificate for an unbounded proposition, not extrapolation of finite sampling.

Executed minima in Bernstein coefficient order, using exact SymPy arithmetic:
- q=0 reading, degree 0, start 1: [5184].
- q=0 vs 1 omission, degree 2, start 2: [1890, 2934, 1746].
- q=1 reading, degree 4, start 2: [239542272, 210387456, 181232640, 152077824, 122923008].

## Executed replay code

```python
import sympy as s
from math import comb
from fractions import Fraction as F
from functools import lru_cache
u,h,z=s.symbols('u h z')
K0=u*(3*u+1)**2*(3*u+4)**2*(2*u*u+4*u+3)/(4*(u+1)**3*(2*u+1)*(4*u+3)**2)
Q=2*(4*h*u*u+26*h*u+12*h+2*u*u-2*u-3)/((u+2)*(u+3))
C=2*(6*h*u*u+11*h*u+4*h+2*u**3+4*u*u+u-1)/((u+1)*(u+2)*(3*u+4))
R=(2*h*u*u+9*h*u+4*h+u*u-1)/((u+1)*(u+2))
E=2*h*(2*u+1)/((u+1)*(u+2))
P=R+E; S=Q+C+R
N1=s.factor(P*Q*(3*u+2)**2);D1=s.factor(S*S*(u+3))
N0,D0=s.fraction(s.factor(K0))
ratio=3*(u+2)*(2*u+1)*(3*u+4)*(3*u+5)/(4*(u+1)*(2*u+3)*(4*u+5)*(4*u+7))
def mincoef(p,start):
    return min(s.Poly(s.expand(p).subs(u,u+start),u).all_coeffs())
def check(p,start,power):
    num,den=s.fraction(s.factor(p));print('denominator',den,flush=True)
    assert mincoef(den,start)>0
    degree=s.degree(num,h)
    pp=s.Poly(s.cancel(num.subs(h,z/(u+1)**power)*(u+1)**(power*degree)),z)
    vals=[mincoef(sum(pp.nth(i)*s.binomial(k,i)/s.binomial(degree,i) for i in range(k+1)),start) for k in range(degree+1)]
    assert min(vals)>0
    print('Bernstein minima',vals,flush=True)
check(K0.subs(u,u+1)-K0,1,0)
check(N0*D1-D0*N1,2,0)
check(N1.subs({u:u+1,h:h*ratio},simultaneous=True)*D1-D1.subs({u:u+1,h:h*ratio},simultaneous=True)*N1,2,1)
@lru_cache(None)
def M(n):
    a=[comb(2*n+2,n)//(n+1)]
    for k in range(n):
        b,r=divmod(a[-1]*(k+2)*(n-k),(k+1)*(n+k+3));assert r==0;a.append(b)
    return a
def conv(a,b,g):
    return sum(a[k]*b[g-k] for k in range(max(0,g-len(b)+1),min(g+1,len(a))))
def coef(a,k):return a[k] if 0<=k<len(a) else 0
def exact(u,q):
    m=u+q;d=u-q
    a,b,c,e=(M(n) for n in (u,m,u-1,m-1))
    Q=conv(a,b,d-1);C=conv(a,b,d);R=conv(c,b,d)+conv(c,b,d-1)
    P=sum(comb(3,j)*conv(c,e,d+1-j) for j in range(4))
    assert P==R+e[0]*(coef(c,d)+coef(c,d+1))
    S=Q+C+q*R
    return F(P*Q*(3*u+q+1)**2,S*S*(u+2*q+1))
n=0
for U in range(1,201):
    for q in range(U):exact(U,q);n+=1
    assert exact(U,0)==F(K0.subs(u,U))
    if U>=2:
        hu=F(comb(2*U,U),comb(4*U+4,U+1))
        assert hu<=F(1,2*U+4)
        assert F(ratio.subs(u,U))*hu==F(comb(2*U+2,U+1),comb(4*U+8,U+2))
        assert exact(U,1)==F((N1/D1).subs({u:U,h:hu}))
print('exact joint reduction checks',n,'closed form q0',200,'q1',199)
```

Actual execution passed all assertions: 20,100 exact full-P boundary identities (entire 1<=u<=200, 0<=q<u), 200 q=0 and 199 q=1 closed-form matches, 199 exact h bounds/transport checks, and the three exact Bernstein certificates. Denominator polynomials after factoring had strictly positive shifted coefficients. No floating-point inference. The symbolic test, not finite input checking, supplies the unbounded strip conclusions. A first attempted generic h<=constant bound failed for q=1 reading; using the exact h transport and the elementary polynomial bound resolved it.

## Next

Extend the fixed-q finite-tail rational reduction to q>=2, using sharper h bounds when needed and exact finite checks for any effective onset. More importantly exploit P=R+E for a direct full-K monotonicity comparison across arbitrary q,d: retain E, compare R/Q and C/Q with the prior coupled port curvature and mixed transport estimates. Do not re-prove the eventual full-scale result or the already proven fixed-deficit strips. Full integer-domain K monotonicity remains open. Independent review and strict Activity observation audit outstanding.
