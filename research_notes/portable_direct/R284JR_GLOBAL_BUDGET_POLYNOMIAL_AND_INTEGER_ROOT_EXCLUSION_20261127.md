# R284JR — Joint denominator carrier and all-budget integer-root exclusion for d=3..80
2026-11-27. Author proof and exact Python checks; NOT_REVIEWED. Existing own recovered EM-DIRECT-0C386E / TASK_RESEARCH, RA-B82240E8488EF5A1DA5186C4, original session open, no formal runs (recovery r1-20261127-2004-recovery). Current LEASED read r1-20261127-2004-leased is WAITING_RESOURCE, EVENT_READ_CONTROL_BUSY at last observation; no shared task acquisition or mutation. Global canonical entries verified at f595758b62f83e03c5ed83d8cb513f68ac6d899d; EM current behavioral snapshot d4be5983f4413a8c48a7dc090e14c5aa99a287ad. P000 V4/V5, ACTIVE worldview, joint observer and residual contracts, portable research and current method consulted. Auxiliary exact arithmetic, not a native spatial bridge.

Frozen inputs: JQ aaf33a191be38a03736f73654f5f43b4d6dfac5d:research_notes/portable_direct/R284JQ_PADIC_LIFT_OBSTRUCTION_AND_CROSS_WINDOW_CLOSURE_20261127.md; JP a1d1eac1c1df905c12c4e7ebb7f41c9a995a7ee7:research_notes/portable_direct/R284JP_BUDGET_ZERO_FIBER_AND_PADIC_JETS_20261127.md. Original observer, including E, is unchanged. JQ covered q<p^6 with an eligible large prime for d<=500; the present theorem removes all prime-factor and upper-q restrictions for d<=80 by a different exact joint observer.

## 1. Exact polynomial carrier, arbitrary fixed d>=3
Let q>=64, d^2<=4q, u=q+d, m=2q+d, R_n(k)=product_{i=0}^{k-1}(n-i)/(n+i+3), l=d-k. Let a=(k+1)(l+1)R_u(k)R_m(l), b=(k+1)l R_u(k)R_m(l-1) (zero for l=0). V=sum a, Q=sum b, A=sum [(u-k)(u+k+2)/(2u(2u+1))]*(a+b). E=R_u(d)*(u-d)*(2d+3)*(m+2)/(2*(2u+1)*(4m+2)), W=A+E, Z=qA+Q+V. Equality qK=32/3 implies C=3q(4q+3d+1)^2 WQ-32(3q+d+1)Z^2=0.

Define D_n=prod_{i=0}^{d-1}(n+i+3), S_n(k)=prod_{i<k}(n-i) prod_{k<=i<d}(n+i+3), so S_n(k)=D_n R_n(k). Define polynomial weights a_k=(k+1)(l+1)S_u(k)S_m(l), b_k=(k+1)l S_u(k)S_m(l-1) or zero. Write v=sum a_k, b=sum b_k, a=sum (u-k)(u+k+2)(a_k+b_k). Put J=2u(2u+1), L=4m+2 and D=JL D_u D_m. All are integer polynomials in q. The *same* denominator gives
Wn=L a+u S_u(d) D_m (u-d)(2d+3)(m+2),
Qn=JL b,
Zn=L (q a+J(b+v)).
Exactly Wn=DW, Qn=DQ, Zn=DZ. Thus
P_d(q)=3q(4q+3d+1)^2 Wn Qn-32(3q+d+1)Zn^2 = D^2 C(q,d).
On the full legal real interval D>0. This is an exact sign and zero-set preserving observer, including the full joint endpoint, no poles erased and no approximation. Dividing P_d by its positive integer content preserves both.

For all d>=3, deg P_d=4d+9. In fact D has degree 2d+3, leading coefficient 32*2^d. As q tends to positive infinity, V -> binom(d+3,3), Q -> binom(d+2,3), A -> (V+Q)/4, E -> (2d+3)/16. Hence
lim C/q^3=48(A_infty+E_infty)Q_infty-96 A_infty^2
= -(d+1)(d+2)(2d+3)(d^2+2d+2)/2 < 0.
Each polynomial term has degree at most 4d+9, and this strictly negative limit proves the exact degree and negative leading coefficient. It also proves that for each fixed d there are only finitely many real zeros, and eventual negativity. The bound is not yet uniform in d.

## 2. All-integer-budget theorem for 3<=d<=80
Set L_d=max(64,ceil(d^2/4)), integer. Let F=P_d/content(P_d) and H_d(t)=F(L_d+t). Descartes' sign rule (ordinary real polynomial theorem) bounds strictly positive real roots with multiplicity by the number of sign changes in its nonzero coefficients. This is a proof over an unbounded q interval, not sampling or modular coverage.

Exact computation finds:
- d=3..10: H_d has zero sign changes and F(L_d)<0. Thus no real root on [L_d,infinity).
- d=11..80: H_d has exactly one sign change, F(L_d)>0 and negative leading coefficient. One and only one real root lies in (L_d,infinity), simple. Exact bisection gives consecutive integers l_d,h_d=l_d+1 with F(l_d)>0 and F(h_d)<0. Therefore that root is strictly between two consecutive integers. No legal integer q is a zero.

