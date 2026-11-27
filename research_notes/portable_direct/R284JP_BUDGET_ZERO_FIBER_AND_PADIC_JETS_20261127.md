# R284JP — Budget-zero fiber, p-adic jet certificates and actual budget coverage
2026-11-27. Author proof and exact Python calculation; NOT_REVIEWED. Own recovered EM-DIRECT-0C386E / TASK_RESEARCH, RA-B82240E8488EF5A1DA5186C4; original session open, no formal runs (r1-20261127-1802-recovery). LEASED inventory r1-20261127-1802-leased-read SUCCEEDED, empty filtered list as of 10:04:09 UTC, source 42c0b9921b4917eec7346e284a8847f7724b0201 (Source changed during read; snapshot only). No shared ownership mutation. Current global canonical entries verified at 06fe30ceda819d4b90b8e13a7e3cc6f663083653; P000 V5, ACTIVE worldview, joint observer/residual fidelity and portable research rules consulted. Auxiliary exact arithmetic observer, not native spatial transfer.

Frozen input: JO 81cc0f06a4cf0209733a50284362f9bb1e8aded9:research_notes/portable_direct/R284JO_FULL_JOINT_BLOCK_TRANSFER_20261127.md; JF df5cac5b9a78bc685dc792efa70c847d75e74704:research_notes/portable_direct/R284JF_OFFSET_ADAPTIVE_HEIGHT_AND_LOCAL_EXCEPTION_BUDGET_20261127.md; JH decfd2e7f01e53d1036716b13efda9bf1bb36e87:research_notes/portable_direct/R284JH_SECOND_BRANCH_REMOVABLE_POLE_AND_HALF_WINDOW_20261127.md; JJ fe21b1a48ffccb3c00640e7d3e2afe6b6b2ba9e1:research_notes/portable_direct/R284JJ_SECOND_BRANCH_EDGE_MOMENT_COMPRESSION_20261127.md. Reuse their primal observer and sufficient pole certificates. No new external analytic theorem.

## 1. A fourth coordinate: q itself, exact zero-budget fiber
Let q>=64, d>=3 integers, d^2<=4q. Use u=q+d,m=2q+d,R_n(k)=prod_{i<k}(n-i)/(n+i+3); l=d-k, a=(k+1)(l+1)R_u(k)R_m(l), b=(k+1)l R_u(k)R_m(l-1) (zero at l=0), v=(u-k)(u+k+2)/(2u(2u+1)), V=sum a, Q=sum b, A=sum v(a+b), E=R_u(d)(u-d)(2d+3)(m+2)/(2(2u+1)(4m+2)), W=A+E,Z=qA+Q+V. Full C=3q(4q+3d+1)^2 WQ-32(3q+d+1)Z^2; equality Y=qK=32/3 implies C=0.

At formal q=0 write B=binom(2d+2,d), N=2d+2. R_d(k)=binom(N,d-k)/B. Weighted binomial polynomial P(x)=sum_{a=0}^N(d+1-a)binom(N,a)x^a=(d+1)(1-x)(1+x)^(2d+1). In V the two indices sum to d, in Q to d+1; the out-of-range endpoint a=d+1 has weight zero, so the complete coefficients are valid, not an independent marginal approximation. The weighted v observer corresponds to a(N-a)/(2d(2d+1)) and a(N-a)binom(N,a)=N(N-1)binom(N-2,a-1). Its polynomial is (d+1)x(1-x)(1+x)^(2d-1). With c(n,k)=[x^k](1-x)^2(1+x)^n and b0=(d+1)^2/B^2 obtain:
V0=b0 c(4d+2,d), Q0=b0 c(4d+2,d+1), A0=b0 c(4d+1,d), E0=0,
Z0=V0+Q0=b0 c(4d+3,d+1)
=4(d+1)^4 binom(4d+3,d+1)/(B^2(3d+3)(3d+4)).
Indeed c(n,k)=binom(n,k)*[(n+1)(n+2)-(4n+8)k+4k^2]/[(n-k+1)(n-k+2)]. All original rational functions are regular with p-unit denominators on q=0 mod p when p>2d+2 (4m+2 at zero is 2(2d+1)). The canceled Z0 product has consecutive factors 3d+5,...,4d+3 divided only by p-units; since p>2d+2, each such factor has at most one p and at most one is divisible. Thus v_p(Z0)=1 if 3d+5<=p<=4d+3, else 0. For p|q, p>2d+2 outside that interval, C mod p=-32(d+1)Z0^2 !=0. This is a new zero-budget fiber, complementary to the prior three windows. All sufficiently large prime q (e.g. q>=73) are certified for every legal d>=3 by p=q>4d+3; q=73 satisfies 4floor(sqrt(4q))+3=71, and q>8sqrt(q)+3 for q>=70.

