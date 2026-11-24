# X6 R161 — Sharp C/A ratio interval for the R159–R160 banks

2026-11-24. AUTHOR EXACT FINITE CERTIFICATE / NOT_REVIEWED. Independent informed static conditional six-pair BRC observer; not native heartbeat evolution, R063, a new P000 assertion, or formal Task progress.

## Theorem

Keep Port 10, the exact R121/R122 integer direction domain and all six labeled pair gaps. Write w=(A,B,C,D)>0, r=C/A, F_v=max_j g_j(v)/s_j, s=(A+B,A+C,A+D,B+C,B+D,C+D). Let W be R159's six-row optimizer bank and T be R160's ten-row near bank. Let eta=min over all 1935 directions.

1. For fixed r>0, min_W F=eta for EVERY A,B,D>0 with C=rA if and only if 1/3<=r<=4/3.
2. For fixed r>0, the joint R159–R160 formula (eta=min_W F and N={v in T:2 F_v<3 min_W F}) is correct for EVERY such weight iff 1/2<=r<=4/3. The endpoints are included. This is sufficiency of the fixed banks, not a claim each member is necessary at every ratio or that T by itself fails outside the optimizer interval.
3. R159/R160's original ratio 22/17 is within this interval. The upward margin in r is only 2/51; the downward margin is 27/34. The first optimizer outsider above 4/3 is (4,-4,1); the first possible near outsider below 1/2 within the valid optimizer range is (3,-1,0) or (3,-4,1).

## Exact proof by projection of typed joint BRC inequalities

R121's 12-row Port-10 Pareto set P covers every feasible direction. R122's componentwise three-halves domination leaves a 20-row necessary near envelope C0. Both facts are recomputed from the integer domain in the checker below.

Fix candidate v, bank W, and multiplier m=1 (optimizer failure) or m=3/2 (near failure relative to W). The existence of a weight with ratio r and F_v<m min_W F is equivalent to existence of positive scaled weights u with the same ratio and:
- s_j(u)>=2 g_j(v) for all six j;
- for every w in W, at least one k satisfies s_k(u)<2 m g_k(w).
Forward: scale the original weights by 2 F_v, which is positive. Reverse: F_v(u)<=1/2 and each F_w(u)>1/(2m). Thus no need to select an active channel of v; the retained six inequalities exactly encode its BRC score. No signed information or native trajectory claim is inferred from this static observer.

For each competitor w, enumerate only k satisfying m g_k(w)>g_k(v). All other choices contradict the lower bound. For a tuple of chosen channels, merge strict upper bounds on each channel by their minimum. This gives a finite union of conjunctions of linear inequalities in four scaled weights. Use exact Fourier–Motzkin elimination of D and B, preserving strictness: when eliminating a variable, combine each positive-coefficient row with each negative-coefficient row by positive multipliers that cancel it, with a strict output whenever either parent is strict. Keep zero-coefficient rows. Constant false rows discard a cell. This projection is exact over the reals, including open facets: a finite family of lower and upper bounds admits an intermediate real iff all pair comparisons hold, with equality allowed only for non-strict bounds.

After eliminating D,B, rows have form a A+c C <= d (or <). Since A>0, substitute C=r A and u=1/A>0, giving c r-d u<=-a with identical strictness. Eliminate u with the same rule, keeping r>0. Each conjunction becomes an exact interval with endpoint inclusion. Union across the finite channel choices gives the complete ratio set, not just sampled values.

## Actual exact interval census (Python integers/Fraction)

For m=1, outsider P minus W:
| v | distinct bound vectors | ratio where it can strictly beat W |
|---|---:|---|
| (3,-7,2) | 2 | (5,infinity) |
| (3,-4,1) | 6 | (0,1/3) |
| (4,-4,1) | 41 | (4/3,infinity) |
| (5,-4,1) | 30 | (5/3,infinity) |
| (7,-1,0) | 6 | (0,3/10) |
| (7,2,-1) | 2 | (14/3,infinity) |

Union (0,1/3) U (4/3,infinity). Pareto coverage makes this exactly the optimizer-bank failure set.

For m=3/2, outsider C0 minus T, relative to W:
| v | distinct bound vectors | ratio where it can satisfy strict near relative to W |
|---|---:|---|
| (1,-3,1) | 24 | (7/2,infinity) |
| (2,-4,1) | 12 | (0,9/32) |
| (3,-7,2) | 9 | (10/3,infinity) |
| (3,-4,1) | 41 | (0,1/2) U (4/3,infinity) |
| (3,-1,0) | 14 | (0,1/2) |
| (3,3,-1) | 9 | (0,3/8) |
| (7,-8,2) | 9 | (0,9/22) |
| (7,-4,1) | 22 | (0,2/7) |
| (7,2,-1) | 9 | (28/9,infinity) |
| (9,-2,0) | 16 | (2,infinity) |

