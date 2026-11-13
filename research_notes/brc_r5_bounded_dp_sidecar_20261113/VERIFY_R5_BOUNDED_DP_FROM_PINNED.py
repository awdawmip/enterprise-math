#!/usr/bin/env python3
"""Verify exact radius-bounded DP and sidecar on the frozen R5 stacked certificate corpus.
Run from Enterprise Math checkout with predecessor R5 verifier present.
This is a certificate-query auxiliary model, not native heartbeat evolution.
"""
from pathlib import Path
from bisect import bisect_left, bisect_right
from array import array
from fractions import Fraction
import hashlib, json, random, statistics, sys, time

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'brc_r5_offline_fenwick_20261112'))
import VERIFY_R5_OFFLINE_FENWICK_FROM_PINNED as P
N,M,lohi,pairs,walls=P.N,P.M,P.lohi,P.pairs,P.walls
assert (N,M,len(walls))==(2880,1065,953)
W=len(walls);n=W+1;K=213;R=2
wall_idx={wall:i for i,wall in enumerate(walls)}
codes=[wall_idx[(1-Fraction(36*q,den))/23] for q,den in pairs]
freq=[0]*W
for c in codes:freq[c]+=1
E=[0]
for f in freq:E.append(E[-1]+f)
assert E[-1]==M and 1<=min(freq)<=max(freq)<=3
ordinals=sorted(range(M),key=lambda i:(codes[i],i))
prefix=[0]
for x in E:prefix.append(prefix[-1]+x)
INF=10**20

def segment(i,j,s):
    return ((s-i+1)*E[s]-(prefix[s+1]-prefix[i])+
            (prefix[j+1]-prefix[s+1])-(j-s)*E[s])

def bounded(i,j):
    if E[j]-E[i]>2*R:return INF,None
    lo=bisect_left(E,E[j]-R,i,j+1)
    hi=bisect_right(E,E[i]+R,i,j+1)-1
    if lo>hi:return INF,None
    s=max(lo,min(hi,(i+j)//2))
    return segment(i,j,s),s



# Radius-bounded local DP. Since E increments by >=1, every valid segment
# contains at most (2*R+1) boundary points, so there are O(n*R) edges per layer.
def bounded_optimal():
    windows=[[] for _ in range(n+1)]
    for j in range(1,n+1):
        i=j-1
        while i>=0 and E[j-1]-E[i]<=2*R:
            cost,s=bounded(i,j-1)
            if cost<INF:
                windows[j].append((i,cost,s))
            i-=1
    edges=sum(map(len,windows))
    prev=[0]+[INF]*n
    parents=[]
    for k in range(1,K+1):
        curr=[INF]*(n+1)
        choice=[None]*(n+1)
        for j in range(k,min(n,k*(2*R+1))+1):
            for i,price,s in windows[j]:
                value=prev[i]+price
                if value<curr[j]:
                    curr[j]=value
                    choice[j]=(i,s)
        prev=curr
        parents.append(choice)
    assert prev[n]<INF
    centers=[];j=n
    for k in range(K,0,-1):
        i,s=parents[k-1][j]
        centers.append(s);j=i
    assert j==0
    centers=sorted(set(centers))
    assert len(centers)==K
    return prev[n],centers,edges

def directory(centers):
    out=bytearray(n);z=0
    for b,x in enumerate(E):
        while z+1<len(centers) and 2*x>E[centers[z]]+E[centers[z+1]]:
            z+=1
        out[b]=z
    return bytes(out)

def serialize(centers):
    return (len(centers).to_bytes(2,'little')
            +b''.join(c.to_bytes(2,'little') for c in centers)
            +directory(centers))

def validate(raw,full=False):
    z=int.from_bytes(raw[:2],'little')
    if z!=K or len(raw)!=2+2*z+n:raise ValueError("sidecar length/budget")
    centers=[int.from_bytes(raw[2+2*i:4+2*i],'little') for i in range(z)]
    indices=raw[2+2*z:]
    if not all(0<=x<n for x in centers) or centers!=sorted(set(centers)):
        raise ValueError("sidecar checkpoint indices")
    if indices!=directory(centers):raise ValueError("sidecar nearest-center directory")
    residuals=[abs(E[b]-E[centers[indices[b]]]) for b in range(n)]
    if max(residuals)>R or sum(residuals)!=1070:
        raise ValueError("sidecar residual guarantee")
    if not full:return len(residuals),max(residuals),sum(residuals)
    masks=[];bits=0;t=0
    for s in centers:
        while t<E[s]:
            bits|=1<<ordinals[t];t+=1
        masks.append(bits)
    checks=0
    for b in range(n):
        rank=[0]
        for c in codes:rank.append(rank[-1]+int(c<b))
        pos=indices[b];s=centers[pos]
        for left,right in lohi:
            count=((masks[pos]>>left)&((1<<(right-left))-1)).bit_count()
            if E[b]>E[s]:
                count+=sum(left<=ordinals[t]<right for t in range(E[s],E[b]))
            elif E[b]<E[s]:
                count-=sum(left<=ordinals[t]<right for t in range(E[b],E[s]))
            assert count==rank[right]-rank[left],(b,left,right)
            checks+=1
    return checks,max(residuals),sum(residuals)

J,centers,edges=bounded_optimal()
assert (J,len(centers),edges)==(1070,213,4214)
sidecar=serialize(centers)
assert len(sidecar)==1382
assert hashlib.sha256(sidecar).hexdigest()=="94341ccf1aa09eb0eb42c045201b36dc9589008209fe77f446d8a4b93cee68b6"
assert hashlib.sha256(sidecar[428:]).hexdigest()=="a947d07d7d494e00e14013eb929b3ffdc9224938ec15289209e68316c50a14b1"
damaged=bytearray(sidecar);damaged[-1]=(damaged[-1]+1)%K
try:
    validate(damaged)
    raise AssertionError("corruption accepted")
except ValueError:
    pass
timed_dp=[];timed_read=[]
for t in range(9):
    start=time.perf_counter()
    j,s,e=bounded_optimal()
    timed_dp.append((time.perf_counter()-start)*1000)
    assert (j,s,e)==(J,centers,edges)
    start=time.perf_counter()
    validate(sidecar)
    timed_read.append((time.perf_counter()-start)*1000)
start=time.perf_counter()
checks,radius,total=validate(sidecar,full=True)
full_ms=(time.perf_counter()-start)*1000
assert (checks,radius,total)==(2747520,2,1070)
out={'status':'PASS_R5_BOUNDED_LOCAL_DP_SIDECAR',
     'pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
     'coordinates':28,'operations':15,'nodes':N,'certificates':M,
     'walls':W,'boundaries':n,'checkpoints':K,'radius':R,
     'optimal_uniform_correction_sum':J,'edges_per_layer':edges,
     'sidecar_bytes':len(sidecar),
     'sidecar_sha256':hashlib.sha256(sidecar).hexdigest(),
     'directory_sha256':hashlib.sha256(sidecar[428:]).hexdigest(),
     'exact_full_node_boundary_checks':checks,
     'corrupt_directory_test':'REJECTED',
     'dp_repeated_median_ms':round(statistics.median(timed_dp),3),
     'sidecar_validation_median_ms':round(statistics.median(timed_read),3),
     'full_exhaustive_ms':round(full_ms,3)}
print(json.dumps(out,sort_keys=True,indent=2))
