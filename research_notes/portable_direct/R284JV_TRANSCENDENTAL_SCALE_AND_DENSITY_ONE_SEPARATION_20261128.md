# R284JV — Transcendental scale, all-order joint asymptotics, and density-one integer separation

2026-11-28. Author proof with exact rational identity check; NOT_REVIEWED. Own recovered metadata: EM-DIRECT-0C386E / TASK_RESEARCH (MCP-8cd6c4fa26b9459d923ff73ba0082220), no formal run, no shared task mutation. Owner query r1-20261128-0000-leased last observed RUNNING; subsequent receipt read returned BACKEND_IDENTITY_CHECK_UNAVAILABLE, operation_sent=false. Global entries read at immutable main@297dbdfb2867d1d1af49ce2428ef43b0196f208d; P000 V4/V5, active worldview, joint/residual and current portable/continuation rules consulted. Ordinary auxiliary arithmetic observer, not a native spatial attribution.

Frozen scientific inputs: JT 23bd59c52f6ea136f84c7b2da94776d4b2bfbd00:research_notes/portable_direct/R284JT_SECOND_ORDER_SCALING_AND_ROOT_DISTANCE_20261127.md; JS b081101b186a92ca04358892d678eb64b9d8f786:research_notes/portable_direct/R284JS_UNIFORM_SCALING_ROOT_AND_EVENTUAL_UNIQUENESS_20261127.md. Exact observer and endpoint E unchanged. Previous JU conversation reported gamma=-12.53363505603851 and interval (-12.534,-12.533), but no published full JU proof/code was confirmed; its numerical gamma is not a premise here. This note supplies an independent existence proof for the constant coefficient, not its numerical certification.

## 1. Transcendence theorem for the scale constant

Let phi(x)=x^2+(1-x)^2/2, I(s)=int_0^1 x(1-x) exp(-s phi(x)) dx, J(s)=int_0^1 x[1-s(1-x)^2] exp(-s phi(x)) dx. JS gives L(s)=4I(s) F(s), F(s)=7s I(s)-3J(s), with a unique simple positive root s_* and alpha_*=1/s_*.

**Theorem. Every nonzero complex zero of F is transcendental. In particular alpha_* is transcendental.**

Put z=s/6, w=3x-1 and define the joint entire carrier
H(z)=int_{-1}^2 exp(-z w^2) dw, e_1(z)=exp(-z), e_4(z)=exp(-4z).
Then phi=1/3+w^2/6 and the exact polynomial weight gives
9 exp(2z) F(6z) = int_{-1}^2 [2z w^3-20z w^2+(14z-3)w+36z-3] exp(-z w^2) dw.
Writing M_j=int_{-1}^2 w^j exp(-z w^2) dw, integration by parts gives
2z M_1=e_1-e_4,
2z M_2=H-e_1-2e_4,
2z M_3=2M_1+e_1-4e_4.
Consequently the exact zero-preserving identity for z != 0 is
18z exp(2z) F(6z)=(72z^2-26z) H(z)+(36z-1)e_1(z)+(18z+1)e_4(z).
It also holds at z=0 as an entire identity.

H is a strict E-function: its exponential generating coefficients are (-1)^n(1+2^(2n+1))/(2n+1), bounded exponentially, with simultaneous denominators dividing lcm(1,...,2N+1)=exp(O(N)) by the elementary Chebyshev bound. It satisfies the differential system below, hence a scalar linear differential equation over Q(z). The exponentials are E-functions as well. The vector (H,e_1,e_4) solves the homogeneous rational first-order system
H'=(-H+e_1+2e_4)/(2z), e_1'=-e_1, e_4'=-4e_4,
whose only possible finite pole is z=0. The three functions are linearly independent over C(z): as z tends to positive infinity, sqrt(z)H(z) tends to sqrt(pi) by the Gaussian integral; any nonzero rational multiple of H has algebraic-power growth or decay and cannot be cancelled by rational multiples of the exponentially decaying functions. With H absent the two distinct exponentials are independent by the same exponential versus rational growth argument.

Apply F. Beukers, "A refined version of the Siegel–Shidlovskii theorem", Ann. of Math. 163 (2006), 369–379, Corollary 1.4 p.371 (regular nonzero algebraic points preserve linear independence of E-function values over algebraic numbers). DOI 10.4007/annals.2006.163.369; https://annals.math.princeton.edu/wp-content/uploads/annals-v163-n1-p08.pdf . The original corollary was checked on the journal PDF. At any nonzero algebraic z all three values are therefore algebraically-linearly independent. The coefficient vector in the exact identity is nonzero: 36z-1 and 18z+1 cannot both vanish. Thus F(6z) cannot vanish there. Since s_* >0, both s_* and its reciprocal alpha_* are transcendental. QED.