Union (0,1/2) U (4/3,infinity). Within [1/3,4/3] the bank value is exactly eta, so this union intersected with the valid optimizer interval is exactly the true near-bank failure set there. Outside [1/3,4/3] the joint formula already fails on its optimum component. This establishes both directions of the joint theorem, without inferring true nearness from an invalid optimizer bank.

Exact full-domain witness: w=(5,5,2,24), r=2/5, eta=min_W F=11/26; outsider (3,-1,0) has F=18/29<33/52. Another w=(3,3,1,14), r=1/3, eta=11/15, same outsider F=18/17<11/10. Both were recalculated over all 1935 rows. The executed certificate returned R161 EXACT PROJECTION PASS. A separate attempted expansion using all P as competitors to decide T-only failure everywhere was not completed; it is not used in this proof.

## Standalone replay (Python 3)

Extract the code fence below into a .py file. This is the same domain generation, exact elimination, union and witness checks used in the completed local run, with diagnostic printing shortened.

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
W=((6,-1,0),(1,0,0),(5,-1,0),(9,-5,1),(4,-1,0),(6,-4,1))
T=set(W)|{(1,3,-1),(4,-4,1),(5,-4,1),(7,-1,0)}
C=[v for v,g in G.items() if not any(all(2*a>=3*b for a,b in zip(g,G[u])) for u in P)]
assert (len(G),len(P),len(C))==(1935,12,20)
assert all(any(all(a<=b for a,b in zip(G[u],g)) for u in P) for g in G.values())
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
J=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
E=[tuple(int(i in j) for i in range(4)) for j in J]
def interval(v,bank,mode):
    opts=[[j for j in range(6) if mode*G[w][j]>G[v][j]] for w in bank]
    basic=[(tuple(-x for x in a)+(-2*g,),False) for a,g in zip(E,G[v])]+[(tuple(-int(i==j) for i in range(4))+(0,),True) for j in range(4)]
    combos=set()
    for js in product(*opts):
        bounds=[None]*6
        for w,j in zip(bank,js):
            b=int(2*mode*G[w][j]);bounds[j]=b if bounds[j] is None else min(b,bounds[j])
        combos.add(tuple(bounds))
    intervals=set()
    for bs in combos:
        rows=clean(basic+[(a+(b,),True) for a,b in zip(E,bs) if b is not None])
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
    return intervals,len(combos)
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
for mode,V,bound in [(1,set(P)-set(W),Q(1,3)),(Q(3,2),set(C)-T,Q(1,2))]:
    allI=set()
    for v in sorted(V):
        I,n=interval(v,W,mode);allI|=I
        print(v,n,merge(I))
    assert merge(allI)==[(Q(0),bound,True,True),(Q(4,3),None,True,False)]
for a,b,c,d,expected in [(5,5,2,24,Q(11,26)),(3,3,1,14,Q(11,15))]:
    s=(a+b,a+c,a+d,b+c,b+d,c+d)
    f={v:max(Q(x,y) for x,y in zip(g,s)) for v,g in G.items()}
    assert min(f.values())==min(f[v] for v in W)==expected
    assert 2*f[(3,-1,0)]<3*expected
print('R161 EXACT PROJECTION PASS')
```

## Provenance and next question
R121 frozen source 8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd; R122 1e4ab68c4f9c91bc60c07017acc57be20829832f; R159 checker 1bb93f9b2c101d026649cd01a77d3585b6283c0e; R160 proof 33ec06a1daf36f007fd03bb30f41c6f369f42e7b and checker bfc76ae24fc838aa8878bd7ca806733574f9d0d7. Current P000 and Heartbeat World, portable research, research method read separately. No frozen task scientific input changed. Current continuation original request r2-20261124-0810-x6-cont-read-v1 last observed RUNNING; no CLAIM, formal Result, or Review. Prior own registration r2-20261124-0310-r155-own-session-v1 success EM-DIRECT-AE5AD5 / RA-B60559848FD879270DCA6317 (historical readback, not live authorization). Next: use exact projection with pruned upper-bound sets for the actual 12-row Pareto bank to classify T-only failure outside the six-bank validity interval, and derive per-ratio minimal candidate sets.