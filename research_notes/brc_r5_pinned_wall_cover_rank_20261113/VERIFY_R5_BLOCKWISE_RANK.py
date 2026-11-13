#!/usr/bin/env python3
"""Blockwise exact suffix-rank reconstruction, frozen R5 rational-wall class.
Original pin 435e77af0d180eac32bd1f9c4c464bc4010b7551. Python stdlib only.
The original 28-coordinate legal-path census is prior scientific evidence.
"""
from fractions import Fraction
from collections import Counter
from bisect import bisect_left,bisect_right
from hashlib import sha256
from time import perf_counter
import tracemalloc,json
W=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
V=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
OLD='d500a95a516544511a50596555556a5a441665a66a9195956669611456565551aa5669aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa6a00'
EXPECTED_T=959842890872466279854034583824629760000
EXPECTED_RANK=291259906744233319113441752826891487978

def construct():
    pairs={3:set(),12:set(),15:set()}
    for mask in range(1,1<<15):
        n=-sum(W[i] for i in range(15) if mask>>i&1)
        weight=-sum(V[i] for i in range(15) if mask>>i&1)
        if n>=3 and weight%36==0 and weight//36 in pairs:
            pairs[weight//36].add(n)
    assert {q:len(v) for q,v in pairs.items()}=={3:538,12:298,15:229}
    histogram=Counter((1-Fraction(36*q,n))/23 for q,ns in pairs.items() for n in ns)
    assert len(histogram)==953 and Counter(histogram.values())==Counter({1:869,2:56,3:28})
    E=[0]
    for tau in sorted(histogram):E.append(E[-1]+histogram[tau])
    assert len(E)==954 and E[-1]==1065
    raw=bytes.fromhex(OLD)
    assert len(raw)==56 and sha256(raw).hexdigest()=='bf4f377e8a3b9823d589d0f5c5b0b5973f374a09aa986d5b729bc695c5de0326'
    stream=int.from_bytes(raw[2:],'little')
    centers=[stream&3];stream>>=2
    for _ in range(212):
        digit=stream&3;stream>>=2
        assert digit<=2
        centers.append(centers[-1]+3+digit)
    assert stream==0 and len(centers)==213 and centers[-1]==952
    starts=[p for p,x in enumerate(E) if x-E[0]<=2]
    ends={p for p,x in enumerate(E) if E[-1]-x<=2}
    upper=[bisect_right(E,E[p]+2)-1 for p in range(len(E))]
    lower=[bisect_left(E,E[p]-2) for p in range(len(E))]
    edges=[[q for q in range(p+1,min(len(E),p+6)) if lower[q]<=upper[p]+1] for p in range(len(E))]
    assert starts==[0,1,2] and ends=={951,952,953} and sum(map(len,edges))==4383
    return E,centers,starts,ends,edges

def nextrow(edges,prev):
    return [sum(prev[q] for q in adj) for adj in edges]

def complete(K,ends,edges):
    rows=[[int(p in ends) for p in range(len(edges))]]
    for t in range(2,K+1):rows.append(nextrow(edges,rows[-1]))
    return rows

class BlockRank:
    def __init__(self,K,ends,edges,B):
        assert B>=1
        self.K,self.B,self.edges=K,B,edges
        a=[int(p in ends) for p in range(len(edges))]
        self.anchors={1:a.copy()}
        for t in range(2,K+1):
            a=nextrow(edges,a)
            if (t-1)%B==0:self.anchors[t]=a.copy()
        self.top=a
        self.base=None;self.rows={}
        self.recomputed=0;self.maxheld=0
    def row(self,t):
        assert 1<=t<=self.K
        base=1+((t-1)//self.B)*self.B
        if self.base!=base:
            r=self.anchors[base];self.rows={base:r}
            for j in range(base+1,min(base+self.B,self.K+1)):
                r=nextrow(self.edges,r)
                self.rows[j]=r
                self.recomputed+=1
            self.base=base
            self.maxheld=max(self.maxheld,len(self.anchors)+len(self.rows))
        return self.rows[t]
    def total(self,starts):
        return sum(self.top[p] for p in starts)

def rank_of(centers,K,starts,edges,row):
    val=sum(row(K)[p] for p in starts if p<centers[0])
    for j,(p,q) in enumerate(zip(centers,centers[1:])):
        assert q in edges[p]
        val+=sum(row(K-1-j)[x] for x in edges[p] if x<q)
    return val

def unrank(value,K,starts,edges,row,total):
    if not 0<=value<total:raise ValueError('rank out of range')
    out=[];rem=value
    for p in starts:
        block=row(K)[p]
        if rem<block:
            out.append(p);break
        rem-=block
    for t in range(K-1,0,-1):
        for q in edges[out[-1]]:
            block=row(t)[q]
            if rem<block:
                out.append(q);break
            rem-=block
        else:raise AssertionError('missing legal suffix')
    assert rem==0
    return out

def benchmark(fn):
    tracemalloc.start();start=perf_counter()
    data=fn();elapsed=perf_counter()-start
    peak=tracemalloc.get_traced_memory()[1];tracemalloc.stop()
    return data,round(elapsed,6),peak

def main():
    E,centers,starts,ends,edges=construct();K=213
    full,tf,mf=benchmark(lambda:complete(K,ends,edges))
    total=sum(full[-1][p] for p in starts)
    ref=rank_of(centers,K,starts,edges,lambda t:full[t-1])
    assert total==EXPECTED_T and ref==EXPECTED_RANK
    assert unrank(ref,K,starts,edges,lambda t:full[t-1],total)==centers
    variants=[]
    for B in (1,8,15,16,32,64):
        (decoded,obj),dt,peak=benchmark(lambda:do_unrank(B,K,ref,starts,ends,edges))
        assert decoded==centers and obj.total(starts)==total
        (r2,ranker),rt,rm=benchmark(lambda:do_rank(B,K,centers,starts,ends,edges))
        assert r2==ref
        variants.append(dict(block=B,unrank_verified=True,rank_verified=True,
                             unrank_seconds=dt,unrank_peak_bytes=peak,
                             rank_seconds=rt,rank_peak_bytes=rm,
                             anchor_rows=len(obj.anchors),recomputed_rows=obj.recomputed,
                             max_rows_held=obj.maxheld))
    print(json.dumps(dict(status='PASS_EXACT_PINNED_R5_BLOCKWISE_SUFFIX_DP',
        true_wall_count=len(E)-1,events=E[-1],centers=len(centers),
        T=str(total),rank=str(ref),rank_hex=ref.to_bytes(17,'big').hex(),
        full_dp_seconds=tf,full_dp_tracemalloc_peak_bytes=mf,variants=variants,
        scope='Frozen R5 rational-wall covering class; exact integer DP; benchmark local CPython only'),indent=2,sort_keys=True))

def do_unrank(B,K,rank,starts,ends,edges):
    a=BlockRank(K,ends,edges,B)
    return unrank(rank,K,starts,edges,a.row,a.total(starts)),a

def do_rank(B,K,centers,starts,ends,edges):
    a=BlockRank(K,ends,edges,B)
    return rank_of(centers,K,starts,edges,a.row),a

if __name__=='__main__':main()
