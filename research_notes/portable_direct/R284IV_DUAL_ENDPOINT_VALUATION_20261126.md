# R284IV — Dual endpoint exact valuation and equality exclusion
2026-11-26. Author proof and executed exact Fraction tests, NOT_REVIEWED. Independent continuation of the auxiliary binary-tag joint-count observer; not a native spatial/dynamics assertion. Frozen source IU@4dad003eece183b44e79c8ce362a823c06bdf8dc:research_notes/portable_direct/R284IU_ENDPOINT_PRIME_EQUALITY_EXCLUSION_20261126.md (blob 3d4d80d903ca0811a672c801cd82fb80f68169b1). IU retains IT/IS/IJ/IO pins. P000 V5, ACTIVE worldview, joint observer and heartbeat companion read. Historical Activity RA-B82240E8488EF5A1DA5186C4 / EM-DIRECT-0C386E; live own identity recovery returned BACKEND_IDENTITY_CHECK_UNAVAILABLE, operation_sent=false. Owner inventory r1-20261126-2205-owner-inventory last observed RUNNING. No shared Task or Activity mutation attempted without verified binding.

## Definitions and result
For integers q>=64, 1<=d<=2sqrt(q), u=q+d,m=u+q, l=d-k, let R_n(j)=prod_{i=0}^{j-1}(n-i)/(n+i+3).
w0=(k+1)(l+1)R_u(k)R_m(l), w1=(k+1)l R_u(k)R_m(l-1) for l>=1 and zero otherwise. v(k)=(u-k)(u+k+2)/(2u(2u+1)).
V=sum w0, Q=sum w1, A=sum v(k)(w0+w1).
E=R_u(d)(u-d)[(d+1)(u+d+2)+(d+2)(u-1-d)](m+2)/[2u(2u+1)(4m+2)].
Write Y=qK=q(3u+q+1)^2(A+E)Q/[(u+2q+1)(qA+Q+V)^2].
Let N1=q+2d+2, N2=q+d+1, T=-d*binom(2d+1,d).
For side 1 take prime p|N1, p>12d+14; for side 2 take prime p|N2, p>4d+6. Let t=vp(Ni). In either case,
vp(Y)=t+vp(Q)>=t, vp(Y-32/3)=0.
Thus the second endpoint gives a new unbounded equality-exclusion family, and the first endpoint's IU inequality is strengthened to exact valuation. Define C_i(d)=sum_{k=0}^{d-1}(k+1)(d-k)R_U(k)R_M(d-k-1) with (U,M)=(-d-2,-3d-4) for i=1 and (-1,-d-2) for i=2. These finite rational sums have p-unit denominators. Then Q=C_i(d) mod p and
Y/N1 = [(5d+7)^2(3d+2)/(5(d+1)(6d+7)T)] C_1(d) mod p;
Y/N2 = [-2/((d+1)T)] C_2(d) mod p.
Every prefactor is a p-unit under its respective hypothesis. In particular vp(Y)>t iff p divides the reduced numerator of C_i(d); the exact excess equals vp(Q), not necessarily vp(C_i(d)) beyond the first digit.

## Proof
The common endpoint product residue, with formal N tending to 0 at n=N-d-2, is N R_n(d) = T mod p: all numerator factors are -(d+2+i) and all denominator factors except the last are i-d+1. Their ratio is - (2d+1)!/[(d+1)!(d-1)!] = T. All these factors are units for p in either case.
Side 1: u=N1-d-2, m=2N1-3d-4, q=N1-2d-2. IU established the unique pole at k=d of V, Q and A integral, and unit status of outer factors. More precisely N1 V=(d+1)T mod p. The endpoint formula gives N1 E=T*(d+1)(3d+2)/(12d+14) mod p, nonzero. Therefore vp(A+E)=-t and vp(qA+Q+V)=-t. At N1=0, q(3u+q+1)^2/(u+2q+1)=2(5d+7)^2/5 mod p, a unit. Inserting the leading residues yields the first displayed coefficient and exact valuation.
Side 2: u=N2-1,m=2N2-d-2,q=N2-d-1. All R_u factors are p-units: numerator shifts -(1+i), denominator shifts i+2. All R_m factors are p-units except the last denominator m+d+2=2N2 at l=d, and all m numerator shifts -(d+2+i) are units. The factors 2u,2u+1,4m+2,u+2q+1,q,3u+q+1 are units, with residues -2,-1,-4d-6,-2d-2,-d-1,-d-3 respectively. Thus unique pole k=0 in V, and none in Q; N2 V=(d+1)T/2 mod p. A has the same pole times v(0)=-1/2 mod p. E is integral because R_u(d) and its endpoint denominators are units. So vp(A+E)=-t. The leading pole of qA+Q+V has coefficient (1+q v(0))=(d+3)/2 mod p times N2 V, a unit; its valuation is -t. The outer prefactor is (d+3)^2/2 mod p. Combining yields Y/N2=-Q/(N2 V) mod p and vp(Y)=t+vp(Q). Q is p-integral, and p>3 implies vp(Y-32/3)=0. Substitution into the shifted Q fibers gives C_i(d) modulo p without singular factors; in particular C_2(d)=sum_{l=1}^d (-1)^(d-l) l R_{-d-2}(l-1), since (k+1)R_{-1}(k)=(-1)^k.
All statements retain V,Q,A,E and full composite q; the p-adic readout is only a certificate for non-equality and extra valuation, not a replacement for the real residual or a real absolute-value bound.

