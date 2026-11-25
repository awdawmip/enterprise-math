# PREFIX-1094 -- Exact rational differential pencil for the paired BRC radial density

2026-11-26. AUTHOR_EXACT_ALGEBRAIC_REDUCTION / FINITE_EXACT_COMPUTATION / NOT_REVIEWED. Independent R6 continuation. Existing own research session metadata at research_session_records/MCP-f6d93209fc8e4c5bb2c3b44f69a47174.json and RA-0ABD84561C86E53067DB0322 (EM-DIRECT-780BBE, TASK_RESEARCH) read back on main. No formal claim or shared task mutation. Current owner read r6-20261126-0458-owner-read last observed RUNNING / NATIVE_RUNNER, error=null; original receipt remains the recovery locator.

Frozen science: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; Stage46 X6 chart O, incoming -e1, reversal -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Preserve the full paired X6 Cell equality, ports, phase, signs and ordered multiplicities through the inherited CT identity. Only the scalar radial observation and its polynomial test functions are represented here, not a native state quotient or evolution. No classical numerical comparison, pi or trigonometric calculation.

Parents:
- f8e95de9568ac9e174179902e12d90f5d6e608a6:research_notes/portable_direct/2026-11-26_r6_prefix1093_grouped_euler_occupancy.md
- e5f4fc3df56133a943b1fd5d1b9784771066b1ea:research_notes/portable_direct/2026-11-25_r6_prefix1082_exact_ct_integer_sign_triangle.md
- 7e8adcd9dac8e9ae5662c71aed1e2211458f12f0:research_notes/portable_direct/2026-11-25_r6_prefix1075_uniform_positive_tail.md

## 1. Moment normalization with an exact weighted pushforward

Write S=sum z_i, B=sum z_i^-1 and R=SB=36x on the auxiliary unit-character carrier of the inherited CT observer. For a nonnegative integer vector b, define the finite (possibly signed/complex) measure mu_b by pushing forward the character weight S^sum(b) prod_i z_i^(-b_i) under R onto [0,36]. Its l-th moment is exactly CT[S^(l+sum b) B^l prod z_i^(-b_i)], the all-positive shift occupation count of PREFIX-1082. These are auxiliary signed weighted measures, not independent marginal probabilities. The moments are real and by compact moment uniqueness so is the measure.

Fix a=abs(d), A=sum a. For derivative subset I with h=|I| and shifted vector b_i=a_i+1_{i in I}, put M_I(l)=mu_b(R^l). The formal series identity theta f_a=t f_(a+1) follows directly from factorial coefficients. Hence the grouped Euler recurrence of PREFIX-1093, after the exact normalization W_I(j)=V_I(j)/(j falling h) for j>=h, gives W_I(j)=M_I(j-h). This uses factorial cancellation, not approximation. Set W_I(j)=0 for j<h. For l>=0, translating j=l+h gives

 (l+h+sum_{i in I}a_i) M_I(l)
   = l sum_{i notin I} M_(I+i)(l-1)
     +(l+h+A) sum_{i in I} M_(I-i)(l).

Terms with zero coefficient are omitted, including l=0 in the first sum. For l=h=0 the identity is 0=0. This follows also by substituting theta f_a=t f_(a+1) in the parent recurrence; explicitly, the up ratio of falling factorials is j-h and the down ratio including j(j+A) is j+A. Every M is the exact integer paired occupation count.

Group identical a_i with multiplicities r_g and let h=(h_g), H=diag(sum h_g), J=diag(sum a_g h_g). Define U_{h,h+e_g}=r_g-h_g and D_{h,h-e_g}=h_g; all other entries zero. M(l) is the column of grouped moments. Then

 (l I+H+J) M(l)=l U M(l-1)+(l I+H+A I)D M(l).

## 2. Exact density differential system, no numerical inversion

Let E=-d/dR (R *), the distributional moment operator: (E mu)(R^l)=l mu(R^l). Let mu be the column of mu_b measures, indexed by h. Distributional differentiation is denoted by a prime. By the moment identity,

 (E+H+J)mu = -U mu' +(E+H+A I)D mu.

The identity holds as compactly supported distributions, not just in finitely many moments: a compactly supported distribution with every polynomial moment zero has an entire Fourier transform whose Taylor series at zero vanishes, hence is zero. Rearranging yields the rational matrix pencil

 [R(I-D)-U] mu' = [H+J-I+(I-A I-H)D] mu.                  (1)

In particular no Cauchy boundary limit or numerical reconstruction is needed for this derivation. On every real interval where the pencil is invertible, the measures are analytic densities: solve the analytic fundamental matrix system locally, multiply the distributional solution by its inverse, and obtain a distribution with derivative zero. This establishes regularity and the exact rational ODE on that interval.

## 3. Determinant and singular locations

