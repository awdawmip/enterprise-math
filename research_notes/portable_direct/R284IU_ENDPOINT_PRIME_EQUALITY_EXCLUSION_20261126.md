# R284IU — Exact shifted fibers, reduced rational height and endpoint-prime equality exclusion
2026-11-26. Author analytic proof and executed exact rational tests; NOT_REVIEWED. Directed continuation of R284, prior own Activity RA-B82240E8488EF5A1DA5186C4 / EM-DIRECT-0C386E; original own session recovery returned registered SUCCEEDED and no shared run. Owner inventory request r1-20261126-2102-owner-inventory last observed RUNNING before this note; no shared Task claimed or mutated. Account canonical entry blobs verified at cf033cb4fd91baec4d762954d93e227dc8a73143. P000 V5, ACTIVE worldview, joint observer and heartbeat companion consulted. This is the existing auxiliary binary-tag joint-count observer, not native spatial or physical attribution.
Frozen science: IT@ce891978ba5d3ceca0fc041948524a50effe9e81 (gap law and height), IS@d235b53a819dc0fd6b4aa3ca3e349de911f5d96a (original formula and exact oracle). Critical-line asymptotic T(q) follows the frozen IJ/IO inputs of IT; no new constant certification. No shared theorem promotion.

## 1. Exact shift of the Q fiber; retain endpoint residual
For q>=64, integer 0<=d<=2sqrt(q), put u=q+d,m=u+q,l=d-k, R_n(j)=product_{i=0}^{j-1}(n-i)/(n+i+3). Define
w0(k)=(k+1)(l+1)R_u(k)R_m(l),
w1(k)=(k+1)l R_u(k)R_m(l-1) if l>=1, else 0,
v(k)=(u-k)(u+k+2)/(2u(2u+1)).
Then V=sum w0, Q=sum w1, A=sum v(k)(w0+w1). This is exact: R_m(l)/R_m(l-1)=(m-l+1)/(m+l+2), cancelling the entire extra rational multiplier l(m+l+2)/((l+1)(m-l+1)) of the original Q. The endpoint is exactly
E=R_u(d)(u-d)[(d+1)(u+d+2)+(d+2)(u-1-d)](m+2)/[2u(2u+1)(4m+2)].
The original indicator remains
qK=q(3u+q+1)^2(A+E)Q/[(u+2q+1)(qA+Q+V)^2].
No branch mass or endpoint is dropped. In particular Q is the V convolution at degree d-1 with u,m held fixed, not the indicator at a different budget. Shifted fibers permit future exact or polynomial approximations without the additional geometric denominator used in IS; an optimized implementation is not claimed here.

## 2. Smaller common rational denominator
Let D*=2u(2u+1)(4m+2) product_{i=0}^{d-1}(u+i+3)(m+i+3).
All four D*V,D*Q,D*A,D*E are integers by the exact shift and endpoint expression. Every factor <=10q, since d<=q/4 and q>=64; in particular 4m+2=8q+4d+2 can exceed 8q, so use this safe base rather than IT's all-factor <=8q claim. Thus D*<=(10q)^(2d+3). IS bounds V<=Z,Q<=4Z,A<=5Z, Z=(d+1)(d+2)(d+3)/6 <=(10q)^3, imply qA+Q+V<=5(q+1)Z. Thus writing c=D*A,b=D*Q,v0=D*V, the positive integer denominator (u+2q+1)(qc+b+v0)^2 <=(10q)^(4d+15). Subtracting 32/3 yields
F=qK-32/3=0 or |F|>=(10q)^(-4d-16).
Compared with IT's 6d+22 exponent this removes a linear d-dependent denominator group; use base 10q for the analytic proof. The executed finite checks below additionally tested the stronger 8q bound for the actual cases, not claimed unconditionally here. IT's stated all-factor <=8q justification requires this base correction independently of the new cancellation. Terminating precision cap (4d+16)ceil(log2(10q))+O(1) is still O(d log q), not a polynomial-log worst-case proof.

## 3. Endpoint prime obstruction (unbounded)
For d>=1 set N=u+d+2=q+2d+2. Suppose a prime p divides N and p>12d+14, and t=v_p(N)>=1. Then
v_p(V)=-t, v_p(Q)>=0, v_p(A)>=0, v_p(E)>=-t,
and v_p(qK)>=t, v_p(F)=0.
Proof: express all factors as integer multiples of N plus small shifts. u=N-d-2,m=2N-3d-4,q=N-2d-2. In R_u(k) the denominator factors u+i+3=N+i-d+1 are units for i<d-1, and exactly N for i=d-1. Numerators u-i=N-d-2-i are units. All m denominator factors m+i+3=2N-3d+i-1 are units, and m numerator factors also units. The factors 2u,2u+1,4m+2=8N-12d-14,u+2q+1=3N-5d-5 are units, as are q, d+1. Hence the only pole in V occurs in the k=d summand, exactly -t; all other summands integral, so no cancellation of its leading pole is possible. Q has no k=d summand. A at k=d cancels that pole through u+d+2=N in v(d), and all other terms integral. The exact E expression leaves at most the same order pole -t. Consequently qA+Q+V has valuation -t. Substitution gives v_p(qK)>=-t+0+2t=t (q and u+2q+1 units, remaining outer numerator integral). Since p>3, 32/3 is a p-adic unit, hence v_p(F)=0, excluding equality. No implication about the real magnitude of F is made. A supplied large-prime divisor is enough; finding such a divisor for arbitrary input is not asserted efficient.

