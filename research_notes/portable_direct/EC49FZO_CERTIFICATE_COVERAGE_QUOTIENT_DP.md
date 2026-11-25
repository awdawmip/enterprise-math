# EC49FZO — Exact certificate-coverage quotient DP; complete first-pass fourth-level census

2026-11-25. Independent portable continuation of EC49FZN; frozen BRC16943, h=14,m=25. Parent dacffe23f2cb901a381a8613c8c7e1b519894af0:research_notes/portable_direct/EC49FZN_SATURATED_CLAUSE_DOMINANCE.md (blob fd8ca737f6f068bb2f7ad3f2ccec852e43c93630). Historical provenance EM-DIRECT-23537B; current private writer binding unconfirmed. Native topic read r4-20261125-1130-ec49as-read-v1 SUCCEEDED, Source 5d0517f3989c34df300b3959232a78e1d151305c, NO_CANONICAL_PUBLICATION_DIRECTORY; native owner projection not evaluated, no formal CLAIM. P000 unchanged.

## Exact coverage-mask quotient

Use the FZM saturated anchored feature certificate and FZN dominance reduction under their genuine-history common potential-hole universe assumptions. Target x=(U,H), |H|=h, B=B_U, O=H minus B, and q retained competing clauses (R_i,L_i,G_i,d_i), d_i>0. Their conjunction is equivalent to all original clauses. Define clause universe Q, row coverage r(T)={i:T intersects R_i}, threshold coverage g(J)={i:|J intersect G_i|>=d_i} for J subset B, and live coverage l(P)={i:P intersects L_i} for P subset complement H. The mandatory missing features O are fixed.

Define a(S,p)=min{|T minus U|: r(T)=S, |T intersect U|=p}; b(D)=min{|J|:g(J)=D,J subset B}, with infinity for absent keys. Define t(E) as minimum number of live columns covering every clause in E. For each live column j, L(j)={i:j in L_i}. Then t(empty)=0, and for any i in E,
t(E)=min_{j:i in L(j)} [1+t(E minus L(j))], with empty minimum infinity. This is exact by choosing a column covering i in any optimal cover; recursion strictly shrinks E, and no repeated physical column is needed. Identical nonempty L(j) may be represented by one actual column, as their cost is identical.

**Theorem**: the precise minimum target-specific query certificate cost is
C_sat(U,H)=|O|+min_{S,D,p}[a(S,p)+b(D)+max(p,t(Q minus (S union D)))].
Proof: each original feature selection maps to (S,D,p), with no smaller costs than a,b and t, and FZI's anchored positive feature pairing gives its resource cost |O|+|J|+|T minus U|+max(|T intersect U|,|P|). Conversely choose actual minimizing row and missing subsets for each finite key and recover a minimum live cover using the recurrence. All retained clauses are satisfied, so FZN implies all original clauses are satisfied; FZM identifies the target and FZI converts its features into a query certificate at the displayed cost. Thus both inequalities hold. This is a second, objective-specific BRC quotient on complete coverage signatures, preserving threshold multiplicity until the signature has been computed. Unlike a Boolean approximation of missing columns, it retains the exact threshold outcomes. It is not a substitute for the dynamic fiber representation of an adaptive decision tree.

The finite implementation enumerates 2^10 row subsets and 2^|B| missing subsets, then keeps only the minima above. The live-cover recursion visits at most 2^q masks. Combining representatives is at most the product of the two retained map sizes; it is not claimed to be polynomial in unrestricted q or to accelerate the adaptive solver. The pruning condition n+|J|+p>=incumbent is safe because max(p,t)>=p. A witness is retained through each quotient.

## Executed exact optimization

Parent local frozen fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923; fullrow.cpp SHA256 3d1ae2d75991d5b6cd9a131f38068f27d04a1e2fc2abccf6e6673893e00f9d0b; prior fourth_partial.csv 494f70227d537e0d57b36477ecaea66ad46dcc7f8c6151deeedc3db440ce8e27, fourth_new.csv 8fcecca3636d17e307ca143224db69b9825b8c7489cf8c13d9b25aefcbba64c8. All four local input hashes match the pinned parent reports.

