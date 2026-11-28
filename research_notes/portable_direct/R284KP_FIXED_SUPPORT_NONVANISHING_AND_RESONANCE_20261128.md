# R284KP — Fixed-support nonvanishing and unique leading-order resonance
2026-11-28. Author proof and exact Python/SymPy/Fraction recalculation, NOT_REVIEWED. Auxiliary R284 arithmetic; no native spatial transfer or formal Result. Continuation of the existing direct research lane, previously recorded EM-DIRECT-0C386E / RA-B82240E8488EF5A1DA5186C4. Current owner query r1-20261128-2000-owner-inventory is RUNNING at last observation; own metadata recovery encountered BACKEND_IDENTITY_CHECK_UNAVAILABLE (operation_sent=false). No shared Task acquisition or owner mutation. Global entry snapshot 0cd7603296f69d9401c55faee4f34fc2dc327e34 (both entry blobs rechecked), P000 V4 verified against canonical blob, ACTIVE worldview human/machine, research role/method and BRC principles; Source startup projection and portable protocol at bf828b288462cb0c862aaa28d7e5a393e6ed239d. Scientific definitions unchanged.

Frozen input:
- JR 88211c0912397b00536b6c4d6427cab29d4499f2:research_notes/portable_direct/R284JR_GLOBAL_BUDGET_POLYNOMIAL_AND_INTEGER_ROOT_EXCLUSION_20261127.md
- KO 0c99ee610045cd1d36e9da996f257ae4afabc0be:research_notes/portable_direct/R284KO_FIXED_SUPPORT_FAMILY_AND_EVEN_DECIC_20261128.md
KO leaves nonvanishing of the fixed-support family open. We establish that every fixed s gives a nonzero polynomial, with exact degree and a unique leading-order cancellation at s=5. This is not pointwise nonvanishing for all d,s simultaneously.

## 1. Signed leading moment and exact coefficient
Keep JR's C, P_d, R_v(k), and KO's s>=0, d>=max(3,s+2), d+s odd, q0=(s-d)/2, u=(d+s)/2, r=R_u(d), H_s=(d+s)(d+s+1) product_{j=0}^s(s-d+2+2j), N_s=K_s H_s^2 C(q0,d)/r^2 with KO's positive constant K_s. Put
M_s=sum_{i=0}^s (i+1)(-3)^i R_s(i), e_s=(s+2)/(4(2s+1)).
For fixed s, the backward ratios rho_i tend to (-3)^i. Thus as d tends to infinity along the admissible parity,
V/(rd) -> M_s; Q/(rd) -> -3 M_s by shifting i to i-1;
A/(rd) -> (3/2) M_s because its weight tends to -3/4;
E/(rd) -> -e_s; W/(rd) -> (3/2)M_s-e_s;
Z/(rd^2) -> -(3/4)M_s.
The two full terms of C give
L_s = lim C(q0,d)/(r^2 d^5) = (63/4) M_s^2 - (9/2)e_s M_s = (9/4)M_s(7M_s-2e_s).
The endpoint E is retained, so this is a joint signed moment calculation rather than positive mass compression. Dropping E changes the resonance.

## 2. Uniform classification of vanishing leading coefficient
Since R_s(i)=(-1)^i(-s)_i/(s+3)_i, the binomial expansion and beta integral for integers yield exactly
M_s=(s+1)(s+2) integral_0^1 t[(1-t)(1-3t)]^s dt.
Indeed integral_0^1 t^(i+1)(1-t)^s dt=(i+1)!s!/(i+s+2)!, giving the displayed finite sum. On [0,1/4], (1-t)(1-3t)=1-4t+3t^2 >= 1-4t >=0, whose integrated contribution is at least 1/16. For even s>=2 the other contributions are nonnegative, so M_s>=1/16>2e_s/7=(s+2)/(14(2s+1)) (at s=2 this threshold is 2/35, and it decreases). For odd s>=7 the negative contribution on [1/3,1] is bounded in magnitude by (4/9)(s+1)(s+2)3^(-s), because the quadratic is at least -1/3 and integral of t on that interval is 4/9. Thus
M_s >= 1/16-(4/9)(s+1)(s+2)3^(-s) > 2e_s/7.
The error decreases for s>=7, and the threshold decreases; the strict inequality at s=7 follows from 1/16-32/2187>3/70. The remaining exact moments are M_0=1, M_1=-1/2, M_3=-1/14, M_5=1/22. For s=5, e_5=7/44 and 7M_5=2e_5. For s=0,1,3 the product defining L is positive. Hence L_s>0 for every s>=0 except s=5, where L_5=0. This proves an all-s classification, not a finite fit.

