# R284HG — Complete finite pre-onset exception classification for u ≥ 10000

2026-11-25; author proof with exact integer polynomial certificates, NOT_REVIEWED. Auxiliary binary-tag word-count model; no new native physical attribution. Frozen source: HF b9fda453ef76999e8ec9cbc776e69f715025819a:research_notes/portable_direct/R284HF_EFFECTIVE_SHARP_LAST_TRANSITION_EXCEPTION_20261125.md, preserving its HE/HC source pins and count definitions. P000 V5, ACTIVE worldview and observer preservation unchanged. Global canonical entries checked at 86107f3c879d34abdfc8b907ab9400ef85521482; EM entries checked at d58596993afaefb2b0db421b44036df5d4010078. Own original registration r1-20261124-0256-r284gd-session-v1 SUCCEEDED; own recovery metadata verified open, no runs, EM-DIRECT-0C386E / RA-B82240E8488EF5A1DA5186C4. Previous owner inventory r1-20261125-0501-owner-read SUCCEEDED with no LEASED entries; fresh r1-20261125-0601-owner-read last observed QUEUED, error null. No shared CLAIM, Result or review.

## Theorem

Assume the HF exact rational-sign transfer and global cutoff, which depend on the frozen HE/HC corridor/count identities. Put f(u)=(isqrt(324u+121887)-169)//3. For every integer u>=10000 and 0<=q<u:

* There is no tie K(q,u)=1.
* The actual largest q with K>1 is f(u)-c(u), with c(u) in {0,1,2,3}.
* Exactly 589126 distinct budgets u>=10000 have c(u)>0: 583054 have c=1, 5979 have c=2, and 93 have c=3.
* Last exception u=2522581650951, agreeing with HF. No scan over that trillion-scale interval is needed.

## Proof and compact classification

Reuse HF's N,B,F=N-B and residual E=324u+121887-(3q+169)^2, with U_E(q)=((3q+169)^2-121887+E)/324. The sign of F transfers to K-1 whenever F!=0 for u>=10000, q<=u/8. Beyond the strip K<1 by HC/HF. Within the strip K0 strictly increases in u and decreases in q. The predicted f is in the strip for every u>=10000 (squaring 6 sqrt(u+13543/36)<u/8 proves this). E never vanishes, and f is the largest q with E>0. For q>=555, U_-1(q)>=10000 and >=8q, as follows from the explicit quadratic (its difference from either lower bound is positive and increasing there).

Introduce the exact observer polynomial G(x,E)=positive common denominator times F(U_E(555+x),555+x), of x-degree 16 and E-degree 9. For E=-1 all 17 coefficients in x are negative; for E=50000 all are positive (certificate below). Thus for q>=555 any strip point with E<=-1 is negative, and any with E>=50000 is positive, by HF monotonicity of K0 in u. This uses the sign of K0-1, not monotonicity of the numerator F alone.

Only E=1,...,49999 in the 54 permissible residues mod 324 can remain; exactly 8333 integers E occur. The map q mod 54 -> E mod 324 is injective, given by (121887-(3q+169)^2) mod 324. For each of the 8333 E, exact coefficient evaluation yields either all positive nonzero coefficients (4350 cases), or exactly one sign change from negative low-order to positive high-order coefficients (3983 cases). Descartes' rule of signs gives at most one positive root in the latter case; where the initial grid point is negative, positivity of the leading coefficient guarantees a crossing. Thus on the grid q>=555 in the unique permitted class r(E) mod 54, the negative points form an initial interval, possibly empty, with at most one tie. Binary search using exact integer Horner evaluation locates its last negative q and tests its adjacent point for equality. If the first point is positive there is no later root, since the only possible positive root is a simple crossing from negative to positive. If the first point is zero it is recorded separately. For q>=555 all these positive E points satisfy the strip bounds by the same quadratic lower bound. The resulting 3852 nonempty arithmetic progressions contain exactly 595233 negative (u,q) pairs, and no ties. The code regenerates every interval endpoint; no floating root finding is used. E of a nonempty interval ranges from 2 to 23675.

For q<=552, F(10000,552)>0 plus HF monotonicity in both variables gives strict positivity for all u>=10000. At fixed q=553 the negative budgets are 10000,...,10011, followed by strict positivity; at q=554 they are 10000,...,10045, followed by strict positivity. These 58 pairs and the boundary signs are checked directly. This handles all remaining strip points and excludes every F=0 in the relevant integer domain. Consequently exact K has no ties there, and the global cutoff excludes ties outside the strip.

To count distinct exceptional budgets rather than pairs, partition the negative pairs by the distance k=f(u)-q>=0. This is equivalent to

18kq+1014k+9k^2 <= E < 18(k+1)q+1014(k+1)+9(k+1)^2.

Each E progression can be intersected with these linear bounds using integer division. The counts are k=0:589126, k=1:6072, k=2:93, none for k>=3. The strict sign transition in HF implies that the count at distance k is exactly the number of budgets with correction c>=k+1, so differencing gives the stated distribution. In particular all q>f are negative; underestimation is impossible in this domain. The maximum correction is exactly 3, attained at 93 budgets.

This is a finite certificate over E rather than u. The 54 residue classes retain the coupled relation between q and u; discarding it would count invalid integer states. The original path counts remain available for other observers. For any u>=10000, compute f and test F(u,f), F(u,f-1), F(u,f-2) by exact integer arithmetic, taking the first positive candidate; if all three negative, return f-3. This is a bounded operation-count exact algorithm, with growing integer bit costs, no huge path counts and no fallback for ties. u<10000 and global strict monotonicity beyond the strip remain open.

