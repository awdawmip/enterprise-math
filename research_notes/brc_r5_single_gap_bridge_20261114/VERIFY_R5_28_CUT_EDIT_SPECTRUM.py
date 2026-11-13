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

# Full 28 individual 3->2 gap closure edit spectrum; generated as a standalone
# extension of the exact center-path/optimal-language kernel above.
def verify_r5_28_cut_edit_spectrum():
    from collections import Counter
    from itertools import combinations
    X,B = frozen_blocks()
    original = [local_dp(b) for b in B]
    m0=[min(d[0]) for d in original]
    assert len(X)==954 and len(B)==29 and sum(m0)==213
    assert sum(d[0][m][0] for d,m in zip(original,m0))==1070
    per_cut=[]; local_checks=0; concavity_checks=0
    for cut in range(28):
        joined = tuple(B[cut])+tuple(y-1 for y in B[cut+1])
        jd=local_dp(joined)
        components=[(str(j),tuple(B[j]),original[j])
                    for j in range(29) if j not in (cut,cut+1)]
        components.append(("joined",joined,jd))
        base_cost=0; min_centers=0; gains=[]
        candidates={5:[],6:[],7:[]}
        for label,b,d in components:
            m=min(d[0]); base_cost+=d[0][m][0];min_centers+=m
            differences=[d[0][k][0]-d[0][k+1][0] for k in range(m,len(b))]
            assert all(a>=b for a,b in zip(differences,differences[1:])),(cut,label)
            concavity_checks+=max(0,len(differences)-1)
            gains.extend(differences)
            for k,g in enumerate(differences,m):
                if g not in (5,6,7):continue
                candidate=minimum_removed(b,d,k,k+1,1 if g==5 else 4)
                if g==5:assert candidate is None,(cut,label,k)
                if g==6:assert candidate is not None and candidate[0]==3,(cut,label,k)
                if g==7:assert candidate is not None and candidate[0]==4,(cut,label,k)
                candidates[g].append((label,k))
                local_checks+=1
        ranked=sorted(gains,reverse=True)
        assert (min_centers,base_cost) in {(213,1070),(212,1077),(212,1075),(212,1076)}
        assert [base_cost-sum(ranked[:k-min_centers]) for k in range(214,223)] == [
            1064,1059,1054,1049,1044,1039,1034,1029,1024],cut
        if min_centers==212:
            assert cut in (5,6,8,9,16)
            rho212=4 if cut in (5,6) else 3
            assert ranked[0] == (7 if cut in (5,6) else 6)
            assert (len(candidates[7]),len(candidates[6])) == (
                (1,1) if cut in (5,6) else ((0,2) if cut==16 else (0,1)))
        else:rho212=None
        rho213=2 if cut in (8,9) else 3
        assert ranked[213-min_centers] == (5 if cut in (8,9) else 6)
        assert all(g==5 for g in ranked[214-min_centers:222-min_centers])
        assert len(candidates[5])>=8
        per_cut.append({
          "cut":cut,"minimum_centers":min_centers,
          "rho_212_to_213":rho212,"rho_213_to_214":rho213,
          "rho_214_to_222":"2 for all 8 steps",
          "gain5_local_checks":len(candidates[5]),
          "gain6_local_checks":len(candidates[6]),
          "gain7_local_checks":len(candidates[7])})
    assert [a["cut"] for a in per_cut if a["rho_212_to_213"] is not None] == [5,6,8,9,16]
    # Independent complete subset enumeration for a declared finite universe.
    cases=adjacent_checks=0
    for n in range(2,8):
        for tail in combinations(range(1,11),n-1):
            points=(0,)+tail;d=local_dp(points);opts={}
            for k in range(1,n+1):
                for s in combinations(range(n),k):
                    ds=[min(abs(v-points[z]) for z in s) for v in points]
                    if max(ds)>2:continue
                    cost=sum(ds)
                    if k not in opts or cost<opts[k][0]:opts[k]=(cost,[s])
                    elif cost==opts[k][0]:opts[k][1].append(s)
            assert {k:v[0] for k,v in opts.items()} == {k:v[0] for k,v in d[0].items()}
            for k in range(min(opts),n):
                truth=min(len(set(s)-set(t)) for s in opts[k][1] for t in opts[k+1][1])
                got=minimum_removed(points,d,k,k+1,n)
                assert got is not None and got[0]==truth
                adjacent_checks+=1
            cases+=1
    assert (cases,adjacent_checks)==(847,2518)
    rh=Counter()
    for item in per_cut:
        if item["rho_212_to_213"] is not None:rh[item["rho_212_to_213"]]+=1
        rh[item["rho_213_to_214"]]+=1
        rh[2]+=8; rh[1]+=70; rh[0]+=662
    assert rh=={0:18536,1:1960,2:226,3:29,4:2}
    assert (local_checks,concavity_checks)==(257,19969)
    result={
       "status":"PASS_EXACT_28_CUT_EDIT_SPECTRUM",
       "science_pin":PIN,"integer_event_boundaries":954,"radius":2,
       "old_blocks":29,"single_gap_closures":28,
       "complete_transition_instances":sum(rh.values()),
       "rho_histogram":dict(sorted(rh.items())),
       "small_exhaustive_instances":cases,
       "small_adjacent_budget_checks":adjacent_checks,
       "local_gain_5_6_7_product_checks":local_checks,
       "checked_concavity_comparisons":concavity_checks,
       "per_cut":per_cut}
    print(json.dumps(result,sort_keys=True,indent=2))

if __name__=="__main__":
    verify_r5_28_cut_edit_spectrum()
