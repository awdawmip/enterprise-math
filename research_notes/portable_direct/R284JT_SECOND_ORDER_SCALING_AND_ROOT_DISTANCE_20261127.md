# R284JT — Second-order joint scaling and local real-root distance

2026-11-27. Author proof and exact rational interval checks; NOT_REVIEWED. Ordinary auxiliary analysis of the exact arithmetic observer, not a native spatial or physical attribution. Own session metadata recovered (EM-DIRECT-0C386E / TASK_RESEARCH, no formal run/claim). No shared Task mutation. Owner query r1-20261127-2203-leased queued at last read. Global entries verified at main@8381e6bda551267805e9e83999632ac5aaed9318. P000 V4/V5, joint/residual and portable contracts consulted.

Frozen scientific source: b081101b186a92ca04358892d678eb64b9d8f786:research_notes/portable_direct/R284JS_UNIFORM_SCALING_ROOT_AND_EVENTUAL_UNIQUENESS_20261127.md; its JR input and full endpoint E unchanged.

## Result

For all sufficiently large integer d the legal real root from JS obeys
q_d = alpha_* d^2 + beta_* d + O(1),
with 1.06702880 < alpha_* < 1.06702881 (JS) and
-4.40471 < beta_* < -4.40468 (exact rational enclosure below).
Moreover near the root, for any fixed B>0, uniformly for |q-q_d|<=B,
C(q,d)/(q^3 d^3) = -(lambda_*+O(1/d))(q-q_d),
where 0.4057998 < lambda_* < 0.4058004.
These are qualitative asymptotics with no explicit d_0 or remainder constant; no integer exclusion for unbounded d follows.

## Exact observer and expansion

Retain all definitions of JS: q=d^2/s, 0<s<=4, h=1/d, x=k/d, y=1-x, u=q+d, m=2q+d, l=d-k.
R_n(k)=prod_{i<k}(n-i)/(n+i+3).
a_k=(k+1)(l+1)R_u(k)R_m(l), b_k=(k+1)l R_u(k)R_m(l-1), with b_k=0 for l=0.
V=sum a_k, Q=sum b_k, A=sum (u-k)(u+k+2)/(2u(2u+1)) (a_k+b_k).
E=R_u(d)(u-d)(2d+3)(m+2)/(2(2u+1)(4m+2)); W=A+E; Z=qA+Q+V.
C=3q(4q+3d+1)^2 WQ-32(3q+d+1)Z^2.

Write phi=x^2+y^2/2, e=exp(-s phi), rho=-2sx-sy+s^2(x^2+y^2/4).
Uniformly in C^1([0,4]) and in k, R_u(k)R_m(l)=e(1+h rho)+O_C1(h^2).
Proof: for n=lambda q+d and c=s/lambda, i/d=t, log of a factor is
-2ct h+(-3c+2c^2 t)h^2+O_C1(h^3).
Indeed numerator and denominator are 1+c(1-t)h and 1+c(1+t)h+3ch^2 after dividing by lambda q. Uniform Taylor remainder (and s derivative) follows on a compact neighborhood of 1 for sufficiently small h. Summing, using sum t = k(k-1)/(2d), gives -c x^2+h(-2cx+c^2 x^2)+O_C1(h^2). Apply to both factors with lambda=1,2; exponentiate. At s=0 use the continuous rational extension.

Define all integrals over x in [0,1]:
I=int xy e, J=int x(1-s y^2)e,
v=int (1+xy rho)e,
j=int [(1-s y^2)(1+x rho)-x(s y/2-s^2 x y^2/2)]e + exp(-s)/2,
a=(2v-J)/4,
b=int xy(3s/4-s^2 x^2/2)e,
e0=exp(-s)/8.
The joint expansions are
V/d^3=I+h v+O_C1(h^2);
(V-Q)/d^2=J+h j+O_C1(h^2);
Q/d^3=I+h(v-J)+O_C1(h^2);
A/d^3=I/2+h a+O_C1(h^2);
[A-(V+Q)/4]/d=b+O_C1(h);
E/d=e0+O_C1(h);
[(V+Q)/q]/d=2s I+O_C1(h).