## 3. Resolve s=5 by retaining the next joint coefficient
Let alpha_i=(2i^2+(4s+8)i)/3 and beta_i=1-i+alpha_i. Expanding each KO ratio gives rho_i=(-3)^i(1+alpha_i/d+O_s(d^-2)). Define a_i=(i+1)(-3)^i R_s(i), b_i=i(-3)^i R_s(i-1) with b_0=0; use zero outside support. The normalized V/r, Q/r are sums of a_i(d+beta_i), b_i(d+beta_i) up to O_s(d^-1). The weight in A expands as -3/4+(2s+2i-1/4)/d+O_s(d^-2), so A/r has constant coefficient sum_i[(2s+2i-1/4)-(3/4)beta_i](a_i+b_i). E/r=-e_s d+(4s-1)(s+2)/(4(4s+2))+O_s(d^-1). All these are ordinary expansions of exact rational functions at infinity for fixed s.

For s=5, direct rational sums give the following coefficients (a subscript is the power of d, all entries normalized by r):
V1=1/22, V0=-56/11; Q1=-3/22, Q0=345/22; A1=3/44, A0=-657/88; E1=-7/44, E0=133/88; W1=-1/11, W0=-131/22; Z2=-3/88, Z1=61/16.
The degree-four coefficient of C/r^2 is
-3/2 (W1 Q0+W0 Q1) -(9s+6)/2 W1 Q1 +32 Z2 Z1 -16(3s+2)Z2^2 = -3747/968.
Therefore C(q0,d)/r^2 = -(3747/968)d^4+O(d^3) at s=5. It is not identically zero.

## 4. Consequences
KO's H_s has degree s+3 and squared leading coefficient 1. Therefore, for any choice of the positive integer K_s in KO:
deg N_s=2s+11 if s !=5; deg N_5=20 (not 21).
All N_s are nonzero; their eventual sign is positive except s=5, whose eventual sign is negative. For each fixed s, at most deg N_s values of d can make N_s(d)=0, with no assertion of the locations or admissibility of those zeros. Hence, for all sufficiently large admissible d at each fixed s, KO's valuation constraint is nonvacuous: p>d+s+2 and p|(2q+d-s) at an integer zero implies v_p(2q+d-s)<=v_p(N_s(d)). For each fixed s and sufficiently large d, at most deg N_s distinct primes >d+s+2 can divide N_s(d), by the degree bound on its absolute value. Thresholds depend on s. This does not prove existence of an eligible prime in a candidate budget or eliminate smooth coordinates. For a fixed finite same-parity block of s, primes exceeding all coordinate differences can appear in at most one coordinate; use the actual N_s rather than treating the observations as independent.

## 5. Exact symbolic and full-branch cross-check
For s=0..5, constructed rational C/r^2 from KO's short support and compared against JR's original full Fraction sums on all admissible d through 100, total 288 cases. The following output was obtained (numerator and denominator are reduced; leading means leading coefficient at infinity).
s=0: numerator degree 8, denominator degree 3, N degree 11, leading 27/2, checked 49.
s=1: numerator degree 10, denominator degree 5, N degree 13, leading 9/2, checked 49.
s=2: numerator degree 12, denominator degree 7, N degree 15, leading 54/25, checked 48.
s=3: numerator degree 14, denominator degree 9, N degree 17, leading 27/196, checked 48.
s=4: numerator degree 16, denominator degree 11, N degree 19, leading 3/14, checked 47.
s=5: numerator degree 17, denominator degree 13, N degree 20, leading -3747/968, checked 47.
The s=0,1 polynomials agree with KN/KO. For s=2,3,4 the reduced denominator is a positive constant times (d-(3s+2)) product_{j=0}^{s-1}(d-(s+2+2j))^2 (d+s+1)^2. The printed numerators from the code below specify the exact observers. For s=2,3,4 all coefficients except the linear coefficient are positive, and the quadratic term dominates the negative linear term for d>=2. Hence these fibers are strictly positive for d>3s+2. The s=5 numerator is mixed and no full pointwise classification is claimed.

