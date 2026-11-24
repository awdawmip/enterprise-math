# X6 R162 — True strict-near ratio atlas and sharp ten-row bank extension

2026-11-24. AUTHOR EXACT FINITE CERTIFICATE / NOT_REVIEWED. Independent informed conditional static six-pair observer, Port 10; no native time-dynamics or P000 promotion. Frozen R121: 8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd; R122: 1e4ab68c4f9c91bc60c07017acc57be20829832f; R161: d21c7ecc1c6ebdfc3e849d9fbe25baae75463c93. All six labeled gaps preserved. No input repinning.

## Result

Write w=(A,B,C,D)>0, r=C/A, s=(A+B,A+C,A+D,B+C,B+D,C+D), F_v=max_j g_j(v)/s_j, eta=min over all 1935 Port-10 directions modulo sign. For a fixed r, let S(r) be the union over A,B,D>0 with C=rA of the TRUE strict near sets {v:2F_v<3eta}. This is not a simultaneous cardinality claim. R161 compared against its six-row bank W; here we compare against the full R121 12-row Pareto bank P and hence the exact eta.

Complete table: every interval is open, infinity is unbounded. Final column is the number of retained maximal upper-bound vectors, prior to projection. No other direction is possible by R122.

| v | r where v is possible | boxes |
|---|---|---:|
| (1,-3,1) | (7/2,infinity) | 3 |
| (1,0,0) | (0,infinity) | 33 |
| (1,3,-1) | (10/9,11/7) U (11/3,infinity) | 10 |
| (2,-4,1) | (0,2/25) | 3 |
| (3,-7,2) | (5,infinity) | 9 |
| (3,-4,1) | (0,1/2) | 9 |
| (3,-1,0) | (0,1/2) | 3 |
| (3,3,-1) | (0,3/8) | 2 |
| (4,-4,1) | (0,infinity) | 32 |
| (4,-1,0) | (0,infinity) | 14 |
| (5,-4,1) | (0,infinity) | 26 |
| (5,-1,0) | (0,infinity) | 24 |
| (6,-4,1) | (0,infinity) | 14 |
| (6,-1,0) | (0,infinity) | 21 |
| (7,-8,2) | (0,9/22) | 2 |
| (7,-4,1) | (0,2/7) | 4 |
| (7,-1,0) | (0,9/20) U (10/9,11/7) | 10 |
| (7,2,-1) | (14/3,infinity) | 9 |
| (9,-5,1) | (0,infinity) | 29 |
| (9,-2,0) | (2,infinity) | 2 |

Consequently T from R160 contains S(r) iff 1/2 <= r <= 2. This follows by union of all outsider intervals, exactly (0,1/2) U (2,infinity). Every optimizer is strictly near (eta>0); thus on this closed interval both eta=min_T F and N={v in T:2F_v<3min_T F} hold. Beyond it, some true near direction is outside T. This strictly extends the R161 six-score-plus-ten-row joint formula's upper limit 4/3 by changing the optimizer to T. The first true upper outsider is (9,-2,0), not (3,-4,1), whose upper interval in R161 was relative to a failing W.

S(r) itself is the unique inclusion-minimal direction support for computing the complete N uniformly over weights at fixed r, because every listed row is realized at some such weight. Eight rows occur as possible members for every r; two additional T rows have disconnected support. For example S(2) has exactly the eight universal rows; S(22/17)=T. These are across-weight candidate unions, not simultaneous populations.

## Proof and new reusable pruning

