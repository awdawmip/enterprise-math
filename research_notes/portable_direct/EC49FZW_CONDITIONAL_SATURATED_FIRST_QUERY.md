# EC49FZW — Conditional saturated first-query residual

2026-11-25; portable continuation of EC49FZV at 3c5c0de42d624482927315f142aa0a5f49095682. Frozen BRC16943, fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923. No claim of formal Task ownership, acceptance or private session identity.

## Theorem

Use the FZU/FZV anchored model with each surviving support V represented by forced holes B_V and permitted holes A_V, with B_V subset A_V and cardinality bound hmax. Fix a saturated target (U,H), |H|=hmax, and O=H minus B_U, b=|O|. A query (r,j) has target answer positive iff r in U and j not in H. Define paid=1 iff r in U and j in O. In the conditioned fiber the remaining free holes are exactly O'=O minus {j} if paid, otherwise O; hence their count is b-paid.

For a rival V != U, compute the post-query forced holes C_V as follows:
* positive: retain only r in V and j not in B_V, then C_V=B_V;
* negative: if r not in V, C_V=B_V; otherwise retain only j in A_V and set C_V=B_V union {j}.
In both cases retain the residual rival iff |C_V union O'| <= hmax. Denote the resulting set Q'. This is exact by the anchored history fiber condition and the FZV saturation theorem; the common positive columns remain common. The one-query contraction can reintroduce a rival to the *residual clause set* when a paid hole is removed from O and that rival has r inactive. Thus one cannot simply subtract a query's covered clauses from the old Q.

For budget k in {b,b+1}, let d=k-1-b+paid. The query can begin an individual certificate of length <=k iff d>=0 and either Q' is empty or d=1 and a single FZV physical token covers Q'. In the latter case equivalently there is a row t for which every rival in Q' differs at t, or an active row t and a target-normal column z such that each rival differs at t or z belongs to C_V. Proof: conditioning costs one query; FZV exactly computes the remaining minimal certificate as |O'| plus minimum unit set cover; d is at most 1. This proves both directions for the fixed target. Intersection of the allowed first queries over selected targets is necessary for adaptive feasibility, not sufficient. Column permutations preserve the actual physical query orbit; the implementation tests one canonical representative per column signature, without replacing the adaptive problem by a fixed-target certificate problem.

## Implementation and evidence

Parent sat_token.cpp is patched at its existing saturation check; only selected saturated witnesses with b in {k,k-1} in the original gate are evaluated. Preserve the existing saturation-cost exclusion. Intersect allowR[j] with the exact predicate above; no change to other search rules or budget. Counters firstChecks,firstDrops,firstEmpty count invocations, removed candidates, and empty intersections. Compile with g++ -O3 -std=c++17. Generate w.in and w2.in via retry_v.py copied to retry_w.py with 'v.csv','v2.csv' appended to files after 'u.csv' and expected unresolved count changed from 516 to 507; run python retry_w.py 0 8 180000 and python retry_w.py 8 16 180000. Parent and new solver both run all 16 roots. All 16 rows have identical first seven fields (including calls and status). Each YES replay checks every labeled joint state. Both NO results are reproduced by unchanged parent solver. The algorithm is not a speedup on this batch; it removes 16019 candidate tests before later existing exclusions, but actual recursion is unchanged. Timing pair runs were concurrent, so no controlled speed claim.

Raw columns: id,n,status,calls,envelopePrunes,satChecks,satPrunes,firstChecks,firstDrops,firstEmpty. Parent outputs are precisely the first seven columns.
```csv
1773,1451,0,180001,4982,161,0,3483,1842,0
1813,1495,0,180001,3228,174,0,3650,1984,0
1815,1499,1,171593,4225,88,0,1889,1007,0
1819,1511,0,180001,2069,126,0,2755,1438,0
1821,1514,-1,178251,4654,153,0,3267,1632,0
1826,1524,-1,168411,8084,127,1,2653,1411,0
1828,1526,0,180001,6786,44,0,914,496,0
1837,1542,1,22380,117,22,0,509,227,0
1838,1542,1,22227,100,22,0,509,227,0
1839,1542,1,22380,117,22,0,509,227,0
1840,1542,1,22227,100,22,0,509,227,0
1841,1544,1,125786,3663,88,0,1795,978,0
1842,1544,1,128750,2358,103,0,2377,1195,0
1843,1545,1,104647,2630,97,0,1996,1044,0
1844,1546,1,65174,260,91,0,1990,1001,0
1845,1546,1,131007,227,102,0,2146,1083,0
```
Status 1 YES, -1 NO, 0 UNKNOWN (cap). Total 1882837 recursive calls, 1442 saturation checks, 1 saturation prune, 30951 first-query predicate tests, 16019 drops, zero empty intersections. 15392 labeled YES states replayed. Timing w/wbase 16.37/16.09 s; w2/w2base 7.43/7.15 s. Frontier: 1873 YES, 25 NO, 495 UNKNOWN of 2393; ordered 3783/43/869 of 4695. Bound 25<=M14<=27 unchanged.

