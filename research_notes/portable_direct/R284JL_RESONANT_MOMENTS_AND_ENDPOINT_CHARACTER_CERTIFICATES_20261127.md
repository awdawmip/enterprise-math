# R284JL — Resonant joint moments and endpoint-character certificates
2026-11-27. Author derivation and exact replay, NOT_REVIEWED. Auxiliary binary-tag arithmetic observer; no native spatial/dynamic transfer claimed. Continue own RA-B82240E8488EF5A1DA5186C4, EM-DIRECT-0C386E, TASK_RESEARCH. Own session recovery r1-20261127-1400-recovery-own confirms the original open registration and no runs; current LEASED inventory request r1-20261127-1400-owner remained RUNNING at last check. No shared task/owner mutation. Frozen science: JK 6dc78691b5e767af4a5185f8b7798c0745c019f1:research_notes/portable_direct/R284JK_ODD_EDGE_TELESCOPING_AND_DISCRIMINANT_20261127.md (blob 6d9d7398afbad2e54190fa3eb933ebf7abb99e78), including its frozen JJ/JI dependencies. Current P000 V5, ACTIVE worldview, joint observer, residual and portable protocols consulted separately. Global canonical entries verified at 1a96733e514890ce6222a05f692659b2f280ed4f.

## 1. Resolve the resonant moment, retaining its harmonic coordinate
Let 3<=r<=d, j=d-r, w=(r-2)/2, t_0=1, t_(k+1)=t_k(k-w)/(k+w+3), P_h(k)=(k-w) rising h, and T=t_(r+1). The JK telescoping identity holds for every integer h>=0, not merely h<r:
 (k+w+3)t_(k+1)P_h(k+1)-(k+w+2)t_k P_h(k)=(h-r)t_k P_h(k).
For h!=r, summing k=0,...,r gives exactly
 S_h=[(r+w+3) T P_h(r+1)-(w+2)P_h(0)]/(h-r).
At resonance h=r, the left hand side is zero at every k. Therefore (k+w+2)t_k P_r(k)=(w+2)P_r(0) for every 0<=k<=r, even if an individual factor vanishes (no division by t_k or P_r is needed). In particular
 S_r=(w+2)P_r(0) H,
 H=sum_(k=0)^r 1/(k+w+2).
This removes the apparent division by zero; the harmonic sum is a genuine retained structural residual, not a limit prescription.

For any polynomial W(k)=sum_(h=0)^m a_h P_h(k), the exact full joint sum is
 sum t_k W(k)=L(W)+B(W)T+C(W)H,
 L=-(w+2) sum_(h!=r) a_h P_h(0)/(h-r),
 B=(r+w+3) sum_(h!=r) a_h P_h(r+1)/(h-r),
 C=(w+2)a_r P_r(0), with a_r=0 if m<r.
Use the JK Newton difference coefficients a_h=(-1)^h Delta^h W(w-i)|_(i=0)/h!. This holds for arbitrary m; the only exceptional eigenvalue is accounted for explicitly. For even r, w is a nonnegative integer and both P_r(0)=0 and T=0, hence both residuals vanish EXACTLY. For odd r, P_r(0) is nonzero. In the observer family below all prime factors of the displayed denominators are <p whenever p>4d+6, because m<=2j+4, |h-r|<=max(m,r), and twice the harmonic denominators are <=3r+2; the endpoint product denominator factors after clearing 2 are <=3r+4.

## 2. Full second-branch joint carrier, all offsets
Use the frozen JK definitions with b=2j+2, sgn=(-1)^r, and
 W_(n,a)(k)=(k+1)[binom(n-k+a-1,a-1)+binom(n-k+a-2,a-1)]
 (binomial understood polynomially). The three polynomials are sgn(j+1)W_(r,b+1), -sgn(j+1)W_(r-1,b+1), and sgn(j+1)W_(r,b)(w-k)(w+k+2)/(2w(2w+1)). Their joint sums are exactly V,Q,A; degrees <=b+1,b+1,b+2. The extra k=r term for Q is zero. Thus each is affine in (T,H), for the entire 3<=r<=d, and Z=q0 A+Q+V (q0=w-d) is also affine. The full residual
 G=3q0(4q0+3d+1)^2 A Q-32(3q0+d+1) Z^2
 is a bivariate polynomial of total degree <=2 in T,H. No coefficient or cross term has been discarded. When m<r this reduces to JK; for even r it reduces to an endpoint-free observer. For fixed j with r>2j+4, no H term enters; elsewhere this is an exact structural representation, not a promise of sublinear evaluation (Newton rows O((j+1)^2), endpoints may require O(r) operations). Scope is the displayed signed observers and their algebraic combinations, not arbitrary future observers.

## 3. Endpoint-character certificate (univariate JK regime)
For odd r=2s+3, JK gives T=(-1)^(s+1)(2s+1)!! ((2s+5)!!)^2/(6s+13)!!. At p>4d+6 all its factors are units. Write chi for the quadratic character of F_p, represented as +1 or -1 on units. Its square class can be obtained without the squared factors:
 epsilon=chi(T)=chi((-1)^(s+1) prod_(i=s+1)^(3s+6) (2i+1)).
