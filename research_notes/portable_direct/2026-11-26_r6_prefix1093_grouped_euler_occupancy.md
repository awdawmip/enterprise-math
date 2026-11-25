# PREFIX-1093 — Linear-step grouped Euler occupancy recurrence and direct row anchors

2026-11-26 Asia/Shanghai. AUTHOR_EXACT_ALGEBRAIC_REDUCTION / FINITE_EXACT_COMPUTATION / NOT_REVIEWED. Independent R6 continuation; original own session registration recovered (MCP-f6d93209fc8e4c5bb2c3b44f69a47174, EM-DIRECT-780BBE, TASK_RESEARCH, RA-0ABD84561C86E53067DB0322). Owner query r6-20261126-0352-owner-read last read RUNNING / NATIVE_RUNNER, error=null; no fresh owner conclusion, no new CLAIM or shared Task state mutation.

Frozen science: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; Stage46 chart O, incoming -e1, reversal -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Full paired six-axis Cell equality, signs, phase, ports and ordered multiplicities preserved. Exact CT observer correspondence inherited; these recurrences calculate that observer, not a new native kernel or time evolution.

Parents:
- e5f4fc3df56133a943b1fd5d1b9784771066b1ea:research_notes/portable_direct/2026-11-25_r6_prefix1082_exact_ct_integer_sign_triangle.md
- 8d25f98107e9602c08ad92e01254d808955431f4:research_notes/portable_direct/2026-11-26_r6_prefix1092_two_anchor_effective_positive_tail.md
- 7e8adcd9dac8e9ae5662c71aed1e2211458f12f0:research_notes/portable_direct/2026-11-25_r6_prefix1075_uniform_positive_tail.md

## 1. New exact linear-step recurrence for the paired occupancy tables

PREFIX-1082 computed each length-N CT table by quadratic sums over the last axis. The new construction replaces all those sums by a constant-size triangular recurrence at each degree.

For an exact shift d=(d_1,...,d_6), let a_i=|d_i|, P=sum d_i^+, Q=sum d_i^-, A=P+Q. Define the formal (not numerically evaluated) series f_i(t)=sum_{l>=0} t^l/[l!(l+a_i)!]. With theta=t d/dt, coefficient comparison gives the exact identity theta^2 f_i=t f_i-a_i theta f_i. It follows just from l(l+a_i)/(l!(l+a_i)!)=1/[(l-1)!(l+a_i-1)!]. No classical trigonometric or alternative propagator calculation is involved.

For I subset of the six indices define U_I=prod_{i in I} theta f_i prod_{i not in I} f_i, and V_I(j)=j!(j+A)![t^j]U_I. The product rule yields

  (j+sum_{i in I}a_i) V_I(j)
    = sum_{i not in I} V_{I+i}(j) + j(j+A) sum_{i in I} V_{I-i}(j-1).

At j=0, V_empty(0)=A!/prod a_i!, all nonempty states zero. For j>=1 compute states in decreasing cardinality; all denominators positive. Every V is an integer: after expansion each summand is the product of the multinomial coefficients j!/prod l_i! and (j+A)!/prod(l_i+a_i)! and prod_{i in I} l_i. Hence the division is exact.

The original PREFIX-1082 paired CT is recovered as

  CT_d(j)=V_empty(j)*(j+P)!(j+Q)!/[j!(j+A)!].

This is exactly the original joint occupation sum, not a probabilistic independence substitution: the formal product is followed by the shared coefficient j and retains every joint occupancy with its exact multiplicity. The signed coefficient of every Laurent monomial remains external and unchanged. Reversals/permutations are only scoped CT equalities.

## 2. Grouping equivalent derivative states

Group equal a_i by value a_g, with r_g axes in group g. A derivative state h=(h_g) records the number of differentiated factors in each group. Since f_i is identical within a group, all subsets with that group profile have exactly the same U and V, not just similar values.

  (j+sum_g a_g h_g) V_h(j)
    = sum_g (r_g-h_g)V_{h+e_g}(j)
      +j(j+A)sum_g h_g V_{h-e_g}(j-1).

