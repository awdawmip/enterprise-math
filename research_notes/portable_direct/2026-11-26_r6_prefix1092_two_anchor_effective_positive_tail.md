# PREFIX-1092 — Effective positive-tail reduction to a local sign interval and two exact BRC anchors

2026-11-26 Asia/Shanghai. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / FINITE_EXACT_COMPUTATION / NOT_REVIEWED. R6 independent continuation of PREFIX-1091. Own registration r6-20261123-2358-session-start-own-v1 recovered SUCCEEDED, EM-DIRECT-780BBE / TASK_RESEARCH, RA-0ABD84561C86E53067DB0322. Fresh owner inventory r6-20261126-0251-owner-read SUCCEEDED, LEASED empty as of 2026-11-25T18:52:23.880991Z, Source 859ea23cc674a817937582d8a7298a7122eca3d6. No new CLAIM or shared task mutation.

Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; same Stage46 chart O, incoming -e1, reversal -5 (phase cover 5q), other weights 1, next incoming -d, both orientations Link {O,e1} blocked without renormalization, exactly two negative steps. Full signed/phase-paired X6 Cell/port/ordered multiplicity carrier retained. CT observer correspondence inherited, not new native kernel revalidation. Cutoffs below are analytical auxiliary tests of the BRC observer, not a new native evolution.

Parents:
- dc4a9d5b431c421d921c34b6e4b25fd4ff51b5d3:research_notes/portable_direct/2026-11-26_r6_prefix1091_shifted_quadratic_brackets.md
- 7e8adcd9dac8e9ae5662c71aed1e2211458f12f0:research_notes/portable_direct/2026-11-25_r6_prefix1075_uniform_positive_tail.md
- cc1fa4471149037fc07977d0cc27e532e75a5f61:research_notes/portable_direct/2026-11-25_r6_prefix1073_zero_edge_sharp_positive_tail.md
- e5f4fc3df56133a943b1fd5d1b9784771066b1ea:research_notes/portable_direct/2026-11-25_r6_prefix1082_exact_ct_integer_sign_triangle.md

## 1. New weighted effective distribution norm

Notation D_M(Q)=D(M+8,Q)=L(x^M(1-x)^Q), x=SB/36, E=x d/dx. By 1075, L(f)=c sum_{a=0}^3 CT[K_a (E+8)^a f], c=1/(4*36^8), with K(n)=sum K_a n^a. This CT notation for C^3 radial test functions means the inherited character-average observer. Replace K by its exact axis-exchange symmetrization K2=(K+swap_01 K)/2; all radial tests unchanged, including derivatives of such tests. Parent 1073's exchange cancellation gives minimum u+v=6 for monomials S^u B^v z^a c^b in K2. In that auxiliary observer |S|=6 sqrt(x), |z|=|c|=1, so if L_a is the sum of absolute n^a coefficients times 6^(u+v), then |(K2)_a| <= L_a x^3.

Exact expansion of (E+8)^a in x^j f^(j) has rows (1), (8,1), (64,17,1), (512,217,27,1). Thus
  |L(f)| <= sum_{j=0}^3 C_j sup_{0<=x<=1} |x^(3+j) f^(j)(x)|,
where C_j=c sum_{a>=j} L_a row[a][j].
Executed integer/rational expansion of the frozen 66-term K and 84-term K2:
  L_a(K2) = [64813308862464,45252563632128,11876524425216,1671768834048].
  C_j = [114025897/629856,118208/2187,1637/324,4/27].
Sum C_j=151345441/629856. For comparison, unweighted unsymmetrized norm constants from K are [217841129/279936,4018249/17496,80953/3888,7/12], sum 96041675/93312. The sum of coefficients decreases by about 4.28x; the new bound also keeps x^3. This is a bound on the specified radial observer, not erasure of the joint path state.

## 2. Explicit rational complement certificate

For 0<s<b<1 let chi_{s,b} be 1 on [0,s], zero on [b,1], and 1-p((x-s)/(b-s)) in between, where p(t)=35t^4-84t^5+70t^6-20t^7. p'(t)=140t^3(1-t)^3, derivatives through order 3 match at the endpoints. Its degree-7 Bernstein controls are [0,0,0,0,1,1,1,1]. Differencing these controls gives derivative sup bounds R_i=[1,7,42,420] for i=0,1,2,3 on [0,1], hence |(1-chi)^(i)|<=R_i/(b-s)^i. All these derivatives are zero below s, including the order-zero complement.

