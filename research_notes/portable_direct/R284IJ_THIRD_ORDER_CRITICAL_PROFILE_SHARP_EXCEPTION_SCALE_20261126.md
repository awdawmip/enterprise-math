# R284IJ — Third-order critical profile and sharp exceptional rounding scale
2026-11-26. Author derivation, NOT_REVIEWED. Continuation of frozen R284II @c7be4488d3caa0ff3fa0a2febac189f084982516:research_notes/portable_direct/R284II_SECOND_ORDER_CRITICAL_PROFILE_20261126.md (pins IH/IC/HY/ID). Same auxiliary binary-tag safe-word total-count observer, no native physical attribution. P000 V5 and ACTIVE worldview retained; the account entry blobs match main@923742e04117a862af0b498a051b30a48c7680a8. Own session recovery returned original registration SUCCEEDED, no runs and no shared claim. Owner inventory r1-20261126-1000-owner-inventory SUCCEEDED, as_of 2026-11-26T02:01:51.930816Z, no LEASED entries in that snapshot, Source drift at completion; no protected task changes.

## Results
Put h=q^(-1/2), d=u-q, s=dh, x=kh, y=s-x, w=exp(-x²-y²/2). Uniformly on each compact positive s interval,
qK=32/3+h Phi(s)+h² Psi(s)+h³ Theta(s)+O(h⁴).
All Phi/Psi symbols and the original exact four joint counts V,Q,A,E are those of II. The new Theta is given below. For the critical level 32/(3q) put s0=unique Phi root, C0=-Psi(s0)/Phi'(s0), and
Z0=-(Theta(s0)+C0 Psi'(s0)+(C0²/2) Phi''(s0))/Phi'(s0).
The crossing is localized to d=s0 sqrt(q)+C0+Z0/sqrt(q)+O(q^-1), in the sense of strict bracketing outside an O(q^-1) band near the crossing. Minimality uses the ID author-level global monotonicity; no real-variable interpolation of discrete K is required.
Rigorous rational enclosures give 8.267<Z0<8.268 and 17<2Z0/s0<18. Thus the II two-term ceil formula has genuinely infinitely many failures, not just possible failures. Conditional on ID, if N(X) counts actual failures of d_min=ceil(s0 sqrt(q)+C0) at q<=X, then
17 s0 <= liminf N(X)/sqrt(X) <= limsup N(X)/sqrt(X) <= 18 s0.
In particular the O(sqrt(X)) exceptional scale in II is sharp. All sufficiently large actual failures underestimate d_min by one. Per large integer n there are 17 or 18 failing q close to ((n-C0)/s0)^2. No equidistribution or irrationality premise is used.

## Proof of the third profile
For c=1,2 set n=c/h²+s/h and j=z/h (here z is the scaled branch variable, not the integral coordinate below). From the exact II product, expand log R_n(j):
log R_n(j)=-z²/c+h(s z²/c²-2z/c)+h² B_c(z)+O(h³),
B_c(z)=-s² z²/c³+2sz/c²+3z²/(2c²)-z⁴/(6c³).
Indeed sum the linear, quadratic and cubic Taylor terms of log(1-i/n)-log(1+(i+3)/n): respectively -(j²+2j)/n, (3j²+6j)/(2n²), and -j⁴/(6n³)+O(h³); fourth and higher terms sum to O(h³) by j=O(h^-1), i/n=O(h). All estimates uniform including endpoints. Therefore R_u(k)R_m(l)=w(1+h a+h² U+O(h³)), U=B_1(x)+B_2(y)+a²/2, a from II.
Let f=xyw, f1=(s+xy a)w, f2=(1+s a+xy U)w.
The Euler-Maclaurin sum h sum over k=0..d equals integral + h/2 endpoint sum + h²/12 derivative difference + O(h³) for the smooth uniformly bounded profiles. Applied term by term, h³ V/H0=I+h J+h² V2+O(h³), where
V2=int f2 + 5s(exp(-s²/2)+exp(-s²))/12.
Here f vanishes at the endpoints, f1 has values s exp(-s²/2), s exp(-s²), and derivative difference of f equals minus their sum.

The exact signed branch (l+1)(t(l)-1) has expansion y²-1+h b+h² c2+O(h³), c2=-(y²+(s-y)b)/2, by dividing [2(y²-1)+h(2y-s)-h²] by [2+h(s-y)+h²]. Thus h²(Q-V)/H0=D+h D1+h² D2+O(h³), where
D2=int [(a+x U)(y²-1)+(1+x a)b+x c2]w
+ [(s²-1)exp(-s²/2)-(1+s a_s)exp(-s²)]/2
+ [(2s²-1)exp(-s²)-(s²-1)exp(-s²/2)]/12,
a_s=s³-2s.
The two last lines are the exact endpoint sum of the order-h profile and derivative difference of the leading profile x(y²-1)w; b(s,0)=0. All integrals from 0 to s. Put r3=(D2-r V2-R J)/I, so Q/V=1+hr+h²R+h³r3+O(h⁴).

Expand shared v(k)=1/4+h² v2+h³ v3+O(h⁴), v2=3/8-x²/4, v3=-3s/8+s x²/2-x/2. Its shared joint mass uses leading 2f and first correction 2f1+x(y²-1)w, with zero leading endpoints. Hence alpha=1/4+h² A2+h³ A3+O(h⁴), where
A3=(int f v3)/I + [int (2f1+x(y²-1)w)v2-A2(2J+D)]/(2I).
Keep E exactly as in II. Expanding rb=1+h(1/s-2s)+O(h²), gamma_m=1/4+O(h²), v(d)=1/4+O(h²), and R_u(d)=exp(-s²)(1+h a_s+O(h²)), gives E/H0=exp(-s²)/(8h) [s+h(3/2+s a_s-s²)+O(h²)]. Since A/H0=[2I+h(2J+D)+O(h²)]/(4h³), E/A=h² E2+h³ E3+O(h⁴), E3=exp(-s²)/(4I)[3/2+s a_s-s²-s(J+D/2)/I].
L/q=L0+h L1+h² L2+h³ L3+O(h⁴), L3=2s-s L2/3-L1/3 by exact division.
Set p2=R-r²/2-8A2, p3=r3-r R+r³/4-4A2 r-8A3.
Then Q/A=2+hr+h²p2+h³p3+O(h⁴). The factor (1+1/(q alpha))^-2=1-8h²+O(h⁴) has no cubic term. Multiply the exact factors as in II:
Theta=2L3+L2 r+L1(p2+2E2-16)+L0[p3+r(E2-8)+2E3].
I is bounded below on the compact positive interval. All uniform remainders above follow from smooth bounded polynomial profiles, uniformly bounded Taylor and Euler-Maclaurin errors, and denominator lower bounds. No term E is discarded.

## Inversion and sharp exception count
Write t=s0 sqrt(q)+C0, T=t+Z0/sqrt(q). For integer d with |d-T|=O(1), Taylor in s around s0 yields qK-32/3=h² Phi'(s0)(d-T)+O(h³ |d-T|+h³ |d-T|²+h⁴), using Phi'(s0)>0 and the definitions of C0,Z0. Thus strict signs follow on either side outside a band H/q, for some finite H, near the crossing; ID transfers signs to the whole valid domain. This also localizes the integer minimum (for > or >=; possible equality in the band). Because Z0>0, eventually the new band lies strictly to the right of t and within one unit of it. Failures of the II ceil formula can only occur when t<=n=ceil(t) and T>=n-O(1/q). Conversely t<=n and T>n+H/q forces failure by exactly one, with d=n+1 above target. At t exactly integer the same statement applies.
Let Q_n=((n-C0)/s0)^2. For bounded Q_n-q and n growing,
sqrt(q)(n-t)=s0 sqrt(q)(Q_n-q)/(sqrt(Q_n)+sqrt(q))=(s0/2)(Q_n-q)+o(1).
Necessity of bounded Q_n-q follows first from n-t<=Z0/sqrt(q)+H/q. Therefore for any fixed small epsilon>0 with 17< W-epsilon<W+epsilon<18, W=2Z0/s0, all q in [Q_n-W+epsilon,Q_n] fail eventually and every failure belongs to [Q_n-W-epsilon,Q_n]. Both intervals have length strictly between 17 and 18, hence contain at least 17 and at most 18 integers respectively. They are disjoint for successive large n, and the number of complete bands below X is s0 sqrt(X)+O(1). This proves the displayed sharp bounds. Finitely many initial q and the last incomplete band affect only O(1). The unknown distribution of fractional Q_n may determine a more precise constant. A third-order ceil rule itself has possible exceptions of smaller-width bands; no unconditional sub-sqrt count is asserted.

## Executed certificates
Python exact Fraction outward interval arithmetic, SymPy polynomial integration, Taylor orders 20/21 with signed remainder, 100-bit integer positive branch carrier. Coefficient derivatives evaluated after x=sz by the operator d/ds-2sg(z), g=z²+(1-z)²/2. Endpoint exponentials use the same exact Taylor bounds; all sign assertions exact. Output:
C (2.0640021544778726, 2.064002154987765)
Theta (-51.11379019679772,-51.11379012295251)
Phi' (33.83371582925074,33.833715834091166)
Phi'' (-36.10698282776693,-36.106982772168706)
Psi' (-73.4893704405427,-73.48937035489031)
Z (8.267072326323373,8.267072340644784)
W (17.079289671559206,17.07928970116405)
Five actual strict counterexamples to universal II rounding (q, II ceil, true bracket upper, qK at n minus target upper bound, qK at n+1 minus target lower bound):
10234,100,101,-0.0002517645275633401,0.0029035262411240144
264559,500,501,-1.988314691470075e-06,0.00012469384387154496
1062628,1000,1001,-2.4443554950945653e-07,3.144457440331195e-05
9590049,3000,3001,-9.027371397801825e-09,3.513394946741952e-06
106658837,10000,10001,-2.398199730024238e-10,3.1682388391394215e-07
These are full branch certificates, not float comparisons; decimal displays are rounded. Minimum interpretation conditional on ID. The proof of sharp order uses uniform expansion rather than extrapolation from five samples.

## Reproduction
The following exact certificate is the local executed algorithm. It uses no arbitrary float signs.

```python
from fractions import Fraction as F
from math import factorial
from functools import lru_cache
import sympy as sp
s,z=sp.symbols('s z'); g=z*z+(1-z)**2/2
class IV:
    def __init__(self,a,b=None):self.a=F(a);self.b=F(a if b is None else b)
    def __add__(self,o):o=cv(o);return IV(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return IV(-self.b,-self.a)
    def __sub__(self,o):return self+-cv(o)
    def __rsub__(self,o):return cv(o)+-self
    def __mul__(self,o):
        o=cv(o);v=[a*b for a in (self.a,self.b) for b in (o.a,o.b)];return IV(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,o):o=cv(o);assert o.a*o.b>0;return self*IV(1/o.b,1/o.a)
    def __rtruediv__(self,o):return cv(o)/self
    def __pow__(self,n):
        v=IV(1)
        for _ in range(n):v=v*self
        return v
    def show(self):return float(self.a),float(self.b)
def cv(o):return o if isinstance(o,IV) else IV(o)
@lru_cache(None)
def gp(k):
    if k==0:return (F(1),)
    a=gp(k-1);r=[F(0)]*(len(a)+2)
    for i,c in enumerate(a):
        for j,b in enumerate([F(1,2),F(-1),F(3,2)]):r[i+j]+=c*b
    return tuple(r)
@lru_cache(None)
def mom(j,k):return sum(c/F(i+j+1) for i,c in enumerate(gp(k)))
@lru_cache(None)
def expmom(j,a,N=20):
    v=sum((-a*a)**k*mom(j,k)/factorial(k) for k in range(N+1));return v+(-a*a)**(N+1)*mom(j,N+1)/factorial(N+1),v
@lru_cache(None)
def ep(a,N=20):
    v=sum((-a)**k/F(factorial(k)) for k in range(N+1));return v+(-a)**(N+1)/F(factorial(N+1)),v
S=IV(F(968081516889,10**12),F(968081516890,10**12))
def integ(p,S=S):
    return sum((F(c)*S**i*IV(expmom(j,S.b)[0],expmom(j,S.a)[1]) for (i,j),c in sp.Poly(p,s,z).terms()),IV(0))
Dop=lambda p:sp.diff(p,s)-2*s*g*p
class Jet:
    def __init__(self,a,b=0,c=0):self.a=cv(a);self.b=cv(b);self.c=cv(c)
    def __add__(self,o):o=jv(o);return Jet(self.a+o.a,self.b+o.b,self.c+o.c)
    __radd__=__add__
    def __neg__(self):return Jet(-self.a,-self.b,-self.c)
    def __sub__(self,o):return self+-jv(o)
    def __rsub__(self,o):return jv(o)+-self
    def __mul__(self,o):o=jv(o);return Jet(self.a*o.a,self.b*o.a+self.a*o.b,self.c*o.a+2*self.b*o.b+self.a*o.c)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=jv(o);a=self.a/o.a;b=(self.b-a*o.b)/o.a;c=(self.c-a*o.c-2*b*o.b)/o.a;return Jet(a,b,c)
    def __rtruediv__(self,o):return jv(o)/self
    def __pow__(self,n):
        r=Jet(1)
        for _ in range(n):r=r*self
        return r
def jv(o):return o if isinstance(o,Jet) else Jet(o)
def ij(p):return Jet(integ(p),integ(Dop(p)),integ(Dop(Dop(p))))
SJ=Jet(S,1,0)
def ej(c):
    e=IV(ep(c*S.b*S.b)[0],ep(c*S.a*S.a)[1]);return Jet(e,-2*c*S*e,(4*c*c*S*S-2*c)*e)
x=s*z;y=s*(1-z);a=s*x*x-2*x+s*y*y/4-y
log2=lambda c,z:-s*s*z*z/c**3+2*s*z/c**2+3*z*z/(2*c*c)-z**4/(6*c**3)
Aw=log2(sp.Integer(1),x)+log2(sp.Integer(2),y)+a*a/2
b=(2*y-s-(y*y-1)*(s-y))/2;c=-(y*y+(s-y)*b)/2
v2=sp.Rational(3,8)-x*x/4;v3=-3*s/8+s*x*x/2-x/2
pI=s*x*y;pJ=s*(s+x*y*a);pD=s*x*(y*y-1);pD1=s*((1+x*a)*(y*y-1)+x*b)
I,J,D,D1=[ij(p) for p in [pI,pJ,pD,pD1]];e0=ej(F(1,2));e1=ej(1);D1=D1-SJ*e1/2
r=D/I;R=(D1-r*J)/I;A2=ij(pI*v2)/I;E2=SJ*e1/(4*I)
L0=F(16,3);L1=56*SJ/9;L2=(25*SJ**2+24)/27
phi=2*L1+L0*r;psi=2*L2+L1*r+L0*(R-r*r/2-8*A2+2*E2-16)
for a0,sign in [(S.a,-1),(S.b,1)]:
    x0=IV(a0);v=F(112,9)*x0+F(16,3)*integ(pD,x0)/integ(pI,x0);assert v.b<0 if sign<0 else v.a>0
C=-psi.a/phi.b
I,J,D,D1,r,R,A2,E2,L1,L2=[j.a for j in [I,J,D,D1,r,R,A2,E2,L1,L2]]
e0,e1=e0.a,e1.a
V2=integ(s*(1+s*a+x*y*Aw))+5*S*(e0+e1)/12
as_=S**3-2*S
D2=integ(s*((a+x*Aw)*(y*y-1)+(1+x*a)*b+x*c))+((S*S-1)*e0-(1+S*as_)*e1)/2+((2*S*S-1)*e1-(S*S-1)*e0)/12
r3=(D2-r*V2-R*J)/I
A3=integ(pI*v3)/I+(integ((2*pJ+pD)*v2)-A2*(2*J+D))/(2*I)
E3=e1/(4*I)*(F(3,2)+S*as_-S*S-S*(J+D/2)/I)
L3=2*S-L2*S/3-L1/3
p2=R-r*r/2-8*A2;p3=r3-r*R+r**3/4-4*A2*r-8*A3
theta=2*L3+L2*r+L1*(p2+2*E2-16)+L0*(p3+r*(E2-8)+2*E3)
Z=-(theta+C*psi.b+C*C*phi.c/2)/phi.b
print('C',C.show(),'theta',theta.show(),'phi prime',phi.b.show(),'phi second',phi.c.show(),'psi prime',psi.b.show(),'Z',Z.show())
assert F(8267,1000)<Z.a<Z.b<F(8268,1000)
for n,q in [(100,10234),(500,264559),(1000,1062628),(3000,9590049),(10000,106658837)]:
    assert n-C.b>0 and n-1-C.b>0
    assert S.b*S.b*q<(n-C.b)**2 and S.a*S.a*q>(n-1-C.a)**2
    print('certified rounding n',n,'q',q)
B=1<<100
def mul(w,n,d):return w[0]*n//d,(w[1]*n+d-1)//d
def add(w,v):return w[0]+v[0],w[1]+v[1]
def prod(w,v):return w[0]*v[0]//B,(w[1]*v[1]+B-1)//B
def weights(n,d):
    w=[(B,B)]
    for i in range(d):w.append(mul(w[-1],n-i,n+i+3))
    return w
def Kq(q,d):
    u=q+d;mm=u+q;p,r=weights(u,d),weights(mm,d);V=Q=A=E=(0,0)
    for k in range(d+1):
        l=d-k;w=mul(prod(p[k],r[l]),(k+1)*(l+1),1);tn=l*(mm+l+2);td=(l+1)*(mm-l+1);vn=(u-k)*(u+k+2);vd=2*u*(2*u+1)
        V=add(V,w);Q=add(Q,mul(w,tn,td));A=add(A,mul(w,vn*(tn+td),vd*td))
        if l==0:E=mul(mul(mul(w,vn,vd),(d+1)*(u+d+2)+(d+2)*(u-1-d),(d+1)*(u+d+2)),mm+2,4*mm+2)
    T=add(add(Q,V),mul(A,q,1));ae=add(A,E);f=F(q*(3*u+q+1)**2,u+2*q+1)
    return f*F(ae[0]*Q[0],T[1]**2),f*F(ae[1]*Q[1],T[0]**2)
for n,q in [(100,10234),(500,264559),(1000,1062628),(3000,9590049),(10000,106658837)]:
    a,b=Kq(q,n);c,d=Kq(q,n+1);assert b<F(32,3)<c
    print("exact bracket",q,n,n+1,float(b-F(32,3)),float(c-F(32,3)))
assert 17<(2*Z/S).a<(2*Z/S).b<18
print("exception band width",(2*Z/S).show())
```

## Next
Obtain explicit uniform fourth-order remainder constant; study distribution of Q_n mod 1 and whether exact leading exceptional coefficient exists without unproved irrationality. Third-term ceil candidates require narrow-band certification. ID remains NOT_REVIEWED.
