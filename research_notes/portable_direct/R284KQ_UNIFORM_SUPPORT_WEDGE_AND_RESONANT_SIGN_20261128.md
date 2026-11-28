# R284KQ — Uniform moving-support wedge and exact resonant sign classification
2026-11-28. Author proof and exact calculation, NOT_REVIEWED. Auxiliary R284 arithmetic; no native spatial transfer. Existing own researcher EM-DIRECT-0C386E / TASK_RESEARCH, RA-B82240E8488EF5A1DA5186C4; own session metadata recovered (r1-20261128-2104-own-recovery), no formal runs. Owner inventory r1-20261128-2104-owner-inventory WAITING_RESOURCE / EVENT_READ_CONTROL_BUSY at last observation; no claim or owner mutation. P000 global V4, Source V5 startup, ACTIVE worldview, joint/residual typing, current portable and research method read. Global entry blobs at 0cd7603296f69d9401c55faee4f34fc2dc327e34 match freshly read main entry blobs. Current behavior separate from frozen scientific input.
Frozen science:
- JR 88211c0912397b00536b6c4d6427cab29d4499f2:research_notes/portable_direct/R284JR_GLOBAL_BUDGET_POLYNOMIAL_AND_INTEGER_ROOT_EXCLUSION_20261127.md
- KO 0c99ee610045cd1d36e9da996f257ae4afabc0be:research_notes/portable_direct/R284KO_FIXED_SUPPORT_FAMILY_AND_EVEN_DECIC_20261128.md
- KP 3446e2f82ae8f61a7893f961d0c7ac065b6f2e39:research_notes/portable_direct/R284KP_FIXED_SUPPORT_NONVANISHING_AND_RESONANCE_20261128.md

## 1. Exact one-state signed moment recurrence
Keep s>=0, d>=max(3,s+2), d+s odd, q0=(s-d)/2, u=(d+s)/2, r=R_u(d), with JR's complete C including endpoint E. KP's M_s=sum_{i=0}^s (i+1)(-3)^i R_s(i) and e_s=(s+2)/(4(2s+1)). The signed moment is
M_s=(s+1)(s+2) integral_0^1 t f(t)^s dt, f(t)=1-4t+3t^2.
Write I_s=integral_0^1 f^s. Because f'=6t-4, M_s=(s+1)(s+2)*(2/3) I_s -(s+2)/6. For s>=1, integration of derivative ((t-2/3)f^s) yields
(2s+1)I_s+(2s/3)I_{s-1}=2/3,
using f(1)=0, f(0)=1 and 3(t-2/3)^2=f+1/3. Substitute I_{s-1} from M_{s-1}; exactly
M_0=1, M_s=(s+2)(1-4 M_{s-1})/[6(2s+1)].
This is an exact quotient for the scalar leading-moment observer, not the full signed branch state. It does not discard the endpoint in KP's L_s=(9/4)M_s(7M_s-2e_s).

Put delta_s=M_s-1/16. Then
delta_s=3/[16(2s+1)] - [2(s+2)/(3(2s+1))] delta_{s-1}.
At s=7, M_7=19/286 and 0<delta_7<3/240. For s>=8, 2(s+2)<3(2s-1), hence induction gives 0<delta_s<=3/[16(2s+1)] for s>=7. In particular M_s -> 1/16 and L_s -> 27/1024. Since 2e_s<=3/10 for s>=7, L_s >= (9/4)(1/16)(7/16-3/10)=99/5120 >1/60. Exact M_0..6 = 1,-1/2,2/5,-1/14,1/7,1/22,12/143 verify L_s>1/60 for s=0..6 except L_5=0. Thus a uniform leading gap holds for all s!=5, stronger than pointwise positivity.

## 2. Uniform error bound for simultaneous s,d
Set t=s+2, B=3t^2 (4/3)^s, epsilon=t^2/d. For all admissible d>=12t^2 we prove
|C(q0,d)/(r^2 d^5)-L_s| <= 10000 B^2 epsilon.
The proof uses the exact KO backward ratios and the joint endpoint, with all constants explicit.

Absolute moment A_abs=sum_{i=0}^s (i+1)3^i R_s(i) equals (s+1)(s+2) integral_0^1 x[(1-x)(1+3x)]^s dx by the same beta identity. The quadratic is at most 4/3 on [0,1], giving A_abs <= (s+1)(s+2)(4/3)^s/2. In the short support, the absolute sums of a_i=(i+1)(-3)^i R_s(i) and b_i=i(-3)^i R_s(i-1), b_0=0, are A_abs and 3 A_abs respectively, both <=B. The latter identity uses the full i=0..s+1 support.

