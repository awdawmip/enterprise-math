# R284HW — Uniform two-parameter wedge monotonicity with paid boundary residual

2026-11-25. Author proof by exact polynomial certificate and explicit residual bound; NOT_REVIEWED. Auxiliary binary-tag safe-word total-count observer, same scope as HU/HV; no native physical attribution. Frozen inputs: HV at 8c93f2c7bee4f925d497c28d5e008977bd0ce872:research_notes/portable_direct/R284HV_FIXED_OMISSION_POWER_RESIDUAL_CERTIFICATES_20261125.md; HT at d9a5329739c288770a164382c7b8b1992d886c65:research_notes/portable_direct/R284HT_TERMINAL_PORT_EXACT_REDUCTION_20261125.md; HU provenance retained through HV. Current global main entry blobs 7b0754aa0fdf6f34db53b0349b6b0ebe74ecda42 and 01de3bea2155db8c4ce29f832906b2df114f88bf fetched; common immutable head not established in this run. Current P000 V5, ACTIVE worldview, joint preservation, portable research and residual policies read. Own session recovery r1-20261125-2100-own-recovery verified original registration SUCCEEDED and session not closed; RA-B82240E8488EF5A1DA5186C4 / EM-DIRECT-0C386E. Owner inventory r1-20261125-2100-owner-read SUCCEEDED, as_of 2026-11-25T12:58:40.696991Z, source 7a3d98091727bc8ed23b9f69d8bfc6c7e3eecbc4, LEASED filter returned no entries. No shared CLAIM or Result mutation.

## Theorem
For all integer q>=0, u>=640 and u>=2q+10,
 K(q,u+1)/K(q,u) > 1+1/[8(u+1)],
 K(q,u)/K(q+1,u) > 1+1/[8(u+1)].
This is a simultaneous unbounded two-parameter region, with explicit effective threshold, rather than a list of fixed-q certificates. The finite region below 640 and the wedge outside u>=2q+10 are not closed by this proof. Prior fixed-q and fixed-deficit results remain separately applicable.

## 1. Exact baseline, without dropping residual
M_n(k)=(k+1)/(n+1) binom(2n+2,n-k), zero outside 0<=k<=n; C_ab(g)=sum_k M_a(k)M_b(g-k). d=u-q, n=u,m=u+q. From HU: Q=C_nm(d-1), V=C_nm(d), A=C_(n-1,m)(d)+C_(n-1,m)(d-1), E=M_(m-1)(0)[M_(n-1)(d)+M_(n-1)(d+1)], K=(A+E)Q(3u+q+1)^2/[(Q+V+qA)^2(u+2q+1)].
HT signed extension R_ab(g)=binom(S,j) f(S,g), S=2(a+b+2), j=a+b-g, f(S,g)=[4(g+2)^2-S]/[S(S-1)]. Exact C=R+nonnegative omitted signed mass. Define K0 by replacing Q,V,A by their corresponding R expressions and E by zero, retaining actual residual as in section 3. For S=4u+2q+4, j=u+2q+1 and common binom(S,j), the normalized baseline counts are
 Q0=f(S,d-1);
 V0=j/(S-j+1) f(S,d);
 A0=j(j-1)/[S(S-1)] f(S-2,d)+j(S-j)/[S(S-1)] f(S-2,d-1).
The common binomial cancels from K0, but not from general joint observers. In section 3 Q0,V0,A0 denote the unnormalized signed counts.

## 2. Uniform polynomial margin
For each of H=K0(q,u+1)/K0(q,u)-1 and H=K0(q,u)/K0(q+1,u)-1, let H=N/D in reduced rational form (SymPy factor, as in replay). Substitute u=2q+x+10. All nonzero coefficients of D and 4(u+1)N-D in (q,x) are positive; all constant terms positive. Thus for all real q,x>=0 both ratios exceed 1+1/[4(u+1)]. Executed exact coefficient counts:
read D degree 19, 207 terms, constant 483532673384757342044160
read margin degree 19, 207 terms, constant 1581509973977163593459712
omit D degree 17, 168 terms, constant 150809020074181066752
omit margin degree 17, 170 terms, constant 4040623115057115417600.
This is a finite two-variable symbolic certificate, 752 nonzero coefficient checks, not a finite sample of q.

## 3. Uniform residual payment
At each of (u,q),(u+1,q),(u,q+1), write parameters U,Qp. U>=640 and U>=2Qp+8. Each of the four convolution counts has t=min(a,b)>=U-1, T=max(a,b)<=3t/2, g>=t/2. The signed baseline is positive, R/binom(S,j)>1/100 (HT proof for t>=50,T<=2t,g>=t/2: S<=7t and 4(g+2)^2-S>=t^2/2). For the hypergeometric law used by HT, each class has mean distance from its first zero layer N=a+1 or M=b+1 at least (g+2)/(1+T/t)>=t/5; j=a+b-g<=2t. HT factorial-moment tail proof gives exp(-2b^2/j) for an upper displacement b. Each excluded tail thus <=exp(-t/25), and C/R-1<=200 exp(-t/25).

The separate boundary E must also be paid. If d>U-1 it is zero. Otherwise the consecutive port ratio (k+2)/(k+1)*(U-1-k)/(U-1+k+3) is <1 for k>=t/2, and M_(m-1)(0)<=M_m(0) (Catalan consecutive ratio). Thus E<=2 M_(U-1)(d) M_m(0). In the convolution C_(U-1,m)(d), this is at most twice the boundary hypergeometric probability mass times its common binomial: the second class has sample count M-1 and the signed factors on this valid branch are in [0,1]. Its displacement from its mean is >=t/5-1>=t/6. The same tail proof bounds that probability by exp(-t/36). Divide by the positive signed R_(U-1,m)(d), which is <= the signed A0 and exceeds binom(S,j)/100. Hence E/A0<=200 exp(-t/36).

