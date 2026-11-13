#!/usr/bin/env python3
"""Exact blockwise min-plus/count suffix DP for frozen R5 12-byte mean-optimal checkpoint rank.
Standard library only; original 28-coordinate witness legality is cited from the unchanged frozen R5 pin.
"""
from bisect import bisect_left, bisect_right
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
from time import perf_counter
import gc, json, statistics, tracemalloc

WEIGHTS=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
OLD56='d500a95a516544511a50596555556a5a441665a66a9195956669611456565551aa5669aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa6a00'
PIN='435e77af0d180eac32bd1f9c4c464bc4010b7551'
R=2; K=213
EXPECTED_J=1070; EXPECTED_T=1338767625695954932334592000
EXPECTED_RANK=417027933051277583800994379
INF=10**18

def fixture():
    pairs={3:set(),12:set(),15:set()}
    for mask in range(1,1<<15):
        n=-sum(WEIGHTS[i] for i in range(15) if mask>>i&1)
        k=-sum(K0[i] for i in range(15) if mask>>i&1)
        if n>=3 and k%36==0 and k//36 in pairs:
            pairs[k//36].add(n)
    assert {q:len(s) for q,s in pairs.items()}=={3:538,12:298,15:229}
    histogram=Counter((1-Fraction(36*q,n))/23 for q,ns in pairs.items() for n in ns)
    assert len(histogram)==953 and Counter(histogram.values())=={1:869,2:56,3:28}
    x=[0]
    for tau in sorted(histogram): x.append(x[-1]+histogram[tau])
    assert len(x)==954 and x[-1]==1065
    raw=bytes.fromhex(OLD56)
    assert len(raw)==56 and sha256(raw).hexdigest()=='bf4f377e8a3b9823d589d0f5c5b0b5973f374a09aa986d5b729bc695c5de0326'
    bits=int.from_bytes(raw[2:],'little'); center=[bits&3]; bits>>=2
    for _ in range(212):
        digit=bits&3; bits>>=2
        assert digit<=2
        center.append(center[-1]+3+digit)
    assert bits==0 and len(center)==K and center[0]==1 and center[-1]==952
    return x,center

def graph(x,r):
    n=len(x)
    start=[p for p in range(n) if x[p]-x[0]<=r]
    end={p for p in range(n) if x[-1]-x[p]<=r}
    upper=[bisect_right(x,x[p]+r)-1 for p in range(n)]
    lower=[bisect_left(x,x[p]-r) for p in range(n)]
    adj=[[] for _ in x]
    for p in range(n):
        for q in range(p+1,min(n,p+2*r+2)):
            if lower[q]<=upper[p]+1:
                price=sum(min(x[b]-x[p],x[q]-x[b]) for b in range(p+1,q+1))
                adj[p].append((q,price))
    head={p:sum(x[p]-x[b] for b in range(p)) for p in start}
    tail={p:sum(x[b]-x[p] for b in range(p+1,n)) for p in end}
    return start,end,adj,head,tail

def first_row(g):
    n=len(g[2]); end=g[1]; tail=g[4]
    return ([tail[p] if p in end else INF for p in range(n)], [int(p in end) for p in range(n)])

def step(g,row):
    oldc,oldn=row; n=len(oldc); adj=g[2]
    c=[INF]*n; d=[0]*n
    for p,branches in enumerate(adj):
        best=INF; ways=0
        for q,w in branches:
            if oldn[q]==0: continue
            z=w+oldc[q]
            if z<best: best=z; ways=oldn[q]
            elif z==best: ways+=oldn[q]
        c[p]=best;d[p]=ways
    return (c,d)

def top_result(g,top):
    start,_,_,head,_=g
    cost,counts=top
    best=min((head[p]+cost[p] for p in start),default=INF)
    ways=sum(counts[p] for p in start if head[p]+cost[p]==best)
    return best,ways

class Full:
    def __init__(self,g,k):
        self.rows=[None,first_row(g)]
        for _ in range(2,k+1):self.rows.append(step(g,self.rows[-1]))
        self.max_rows_held=k
    def row(self,t):return self.rows[t]

class Blocks:
    def __init__(self,g,k,B):
        assert B>=1
        self.g=g;self.k=k;self.B=B;self.anchors={1:first_row(g)}
        latest=self.anchors[1]
        for t in range(2,k+1):
            latest=step(g,latest)
            if (t-1)%B==0:self.anchors[t]=latest
        self.top=latest
        self.current_base=None;self.recent={};self.recomputed=0
        self.max_rows_held=len(self.anchors)+1
    def row(self,t):
        assert 1<=t<=self.k
        base=1+((t-1)//self.B)*self.B
        if self.current_base!=base:
            latest=self.anchors[base]
            self.recent={base:latest}
            for j in range(base+1,min(self.k+1,base+self.B)):
                latest=step(self.g,latest)
                self.recent[j]=latest;self.recomputed+=1
            self.current_base=base
            self.max_rows_held=max(self.max_rows_held,len(self.anchors)+len(self.recent))
        return self.recent[t]

def unrank(g,k,rank,decoder):
    best,total=top_result(g,decoder.row(k))
    if not 0<=rank<total:raise ValueError('rank outside optimal class')
    start,ends,adj,head,tail=g
    out=[]
    c,n=decoder.row(k)
    for p in start:
        if head[p]+c[p]!=best:continue
        if rank<n[p]:out.append(p);break
        rank-=n[p]
    prevc=decoder.row(k)[0]
    for t in range(k-1,0,-1):
        p=out[-1];c,n=decoder.row(t)
        for q,w in adj[p]:
            if w+c[q]!=prevc[p]:continue
            if rank<n[q]:out.append(q);break
            rank-=n[q]
        else:raise AssertionError('unreachable optimal suffix')
        prevc=c
    assert rank==0 and out[-1] in ends
    return out

def rank_of(g,k,centers,decoder):
    start,ends,adj,head,tail=g
    top=decoder.row(k);best,total=top_result(g,top)
    if head.get(centers[0],INF)+top[0][centers[0]]!=best:
        raise ValueError('not an optimal start')
    rank=sum(top[1][p] for p in start if p<centers[0] and head[p]+top[0][p]==best)
    current=top
    for j,(p,q) in enumerate(zip(centers,centers[1:])):
        suffix=decoder.row(k-j-1)
        if not any(v==q and w+suffix[0][q]==current[0][p] for v,w in adj[p]):
            raise ValueError('not an optimal transition')
        rank+=sum(suffix[1][v] for v,w in adj[p] if v<q and w+suffix[0][v]==current[0][p])
        current=suffix
    if centers[-1] not in ends:raise ValueError('invalid end')
    return rank

def evaluate(g,k,centers,rank,variant,B=0):
    gc.collect();tracemalloc.start();t0=perf_counter()
    x=Full(g,k) if variant=='full' else Blocks(g,k,B)
    result=top_result(g,x.row(k))
    decoded=unrank(g,k,rank,x)
    elapsed=perf_counter()-t0; peak=tracemalloc.get_traced_memory()[1];tracemalloc.stop()
    assert decoded==centers
    assert result==(EXPECTED_J,EXPECTED_T)
    # A separate rank pass is performed without memory sampling so that the
    # unranking peak concerns exactly one cold decode.
    y=Full(g,k) if variant=='full' else Blocks(g,k,B)
    assert rank_of(g,k,centers,y)==rank
    return {'variant':variant,'block':B or None,
            'cold_unrank_seconds':round(elapsed,6),'peak_tracemalloc_bytes':peak,
            'anchors':len(x.anchors) if variant!='full' else k,
            'max_rows_held':x.max_rows_held,
            'recomputed_rows':x.recomputed if variant!='full' else 0,
            'decoded_centers':len(decoded)}

def small_exhaustive():
    tests=matches=0
    for number in range(1,5):
        for increments in product((1,2,3),repeat=number):
            x=[0]
            for d in increments:x.append(x[-1]+d)
            for r in range(4):
                g=graph(x,r)
                for k in range(1,len(x)+1):
                    a=Full(g,k)
                    reference=top_result(g,a.row(k))
                    for B in (1,2,3):
                        z=Blocks(g,k,B)
                        assert top_result(g,z.row(k))==reference
                    legal=[]
                    for subset in combinations(range(len(x)),k):
                        error=[min(abs(x[b]-x[s]) for s in subset) for b in range(len(x))]
                        if max(error)<=r:legal.append((subset,sum(error)))
                    tests+=1
                    if not legal:
                        assert reference[1]==0
                        continue
                    opt=min(v for _,v in legal)
                    good=[s for s,c in legal if c==opt]
                    assert reference==(opt,len(good))
                    for i,s in enumerate(good):
                        for B in (1,2,3):
                            d=Blocks(g,k,B)
                            assert unrank(g,k,i,d)==list(s)
                            d=Blocks(g,k,B)
                            assert rank_of(g,k,s,d)==i
                            matches+=1
    return {'small_instances':tests,'blockwise_optimal_rank_unrank_crosschecks':matches}

def main():
    t0=perf_counter();x,centers=fixture();g=graph(x,R)
    assert sum(len(a) for a in g[2])==4383
    assert (len(x),x[-1])==(954,1065)
    make_seconds=perf_counter()-t0
    results=[]
    for B in (0,1,4,8,12,15,16,24,32,64):
        results.append(evaluate(g,K,centers,EXPECTED_RANK,'full' if B==0 else 'blockwise',B))
    tests=small_exhaustive()
    output={'status':'PASS_EXACT_PINNED_R5_BLOCKWISE_MINPLUS_COUNT',
            'frozen_pin':PIN,'parent_pr':2268,
            'boundaries':len(x),'events':x[-1],'radius':R,
            'centers':K,'graph_edges':sum(map(len,g[2])),
            'optimum_correction':EXPECTED_J,'optimal_class_size':str(EXPECTED_T),
            'historical_optimal_rank':str(EXPECTED_RANK),
            'historical_rank_12byte_hex':EXPECTED_RANK.to_bytes(12,'big').hex(),
            'fixture_seconds':round(make_seconds,6),
            'variant_results':results,'small_exhaustive':tests,
            'measurement_scope':'CPython single-machine tracemalloc of table construction plus one unrank; fixture excluded; no full query RSS'}
    print(json.dumps(output,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':main()