## Executed reproduction

Python 3 / SymPy, exact integer/rational operations only. The following code reproduces all certificate checks and counts (the actual run used the same algorithm and printed the output below).

```python
import sympy as s
from math import isqrt
from collections import Counter
u,q,x,e=s.symbols('u q x e')
H=u+2*q+1;D=H+3*u;J=3*u+q
def T(a,b,x,t):
    def R(k):return s.prod((a-j)/(b+j+1) for j in range(k))
    return 1-R(x+1)-R(t+1)+R(x+t+2)
S=T(H,3*u,1,1)+q*H/D*T(H-1,3*u,0,1)
P=H/(3*u+1)*T(H-1,3*u+1,0,0)
Q=(D+1)/(3*u+1)*T(H,3*u+1,0,0)
N,B=map(s.expand,s.fraction(s.factor(P*Q*(J+1)**2/(S*S*H))))
F=N-B
G=s.Poly(F.subs(u,((3*q+169)**2-121887+e)/324).subs(q,x+555),x,e).clear_denoms()[1]
cs=[[int(G.coeff_monomial(x**i*e**j)) for j in range(10)] for i in range(17)]
def ev(c,t):
    v=0
    for a in reversed(c):v=v*t+a
    return v
def coefficients(E):return [ev(c,E) for c in cs]
assert all(a<0 for a in coefficients(-1))
assert all(a>0 for a in coefficients(50000))
res={(121887-(3*j+169)**2)%324:j for j in range(54)}
assert len(res)==54
f=s.lambdify((u,q),s.factor(N)-s.factor(B),'math')
count=0;kinds={};ties=[];records=[];last=(0,0,0)
for E in range(1,50000):
    if E%324 not in res:continue
    c=coefficients(E)
    sg=[1 if a>0 else -1 for a in c if a]
    changes=sum(a!=b for a,b in zip(sg,sg[1:]))
    key=(sg[0],changes,sg[-1])
    kinds[key]=kinds.get(key,0)+1
    assert sg[-1]==1 and changes<=1,(E,sg)
    r=res[E%324];lo=555;first=lo+(r-lo)%54
    def val(Q):return ev(c,Q-555)
    if val(first)>0:continue
    L=0;R=1
    if val(first)==0:ties.append((E,first));continue
    while val(first+54*R)<0:R*=2
    while R-L>1:
        mid=(R+L)//2
        if val(first+54*mid)<0:L=mid
        else:R=mid
    end=first+54*L;n=L+1
    if val(first+54*R)==0:ties.append((E,first+54*R))
    count+=n;v=((3*end+169)**2-121887+E)//324
    if v>last[0]:last=(v,end,E)
    records.append((E,first,end,n))
print('coefficient patterns',kinds,'intervals',len(records),'negative pairs',count,'ties',ties,'last',last)
assert f(10000,552)>0
small=[]
for Q in [553,554]:
    assert f(10000,Q)<0
    U=10000
    while f(U,Q)<0:
        small.append((U,Q));U+=1
    assert f(U,Q)>0
    print('small q',Q,'first positive u',U)
assert not ties
hist=Counter()
for E,first,end,n in records:
    for k in range(10):
        low=(E-1014*(k+1)-9*(k+1)**2)//(18*(k+1))+1
        high=(E-1014*k-9*k*k)//(18*k) if k else end
        low=max(first,low);high=min(end,high)
        low+=(first-low)%54
        if low<=high:hist[k]+=(high-low)//54+1
    assert E<18*10*first+1014*10+9*100
for U,Q in small:
    k=(isqrt(324*U+121887)-169)//3-Q
    assert k>=0
    hist[k]+=1
assert sum(hist.values())==count+len(small)
print('small pairs',len(small),'distance histogram',dict(sorted(hist.items())))
print('correction distribution',{k+1:hist[k]-hist[k+1] for k in sorted(hist) if hist[k]})
print('largest intervals',sorted(records,key=lambda t:t[-1],reverse=True)[:10])
print('E range',min(t[0] for t in records),max(t[0] for t in records))
assert hist[0]==589126
assert last==(2522581650951,9529526,2)
```

Actual local output:
```
coefficient patterns {(-1, 1, 1): 3983, (1, 0, 1): 4350} intervals 3852 negative pairs 595233 ties [] last (2522581650951, 9529526, 2)
small q 553 first positive u 10012
small q 554 first positive u 10046
small pairs 58 distance histogram {0: 589126, 1: 6072, 2: 93}
correction distribution {1: 583054, 2: 5979, 3: 93}
largest intervals [(2, 578, 9529526, 176463), (11, 581, 1732415, 32072), (14, 594, 1361124, 25196), (23, 561, 828381, 15331), (26, 598, 732784, 13560), (35, 583, 544255, 10069), (38, 590, 501278, 9273), (47, 593, 405269, 7495), (50, 570, 380892, 7044), (59, 591, 322755, 5967)]
E range 2 23675
```

## Continuation

The finite pre-onset classification and integer ties for u>=10000 are closed at author-proof scope, contingent on the frozen HF/HE/HC identities. Do not enumerate 2.5 trillion budgets. Next: lower the paid rational-strip threshold (currently 10000), then close remaining small-u cases by exact integer moment counting, and continue full-domain strict monotonicity outside the strip as a separate question. No shared task completion or mathematical admission asserted.
