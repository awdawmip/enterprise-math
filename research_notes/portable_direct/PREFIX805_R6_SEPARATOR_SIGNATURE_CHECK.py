#!/usr/bin/env python3
"""PREFIX-805 exact integer separator boundary-signature quotient.
Standard-library Python 3.9+, no floating arithmetic in mathematical output.
Counts and exponent tuples are arbitrary-precision signed integers.
"""
import json
import time
import random
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import product

ZERO=(0,0)
def w_default(e,c):
    i,j=divmod(e,c)
    return ((i+2*j)%5-2,(3*i-j+7)%5-2)
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def minus(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(x,a):return tuple(v*x for v in a)
def merge_hist(A,B,shift=ZERO):
    out=Counter()
    for a,ca in A.items():
        for b,cb in B.items():out[plus(plus(a,b),shift)]+=ca*cb
    return dict(out)

def solve_edges(b,c,edges,K,R,S,W):
    """An exact memoized suffix Laurent polynomial; cache only future residual demand."""
    ed=tuple(e for e in edges if K[e]>0)
    counters={'states':0,'branches':0,'leaves':0}
    @lru_cache(None)
    def rec(k,r,s):
        counters['states']+=1
        if any(v<0 for v in r+s):return ()
        if k==len(ed):
            counters['leaves']+=1
            return ((ZERO,1),) if not any(r+s) else ()
        e=ed[k];i,j=divmod(e,c)
        ans=Counter()
        for t in range(min(K[e],r[i],s[j])+1):
            counters['branches']+=1
            rr=list(r);ss=list(s);rr[i]-=t;ss[j]-=t
            for z,m in rec(k+1,tuple(rr),tuple(ss)):
                ans[plus(scale(t,W[e]),z)]+=m
        return tuple(sorted((z,v) for z,v in ans.items() if v))
    h=dict(rec(0,tuple(R),tuple(S)))
    return h,counters

def direct_bruteforce(b,c,K,R,S,W):
    edges=[e for e,k in enumerate(K) if k>0]
    hist=Counter();calls=0
    rr=[0]*b;ss=[0]*c
    def dfs(k,obs):
        nonlocal calls
        calls+=1
        if k==len(edges):
            if tuple(rr)==tuple(R) and tuple(ss)==tuple(S):hist[obs]+=1
            return
        e=edges[k];i,j=divmod(e,c)
        for t in range(K[e]+1):
            rr[i]+=t;ss[j]+=t
            if rr[i]<=R[i] and ss[j]<=S[j]:dfs(k+1,plus(obs,scale(t,W[e])))
            rr[i]-=t;ss[j]-=t
    dfs(0,ZERO)
    return dict(hist),calls

def split_edges(b,c,K,rowsA,colsA):
    UA=set(rowsA);VA=set(colsA)
    A=[];B=[];X=[]
    for e,k in enumerate(K):
        if k==0:continue
        i,j=divmod(e,c)
        if i in UA and j in VA:A.append(e)
        elif i not in UA and j not in VA:B.append(e)
        else:X.append(e)
    return A,B,X

def separator_solve(b,c,K,R,S,W,rowsA,colsA):
    """Raw crossing allocations and exact observer-sufficient signature quotient.
    Last positive-capacity crossing edge is determined by cut conservation.
    """
    A,B,X=split_edges(b,c,K,rowsA,colsA)
    UA=set(rowsA);VA=set(colsA)
    sigma=lambda e: 1 if divmod(e,c)[0] in UA else -1
    D=sum(R[i] for i in UA)-sum(S[j] for j in VA)
    groups=defaultdict(int)
    transfer_raw=0;range_candidates=0;invalid_cut=0
    def accept(ts):
        nonlocal transfer_raw
        rs=list(R);cs=list(S);obs=ZERO
        for e,t in zip(X,ts):
            i,j=divmod(e,c)
            rs[i]-=t;cs[j]-=t
            obs=plus(obs,scale(t,W[e]))
        if min(rs+cs,default=0)<0:return
        transfer_raw+=1
        # Residual demands on all vertices plus crossing observable are sufficient.
        groups[(tuple(rs),tuple(cs),obs)]+=1
    if X:
        final=X[-1];sg=sigma(final)
        for prefix in product(*(range(K[e]+1) for e in X[:-1])):
            range_candidates+=1
            t_last=sg*(D-sum(sigma(e)*t for e,t in zip(X[:-1],prefix)))
            if 0<=t_last<=K[final]:accept(prefix+(t_last,))
            else:invalid_cut+=1
    elif D==0:accept(())
    component_cacheA={};component_cacheB={}
    stats={'raw_cut_allocations_after_margin_bounds':transfer_raw,
           'crossing_prefix_candidates':range_candidates,
           'invalid_cut_or_capacity_prefixes':invalid_cut,
           'quotient_signatures':len(groups),'raw_named_crossing_edges':len(X),
           'component_A_calls':0,'component_B_calls':0,'component_A_dp_states':0,'component_B_dp_states':0}
    total=Counter()
    for (rs,cs,obs),multiplicity in groups.items():
        if (rs,cs) not in component_cacheA:
            ar=tuple(rs[i] if i in UA else 0 for i in range(b))
            ac=tuple(cs[j] if j in VA else 0 for j in range(c))
            component_cacheA[(rs,cs)]=solve_edges(b,c,A,K,ar,ac,W)
            stats['component_A_calls']+=1
            stats['component_A_dp_states']+=component_cacheA[(rs,cs)][1]['states']
        if (rs,cs) not in component_cacheB:
            br=tuple(rs[i] if i not in UA else 0 for i in range(b))
            bc=tuple(cs[j] if j not in VA else 0 for j in range(c))
            component_cacheB[(rs,cs)]=solve_edges(b,c,B,K,br,bc,W)
            stats['component_B_calls']+=1
            stats['component_B_dp_states']+=component_cacheB[(rs,cs)][1]['states']
        ha,_=component_cacheA[(rs,cs)];hb,_=component_cacheB[(rs,cs)]
        for z,n in merge_hist(ha,hb,obs).items():total[z]+=multiplicity*n
    return dict(total),stats

def to_json_hist(H):return [{'exponent':list(k),'count':v} for k,v in sorted(H.items())]

def fixed_case(name,b,c,edges,R,S,rowsA,colsA,weights=None):
    K=[0]*(b*c)
    for i,j,v in edges:K[i*c+j]=v
    W=[w_default(e,c) for e in range(b*c)] if weights is None else [weights.get((e//c,e%c),ZERO) for e in range(b*c)]
    t0=time.perf_counter();bhi,bcounters=solve_edges(b,c,list(range(b*c)),K,R,S,W);base_time=time.perf_counter()-t0
    t1=time.perf_counter();shi,scounters=separator_solve(b,c,K,R,S,W,rowsA,colsA);sep_time=time.perf_counter()-t1
    t2=time.perf_counter();dhi,dcalls=direct_bruteforce(b,c,K,R,S,W);direct_time=time.perf_counter()-t2
    assert dhi==shi==bhi,(name,dhi,shi,bhi)
    return {'name':name,'b':b,'c':c,'capacities':K,'row_demand':list(R),'col_demand':list(S),
            'cut_rowsA':list(rowsA),'cut_colsA':list(colsA),
            'named_tables':sum(bhi.values()),'observer_support':len(bhi),
            'histogram':to_json_hist(bhi),'baseline_memo':bcounters,
            'separator':scounters,'direct_dfs_calls':dcalls,
            'timing_seconds_single_run':{'baseline_memo':round(base_time,6),'separator':round(sep_time,6),'direct':round(direct_time,6)}}

def check_signature_witness():
    b=c=4
    edges=[]
    for i in (0,1):
        for j in (0,1,2,3):edges.append((i,j,1))
    for i in (2,3):
        for j in (2,3):edges.append((i,j,1))
    R=(2,2,1,1);S=(1,1,2,2)
    zero=fixed_case('signature_merges_hidden_named_crossings',b,c,edges,R,S,(0,1),(0,1),{})
    distinguish=fixed_case('source_specific_future_observer',b,c,edges,R,S,(0,1),(0,1),{(0,2):(1,0)})
    assert zero['named_tables']==distinguish['named_tables']
    assert zero['observer_support']==1 and distinguish['observer_support']>1
    assert zero['separator']['quotient_signatures']<distinguish['separator']['quotient_signatures']
    return zero,distinguish

def run():
    start=time.perf_counter()
    rng=random.Random(80520261115)
    tests=0;matrices=0;counts=0;merged=0
    # Complete bounded Cartesian capacity configurations and ALL induced fibers.
    for b,c,capmax in ((2,2,2),(2,3,1)):
        for K in product(range(capmax+1),repeat=b*c):
            matrices+=1;W=[w_default(e,c) for e in range(b*c)]
            fibers=set()
            for t in product(*(range(k+1) for k in K)):
                rr=[0]*b;ss=[0]*c
                for e,x in enumerate(t):i,j=divmod(e,c);rr[i]+=x;ss[j]+=x
                fibers.add((tuple(rr),tuple(ss)))
            for R,S in fibers:
                cutrows=(0,);cutcols=(0,) if c==2 else (0,1)
                base,_=solve_edges(b,c,range(b*c),K,R,S,W)
                sep,st=separator_solve(b,c,K,R,S,W,cutrows,cutcols)
                assert base==sep,('bounded exhaustive',b,c,K,R,S,base,sep)
                tests+=1;counts+=sum(base.values());merged+=st['raw_cut_allocations_after_margin_bounds']-st['quotient_signatures']
    sample=[]
    for case in range(100):
        b,c=3,3;K=[rng.randrange(3) for _ in range(9)]
        planted=[rng.randrange(k+1) for k in K]
        R=[sum(planted[i*c+j] for j in range(c)) for i in range(b)]
        S=[sum(planted[i*c+j] for i in range(b)) for j in range(c)]
        W=[w_default(e,c) for e in range(b*c)]
        base,_=solve_edges(b,c,range(b*c),K,R,S,W)
        sep,st=separator_solve(b,c,K,R,S,W,(0,1),(0,))
        direct,_=direct_bruteforce(b,c,K,R,S,W)
        assert base==sep==direct,('sample',case,K,R,S)
        sample.append({'support':len(base),'tables':sum(base.values()),'cut_signatures':st['quotient_signatures']})
    zero,dist=check_signature_witness()
    bench=[]
    sparse=[(i,j,2) for i in (0,1) for j in (0,1)] + [(i,j,2) for i in (2,3) for j in (2,3)] +[(0,2,2),(1,2,2)]
    bench.append(fixed_case('sparse_two_block_two_crossings',4,4,sparse,(3,3,2,2),(2,2,4,2),(0,1),(0,1)))
    dense=[(i,j,1) for i in range(4) for j in range(4)]
    bench.append(fixed_case('dense_4x4_unit_capacities',4,4,dense,(2,2,2,2),(2,2,2,2),(0,1),(0,1)))
    return {'schema':'PREFIX805_BOUNDARY_SIGNATURE_QUOTIENT_V1',
            'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
            'arithmetic':'exact Python integers, two-coordinate signed integer Laurent exponents',
            'complete_families':['2x2 capacities 0..2 all induced margin fibers', '2x3 capacities 0..1 all induced margin fibers'],
            'exhaustive':{'capacity_patterns':matrices,'margin_fibers':tests,'counted_named_tables':counts,'raw_allocation_minus_quotient_signature_total':merged},
            'sampled':{'seed':80520261115,'case_count':100,'model':'3x3 capacities 0..2, one planted table per case','cases_summary':{'total_tables':sum(s['tables'] for s in sample),'total_support':sum(s['support'] for s in sample)}},
            'observer_sensitive_witness':{'zero_observer':zero,'named_edge_observer':dist},
            'timed_examples':bench,
            'wall_seconds_total':round(time.perf_counter()-start,6),
            'result':'ALL_CHECKS_PASS PREFIX805 EXACT_BOUNDARY_SIGNATURE_QUOTIENT'}
if __name__=='__main__': print(json.dumps(run(),indent=2,sort_keys=True,ensure_ascii=False))