For every one of 2393 fourth-level roots, select one saturated state by deterministic index (root_id*16943)%len(saturated_states), preserving gen.physical order. Compute exact minimum, lift a feature witness, and independently filter the explicitly expanded labeled states to verify uniqueness. Recompute against unreduced clauses for root IDs divisible by 45 (54 cases). All assertions passed. 2,737,805 explicit state comparisons. Clause count 14,710 before and 9,558 after pairwise reduction. Exact minimum cost histogram 1:1, 2:60, 3:634, 4:1313, 5:373, 6:12. Max-cost IDs 1973,2019,2128,2170,2198,2236,2274,2333,2346,2350,2367,2376. Aggregate retained row keys 91,595 (max 250 per target), missing coverage keys 18,690 (max 78), memoized live masks 25,096 (max 154). Wall time 8.473547883 seconds for this script on current container; no controlled baseline timing. The sample covers every root, not every saturated state. All sampled costs <=6, so this experiment provides no root exclusion at k=15. Next useful application is a small remaining-budget adaptive node, not simply more root samples.

Executed quotient_opt.py SHA256 c0f834a8cbadc6560a269026b77ea0a5e15d227bb489e7db4c81b9d9613f4bf1. Raw opt_results.csv SHA256 bae9349c4561aab85024531669e80c1b9493444f41b66b9e283b1404929fdd43, fields root_id,U,H,cost,T,P,J,n_original,n_reduced,row_keys,missing_keys,live_memo. Raw witnesses are included in the local reproduction archive. Complete cost histogram, deterministic algorithm and seed are preserved here.

```python
from functools import lru_cache
from collections import Counter
from gen import physical
from fourth import fibers
from dominance import constraints,reduce,covered
import json,csv,time

def bits(s):
    while s:
        x=s&-s;yield x;s^=x

def subsets(s):
    x=s
    while True:
        yield x
        if x==0:break
        x=(x-1)&s

def optimum(u,b,o,q):
    # Masks are indexed by competing support, not by physical column.
    allq=(1<<len(q))-1
    rows=[sum(1<<i for i,(r,l,g,d) in enumerate(q) if r&x) for x in bits(1023)]
    live={sum(1<<i for i,(r,l,g,d) in enumerate(q) if l&x):x for x in bits(((1<<25)-1)&~(b|o))}
    live.pop(0,None)
    byclause=[[v for v in live if v>>i&1] for i in range(len(q))]
    @lru_cache(None)
    def tau(s):
        if not s:return (0,0)
        i=min((x.bit_length()-1 for x in bits(s)),key=lambda i:len(byclause[i]))
        best=(100,0)
        for v in byclause[i]:
            n,p=tau(s&~v)
            if n+1<best[0]:best=(n+1,p|live[v])
        return best
    # For equal coverage and equal positive-row cost retain cheapest negative cost.
    tr={}
    for t in range(1024):
        c=0
        for x in bits(t):c|=rows[x.bit_length()-1]
        p=(t&u).bit_count();n=(t&~u).bit_count();key=(c,p)
        if key not in tr or n<tr[key][0]:tr[key]=(n,t)
    # For equal threshold coverage retain a minimum-cardinality missing subset.
    jr={}
    for j in subsets(b):
        c=sum(1<<i for i,(r,l,g,d) in enumerate(q) if (j&g).bit_count()>=d)
        n=j.bit_count()
        if c not in jr or n<jr[c][0]:jr[c]=(n,j)
    best=(100,0,0,0)
    for (r,p),(n,t) in tr.items():
        if n+p>=best[0]:continue
        for c,(nj,j) in jr.items():
            if n+nj+p>=best[0]:continue
            l,P=tau(allq&~(r|c));cost=n+nj+max(p,l)
            if cost<best[0]:best=(cost,t,P,j)
    cost,t,P,j=best
    assert covered(q,t,P,j)
    assert cost==j.bit_count()+(t&~u).bit_count()+max((t&u).bit_count(),P.bit_count())
    return cost+o.bit_count(),t,P,j,len(tr),len(jr),tau.cache_info().currsize

if __name__=='__main__':
    roots=json.load(open('fourth.json')); totals=Counter(); start=time.monotonic()
    with open('opt_results.csv','w') as f:
        w=csv.writer(f,lineterminator='\n')
        for i in range(len(roots)):
            n,key,_,_=roots[i];r,mask,other=key;fs=list(fibers(key));st=physical([mask,*other],14,r,0);assert len(st)==n
            sat=[(u,h) for u,h in st if h.bit_count()==14];u,h=sat[(i*16943)%len(sat)]
            b,o,q=constraints(fs,u,h);z=reduce(q)
            c,t,p,j,nt,nj,nl=optimum(u,b,o,z)
            assert covered(q,t,p,j)
            assert [(v,K) for v,K in st if not ((u^v)&t or K&p or (o|j)&~K)]==[(u,h)]
            if i%45==0:
                c2,*_=optimum(u,b,o,q);assert c2==c;totals['unreduced_checks']+=1
            totals['targets']+=1;totals['before']+=len(q);totals['after']+=len(z);totals['state_comparisons']+=len(st);totals['cost_'+str(c)]+=1
            w.writerow((i,u,h,c,t,p,j,len(q),len(z),nt,nj,nl));f.flush()
    print(dict(totals));print('seconds',time.monotonic()-start)
```

