# R284JS — Uniform scaling limit, eventual unique real root, and asymptotic budget localization

2026-11-27. Author proof and exact checks, NOT_REVIEWED. Own researcher EM-DIRECT-0C386E / TASK_RESEARCH; existing session recovery via approved custody succeeded (own metadata; no formal runs or claim authority). Current owner query r1-20261127-2055-leased was RUNNING at last observation. No shared task acquired or mutated. Global entry blobs verified at main@17c936b17643e4c8cbdaa361ec22bbcd805d68ee. Current portable continuation, P000 V4/V5, ACTIVE worldview, joint/residual constraints and research method consulted. This is ordinary auxiliary asymptotic analysis of the exact arithmetic observer, not a native spatial or physical bridge.

Frozen scientific source: 88211c0912397b00536b6c4d6427cab29d4499f2:research_notes/portable_direct/R284JR_GLOBAL_BUDGET_POLYNOMIAL_AND_INTEGER_ROOT_EXCLUSION_20261127.md, including its full endpoint E. JR's finite d<=80 all-integer theorem remains unchanged. The present result addresses uniform large-d real-root structure, not integer exclusion.

## 1. Exact joint scaling coordinates

Use JR definitions q>=64, d>=3, d^2<=4q, u=q+d, m=2q+d, l=d-k, R_n(k)=prod_{i=0}^{k-1}(n-i)/(n+i+3).
a_k=(k+1)(l+1) R_u(k)R_m(l);
b_k=(k+1)l R_u(k)R_m(l-1) (0 at l=0).
V=sum a_k, Q=sum b_k,
A=sum [(u-k)(u+k+2)/(2u(2u+1))](a_k+b_k),
E=R_u(d)(u-d)(2d+3)(m+2)/(2(2u+1)(4m+2)), W=A+E, Z=qA+Q+V.
C=3q(4q+3d+1)^2 WQ-32(3q+d+1)Z^2.
As in JR, target equality implies C=0.

Let s=d^2/q in (0,4], x=k/d, y=1-x, phi(x)=x^2+y^2/2. Define
I(s)=int_0^1 xy exp(-s phi(x)) dx,
J(s)=int_0^1 x(1-s y^2) exp(-s phi(x)) dx.
For fixed d, normalized observables extend smoothly to s=0 by taking q to infinity; all asymptotic error statements below are uniform in C^1([0,4]) as d tends to infinity. The derivative is with respect to s; O_C1 means sup norm plus sup first derivative.

**Theorem A (full joint limit).**
C(q,d)/(q^3 d^5) = L(s)+O_C1(d^-1),
where L(s)=28s I(s)^2-12 I(s)J(s).

Proof: for R_u(k), use the exact product of [1+s(d-i)/d^2]/[1+s(d+i+3)/d^2]. Its log is the sum of -s(2i+3)/d^2 plus O_C1(d^-2) per factor, by elementary log expansion on a uniform small interval for large d. Summing at most d factors gives log R_u(k)=-s x^2+O_C1(d^-1). Likewise log R_m(l)=-s y^2/2+O_C1(d^-1), replacing s by s/2 in the factors. Exponentiating preserves the error in C^1 uniformly in k. All factors are positive for legal real q. The integrands and their first s derivatives have uniformly bounded x derivatives on the compact rectangle. Riemann sums yield V/d^3=I+O_C1(d^-1).

Crucially, subtract the joint weights exactly before estimating:
a_k-b_k=(k+1) R_u(k)R_m(l) [1-l(2l+1)/(m-l+1)].
This also holds at l=0; it follows from the ratio R_m(l-1)/R_m(l)=(m+l+2)/(m-l+1) for l>=1. Since l(2l+1)/(m-l+1)=s y^2+O_C1(d^-1), we get (V-Q)/d^2=J+O_C1(d^-1), hence Q/d^3=I+O_C1(d^-1).