Write (n)_h=n(n-1)...(n-h+1) with value 0 if h>n. For nonnegative integers p,q with p+q>0 define
  H(p,q;s)=max_{s<=x<=1} x^p(1-x)^q
          = t^p(1-t)^q, t=max(s,p/(p+q)),
with 0^0=1 for q=0. This follows by differentiation, including the q=0 endpoint. For integer M>=0,Q>=3 define
  e(M,Q;s,b)=sum_{j=0}^3 C_j sum_{i+h+l=j, h<=M}
   j!/(i!h!l!) * R_i/(b-s)^i * (M)_h (Q)_l
   * H(M+3+i+l,Q-l;s).
Leibniz applied to (1-chi)x^M y^Q, followed by the weighted norm of section 1, proves
  |L((1-chi_{s,b})x^M y^Q)| <= e(M,Q;s,b).
All quantities are finite rational numbers. Also e <= J(s,b)(1+M+Q)^3(1-s)^(Q-3), where
  J(s,b)=sum_j C_j sum_{i=0}^j binom(j,i) R_i/(b-s)^i.
Indeed bound x powers by 1, (1-x) by 1-s, and sum the remaining falling powers by (M+Q)^(j-i). This coarser bound is useful for a uniform cone; retain the sharper e for fixed rows.

## 3. Two-anchor positivity transfer

Assume a certified rational delta in (0,1/9) such that g>=0 on (0,delta), where g is the effective ordinary density of 1075. That parent proves existence and strict zero-edge positivity but not an explicit numerical delta. Choose rational 0<s<b<v<w<=delta. Let Q0>=3 and measure mu=chi_{s,b}(x) g(x) y^Q0 dx. It is nonnegative, supported in [0,b]. Integration by parts at zero is justified by 1075, also for these C^3 cutoffs. Compute exact BRC anchors d0=D_0(Q0), d1=D_1(Q0), and e_i=e(i,Q0;s,b). If
  A=d0-e0>0, d1-e1>0,
set a=(d1-e1)/(d0+e0)>0. Then mu([0,b])>=A, its first moment >=d1-e1, and mu([0,b])<=d0+e0. Thus its normalized mean is >=a. By Jensen for integer M>=1 (and directly for M=0), its Mth moment is >=A a^M. Since y>=1-b on support, for t=Q-Q0>=0,
  L(chi_{v,w} x^M y^Q) >= A a^M (1-b)^t.
Proof: chi_{v,w}=1 on support of chi_{s,b}; both integrals involve the same nonnegative g, and y^t>= (1-b)^t there. Therefore
  D_M(Q) >= A a^M (1-b)^(Q-Q0) - e(M,Q;v,w).
This is a finite rational sufficient sign certificate, valid also for Q=Q0. No need to quantify h(0), the positive density coefficient or its Holder remainder once delta is certified. For every valid delta and cutoffs, a search over Q0 eventually succeeds: 1075's g(x)=A0 x^3+O(x^(3+eta)), A0>0, implies d_i asymptotic to A0 Gamma(i+4) Q0^(-i-4) by the beta integral, while e_i decays exponentially times a polynomial. This is a conditional effective reduction of the explicit uniform threshold to one local sign interval, not a numerical proof of that interval.

## 4. Uniform cone and fixed-row certificate without scanning the infinite tail

Put q=(1-v)/(1-b) in (0,1), J=J(v,w). From section 3 and the coarse bound, the adverse-to-positive ratio is <=
  R(M,t)=J(1-v)^(Q0-3)/A * (1+M+Q0+t)^3 * a^(-M) * q^t.
Choose integer L>=1 passing these three rational tests:
  q^L <= a/8;
  q * ((Q0+L+2)/(Q0+L+1))^3 <= 1;
  J(1-v)^(Q0-3)(1+Q0+L)^3 q^L < A.
Then D_M(Q)>0 for all M>=0, Q>=Q0+L(M+1). To prove, write t=L(M+1)+u with u>=0. At M=u=0, R<1 by the third inequality. Incrementing M at fixed u multiplies the polynomial factor by at most 8, because its base >=L+1; exponential factor multiplies by q^L/a. Incrementing u at fixed M multiplies the polynomial factor by at most ((Q0+L+2)/(Q0+L+1))^3, exponential factor by q. Thus R never increases. Such L exists by geometric decay; all tests can be performed with rational powers. The bound is conservative.