## Fourth-level first pass completed

Reuse unchanged fullrow.cpp and fourth_input.py (FZL/FZM sources, parent reproduction). Compile g++ -O3 -std=c++17 fullrow.cpp -o solver; generate inputs with python fourth_input.py LO 2393 12000 > input.txt; run timeout 18s ./solver < input.txt > fourth_tail.csv (LO=1739), repeat from first uncompleted ID 1934 into fourth_tail2.csv, then timeout 29s with LO=2121 into fourth_tail3.csv. No interrupted row is classified. Last segment completed all 272 roots.

New completed roots 1739..2392 inclusive: 654; 53 YES, 10 NO (complete solver termination with -1), 591 cap-UNKNOWN. New recursive calls 7,482,272; new actual-label state replays 93,060. YES IDs:
1774,1790,1791,1817,1823,1831,1832,1847,1866,1867,1874,1875,1876,1882,1883,1907,1908,1915,1917,1919,1923,1928,1929,1941,1942,1943,1944,1945,1951,1952,1953,1971,1976,1979,1980,1987,1989,2059,2060,2078,2079,2081,2097,2102,2110,2111,2150,2151,2153,2154,2155,2156,2247.
NO IDs:
2178,2183,2185,2243,2249,2267,2268,2270,2372,2373.
All other new IDs cap-UNKNOWN, not NO.
Raw completed CSV SHA256: fourth_tail.csv (195 rows) 39e5905f452019166e153a69f9bfaa3999751c7f4401444bdc4168ab928b590d; fourth_tail2.csv (187 rows) 430032a6896ffdeb296cac1dc4a95d59e8348c2b1fc369b338e8a309f9660b4c; fourth_tail3.csv (272 rows) f3a48a67388492b3c2382dd80a441c6d42bb43f3806d5b72d3cc46c5f5ae7241. Each raw CSV preserved in local reproduction archive. The new coverage-mask optimizer was separately evaluated, not used in this adaptive run.

Cumulative 2393/2393 first-pass roots have a completed status: 1600 YES, 10 NO, 783 cap-UNKNOWN. Ordered 4695 histories: 3228 YES, 18 NO, 1449 cap-UNKNOWN. The definitive classifications are 1610/2393; the 783 remain unresolved, not unrun. Full 25-column strategy remains open, M14=25..27, finite exceptions exact 35/82. Next: keep 1600 YES and 10 NO; target the 783 remaining difficult roots. Apply exact certificate budget tests at smaller remaining depths with selective invocation and measure cost versus unchanged solver. Raw CSVs and witness CSV in local archive; report gives all new status IDs and exact executed optimizer. AUTHOR_PROVED / EXACT_FINITE_CERTIFICATE_OPTIMIZATION_AND_PARTIAL_BRANCH_REPLAY / PARENT_DEPENDENT / NOT_REVIEWED.