For V use (x+h)(y+h)=xy+h+O(h^2) and the composite trapezoid rule: h sum_{k=0}^d f(kh)=int f+h(f(0)+f(1))/2+O(h^2), with the same remainder for s derivatives because the coefficient functions have bounded second x derivatives. The leading V endpoints vanish.
For the exact joint difference use JS identity a_k-b_k=(k+1)R_u(k)R_m(l)[1-l(2l+1)/(m-l+1)]. Expand the ratio as s y^2+h(s y/2-s^2 x y^2/2)+O_C1(h^2). The leading difference endpoint at x=1 equals exp(-s), yielding the explicit half-endpoint in j.
For A use exact weight minus 1/4 = [3u/2-k(k+2)]/[2u(2u+1)] = h^2(3s/8-s^2 x^2/4)+O_C1(h^3). The endpoint E prefactors give e0. Thus neither the joint difference nor endpoint E is discarded.

## Second normalized coefficient

Let L=28s I^2-12 I J as in JS. Direct expansion gives
C/(q^3 d^5)=L+h M+O_C1(h^2)
where
M=-12 I j-24 a J-48 I b+36s I(v-J)+40s I a
  +(27s^2/2-188s)I^2+6 exp(-s) I.

Proof: in C/q^3 the prefactors of WQ and (A+(V+Q)/q)^2 are
48+72s h+(24s+27s^2)h^2+O_C1(h^3)
and 96+32s h+32s h^2, respectively. Retain 48A(Q-2A) exactly until expansion: Q-2A=-(V-Q)/2-2[A-(V+Q)/4]. Its order d^4 coefficient is -12 I j-24 a J-48 I b. First-order prefactors give 36s I(v-J)+40s I a at order d^4. Second-order prefactors give (4s+27s^2/2)I^2. Endpoint E contributes 48 e0 I=6 exp(-s)I. The cross term with (V+Q)/q contributes -192s I^2. All remaining terms are O_C1(d^3) before division by d^5. This argument uses the cancellation-preserving expression, so no unknown second-order marginal coefficient of A or Q is needed.