For any fixed M a sharper all-Q certificate is available without using the coarse J. If (M+6)/(M+6+Q0-3)<=v, every H in the complement bound e(M,Q;v,w) reaches its maximum at x=v for all Q>=Q0: p<=M+6, q_exponent>=Q0-3. After dividing e by (1-b)^(Q-Q0), the Q-dependent factor in a term with l derivatives on y is proportional to (Q)_l q^Q. For Q>=Q0>=3 the ratio at consecutive integers is q*(Q+1)/(Q+1-l); it is <=1 iff Q+1>=l/(1-q), and decreases with Q. For l=0 its maximum is at Q0; for l>0 it is at Q_l=max(Q0,ceil(l/(1-q))-1) (ties harmless). Consequently the sum of termwise maxima is a finite rational upper bound B_M for e(M,Q;v,w)/(1-b)^(Q-Q0) on all Q>=Q0. Test B_M<A a^M to certify the whole row beyond Q0. This removes the need for an infinite scan or additional Gram moments. Once an actual delta is certified, negativity beyond the proved cone is exactly zero and finite sign scanning plus the existing BRC integer recurrence suffices to recover the full negative mass for each fixed input.

## 5. Executed conditional benchmark (not a certification of delta)

Use hypothetical delta=1/24, s=1/27,b=1/26,v=1/25,w=1/24, Q0=1100. The chosen delta is below the earlier exploratory last-edge estimate near 0.0446, but g>=0 on (0,1/24) remains unproved. No conclusion that this hypothesis holds is drawn from the computation.

Actual exact BRC anchor calculation reused 1082's paired occupancy recurrence, eight shift classes, Nmax=1102,Jmax=1112; all first eight A_m matched the frozen parent. Used integer binomial transform at (M,Q0)=(0,1100),(1,1100), original signed coefficients and full pair occupancy. Exact rational anchor and complement checks passed; decimal displays:
  d0=6.117685319778036e-14, e0=9.617770264163692e-17;
  d1=2.1262540426806964e-16, e1=3.601836523265969e-18;
  A=6.108067549513872e-14, a=0.0034113469608594814.
Digest SHA256 of compact JSON [str(d0),str(d1),str(e0),str(e1)]:
8f0fbba806fa257c6bb826a5b2f62f6c0099525c1e5c023ee0253eda42fa2c72.
Exact tests of section 4 for L=24700 pass (search multiples of 100; not minimal). Thus conditional uniform Q>=1100+24700(M+1).
Fixed-row all-Q B_M/(A a^M) exact comparisons, displayed rounded:
  M=0: 0.00005793302637682033 PASS
  M=1: 0.0006873326169661546 PASS
  M=2: 0.008154488583676085 PASS
  M=3: 0.09674208538754249 PASS
  M=4: 1.1476857987734133 FAIL (sufficient test, not negative witness)
  M=5: 13.615052772155236 FAIL
  M=6: 161.51182481568182 FAIL
  M=7: 1915.922388208702 FAIL
  M=8: 22726.890413234683 FAIL
  M=9: 269581.7996009625 FAIL
  M=10: 3197639.460880547 FAIL
  M=11: 37927719.718232706 FAIL.
Hence conditional on the local sign hypothesis, four entire rows M=0,1,2,3 have strict positivity for every Q>=1100. In particular for the ongoing benchmark (m,r,k)=(0,1,115), U>=985 gives zero negative tail, conditionally; no global sign inference from the finite scan. The Jensen bound degrades for growing M; direct same-M anchor or multiple anchor moments are possible improvements. No independent review, native re-enumeration or classical trig/pi calculation was performed.

## 6. Reproduction

