#!/usr/bin/env python3
"""Frozen R5 exact radius-2 separator theorem and all-budget min-plus component DP.
Scientific data pinned to awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551.
No numpy or floating-point arithmetic.
"""
from fractions import Fraction
from collections import Counter
from itertools import product,combinations
from bisect import bisect_left,bisect_right
import hashlib,json,time
W=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
PIN='435e77af0d180eac32bd1f9c4c464bc4010b7551'

def frozen():
    pools={3:set(),12:set(),15:set()}; n=k=mask=0
    for i in range(1,1<<15):
        bit=1<<((i&-i).bit_length()-1)
        mask ^= bit; j=bit.bit_length()-1
        if mask&bit:n-=W[j];k-=K0[j]
        else:n+=W[j];k+=K0[j]
        assert mask == i^(i>>1)
        if n>=3 and k%36==0 and k//36 in pools:pools[k//36].add(n)
    assert [len(pools[q]) for q in (3,12,15)]==[538,298,229]
    mult=Counter(Fraction(n,q) for q in pools for n in pools[q])
    assert len(mult)==953 and Counter(mult.values())=={1:869,2:56,3:28}
    x=[0]
    for wall in sorted(mult):x.append(x[-1]+mult[wall])
    assert len(x)==954 and x[-1]==1065
    return x

def frontier_dp(x,R):
    N=len(x);P=[0]
    for z in x:P.append(P[-1]+z)
    U=[bisect_right(x,z+R)-1 for z in x]
    L=[bisect_left(x,z-R) for z in x]
    incoming=[[] for _ in x]
    for p in range(N):
        for q in range(p+1,min(N,p+2*R+2)):
            if L[q] > U[p]+1:continue
            middle=bisect_right(x,(x[p]+x[q])//2,p+1,q+1)
            val=P[middle]-P[p+1]-(middle-p-1)*x[p]
            val+=(q-middle+1)*x[q]-(P[q+1]-P[middle])
            incoming[q].append((p,val))
    prev=[None]*N
    for q in range(N):
        if x[q]-x[0]<=R:prev[q]=q*x[q]-P[q]
    rows={}; E=sum(map(len,incoming))
    for k in range(1,N+1):
        right=[v+P[N]-P[q+1]-(N-q-1)*x[q] for q,v in enumerate(prev) if v is not None and U[q]==N-1]
        if right:rows[k]=min(right)
        if k==N:break
        curr=[None]*N
        for q,edges in enumerate(incoming):
            costs=[prev[p]+w for p,w in edges if prev[p] is not None]
            if costs:curr[q]=min(costs)
        prev=curr
        if all(v is None for v in prev):break
    return rows,E

def split_by_radius(x,R):
    result=[]; start=0
    for i in range(len(x)-1):
        if x[i+1]-x[i]>R:
            result.append(x[start:i+1]);start=i+1
    result.append(x[start:])
    return result

def composed_frontier(x,R):
    blocks=split_by_radius(x,R)
    rows={0:0}; edge_count=0; profiles=[]
    for b in blocks:
        curve,e=frontier_dp(b,R); edge_count+=e
        profiles.append({'n':len(b),'dR':min(curve),'events_span':b[-1]-b[0]})
        nextrows={}
        for k,a in rows.items():
            for h,c in curve.items():
                z=k+h; val=a+c
                if z not in nextrows or val<nextrows[z]:nextrows[z]=val
        rows=nextrows
    return rows,profiles,edge_count

def merged_convex_frontier(x,R):
    """Exact if each component's consecutive marginal gain is nonincreasing.
    Return None when an actual component violates this sufficient condition.
    """
    import heapq
    curves=[]; total_k=0; total_j=0; heap=[]; row={}
    for i,b in enumerate(split_by_radius(x,R)):
        local,_=frontier_dp(b,R)
        k0=min(local); gains=[local[k-1]-local[k] for k in range(k0+1,len(b)+1)]
        if any(gains[j] > gains[j-1] for j in range(1,len(gains))):return None
        curves.append(gains);total_k+=k0;total_j+=local[k0]
        if gains:heapq.heappush(heap,(-gains[0],i,0))
    row[total_k]=total_j
    while heap:
        neg_g,i,j=heapq.heappop(heap)
        total_k+=1;total_j+=neg_g;row[total_k]=total_j
        if j+1<len(curves[i]):heapq.heappush(heap,(-curves[i][j+1],i,j+1))
    return row

def direct_brute(x,r):
    d={}
    for k in range(1,len(x)+1):
        v=[]
        for S in combinations(x,k):
            distance=[min(abs(z-s) for s in S) for z in x]
            if max(distance)<=r:v.append(sum(distance))
        if v:d[k]=min(v)
    return d

def run():
    tested=0; nontrivial_splits=0
    for n in range(1,8):
        for ds in product((1,2,3,4),repeat=n-1):
            x=[0]
            for d in ds:x.append(x[-1]+d)
            for r in (0,1,2,3):
                composed,parts,_=composed_frontier(x,r)
                expected=direct_brute(x,r)
                assert composed==expected,(x,r,composed,expected)
                tested+=1
                if len(parts)>1:nontrivial_splits+=1
    x=frozen();t0=time.perf_counter()
    allrows,edge_direct=frontier_dp(x,2)
    full_seconds=time.perf_counter()-t0
    t0=time.perf_counter()
    rows,profiles,edge_split=composed_frontier(x,2)
    split_seconds=time.perf_counter()-t0
    assert rows==allrows and len(rows)==742
    t0=time.perf_counter()
    heaprows=merged_convex_frontier(x,2)
    heap_seconds=time.perf_counter()-t0
    assert heaprows is not None and heaprows==rows
    assert len(profiles)==29 and sum(z['n'] for z in profiles)==954
    assert min(rows)==213 and rows[213]==1070 and rows[351]==603
    assert all(rows[k]==954-k for k in range(351,955))
    payload=''.join(f'{k},{j}\n' for k,j in sorted(rows.items()))
    digest=hashlib.sha256(payload.encode()).hexdigest()
    assert digest=='1de18dc9b43790c9bcb66e5ba8a88532dfd2de9979ee4d936cef8a1704b3dab9',digest
    assert sum(rows.values())==292961 and sum(k*v for k,v in rows.items())==130909193
    print(json.dumps({
      'status':'PASS_EXACT','pin':PIN,'R':2,
      'bruteforce_tests':tested,'nontrivial_separator_tests':nontrivial_splits,
      'N':len(x),'wall_count':len(x)-1,'event_count':x[-1],
      'component_count':len(profiles),'component_lengths':[v['n'] for v in profiles],
      'component_dR':[v['dR'] for v in profiles],
      'max_component_size':max(v['n'] for v in profiles),
      'sum_component_dR':sum(v['dR'] for v in profiles),
      'sum_component_edges':edge_split,'full_graph_edges':edge_direct,
      'all_budgets':len(rows),'cost_sum':sum(rows.values()),
      'weighted_cost_sum':sum(k*v for k,v in rows.items()),
      'curve_sha256':digest,
      'all_components_discrete_convex':True,
      'heap_merged_all_budgets':len(heaprows),
      'time_single_run_heap_sec':round(heap_seconds,6),
      'time_single_run_full_dp_sec':round(full_seconds,6),
      'time_single_run_components_sec':round(split_seconds,6)
      },ensure_ascii=False,indent=2))

if __name__=='__main__':run()
