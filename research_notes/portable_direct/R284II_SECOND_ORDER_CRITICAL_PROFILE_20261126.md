# R284II — Second-order critical profile, structural boundary shift and density-one rounding
2026-11-26. Author derivation, NOT_REVIEWED. Continuation of R284IH @c5d7de0bf5211be9149d31cb5c7343a0e0a16a7c:research_notes/portable_direct/R284IH_CRITICAL_SQRT_INVERSE_PROFILE_20261126.md, which pins IC/HY/IG/ID. Auxiliary binary-tag safe-word total-count observer only; no native physical attribution. Current account main entry blobs verified at 06eaa8c5eb8c3c292cc39fe66c49954bfb1932d7, current P000 V5 and worldview read. Historical same-lane RA-B82240E8488EF5A1DA5186C4 and own-session recovery returned registration SUCCEEDED; no shared claim or execution authority. Prior owner inventory SUCCEEDED (no LEASED); fresh request r1-20261126-0904-owner-inventory was RUNNING at last check. No protected task changes.

## Theorem
Put h=q^(-1/2), d=u-q, s=dh, x=kh, y=s-x, w=exp(-x^2-y^2/2). Uniformly for s in any compact subinterval of (0,infinity),
qK=32/3+h Phi(s)+h^2 Psi(s)+O(h^3),
with Phi from IH and the following explicit integrals (integral means 0 to s, dx):
a=s*x^2-2*x+s*y^2/4-y,
b=(2*y-s-(y^2-1)*(s-y))/2,
I=int xy w, J=int (s+xy a)w,
D=int x(y^2-1)w=-I',
D1=int ((xa+1)(y^2-1)+xb)w - s exp(-s^2)/2,
X=int x^3 y w.
r=D/I, R=D1/I-r J/I, A2=3/8-X/(4I), E2=s exp(-s^2)/(4I).
L0=16/3, L1=56s/9, L2=(25s^2+24)/27.
Psi=2L2+L1*r+L0*(R-r^2/2-8A2+2E2-16).
The E2 term is the genuine boundary branch, not a numerical error.

For target q c(q)=32/3+lambda*h+mu*h^2+O(h^3), let Phi(s_lambda)=lambda. Set C_lambda=(mu-Psi(s_lambda))/Phi'(s_lambda). There is a finite constant H (dependent on target remainder and lambda,mu) such that for sufficiently large q, all d below s_lambda sqrt(q)+C_lambda-H/sqrt(q) in the local window are below target near the crossing, and all above s_lambda sqrt(q)+C_lambda+H/sqrt(q) near the crossing are above target. Conditional on ID's author-level global monotonicity, the least d with K>c(q) (or >=) equals ceil(s_lambda sqrt(q)+C_lambda) whenever its distance to Z exceeds H/sqrt(q). This holds outside O(sqrt(X)) integer q<=X. For the critical level lambda=mu=0, exact rational enclosures give
0.968081516889 < s0 < 0.968081516890,
2.064002 < C0 < 2.064003.
Boundary E lowers this constant shift by 0.2990206488... (rigorous interval in [0.299020,0.299022]). Omitting E produces a different observer. No universal rounding at exceptional q is asserted.

## Proof
Use IH's exact joint count normalization H0=M_u(0)M_m(0), m=2q+d,
V/H0=sum (k+1)(l+1)R_u(k)R_m(l), l=d-k,
Q/V from t(l)=l(m+l+2)/((l+1)(m-l+1)),
A=sum P_k v(k)(1+t(l)), v(k)=(u-k)(u+k+2)/(2u(2u+1)),
E/H0=(d+1)R_u(d)v(d)(1+r_b) gamma_m,
r_b=(d+2)(u-1-d)/((d+1)(u+d+2)), gamma_m=(m+2)/(4m+2).
K=L(A+E)Q/(Q+V+qA)^2, L=(3u+q+1)^2/(u+2q+1).

The product R_n(k)=prod_{i<k}(n-i)/(n+i+3) has log=-(k^2+2k)/n+O(h^2) for n~q, k=O(1/h): the difference of quadratic terms is O(sum(i+1)/n^2), and cubic remainder O(sum(i+3)^3/n^3), both O(h^2). Expanding 1/u and 1/m gives R_u(k)R_m(l)=w(1+h a+O(h^2)) uniformly including endpoints. Thus h^3 V/H0=I+h J+O(h^2). Use the trapezoid Euler-Maclaurin estimate h sum f(kh)=int f+h(f(0)+f(s))/2+O(h^2) uniformly for smooth bounded derivatives on the compact triangular domain. The leading xyw vanishes at both endpoints, so J has no endpoint term.

The exact branch difference (l+1)(t(l)-1)=(2l(l+1)-m-1)/(m-l+1)=y^2-1+h b+O(h^2), uniformly. Consequently h^2(Q-V)/H0=D+h D1+O(h^2). Here the leading x(y^2-1)w has endpoint values 0 and -s exp(-s^2), giving the indispensable endpoint term of D1. Therefore Q/V=1+h r+h^2 R+O(h^3), by I bounded below. This directly pays the signed difference, not two independent approximation errors.