In particular there are infinitely many near-critical pairs obeying this obstruction. For any sufficiently large prime p, let d be a nearest integer to s0 sqrt(p)+C0-s0^2 and q=p-2d-2. Then q~p,d~s0 sqrt(q), p>12d+14, d^2<=4q and q>=64. Expanding sqrt(p-2d-2)=sqrt(p)-s0+O(p^-1/2) gives T(q)=s0 sqrt(p)+C0-s0^2+O(p^-1/2). Thus |d-T(q)|<=1/2+O(p^-1/2)<1 eventually. Infinitely many distinct q follow from unbounded primes and q~p. These are genuine local candidates of IT; this does not assert that every nearest candidate or every budget is covered, nor that equality is ruled out globally.

## 4. Executed checks
Python Fraction/integer computation over every q=64..399 and d=0..floor(sqrt(4q)): 10,142 joint identity, denominator and height checks; 1,780 qualifying (q,d,p) valuation checks, five with v_p(qK)>v_p(N), maximum valuation 2. The finite 8q height bound also passed every case. Five large prime-endpoint pairs (p,q,d,v_p(qK)): (1009,943,32,1),(5003,4861,70,1),(10007,9809,98,1),(20011,19733,138,1),(29989,29649,169,1). Additional p^2 cases (p,d)=(101,2),(127,5),(211,10), q=p^2-2d-2: all v_p(qK)>=2. No earlier IS benchmark was repeated; all new comparisons exact. Approximate constants only select the five candidate pairs; exact p-adic checks independent of them.

Reproduction (standard library, equivalent finite loop; includes original and shifted observers):
```python
from fractions import Fraction as F
from math import isqrt,prod

def vals(q,d):
    u=q+d;m=u+q
    def w(n):
        a=[F(1)]
        for i in range(d): a.append(a[-1]*F(n-i,n+i+3))
        return a
    P,R=w(u),w(m)
    V=Q=A=E=Q2=A2=F(0)
    for k in range(d+1):
        l=d-k; v=F((u-k)*(u+k+2),2*u*(2*u+1))
        w0=(k+1)*(l+1)*P[k]*R[l]
        t=F(l*(m+l+2),(l+1)*(m-l+1))
        V+=w0;Q+=w0*t;A+=w0*v*(1+t)
        w1=(k+1)*l*P[k]*R[l-1] if l else 0
        Q2+=w1;A2+=(w0+w1)*v
        if not l:E=w0*v*(1+F((d+2)*(u-1-d),(d+1)*(u+d+2)))*F(m+2,4*m+2)
    E2=P[d]*F((u-d)*((d+1)*(u+d+2)+(d+2)*(u-1-d))*(m+2),2*u*(2*u+1)*(4*m+2))
    assert (Q,A,E)==(Q2,A2,E2)
    D=prod((u+i+3)*(m+i+3) for i in range(d))*2*u*(2*u+1)*(4*m+2)
    v,b,c,e=[D*x for x in (V,Q,A,E)]
    assert all(x.denominator==1 for x in (v,b,c,e))
    den=(u+2*q+1)*(q*c+b+v)**2
    assert den<=(8*q)**(4*d+15)
    K=F(q*(3*u+q+1)**2)*(c+e)*b/den
    assert K==F(q*(3*u+q+1)**2,u+2*q+1)*(A+E)*Q/(q*A+Q+V)**2
    if K!=F(32,3):assert abs(K-F(32,3))>=F(1,(8*q)**(4*d+16))
    return V,Q,A,E,K

def vp(x,p):
    if not x:return float('inf')
    def v(a):
        a=abs(a);i=0
        while a%p==0:a//=p;i+=1
        return i
    x=F(x);return v(x.numerator)-v(x.denominator)

def prime(p):return p>=2 and all(p%i for i in range(2,isqrt(p)+1))
N=checks=higher=maxv=0
for q in range(64,400):
    for d in range(isqrt(4*q)+1):
        V,Q,A,E,K=vals(q,d);N+=1
        if not d:continue
        n=q+2*d+2
        for p in range(12*d+15,n+1):
            if n%p or not prime(p):continue
            t=vp(n,p)
            assert vp(V,p)==-t and vp(Q,p)>=0 and vp(A,p)>=0 and vp(E,p)>=-t
            assert vp(K,p)>=t and vp(K-F(32,3),p)==0
            checks+=1;higher+=vp(K,p)>t;maxv=max(maxv,vp(K,p))
print(N,checks,higher,maxv)
for p,q,d in [(1009,943,32),(5003,4861,70),(10007,9809,98),(20011,19733,138),(29989,29649,169)]:
    assert prime(p) and p==q+2*d+2 and p>12*d+14 and d*d<=4*q
    K=vals(q,d)[-1];assert vp(K,p)>=1 and vp(K-F(32,3),p)==0
for p,d in [(101,2),(127,5),(211,10)]:
    K=vals(p*p-2*d-2,d)[-1]
    assert vp(K,p)>=2 and vp(K-F(32,3),p)==0
```

## Next
Use shifted Q in the actual IS polynomial oracle, removing its geometric denominator approximation; benchmark full adaptive three-state search. Investigate other pole locations with multiple fibers and CRT, and whether enough large-prime obstructions exist at actual minimum candidates. Neither real inverse-polynomial separation nor global equality exclusion follows from this theorem. Preserve full V,Q,A,E and author/unreviewed status.
