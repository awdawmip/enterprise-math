# R284IO — Transcendence of the critical inverse response, and reduced-denominator separation
2026-11-26. Author proof, NOT_REVIEWED. Own directed R284 continuation, no shared Task claimed or changed. Registration receipt r1-20261124-0256-r284gd-session-v1 recovered SUCCEEDED, EM-DIRECT-0C386E / RA-B82240E8488EF5A1DA5186C4; current owner inventory r1-20261126-1500-owner-inventory last observed RUNNING. Account entries matched immutable main@2c62810dc8ed326237fe859ccdc728669383e944; Source P000 V5, joint relation/Heartbeat and ACTIVE worldview retained. This is an external arithmetic observer of the safe-word joint counts, not a native spatial/physical attribution.

Frozen scientific inputs:
- IK: edf8d2a631c536cc4f7e9f4c94ed3fa77306c3bd:research_notes/portable_direct/R284IK_CRITICAL_EXCEPTION_EQUIDISTRIBUTION_20261126.md (exact moments and root relation).
- IL: 0ba4281d63293680694a2bb4843b732fd2cf819f:research_notes/portable_direct/R284IL_QUANTITATIVE_JOINT_DIOPHANTINE_SEPARATION_20261126.md (endpoint ratio and integral certificates).
- IN: bc20c5fd1f613eb8926a720dc23db2dfa82095b5:research_notes/portable_direct/R284IN_SHARP_LOG_DISCREPANCY_OBSTRUCTION_20261126.md (general obstruction).
- IH/II/IJ/ID through these pins. The actual integer-budget minimum still depends on ID author-level monotonicity.

## 1. Theorem: actual critical slope is transcendental
For the IH response Phi(s)=112s/9+(16/3)D/I, every positive algebraic s gives transcendental Phi(s). Consequently for every algebraic target lambda, the unique positive solution s_lambda of Phi(s)=lambda is transcendental. In particular s0, z0=s0^2 and A=1/s0^2 are transcendental. This resolves the stronger question left open by IK, which had only proved the disjunction concerning A and B=-2C0/s0^2. The original general discrepancy rate remains IM's; transcendence alone gives no finite irrationality exponent. A is now known irrational without invoking C0.

## 2. Preserve the endpoint state in a rational differential system
IK gives the three retained observations m(s)=int_0^s exp(-x^2-(s-x)^2/2) dx, e=exp(-s^2/2), f=exp(-s^2). Put z=s^2 and
g(t)=t^2+(1-t)^2/2=1/3+(3/2)(t-1/3)^2,
F(z)=int_0^1 exp(-z g(t)) dt, E(z)=exp(-z/2), G(z)=exp(-z).
Then m(s)=s F(s^2). Integration of d/dt[(t-1/3) exp(-z g(t))] yields the exact system
2z F'(z)+(1+2z/3)F(z)=(E(z)+2G(z))/3,
E'=-E/2, G'=-G.
The matrix is rational and its only finite pole is 0. The endpoint terms E and G are retained separately. This is a differential-system representation of the same joint integral, not a change of underlying safe-word model.

The functions F,E,G are E-functions in Siegel's standard sense. For F, write F(z)=sum a_n z^n/n!, a_n=(-1)^n int_0^1 g(t)^n dt. All a_n are rational with |a_n|<=1, because 1/3<=g<=1. For k<=n, the common denominator 2^n lcm(1,...,2n+1) clears a_k, since g^k has coefficients in 2^(-k) Z and degree 2k. This common denominator has exponential growth: for L(m)=lcm(1,...,m), L(2m)/L(m) divides binom(2m,m) (each new prime power in (m,2m] contributes one factor p, and the p-adic factorial valuation at that power contributes one). Dyadic iteration gives L(n)<=16^n. Entireness follows directly from the integral or the series. The displayed finite rational differential system implies a scalar polynomial-coefficient differential equation for each component by linear dependence of successive derivatives over Q(z). The exponentials satisfy the same E-function conditions immediately.

F,E,G are linearly independent even over C(z). For real z>=9, the interval |t-1/3|<=z^(-1/2) lies inside [0,1]. Thus F(z)>=2 exp(-3/2) z^(-1/2) exp(-z/3). In any polynomial linear relation p(z)F(z)+q(z)E(z)+r(z)G(z)=0, if p is nonzero, its term eventually dominates the sum of the other two (exponential gap outweighs all polynomial powers). Hence p=0. Then q=0 by the analogous gap between E and G, and r=0. Clearing rational denominators proves independence.