The A weight differs from 1/4 by [3u/2-k(k+2)]/[2u(2u+1)] = O_C1(d^-2). Thus A=(V+Q)/4+O_C1(d), A/d^3=I/2+O_C1(d^-1), and Q-2A=-(V-Q)/2+O_C1(d). E=O_C1(d): after substituting q=d^2/s its rational prefactors have bounded C^1 norm after removing the explicit factor (2d+3); the R factor already has bounded C^1 norm. Also (V+Q)/q=O_C1(d).
In the exact expression
C/q^3=3(4+(3d+1)/q)^2 WQ-32(3+(d+1)/q)(A+(Q+V)/q)^2,
the two prefactors are 48+72s/d+O_C1(d^-2), and 96+32s/d+O_C1(d^-2), respectively.
The leading cancellation is 48 A(Q-2A)=-12d^5 I J+O_C1(d^4). Replacing W by A and the second squared observer by A^2 costs O_C1(d^4), because the omitted E and (Q+V)/q are O_C1(d). The first-order prefactors contribute (36-8)s d^5 I^2+O_C1(d^4). This proves the theorem. All error estimates retain the joint difference before approximating; independent leading approximations to V and Q alone would not determine L.

## 2. Uniqueness and simple crossing of the scaling limit

Put alpha=1/s>0, define probability measure with density xy exp(-phi/alpha)/I(1/alpha), and expectation E_alpha. Then
R(alpha)=alpha J(1/alpha)/I(1/alpha)=alpha E_alpha[1/y]-E_alpha[y].
The endpoint singularity of 1/y is integrable since the density contains y. Differentiation under the integral on compact positive alpha intervals is valid.
L(s)=12s I(s)^2(7/3-R(1/s)) for s>0; L(0)=-1 since I(0)=1/6 and J(0)=1/2.

Claim 1: E_alpha[1/y]<3 and E_alpha[y]>=1/2 for all alpha>0.
For the first, integrate x(3x-2) exp(-phi/alpha). Its unweighted integral is zero; phi<=1/2 on [0,2/3] and phi>=1/2 on [2/3,1], so multiplication by the exponential makes the negative contribution strictly larger in magnitude than the positive contribution (compare with exp(-1/(2alpha))). Thus 3I>int x exp(-phi/alpha). For the second, pair x and 1-x: phi(x)-phi(1-x)=x-1/2, and xy is symmetric, so x<1/2 has greater density than its reflected point. Hence E_alpha[y]>1/2.

It follows that R(alpha)<3alpha-1/2, in particular R<7/3 on alpha<=17/18.
Claim 2: R is strictly increasing on [17/18,infinity).
For g=1/y, the derivative rule is dE_alpha[f]/dalpha=Cov_alpha(f,phi)/alpha^2.
Since 1/3<=phi<=1, Cov(g,phi)>=-(2/3)E[g]. For bounded y and phi, Cauchy-Schwarz and the elementary range variance bound give |Cov(y,phi)|<=1/6. Thus
R'(alpha)>=E[g](1-2/(3alpha))-1/(6alpha^2)
>=1-2/(3alpha)-1/(6alpha^2)>0 on alpha>=17/18 (the right side is increasing and positive at 17/18).
Finally R(alpha)>=alpha-1 tends to infinity. Therefore there exists a unique alpha_*>17/18 with R(alpha_*)=7/3; the crossing is simple. The exact rational enclosure below puts alpha_* in (1.06702880,1.06702881).

Consequently L has precisely one zero s_*=1/alpha_* in [0,4], negative for s<s_*, positive for s>s_*, and L'(s_*)>0 (differentiate the factorized formula). 

## 3. Uniform eventual uniqueness of the original real root

**Theorem B.** There exists an integer d_0 such that for every integer d>=d_0 the original C has exactly one real zero q_d on the legal real interval q>=d^2/4 (which then implies q>=64). It is simple, with C positive below it and negative above it. Moreover
q_d=alpha_* d^2+O(d).

Proof: choose a closed small interval about s_* inside (0,4) on which L'>c>0. On the compact complement L is bounded strictly away from zero; its signs at the two endpoints of the small interval are opposite. By Theorem A uniform C^1 convergence, for all sufficiently large d the normalized C has the same signs outside this interval and strictly positive derivative inside. It has precisely one simple zero s_d there. By the mean value theorem and Theorem A, |s_d-s_*|=O(1/d); inversion on an interval bounded away from zero gives q_d=alpha_* d^2+O(d). The prefactor q^3 d^5 is positive, so normalized signs transfer to C. The proof is qualitative in d_0; no explicit d_0 or O(d) constant is claimed here. It covers all legal real budgets, even q/d^2 unbounded, through compact s=0. No integer-root exclusion for large d follows from this alone.

## 4. Rigorous enclosure of alpha_* and exact sign examples