This proof only claims transcendence of F zeros; a complex zero of I in the other factor of L is outside its scope.

## 2. All-order expansion existence without a numerical gamma premise

Use exact JT definitions:
q=d^2/s, h=1/d, x=k/d, y=1-x, u=q+d, m=2q+d, l=d-k,
R_n(k)=prod_{i<k}(n-i)/(n+i+3),
a_k=(k+1)(l+1)R_u(k)R_m(l), b_k=(k+1)l R_u(k)R_m(l-1) (zero when l=0),
V=sum a_k, Q=sum b_k, A=sum [(u-k)(u+k+2)/(2u(2u+1))](a_k+b_k),
E=R_u(d)(u-d)(2d+3)(m+2)/(2(2u+1)(4m+2)),
C=3q(4q+3d+1)^2(A+E)Q-32(3q+d+1)(qA+Q+V)^2.
Target equality implies C=0.

For any fixed integer N and derivative order r, all the normalized V/d^3,Q/d^3,A/d^3,E/d^3 have uniform h expansions to degree N, with O_{C^r}(h^(N+1)) on s in [0,4]. Proof: the log of each R factor, after division by lambda q (lambda=1 or 2), is
log[1+(s/lambda)(1-i h)h]-log[1+(s/lambda)(1+i h)h+3(s/lambda)h^2].
Taylor to degree N+1 with uniform O_{C^r}(h^(N+2)) per factor. At each power of h the coefficient is a polynomial in i h and s. Sums over i<k of powers of i h are exact Faulhaber polynomials in x=k h and h, with lowest h power -1. Thus the summed log has uniform expansion through degree N with remainder O_{C^r}(h^(N+1)), leading -s x^2/lambda. Exponentiation preserves the expansion, with smooth coefficient functions in x,s. For Q use b_k=(k+1)l R_u(k)R_m(l)*(m+l+2)/(m-l+1), including l=0 by the zero multiplier. Normalized V,Q are h times sums of smooth coefficient functions and rational weights analytic in h at zero, uniformly for x,s in the compact rectangle. The same is true for A. Euler–Maclaurin to the necessary fixed order applied to each smooth coefficient (also to its first r s derivatives) yields the desired expansions; the accumulated error of h times d+1 summands remains O(h^(N+1)). E/d^3 is h^2 times a similarly analytic rational prefactor times R_u(d); its full endpoint is retained. No smooth extension of the integer d itself is needed.

Set v=V/d^3, b=Q/d^3, a=A/d^3, e=E/d^3. Exactly
C/(q^3 d^5) = h^-1 {3[4+s(3h+h^2)]^2 (a+e)b -32[3+s(h+h^2)] [a+s h^2(v+b)]^2}.
The h^0 coefficient inside braces cancels because (v,b,a,e) has leading (I,I,I/2,0). Taking each normalized observation to one extra order therefore proves the uniform expansion of the complete normalized C to arbitrary fixed order, preserving the coupled cancellation rather than independently discarding subleading terms.