Invoke F. Beukers, "A refined version of the Siegel-Shidlovskii theorem", Annals of Mathematics 163 (2006), 369–379, Corollary 1.4, page 371, DOI https://doi.org/10.4007/annals.2006.163.369 ; publisher PDF https://annals.math.princeton.edu/wp-content/uploads/annals-v163-n1-p08.pdf (actual corollary inspected). It asserts linear independence over algebraic numbers of E-function values at any nonzero algebraic point ordinary for their common rational system, provided the functions are linearly independent over algebraic rational functions. Here every nonzero algebraic z is ordinary, so F(z),E(z),G(z) are algebraically-coefficient linearly independent. This is a sourced external theorem, not a new proof of Beukers's result.

## 3. Transfer to the actual critical observer and all algebraic targets
IK's exact moment reductions (D=-I') give
I=[(2s^2-3)m+2s e+s f]/9,
D=[(4s^3-18s)m+(4s^2-3)e+(2s^2+3)f]/27.
The 2-by-2 minor of the coefficient matrix of (I,D), in columns (e,f), equals s/27, strictly positive for s>0. Thus their coefficient vectors are linearly independent at every positive s. If s is positive algebraic, z=s^2 is nonzero algebraic and (m,e,f)=(sF(z),E(z),G(z)) are linearly independent over algebraic numbers. If Phi(s)=lambda were algebraic, D+[(7/3)s-(3/16)lambda]I=0 would be a nontrivial linear relation with algebraic coefficients, impossible. Since IH proves strict monotonicity and full real range, all algebraic levels lambda have transcendental inverse. No algebraic root premise is used for existence.

For lambda=0 specifically, the equivalent root is
H(z)=(6z-1)E(z)+(3z+1)G(z)+z(6z-13)F(z)=0.
This is an exact preserved endpoint relation and an alternative short proof: the coefficient vector is nonzero at every z>0. It also gives a one-dimensional high-precision rational evaluator, without recomputing huge true-K counts. Neither s0 nor its square nor its reciprocal can be algebraic; algebraic numbers are closed under taking algebraic roots and inverses.

## 4. Quantitative refinement: polylogarithmically reduced denominators
We also sharpen IL on a restricted but explicit family of simultaneous rational approximations. Let T be a positive integer, p,l nearest integers to TA,TB, eta=max(|TA-p|,|TB-l|). Write p/T=a/r reduced, T=j r, p=j a. For any fixed 0<=theta<1 and fixed c0>0, epsilon>0, for all sufficiently large T with r<=c0(log T)^theta,
eta >= T^[-(1+theta)/(1-theta)-epsilon].
This result is for the actual joint endpoint pair and not for arbitrary pairs satisfying IL. It does not prove a uniform polynomial lower bound for unrestricted r.