The inverse has the same square character, which explains the positive product here. Adjacent odd offsets obey the exact recurrence
 T_(s+1)/T_s=-(2s+3)(2s+7)^2/[(6s+15)(6s+17)(6s+19)].
This follows by cancellation of consecutive odd double factorials. At a common eligible p one may propagate either the exact endpoint residue in O(1) field operations per offset, or its character via the ratio. It does not imply that the same p divides distinct primal pole coordinates for a fixed q,d.

Now take 2j+4<r, so H disappears from V,Q,A, and write f(X)=g2 X^2+g1 X+g0 from the exact JK carrier. If p divides N=2q+2d-r+2, p>4d+6, and q>=64, d^2<=4q, frozen JG/JI/JJ pole/edge reduction says equality qK=32/3 forces f(T)=0 mod p. Since T!=0 and T^((p-1)/2)=epsilon mod p, the following sufficient certificate is exact:
 gcd(f(X), X^((p-1)/2)-epsilon)=1 in F_p[X] => qK!=32/3.
Proof: any actual root T would be a common linear factor. Conversely gcd nonconstant iff f has some root in the known nonzero character class, since the second polynomial is split with simple roots (Euler criterion). For f=0 no certificate, and a nonzero constant always certifies. This includes every JK discriminant-nonresidue certificate and additionally can exclude roots having incompatible character, including zero roots. With epsilon given, compute X^((p-1)/2) modulo f by binary modular polynomial exponentiation (degree <=2), then a small Euclidean gcd: O(log p) field arithmetic, no root extraction or full endpoint evaluation needed. If epsilon must be computed from scratch, the class product costs O(r) field operations and is not a single-coordinate speedup over direct endpoint evaluation; the new method separates class acquisition from the root-exclusion test. More generally if m|p-1 and T^((p-1)/m) is known, the analogous gcd gives the m-th power class certificate.

Explicit strict-gain witness: d=r=5, p=37, q=89, N=185. The coefficients (g2,g1,g0) mod p are (9,1,0), roots 0 and 4, discriminant 1. T mod p=22 has character -1, while the only nonzero root has character +1. Thus JK discriminant test does not certify, but this character test does; actual residual mod p is 12. A linear-degenerate gain also occurs at d=r=5,p=31,q=74, coefficients (0,21,15), epsilon=+1, T=8, residual 28. Neither example claims equality was ever plausible over Q.

## 4. Exact execution and validation scope
Python Fraction and exact prime enumeration: all 465 pairs 3<=r<=d<=32 matched direct V,Q,A, including 165 odd and 155 even pairs satisfying 2j+4>=r (conservative possible-resonance threshold). Every odd pair of that subset had nonzero H coefficient in all three observers AND Z; the even subset had all H coefficients zero. This is a finite observation, not a universal nonvanishing theorem. Replayed the JK formal modular scope: 5<=d<=100, odd 5<=r<=d, j<=8, 2j+4<r, all primes 4d+6<p<1000. 44,652 formal pairs; old test 22,104; character gcd test 27,720; strict additions 5,616; actual residual zeros 105; every old certificate remained valid and every new certificate implied actual nonzero. The odd endpoint step recurrence was verified on each eligible (d,r). These are formal pairs, not a sample of distinct primal q; primal certification requires divisibility, as in the explicit witnesses. No density extrapolation, no independent review. Next: derive a cheap endpoint square-class source or use reciprocal classes across fixed-p sweeps; explore whether the resonant coefficients have a closed sign/height formula, and combine the filters across three windows. All-budget non-equality, cross-offset exceptional compatibility and real inverse-polynomial separation remain open.

