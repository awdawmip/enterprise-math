#!/usr/bin/env python3
"""Frozen R5 exact allocation-coupled optimal-set edit, standard library only.
Proof scope: integer event-boundary radius 2, NOT native 28-coordinate workload.
Run: python VERIFY_R5_ALLOCATION_EDIT.py
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
import json

PIN = "435e77af0d180eac32bd1f9c4c464bc4010b7551"
W = (336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0 = (-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)

def frozen_blocks():
    pools={3:set(),12:set(),15:set()}
    mask=n=k=0
    for step in range(1,1<<15):
        bit=step&-step
        i=bit.bit_length()-1
        mask^=bit
        sign=1 if mask&bit else -1
        n+=sign*W[i]
        k+=sign*K0[i]
        assert mask == (step^(step>>1))
        if n>=3 and k%36==0 and k//36 in pools:
            pools[k//36].add(n)
    assert [len(pools[t]) for t in (3,12,15)] == [538,298,229]
    events=Counter(Fraction(p,q) for q,vs in pools.items() for p in vs)
    assert len(events)==953 and Counter(events.values())=={1:869,2:56,3:28}
    x=[0]
    for w in sorted(events): x.append(x[-1]+events[w])
    assert len(x)==954 and x[-1]==1065
    blocks=[];left=0
    for i in range(1,len(x)):
        if x[i]-x[i-1]>2:
            blocks.append(x[left:i])
            left=i
    blocks.append(x[left:])
    assert len(blocks)==29
    return x,blocks

def local_dp(x):
    n=len(x)
    incoming=[[] for _ in x]
    for p in range(n):
        for q in range(p+1,min(n,p+6)):
            vals=[min(x[b]-x[p],x[q]-x[b]) for b in range(p+1,q)]
            if all(v<=2 for v in vals):
                incoming[q].append((p,sum(vals)))
    row=[None]*n
    for p in range(n):
        if x[p]-x[0]<=2:
            row[p]=(sum(x[p]-x[b] for b in range(p)),1)
    rows=[row];answer={}
    for budget in range(1,n+1):
        ends=[(p,v[0]+sum(x[b]-x[p] for b in range(p+1,n)),v[1])
              for p,v in enumerate(row) if v is not None and x[-1]-x[p]<=2]
        if ends:
            best=min(v for _,v,_ in ends)
            answer[budget]=(best,sum(c for _,v,c in ends if v==best))
        if budget==n: break
        nxt=[None]*n
        for q,edges in enumerate(incoming):
            vals=[(row[p][0]+w,row[p][1]) for p,w in edges if row[p]]
            if vals:
                m=min(z for z,_ in vals)
                nxt[q]=(m,sum(c for z,c in vals if z==m))
        row=nxt; rows.append(row)
    return answer,rows,incoming

def optimal_language(x,summary,k):
    answers,rows,incoming=summary
    best=answers[k][0]
    good=[set() for _ in range(k+1)]
    for q,item in enumerate(rows[k-1]):
        if item and x[-1]-x[q]<=2 and item[0]+sum(x[b]-x[q] for b in range(q+1,len(x)))==best:
            good[k].add(q)
    for t in range(k,1,-1):
        for q in good[t]:
            val=rows[t-1][q][0]
            for p,w in incoming[q]:
                if rows[t-2][p] and rows[t-2][p][0]+w==val:
                    good[t-1].add(p)
    nxt={(0,-1):tuple(sorted(good[1]))}
    for t in range(1,k):
        for p in good[t]: nxt[(t,p)]=[]
        for q in good[t+1]:
            for p,w in incoming[q]:
                if p in good[t] and rows[t-1][p][0]+w==rows[t][q][0]:
                    nxt[t,p].append(q)
    return {z:tuple(sorted(v)) for z,v in nxt.items()}

def minimum_removed(x,summary,k,l,limit):
    """Exact if delta<=limit; None establishes delta>limit. Also returns witness."""
    old=optimal_language(x,summary,k)
    new=optimal_language(x,summary,l)
    for bound in range(max(0,k-l),limit+1):
        new_bound=bound+l-k
        if new_bound<0:continue
        @lru_cache(None)
        def visit(i,p,j,q,d,a):
            if d>bound or a>new_bound:return None
            if i==k and j==l:
                return () if d==bound and a==new_bound else None
            if i<k and j<l:
                for c in sorted(set(old.get((i,p),()))&set(new.get((j,q),()))):
                    tail=visit(i+1,c,j+1,c,d,a)
                    if tail is not None:return (("same",c),)+tail
            if i<k and d<bound:
                for c in old.get((i,p),()):
                    tail=visit(i+1,c,j,q,d+1,a)
                    if tail is not None:return (("old",c),)+tail
            if j<l and a<new_bound:
                for c in new.get((j,q),()):
                    tail=visit(i,p,j+1,c,d,a+1)
                    if tail is not None:return (("new",c),)+tail
            return None
        alignment=visit(0,-1,0,-1,0,0)
        if alignment is not None:
            s=tuple(v for typ,v in alignment if typ!="new")
            t=tuple(v for typ,v in alignment if typ!="old")
            assert len(s)==k and len(t)==l and s==tuple(sorted(set(s))) and t==tuple(sorted(set(t)))
            assert len(set(s)-set(t))==bound
            for centers,budget in ((s,k),(t,l)):
                distances=[min(abs(y-x[z]) for z in centers) for y in x]
                assert max(distances)<=2 and sum(distances)==summary[0][budget][0]
            return bound,s,t
    return None

def optimal_allocations(summaries,minimum,u):
    dps={0:(0,[()])}
    for summary,m in zip(summaries,minimum):
        nxt={}
        for used,(cost,allocs) in dps.items():
            for v in range(u-used+1):
                newcost=cost+summary[0][m+v][0]-summary[0][m][0]
                idx=used+v
                variants=[a+(v,) for a in allocs]
                if idx not in nxt or newcost<nxt[idx][0]:
                    nxt[idx]=(newcost,variants)
                elif newcost==nxt[idx][0]:
                    nxt[idx][1].extend(variants)
        dps=nxt
    return dps[u]

def crosscheck():
    cases=pairs=feasible=0
    for n in range(2,7):
        for tail in combinations(range(1,9),n-1):
            x=(0,)+tail
            summary=local_dp(x)
            opts={}
            for k in range(1,n+1):
                for c in combinations(range(n),k):
                    distances=[min(abs(y-x[z]) for z in c) for y in x]
                    if max(distances)>2:continue
                    feasible+=1
                    score=sum(distances)
                    if k not in opts or score<opts[k][0]:
                        opts[k]=(score,[c])
                    elif score==opts[k][0]:opts[k][1].append(c)
            assert {k:z[0] for k,z in opts.items()}=={k:z[0] for k,z in summary[0].items()}
            for k in opts:
                for l in opts:
                    if k==l:continue
                    truth=min(len(set(s)-set(t)) for s in opts[k][1] for t in opts[l][1])
                    guess=minimum_removed(x,summary,k,l,n)
                    assert guess and guess[0]==truth,(x,k,l,truth,guess)
                    pairs+=1
            cases+=1
    return {"input_sets":cases,"ordered_budget_pairs":pairs,"feasible_subsets":feasible}

def main():
    x,blocks=frozen_blocks()
    summaries=[local_dp(b) for b in blocks]
    minimum=[min(d[0]) for d in summaries]
    assert sum(minimum)==213
    base=sum(d[0][m][0] for d,m in zip(summaries,minimum))
    assert base==1070
    fronts=[optimal_allocations(summaries,minimum,u) for u in range(5)]
    costs=[base+item[0] for item in fronts]
    assert costs==[1070,1064,1059,1054,1049]
    cache={}
    transitions=[]
    for u in range(4):
        best=None;tested=0
        for a in fronts[u][1]:
            for b in fronts[u+1][1]:
                tested+=1
                subtotal=0;changed=[];infeasible=False
                for i,(p,q) in enumerate(zip(a,b)):
                    if p==q:continue
                    key=(i,p,q)
                    if key not in cache:
                        cache[key]=minimum_removed(blocks[i],summaries[i],minimum[i]+p,minimum[i]+q,5)
                    res=cache[key]
                    if res is None:
                        infeasible=True
                        break
                    subtotal+=res[0]
                    changed.append((i,p,q,res))
                if infeasible:continue  # no pair with <=5 removals in a changed block
                score=(subtotal,sum(len(blocks[i]) for i,_,_,_ in changed))
                if best is None or score<best[0]:best=(score,changed)
        assert best is not None
        rho=best[0][0]
        assert rho==[3,2,2,2][u]
        witnesses=[]
        for i,p,q,(delta,s,t) in best[1]:
            witnesses.append({
                "zero_based_block":i,"from_extra":p,"to_extra":q,
                "old": [blocks[i][z]-blocks[i][0] for z in s],
                "new": [blocks[i][z]-blocks[i][0] for z in t],
                "removed": delta
            })
        transitions.append({
            "K":213+u,"K_plus_one":214+u,
            "costs":[costs[u],costs[u+1]],"rho":rho,
            "minimum_symmetric_difference":2*rho+1,
            "allocation_pairs_checked":tested,"witness_blocks":witnesses})
    result={
        "scientific_pin":PIN,"status":"PASS_EXACT_LOCAL",
        "event_boundaries":len(x),"activation_events":x[-1],
        "independent_blocks":len(blocks),"minimum_centers":sum(minimum),
        "all_optimal_allocation_counts":[len(z[1]) for z in fronts],
        "costs_K213_to_217":costs,
        "transitions":transitions,
        "independent_exhaustive_crosscheck":crosscheck(),
        "scope":"Exact integer event-boundary radius-2 optimization, not native prefix-query benchmark"
    }
    print(json.dumps(result,sort_keys=True,indent=2))
if __name__=="__main__":main()