For i<=s+1, rho_i=R_u(d-i)/r. Each factor of rho_i/(-3)^i is
(1+(s+4-2j)/(3d))/(1-(s+2+2j)/d), j=0..i-1.
Its difference from 1 is nonnegative and <=6t/d (the numerator difference before dividing is (4s+10+4j)/(3d)<=3t/d, denominator >=1/2). Hence 1<=rho_i/(-3)^i<=exp(6t^2/d)<=exp(1/2)<2 and the difference from 1 is <=12 epsilon (exp(x)-1<=2x for 0<=x<=1/2). The additional factor (1+(1-i)/d) is positive and at most 1+1/d. Its product with rho_i/(-3)^i is <2 and differs from 1 by <=14 epsilon. Thus Vbar=V/(rd), Qbar=Q/(rd) obey
|Vbar-M_s|, |Qbar+3M_s| <=14 B epsilon; |Vbar|,|Qbar|<=2B.

The weight for A at i is w_i=(-d+s+2i)(3d+s-2i+4)/[4(d+s)(d+s+1)]. Expanding w_i+3/4 gives numerator d(3a-b+6s+3)+ab+3s(s+1), denominator 4(d+s)(d+s+1), with a=s+2i, b=s-2i+4. Use |a|<=3t, |b|<=2t, |3a-b+6s+3|<=19t and |ab+3s(s+1)|<=9t^2. Consequently |w_i+3/4|<=10t/d. The combined absolute mass at finite d is <=4B, so Abar=A/(rd) has |Abar-(3/2)M_s|<=21 B epsilon+40B t/d<=61B epsilon, |Abar|<=8B. This controls signed cancellation by retaining the joint sum instead of replacing it by a positive mass.

Ebar=E/(rd)=-e_s (1-s/d)(1+3/(2d))/(1+(s+1)/d). Direct subtraction gives |Ebar+e_s|<=4t/d and |Ebar|<=1. Hence Wbar=W/(rd) obeys |Wbar-W0|<=65B epsilon, |Wbar|<=9B, |W0|<=2B with W0=(3/2)M_s-e_s. Zbar=Z/(rd^2)=(q0/d)Abar+(Qbar+Vbar)/d, so |Zbar-Z0|<=39B epsilon, |Zbar|<=5B, |Z0|<=B, Z0=-(3/4)M_s. Also |Q0|=|-3M_s|<=B.

Now C/(r^2 d^5)=alpha Wbar Qbar+beta Zbar^2 where alpha=3(q0/d)(1+(2s+1)/d)^2, beta=-32(3q0+d+1)/d. Their limiting coefficients are -3/2 and 16 respectively. Expanding gives |alpha+3/2|<=15t/d and |beta-16|<=48t/d (use 0<=(2s+1)/d<1).
Subtract the limiting expression exactly, preserving both terms:
first product difference <=15 epsilon*18B^2+(3/2)*(65*2+2*14) B^2 epsilon;
second product difference <=48 epsilon*25B^2+16*39*6 B^2 epsilon.
Sum <6000 B^2 epsilon, so the stated 10000 bound holds. All bounds apply jointly to varying s,d; no pointwise asymptotic substitution is used.

Corollary (explicit uniform moving-support wedge). For every admissible s!=5 and
d >= 10800000 (s+2)^6 (16/9)^s
we have C(q0,d)/(r^2 d^5)>1/120. Indeed the RHS threshold is 1200000 B^2 t^2; error <=1/120 and L_s>1/60. The observer N_s(d) is nonzero on this wedge. In particular for any fixed 0<c<1/log(16/9), all s<=c log d except s=5 satisfy the wedge for sufficiently large d, with admissible parity. The explicit constant is conservative; it establishes joint growth, not a practical optimal threshold. This is a uniform sign theorem in the varying parameter, not a finite fit. KO's valuation rule continues to apply in its exact stated prime range; the sign wedge alone does not give a uniform bound on N_s coefficients or an integer-root exclusion for the original positive q.

## 3. Full s=5 resonance sign, all admissible d
From exact KO short-support evaluation, reproduce KP's reduced C/r^2=-P(d)/D5(d) where
D5=1936(d-17)(d-15)^2(d-13)^2(d-11)^2(d-9)^2(d-7)^2(d+6)^2.
P has degree 17 and descending coefficients:
[7494,-1517131,34171374,-2484949450,23336426158,-1315154378302,3038377984726,-259251287472466,-124464732528398,-18657766842097828,2903062415026026,-313090353852355678,-9050207764794534,-922968867952473714,-92465430427562122926,-151263138513165340806,240158799016295906880,-75431568107652912225].
The exact shift P(x+8) has signs [+,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-], exactly one variation. Exact endpoints:
P(8)=-804925343910016617005025
P(187)=-3531674726718699521314454364858875904000
P(188)=13788753995315632833104379606103313930175
Descartes and IVT give exactly one root on (8,infinity), in (187,188), simple. Sign P<0 below it and P>0 above. Since s=5 requires even d>=8, denominator never vanishes and changes sign at 17. Therefore C/r^2<0 for even 8<=d<=16, >0 for even 18<=d<=186, <0 for even d>=188. No admissible integer d is a zero of this fiber; this is an all-budget-in-d statement for this formal negative-budget observer, not the original positive-budget root theorem. Combining KP's s=2,3,4 numerator coefficients (positive apart from linear term dominated by quadratic for d>=2) with the explicit s=0,1 formulas (positive numerator and no denominator zero on admissible parity) gives pointwise nonzero for s=0..5 at all admissible d. The s=5 unique sign crossing lies between integers and remains an available observer.

