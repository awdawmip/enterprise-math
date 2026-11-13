#!/usr/bin/env python3
"""Reproduce R5 exact byte directory from the frozen stacked certificate corpus.
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

def optimal_centers():
    prev=[0]+[INF]*n
    rows=[]
    for k in range(1,K+1):
        curr=[INF]*(n+1);choice=array('H',[0])*(n+1)
        for j in range(k,n+1):
            best=INF;bi=0
            for i in range(j-1,k-2,-1):
                if E[j-1]-E[i]>2*R:break
                val,s=bounded(i,j-1)
                if val==INF:continue
                val+=prev[i]
                if val<best:best=val;bi=i
            curr[j]=best;choice[j]=bi
        prev=curr;rows.append(choice)
    assert prev[-1]<INF
    centers=[];j=n
    for k in range(K,0,-1):
        i=rows[k-1][j];cost,s=bounded(i,j-1)
        assert cost<INF
        centers.append(s);j=i
    assert j==0
    return prev[-1],centers[::-1]

J,centers=optimal_centers()
assert J==1070 and len(centers)==K and len(set(centers))==K
coords=[E[c] for c in centers]

# Build immutable activation bitmaps by increasing event count.
bitmaps=[];bits=0;ptr=0
for count in coords:
    while ptr<count:
        bits|=1<<ordinals[ptr];ptr+=1
    bitmaps.append(bits)

def choose(b):
    target=E[b];z=bisect_left(coords,target)
    if z==0:return 0
    if z==K:return K-1
    return z if coords[z]-target < target-coords[z-1] else z-1

# Direct-address 954-byte array; center IDs 0..212.
center_of_wall=bytes(choose(b) for b in range(n))
assert len(center_of_wall)==954
# Exact Voronoi boundary characterization; ties go to the left.
transitions=[bisect_right(E,(coords[i]+coords[i+1])//2)-1 for i in range(K-1)]
assert list(center_of_wall)==[bisect_left(transitions,b) for b in range(n)]
assert max(abs(E[b]-coords[center_of_wall[b]]) for b in range(n))==2
E16=array('H',E);coords16=array('H',coords)

def evaluate(v,b,z,compact=False):
    left,right=lohi[v]
    if left==right:return 0
    target=(E16 if compact else E)[b]
    saved=(coords16 if compact else coords)[z]
    ans=((bitmaps[z]>>left)&((1<<(right-left))-1)).bit_count()
    if saved<target:
        for j in range(saved,target):ans+=int(left<=ordinals[j]<right)
    elif saved>target:
        for j in range(target,saved):ans-=int(left<=ordinals[j]<right)
    return ans

# Exhaustive full wall-boundary x prefix-node check against direct rank oracle.
full_checks=0
for b in range(n):
    cumulative=[0]
    for code in codes:cumulative.append(cumulative[-1]+int(code<b))
    z=center_of_wall[b]
    assert z==choose(b)
    for v,(left,right) in enumerate(lohi):
        truth=cumulative[right]-cumulative[left]
        assert evaluate(v,b,z)==truth
        assert evaluate(v,b,z,True)==truth
        full_checks+=1
assert full_checks==2747520

# Interleaved repeated timings; parameter-to-wall bisect is charged to every query.
def query(v,r,method):
    b=bisect_right(walls,r)
    if method=='binary':z=choose(b)
    else:z=center_of_wall[b]
    return evaluate(v,b,z,method=='compact')

rng=random.Random(2026111309)
large=[v for v,(left,right) in enumerate(lohi) if right-left>=32]
pool=walls+[ (walls[i]+walls[i+1])/2 for i in range(0,W-1,17)]
workloads={}
for kind,num in [('random',8192),('hotmix',8192),('root',1024)]:
    nodes=([0]*num if kind=='root' else
           [rng.choice([0]+large[:16]) if rng.randrange(4) else rng.randrange(N)
            for _ in range(num)] if kind=='hotmix' else
           [rng.randrange(N) for _ in range(num)])
    requests=list(zip(nodes,[rng.choice(pool) for _ in range(num)]))
    gold=[query(v,r,'binary') for v,r in requests]
    times={name:[] for name in ('binary','direct','compact')}
    for _ in range(15):
        names=list(times);rng.shuffle(names)
        for name in names:
            begin=time.perf_counter_ns()
            actual=[query(v,r,name) for v,r in requests]
            elapsed=(time.perf_counter_ns()-begin)/1e6
            assert actual==gold
            times[name].append(elapsed)
    workloads[kind]={'queries':num,'checksum':sum(gold),
        'median_ms':{name:round(statistics.median(series),3)
                     for name,series in times.items()}}

out={'status':'EXACT_VERIFIED_R5_DIRECT_ADDRESS_DIRECTORY',
     'scientific_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
     'N':N,'M':M,'W':W,'K':K,'radius':R,'mean_total':J,
     'checks':full_checks,
     'direct_directory_bytes':len(center_of_wall),
     'direct_directory_sha256':hashlib.sha256(center_of_wall).hexdigest(),
     'selected_python_bytes':{'binary_centers':sys.getsizeof(coords)+sum(map(sys.getsizeof,coords)),
         'compact_directory_plus_centers':sys.getsizeof(center_of_wall)+sys.getsizeof(coords16),
         'E_list':sys.getsizeof(E)+sum(map(sys.getsizeof,E)),
         'E_uint16':sys.getsizeof(E16)},
     'timings':workloads}
print(json.dumps(out,sort_keys=True,ensure_ascii=False,indent=2))