Use R161 exact normalization: F_v < m min_bank F iff positive scaled weights u with s_j(u)>=2g_j(v) for all j, and for each bank row w some j with s_j(u)<2m g_j(w). Scaling by 2F_v proves forward, and the reverse follows from F_v(u)<=1/2 and F_w(u)>1/(2m). All six constraints are retained. For true nearness use m=3/2 and the entire Pareto bank P, whose coverage is checked again below. For each competitor only channels with 2m g_j(w)>2g_j(v) can work. Represent a conjunction of selected strict upper bounds as a six-vector b, with infinity for absent bounds. Appending a competitor means taking the componentwise minimum with one eligible upper bound, and taking the union across choices. If b<=c componentwise, its feasible set is included in that of c, including equality/strictness, since every finite upper bound is strict. Discard b. This deletion is safe at every subsequent update: min(b,x)<=min(c,x) for every future constraint. Induction proves maximal-box antichain pruning preserves the exact union at every stage. No sample or floating feasibility is used.

For each retained box use exact strict Fourier–Motzkin elimination of D,B, as in R161. A row aA+cC<=d becomes cr-dt<=-a under t=1/A>0, C=rA, with strictness preserved. Eliminate t. Each feasible conjunction gives one exact interval; take their union. Strict inequalities are propagated if either parent is strict; discard false constants. For a finite collection of lower and upper bounds on an eliminated real variable, pairwise comparisons are necessary and sufficient, including strict endpoints. Thus the projection is exact. The domain is the pinned R121 integer Port, q=max(sum positive,sum negative)<=10; h=(0,x+3y+6z,3x+12y+30z,7x+39y+126z); six labeled gaps are absolute pair differences. The calculation below directly implements this declared static BRC observer and algebraic comparisons, not native evolution.

## Secondary computation: strict winner within P

For each v in P, remove v from the competitor list and use m=1. The resulting interval is exactly where v can strictly beat every other P row (not a claim of unique full-domain winner if a dominated row ties). It provides the following next frontier for adaptive optimizer-bank analysis:
(1,0,0): (0,1) U (1,2);
(3,-7,2): (29/3,infinity);
(3,-4,1): (0,1/3);
(4,-4,1): (4/3,infinity);
(4,-1,0): (0,infinity);
(5,-4,1): (5/3,infinity);
(5,-1,0): (0,1) U (1,infinity);
(6,-4,1): (0,infinity);
(6,-1,0): (0,7/5);
(7,-1,0): (0,3/17);
(7,2,-1): (7,29);
(9,-5,1): (0,infinity).
At exceptional ratios where only tied optima may be available, minimal optimizer-bank selection still needs its own argument; do not equate strict-winner atlas with a full minimal optimizer theorem.

## Executed replay (Python 3)

The following code was executed locally successfully; all 20 near intervals and 12 strict-P-winner intervals printed exactly as above. The 1935/12/20 counts and Pareto coverage assertions passed. All arithmetic for the projection uses integers/Fraction. Extract the code into a .py file and run it.

