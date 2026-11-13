#!/usr/bin/env python3
"""Frozen R5 lexicographic coverage frontier: monotone midpoint scan vs binary search.
All scientific decisions use exact integer and rational arithmetic; no deps outside stdlib.
"""
import json, time, statistics, tracemalloc
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from bisect import bisect_left, bisect_right
from hashlib import sha256

PIN='435e77af0d180eac32bd1f9c4c464bc4010b7551'
WEIGHTS=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
OLD56='d500a95a516544511a50596555556a5a441665a66a9195956669611456565551aa5669aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa6a00'

def frozen_events():
    pools={3:set(),12:set(),15:set()}
    for mask in range(1,1<<15):
        n=-sum(a for i,a in enumerate(WEIGHTS) if mask>>i&1)
        k=-sum(a for i,a in enumerate(K0) if mask>>i&1)
        if n>=3 and k%36==0 and k//36 in pools:
            pools[k//36].add(n)
    assert [len(pools[q]) for q in (3,12,15)] == [538,298,229]
    h=Counter((1-Fraction(36*q,n))/23 for q in pools for n in pools[q])
    assert len(h)==953 and Counter(h.values())=={1:869,2:56,3:28}
    x=[0]
    for t in sorted(h): x.append(x[-1]+h[t])
    assert len(x)==954 and x[-1]==1065
    return x

def fast_frozen_events():
    """Exact one-bit subset recurrence and reduced-ratio threshold ordering."""
    size=1<<len(WEIGHTS)
    ns=[0]*size;ks=[0]*size
    pools={3:set(),12:set(),15:set()}
    for mask in range(1,size):
        lb=mask & -mask
        i=lb.bit_length()-1
        prior=mask^lb
        n=ns[mask]=ns[prior]-WEIGHTS[i]
        k=ks[mask]=ks[prior]-K0[i]
        if n>=3 and k%36==0:
            q=k//36
            if q in pools:pools[q].add(n)
    assert [len(pools[q]) for q in (3,12,15)] == [538,298,229]
    # t=(1-36q/n)/23; on positive n,q, t strictly increases with n/q.
    # Identical ratios are identical threshold values and must retain multiplicity.
    ratios=Counter(Fraction(n,q) for q in pools for n in pools[q])
    assert len(ratios)==953 and Counter(ratios.values())=={1:869,2:56,3:28}
    x=[0]
    for z in sorted(ratios):x.append(x[-1]+ratios[z])
    assert len(x)==954 and x[-1]==1065
    return x

def bench_events(repeats=11):
    out={'baseline':[],'recurrence':[]}
    for i in range(repeats):
        order=(('baseline',frozen_events),('recurrence',fast_frozen_events)) if i%2==0 else (('recurrence',fast_frozen_events),('baseline',frozen_events))
        for label,fun in order:
            start=time.perf_counter_ns()
            assert fun()==_expected_events
            out[label].append((time.perf_counter_ns()-start)/1e6)
    a=statistics.median(out['baseline']);b=statistics.median(out['recurrence'])
    return {'baseline_ms_median':round(a,5),'recurrence_ms_median':round(b,5),'speedup':round(a/b,4)}

def original_centers():
    raw=bytes.fromhex(OLD56)
    assert len(raw)==56 and sha256(raw).hexdigest()=='bf4f377e8a3b9823d589d0f5c5b0b5973f374a09aa986d5b729bc695c5de0326'
    bits=int.from_bytes(raw[2:],'little')
    cs=[bits&3];bits>>=2
    for _ in range(212):
        d=bits&3;bits>>=2
        assert d<=2
        cs.append(cs[-1]+3+d)
    assert bits==0 and (len(cs),cs[0],cs[-1])==(213,1,952)
    return cs

def objective(x, cs):
    d=[min(abs(z-x[p]) for p in cs) for z in x]
    return max(d),sum(d)

def slow_baseline(x, r):
    n=len(x); pref=[0]
    for a in x:pref.append(pref[-1]+a)
    U=[bisect_right(x,z+r)-1 for z in x]
    V=[bisect_left(x,z-r) for z in x]
    def cost(p,q):
        j=bisect_right(x,(x[p]+x[q])//2,p+1,q+1)
        return (pref[j]-pref[p+1])-(j-p-1)*x[p] + (q-j+1)*x[q]-(pref[q+1]-pref[j])
    dp=[None]*n; ways=[0]*n; succ=[None]*n; edges=0
    for p in range(n-1,-1,-1):
        best=(1,(pref[n]-pref[p+1])-(n-p-1)*x[p]) if U[p]==n-1 else None
        count=1 if best is not None else 0; nxt=None
        for q in range(p+1,min(n,p+2*r+2)):
            if V[q]>U[p]+1:continue
            edges+=1
            if dp[q] is None:continue
            a=(dp[q][0]+1,dp[q][1]+cost(p,q))
            if best is None or a<best:
                best=a;count=ways[q];nxt=q
            elif a==best:
                count+=ways[q]
                if nxt is not None and q<nxt:nxt=q
        dp[p]=best;ways[p]=count;succ[p]=nxt
    opt=None; count=0;pstart=None
    for p in range(n):
        if x[p]-x[0]>r:break
        if dp[p] is None:continue
        cand=(dp[p][0],dp[p][1]+p*x[p]-pref[p])
        if opt is None or cand<opt:opt=cand;count=ways[p];pstart=p
        elif cand==opt:count+=ways[p]
    cs=[];p=pstart
    while p is not None:cs.append(p);p=succ[p]
    return (opt,count,tuple(cs),edges)

def linear_midpoint_dp(x,r):
    """O(N(2R+1)) integer ops, O(N) words; exact optimal tuple/count/first path."""
    n=len(x);pref=[0]
    for z in x:pref.append(pref[-1]+z)
    # Two monotone pointers compute coverage endpoints in O(N).
    L=[0]*n;U=[0]*n
    a=b=0
    for p,z in enumerate(x):
        while a<n and x[a]<z-r:a+=1
        if b<p:b=p
        while b+1<n and x[b+1]<=z+r:b+=1
        L[p]=a;U[p]=b
    dp=[None]*n;ways=[0]*n;succ=[None]*n;edges=0;midpoint_visits=0
    for p in range(n-1,-1,-1):
        xp=x[p]
        best=(1,(pref[n]-pref[p+1])-(n-p-1)*xp) if U[p]==n-1 else None
        count=int(best is not None);nxt=None
        m=p+1
        for q in range(p+1,min(n,p+2*r+2)):
            # As q advances, the midpoint threshold is monotone.
            xq=x[q]
            while m<=q and 2*x[m]<=xp+xq:
                m+=1;midpoint_visits+=1
            if L[q]>U[p]+1:continue
            edges+=1
            if dp[q] is None:continue
            w=(pref[m]-pref[p+1])-(m-p-1)*xp + (q-m+1)*xq-(pref[q+1]-pref[m])
            cand=(dp[q][0]+1,dp[q][1]+w)
            if best is None or cand<best:
                best=cand;count=ways[q];nxt=q
            elif cand==best:
                count+=ways[q]
                if nxt is not None and q<nxt:nxt=q
        dp[p]=best;ways[p]=count;succ[p]=nxt
    opt=None;count=0;start=None
    for p in range(n):
        if x[p]-x[0]>r:break
        if dp[p] is None:continue
        cand=(dp[p][0],dp[p][1]+p*x[p]-pref[p])
        if opt is None or cand<opt:opt=cand;count=ways[p];start=p
        elif cand==opt:count+=ways[p]
    cs=[];p=start
    while p is not None:cs.append(p);p=succ[p]
    return (opt,count,tuple(cs),edges),midpoint_visits

def exhaustive():
    cases=0;checks=0
    for n in range(1,8):
        for increments in product((1,2,3),repeat=n-1):
            x=[0]
            for d in increments:x.append(x[-1]+d)
            for r in range(6):
                got,scan=linear_midpoint_dp(x,r)
                ref=slow_baseline(x,r)
                assert got==ref,(x,r,got,ref)
                best=None;num=0;first=None
                for k in range(1,n+1):
                    for cs in combinations(range(n),k):
                        d,j=objective(x,cs);checks+=1
                        if d>r:continue
                        tup=(k,j)
                        if best is None or tup<best:best=tup;num=1;first=cs
                        elif tup==best:num+=1;first=min(first,cs)
                    if best is not None:break
                assert got[:3]==(best,num,first)
                cases+=1
    return cases,checks

def bench(x, r, repeats=9):
    first=linear_midpoint_dp(x,r)[0]
    assert first==slow_baseline(x,r)
    a=[];b=[]
    for z in range(repeats):
        if z&1:
            f=linear_midpoint_dp;g=slow_baseline
        else:
            g=slow_baseline;f=linear_midpoint_dp
        for fun,out in ((f,a if f is linear_midpoint_dp else b),(g,b if g is slow_baseline else a)):
            t=time.perf_counter_ns()
            val=fun(x,r)
            out.append((time.perf_counter_ns()-t)/1000000)
            assert (val[0] if fun is linear_midpoint_dp else val)==first
    return {'R':r,'baseline_ms_median':round(statistics.median(b),5),'linear_ms_median':round(statistics.median(a),5),'speedup':round(statistics.median(b)/statistics.median(a),4)}

def bench_full(x,repeats=11):
    comparisons=[]
    for r in (2,9,36):
        samples={"old":[],"new":[]}
        for t in range(repeats):
            for label,proc,dp in ((("old",frozen_events,slow_baseline),("new",fast_frozen_events,linear_midpoint_dp)) if t%2==0 else (("new",fast_frozen_events,linear_midpoint_dp),("old",frozen_events,slow_baseline))):
                tic=time.perf_counter_ns()
                z=proc()
                outcome=dp(z,r)
                assert z==x
                samples[label].append((time.perf_counter_ns()-tic)/1e6)
        a=statistics.median(samples["old"]); b=statistics.median(samples["new"])
        comparisons.append({"R":r,"baseline_ms_median":round(a,5),"new_ms_median":round(b,5),"speedup":round(a/b,4)})
    return comparisons

def main():
    global _expected_events
    _expected_events=frozen_events()
    x=fast_frozen_events();cs=original_centers()
    assert x==_expected_events
    assert objective(x,cs)==(2,1070)
    cases,checks=exhaustive()
    census=[];visits=0
    for r in range(37):
        got,v=linear_midpoint_dp(x,r)
        ref=slow_baseline(x,r)
        assert got==ref,(r,got[:2],ref[:2])
        (k,j),nways,centers,edges=got
        if r in (0,1,2,9,25,26,36):census.append({'R':r,'K':k,'J':j,'ways':str(nways),'edges':edges,'midpoint_visits':v})
        visits+=v
    assert [(c['K'],c['J']) for c in census if c['R'] in (2,9,36)]==[(213,1070),(57,4384),(15,16813)]
    timings=[bench(x,r) for r in (2,9,36)]
    event_timing=bench_events()
    total_timings=bench_full(x)
    print(json.dumps({'status':'PASS','pin':PIN,'case_count':cases,'subset_count':checks,'frozen_boundaries':len(x),'frozen_events':x[-1],'radii_verified':37,'midpoint_visits_all_radii':visits,'selected_rows':census,'benchmark':timings,'event_build_benchmark':event_timing,'full_build_and_dp_benchmark':total_timings},indent=2))

if __name__=='__main__':main()
