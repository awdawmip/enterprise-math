# PREFIX-1082 — Exact integer CT sign triangle and finite fourth-crossing witnesses

2026-11-25. AUTHOR_EXACT_ALGEBRAIC_REDUCTION / FINITE_EXACT_COMPUTATION / NOT_REVIEWED. Independent continuation of R6; own registration metadata recovered (MCP-f6d93209fc8e4c5bb2c3b44f69a47174; EM-DIRECT-780BBE; RA-0ABD84561C86E53067DB0322, TASK_RESEARCH). Current owner inventory request r6-20261125-1647-owner-read SUCCEEDED, empty LEASED filter as of 2026-11-25T08:48:19.341369Z, Source 4709efbdf55fa7e93b294b600401ffd5c1285e74. No new CLAIM or shared task mutation.

Frozen science: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. Stage46 X6 chart O, incoming -e1, reversal -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Preserve full paired X6 Cell, signed phase, port labels, ordered multiplicity. Scalar CT readout only, not a native spatial coordinate or new propagation kernel.

Parents:
- f4bc55889416ec8d3561a99c89002fafa4f7121a:research_notes/portable_direct/2026-11-25_r6_prefix1081_critical_two_bin_phase.md
- e0f2b98af08e22ba965ccee820c395b7ab776e6c:research_notes/portable_direct/2026-11-25_r6_prefix1072_zero_edge_common_factor.md
- cc1fa4471149037fc07977d0cc27e532e75a5f61:research_notes/portable_direct/2026-11-25_r6_prefix1073_zero_edge_sharp_positive_tail.md
- 7e8adcd9dac8e9ae5662c71aed1e2211458f12f0:research_notes/portable_direct/2026-11-25_r6_prefix1075_uniform_positive_tail.md

## 1. Exact integer observer, not root rounding

Let S=sum z_i, B=sum z_i^-1, z=z_0, c=z_1^-1. Build H_0,H_1 from the inherited compact numerator and define K(n)=H_0 H_0* - H_1 H_1*. Star interchanges S,B and inverts z,c. Expand in the four formal Laurent variables before substituting the six-axis sums. The result has 66 distinct monomials S^u B^v z^a c^b with nonzero integer polynomial coefficients of degree at most 3 in n. All terms have u-v=-a+b, as checked exactly.

Put A_m=CT[K(m+8)(SB)^m]. The parent exact observer gives D_m(0)=A_m/(4*36^(8+m)), with D_m(k)=D(m+8,k). Hence
    T(m,k)=4*36^(8+m+k) D_m(k)
          =sum_(j=0)^k (-1)^j binom(k,j)36^(k-j) A_(m+j).
    T(m,0)=A_m; T(m,k+1)=36 T(m,k)-T(m+1,k).
Every T is an integer, and its sign is the exact sign of the BRC paired observer. In particular the last two bins can be evaluated without an asymptotic crossing, numerical cancellation tolerance, or numerical trigonometry. This is exact integer verification, not a claim of a bounded-precision implementation or measured speedup over native enumeration.

## 2. Six-axis constant-term contraction

For a monomial S^(u+m) B^(v+m) z^a c^b, let d=(-a,b,0,0,0,0). Put d_i^+=max(d_i,0), d_i^-=max(-d_i,0), P=sum d_i^+, Q=sum d_i^- and J=u+m-P=v+m-Q. If J<0 the CT is zero. Otherwise the CT equals
    (J+P)!(J+Q)! sum_(l_1+...+l_6=J, l_i>=0) prod_i 1/[(l_i+d_i^+)!(l_i+d_i^-)!].
Proof: expand the positive and negative multinomials; zero exponent requires their six occupation counts to differ by exactly d. Parametrize the paired occupations by l_i+d_i^+, l_i+d_i^-. Thus joint Cell equality is enforced on every axis and ordered multiplicities are the two multinomial coefficients. No absolute-value projection or port erasure is used.

For a subset of axes with accumulated shifts P,Q, let F(J) be this integer count. Appending one axis with shifts p,q gives
    F_new(J)=sum_(l=0)^J binom(J+P+p,l+p) binom(J+Q+q,l+q) F(J-l).