Let N=prod_g(r_g+1). For R>0 conjugate the pencil by diag(R^(h/2)); it becomes R I-sqrt(R)(U+D). This is an algebraic similarity to determine a polynomial determinant, not a numerical or physical computation. Each group matrix U_g+D_g is the action of u d/dv+v d/du on symmetric homogeneous polynomials of degree r_g (or the equivalent transpose on value vectors), with eigenvalues r_g-2j, j=0..r_g, by changing polynomial variables to u+v,u-v. The sum on the tensor product has eigenvalues 6-2k with multiplicities m_k=[t^k]prod_g(1+t+...+t^r_g). Since m_k=m_(6-k), pair the nonzero eigenvalues. As a polynomial identity,

 det[R(I-D)-U] = R^(m_0+m_1+m_2+m_3)
                 (R-36)^m_0 (R-16)^m_1 (R-4)^m_2.

All eight parent shift classes have only four possible grouped multiplicity profiles, with determinants:
- r=(5,1): N=12, R^7 (R-36)(R-16)^2(R-4)^2.
- r=(4,1,1): N=20, R^12 (R-36)(R-16)^3(R-4)^4.
- r=(4,2): N=15, R^9 (R-36)(R-16)^2(R-4)^3.
- r=(6): N=7, R^4 (R-36)(R-16)(R-4).

Thus the ODE has no possible finite real singularity in the open lower band 0<x<1/9, including the target 0<x<=1/24. The possible singularities of the pencil are x=0,1/9,4/9,1. This is not a claim about nonremovable singularities of each scalar solution or the sign of the density.

## 4. Mixed shifts and a compact system for the actual signed residual

For the original signed shift d define mu_d by the weight S^P B^Q prod z_i^(-d_i), P=sum d_i^+, Q=sum d_i^-, A=P+Q. Its l-th moment is the original exact CT count. The parent factorial identity gives

 mu_d(R^l) = [prod_{i=1}^P(l+i)/(l+Q+i)] mu_abs(d)(R^l).

Signed reversal and permutation are exact for these scoped radial moments, hence for these compact measures. In the eight classes of PREFIX-1082 the only mixed cases, after reversal if needed, have P=1 and Q=1 or 2. Thus (E+Q+1)mu_d=(E+1)mu_a. Introduce the finite signed measure

 nu_Q = integral_0^1 t^Q (dilation_t)_* mu_a dt.

Its moments are mu_a(R^l)/(l+Q+1). Consequently mu_d=mu_a-Q nu_Q by compact moment uniqueness. On a regular interval R>0 the auxiliary density satisfies

 R nu_Q'=Q nu_Q-mu_a,

and wherever densities exist its integral representation is nu_Q(R)=R^Q integral_R^36 mu_a(s) s^(-Q-1) ds (interpret the integral against the measure if necessary). The dilation formula fixes the integration constant globally; the local ODE alone does not. The six distinct absolute shift classes have 78 grouped states, with two additional mixed-shift auxiliary states: an explicit block realization of at most 80 scalar functions, rather than 113 grouped states plus mixed corrections. Some functions coincide across blocks; 35 distinct nonnegative shifted b profiles were counted, but a closed invertible 35-state pencil has not been constructed.

Let p_{u,v,a,b}(n) be the integer polynomials in the 66-term K(n) of PREFIX-1082. Here a,b in the subscript are Laurent exponents, not the absolute shift vector. For each term set d=(-a,b,0,0,0,0), j0=u-P=v-Q. Exact expansion of the parent code gives 2<=j0<=6. Hence define the compact distribution

 lambda = 1/(4*36^8) sum_{terms} p_{u,v,a,b}(E+8) [R^j0 mu_d].

Its m-th normalized moment is exactly D_m(0) because E acting on a polynomial moment returns m, and binomial linearity gives D_m(k)=lambda[(R/36)^m(1-R/36)^k] for every nonnegative integer m,k. In regular intervals the effective ordinary x-density g(x)=36 lambda(36x) is obtained by the same differential expression on densities. It is analytic there, and can be computed as a rational linear readout of the 80-state ODE by using (1) to eliminate its finitely many derivatives. No original path, sign, phase or multiplicity is replaced; this is an exact observer realization for all polynomial radial tests.

## 5. Actual exact verification

Local Python/SymPy calculation: eight inherited shifts, all 113 grouped states, l=0..5; 678 component equalities of the translated moment recurrence, 48 mixed-orientation moment-ratio checks (including pure cases), eight exact characteristic polynomial identities and 64 determinant evaluations at R=1,2,4,9,16,25,36,49, all passed. Parent 66-term symbolic expansion separately checked: shift offset range 2..6 and mixed (min(P,Q),max(P,Q)) pairs exactly (1,1),(1,2). Unique shifted b profiles across the six blocks: 35 (78 total block entries). No ODE integration, interval sign certificate, formal checker or independent review executed.

