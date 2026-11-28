# R284KS — first-order signed transport and arithmetic thin resonance strip

2026-11-28. Author proof and exact Fraction computation, NOT_REVIEWED. Auxiliary R284 arithmetic, no native spatial transfer or formal Result. Existing independent frontier EM-DIRECT-0C386E / TASK_RESEARCH / RA-B82240E8488EF5A1DA5186C4. Own recovery r1-20261128-2304-own-metadata returned original open session, no formal runs; metadata is not CLAIM. Owner read r1-20261128-2304-owner-inventory initiated; no shared task acquisition/mutation. Global canonical entry blobs matched main snapshot 5a5e6d3d8f06c21850e61bf9e0d50f57cfcfd265; P000 V4 projection matched canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; Source V5 foundation startup, ACTIVE worldview, portable protocol and current research method read/reused. Frozen science: KR cf64c7743fb98b07702cb2cf401c1cc07c0f01b2:research_notes/portable_direct/R284KR_BETA_SIGNED_TRANSPORT_AND_LINEAR_SUPPORT_RESONANCE_20261128.md (its JR/KO/KP/KQ pins unchanged).

## 1. Main theorem

Retain KR's complete signed arithmetic observer, including endpoint E. Let d,s be admissible integers, d+s odd, d>=8(s+4), x=s/d in [1/10,1/8], q0=(s-d)/2, r=R_((d+s)/2)(d). Define F(d,s)=C(q0,d)/(r^2 d^5). Uniformly on this compact wedge,

F(d,s)=Phi(x)+Psi(x)/d+O(d^-2),

with absolute constant on the specified wedge and
Phi(x)=(x-1)^3(x+3)J(x)/(1024(x+1)^2),
J(x)=52x^4+147x^3-63x^2+89x-9,
Psi(x)=-(x-1)^3 H(x)/(4096 x (x+1)^3),
H(x)=236x^8+3111x^7+9679x^6+5651x^5-8053x^4-10987x^3-2307x^2-2127x+189.

This is the first-order coefficient of the full joint residual, not a fit. Constants in O(d^-2) are not optimized or explicitly evaluated.

## 2. Proof: signed integral expansion with uniform remainder

KR gives S_s(y)=(s+1)(s+2) integral_0^1 t[(1-t)(1-yt)]^s dt and T_s(y)=-y S_s(y), and represents the signed backward ratio via inverse Beta Y. Set f(y)=(1+y)^-2 and g(y)=6y/(1+y)^4. Uniformly for 1<=y<=11/2,

S_s(y)=f(y)+g(y)/s+O(s^-2).

Indeed let t=z/s and restrict initially t<=1/12. Write -log((1-t)(1-yt))=(1+y)t+(1+y^2)t^2/2+O(t^3), with nonnegative remainder bounded by an absolute constant times t^3 (yt<=11/24). For A=(1+y^2)z^2/(2s), B=O(z^3/s^2), B>=0, the difference of exp(-A-B) and 1-A has magnitude <= A^2/2+B, by the Taylor inequality for exp(-A) and its Lipschitz bound on nonnegative inputs. Multiply by z exp(-(1+y)z) and integrate: the error is O(s^-2). The positive and negative pieces on t>=1/12 have magnitudes <=(11/12)^s and <=(81/88)^s respectively; the rescaled exponential tails are also negligible. The prefactor (s+1)(s+2)/s^2=1+3/s+2/s^2 yields g=3/(1+y)^2-3(1+y^2)/(1+y)^4=6y/(1+y)^4. The same rescaling, or differentiating the finite integral first, gives S_s^(j)=f^(j)+O(1/s) for fixed j<=3: on the small-t range the j-th derivative integrand has factor (-1)^j(s)_fall_j t^j(1-t)^j times f_y(t)^(s-j), where f_y(t)=(1-t)(1-yt); after t=z/s its leading factor relative to z^j is 1+O((1+z)/s), and the exponential difference is bounded by O(z^2/s) times the integrable leading envelope. On the rest use the same exponential bounds with s-j and polynomial prefactors. This proves the leading derivative estimate without assuming differentiation of an arbitrary O-term. T_s follows by multiplication by -y.

## 3. Inverse-Beta first-order expectation

Put y0=(3+x)/(1-x), m1=(4+2y0)/(1-x), v1=2y0(y0-1)/(1-x). KR's a=(3d+s+4)/2, b=(d-s-2)/2 give the exact fixed moments E[Y^k]=product_{j=0}^{k-1}(a-j)/(b-j). Expanding each factor for fixed k<=4 yields

E[Y^k]=y0^k+(k y0^(k-1)m1+binom(k,2)y0^(k-2)v1)/d+O(d^-2).

This follows because the j-th ratio is y0+[m1+2j(y0-1)/(1-x)]/d+O(d^-2). Consequently E[Y-y0]=m1/d+O(d^-2), E[(Y-y0)^2]=v1/d+O(d^-2), while the signed third and the nonnegative fourth moments about y0 are O(d^-2); the constant and first-order terms cancel by binomial differences. Uniformity follows since 1-x>=7/8.