The base for one zero axis is F(J)=1. Permuting axes and reversing all d preserve this scalar CT count by relabeling the multinomial summation, with the original signed coefficient still attached to its monomial. This equality is scoped to the CT only. There are eight shift classes under this symmetry, all with at least four zero axes. Share the four-zero-axis table and append the two remaining axes. This computes a reusable sequence for each class, then every A_m by 66 evaluations of the cubic polynomials and exact integer arithmetic.

## 3. Executed finite classification

Using N=1200, computed every m,k>=0 with m+k<=1200: 721801 exact signed integer observations. No zero was found in this triangle. The following entries list k where a sign changes, starting with positive at k=0 (all listed rows):
    m=0: 5,101
    m=5: 13,209
    m=8: 18,273
    m=9: 20,294
    m=10: 22,86,90,315
    m=12: 25,91,113,358
    m=15: 30,106,142,422
    m=20: 39,133,187,529
    m=25: 47,161,230,636
    m=30: 55,191,273,743
    m=35: 62,221,316,850
    m=40: 70,252,359,957
    m=45: 78,284,401,1065
    m=46: 80,290,409,1086
    m=47: 81,296,418,1108
    m=48: 83,303,426,1129
    m=49: 84,309,435,1150
    m=50: 86,315,443 (fourth crossing outside or not observed in available window)
    m=100: 160,645,861 (fourth crossing not observed in available window)
Every row m=0..9 has exactly two observed transitions; every row m=10..49 has exactly four in its tested window. Thus at n=18 (m=10) the observed intermediate positive window is exactly k=86..89; its existence is a finite exact sign result independent of asymptotic approximations. The observed fourth recovery moves by 21 or 22 per unit m in the final displayed segment. This suggests a lower-band crossing slope near 21.4 and a corresponding spectral coordinate near 0.0446 as exploratory parameters for future localization, not a certified bound on the limiting p. No global last-negative assertion follows solely from the finite triangle. The asymptotic theorem of PREFIX-1075 is a separate conditional result.

Cross-checks actually executed: eight shift classes x J=0..5, 48 direct six-axis occupation sums against the dynamic recurrence; eight direct binomial-transform sign checks at (m,k)=(0,0),(0,5),(0,100),(10,86),(10,90),(49,1149),(49,1150),(49,1151). All passed. First eight A_m:
    3474227232,83430021744,2013683977632,50005705455360,1283772437946144,33996158582646432,924583802183434368,25711602118824644352.
SHA256 of compact JSON A: e35428c11683e8754f384deabbfbc036783a046d2e60bbc99cf1e32488c479c3
SHA256 of compact JSON switch rows (each row records initial sign and each change): 751ad5624254fde1166a87c0db04db4c9afd5d6c6f2c9ce9dcbedff310a5e387.
The computation uses Python unbounded integers and SymPy exact polynomials. Reproduction below, including evidence checks. No native kernel/path re-enumeration, classical trig/pi numerical reference, independent review or formal checker. The analytic bridge from the original BRC carrier is inherited. The exact finite scan is conditional on that bridge; the integer recurrence and its finite checks are independently reproducible.

## 4. Reproduction