Executed code (Python with SymPy; exact rational operations):
```python
import sympy as S
from fractions import Fraction as F
from math import prod
x=S.symbols('d')

def compressed(s):
    d=x;q=(s-d)/2;u=(d+s)/2;J=(d+s)*(d+s+1)
    B=prod(s-d+2+2*j for j in range(s+1));H=J*B
    V=Q=A=0;r=1;R=1;prev=0
    for i in range(s+2):
        if i:
            r*=S.Rational(s-i+1,s+i+2)
            R*= (3*d+s+6-2*i)/(s-d+2*i)
        a=(d-i+1)*(i+1)*R*r;b=(d-i+1)*i*R*prev
        V+=a;Q+=b;A+=(u-d+i)*(u+d-i+2)*(a+b)/J
        prev=r
    V,Q,A=map(S.cancel,(V,Q,A))
    E=(u-d)*(2*d+3)*(s+2)/(2*(2*u+1)*(4*s+2))
    W=S.cancel(A+E);Z=S.cancel(q*A+Q+V)
    C=S.factor(3*q*(4*q+3*d+1)**2*W*Q-32*(3*q+d+1)*Z**2)
    N=S.Poly(S.cancel(H**2*C),x)
    return C,N

def primal(d,s):
    q=F(s-d,2);u=q+d;n=s
    def rr(v):
        a=[F(1)]
        for i in range(d):a.append(a[-1]*F(v-i,v+i+3))
        return a
    U,M=rr(u),rr(n);V=Q=A=F(0)
    for k in range(d+1):
        l=d-k;a=(k+1)*(l+1)*U[k]*M[l];b=(k+1)*l*U[k]*M[l-1] if l else 0
        V+=a;Q+=b;A+=F((u-k)*(u+k+2),2*u*(2*u+1))*(a+b)
    E=U[d]*F((u-d)*(2*d+3)*(n+2),2*(2*u+1)*(4*n+2));Z=q*A+Q+V
    return (3*q*(4*q+3*d+1)**2*(A+E)*Q-32*(3*q+d+1)*Z**2)/U[d]**2

if __name__=='__main__':
    for s in range(6):
        C,N=compressed(s);num,den=S.fraction(C);pn,pd=S.Poly(num,x),S.Poly(den,x)
        print('s',s,'C',C,'N degree',N.degree(),'C exponent',pn.degree()-pd.degree(),'leading',pn.LC()/pd.LC(),flush=True)
        count=0
        for d in range(max(3,s+2),101):
            if (d+s)%2==0:continue
            a=primal(d,s);b=C.subs(x,d);assert a==F(int(b.p),int(b.q)),(s,d,a,b)
            count+=1
        print('verified',count,flush=True)
```

Raw exact reduced numerator coefficient vectors (descending degree; s=3 has external factor 3, s=5 external factor -1):
s=2: [54,1137,21760,253118,2189804,10529045,34422227,67103960,460103848,1809026928,1987045488,-40030848,15323904].
s=3: 3*[36,6176,254919,3411960,73153550,643137024,6268367517,24223147216,102097514376,121557236736,1844665103761,11437439303928,13252889556966,-6957100009440,984094855275].
s=4: [42,451,126674,1151294,121447696,707712371,29352971889,148181618104,2277044175608,4832399420400,39838337491344,9309674500608,624891798284800,7660511604301824,10098903298904064,-11033690150338560,2551238000640000].
s=5: -[7494,-1517131,34171374,-2484949450,23336426158,-1315154378302,3038377984726,-259251287472466,-124464732528398,-18657766842097828,2903062415026026,-313090353852355678,-9050207764794534,-922968867952473714,-92465430427562122926,-151263138513165340806,240158799016295906880,-75431568107652912225].
Denominator constants respectively 25,784,196,1936 with the same factor formula above also for s=5. No floating point was used for any equality test. Cross-checks are author's separate implementations, not independent research review.

## Next
Use s=2,3,4 on the still-unresolved d>3200 root-adjacent candidates and quantify union gain with prior coordinates; determine actual finite exceptions in s=5 and whether more general nonvanishing thresholds can be uniform in s. The sign resonance suggests that subleading signed moments and endpoint terms matter for other joint observers. No expansion of the all-budget range d<=3200 is claimed. No all-parameter integer exclusion or formal Result.
