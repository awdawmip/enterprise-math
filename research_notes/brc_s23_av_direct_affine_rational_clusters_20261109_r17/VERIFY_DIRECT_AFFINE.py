#!/usr/bin/env python3
"""Direct Farey-threshold -> affine-run emitter for an irrational circle observer.

Finite certificate: frozen S23/AV m=128, L<=2,000,000. No constant-risk
block table is materialized by this implementation. Phase memberships
are pre-indexed in O(N) memory; future work may replace them with exact
floor-sum rank/select to remove this N-dependence. Standard library only.
"""
import bisect
import csv
import hashlib
import io
import time
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).parent
P,Q=262204504569236716045286,10**24
LO,HI=F(P,Q),F(P+1,Q)
M,N=128,2000128


def theta_certificate():
    def log(z):
        acc,term=F(0),z
        for k in range(160):
            acc+=2*term/F(2*k+1)
            term*=z*z
        return acc, acc+2*term/(321*(1-z*z))
    a,b=log(F(3,4)); c,d=log(F(3,17))
    lo,hi=a/d,b/c
    def theta(r):return 79*(2074774-380295*r)/(79*r-431)-46
    assert 79*lo>431 and LO<theta(hi)<theta(lo)<HI


def cmp_pair(a,b):
    vals=[a+b*z for z in (LO,HI)]
    assert (vals[0]>0 and vals[1]>0) or (vals[0]<0 and vals[1]<0) or vals==[0,0]
    return (vals[0]>0)-(vals[0]<0)


def advance(a,b,c,d):
    diff=[(b+d)*t-(a+c) for t in (LO,HI)]
    assert diff[0]*diff[1]>0
    return (a+c,b+d,c,d) if diff[0]>0 else (a,b,a+c,b+d)


def farey_at_n(n):
    a,b,c,d=0,1,1,1
    while b+d<=n-1:
        a,b,c,d=advance(a,b,c,d)
    return a,b,c,d


def history_members(m,n):
    positions=[];orders=[]
    for t in (LO,HI):
        s=sorted(((i*t.numerator)%t.denominator,i) for i in range(m))
        positions.append([v for v,_ in s]);orders.append([i for _,i in s])
    assert orders[0]==orders[1]
    out=[[] for _ in range(m)]
    for i in range(n+1):
        loc=[]
        for j,t in enumerate((LO,HI)):
            v=(i*t.numerator)%t.denominator
            loc.append(bisect.bisect_right(positions[j],v)-1)
        assert loc[0]==loc[1],('ambiguous historical arc',i)
        out[loc[0]].append(i)
    return out


def risk_at(n,epoch,arcs):
    a,b,c,d=epoch
    u,v,w=(-a,b),(c,-d),(c-a,b-d)
    A,B=1,0
    for row in arcs:
        cut=bisect.bisect_left(row,n-b)
        right=bisect.bisect_left(row,d)
        candidates=[]
        if cut>0:candidates.append(u)
        if bisect.bisect_left(row,n)>right:candidates.append(v)
        if right>cut:candidates.append(w)
        assert candidates,(n,epoch)
        best=candidates[0]
        for x in candidates[1:]:
            if cmp_pair(x[0]-best[0],x[1]-best[1])>0:best=x
        A-=best[0]; B-=best[1]
    return A,B


class AffineEmitter:
    def __init__(self,writer,initial_n,initial_value):
        self.writer=writer
        self.last_n=initial_n
        self.last_v=initial_value
        self.pending=None
        self.count=0
        self.positive=0
        self.signatures=set()
        self.closed=[] # Only the first few output rows for display; no risk-block table.

    def increments(self,left,right,da,db):
        if left>right:return
        assert left==self.last_n+1,(left,self.last_n)
        assert cmp_pair(da,db)>=0
        old=self.last_v
        self.last_v=(old[0]+(right-left+1)*da, old[1]+(right-left+1)*db)
        self.last_n=right
        if self.pending is not None and self.pending[4:]==(da,db):
            self.pending=(self.pending[0],right,*self.pending[2:])
        else:
            self.flush()
            self.pending=(left-1,right,*old,da,db)

    def take_constant_segment(self,start,end,value):
        assert start<=end
        assert start==self.last_n+1 or (start==M and self.last_n==M)
        if start==M:
            assert value==(0,0)
        else:
            da=value[0]-self.last_v[0]
            db=value[1]-self.last_v[1]
            self.increments(start,start,da,db)
        if start<end:
            self.increments(max(start+1,M+1),end,0,0)
        assert self.last_v==value

    def flush(self):
        if self.pending is None:return
        record=self.pending
        self.writer.writerow(record)
        self.count+=1
        self.signatures.add(record[4:])
        if record[4:]!=(0,0):self.positive+=1
        if len(self.closed)<6:self.closed.append(record)
        self.pending=None

    def finish(self):
        self.flush()


def run():
    start=time.perf_counter()
    theta_certificate()
    arcs=history_members(M,N)
    epoch=farey_at_n(M)
    n=M; epochs=0;thresholds=0;segments=0
    outfile=ROOT/'DIRECT_AFFINE_RUNS_2M.tsv'
    with outfile.open('w',encoding='utf-8',newline='') as fp:
        writer=csv.writer(fp,delimiter='\t',lineterminator='\n')
        writer.writerow(['n0','n1','A0','B0','dA','dB'])
        emitter=AffineEmitter(writer,M,(0,0))
        while n<=N:
            epochs+=1
            a,b,c,d=epoch
            end=min(N,b+d)
            changes={n}
            for row in arcs:
                if not row:continue
                t=b+row[0]+1
                if n<t<=end:changes.add(t)
                k=bisect.bisect_left(row,d)
                if k<len(row):
                    t=row[k]+1
                    if n<t<=end:changes.add(t)
                if k:
                    t=b+row[k-1]+1
                    if n<t<=end:changes.add(t)
            points=sorted(changes)
            thresholds+=len(points)-1
            for j,p in enumerate(points):
                q=points[j+1]-1 if j+1<len(points) else end
                value=risk_at(p,epoch,arcs)
                emitter.take_constant_segment(p,q,value)
                segments+=1
            n=end+1
            if n<=N: epoch=advance(*epoch)
        emitter.finish()
    data=outfile.read_bytes()
    ref=ROOT.parent/'brc_s23_av_affine_increment_codec_20261109_r16/AFFINE_RUNS_2M.tsv'
    if ref.exists():
        assert data==ref.read_bytes(), 'Prior r16 local table differs'
    assert (epochs,thresholds,emitter.count,len(emitter.signatures))==(29,6577,102,13)
    assert emitter.last_n==N and emitter.last_v==(-21156991,80688896)
    assert hashlib.sha256(data).hexdigest()=='26707bc77d7b7267495df34045f1c5111a2d21cb7c8222e83e65775897b013e1'
    print('PASS_DIRECT_FAREY_TO_AFFINE_2M')
    print('exact_theta_LO_HI',P,P+1,Q)
    print('m_n_final',M,N,'epochs',epochs,'thresholds',thresholds,'candidates_risk_calls',segments)
    print('affine_runs',emitter.count,'positive_runs',emitter.positive,'distinct_deltas',len(emitter.signatures))
    print('last_risk',emitter.last_v)
    print('stream_sha256',hashlib.sha256(data).hexdigest(),'bytes',len(data))
    print('known_prior_r16_sha_match',True)
    print('first_six',emitter.closed)
    print('elapsed_s',round(time.perf_counter()-start,3))


if __name__=='__main__':run()