In particular f_d(s)=L(s)+h M(s)+h^2 N(s)+O_{C^1}(h^3) with smooth coefficients (M as in JT; no numerical N needed). JS supplies eventual uniqueness and L'(s_*)>0. Taylor expansion around s_* gives
s_d=s_*+a_1 h+a_2 h^2+O(h^3),
a_1=-M(s_*)/L'(s_*),
a_2=-[N(s_*)+M'(s_*)a_1+L''(s_*)a_1^2/2]/L'(s_*).
Indeed evaluating f_d at this candidate gives O(h^3); the derivative bounded away from zero near s_* and the mean value theorem bound the actual root distance by O(h^3). Invert to conclude q_d=alpha_* d^2+beta_* d+gamma_*+O(1/d). By the same argument an expansion exists to any fixed order. This is qualitative, not an explicit uniform remainder constant or effective d_0.

## 3. Weyl and density-one global separation theorem

For each fixed integers a>=1, b, the sequence q_{a n+b} (ignoring the finite initial range where the unique real root is not defined by JS) is uniformly distributed mod 1. Indeed its difference from the quadratic polynomial alpha_*(an+b)^2+beta_*(an+b)+gamma_* tends to zero, and that polynomial has irrational leading coefficient a^2 alpha_*. Weyl's polynomial equidistribution theorem applies; a perturbation tending to zero preserves uniform distribution by Weyl's criterion. In particular, for 0<=t<=1/2 the natural limiting fraction of d with dist(q_d,Z)<=t is 2t, in every fixed arithmetic progression (relative density within that progression). Exact integer roots are a density-zero set, and the same holds for dist(q_d,Z)<=epsilon_d for any positive epsilon_d tending to zero: bound by the density 2t for arbitrary fixed t>0 and send t to zero.

Stronger: define the global integer residual
g_d = min_{q integer, q>=max(64,ceil(d^2/4))} |C(q,d)|/(q^3 d^3).
For all sufficiently large d the minimum exists and
g_d = (lambda_*+O(1/d)) dist(q_d,Z), lambda_*=s_*^2 L'(s_*)>0 (JT).
Proof: choose fixed small closed s interval about s_* where f_d' is uniformly positive, and bound |f_d| away from zero outside it by JS. Outside the interval the residual d^2 |f_d| tends uniformly to infinity. Inside, |d^2 f_d(s)| >= c |q-q_d| for fixed c>0, since |s-s_d|=d^2 |q-q_d|/(q q_d) and q/d^2, q_d/d^2 are bounded above there. The nearest integer budget is legal for large d since alpha_*>1/4; its residual is bounded by JT. Choose a fixed B large enough that cB exceeds that upper bound. Thus the minimum occurs among the finitely many integers |q-q_d|<=B, and JT gives the two-sided estimate there, including possible exact zeros. This is a uniform estimate over all legal integer budgets, not merely one selected q.

Consequently for 0<=t<=lambda_*/2, limiting proportion of d with g_d<=t is 2t/lambda_*; below zero it is zero and above lambda_*/2 it is one. It holds in each fixed progression as well. In particular liminf g_d=0, limsup g_d=lambda_*/2, and for any positive epsilon_d->0, outside a density-zero exceptional set ALL legal integer q obey |C(q,d)|/(q^3 d^3)>epsilon_d. Taking epsilon_d=d^-A for any fixed A>0 yields density-one inverse-polynomial separation in this normalized residual, and density-one all-budget non-equality for the mother problem. The quantifier is density in d, not density over q. There is no uniform positive constant lower bound for g_d, nor an all-d inverse-polynomial bound from this proof. No transfer to a different normalization of K without its exact denominator.

## 4. Exact identity check and evidence

Executed independently with Python Fraction: 61 coefficients (degrees 0..60) matched in the exact identity after multiplying by 2z. This is a transcription check; analytic integration by parts proves the whole identity.

```python
from fractions import Fraction as F
from math import factorial
def moment(k): return F(2**(k+1)-(-1)**(k+1),k+1)
def P(n): return F((-1)**n,factorial(n)) if n>=0 else F(0)
def M(k,n): return P(n)*moment(k+2*n) if n>=0 else F(0)
def E(c,n): return F((-c)**n,factorial(n)) if n>=0 else F(0)
for n in range(61):
    lhs=2*(-3*M(1,n-1)-3*M(0,n-1)+2*M(3,n-2)-20*M(2,n-2)+14*M(1,n-2)+36*M(0,n-2))
    rhs=72*M(0,n-2)-26*M(0,n-1)+36*E(1,n-1)-E(1,n)+18*E(4,n-1)+E(4,n)
    assert lhs==rhs,(n,lhs,rhs)
print('61 exact rational Taylor coefficients matched (degrees 0..60).')
```

Observed stdout: 61 exact rational Taylor coefficients matched (degrees 0..60).
No independent review or formal checker run. No shared task closure. Prior JR finite exclusion and JP/JQ conditional ranges are unchanged. No new finite range enumeration claimed.

## 5. Next

Find a quantitative irrationality / discrepancy bound or a stronger joint arithmetic obstruction for the exceptional density-zero d; transcendence alone gives neither a power-rate discrepancy nor pointwise integer separation for a polynomial with unknown beta/gamma arithmetic relations. Retain JQ p-adic and JO exact joint certificate routes for exceptional d. The effective uniform remainder and effective uniqueness threshold remain open. Recover the missing JT Activity association from its immutable source; preserve prior JU report as unverified numerical continuation, not as a completed remote artifact.
