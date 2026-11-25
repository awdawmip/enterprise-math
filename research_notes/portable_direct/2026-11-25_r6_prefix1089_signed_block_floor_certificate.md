# PREFIX-1089 -- Exact signed-block lower certificate for the global envelope floor

2026-11-25. AUTHOR_CONDITIONAL_ALGEBRAIC_PROOF / FINITE_EXACT_COMPUTATION / NOT_REVIEWED. Independent R6 continuation. Original own registration r6-20261123-2358-session-start-own-v1 recovered SUCCEEDED; EM-DIRECT-780BBE / TASK_RESEARCH, RA-0ABD84561C86E53067DB0322. Owner request r6-20261125-2352-owner-read last observed RUNNING during derivation; no new CLAIM or shared Task mutation.

Frozen science: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; Stage46 X6 chart O, incoming -e1, reversal -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Preserve full signed phase-paired Cell/port/ordered multiplicity carrier. The CT observer and auxiliary character variables do not replace native geometry or native dynamics. Correspondence inherited, not newly independently verified.

Parents:
- d1fa22a25dd88794463f6a47c9903f7ebdd62f81:research_notes/portable_direct/2026-11-25_r6_prefix1088_low_order_shared_gram_benchmark.md
- 2f3bf251ebcd76aa5cbcae50f47c9fe3a861d010:research_notes/portable_direct/2026-11-25_r6_prefix1087_divergence_completeness_and_envelope_floor.md
- 508dd49782d0203dbcf0e7891fa01484da5be5ef:research_notes/portable_direct/2026-11-25_r6_prefix1085_quadratic_orbit_tail_certificate.md
- e5f4fc3df56133a943b1fd5d1b9784771066b1ea:research_notes/portable_direct/2026-11-25_r6_prefix1082_exact_ct_integer_sign_triangle.md
- ba684dc121d63bef952982f17c35aee8e356475b:research_notes/portable_direct/2026-11-25_r6_prefix1084_newton_global_tail_certificate.md

## 1. A cheap certified lower bound on the remaining possible Gram improvement

Use parent scope m>=0,r>=1,k>=3,U>=7, M=m+r, D_m(k)>0. Q=k+u, x=SB/36, y=1-x, w_Q=x^(M+2)y^(Q-3), c_u=binom(u+r-1,r-1), c=1/(8*36^6). Define positive b_u=c_u CT[w_Q], signed normalized f_u=c_u D_M(Q)/D_m(k), and tails B(t)=sum_(u>=t)b_u and S(t)=sum_(u>=t)f_u. The parent finite tail identities compute both exactly; B(t)=L(1,M+2,k-3,r,t), S(t) from PREFIX-1084. Write B=B(U).

For any auxiliary carrier G_Q with the same exact bin CT as F_Q, including arbitrary bin-dependent null controls, its normalized single-envelope square satisfies
    A(G)^2 = B * sum_u c_u CT[w_Q (c G_Q/D_m(k))^2]
           >= B * sum_u f_u^2/b_u = F_*^2.
The inequality is binwise Cauchy-Schwarz; parent completeness identifies F_* as the infimum for independent bin-local controls, but the lower bound itself requires no completeness theorem. It also holds for the more restricted shared Gram families. All masses are finite by the parent norm estimates.

For finite cutpoints U=t_0<t_1<...<t_l, with a final infinite block, set
    L(P)^2 = B*[sum_(i<l) (S(t_i)-S(t_(i+1)))^2/(B(t_i)-B(t_(i+1)))
                              + S(t_l)^2/B(t_l)].
Then |S(U)| <= L(P) <= F_* <= A(G).
Proof: apply weighted Cauchy-Schwarz to f_u/sqrt(b_u) and sqrt(b_u) separately in each block. The finite tail identities provide the block numerator and denominator, without Gram cross products or individually scanning the block. All denominators are strictly positive by positive radial weights. The exact rational L(P)^2 can be compared without computing a square root.

The lower bound is monotone under refinement. If a block of mass B1+B2 and signed sum S1+S2 is split, the gain in L(P)^2 is exactly
    B * B1*B2/(B1+B2) * (S1/B1-S2/B2)^2.
Expansion proves the identity. It quantifies the between-block variation in signed means, even when signs differ. For singleton blocks through a growing cutoff T and one infinite remainder, L(P)^2 tends to F_*^2: the singleton sum tends monotonically to sum f_u^2/b_u, and S(T)^2/B(T) <= sum_(u>=T) f_u^2/b_u tends to zero. Thus these are convergent lower certificates, not merely asymptotic guesses.

For any target epsilon, if L(P)^2 > (S(U)+2 epsilon)^2 with S(U)+2 epsilon>=0, then no amount of bin-null Gram optimization in a single global envelope of this fixed radial weight can deliver negative-tail upper certificate <=epsilon. Change outer weights, partition, or use a different proof. This says nothing about impossibility of the true negative mass being <=epsilon. Conversely, a small L(P) alone does not prove a small achievable envelope or quantify remaining removable variance. A complementary certified upper bound on F_* requires control of the omitted squared bin means. Native branch state is unchanged.

## 2. Exact fixed-input experiment

(m,r,k)=(0,1,115), M=1, cutoff V=400. Here b_u=CT[x^3 y^(112+u)], B(t)=CT[x^2 y^(112+t)], S(t)=D_0(115+t)/D_0(115). Reused the 66 signed Laurent terms, eight joint displacement classes and integer recurrence from PREFIX-1082. Radial moments use the same zero-shift joint CT occupation table, not an independent classical reference. Exact integers and fractions; display decimals only after comparison.

