#!/usr/bin/env python3
"""Pinned BRC R5: exact fixed-radius, all-cardinalities K/J Pareto frontier.
Independent stdlib implementation; original 15-atom integer input from
awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551.
"""
from fractions import Fraction
from collections import Counter
from bisect import bisect_left, bisect_right
from itertools import combinations, product
import json, hashlib
from pathlib import Path

PIN='435e77af0d180eac32bd1f9c4c464bc4010b7551'
W=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)

def frozen_x():
    pools={3:set(),12:set(),15:set()}
    n=k=mask=0
    for i in range(1,1<<len(W)):
        j=(i&-i).bit_length()-1;bit=1<<j;mask^=bit
        if mask&bit:n-=W[j];k-=K0[j]
        else:n+=W[j];k+=K0[j]
        assert mask==i^(i>>1)
        if n>=3 and k%36==0 and k//36 in pools:pools[k//36].add(n)
    assert [len(pools[q]) for q in (3,12,15)]==[538,298,229]
    mult=Counter(Fraction(n,q) for q in pools for n in pools[q])
    assert len(mult)==953 and Counter(mult.values())=={1:869,2:56,3:28}
    x=[0]
    for t in sorted(mult):x.append(x[-1]+mult[t])
    assert len(x)==954 and x[-1]==1065
    return x

def frontier(x, radius):
    N=len(x);P=[0]
    for z in x:P.append(P[-1]+z)
    U=[bisect_right(x,z+radius)-1 for z in x]
    L=[bisect_left(x,z-radius) for z in x]
    # Each edge's additive Voronoi contribution excludes p, includes q.
    incoming=[[] for _ in x]
    for p in range(N):
        for q in range(p+1,min(N,p+2*radius+2)):
            if L[q]>U[p]+1:continue
            middle=bisect_right(x,(x[p]+x[q])//2,p+1,q+1)
            cost=(P[middle]-P[p+1])-(middle-p-1)*x[p] + (q-middle+1)*x[q]-(P[q+1]-P[middle])
            incoming[q].append((p,cost))
    # We only track costs: O(N) states, O(K |E|) operations.
    prev=[None]*N
    for q in range(N):
        if x[q]-x[0]<=radius: prev[q]=q*x[q]-P[q]
    rows={}
    edges=sum(len(a) for a in incoming)
    min_cardinality=None
    for count in range(1,N+1):
        candidates=[(v+(P[N]-P[q+1])-(N-q-1)*x[q],q) for q,v in enumerate(prev) if v is not None and U[q]==N-1]
        if candidates:
            val,q=min(candidates)
            rows[count]=(val,q)
            if min_cardinality is None:min_cardinality=count
        if count==N:break
        curr=[None]*N
        for q,arr in enumerate(incoming):
            best=None
            for p,w in arr:
                if prev[p] is not None:
                    t=prev[p]+w
                    if best is None or t<best:best=t
            curr[q]=best
        prev=curr
        if all(v is None for v in prev):break
    assert rows and rows[max(rows)][0]==0 and len(rows)==N-min_cardinality+1
    return {"R":radius,"N":N,"edges":edges,"min_K":min_cardinality,"all":rows}

def tiny_brute(x,r):
    f=frontier(x,r)['all']
    direct={}
    for k in range(1,len(x)+1):
        vals=[]
        for cs in combinations(range(len(x)),k):
            err=[min(abs(x[b]-x[s]) for s in cs) for b in range(len(x))]
            if max(err)<=r:vals.append(sum(err))
        if vals:direct[k]=min(vals)
    assert {k:v[0] for k,v in f.items()}==direct,(x,r,f,direct)

def greedy_min_centers(x,r):
    i=count=0
    while i<len(x):
        p=bisect_right(x,x[i]+r)-1
        i=bisect_right(x,x[p]+r)
        count+=1
    return count

def run():
    small=0
    for n in range(1,8):
        for gaps in product((1,2,3),repeat=n-1):
            x=[0]
            for d in gaps:x.append(x[-1]+d)
            for r in range(3):
                tiny_brute(x,r); small+=1
    X=frozen_x(); result=frontier(X,2)
    curve=[(k,v[0]) for k,v in sorted(result['all'].items())]
    assert curve[0]==(213,1070) and curve[-1]==(954,0)
    assert greedy_min_centers(X,2)==213 and greedy_min_centers(X,1)==351
    assert next(k for k,j in curve if j==954-k)==351
    assert all(a>=b for (_,a),(_,b) in zip(curve,curve[1:]))
    # One marginal improvement per extra center, may or may not decrease monotonically.
    improvements=[(curve[i][0],curve[i-1][1]-curve[i][1]) for i in range(1,len(curve))]
    irregular=[(improvements[i-1],improvements[i]) for i in range(1,len(improvements)) if improvements[i][1]>improvements[i-1][1]]
    # digest of all K,J rows using canonical ASCII lines, stable independent of JSON serialization
    payload=''.join(f'{k},{j}\n' for k,j in curve)
    result={"status":"PASS_EXACT","pin":PIN,"scope":"R=2; 954 frozen event-coordinate boundaries; exact integer arithmetic; all K in [213,954]","small_bruteforce_cases":small,"edges":result['edges'],"rows":len(curve),"K_min_R1":greedy_min_centers(X,1),"K_min_R2":greedy_min_centers(X,2),"saturation_threshold_K":351, "cost_sum":sum(j for _,j in curve),"weighted_cost_sum":sum(k*j for k,j in curve),"first_twelve":curve[:12],"last_twelve":curve[-12:],"selected":{str(k):result['all'][k][0] for k in [213,214,215,220,230,250,300,400,500,600,700,800,900,954]},"nonconvex_improvement_pairs_count":len(irregular),"first_nonconvex_pairs":irregular[:10],"marginal_histogram":dict(sorted(Counter(z[1] for z in improvements).items())),"max_marginal_gain":max(z[1] for z in improvements),"min_marginal_gain":min(z[1] for z in improvements),"curve_sha256":hashlib.sha256(payload.encode()).hexdigest(),"curve_lines":len(curve)}
    print(json.dumps(result,indent=2))
    with open(Path(__file__).with_name('EXACT_FRONTIER.csv'),'w') as f:f.write('K,J\n'+payload)
    with open(Path(__file__).with_name('EXACT_OUTPUT.json'),'w') as f:json.dump(result,f,indent=2)

if __name__=='__main__':run()