## Second unbounded near-critical family
For sufficiently large prime p, take d=nearest integer to s0 sqrt(p)+C0-s0^2/2, q=p-d-1. Then N2=p, q~p, d~s0 sqrt(q), p>4d+6 and d^2<=4q since s0<2 by the frozen IO interval. Taylor expansion gives sqrt(q)=sqrt(p)-s0/2+O(p^-1/2). Thus for the frozen critical approximation Tcrit(q)=s0 sqrt(q)+C0+Z0/sqrt(q), |d-Tcrit(q)|<=1/2+O(p^-1/2)<1 eventually. Infinitely many distinct q follow from q~p and unbounded primes. No density or universal exclusion follows from this construction.

## Exact executed tests and reproduction
Python standard library Fraction, d=1..25, all primes p<=1200 satisfying the respective bound, N in {p,2p,p^2}, q=N-2d-2 or N-d-1, retain q>=64 and d*d<=4q. 11,784 side-1 and 13,247 side-2 cases, all assertions passed. Extra valuation cases 15 and 29 respectively (case counts, not distinct primes). Examples side 1: (q,d,p,N)=(301,7,317,317),(618,7,317,634),(100473,7,317,100489),(149,8,167,167); side 2: (78,3,41,82),(1677,3,41,1681),(98,4,103,103),(201,4,103,206),(10604,4,103,10609). Exact replay:
```python
from fractions import Fraction as F
from math import isqrt,comb
def R(n,d):
    a=[F(1)]
    for i in range(d):a.append(a[-1]*F(n-i,n+i+3))
    return a
def C(d,i):
    u,m=(-d-2,-3*d-4) if i==1 else (-1,-d-2)
    P,S=R(u,d-1),R(m,d-1)
    return sum((k+1)*(d-k)*P[k]*S[d-k-1] for k in range(d))
def vals(q,d):
    u=q+d;m=u+q;P,S=R(u,d),R(m,d);V=Q=A=F(0)
    for k in range(d+1):
        l=d-k;v=F((u-k)*(u+k+2),2*u*(2*u+1))
        w0=(k+1)*(l+1)*P[k]*S[l]
        w1=(k+1)*l*P[k]*S[l-1] if l else 0
        V+=w0;Q+=w1;A+=v*(w0+w1)
    E=P[d]*F((u-d)*((d+1)*(u+d+2)+(d+2)*(u-1-d))*(m+2),2*u*(2*u+1)*(4*m+2))
    Y=F(q*(3*u+q+1)**2,u+2*q+1)*(A+E)*Q/(q*A+Q+V)**2
    return V,Q,A,E,Y
def vp(x,p):
    if not x:return float('inf')
    x=F(x);a,b=abs(x.numerator),x.denominator;t=0
    while a%p==0:a//=p;t+=1
    while b%p==0:b//=p;t-=1
    return t
def mod(x,p):
    x=F(x);return x.numerator*pow(x.denominator,-1,p)%p
ps=[p for p in range(2,1201) if all(p%j for j in range(2,isqrt(p)+1))]
counts=[0,0];extra=[0,0]
for i in (1,2):
    for d in range(1,26):
        T=-d*comb(2*d+1,d)
        for p in ps:
            if p <= (12*d+14 if i==1 else 4*d+6):continue
            for N in (p,2*p,p*p):
                q=N-(2*d+2 if i==1 else d+1)
                if q<64 or d*d>4*q:continue
                t=vp(N,p);V,Q,A,E,Y=vals(q,d);c=C(d,i)
                assert vp(V,p)==-t and mod(Q,p)==mod(c,p)
                if i==1:
                    assert vp(A,p)>=0 and vp(E,p)==-t
                    assert mod(N*V,p)==mod((d+1)*T,p)
                    assert mod(N*E,p)==mod(T*F((d+1)*(3*d+2),12*d+14),p)
                    ratio=F((5*d+7)**2*(3*d+2),5*(d+1)*(6*d+7)*T)
                else:
                    assert vp(A,p)==-t and vp(E,p)>=0
                    assert mod(N*V,p)==mod(F((d+1)*T,2),p)
                    assert mod(N*A,p)==mod(-F((d+1)*T,4),p)
                    ratio=-F(2,(d+1)*T)
                assert vp(Y,p)==t+vp(Q,p)
                assert mod(Y/N,p)==mod(ratio*c,p)
                assert vp(Y-F(32,3),p)==0
                counts[i-1]+=1;extra[i-1]+=vp(Q,p)>0
print(counts,extra)
# [11784,13247] [15,29]
```
Next: classify interior multiple poles and higher p-adic lifts of Q; implement shifted polynomial IS oracle separately. Real inverse-polynomial separation remains open. No independent review or shared Result claimed.