Proof: as in IL z'=T/p=r/a and C'=-l/(2p) lie close to the actual (z,C), with |z'-z|+|C'-C|=O(eta/T). The reduced denominator b of t'=z'/2 is <=2a=O(r). In the rational function R(z',C') of IL, the numerator and denominator, after multiplying by j a^3, are integers of size O(j r^3)=O(T r^2): the cubic z' polynomials clear with a^3 and the C' times quadratic terms clear with j a^3. Thus the rational v/d=R(z',C') has d<=O(T r^2)=T^(1+o(1)). The nonzero denominator neighborhood and Lipschitz comparison from IL give |exp(t')-v/d|<=K eta/T. The exponents t' remain in [2/5,3/5].

Reuse IL's positive integral J_n=1/n! int_0^(a'/b) exp(x)x^n(a'-b x)^n dx=U_n exp(t')-V_n with integer U_n,V_n (a'/b is t' reduced). It gives
(b/100)^n/(5 n!) <= J_n <= e(b/4)^n/n!,
|U_n| <= (n+1)2^n b^n (2n)^n.
For fixed delta>0 choose n=ceil((1+delta)log T/((1-theta)log log T)). Since b=O((log T)^theta), n log(n/b)>=(1+delta/2)log T eventually. Hence J_n<1/(2d); U_n nonzero. If U_n v/d-V_n is nonzero it has absolute value >=1/d, and error >=1/(2d |U_n|). If zero, error=J_n/|U_n|. For the latter inverse error, log(|U_n|/J_n)<=2n log n+O(n+log(n+1)) (the b^n factors cancel). For the former, log(2d |U_n|)<=log(2d)+n(log b+log n)+O(n+log(n+1)). Both are <=[2(1+delta)/(1-theta)+o(1)]log T. Taking delta sufficiently small compared to epsilon and absorbing fixed constants gives |exp(t')-v/d|>=T^[-2/(1-theta)-epsilon/2], hence the claimed eta bound with epsilon. For eta/T not in the fixed small neighborhood the inequality is immediate. This proof makes explicit why preserving the reduced denominator r, rather than treating the entire shared denominator T as the exponent denominator, improves the separation resource in this regime. For theta=1/2 the exponent is 3+epsilon. Strong joint resonances with eta<T^(-mu), mu>1, must therefore eventually have r>c0(log T)^theta for each theta<(mu-1)/(mu+1). No statement about unrestricted large primitive denominator or individual irrationality measure of A follows.

## 5. Executed exact checks
Local Python Fraction and SymPy: 46 coefficients via two independent constructions (polynomial integration and differential recurrence), common denominator integrality for each, symbolic endpoint minor and root identity, 110 exact rational bisections with alternating Taylor bounds of order 44/45. Output:
exact coefficient and denominator checks 46
endpoint minor: s/27
z0 enclosure: (93718182334228629862467342690845, 93718182334228629862467342690846, 100000000000000000000000000000000)
A enclosure: (106702880390241057864214614650799, 106702880390241057864214614650800, 100000000000000000000000000000000)
The triples denote (lower numerator,upper numerator,denominator). Their width is 10^(-32). No floating point signs. The universal proof uses Beukers, not numerical evidence. The reduced-denominator estimate uses the analytic bounds from IL, not a finite search. No new true-K evaluation.

Reproduction:
```python
from fractions import Fraction as F
from math import factorial,lcm
import sympy as sp
N=44
an=[F(1)]
for n in range(1,N+2):
    an.append(( ((-F(1,2))**n+2*(-1)**n)/3-F(2*n,3)*an[-1])/(2*n+1))
p=[F(1)];g=[F(1,2),F(-1),F(3,2)];L=1
for n in range(N+2):
    assert an[n]==(-1)**n*sum(v/F(j+1) for j,v in enumerate(p))
    assert 0<(-1)**n*an[n]<=1
    L=lcm(*range(1,2*n+2)); assert (an[n]*2**n*L).denominator==1
    r=[F(0)]*(len(p)+2)
    for j,v in enumerate(p):
        for k,w in enumerate(g):r[j+k]+=v*w
    p=r
print('exact coefficient and denominator checks',N+2)
s,m,e,f=sp.symbols('s m e f');I=(2*e*s+f*s+(2*s*s-3)*m)/9
D=-sp.expand(sp.diff(I,s)+sp.diff(I,m)*(-2*s*m+e+2*f)/3-sp.diff(I,e)*s*e-sp.diff(I,f)*2*s*f)
minor=sp.det(sp.Matrix([[sp.diff(I,e),sp.diff(I,f)],[sp.diff(D,e),sp.diff(D,f)]]))
assert sp.simplify(minor-s/27)==0
assert sp.simplify(9*(D+sp.Rational(7,3)*s*I)-((6*s*s-1)*e+(3*s*s+1)*f+s*(6*s*s-13)*m))==0
print('endpoint minor:',sp.factor(minor))
fac=[factorial(n) for n in range(N+2)]
def bounds(z,coef):
    a=sum(coef[n]*z**n/fac[n] for n in range(N+1)); b=a+coef[N+1]*z**(N+1)/fac[N+1]
    return b,a
ce=[(-F(1,2))**n for n in range(N+2)];cf=[F((-1)**n) for n in range(N+2)]
def H(z):
    pairs=[(6*z-1,bounds(z,ce)),(3*z+1,bounds(z,cf)),(z*(6*z-13),bounds(z,an))]
    lo=hi=F(0)
    for c,(a,b) in pairs:
        lo+=min(c*a,c*b);hi+=max(c*a,c*b)
    return lo,hi
l,h=F(93,100),F(94,100);assert H(l)[1]<0<H(h)[0]
for i in range(110):
    mid=(l+h)/2;a,b=H(mid)
    if b<0:l=mid
    elif a>0:h=mid
    else:raise AssertionError('precision not enough')
def out(l,h,k):
    scale=10**k;a=(l*scale)//1;b=-((-h*scale)//1)
    return a,b,scale
print('z0 enclosure:',out(l,h,32));print('A enclosure:',out(1/h,1/l,32))
assert H(l)[1]<0<H(h)[0]
```

## Next
The reduced-denominator regime is now polynomially separated, and the actual A is proven transcendental. Seek a uniform estimate for near-zero values of the explicit E-function H at rational z (varying denominator), ideally using its low-rank differential system and the simultaneous endpoint relation. Existing non-Liouville results for E-function VALUES at fixed algebraic points do not automatically bound approximation of a transcendental ZERO. Study whether the large primitive denominator branch can exploit the additional independent observation F rather than just IL's exponential relation. Separately obtain explicit uniform true-K fourth-order remainder for sparse fallback. Preserve prior ID proof review pending. No formal Result or Working Truth admission claimed.