## 4. Reproduction (executed Python)
```python
from fractions import Fraction as F
import sympy as S
x=S.symbols('d')
def short(d,s):
    q=(s-d)/2;u=(d+s)/2;J=(d+s)*(d+s+1)
    V=Q=A=0;r=R=1;prev=0
    for i in range(s+2):
        if i:
            r*=F(s-i+1,s+i+2)
            R*=(3*d+s+6-2*i)/(s-d+2*i)
        a=(d-i+1)*(i+1)*R*r;b=(d-i+1)*i*R*prev
        V+=a;Q+=b;A+=(u-d+i)*(u+d-i+2)*(a+b)/J
        prev=r
    E=(u-d)*(2*d+3)*(s+2)/(2*(2*u+1)*(4*s+2))
    W=A+E;Z=q*A+Q+V
    return 3*q*(4*q+3*d+1)**2*W*Q-32*(3*q+d+1)*Z**2
def moment(s):
    r=F(1);m=F(1);abs_m=F(1)
    for i in range(1,s+1):
        r*=F(s-i+1,s+i+2)
        z=(i+1)*3**i*r
        m+=(-1)**i*z;abs_m+=z
    return m,abs_m
m=F(1);n=0
for s in range(101):
    if s: m=F(s+2,6*(2*s+1))*(1-4*m)
    direct,a=moment(s);assert m==direct
    assert a<=F((s+1)*(s+2),2)*F(4,3)**s
    e=F(s+2,4*(2*s+1));L=F(9,4)*m*(7*m-2*e)
    assert L==0 if s==5 else L>F(1,60)
    if s>=7: assert 0<=m-F(1,16)<=F(3,16*(2*s+1))
    n+=1
print('moment recurrence / absolute bound / uniform L checks:',n)
C=S.factor(short(x,5));num,den=S.fraction(C)
P=S.Poly(-num,x);print('s5 numerator sign-normalized coefficients:',P.all_coeffs());print('s5 denominator:',S.factor(den))
shift=S.Poly(P.as_expr().subs(x,x+8),x);signs=[int(S.sign(c)) for c in shift.all_coeffs() if c]
print('s5 shift8 signs:',signs);assert signs==[1]+[-1]*17
for d in (8,187,188): print('P(%d)='%d,P.eval(d))
assert P.eval(187)<0<P.eval(188)
for d in range(8,401,2):
    c=short(F(d),5);assert (c>0)==(18<=d<=186) and c!=0
print('s5 exact short-support sign tests:',len(range(8,401,2)))
n=0
for s in range(21):
    t=s+2;B=3*t*t*F(4,3)**s;m,_=moment(s);e=F(s+2,4*(2*s+1));L=F(9,4)*m*(7*m-2*e)
    for d0 in [12*t*t,100*t*t,10**6*t*t,(1200000*B*B*t*t).__ceil__()]:
        d=d0 if (d0+s)%2 else d0+1
        C=short(F(d),s)/d**5
        assert abs(C-L)<=10000*B*B*t*t/d
        if d>=1200000*B*B*t*t and s!=5:assert C>0
        n+=1
print('uniform error bound exact checks:',n)
```
Actual execution: 101 moment recurrence/absolute bound/leading gap checks; s=5 polynomial coefficients, denominator, shift signs and three evaluations exactly as above; 197 exact short-support sign tests (d=8,10,...,400); 84 exact error bound checks (s=0..20, four d scales, adjusted parity). All passed. Symbolic and rational checks are author verification, not independent review. The uniform theorem follows from the analytic bound, not these samples.

## Next
Use the now uniformly nonzero short-support block and its signed leading recurrence to investigate joint constraints on the still-unresolved positive-budget roots. Improve the exponential absolute-mass bound by grouping adjacent signed contributions while preserving endpoint; derive uniform coefficient-height bounds if claiming an exception count with s growing. Then compare union gains of s=2,3,4,5 observers on actual d>3200 root-adjacent candidates; no new all-budget positive-q range claimed. No formal Result or independent review.