```python
from itertools import product
from fractions import Fraction as Q
from math import gcd
from functools import reduce
G={}
for v in product(range(-10,11),repeat=3):
    if not any(v) or next(z for z in v if z)<0 or max(sum(max(z,0) for z in v),sum(max(-z,0) for z in v))>10:continue
    x,y,z=v;h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
    G[v]=tuple(abs(h[j]-h[i]) for i,j in ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3)))
P=[v for v,g in G.items() if not any(u!=v and all(a<=b for a,b in zip(h,g)) for u,h in G.items())]
W={(6,-1,0),(1,0,0),(5,-1,0),(9,-5,1),(4,-1,0),(6,-4,1)}
T=W|{(1,3,-1),(4,-4,1),(5,-4,1),(7,-1,0)}
C=[v for v,g in G.items() if not any(all(2*a>=3*b for a,b in zip(g,G[u])) for u in P)]
assert (len(G),len(P),len(C))==(1935,12,20)
assert all(any(all(a<=b for a,b in zip(G[u],g)) for u in P) for g in G.values())
J=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3));E=[tuple(int(i in j) for i in range(4)) for j in J]
def clean(rows):
    out={}
    for row,strict in rows:
        a,b=row[:-1],row[-1]
        if not any(a):
            if b<0 or (strict and b==0):return None
            continue
        h=reduce(gcd,row,0);row=tuple(x//h for x in row)
        out[row]=out.get(row,False) or strict
    return list(out.items())
def elim(rows,i):
    if rows is None:return None
    p=[(a,s) for a,s in rows if a[i]>0];n=[(a,s) for a,s in rows if a[i]<0]
    z=[(a[:i]+a[i+1:],s) for a,s in rows if a[i]==0]
    for a,s in p:
        for b,t in n:
            z.append((tuple(a[i]*y-b[i]*x for k,(x,y) in enumerate(zip(a,b)) if k!=i),s or t))
    return clean(z)
def merge(I):
    out=[]
    for l,h,ls,hs in sorted(I,key=lambda x:(x[0],x[2])):
        if not out:out.append((l,h,ls,hs));continue
        a,b,s,t=out[-1]
        if b is not None and (l>b or (l==b and t and ls)):out.append((l,h,ls,hs));continue
        if b is None:continue
        if h is None or h>b:out[-1]=(a,h,s,hs)
        elif h==b:out[-1]=(a,b,s,t and hs)
    return out
INF=10**6
assert max(max(g) for g in G.values())*3<INF
def maximal(boxes):
    out=[]
    for x in sorted(set(boxes),key=lambda x:(sum(x),x),reverse=True):
        if not any(all(a<=b for a,b in zip(x,y)) for y in out):out.append(x)
    return out
def boxes_for(v,bank,m2):
    opts=[[(j,m2*G[w][j]) for j in range(6) if m2*G[w][j]>2*G[v][j]] for w in bank]
    boxes=[(INF,)*6]
    for opt in sorted(opts,key=len):
        boxes=maximal([b[:j]+(min(b[j],u),)+b[j+1:] for b in boxes for j,u in opt])
    return boxes
def project(v,bank,m2):
    basic=[(tuple(-x for x in a)+(-2*g,),False) for a,g in zip(E,G[v])]+[(tuple(-int(i==j) for i in range(4))+(0,),True) for j in range(4)]
    boxes=boxes_for(v,bank,m2); intervals=set()
    for bs in boxes:
        rows=clean(basic+[(a+(b,),True) for a,b in zip(E,bs) if b!=INF])
        rows=elim(elim(rows,3),1)
        if rows is None:continue
        rows=clean([((a[1],-a[2],-a[0]),s) for a,s in rows]+[((0,-1,0),True),((-1,0,0),True)])
        rows=elim(rows,1)
        if rows is None:continue
        lo=Q(0);hi=None;ls=True;hs=False
        for (a,b),s in rows:
            x=Q(b,a)
            if a<0:
                if x>lo:lo,ls=x,s
                elif x==lo:ls|=s
            else:
                if hi is None or x<hi:hi,hs=x,s
                elif x==hi:hs|=s
        if hi is None or lo<hi or (lo==hi and not(ls or hs)):intervals.add((lo,hi,ls,hs))
    return merge(intervals),len(boxes)
if __name__=='__main__':
    for v in sorted(C):
        print(v,project(v,P,3), 'T' if v in T else '',flush=True)
    print('unique strict P winners:')
    for v in sorted(P):print(v,project(v,[u for u in P if u!=v],2),flush=True)
```

## Provenance and continuation

Source P000 V5, ACTIVE Heartbeat World, joint static observer and current portable/method rules preserved. Researcher original registration receipt r2-20261124-0310-r155-own-session-v1 SUCCEEDED, EM-DIRECT-AE5AD5 / RA-B60559848FD879270DCA6317; custody status registration SUCCEEDED, not revoked/closed, execution_authorized=false. Native continuation request r2-20261124-0910-x6-cont-read-v1 last observed RUNNING/SOURCE_MATERIALIZATION; no formal CLAIM or Result/Review made. Independent review pending. Next: use the strict-P-winner table to derive a truly minimal optimizer support at each fixed ratio, including exact exceptional tie ratios, and search for simpler algebraic criteria for the antichain projection.