```python
import sympy as sy
from collections import defaultdict
from math import comb, factorial, prod
import hashlib,json
t,S,B,z,c,n=sy.symbols('t S B z c n')
R=1-t*S
def H(j):
    b=1/z; cj=b if j==0 else c; delta=int(j==0)
    U=B-6*R*b-36*t; V=B-6*R*cj-36*t
    W=B-6*R*(b+cj)+36*delta*R**2*b-36*t**2*S
    C0=1-6*R*delta-6*t*z
    N=sy.Poly(sy.expand((1-z*t)*U*V+R*t*(36-11*z*t)*W
       -10*t**2*R**2*C0-390*z*t**3*R**2-390*delta*t**2*R**3),t)
    return sy.expand(sum((n-i-1)*(n-i-2)*N.nth(i)*S**(5-i)
                         for i in range(6)))
def star(h): return h.xreplace({S:B,B:S,z:1/z,c:1/c})
H0,H1=H(0),H(1)
K=sy.expand(H0*star(H0)-H1*star(H1))
coeff=defaultdict(lambda:0)
for term in K.as_ordered_terms():
    powers=term.as_powers_dict()
    key=tuple(int(powers.get(v,0)) for v in (S,B,z,c))
    coeff[key]+=term/(S**key[0]*B**key[1]*z**key[2]*c**key[3])
coeff={k:sy.Poly(sy.expand(v),n) for k,v in coeff.items()
       if sy.expand(v)!=0}
assert len(coeff)==66 and max(v.degree() for v in coeff.values())==3
def canonical(d):
    return min(tuple(sorted(d)),tuple(sorted(-x for x in d)))
ks=set()
for u,v,a,b in coeff:
    assert u-v==-a+b
    ks.add(canonical((-a,b,0,0,0,0)))
assert len(ks)==8
Nmax=1200; Jmax=Nmax+10
BC=[[1] for _ in range(Jmax+5)]
for i in range(1,len(BC)):
    prev=BC[i-1]
    BC[i]=[1]+[prev[j-1]+prev[j] for j in range(1,i)]+[1]
T4=[1]*(Jmax+1)
for _ in range(3):
    T4=[sum(BC[j][l]**2*T4[j-l] for l in range(j+1))
        for j in range(Jmax+1)]
def calc(d):
    d=[x for x in d if x]; T=T4; ap=am=0
    for di in d+[0]*(2-len(d)):
        pp=max(di,0); mm=max(-di,0); ap+=pp; am+=mm
        T=[sum(BC[j+ap][l+pp]*BC[j+am][l+mm]*T[j-l]
               for l in range(j+1)) for j in range(Jmax+1)]
    return T
tables={d:calc(d) for d in ks}
A=[]
for m in range(Nmax+1):
    val=0
    for (u,v,a,b),pol in coeff.items():
        d=(-a,b,0,0,0,0)
        j=m+u-sum(max(x,0) for x in d)
        assert j==m+v-sum(max(-x,0) for x in d)
        if j>=0: val+=int(pol.eval(m+8))*tables[canonical(d)][j]
    A.append(val)
switches=[[] for _ in A]; prev_sign=[None]*len(A); cur=A[:]
for k in range(Nmax+1):
    for m,v in enumerate(cur):
        sg=(v>0)-(v<0)
        if sg!=prev_sign[m]:
            switches[m].append((k,sg));prev_sign[m]=sg
    cur=[36*cur[i]-cur[i+1] for i in range(len(cur)-1)]
def comps(j,n):
    if n==1:
        yield (j,);return
    for a in range(j+1):
        for rest in comps(j-a,n-1): yield (a,)+rest
for d in ks:
    pp=[max(x,0) for x in d]; mm=[max(-x,0) for x in d]
    for j in range(6):
        u=j+sum(pp);v=j+sum(mm)
        brute=sum(factorial(u)*factorial(v)//prod(
            factorial(x+p)*factorial(x+q)
            for x,p,q in zip(l,pp,mm)) for l in comps(j,6))
        assert brute==tables[d][j]
for m,k in [(0,0),(0,5),(0,100),(10,86),(10,90),
            (49,1149),(49,1150),(49,1151)]:
    v=sum((-1)**j*comb(k,j)*36**(k-j)*A[m+j] for j in range(k+1))
    assert ((v>0)-(v<0))==next(sg for pos,sg in reversed(switches[m])
                               if pos<=k)
digest=lambda obj:hashlib.sha256(json.dumps(obj,separators=(',',':')).encode()).hexdigest()
assert digest(A)=='e35428c11683e8754f384deabbfbc036783a046d2e60bbc99cf1e32488c479c3'
assert digest(switches)=='751ad5624254fde1166a87c0db04db4c9afd5d6c6f2c9ce9dcbedff310a5e387'
assert all(s!=0 for row in switches for _,s in row)
print('PREFIX1082_EXACT_CT_TRIANGLE_PASSED', (Nmax+1)*(Nmax+2)//2)
```

## 5. Next

Use exact T(m,k) signs at candidate adjacent terminal positions to certify finite joint negative-mass bins and avoid phase rounding. Extend the integer CT contraction with targeted higher-order evaluation or interval certificates to obtain a genuine p/d bound (the current finite slope is not such a certificate). Compare finite crossings with the predicted asymptotic slopes; the intermediate recovery is still far from its limiting 5m/4 scale in this window, so finite observations cannot replace the parent asymptotic analysis. Explicit uniform positivity constant C and actual global sign-count classification remain open. Mother objective B_fix,odd(32) remains open.