Run PREFIX-1082 section 4 through the generation of A, setting Nmax=1102 (keep Jmax=Nmax+10); do not run its N=1200-specific switch/digest assertions. Assert first eight A_m equal the parent list. Reuse its K, coeff, symbols, comb, factorial, prod, sy and hashlib,json. The following suffix reproduces the new exact results (equivalent to executed calculation):
```python
from fractions import Fraction as F
from math import ceil
from collections import defaultdict
K2=sy.expand((K+K.xreplace({z:1/c,c:1/z}))/2)
co2=defaultdict(lambda:0)
for term in K2.as_ordered_terms():
    p=term.as_powers_dict()
    key=tuple(int(p.get(v,0)) for v in (S,B,z,c))
    co2[key]+=term/(S**key[0]*B**key[1]*z**key[2]*c**key[3])
co2={k:sy.Poly(sy.expand(v),n) for k,v in co2.items() if sy.expand(v)!=0}
assert len(co2)==84 and min(k[0]+k[1] for k in co2)==6
rows=[[1]]
for _ in range(3):
    row=rows[-1]; new=[0]*(len(row)+1)
    for j,vv in enumerate(row):
        new[j]+=(8+j)*vv; new[j+1]+=vv
    rows.append(new)
assert rows==[[1],[8,1],[64,17,1],[512,217,27,1]]
L2=[sum(abs(F(p.nth(a)))*6**(u+v)
        for (u,v,_,_),p in co2.items()) for a in range(4)]
C2=[sum(L2[a]*rows[a][j] for a in range(j,4))/(4*36**8) for j in range(4)]
assert C2==[F(114025897,629856),F(118208,2187),F(1637,324),F(4,27)]
assert A[:8]==[3474227232,83430021744,2013683977632,50005705455360,
    1283772437946144,33996158582646432,924583802183434368,25711602118824644352]
def D(M,Q):
    return F(sum((-1)**j*comb(Q,j)*36**(Q-j)*A[M+j] for j in range(Q+1)),4*36**(8+M+Q))
def mx(p,q,s):
    xx=max(s,F(p,p+q));return xx**p*(1-xx)**q
def fall(n,j):
    return prod(range(n-j+1,n+1)) if n>=j else 0
R=[1,7,42,420]
def err(M,Q,s,b):
    return sum(C2[j]*F(factorial(j),factorial(i)*factorial(h)*factorial(l))
        *R[i]/(b-s)**i*fall(M,h)*fall(Q,l)*mx(M+3+i+l,Q-l,s)
        for j in range(4) for i in range(j+1) for h in range(j-i+1)
        for l in [j-i-h] if M>=h and Q>=l)
s,b,v,w=F(1,27),F(1,26),F(1,25),F(1,24); Q0=1100
d0,d1=D(0,Q0),D(1,Q0); e0,e1=err(0,Q0,s,b),err(1,Q0,s,b)
assert d0>e0 and d1>e1
A0=d0-e0; a=(d1-e1)/(d0+e0); q=(1-v)/(1-b)
J=sum(C2[j]*sum(comb(j,i)*R[i]/(w-v)**i for i in range(j+1)) for j in range(4))
L=24700
assert q**L<=a/8 and q*F(Q0+L+2,Q0+L+1)**3<=1
assert J*(1-v)**(Q0-3)*(1+Q0+L)**3*q**L<A0
for M in range(12):
    assert F(M+6,M+6+Q0-3)<=v
    bound=F(0)
    for j in range(4):
        for i in range(j+1):
            for h in range(j-i+1):
                l=j-i-h
                if h>M:continue
                Qs=max(Q0,ceil(F(l,1-q))-1) if l else Q0
                bound+=C2[j]*F(factorial(j),factorial(i)*factorial(h)*factorial(l))*R[i]/(w-v)**i*fall(M,h)*fall(Qs,l)*v**(M+3+i+l)*(1-v)**(Qs-l)/(1-b)**(Qs-Q0)
    ratio=bound/(A0*a**M)
    assert (ratio<1)==(M<=3)
    print(M,float(ratio),ratio<1)
raw=[str(d0),str(d1),str(e0),str(e1)]
assert hashlib.sha256(json.dumps(raw,separators=(',',':')).encode()).hexdigest()=='8f0fbba806fa257c6bb826a5b2f62f6c0099525c1e5c023ee0253eda42fa2c72'
```

## 7. Next

Prove a quantitative lower-band positivity interval, e.g. test the specific candidate delta=1/24 via validated bounds on the actual six-character weighted pushforward, not a fit to the sign triangle. Any smaller certified delta can be used with fresh rational cutoffs and two anchors. Improve Jensen transfer by choosing M-specific or multiple local moments, reduce the large uniform L, and compare fixed-row sign cutoffs to the actual last crossings. Until local sign interval certified, keep unconditional explicit C, actual p,d and mother B_fix,odd(32) open. The new result is a rigorous conditional reduction, with executable exact rational tests and conditional whole-tail benchmark.