The exact v(k)=1/4+h^2(3/8-x^2/4)+O(h^3) uniformly. The shared measure P_k(1+t(l))/(Q+V) has leading density xyw/I; its bounded polynomial moments differ by O(h) from that density, since the V weights have O(h) Riemann error and sum P_k|t(l)-1|=O(H0 h^-2) by the exact branch difference. Hence alpha=A/(Q+V)=1/4+h^2 A2+O(h^3). The exact endpoint factors yield E/H0=s exp(-s^2)/(8h)+O(1); A/H0=I/(2h^3)+O(h^-2); hence E/A=h^2 E2+O(h^3). No endpoint removed. Expand
Q/A=2+h r+h^2(R-r^2/2-8A2)+O(h^3),
(1+(Q+V)/(qA))^-2=1-8h^2+O(h^4),
L/q=L0+h L1+h^2 L2+O(h^3).
Multiplication in qK=(L/q)(1+E/A)(Q/A)(1+(Q+V)/(qA))^-2 proves the profile.

For inversion, write t_q=s_lambda sqrt(q)+C_lambda. For integer d=t_q+epsilon, |epsilon|<=2, smoothness and Taylor give qK-qc(q)=h^2 Phi'(s_lambda)*epsilon+O(h^3) uniformly. IH provides Phi'>=112/9. Choose H larger than the uniform error constant divided by Phi'. If dist(t_q,Z)>Hh, floor and ceil bracket strictly; ID supplies minimality. Near exceptional q use slightly wider integer bracketing. For density-one rounding no irrationality premise is needed: if |s_lambda sqrt(q)+C_lambda-n|<=H/sqrt(q), then |q-((n-C_lambda)/s_lambda)^2|<=2H/s_lambda+H^2/(s_lambda^2 q). Each n permits O(1) integer q; n ranges over O(sqrt(X)) integers for q<=X. Therefore at most O(sqrt(X)) possible exceptional q. This is a bound, not a proof that every exceptional q fails.

## Executed exact certificates
Local Python/SymPy/Fraction, no floating-point signs. Taylor lower/upper orders 19/18 on [0,1]; integrate exact monomial moments of z^j g(z)^k, g=z^2+(1-z)^2/2. Monomial weights are nonnegative, so at a root interval [a,b] the moments are bounded below by lower Taylor at b and above by upper Taylor at a. Evaluate polynomial coefficients with interval arithmetic. Phi' via g moments: 112/9+16/s^2+(32/3)(E[g]-2s^2 Var[g]).
Actual enclosures (decimal displays only):
s in (0.968081516889,0.968081516890)
Psi in [-69.83286238286676,-69.83286237550669]
Phi' in [33.83371583023604,33.83371583310587]
shift in [2.0640021545365146,2.064002154929123]
boundary shift contribution in [0.2990206488119597,0.29902064884368].
80-bit positive integer interval recurrence from IH, evaluated all joint branches and E at eight square budgets; exact comparisons bracket 32/3.
q,d_lo,d_hi, upper_lo_gap,lower_hi_gap:
10000,98,99,-0.0031066888988601007,0.00014813857518938258
40000,195,196,-0.0005982645361201683,0.00023033507421498634
250000,486,487,-1.627206377483222e-05,0.00011778086827483596
1000000,970,971,-5.1807204333848665e-06,2.8493188921976675e-05
4000000,1938,1939,-1.9511699287802353e-06,6.487585656595669e-06
25000000,4842,4843,-6.399307319536034e-07,7.122269230623813e-07
100000000,9682,9683,-2.976196774653454e-07,4.058322125644428e-08
400000000,19363,19364,-5.8753449024338166e-08,2.5813220452824484e-08
All 8 brackets agree with ceil of the two-term threshold. Finite calculations are not used to infer the uniform asymptotic.