## 2. Gap-prime jet theorem: at most two residue classes modulo p^3
For prime 3d+5<=p<=4d+1, the canceled Q0 and A0 products contain respectively 3d+4,...,4d+2 and 3d+4,...,4d+1; their coefficient numerators are respectively 4d(d+1),4(d+1)^2+2. Thus Q0,A0,W0 divisible by p; Z0 has valuation exactly 1. Rational p-unit functions have Taylor congruences for increments divisible by p^k: F(x+h)=F(x)+h F'(x) mod p^(2k), by polynomial multiplication and inversion of unit denominators. Derivatives reduce modulo p to their q=0 values on this fiber. No actual pole or missing endpoint E.

Write q=p s mod p^2. If z1=Z'(0) mod p, then Z(q)/p = Z0/p+s z1 mod p. If nonzero, C has valuation exactly 2 because first term divisible by p^3. If z1=0 this certifies every q divisible by p. Otherwise exactly one s0=-Z0/(p z1) mod p is a potential failure; s0!=0 so all q divisible by p^2 are certified. At q=p s0 mod p^2, W/p and Q/p are also affine first jets. If both are nonzero, first term has valuation 3, second at least 4, so C has valuation 3.

For the remaining case at least one W/p,Q/p is zero. Put q*=p s0 (least representative), q=q*+p^2 h mod p^3. Z/p^2=z2+h z1 mod p where z2=Z(q*)/p^2 mod p. If W/p=0 and Q/p is unit, WQ/p^3 = (W(q*)/p^2+h W'(0))*(Q(q*)/p) mod p. Interchange W,Q for the other case; if both zero the product is zero mod p. Write this affine function as L0+L1 h. Then
C/p^4 = 3s0(3d+1)^2(L0+L1 h)-32(d+1)(z2+h z1)^2 mod p.
Its quadratic coefficient -32(d+1)z1^2 is a unit. Therefore at most two h mod p can give zero. For fixed d,p, all q divisible by p are certified apart from at most two explicitly computable congruence classes modulo p^3; those classes are noncertificates, not equality examples. This is a deterministic compatible-jet constraint, no independence premise. If the quadratic has no root the entire fiber closes at order four.

Boundary p=4d+3 prime: Q0,W0 are units (their binomial tops <p; the coefficient factors at d=-3/4 mod p are units for d>=3). Also 3d+1=-5/4 mod p is a unit. Z0 has valuation 1. If t=v_p(q)=1 then C has valuation 1; if t>=3, C has valuation 2. If t=2, write q=p^2 s mod p^3. Then C/p^2=3s(3d+1)^2 W0 Q0-32(d+1)(Z0/p)^2 mod p. At most one nonzero s can fail. This handles all p>2d+2 with at most two residual classes mod p^3 for each fixed d,p. It does not require computing individual p-adic valuations at every q: evaluate q=0,p and, only in the exceptional first-jet class, q*,q*+p^2 to compute the polynomial. Original observers and E are retained. For fixed d,p, a budget interval of length <p^3 contains at most two of these undecided q, irrespective of smoothness or statistical independence.

## 3. Actual computation, exact Python
Direct Fraction equality of V,Q,A,Z at q=0 for d=3..100 (98); 2343 legal primal (q,d,p) tests with p in [2d+3,4d+49], q in {p,2p,p^2}, excluding interior gap; 49 at boundary p=4d+3, all tested C nonzero. Boundary t=2 exceptional class separately derived, not excluded universally by those finite checks.
Interior gap d=3..500, all primes 3d+5..4d+1: 17579 pairs. 12 zero Z slope (every multiple certified at v=2); 17546 with both nonzero first WQ jets at sole possible s (v=3); 21 unresolved at first jet, all W jet zero and Q jet nonzero. Fourth-jet quadratic: 9 no roots, 12 exactly two roots; 86 direct checks of C mod p^5 at h in {0,1,2} plus roots confirmed the classification. Thus 17567 of 17579 pairs have full fiber closure by these jets. The 12 pairs with remaining classes (d,p,s0,h roots):
(8,29,22,[4,26]), (27,89,33,[1,87]), (46,173,29,[25,41]), (77,293,180,[58,150]), (94,337,13,[95,151]), (101,317,48,[61,276]), (281,1093,693,[203,466]), (311,1049,362,[208,234]), (323,1021,416,[439,661]), (404,1429,1271,[424,505]), (445,1433,347,[110,1214]), (493,1597,1287,[1378,1480]). Boundary p=4d+3: 153 primes d=3..500, verified the unique possible exceptional class via C mod p^3 for each. None of those classes intersects the actual q<=2048 scan.

Actual budget exhaustive scan q=64..2048, d=3..floor(sqrt(4q)), 117996 pairs. Use largest prime of each integer as sufficient witness (not asserting all possible certificates tested); JF r=1..floor(d/10), p>20d+20; JH r=2 p>2d+1 with H(d), JO/JJ second r=3..d p>4d+6. Near second window r<=max(3,floor(d/10)) plus r2; far even window d-r<=max(3,floor(d/10)). No JA r1 test, so scoped comparison only. Results: first 42161; near second 107517; far second 88734; three-window union 115649; all second offsets 117985; union with JF unchanged 117985; new q-fiber 70033; union with new q-fiber 117994. New q-fiber alone rescued 9: (67,3),(69,3),(95,3),(101,4),(267,3),(1026,3),(1247,3),(2013,3),(2045,3). 1866769 nonzero second coordinate hits; 4337 zero hits; first zero hits 32. Remaining (100,5),(125,3): exact primal C negative, numerator/denominator bit lengths (140,107),(121,89); reduced numerators -829721988377420860355528917343731096043024 and -1629655384874924024893492469224330725. Hence finite exhaustive non-equality for this domain, using frozen sufficient certificates and two full rational evaluations. This is not an unbounded proof.

Replay code (same exact formulas as executed; combined in one script, explicit boundary correction):
```python
from fractions import Fraction as F
from math import comb,isqrt
from collections import Counter
from functools import lru_cache
from sympy import primerange,isprime
def rr(n,k):
    t=[F(1)];n=F(n)
    for i in range(k):t.append(t[-1]*(n-i)/(n+i+3))
    return t
def primal(q,d):
    u=q+d;m=2*q+d;U=rr(u,d);M=rr(m,d);V=Q=A=F(0)
    for k in range(d+1):
        l=d-k;a=(k+1)*(l+1)*U[k]*M[l];b=(k+1)*l*U[k]*M[l-1] if l else 0
        v=F((u-k)*(u+k+2),2*u*(2*u+1));V+=a;Q+=b;A+=v*(a+b)
    E=U[d]*F((u-d)*(2*d+3)*(m+2),2*(2*u+1)*(4*m+2));Z=q*A+Q+V
    return V,Q,A,E,Z,3*q*(4*q+3*d+1)**2*(A+E)*Q-32*(3*q+d+1)*Z**2
def coef(n,k):return comb(n,k)-2*comb(n,k-1)+comb(n,k-2)
def mod(x,p):return x.numerator*pow(x.denominator,-1,p)%p
def primalmod(q,d,p):
    u=q+d;m=2*q+d
    def R(n):
        t=[1]
        for i in range(d):t.append(t[-1]*(n-i)*pow(n+i+3,-1,p)%p)
        return t
    U=R(u);M=R(m);V=Q=A=0;iv=pow(2*u*(2*u+1),-1,p)
    for k in range(d+1):
        l=d-k;a=(k+1)*(l+1)*U[k]*M[l]%p;b=(k+1)*l*U[k]*M[l-1]%p if l else 0
        v=(u-k)*(u+k+2)*iv%p;V=(V+a)%p;Q=(Q+b)%p;A=(A+v*(a+b))%p
    E=U[d]*(u-d)*(2*d+3)*(m+2)*pow(2*(2*u+1)*(4*m+2),-1,p)%p
    return V,Q,A,(A+E)%p,(q*A+Q+V)%p
def cross(q,d,vals,m):
    V,Q,A,W,Z=vals
    return (3*q*(4*q+3*d+1)**2*W*Q-32*(3*q+d+1)*Z**2)%m
for d in range(3,101):
    V,Q,A,E,Z,C=primal(0,d);b=F((d+1)**2,comb(2*d+2,d)**2)
    assert (V,Q,A,Z)==tuple(b*coef(n,k) for n,k in [(4*d+2,d),(4*d+2,d+1),(4*d+1,d),(4*d+3,d+1)])
    assert Z==F(4*(d+1)**4*comb(4*d+3,d+1),comb(2*d+2,d)**2*(3*d+3)*(3*d+4))
stats=Counter();exceptions={};special={};checks=0
for d in range(3,501):
    for p in map(int,primerange(3*d+5,4*d+2)):
        m=p*p;a=primalmod(0,d,m);b=primalmod(p,d,m)
        assert all(a[i]%p==0 for i in [1,2,3,4]) and a[4]//p
        sl=[(y-x)//p%p for x,y in zip(a,b)]
        stats['gap']+=1
        if not sl[4]:stats['zero_slope']+=1;continue
        s=-(a[4]//p)*pow(sl[4],-1,p)%p;assert s
        W=(a[3]//p+s*sl[3])%p;Q=(a[1]//p+s*sl[1])%p
        if W and Q:stats['third']+=1;continue
        stats['first_unresolved']+=1
        m=p**3;q=p*s;a=primalmod(q,d,m);b=primalmod(q+p*p,d,m)
        z0=a[4]//(p*p);z1=(b[4]-a[4])//(p*p)%p;assert a[4]%(p*p)==0 and z1
        if not W and Q:l0=a[3]//(p*p)*Q;l1=(b[3]-a[3])//(p*p)*Q
        elif not Q and W:l0=a[1]//(p*p)*W;l1=(b[1]-a[1])//(p*p)*W
        else:l0=l1=0
        rt=[h for h in range(p) if (3*s*(3*d+1)**2*(l0+l1*h)-32*(d+1)*(z0+z1*h)**2)%p==0]
        assert len(rt)<=2;stats['roots_'+str(len(rt))]+=1
        exceptions[d,p]={p*s+p*p*h for h in rt}
        for h in set([0,1,2]+rt):
            q=p*s+p*p*h;m=p**5;c=cross(q,d,primalmod(q,d,m),m)
            assert c%(p**4)==0 and (c==0)==(h in rt);checks+=1
    p=4*d+3
    if isprime(p):
        V,Q,A,W,Z=primalmod(0,d,p*p);assert W%p and Q%p and Z%p==0 and Z//p
        s=32*(d+1)*(Z//p)**2*pow(3*(3*d+1)**2*W*Q,-1,p)%p;assert s
        special[d,p]=p*p*s
        assert cross(p*p*s,d,primalmod(p*p*s,d,p**3),p**3)==0
print(stats,checks,len(special))
@lru_cache(None)
def second(d,r):
    u=F(r-2,2);q=u-d;j=d-r;c=[(-1)**h*comb(2*j+h+1,h) for h in range(r+1)];U=rr(u,r);B=[(u+2)/(2*(2*u+1))]
    for k in range(r):B.append(B[-1]*(u-k-1)/(u+k+2))
    V=Q=A=F(0)
    for k in range(r+1):
        l=d-k;h=r-k;a=(k+1)*(l+1)*c[h];b=(k+1)*l*c[h-1] if h else 0
        V+=U[k]*a;Q+=U[k]*b;A+=B[k]*(a+b)
    Z=q*A+Q+V
    return 3*q*(4*q+3*d+1)**2*A*Q-32*(3*q+d+1)*Z**2
@lru_cache(None)
def first(d,r):
    j=d-r;q=-2*d+r-2;u=q+d;m=2*q+d;R=rr(m,r);V=Q=A=F(0)
    for h in range(r+1):
        k=j+h;l=r-h;c=(-1)**h*comb(2*j+h+1,h);a=(k+1)*(l+1)*c*R[l];b=(k+1)*l*c*R[l-1] if l else 0;v=F((u-k)*(u+k+2),2*u*(2*u+1));V+=a;Q+=b;A+=v*(a+b)
    E=(-1)**r*comb(2*j+r+1,r)*F((u-d)*((d+1)*(u+d+2)+(d+2)*(u-1-d))*(m+2),2*u*(2*u+1)*(4*m+2));Z=q*A+Q+V
    return 3*q*(4*q+3*d+1)**2*(A+E)*Q-32*(3*q+d+1)*Z**2
hi=2048;fs=[0]*(2*hi+4*isqrt(hi)+10)
for p in range(2,len(fs)):
    if not fs[p]:
        for k in range(p,len(fs),p):fs[k]=p
cnt=Counter();rescued=[];uncovered=[]
for q in range(64,hi+1):
    for d in range(3,isqrt(4*q)+1):
        cnt['pairs']+=1;p=fs[q]
        c0=p>2*d+2 and q%(p**3) not in exceptions.get((d,p),set()) and q%(p**3)!=special.get((d,p),-1)
        c1=c2=c3=full=False
        for r in range(1,d//10+1):
            p=fs[q+2*d-r+2]
            if p>20*d+20:
                if mod(first(d,r),p):c1=True
                else:cnt['first_zero']+=1
        H=64*d**6-61*d**5+13*d**4+61*d**3-29*d**2+16;p=fs[q+d]
        if p>2*d+1 and H%p:c2=full=True
        for r in range(3,d+1):
            p=fs[2*q+2*d-r+2]
            if p>4*d+6:
                if mod(second(d,r),p):
                    full=True
                    if r<=max(3,d//10):c2=True
                    if r%2==0 and d-r<=max(3,d//10):c3=True
                    cnt['second_nonzero_coordinates']+=1
                else:cnt['second_zero_coordinates']+=1
        for name,flag in [('q',c0),('first',c1),('near_second',c2),('far_second',c3),('full_second',full),('three_union',c1 or c2 or c3),('full_union',c1 or full),('new_union',c0 or c1 or full)]:cnt[name]+=bool(flag)
        if c0 and not(c1 or full):rescued.append((q,d))
        if not(c0 or c1 or full):uncovered.append((q,d))
print(cnt,rescued,uncovered)
for q,d in uncovered:
    C=primal(q,d)[-1];assert C;print(q,d,C.numerator,C.denominator)
```

Next: investigate the 12 residual gap-prime pairs via higher jets and overlap with other coordinates, and p-adic square-class of WQ at actual q. For smooth q without eligible prime use earlier joint windows; pursue pointwise deterministic shared-absence constraint. All-budget non-equality and real inverse-polynomial separation remain open.