The coarse partition uses cutpoints U and all subsequent members of (20,40,80,120,200,300,400); the fine partition uses every integer through 400. The 393 distinct terminal bins u=7..399 (Q=122..514) were checked exactly. Both radial and signed tail differences agree with direct bins at every one of these 393 positions. The first eight A_m match PREFIX-1082. Exactly one negative bin occurs in the tested U=7 range, at u=7 (Q=122), normalized negative mass 0.0009682364760895870. All tested bins u=8..399 are positive (the code explicitly checks no other negative; positivity follows from the exact nonzero scan inherited for these indices, not from extrapolation). No assertion that all bins beyond 399 are positive is made.

U | signed tail S(U) | coarse L | fine L | lower bound on true abs tail
7 | 1.073262313564349 | 1.18135956313 | 1.19100077717 | 1.075198786516528
20 | 0.9919840883769684 | 1.01041245208 | 1.01413200833 | 0.9919840883769684
120 | 0.2046283406925884 | 0.207552727985 | 0.207704998062 | 0.2046283406925884

S(400)=0.01188607960753790. The true absolute tail lower bound is sum of scanned absolute bins plus |S(400)|. It is not an upper bound. The lower certificate for the best possible single-envelope negative-mass upper bound is (L-S)/2, approximately 0.05886923, 0.01107396, 0.00153833 respectively. Verified exactly by rational square comparisons that these lower bounds exceed 0.058, 0.011, 0.0015, respectively. For U=120 the five-control envelope of PREFIX-1088 is 33.74205, while even perfect single-envelope internal cancellation cannot give a negative-mass upper certificate <=0.0015 with this fixed radial measure. This is a rigorous obstruction to one certificate strategy, not to actual small negative mass. The lower bound does not determine how much of the current 33.74205 can be removed; no new Gram matrix computed.

Compact JSON SHA256 of ordered records: d8375159a238495bde6462a54a8ff45a248c894bcaaea5ecd35588f9c69423f6. No native path re-enumeration, classical trig/pi reference, formal checker, independent review or new runtime improvement claim.

## 3. Reproduction

Run PREFIX-1082 section 4 from imports through construction of coeff, canonical, ks, T4, calc, tables, A (stop before switches). Use Nmax=520, Jmax=Nmax+12, and include zero shift via ks.add((0,)*6) before tables; assert len(ks)==8. This is the same exact paired CT recurrence, with the same carrier and first eight integers. Then run this suffix; the actual executed script uses equivalent variable names and Pascal initialization.

```python
from fractions import Fraction as Fr
from decimal import Decimal,localcontext
import hashlib,json,sys
sys.set_int_max_str_digits(0)
N=Nmax
assert A[:8]==[3474227232,83430021744,2013683977632,50005705455360,1283772437946144,33996158582646432,924583802183434368,25711602118824644352]
def rows(arr):
    out=[]
    while arr:
        out.append(arr[:4]); arr=[36*x-y for x,y in zip(arr,arr[1:])]
    return out
DR=rows(A); BR=rows(tables[(0,)*6][:N+1]); p36=[36**i for i in range(N+10)]
def D(m,q):return Fr(DR[q][m],4*p36[8+m+q])
def b(a,q):return Fr(BR[q][a],p36[a+q])
k=115; den=D(0,k);assert den>0
def s(u):return D(0,k+u)/den
def Btail(u):return b(2,k+u-3)
def f(u):return D(1,k+u)/den
def mass(u):return b(3,k+u-3)
V=400
for u in range(7,V):
    assert s(u)-s(u+1)==f(u)
    assert Btail(u)-Btail(u+1)==mass(u)>0
def floor2(U,edges):
    assert edges[0]==U
    return Btail(U)*(sum((s(a)-s(b0))**2/(Btail(a)-Btail(b0)) for a,b0 in zip(edges,edges[1:]))+s(edges[-1])**2/Btail(edges[-1]))
def dec(q):
    with localcontext() as ctx:
        ctx.prec=16
        return Decimal(q.numerator)/Decimal(q.denominator)
rec=[]
for U in (7,20,120):
    vals=[f(u) for u in range(U,V)]
    assert sum(vals,Fr(0))+s(V)==s(U)
    cuts=[U]+[t for t in (20,40,80,120,200,300,400) if t>U]
    coarse=floor2(U,cuts);fine=floor2(U,list(range(U,V+1)))
    assert s(U)**2<=coarse<=fine
    abs_lower=sum(map(abs,vals),Fr(0))+abs(s(V))
    negative=sum((-x for x in vals if x<0),Fr(0))
    assert fine>=abs_lower**2
    thresholds={7:Fr(58,1000),20:Fr(11,1000),120:Fr(15,10000)}
    assert fine>(s(U)+2*thresholds[U])**2
    assert [u for u in range(U,V) if f(u)<0]==([7] if U==7 else [])
    rec.append([U,V,cuts,*map(str,[s(U),s(V),Btail(U),coarse,fine,abs_lower,negative]),sum(x<0 for x in vals)])
    with localcontext() as ctx:
        ctx.prec=12
        print(U,dec(s(U)),dec(coarse).sqrt(),dec(fine).sqrt(),dec(abs_lower),dec(negative))
assert hashlib.sha256(json.dumps(rec,separators=(',',':')).encode()).hexdigest()=='d8375159a238495bde6462a54a8ff45a248c894bcaaea5ecd35588f9c69423f6'
```

## 4. Next problem

Use signed/radial tail pairs to guide outer block selection; a high exact block-split gain flags unavoidable between-bin variation in the single envelope. Obtain a complementary upper certificate for the omitted squared bin means (e.g. a certified positive radial weighting / tail second moment), so that the inner and outer variance budgets can actually be separated numerically. Then benchmark adaptive block choices against the prior five-control run. The explicit uniform positivity constant, p and d certification and original mother objective remain open.