## Replay
Run Python 3 with sympy. This is the executed algorithm, condensed from the local replay; all arithmetic is exact.
```python
from fractions import Fraction as F
from math import comb,factorial
from sympy import primerange
def rise(x,h):
    v=F(1)
    for i in range(h):v*=x+i
    return v
def bc(x,h):return rise(x-h+1,h)/factorial(h)
def W(n,a,k):return (k+1)*(bc(n-k+a-1,a-1)+bc(n-k+a-2,a-1))
def weights(d,r):
    j=d-r;w=F(r-2,2);b=2*j+2;s=(-1)**r
    return [(lambda k:s*(j+1)*W(r,b+1,k),b+1),
            (lambda k:-s*(j+1)*W(r-1,b+1,k),b+1),
            (lambda k:s*(j+1)*W(r,b,k)*(w-k)*(w+k+2)/(2*w*(2*w+1)),b+2)]
def split(w,r,P,m):
    row=[P(w-i) for i in range(m+1)]
    A=B=C=F(0);a=b=F(1)
    for h in range(m+1):
        c=(-1)**h*row[0]/factorial(h)
        if h==r:C=c*(w+2)*a
        else:
            A-=c*(w+2)*a/(h-r)
            B+=c*(r+w+3)*b/(h-r)
        row=[y-x for x,y in zip(row,row[1:])]
        a*=h-w;b*=r+1-w+h
    return A,B,C
def direct(d,r):
    u=F(r-2,2);j=d-r;U=F(1);B=(u+2)/(2*(2*u+1));V=Q=A=F(0)
    for k in range(r+1):
        h=r-k;l=d-k;c=(-1)**h*comb(2*j+h+1,h)
        a=(k+1)*(l+1)*c
        b=(k+1)*l*(-1)**(h-1)*comb(2*j+h,h-1) if h else 0
        V+=U*a;Q+=U*b;A+=B*(a+b)
        U*=(u-k)/(u+k+3);B*=(u-k-1)/(u+k+2)
    return V,Q,A
def G(d,r,V,Q,A):
    q=F(r-2,2)-d;Z=q*A+Q+V
    return 3*q*(4*q+3*d+1)**2*A*Q-32*(3*q+d+1)*Z**2
def endpoint(w,r):
    t=F(1)
    for k in range(r+1):t*=(k-w)/(k+w+3)
    return t
def harm(w,r):return sum((1/(w+2+k) for k in range(r+1)),F(0))
def mod(x,p):return x.numerator*pow(x.denominator,-1,p)%p
def char(x,p):return pow(x,(p-1)//2,p)
def cert(a,b,c,eps,p):
    def trim(f):
        while f and f[-1]==0:f.pop()
        return f
    def rem(f,g):
        f=trim([x%p for x in f]);g=trim([x%p for x in g]);assert g
        inv=pow(g[-1],-1,p)
        while len(f)>=len(g):
            z=f[-1]*inv%p;k=len(f)-len(g)
            for i,t in enumerate(g):f[i+k]=(f[i+k]-z*t)%p
            trim(f)
        return f
    def mul(f,g):
        if not f or not g:return []
        z=[0]*(len(f)+len(g)-1)
        for i,x in enumerate(f):
            for j,y in enumerate(g):z[i+j]=(z[i+j]+x*y)%p
        return rem(z,P)
    P=trim([c,b,a])
    if not P:return False
    if len(P)==1:return True
    n=(p-1)//2;v=[1];u=rem([0,1],P)
    while n:
        if n&1:v=mul(v,u)
        n//=2
        if n:u=mul(u,u)
    if not v:v=[0]
    v[0]=(v[0]-eps)%p;v=trim(v);f=P
    while v:f,v=v,rem(f,v)
    return len(f)==1
count=oddres=evres=0;nonzero=[0,0,0];znonzero=0
for d in range(3,33):
    for r in range(3,d+1):
        w=F(r-2,2);t=endpoint(w,r);H=harm(w,r)
        c=[split(w,r,P,m) for P,m in weights(d,r)]
        assert tuple(a+b*t+h*H for a,b,h in c)==direct(d,r)
        count+=1
        if 2*(d-r)+4>=r:
            if r%2:
                oddres+=1
                for i in range(3):nonzero[i]+=bool(c[i][2])
                znonzero+=bool(c[0][2]+c[1][2]+(w-d)*c[2][2])
            else:
                evres+=1;assert all(x[2]==0 for x in c)
print(count,oddres,evres,nonzero,znonzero)
total=old=new=additional=zeros=0;witness=None
for d in range(5,101):
    for r in range(5,d+1,2):
        j=d-r
        if j>8 or 2*j+4>=r:continue
        w=F(r-2,2);t=endpoint(w,r)
        tr=[split(w,r,P,m) for P,m in weights(d,r)]
        assert all(z==0 for a,b,z in tr)
        z,plus,minus=[G(d,r,*(a+b*v for a,b,_ in tr)) for v in (0,1,-1)]
        coeff=((plus+minus)/2-z,(plus-minus)/2,z)
        assert G(d,r,*direct(d,r))==coeff[0]*t*t+coeff[1]*t+coeff[2]
        s=(r-3)//2
        assert endpoint(w+1,r+2)==-t*(2*s+3)*(2*s+7)**2/((6*s+15)*(6*s+17)*(6*s+19))
        for p in primerange(4*d+7,1000):
            p=int(p);a,b,c=map(lambda x:mod(x,p),coeff);tm=mod(t,p)
            eps=char(tm,p);val=(a*tm*tm+b*tm+c)%p
            was=(a!=0 and char((b*b-4*a*c)%p,p)==p-1) or (a==b==0 and c!=0)
            now=cert(a,b,c,eps,p)
            assert not was or now
            assert not now or val!=0
            if now and not was and witness is None:witness=(d,r,p,a,b,c,eps,tm,val)
            total+=1;old+=was;new+=now;additional+=now and not was;zeros+=val==0
print(total,old,new,additional,zeros,witness)
# Expected observed: 465 165 155 [165,165,165] 165
# 44652 22104 27720 5616 105 (5,5,31,0,21,15,1,8,28)
```