Reproduction (uses exact integers and symbolic matrix operations; CT from parent paired occupation law):
```python
from collections import Counter
from itertools import product
from math import factorial,prod
import sympy as sy
import hashlib,json
shifts=[(-3,0,0,0,0,0),(-2,-1,0,0,0,0),(-2,0,0,0,0,0),(-2,0,0,0,0,1),(-1,-1,0,0,0,0),(-1,0,0,0,0,0),(-1,0,0,0,0,1),(0,0,0,0,0,0)]
def comps(l,n):
    if n==1:
        yield (l,);return
    for a in range(l+1):
        for rest in comps(l-a,n-1):yield (a,)+rest
def ct(d,l):
    p=[max(a,0) for a in d];q=[max(-a,0) for a in d]
    return sum(factorial(l+sum(p))*factorial(l+sum(q))//prod(factorial(v+i)*factorial(v+j) for v,i,j in zip(c,p,q)) for c in comps(l,6))
R=sy.symbols('R'); checks=0; ratios=0; det_checks=0; evidence=[]
for d in shifts:
    groups=sorted(Counter(map(abs,d)).items()); a=[v for v,_ in groups];r=[n for _,n in groups];A=sum(map(abs,d))
    states=list(product(*(range(n+1) for n in r))); ix={h:i for i,h in enumerate(states)}; n=len(states)
    U=sy.zeros(n);D=sy.zeros(n);H=sy.diag(*map(sum,states));J=sy.diag(*(sum(v*k for v,k in zip(a,h)) for h in states))
    M={}
    for h in states:
        i=ix[h]
        for g in range(len(r)):
            if h[g]<r[g]:U[i,ix[h[:g]+(h[g]+1,)+h[g+1:]]]=r[g]-h[g]
            if h[g]:D[i,ix[h[:g]+(h[g]-1,)+h[g+1:]]]=h[g]
        b=tuple(x for v,k,t in zip(a,h,r) for x in [v+1]*k+[v]*(t-k))
        M[h]=[ct(b,l) for l in range(6)]
    for l in range(6):
        V=sy.Matrix([M[h][l] for h in states]); prev=sy.Matrix([M[h][l-1] if l else 0 for h in states]);I=sy.eye(n)
        assert (l*I+H+J)*V==l*U*prev+(l*I+H+A*I)*D*V
        checks+=n
    P=sum(max(v,0) for v in d);Q=sum(max(-v,0) for v in d)
    for l in range(6):
        assert ct(d,l)*prod(l+Q+i for i in range(1,P+1))==M[states[0]][l]*prod(l+i for i in range(1,P+1))
        ratios+=1
    mult=Counter(map(sum,states)); target=prod((R-(6-2*k))**v for k,v in mult.items())
    assert sy.expand((U+D).charpoly(R).as_expr()-target)==0
    det=R**(sum(mult[k] for k in range(4)))*prod((R-(6-2*k)**2)**mult[k] for k in range(3))
    for x in [1,2,4,9,16,25,36,49]:
        assert (x*(I-D)-U).det()==det.subs(R,x)
        det_checks+=1
    evidence.append([d,n,[mult[k] for k in range(7)],str(sy.factor(det))])
assert (checks,ratios,det_checks)==(678,48,64)
assert hashlib.sha256(json.dumps(evidence,separators=(',',':')).encode()).hexdigest()=='5bea3ed5ce8a7beed2670b28bc2e31fb68b9779d2a899923d9fcc0dec890f26c'
print(evidence)
# Reuse PREFIX-1082 section 4 through coeff definition for offset check:
# js=[]; mixed=set()
# for u,v,a,b in coeff:
#     d=(-a,b,0,0,0,0); P=sum(max(i,0) for i in d);Q=sum(max(-i,0) for i in d)
#     assert u-P==v-Q;js.append(u-P)
#     if P and Q:mixed.add(tuple(sorted((P,Q))))
# assert (len(coeff),min(js),max(js),mixed)==(66,2,6,{(1,1),(1,2)})
```

## 6. Next

The central missing step is a rigorously anchored local solution of the pencil, with error bounds near its singular endpoint R=0, and an enclosure for the actual signed readout over 0<R<=3/2. The inherited positive leading term of PREFIX-1075 is existential, not an explicit starting enclosure. Derive a regular-singular gauge or a direct moment-to-density interval anchor; then propagate rational enclosures away from zero and certify g>=0 to R=3/2 if true. This would discharge the exact hypothesis needed for PREFIX-1092/1093 complete negative mass, rather than merely scanning farther. Current result does not discharge it. Mother B_fix,odd(32), p and d remain open. No new formal Task, claim, Result, acceptance or physical attribution.
