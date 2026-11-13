#!/usr/bin/env python3
"""Exact interval-array min-plus/count DP for the frozen R5 12-byte optimal-center rank."""
from bisect import bisect_left, bisect_right
from hashlib import sha256
from time import perf_counter
import json

from VERIFY_R5_INTERVAL_SUPPORT import frozen_events,support_intervals

R,K=2,213
OLD56='d500a95a516544511a50596555556a5a441665a66a9195956669611456565551aa5669aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa6a00'
ORIGINAL_RANK=int.from_bytes(bytes.fromhex('0158f5198cd12c63a2ba0a4b'),'big')
EXPECTED_J=1070
EXPECTED_T=1338767625695954932334592000

def original_centers():
    raw=bytes.fromhex(OLD56)
    assert sha256(raw).hexdigest()=='bf4f377e8a3b9823d589d0f5c5b0b5973f374a09aa986d5b729bc695c5de0326'
    bits=int.from_bytes(raw[2:],'little'); out=[bits&3];bits>>=2
    for _ in range(212):
        out.append(out[-1]+3+(bits&3));bits>>=2
    assert bits==0 and len(out)==K and out[-1]==952
    return out

def graph(x,r):
    n=len(x); upper=[bisect_right(x,x[p]+r)-1 for p in range(n)]
    lower=[bisect_left(x,x[q]-r) for q in range(n)]
    g=[[] for _ in x]
    for p in range(n):
        for q in range(p+1,min(n,p+2*r+2)):
            if lower[q]<=upper[p]+1:
                cost=sum(min(x[b]-x[p],x[q]-x[b]) for b in range(p+1,q+1))
                g[p].append((q,cost))
    return g

class IntervalDP:
    def __init__(self,x,r,k,g):
        self.x,self.r,self.k,self.g=x,r,k,g
        spans,_=support_intervals(x,r,k)
        rows=[]
        a,b=spans[0];n=len(x)
        ps=[0]
        for v in x:ps.append(ps[-1]+v)
        cost=[(ps[-1]-ps[p+1])-(n-1-p)*x[p] for p in range(a,b+1)]
        count=[1]*(b-a+1)
        rows.append((a,cost,count))
        for t in range(2,k+1):
            na,nb=spans[t-1];oa,oc,on=rows[-1]
            nc=[];nn=[]
            for p in range(na,nb+1):
                best=10**30;ways=0
                for q,w in g[p]:
                    if not oa<=q<oa+len(oc):continue
                    y=w+oc[q-oa]
                    if y<best:best,ways=y,on[q-oa]
                    elif y==best:ways+=on[q-oa]
                assert ways>0
                nc.append(best);nn.append(ways)
            rows.append((na,nc,nn))
        self.rows=rows
        self.support_cells=sum(len(row[1]) for row in rows)
    def value(self,t,p):
        a,c,n=self.rows[t-1]
        return (c[p-a],n[p-a]) if a<=p<a+len(c) else (10**30,0)
    def summary(self):
        x,r,k=self.x,self.r,self.k
        start=[p for p in range(len(x)) if x[p]-x[0]<=r]
        head=lambda p:sum(x[p]-x[b] for b in range(p))
        best=min((head(p)+self.value(k,p)[0] for p in start),default=10**30)
        total=sum(self.value(k,p)[1] for p in start if head(p)+self.value(k,p)[0]==best)
        return best,total
    def unrank(self,rank):
        best,total=self.summary();assert 0<=rank<total
        x,r,k=self.x,self.r,self.k
        start=[p for p in range(len(x)) if x[p]-x[0]<=r]
        head=lambda p:sum(x[p]-x[b] for b in range(p))
        out=[]
        for p in start:
            cost,ways=self.value(k,p)
            if head(p)+cost!=best:continue
            if rank<ways:out=[p];break
            rank-=ways
        assert out
        for t in range(k,1,-1):
            p=out[-1];need=self.value(t,p)[0]
            for q,w in self.g[p]:
                cost,ways=self.value(t-1,q)
                if w+cost!=need:continue
                if rank<ways:out.append(q);break
                rank-=ways
            else:raise AssertionError('unreachable optimal path')
        assert rank==0
        return out
    def rank_of(self,centers):
        best,total=self.summary()
        k=self.k
        start=[p for p in range(len(self.x)) if self.x[p]-self.x[0]<=self.r]
        head=lambda p:sum(self.x[p]-self.x[b] for b in range(p))
        p=centers[0]
        assert head(p)+self.value(k,p)[0]==best
        ans=sum(self.value(k,b)[1] for b in start if b<p and head(b)+self.value(k,b)[0]==best)
        for t,(p,q) in zip(range(k,1,-1),zip(centers,centers[1:])):
            parent=self.value(t,p)[0]
            assert any(j==q and w+self.value(t-1,q)[0]==parent for j,w in self.g[p])
            ans+=sum(self.value(t-1,j)[1] for j,w in self.g[p] if j<q and w+self.value(t-1,j)[0]==parent)
        return ans

def directory(x,centers):
    coords=[x[s] for s in centers]
    out=[]
    for target in x:
        z=bisect_left(coords,target)
        if z==0:z=0
        elif z==len(coords):z-=1
        elif coords[z]-target>=target-coords[z-1]:z-=1
        out.append(z)
    return bytes(out)

def result():
    x=frozen_events(); centers=original_centers();g=graph(x,R)
    t=perf_counter();dp=IntervalDP(x,R,K,g); elapsed=perf_counter()-t
    assert dp.summary()==(EXPECTED_J,EXPECTED_T)
    got=dp.unrank(ORIGINAL_RANK)
    assert got==centers
    assert dp.rank_of(centers)==ORIGINAL_RANK
    from struct import pack
    packed=b''.join(pack('<H',c) for c in got)
    d=directory(x,centers)
    hashes={'uint16_center_sha256':sha256(packed).hexdigest(),'direct_directory_sha256':sha256(d).hexdigest()}
    assert hashes=={'uint16_center_sha256':'b6d9f351d2ed5c41e8b6061de6517519037fdb3918dd7656f420e584e8bda4a1',
                    'direct_directory_sha256':'a947d07d7d494e00e14013eb929b3ffdc9224938ec15289209e68316c50a14b1'}
    return dict(status='PASS_R5_INTERVAL_ARRAY_DP',original_pin='435e77af0d180eac32bd1f9c4c464bc4010b7551',
       cost=EXPECTED_J,optimal_paths=str(EXPECTED_T),rank=str(ORIGINAL_RANK),
       support_cells=dp.support_cells,original_centers=len(got),directory_bytes=len(d),
       build_seconds_single=round(elapsed,6),hashes=hashes)

if __name__=='__main__':print(json.dumps(result(),sort_keys=True,indent=2))