Terms with zero coefficient are omitted. Descending total h gives an acyclic within-degree solve. State count is prod_g(r_g+1). For the eight inherited shift classes this gives, in sorted shift order:
  (-3,0,0,0,0,0):12
  (-2,-1,0,0,0,0):20
  (-2,0,0,0,0,0):12
  (-2,0,0,0,0,1):20
  (-1,-1,0,0,0,0):15
  (-1,0,0,0,0,0):12
  (-1,0,0,0,0,1):15
  (0,0,0,0,0,0):7.
Total 113 grouped states across eight tables versus 512 subset states. Per fixed shift, CT table construction needs O(N) arithmetic operations on growing integers (including sequential factorials), versus the inherited quadratic convolution operation count. This is an arithmetic-operation bound, not O(N) bit complexity. Full A construction and the T sign triangle are separate; the latter still needs quadratic work if all entries are wanted. No end-to-end speed comparison against the old implementation claimed.

## 3. Actual exact checks

Executed ungrouped 64-state recurrence, then grouped recurrence through Jmax=2010, Nmax=2000. Every grouped table entry J=0..1260 matched the ungrouped recurrence (8*1261=10088 exact comparisons); 48 direct six-axis occupation sums J=0..5 also matched. All divisions checked exact. First eight A integers matched PREFIX-1082; SHA256 of compact JSON A[0:1201] exactly matched its e35428c11683e8754f384deabbfbc036783a046d2e60bbc99cf1e32488c479c3. Thus the complete earlier 1201-integer input to the sign triangle is reproduced, not just sampled signs. The 1092 d0,d1,e0,e1 digest also matched 8f0fbba806fa257c6bb826a5b2f62f6c0099525c1e5c023ee0253eda42fa2c72. Local extended Python calculation took about 13.1 seconds including SymPy setup, both recurrences, cross-checks, finite sign triangle and anchor tests; no old implementation timing comparison.

## 4. Direct same-row anchor replaces Jensen loss where useful

Retain 1092's local sign hypothesis g>=0 on (0,delta), and rational 0<s<b<v<w<=delta. Let chi be its C^3 cutoff and e its rigorous complement bound. For each fixed M,Q0 define

  A_M=D_M(Q0)-e(M,Q0;s,b).

If A_M>0, the exact local positive integral of chi_{s,b} x^M y^Q0 is >=A_M. On its support y>=1-b, and chi_{v,w}=1. Therefore for all integer Q>=Q0,

  D_M(Q)>=A_M (1-b)^(Q-Q0)-e(M,Q;v,w).

This uses only the same-row anchor, with no Jensen power a^M. The earlier all-Q finite termwise maximum B_M from 1092 applies unchanged whenever (M+6)/(M+6+Q0-3)<=v. Strict B_M<A_M certifies the entire row. If the two-anchor bound A*a^M is available too, use the maximum of it and A_M (each separately valid, including when A_M<=0). Failure of a sufficient test does not assert a negative observation.

Use the same hypothetical delta=1/24, s=1/27,b=1/26,v=1/25,w=1/24. Exact signed T triangle through M+Q<=2000. Direct row tests M=0..40, each Q0 in {1000,1100,1200,1400,1600,1800,1900}. The passing M sets are precisely:
  1000: 0..1
  1100: 0..2
  1200: 0..4
  1400: 0..8
  1600: 0..12
  1800: 0..16
  1900: 0..18.
Thus 19 rows have conditional whole-tail positive certificates at Q>=1900; not a uniform claim for arbitrary M. At Q0=1100 the prior two-anchor certificate covered M=3, which the direct anchor alone did not; retain both methods rather than replace the former universally. This experiment does not establish the local sign hypothesis.

## 5. Exact negative mass conditional on that interval

For (m,r,k)=(0,1,115), the finite exact M=1 row has switches (0,+),(6,-),(123,+) through Q=1900. In the actually scanned Q=0..1900 range the sign is negative exactly 6..122. For the joint observation starting at Q=115, negatives are precisely Q=115..122 in the scanned range. Conditional on delta=1/24, PREFIX-1092 or the same-row test at Q0=1000 certifies all remaining Q. Thus, conditional on this local density sign, the complete negative joint mass is

  N_full = -sum_{Q=115}^{122} D_1(Q)/D_0(115)
         = D_0(123)/D_0(115)-1
         = 0.07423055004043812 (rounded display).
  N_tail(U=7) = -D_1(122)/D_0(115) = 0.0009682364760895871 (rounded display).