For any fixed smooth rational function h used below (denominators powers of 1+y, no poles for y>=1), Taylor to cubic at y0 on the KR central interval gives E[h(Y)]=h(y0)+(m1 h'(y0)+(v1/2)h''(y0))/d+O(d^-2). The signed cubic term and fourth-order remainder are O(d^-2). For truncation to Y<=11/2, fixed-order moment tails through order four are exponentially small: use KR's inverse-moment ratios <=5 for j<=s+floor(d/32), giving E[Y^k 1_tail] <=5^k(10/11)^floor(d/32) for fixed k<=4 and sufficiently large d; the actual S_s,T_s and Euler moments' tails are exponentially suppressed by KR's full signed integral bound. On the compact wedge s is proportional to d, so s^-2=O(d^-2). Thus the joint expectation of S_s (or T_s) has leading h=f (or -yf), correction h1=m1 h'+v1 h''/2+g_h/x with g_h=g (or -yg), all evaluated at y0. Euler moments through order three have leading values from h with O(1/d) error: use the derivative estimate of section 2 and the same expectation formula. This suffices for every coefficient multiplied by d^-1 or d^-2 in KR's finite observer.

## 4. Full endpoint-retaining algebra

Write normalized Vbar=V/(rd), Qbar=Q/(rd), Abar=A/(rd), Ebar=E/(rd), Wbar=W/(rd), Zbar=Z/(rd^2); subscripts 0,1 are coefficients at orders 1,d^-1. D=y*d/dy. For (V,Q), use h=f,-yf respectively; each first coefficient is
h1+(1-D)h at y0 (KR operator L_d).
Set w=(x-1)(x+3)/(4(x+1)^2), w1=(x-1)/(x+1)^2-w/(x+1).
Then A0=w(V0+Q0),
A1=w(V1+Q1)+w1(V0+Q0)+2/(x+1)^2 D((1-y)f)|_{y0}.
Indeed w(i)=w+[w1+2i/(x+1)^2]/d+O(d^-2) coefficientwise as a quadratic polynomial in i; bounded Euler moments through order 3 justify the residual. KR's exact Ebar gives
E0=(x-1)/(8(x+1)),
E1=E0(3/(2x)+3/2-1/(x+1)).
Wj=Aj+Ej; Z0=(x-1)A0/2, Z1=(x-1)A1/2+V0+Q0.

Explicit coefficients after rational simplification:
V1=-(x-1)(5x^3+19x^2-17x+9)/(128x);
Q1=-(x-1)(5x^3+31x^2+7x-27)/(128x);
A1=-(x-1)(5x^5+35x^4+38x^3+18x^2+5x+27)/(256x(x+1)^2);
E1=(x-1)(3x^2+4x+3)/(16x(x+1)^2);
W1=-(x-1)(5x^3+25x^2-17x-21)/(256x);
Z1=-(x-1)(5x^6+30x^5-61x^4-212x^3-205x^2-42x-27)/(512x(x+1)^2).

For c=(3/2)(x-1)(1+2x)^2, c1=3(x-1)(1+2x), e=16(1-3x), the full normalized C is (c+c1/d+O(d^-2))Wbar Qbar+(e-32/d)Zbar^2. Thus
Psi=c1 W0 Q0+c(W1 Q0+W0 Q1)-32 Z0^2+2e Z0 Z1.
Substitution of the coefficients above proves the displayed rational formula for Psi, checked by SymPy exact symbolic simplification. All errors in this step are O(d^-2) since the normalized joint values and coefficients are bounded on the wedge. In particular endpoint E1 is retained and affects Psi.

## 5. Corrected resonance and arithmetic sparsity

Let alpha be the unique KR root of J in (0,1/8). It lies in (1/10,1/8). Let beta=-Psi(alpha)/Phi'(alpha); alpha=0.107140924600131309809267119349... and beta=-0.670172840770269570838659179813... (numerical display); Phi'(alpha)=-0.142401337162959..., Psi(alpha)=-0.0954335086559852....

By KR's bounded-width result all sufficiently large formal zero fibers on the original wedge satisfy s-alpha*d=O(1), hence lie in the present compact wedge. Taylor expansion of Phi and Psi around alpha gives
d F(d,s)=Phi'(alpha)(s-alpha*d-beta)+O(d^-1)
uniformly on any fixed bounded-width strip. Therefore there is a constant K such that every sufficiently large admissible formal zero satisfies

|s-alpha*d-beta| <= K/d.

Outside this thin strip but inside any fixed-width KR strip, with sufficiently large K for that strip, the sign of F is the sign of Phi'(alpha)(s-alpha*d-beta). KR handles regions separated from the resonance. No assertion that an exact zero exists or that the strip is empty. In particular this is about the formal negative-budget fibers, not the original positive-budget zeros.

The thin strip has a provable sublinear count. J has no root modulo 17 (check all 17 residues), and the rational root theorem gives a denominator dividing 52, coprime to 17. Hence J has no rational root. If two distinct pairs (d,s),(d',s') in the strip have D<=d,d'<=2D, then for sufficiently large D each d has at most one s. Set k=|d-d'|>=1 and l=(s-s')*sgn(d-d'). We have |l-alpha*k|<=2K/D. Since J(l/k) is a nonzero integer divided by k^4, the mean-value theorem on a fixed interval containing alpha and l/k gives |l-alpha*k|>=1/(M k^3) for a finite constant M (bound for |J'| on e.g. [-1,2], for sufficiently large D). Thus k>=(D/(2KM))^(1/3) (take K>0). Ordered d-values have this minimum spacing; hence at most O(D^(2/3)) possible pairs per dyadic block, and O(X^(2/3)) up to X after adding a finite initial region. This counts candidate locations, not actual zeros, and is an elementary bound without distribution assumptions. It improves KR's O(X) candidate count.

## 6. Reproduction: executed local exact Fraction check

SymPy independently simplified the coefficient expression in section 4. The following program checks the finite near-resonance sample using the original KR short sum (all residual comparisons exact; decimals only display). It also checks J has no root mod 17. This finite sample does not establish a uniform numerical K or the O-bound; those follow from the argument above.

```python
from fractions import Fraction as F
from math import floor
def J(x):return 52*x**4+147*x**3-63*x*x+89*x-9
def phi(x):return (x-1)**3*(x+3)*J(x)/(1024*(x+1)**2)
def psi(x):return -(x-1)**3*(236*x**8+3111*x**7+9679*x**6+5651*x**5-8053*x**4-10987*x**3-2307*x**2-2127*x+189)/(4096*x*(x+1)**3)
def short(d,s):
    q=F(s-d,2);u=F(d+s,2);den=(d+s)*(d+s+1)
    V=Q=A=F(0);r=rho=F(1);prev=F(0)
    for i in range(s+2):
        if i:
            r*=F(s-i+1,s+i+2)
            rho*=F(3*d+s+6-2*i,s-d+2*i)
        a=(d-i+1)*(i+1)*rho*r;b=(d-i+1)*i*rho*prev
        V+=a;Q+=b;A+=F((u-d+i)*(u+d-i+2),den)*(a+b)
        prev=r
    E=F((u-d)*(2*d+3)*(s+2),2*(2*u+1)*(4*s+2))
    W=A+E;Z=q*A+Q+V
    C=3*q*(4*q+3*d+1)**2*W*Q-32*(3*q+d+1)*Z**2
    return C/d**5
lo=F(1,10);hi=F(1,8)
for _ in range(80):
    md=(lo+hi)/2
    if J(md)<0:lo=md
    else:hi=md
n=0;mx=F(0)
for d in (1000,2000,4000,8000,16000):
    base=floor(lo*d);base-=int((base+d)%2==0)
    for s in (base-2,base,base+2):
        assert d>=8*(s+4) and (d+s)%2
        x=F(s,d);c=short(d,s);err=d*d*(c-phi(x)-psi(x)/d);mx=max(mx,abs(err));n+=1
        print(d,s,'Cnorm=%+.10e'%float(c),'d2err=%+.8f'%float(err))
assert all(J(i)%17 for i in range(17))
print('count',n,'max abs scaled error',float(mx),'exact < 4?',mx<4)
```

Actual output:
```
1000 105 Cnorm=+2.1523083663e-04 d2err=-2.25773291
1000 107 Cnorm=-7.7192772123e-05 d2err=-2.14587977
1000 109 Cnorm=-3.6366226667e-04 d2err=-2.04167990
2000 211 Cnorm=+1.8913283324e-04 d2err=-2.23567627
2000 213 Cnorm=+4.3997620316e-05 d2err=-2.17960508
2000 215 Cnorm=-9.9674471859e-05 d2err=-2.12549182
4000 425 Cnorm=+1.0392617931e-04 d2err=-2.19667417
4000 427 Cnorm=+3.1995131425e-05 d2err=-2.16909741
4000 429 Cnorm=-3.9574996703e-05 d2err=-2.14200535
8000 855 Cnorm=+2.6027349933e-05 d2err=-2.16386694
8000 857 Cnorm=-9.6906276947e-06 d2err=-2.15031203
8000 859 Cnorm=-4.5319165996e-05 d2err=-2.13687642
16000 1711 Cnorm=+2.3051859897e-05 d2err=-2.16125753
16000 1713 Cnorm=+5.2097189600e-06 d2err=-2.15447786
16000 1715 Cnorm=-1.2610114784e-05 d2err=-2.14772809
count 15 max abs scaled error 2.2577329055579383 exact < 4? True
```

## 7. Next

Derive explicit second-order coefficient and constants for the narrow strip, or a uniform arithmetic height bound for linearly growing observers. A shrinking strip alone does not prove integer separation; the inhomogeneous approximation problem involves beta as well as alpha. The original positive-budget all-integer exclusion range remains 3<=d<=3200 (previously established scope, unchanged here). No independent scientific review or Foundation admission claimed.