Set delta=200 exp(-(u-1)/36). All three adjacent parameter locations have C/R-1<=delta and E/A0<=delta, and so the exact K/K0 is between (1+delta)^(-2) and (1+2delta)(1+delta). The lower and upper bounds preserve the positive residual signs: A+E in numerator and A in denominator are not treated as independent arbitrary omitted data. For u>=640, delta<1/[100(u+1)]: at u=640 use e>8/3, (639)/36>17 and (8/3)^17>20000*641 (exact rational check); (u+1)exp(-(u-1)/36) decreases thereafter. Consequently each true adjacent ratio is > (1+1/[4(u+1)])/[(1+delta)^3(1+2delta)]. For 0<=delta<=0.1, denominator <=1+6delta by expansion. With delta<1/[100(u+1)], the ratio is >1+1/[8(u+1)] by elementary cross multiplication. This completes the simultaneous wedge theorem.

## 4. Exact replay and evidence
Python SymPy exact integer polynomials and fractions. Executed script logic below; no floating point used for signs. 60 exact true and baseline adjacent comparisons in 30 base locations, U in 40,100,250,640,800,1024 and q in {0,1,(U-10)//8,(U-10)//4,(U-10)//2}. At each of three compared locations, baseline rational formula checked against direct signed binomials, residual sandwich and each relative bound checked whenever U>=640. All assertions passed. Minimum observed (U+1) times the smaller true ratio gap = 1.0006511082758174 at (1024,0) (decimal display only). The infinite proof is the polynomial certificate plus paid residual, not this sample.

```python
from math import comb
from fractions import Fraction as F
from functools import lru_cache
import sympy as s
u,q,x=s.symbols('u q x',integer=True,nonnegative=True)
S=4*u+2*q+4;j=u+2*q+1;d=u-q
f=lambda S,g:(4*(g+2)**2-S)/(S*(S-1))
Q=f(S,d-1); V=j/(S-j+1)*f(S,d)
A=j*(j-1)/(S*(S-1))*f(S-2,d)+j*(S-j)/(S*(S-1))*f(S-2,d-1)
K=s.factor(A*Q*(3*u+q+1)**2/((Q+V+q*A)**2*(u+2*q+1)))
for name,a,b in [('read',K.subs(u,u+1),K),('omit',K,K.subs(q,q+1))]:
    N,D=s.fraction(s.factor(a/b-1))
    for label,expr in [('D',D),('margin',4*(u+1)*N-D)]:
        p=s.Poly(expr.subs(u,2*q+x+10),x,q)
        assert all(c>0 for c in p.coeffs()) and p.coeff_monomial(1)>0
        print(name,label,p.total_degree(),len(p.terms()),p.coeff_monomial(1))
assert F(8,3)**17 > 20000*641
@lru_cache(None)
def M(n):
    a=[comb(2*n+2,n)//(n+1)]
    for k in range(n):
        v,r=divmod(a[-1]*(k+2)*(n-k),(k+1)*(n+k+3)); assert r==0; a.append(v)
    return a
def C(n,m,g):
    a,b=M(n),M(m)
    return sum(a[k]*b[g-k] for k in range(max(0,g-m),min(n,g)+1))
def R(n,m,g):
    S=2*(n+m+2); j=n+m-g
    return F(comb(S,j)*(4*(g+2)**2-S),S*(S-1))
def true_and_base(U,Qp):
    m=U+Qp;d=U-Qp
    Q,V=C(U,m,d-1),C(U,m,d); A=C(U-1,m,d)+C(U-1,m,d-1)
    Q0,V0=R(U,m,d-1),R(U,m,d); A0=R(U-1,m,d)+R(U-1,m,d-1)
    E=M(m-1)[0]*sum(M(U-1)[k] for k in (d,d+1) if k<U)
    fac=F((3*U+Qp+1)**2,U+2*Qp+1)
    z=fac*F((A+E)*Q,(Q+V+Qp*A)**2); z0=fac*A0*Q0/(Q0+V0+Qp*A0)**2
    assert z0==F(str(K.subs({u:U,q:Qp})))
    if U>=640:
        delta=F(1,100*(U+1))
        assert all(0<=a/b-1<=delta for a,b in [(Q,Q0),(V,V0),(A,A0)])
        assert 0<=E/A0<=delta
        assert (1+delta)**-2 <= z/z0 <= (1+2*delta)*(1+delta)
    return z,z0
cnt=0;min_gap=None
for U in (40,100,250,640,800,1024):
    for Qp in sorted({0,1,(U-10)//8,(U-10)//4,(U-10)//2}):
        a,a0=true_and_base(U,Qp); b,b0=true_and_base(U+1,Qp); c,c0=true_and_base(U,Qp+1)
        assert b0/a0-1>F(1,4*(U+1)); assert a0/c0-1>F(1,4*(U+1)); assert b>a>c
        cnt+=2
        v=min(b/a-1,a/c-1)*(U+1)
        if min_gap is None or v<min_gap[0]: min_gap=(v,U,Qp)
print('comparisons',cnt,'min scaled actual gap',float(min_gap[0]),min_gap[1:])
```

## Next
Use the two-variable rational certificate in a wider wedge, with explicitly paid tails as d decreases. The remaining critical region near d=O(sqrt(u)) requires a different payment or a uniform discrete sign certificate. Do not repeat fixed q=0..12. Finite 250<u<640 wedge completion is another bounded open subproblem. Independent mathematical review and strict Activity observation audit pending.
