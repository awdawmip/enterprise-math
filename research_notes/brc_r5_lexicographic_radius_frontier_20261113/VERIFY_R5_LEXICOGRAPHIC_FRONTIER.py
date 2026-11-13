#!/usr/bin/env python3
"""Exact lexicographic minimum-center/mean-cost radius frontier, frozen R5 pin."""
import json
from bisect import bisect_left, bisect_right
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from hashlib import sha256

PIN = '435e77af0d180eac32bd1f9c4c464bc4010b7551'
WEIGHTS = (336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0 = (-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
OLD56 = 'd500a95a516544511a50596555556a5a441665a66a9195956669611456565551aa5669aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa6a00'

def frozen_events():
    pools = {3:set(),12:set(),15:set()}
    for mask in range(1,1<<15):
        n = -sum(a for i,a in enumerate(WEIGHTS) if mask>>i&1)
        k = -sum(a for i,a in enumerate(K0) if mask>>i&1)
        if n>=3 and k%36==0 and k//36 in pools: pools[k//36].add(n)
    assert [len(pools[q]) for q in (3,12,15)] == [538,298,229]
    h = Counter((1-Fraction(36*q,n))/23 for q in pools for n in pools[q])
    assert len(h)==953 and Counter(h.values())=={1:869,2:56,3:28}
    x = [0]
    for t in sorted(h): x.append(x[-1]+h[t])
    assert len(x)==954 and x[-1]==1065
    return x

def legacy_centers():
    raw = bytes.fromhex(OLD56)
    assert len(raw)==56 and sha256(raw).hexdigest()=='bf4f377e8a3b9823d589d0f5c5b0b5973f374a09aa986d5b729bc695c5de0326'
    bits = int.from_bytes(raw[2:],'little')
    cs = [bits&3]; bits >>= 2
    for _ in range(212):
        d = bits&3; bits >>= 2
        assert d<=2
        cs.append(cs[-1]+3+d)
    assert bits==0 and (len(cs),cs[0],cs[-1])==(213,1,952)
    return cs

def objective(x,centers):
    ds = [min(abs(z-x[p]) for p in centers) for z in x]
    return max(ds),sum(ds)

def greedy_count(x,r):
    n=len(x)
    left=[bisect_left(x,v-r) for v in x]
    right=[bisect_right(x,v+r)-1 for v in x]
    first=0; cs=[]; witnesses=[]
    while first<n:
        p=bisect_right(left,first)-1
        assert p>=first and left[p]<=first<=right[p]
        cs.append(p); witnesses.append(first)
        first=right[p]+1
    assert all(not (left[p]<=a and b<=right[p])
               for p in range(n) for a,b in zip(witnesses,witnesses[1:]))
    return cs,witnesses

def lexicographic_dp(x,r):
    n=len(x)
    U=[bisect_right(x,x[p]+r)-1 for p in range(n)]
    V=[bisect_left(x,x[p]-r) for p in range(n)]
    pref=[0]
    for z in x: pref.append(pref[-1]+z)
    def edge_cost(p,q):
        j=bisect_right(x,(x[p]+x[q])//2,p+1,q+1)
        left=(pref[j]-pref[p+1])-(j-p-1)*x[p]
        right=(q-j+1)*x[q]-(pref[q+1]-pref[j])
        return left+right
    def head(p): return p*x[p]-pref[p]
    def tail(p): return (pref[n]-pref[p+1])-(n-p-1)*x[p]
    dp=[None]*n; ways=[0]*n; succ=[None]*n; edges=0
    for p in range(n-1,-1,-1):
        options=[]
        if U[p]==n-1: options.append(((1,tail(p)),1,None))
        for q in range(p+1,min(n,p+2*r+2)):
            if V[q]>U[p]+1: continue
            edges+=1
            if dp[q] is not None:
                k,c=dp[q]
                options.append(((k+1,c+edge_cost(p,q)),ways[q],q))
        if options:
            best=min(z[0] for z in options)
            dp[p]=best
            ways[p]=sum(z[1] for z in options if z[0]==best)
            succ[p]=min((z[2] for z in options if z[0]==best),
                        key=lambda q:-1 if q is None else q)
    starts=[]
    for p in range(n):
        if x[p]-x[0]<=r and dp[p] is not None:
            k,c=dp[p]
            starts.append(((k,c+head(p)),ways[p],p))
    opt=min(z[0] for z in starts)
    count=sum(z[1] for z in starts if z[0]==opt)
    p=min(z[2] for z in starts if z[0]==opt)
    centers=[]
    while p is not None:
        centers.append(p); p=succ[p]
    assert len(centers)==opt[0]
    dist,cost=objective(x,centers)
    assert dist<=r and cost==opt[1]
    return {'K':opt[0],'J':opt[1],'ways':count,'centers':centers,'edges':edges}

def exhaustive_small():
    tests=subsets=ties=0
    for n in range(1,8):
        for steps in product((1,2,3),repeat=n-1):
            x=[0]
            for a in steps: x.append(x[-1]+a)
            for r in range(6):
                valid=[]
                for k in range(1,n+1):
                    for cs in combinations(range(n),k):
                        d,j=objective(x,cs)
                        subsets+=1
                        if d<=r:valid.append((k,j,cs))
                    if valid:break
                best=min((k,j) for k,j,cs in valid)
                count=sum((k,j)==best for k,j,cs in valid)
                got=lexicographic_dp(x,r)
                assert (got['K'],got['J'],got['ways'])==(*best,count)
                assert tuple(got['centers'])==min(cs for k,j,cs in valid if (k,j)==best)
                tests+=1;ties+=(count>1)
    return {'input_radius_cases':tests,'subsets_evaluated':subsets,'tie_cases':ties}

def main():
    x=frozen_events()
    assert objective(x,legacy_centers())==(2,1070)
    small=exhaustive_small()
    rows=[]
    for r in range(37):
        result=lexicographic_dp(x,r)
        gc,gw=greedy_count(x,r)
        assert result['K']==len(gc)==len(gw) and objective(x,gc)[0]<=r
        rows.append({'R':r,'K':result['K'],'J':result['J'],
                     'ways':str(result['ways']),
                     'greedy_J':objective(x,gc)[1], 'edges':result['edges'],
                     'first':result['centers'][:8],
                     'last':result['centers'][-8:]})
    assert [(rows[r]['K'],rows[r]['J']) for r in (2,9,36)]==[(213,1070),(57,4384),(15,16813)]
    assert rows[2]['ways']=='1338767625695954932334592000'
    assert [z['R'] for z in rows if z['greedy_J']==z['J']]==[0,1]
    print(json.dumps({'status':'PASS_EXACT_LEXICOGRAPHIC_RADIUS_PARETO',
                      'frozen_pin':PIN,'boundaries':954,'events':1065,
                      'small_exhaustive':small,'rows':rows},
                     ensure_ascii=False,indent=2))

if __name__=='__main__': main()