Let s_*=1/alpha_* be the simple root of L from JS, L'(s_*)>0. JS gives s_d-s_*=O(h). Taylor expansion of L and M at s_* (smooth integral functions) gives
s_d=s_*-h M(s_*)/L'(s_*)+O(h^2).
Invert on a compact positive neighborhood:
beta_*=M(s_*)/(s_*^2 L'(s_*)).
For |q-q_d|<=B use the mean value theorem in s on the normalized C: its derivative equals L'(s_*)+O(h) uniformly there. Exactly s-s_d=-d^2(q-q_d)/(qq_d). Multiply by d^2 and use q/d^2=alpha_*+O(h), q_d/d^2=alpha_*+O(h). This proves the claimed distance formula with lambda_*=s_*^2 L'(s_*), including q=q_d by equality. In particular the nearest-integer normalized gap is asymptotically proportional to dist(q_d,Z), but no positive lower bound for that distance has been shown. A bounded root remainder is not a certificate of separation.

## Exact interval verification

The following Python was executed with exact Fraction interval arithmetic. The degree-18 Taylor remainder of exp(-s phi) has absolute value <=1/19! for 0<=s<=1, phi in [1/3,1]. Integrating a possibly signed interval polynomial weight costs at most its coefficient absolute-sum times this remainder. The prior certified alpha interval supplies the s interval. The displayed decimal bounds below are weaker outward rational enclosures; the assertions are exact. No float is used for certification.

```python
from fractions import Fraction as F
from math import factorial
class R:
    def __init__(self,a,b=None): self.a=F(a);self.b=F(a if b is None else b)
    def __add__(self,o):
        o=rr(o);return R(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return R(-self.b,-self.a)
    def __sub__(self,o):return self+-rr(o)
    def __rsub__(self,o):return rr(o)+-self
    def __mul__(self,o):
        o=rr(o);v=[self.a*o.a,self.a*o.b,self.b*o.a,self.b*o.b];return R(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=rr(o);assert o.a*o.b>0;return self*R(1/o.b,1/o.a)
    def __repr__(self):return str((float(self.a),float(self.b)))
def rr(o):return o if isinstance(o,R) else R(o)
def add(a,b):return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]
def scale(a,b):return [v*b for v in a]
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):c[i+j]+=u*v
    return c
phi=[F(1,2),-1,F(3,2)]; x=[0,1]; y=[1,-1]; xy=mul(x,y)
def integ(w,s):
    p=[F(1)]; t=R(1); total=R(0)
    for k in range(19):
        total+=t*sum((v*F(1,i+1) for i,v in enumerate(mul(w,p))),R(0))/factorial(k)
        p=mul(p,phi);t=t*(-s)
    norm=sum(max(abs(rr(v).a),abs(rr(v).b)) for v in w)
    e=norm/F(factorial(19));return total+R(-e,e)
def calc(s):
    rho=add(add(scale(x,-2*s),scale(y,-s)),scale(add(mul(x,x),scale(mul(y,y),F(1,4))),s*s))
    B=add([1],scale(mul(y,y),-s)); c=add(scale(y,s/2),scale(mul(x,mul(y,y)),-s*s/2))
    I=integ(xy,s);J=integ(mul(x,B),s)
    v=integ(add([1],mul(xy,rho)),s)
    t=R(1);e=R(0)
    for k in range(19):e+=t/factorial(k);t=t*(-s)
    e+=R(-F(1,factorial(19)),F(1,factorial(19)))
    j=integ(add(mul(B,add([1],mul(x,rho))),scale(mul(x,c),-1)),s)+e/2
    a=(2*v-J)/4;b=integ(mul(xy,add([3*s/4],scale(mul(x,x),-s*s/2))),s)
    M=-12*I*j-24*a*J-48*I*b+36*s*I*(v-J)+40*s*I*a+(F(27,2)*s*s-188*s)*I*I+6*e*I
    Ip=-integ(mul(xy,phi),s);Jp=-integ(add(mul(x,mul(y,y)),mul(mul(x,B),phi)),s)
    Lp=28*I*I+56*s*I*Ip-12*(Ip*J+I*Jp)
    return M,Lp,M/(s*s*Lp)
s=R(F(100000000,106702881),F(100000000,106702880));M,Lp,beta=calc(s)
print(M,Lp,beta,s*s*Lp)
assert beta.a>F(-440471,100000) and beta.b<F(-440468,100000)
lam=s*s*Lp
assert lam.a>F(4057998,10000000) and lam.b<F(4058004,10000000)
```

Actual approximate display of exact interval endpoints:
M [-1.7874305465311233,-1.7874243881207528];
L' [0.4620236803745054,0.4620240921427508];
beta [-4.404709099583151,-4.404689915464301];
lambda [0.4057999078078233,0.4058002770740649].

Exploratory 45-digit mpmath quadrature and direct original product recurrence (not rigorous root certificates) gave alpha approx 1.06702880390241058, beta approx -4.40469950082931137. Numerical local crossing estimates q_d-alpha*d^2-beta*d were -12.4012091, -12.4283733, -12.4816814, -12.5130155, -12.5233522, -12.5285004 at d=80,100,200,500,1000,2000. These motivate an order-one coefficient; no value or bound for that coefficient is proved. JR's verified all-budget integer exclusion d<=80 and JS eventual uniqueness are retained, not expanded by these numerical samples.

## Next

Derive the h^2 correction of the normalized joint residual and an explicit uniform remainder bound on a neighborhood of s_*; obtain effective localization of the nearest candidate integer(s), then use exact arithmetic and the JQ/JP residue certificates. Need effective d_0 or finite bridge and a genuine Diophantine separation bound; increasing asymptotic order alone does not prove a uniform gap. No new formal Result, independent review or task closure.