This proves qK(q,d)!=32/3 for every integer q>=64, 3<=d<=80, d^2<=4q, independently of smoothness, prime size, or q upper bound. It proves a unique real zero of C in the indicated interval for d=11..80 (not an integer equality counterexample). In particular, a claim of uniform real non-vanishing over that entire continuous domain would be false; the integer lattice is material.

All 70 lower endpoints l_d in order d=11..80:
69,89,111,135,162,190,221,254,289,326,366,407,451,496,544,594,646,701,757,816,876,939,1004,1071,1140,1212,1285,1361,1438,1518,1600,1684,1771,1859,1950,2042,2137,2234,2333,2435,2538,2643,2751,2861,2973,3087,3203,3321,3442,3564,3689,3816,3945,4076,4209,4344,4482,4622,4763,4907,5053,5201,5352,5504,5659,5816,5974,6135,6298,6464.

## 3. Reproduction
Exact Python/SymPy polynomial ring ZZ[q] only; no floating point and no factorization. Raw common denominator retained. 78 full coefficient sign checks; 70 bracketing pairs. Independent original Fraction implementation checked 218 signs (8 left endpoints + 70 sets of left endpoint and two bracket endpoints). All passed. Maximum raw degree 329 at d=80. A trial with polynomial gcd cancellation was unnecessary; the raw carrier sufficed. The following combines the executed raw polynomial and independent checks.

```python
from sympy.polys.rings import ring
from sympy import ZZ
from fractions import Fraction as Fq
R,x=ring('q',ZZ)
def carrier(d):
    u=x+d;m=2*x+d
    def scaled(n):
        tail=[R.one]*(d+1)
        for k in range(d-1,-1,-1): tail[k]=tail[k+1]*(n+k+3)
        z=R.one; out=[]
        for k in range(d+1):
            out.append(z*tail[k]);z*=n-k
        return tail[0],out
    Du,U=scaled(u); Dm,M=scaled(m)
    V=Q=A=R.zero
    for k in range(d+1):
        l=d-k
        a=(k+1)*(l+1)*U[k]*M[l]
        b=(k+1)*l*U[k]*M[l-1] if l else R.zero
        V+=a;Q+=b;A+=(u-k)*(u+k+2)*(a+b)
    J=2*u*(2*u+1);L=4*m+2
    W=L*A+u*U[d]*Dm*(u-d)*(2*d+3)*(m+2)
    Qn=J*L*Q;Zn=L*(x*A+J*(Q+V))
    P=3*x*(4*x+3*d+1)**2*W*Qn-32*(3*x+d+1)*Zn**2
    return P.primitive()[1]
def shift_coeffs(P,a):
    out=R.zero
    for c in reversed([P.get((i,),0) for i in range(P.degree()+1)]):
        out=out*(x+a)+c
    return out
def variations(P):
    a=[int(c>0) for _,c in sorted(P.items(),reverse=True) if c]
    return sum(i!=j for i,j in zip(a,a[1:]))
def primal(q,d):
    u=q+d;m=2*q+d
    def rr(n):
        a=[Fq(1)]
        for i in range(d): a.append(a[-1]*Fq(n-i,n+i+3))
        return a
    U,M=rr(u),rr(m);V=Q=A=Fq(0)
    for k in range(d+1):
        l=d-k;a=(k+1)*(l+1)*U[k]*M[l]
        b=(k+1)*l*U[k]*M[l-1] if l else 0
        V+=a;Q+=b;A+=Fq((u-k)*(u+k+2),2*u*(2*u+1))*(a+b)
    E=U[d]*Fq((u-d)*(2*d+3)*(m+2),2*(2*u+1)*(4*m+2))
    Z=q*A+Q+V
    return 3*q*(4*q+3*d+1)**2*(A+E)*Q-32*(3*q+d+1)*Z**2
rows=[]
for d in range(3,81):
    lo=max(64,(d*d+3)//4);P=carrier(d);v=variations(shift_coeffs(P,lo))
    a=P.evaluate(x,lo);assert a!=0
    assert P.degree()==4*d+9 and P.LC<0
    if v==0:
        assert d<=10 and primal(lo,d)<0
        rows.append([d,P.degree(),v,lo,None,None]);continue
    assert d>=11 and v==1 and a*P.LC<0
    hi=2*lo
    while P.evaluate(x,hi)*a>0: hi*=2
    l=lo
    while hi-l>1:
        mid=(hi+l)//2;y=P.evaluate(x,mid);assert y!=0
        if y*a>0:l=mid
        else:hi=mid
    assert P.evaluate(x,l)*P.evaluate(x,hi)<0
    assert primal(lo,d)>0 and primal(l,d)>0 and primal(hi,d)<0
    rows.append([d,P.degree(),v,lo,l,hi])
assert len(rows)==78 and sum(z[2] for z in rows)==70
print(rows)
```

## 4. Frontier
Try to prove the observed one-sign-change property uniformly in d without constructing all coefficients, using the positive denominator product and joint weighted convolution. Then study the unique crossing q_d asymptotically and its integer separation (the brackets alone do not give a uniform distance). The original smooth-budget obstruction has now been eliminated for d<=80, but unbounded d remains open. In the range 81..500 JQ's different conditional theorem is retained. A lower bound for |qK-32/3| on legal integer q is not yet obtained. No formal Result, task closure or independent review claimed.