The telescoping uses D_1(Q)=D_0(Q)-D_0(Q+1), the exact observer identity. The finite values alone are unconditional finite lower bounds relative to the inherited observer. Exact fraction digest SHA256 compact JSON [str(N_full),str(N_tail(7))] = 383b34fa31bd2a4658a51fc26c77ef8af2269164e3d0f61f018fa35097eff4e2. No claim that delta is already certified.

## 6. Reproduction

Use PREFIX-1082 section 4 from its beginning through the definition of ks and assertion len(ks)==8. Do not run its subsequent old table construction. It supplies K, coeff, canonical, ks, comb, factorial, prod, hashlib,json. Then execute this equivalent suffix (the actual run also recorded local timing):
```python
from itertools import product
from collections import Counter
from fractions import Fraction as F
from math import ceil
import sys
sys.set_int_max_str_digits(0)
def table(d,N,grouped):
    ds=list(map(abs,d)); A=sum(ds); P=sum(max(x,0) for x in d); Q=A-P
    groups=sorted(Counter(ds).items()) if grouped else [(a,1) for a in ds]
    a=[v for v,_ in groups]; r=[v for _,v in groups]
    states=sorted(product(*(range(v+1) for v in r)),key=sum,reverse=True)
    ids={s:i for i,s in enumerate(states)}; zero=ids[tuple(0 for _ in r)]
    up=[]; down=[]; shift=[]
    for s in states:
        up.append([(ids[s[:i]+(s[i]+1,)+s[i+1:]],r[i]-s[i]) for i in range(len(r)) if s[i]<r[i]])
        down.append([(ids[s[:i]+(s[i]-1,)+s[i+1:]],s[i]) for i in range(len(r)) if s[i]])
        shift.append(sum(v*k for v,k in zip(a,s)))
    fac=[factorial(j) for j in range(N+A+1)]
    prev=[0]*len(states); prev[zero]=fac[A]//prod(fac[q] for q in ds)
    out=[fac[P]*fac[Q]//prod(fac[q] for q in ds)]
    for j in range(1,N+1):
        cur=[0]*len(states)
        for m in range(len(states)):
            val=sum(c*cur[k] for k,c in up[m])+j*(j+A)*sum(c*prev[k] for k,c in down[m])
            cur[m],rem=divmod(val,j+shift[m]); assert rem==0
        v,rem=divmod(cur[zero]*fac[j+P]*fac[j+Q],fac[j]*fac[j+A]); assert rem==0
        out.append(v); prev=cur
    return out,len(states)
Nmax=2000; Jmax=Nmax+10; tables={}
for d in sorted(ks):
    vals,nstates=table(d,Jmax,True)
    assert vals[:1261]==table(d,1260,False)[0]
    tables[d]=vals; print(d,nstates)
def comps(j,n):
    if n==1:
        yield (j,); return
    for a in range(j+1):
        for rest in comps(j-a,n-1): yield (a,)+rest
for d in ks:
    pp=[max(x,0) for x in d]; mm=[max(-x,0) for x in d]
    for j in range(6):
        u=j+sum(pp);v=j+sum(mm)
        brute=sum(factorial(u)*factorial(v)//prod(factorial(x+p)*factorial(x+q) for x,p,q in zip(l,pp,mm)) for l in comps(j,6))
        assert brute==tables[d][j]
A=[]
for m in range(Nmax+1):
    val=0
    for (u,v,a,b),pol in coeff.items():
        d=(-a,b,0,0,0,0);j=m+u-sum(max(x,0) for x in d)
        assert j==m+v-sum(max(-x,0) for x in d)
        if j>=0:val+=int(pol.eval(m+8))*tables[canonical(d)][j]
    A.append(val)
digest=lambda obj:hashlib.sha256(json.dumps(obj,separators=(',',':')).encode()).hexdigest()
assert A[:8]==[3474227232,83430021744,2013683977632,50005705455360,1283772437946144,33996158582646432,924583802183434368,25711602118824644352]
assert digest(A[:1201])=='e35428c11683e8754f384deabbfbc036783a046d2e60bbc99cf1e32488c479c3'
C=[F(114025897,629856),F(118208,2187),F(1637,324),F(4,27)]; R=[1,7,42,420]
def fall(n,j):return prod(range(n-j+1,n+1)) if n>=j else 0
def mx(p,q,s):
    xx=max(s,F(p,p+q));return xx**p*(1-xx)**q
def terms(M,s,b):
    for j in range(4):
        for i in range(j+1):
            for h in range(j-i+1):
                l=j-i-h
                if h<=M:
                    yield (C[j]*F(factorial(j),factorial(i)*factorial(h)*factorial(l))*R[i]/(b-s)**i*fall(M,h),M+3+i+l,l)
def err(M,Q,s,b):return sum(co*fall(Q,l)*mx(p,Q-l,s) for co,p,l in terms(M,s,b))
def tailbound(M,Q0,b,v,w):
    if F(M+6,M+6+Q0-3)>v:return None
    q=(1-v)/(1-b);ret=F(0)
    for co,p,l in terms(M,v,w):
        Qs=max(Q0,ceil(F(l,1-q))-1) if l else Q0
        ret+=co*fall(Qs,l)*v**p*(1-v)**(Qs-l)/(1-b)**(Qs-Q0)
    return ret
wanted={1000,1100,1200,1400,1600,1800,1900}; rows={}
cur=A[:]; signrows=[[] for _ in range(41)]; neg=[]
for Q in range(max(wanted)+1):
    for M in range(41):
        sg=(cur[M]>0)-(cur[M]<0)
        if not signrows[M] or signrows[M][-1][1]!=sg:signrows[M].append((Q,sg))
    if Q>=115 and cur[1]<0:neg.append((Q,F(-cur[1],4*36**(9+Q))))
    if Q in wanted:rows[Q]=[F(cur[M],4*36**(8+M+Q)) for M in range(41)]
    cur=[36*cur[i]-cur[i+1] for i in range(len(cur)-1)]
s,b,v,w=F(1,27),F(1,26),F(1,25),F(1,24)
d0,d1=rows[1100][:2];e0,e1=err(0,1100,s,b),err(1,1100,s,b)
assert digest([str(d0),str(d1),str(e0),str(e1)])=='8f0fbba806fa257c6bb826a5b2f62f6c0099525c1e5c023ee0253eda42fa2c72'
limits={1000:1,1100:2,1200:4,1400:8,1600:12,1800:16,1900:18}
for Q,vals in sorted(rows.items()):
    passed=[]
    for M,d in enumerate(vals):
        aa=d-err(M,Q,s,b);bb=tailbound(M,Q,b,v,w)
        if aa>0 and bb is not None and bb<aa:passed.append(M)
    assert passed==list(range(limits[Q]+1));print(Q,passed)
assert [q for q,_ in neg]==list(range(115,123))
assert signrows[1]==[(0,1),(6,-1),(123,1)]
D0115=F(sum((-1)**j*comb(115,j)*36**(115-j)*A[j] for j in range(116)),4*36**123)
fullmass=sum(v for _,v in neg)/D0115; last=neg[-1][1]/D0115
assert digest([str(fullmass),str(last)])=='383b34fa31bd2a4658a51fc26c77ef8af2269164e3d0f61f018fa35097eff4e2'
print(float(fullmass),float(last))
```

The grouped recurrence proof and exact computations are author-checked, no independent review. No classical numeric comparison, native re-enumeration, physical attribution or formal Task closure.

## 7. Next
The main scientific dependency remains an explicit lower-band density sign interval, e.g. delta=1/24. The faster exact occupancy recurrence enables larger targeted moment calculations and potentially a rational differential-equation certificate for the weighted pushforward. A finite sign triangle, even much larger, cannot by itself prove this density interval. Seek certified analytic local bounds or a validated differential representation; compare direct and two-anchor transfer at fixed rows and use the exact mass formula once the hypothesis is discharged. Mother B_fix,odd(32), true boundary p and order d remain open.