## Independent finite comparison

Seed Random(16943). Two small anchored models (nr,nc,hmax)=(3,4,2),(4,5,3), supports all odd masks; each starts with column 0 normal. Generate 100 histories per model with 0..6 random queries answered by a randomly chosen saturated target. For every physical query compare direct predicate at k=b,b+1 to 1+brute conditioned state certificate <=k. 6400 comparisons, 655 accepted, zero mismatch. For frozen roots i=0,61,... select saturated target sat[(16943*i)%len(sat)] and every physical query and both budgets; compare with 1+FZV token(child(...))[0]. 20000 comparisons, 668 accepted, zero mismatch. Code below is executable with the parent's forced_hole.py, token_check.py and fourth.py.
```python
from random import Random
from collections import Counter
from forced_hole import explicit,child,brute,obs
from token_check import token
from fourth import fibers
import json

def direct(f,u,h,nr,nc,hmax,r,j,k):
    b0=next(b for v,b,a in f if v==u);o=h&~b0;b=o.bit_count()
    assert b in (k,k-1)
    bit=1<<j;pos=bool(u>>r&1 and not h&bit);paid=bool(u>>r&1 and o&bit)
    op=o&~(bit if paid else 0);d=k-1-b+paid
    if d<0:return False
    q=[]
    for v,c,a in f:
        if v==u:continue
        active=bool(v>>r&1)
        if pos:
            if not active or c&bit:continue
        elif active:
            if not a&bit:continue
            c|=bit
        if (c|op).bit_count()<=hmax:q.append((v^u,c&~h))
    if not q:return True
    if not d:return False
    assert d==1
    return any(all(diff&(1<<t) or (u>>t&1 and holes&(1<<z)) for diff,holes in q) for t in range(nr) for z in range(nc) if not h>>z&1)

def check():
    rng=Random(16943);c=Counter()
    for nr,nc,hm in [(3,4,2),(4,5,3)]:
        allf=[(u,0,((1<<nc)-1)^1) for u in range(1,1<<nr,2)]
        for _ in range(100):
            f=allf[:];u,h=x=rng.choice([x for x in explicit(f,hm) if x[1].bit_count()==hm])
            for _ in range(rng.randrange(7)):
                r,j=rng.randrange(nr),rng.randrange(nc);f=child(f,r,j,obs(x,r,j),hm)
            states=explicit(f,hm);b=(h&~next(c for v,c,a in f if v==u)).bit_count()
            for r in range(nr):
                for j in range(nc):
                    st=[y for y in states if obs(y,r,j)==obs(x,r,j)];actual=1+brute(st,x,nr,nc)
                    for k in (b,b+1):
                        pred=direct(f,u,h,nr,nc,hm,r,j,k);assert pred==(actual<=k),(f,x,r,j,k,actual)
                        c['small_checks']+=1;c['small_accepts']+=pred
    roots=json.load(open('fourth.json'))
    for i in range(0,len(roots),61):
        _,key,_,_=roots[i];f=list(fibers(key));st=explicit(f,14);sat=[x for x in st if x[1].bit_count()==14];u,h=x=sat[(16943*i)%len(sat)];b=(h&~next(c for v,c,a in f if v==u)).bit_count()
        for r in range(10):
            for j in range(25):
                g=child(f,r,j,obs(x,r,j),14);actual=1+token(g,u,h,10,25,14)[0]
                for k in (b,b+1):
                    pred=direct(f,u,h,10,25,14,r,j,k);assert pred==(actual<=k),(i,x,r,j,k,actual)
                    c['frozen_checks']+=1;c['frozen_accepts']+=pred
    print(dict(c))
if __name__=='__main__':check()
```

## Next
The additional tests are redundant with other pruning on these 16 roots. Measure overlap against prior candidate gates before spending more runtime. Use the conditional-residual theorem to derive cheaper direct multi-witness obstruction tests or selective evaluation, and continue only the remaining 495 roots. Preserve the exact positive/negative observations and physical labels. AUTHOR_PROVED / EXACT_FINITE_CHECK / PARTIAL_EXACT_BRANCH_REPLAY / NOT_REVIEWED.