For alpha>=1, write F(alpha)=7I-3alpha U+3B, U=int x exp(-phi/alpha), B=int xy^2 exp(-phi/alpha); here I=I(1/alpha). F=I(7-3R), so its sign detects the crossing. For 0<=phi/alpha<=1, the degree 17 and 18 alternating Taylor polynomials bound the exponential below and above. Integrate each against the nonnegative polynomial weights x, xy, xy^2 with rational arithmetic. The actual outward bounds in units 10^-14 are [383424,383425] at alpha=1.06702880, and [-599109,-599108] at alpha=1.06702881. Thus the displayed enclosure is rigorous.

Additional exact integer signs from the JR joint carrier (not floating-point root finding) yield opposite-sign adjacent budgets:
d=80: (6464,6465); d=100: (10217,10218); d=200: (41787,41788); d=500: (264542,264543); d=1000: (1062611,1062612).
At each lower endpoint C>0, at each upper C<0. These are sign-crossing brackets only for individual d>80, not a finite global uniqueness or exclusion certificate. Qualitative Theorem B does not specify whether its threshold is below those samples. The lower endpoints' empirical correction (q-alpha_*d^2)/d tends toward roughly -4.4 in these five samples; no second-order coefficient is claimed.

Executed reproducible Python, exact arithmetic for both the enclosure and sign brackets:
```python
from fractions import Fraction as F
from math import factorial, prod

def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b): c[i+j]+=u*v
    return c

def integrate(a): return sum((v/F(i+1) for i,v in enumerate(a)), F(0))
def interval(alpha,w,N=18):
    assert N%2==0 and alpha>=1
    p=[F(1,2)/alpha,-1/alpha,F(3,2)/alpha]; power=[F(1)]; s=F(0)
    for k in range(N+1):
        v=integrate(mul(w,power))/factorial(k)
        if k%2: s-=v
        else: s+=v
        if k==N-1: lower=s
        power=mul(power,p)
    return lower,s

def bounds(a):
    I=interval(a,[0,1,-1]); U=interval(a,[0,1]); B=interval(a,[0,1,-2,1])
    return 7*I[0]-3*a*U[1]+3*B[0],7*I[1]-3*a*U[0]+3*B[1]
lo=F(106702880,100000000);hi=F(106702881,100000000)
b1,b2=bounds(lo),bounds(hi)
assert b1[0]>0 and b2[1]<0
for a,b in [b1,b2]: print(a*10**14//1, -((-b*10**14)//1))

def sign(q,d):
    u=q+d;m=2*q+d
    def scaled(n):
        v=prod(n+i+3 for i in range(d)); a=[v]
        for k in range(d):
            v,rem=divmod(v*(n-k),n+k+3);assert rem==0;a.append(v)
        return a[0],a
    Du,U=scaled(u);Dm,M=scaled(m);V=Q=A=0
    for k in range(d+1):
        l=d-k; a=(k+1)*(l+1)*U[k]*M[l];b=(k+1)*l*U[k]*M[l-1] if l else 0
        V+=a;Q+=b;A+=(u-k)*(u+k+2)*(a+b)
    J=2*u*(2*u+1); L=4*m+2
    W=L*A+u*U[d]*Dm*(u-d)*(2*d+3)*(m+2);Qn=J*L*Q;Zn=L*(q*A+J*(Q+V))
    P=3*q*(4*q+3*d+1)**2*W*Qn-32*(3*q+d+1)*Zn**2
    return (P>0)-(P<0)
for d in [80,100,200,500,1000]:
    l=d*d//4;h=2*d*d
    assert sign(l,d)==1 and sign(h,d)==-1
    while h-l>1:
        q=(l+h)//2;v=sign(q,d);assert v
        if v>0:l=q
        else:h=q
    assert sign(l,d)==1 and sign(h,d)==-1
    print(d,l,h)
```

## 5. Next question

Develop the order d^-1 correction in the normalized joint limit (requires first correction of V-Q, not just independent observer estimates) and obtain an explicit effective d_0 via controlled derivative/error constants. Then combine real-root localization with exact integer/p-adic certification. A bounded leading coefficient interval and O(d) root error do not imply any integer separation; a uniform inverse-polynomial gap remains open. Do not extend JR's d<=80 integer theorem to d>80 based solely on the five crossing samples. No formal Result, task closure, independent review or new native Foundation claim.