## Reproduction
Python 3 with SymPy; exact signs, no overflow. Full branch recurrence follows IH unchanged.
```python
from fractions import Fraction as F
from functools import lru_cache
from math import factorial
import sympy as sp
s,z=sp.symbols('s z'); g=z*z+(1-z)**2/2
@lru_cache(None)
def mom(j,k):
    p=sp.Poly(g**k,z)
    return sum(F(c)/F(i[0]+j+1) for i,c in p.terms())
@lru_cache(None)
def expmom(j,a,N=18):
    v=sum((-a*a)**k*mom(j,k)/factorial(k) for k in range(N+1))
    return v+(-a*a)**(N+1)*mom(j,N+1)/factorial(N+1),v
class IV:
    def __init__(self,a,b=None):self.a=F(a);self.b=F(a if b is None else b)
    def __add__(self,o):
        o=cv(o);return IV(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return IV(-self.b,-self.a)
    def __sub__(self,o):return self+-cv(o)
    def __rsub__(self,o):return cv(o)+-self
    def __mul__(self,o):
        o=cv(o);v=[a*b for a in [self.a,self.b] for b in [o.a,o.b]];return IV(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=cv(o);assert o.a*o.b>0;return self*IV(1/o.b,1/o.a)
    def __rtruediv__(self,o):return cv(o)/self
    def __pow__(self,n):
        v=IV(1)
        for _ in range(n):v=v*self
        return v
    def show(self):return (float(self.a),float(self.b))
def cv(o):return o if isinstance(o,IV) else IV(o)
def integ(p,S):
    return sum((F(c)*S**i*IV(expmom(j,S.b)[0],expmom(j,S.a)[1]) for (i,j),c in sp.Poly(p,s,z).terms()),IV(0))
x=s*z;y=s*(1-z); a=s*x*x-2*x+s*y*y/4-y;b=(2*y-s-(y*y-1)*(s-y))/2
pI=s*x*y;pJ=s*(s+x*y*a);pD=s*x*(y*y-1);pD1=s*((x*a+1)*(y*y-1)+x*b);pX=s*x**3*y
@lru_cache(None)
def ep(a,N=18):
    v=sum((-a*a)**k/F(factorial(k)) for k in range(N+1));return v+(-a*a)**(N+1)/F(factorial(N+1)),v
def phi(S):return F(112,9)*S+F(16,3)*integ(pD,S)/integ(pI,S)
S=IV(F(968081516889,10**12),F(968081516890,10**12))
assert phi(IV(S.a)).b<0<phi(IV(S.b)).a
I,J,D,D1,X=[integ(p,S) for p in [pI,pJ,pD,pD1,pX]]; e=IV(ep(S.b)[0],ep(S.a)[1]);D1=D1-S*e/2
r=D/I;r2=D1/I-r*J/I; a2=F(3,8)-X/(4*I);e2=S*e/(4*I)
L0=F(16,3);L1=F(56,9)*S;L2=(25*S**2+24)/27
psi=2*L2+L1*r+L0*(r2-r*r/2-8*a2+2*e2-16)
G=integ(pI*g,S)/I;G2=integ(pI*g*g,S)/I
slope=F(112,9)+16/S**2+F(32,3)*(G-2*S**2*(G2-G*G));shift=-psi/slope
assert F(2064002,10**6)<shift.a<shift.b<F(2064003,10**6)
assert F(299020,10**6)<(2*L0*e2/slope).a<(2*L0*e2/slope).b<F(299022,10**6)
print('s interval',S.show(),'psi',psi.show(),'slope',slope.show(),'shift',shift.show(),'boundary shift contribution',(2*L0*e2/slope).show())
B=1<<80
def mul(w,n,d):return w[0]*n//d,(w[1]*n+d-1)//d
def add(w,v):return w[0]+v[0],w[1]+v[1]
def prod(w,v):return w[0]*v[0]//B,(w[1]*v[1]+B-1)//B
def weights(n,d):
    w=[(B,B)]
    for i in range(d):w.append(mul(w[-1],n-i,n+i+3))
    return w
def Kq(q,d):
    u=q+d;m=u+q;p,r=weights(u,d),weights(m,d);V=Q=A=E=(0,0)
    for k in range(d+1):
        l=d-k;w=mul(prod(p[k],r[l]),(k+1)*(l+1),1);tn=l*(m+l+2);td=(l+1)*(m-l+1);vn=(u-k)*(u+k+2);vd=2*u*(2*u+1)
        V=add(V,w);Q=add(Q,mul(w,tn,td));A=add(A,mul(w,vn*(tn+td),vd*td))
        if l==0:E=mul(mul(mul(w,vn,vd),(d+1)*(u+d+2)+(d+2)*(u-1-d),(d+1)*(u+d+2)),m+2,4*m+2)
    T=add(add(Q,V),mul(A,q,1));ae=add(A,E);f=F(q*(3*u+q+1)**2,u+2*q+1)
    return IV(f*F(ae[0]*Q[0],T[1]**2),f*F(ae[1]*Q[1],T[0]**2))
for n in [100,200,500,1000,2000,5000,10000,20000]:
    q=n*n;pred=n*S+shift;assert pred.a//1==pred.b//1;d=int(pred.a//1);l=Kq(q,d);r=Kq(q,d+1);assert l.b<F(32,3)<r.a
    print('q',q,'bracket',d,d+1,'gaps',float(l.b-F(32,3)),float(r.a-F(32,3)))
```

## Next
Compute third-order profile and explicit compact-window remainder constants, then resolve near-integer exceptions by the original exact interval carrier. Explore whether an explicit density-one certificate can be made practical. ID remains NOT_REVIEWED. IH Activity association remains pending until own record binding/authorized CAS; do not mistake prior published proof for a formal result.
