"""Exact finite history sets with an upper bound on paid probes before first-stage delivery.
All query costs one here; raw BRC command prices are in deadline_kernel.py.
"""
import argparse,json
from collections import Counter
from functools import cache
from itertools import product
from pathlib import Path

def bitset(ids):return sum(1<<j for j in ids)
def masks(values):
    # one mask per row label; each world belongs to exactly one.
    m={}
    for h,v in enumerate(values):m[v]=m.get(v,0)|(1<<h)
    return tuple(m.values())
def unique(U,cells):return any(not U&~c for c in cells)
def solver(cols,first,full,prices=None):
    """Records are feasible input worlds. Full is the required ordered transcript."""
    f0=masks(first);f1=masks(full)
    N=len(full);W=(1<<N)-1
    prices=tuple(prices or [0]*N)
    @cache
    def f(U,L):
        if unique(U,f1):return max(prices[h] for h in range(N) if U&(1<<h))
        fixed=unique(U,f0)
        if fixed and L!=-1:return f(U,-1)
        if not fixed and L==0:return 10**8
        childL=L-1 if L>0 else -1
        opts=[max(f(V,childL),f(U^V,childL)) for c in cols if (V:=U&c) and V!=U]
        return 1+min(opts)
    return f,W

def general_census():
    totals=Counter();hist=Counter();delta=Counter();ex=None
    for n in range(1,4):
        H=1<<n;cases=0
        for si in range(n):
            others=[j for j in range(n) if j!=si]
            queries=[bitset(h for h in range(H) if h&(1<<j)) for j in range(n)]
            for p,q in product(range(1<<(n-1)),repeat=2):
                maps=tuple(tuple(j for i,j in enumerate(others) if D>>i&1) for D in (p,q))
                first=tuple((h>>si)&1 for h in range(H))
                full=tuple((s,tuple((h>>j)&1 for j in maps[s])) for h,s in enumerate(first))
                f,_=solver(queries,first,full)
                for W in range(1,1<<H):
                    c,e=f(W,-1),f(W,1)
                    assert 0<=e-c<=1
                    cases+=1;delta[(n,e-c)]+=1
                    if e>c:
                        key=(n,W.bit_count(),si,p,q,W)
                        if ex is None or key<ex[0]:ex=(key,dict(coordinates=n,histories=[h for h in range(H) if W>>h&1],selector=si,payloads=maps,free=c,deadline_one=e))
                        hist[n,W.bit_count()]+=1
        totals[n]=cases
    return dict(per_coordinates=dict(totals),strict_by_coordinates_and_histories={str(k):v for k,v in hist.items()},
            totals_by_coordinates_and_penalty={str(k):v for k,v in delta.items()},total=sum(totals.values()),minimal=ex[1])
def block_models(ds):
    D=sum(ds);H=1<<D;k=len(ds);offs=[sum(ds[:i]) for i in range(k)]
    cols=[bitset(h for h in range(H) if h>>j&1) for j in range(D)]
    rows=[]
    for h in range(H):
        rows.append(tuple(int((h>>o)&((1<<d)-1)==(1<<d)-1) for d,o in zip(ds,offs)))
    cols.extend(bitset(h for h in range(H) if rows[h][i]) for i in range(k))
    # full transcript contains selector vector, followed only by bits of zero blocks;
    # from the selector vector omitted bits of true blocks equal 1.
    labels=tuple((row,tuple((h>>(o+j))&1 for i,(d,o) in enumerate(zip(ds,offs)) if not row[i] for j in range(d))) for h,row in enumerate(rows))
    assert len(set(labels))==H
    f,W=solver(tuple(cols),rows,labels)
    ret=[]
    for L in range(k-1,D+1):
        v=f(W,L)
        if L<k:assert v>=10**8;ret.append(None);continue
        slack=L-k;b=0
        for cost in sorted(d-1 for d in ds):
            if cost>slack:break
            slack-=cost;b+=1
        assert v==D+k-b,(ds,L,b,v)
        ret.append(v)
    return dict(block_dimensions=ds,histories=H,latencies=list(range(k-1,D+1)),optimal_worst_probes=ret,oracle_states=f.cache_info().currsize)
def run():
    profiles=[(2,),(3,),(4,),(5,),(6,),(2,2),(2,3),(3,3),(2,4),(2,2,2),(2,2,3)]
    rows=[block_models(ds) for ds in profiles]
    return dict(status="PASS",census=general_census(),heterogeneous_blocks=rows,
                parameter_tests=sum(len(v['latencies']) for v in rows))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=Path(__file__).with_name('deadline_results.json'));a=p.parse_args()
    res=run();a.out.write_text(json.dumps(res,sort_keys=True,indent=2)+'\n');print(res['census'],res['parameter_tests'])
