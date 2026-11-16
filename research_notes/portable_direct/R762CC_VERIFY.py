#!/usr/bin/env python3
"""R762CC exact census. Python3 stdlib. All 729 coherent S6xC3 sign-only laws."""
import itertools, collections, json
R=(1,1,3,3)
OPTIONS=[((0,0),)+tuple((1,m) for m in range(1<<r)) for r in R]

def B(k,m):
    if k==0: return int(m==0)
    if k==1: return (3**m+3*((-1)**m))//4
    if k==2: return (6**m+4+5*((-2)**m))//10
    if k==3: return (9**m+5*3**m+9*((-1)**m)+5*((-3)**m))//20
    raise AssertionError(k)

def features(P):
    n=[0]*4
    sector=[]; rooted=[]; closure=[]
    for r,(c,mask) in zip(R,P):
        k=mask.bit_count()
        if c: n[k]+=r
        sector.append((c,k))
        rooted += [(mask>>j)&1 for j in range(r)]
        closure.append(c)
    A=(sum(n),sum(n[k]*B(k,4) for k in range(4)))
    S=tuple(sector)
    S_two_count=tuple((c,3*k if c else 0) for c,k in S)
    E=tuple(rooted)
    J=tuple(closure)+E
    return tuple(n),A,S,S_two_count,E,J

P=list(itertools.product(*OPTIONS))
assert len(P)==729
F=list(map(features,P))
targets={'aggregate':(1,90),'sector':(2,225),'event':(4,256),'joint':(5,729)}
hist={}
for name,(i,count) in targets.items():
    buckets=collections.Counter(f[i] for f in F)
    assert len(buckets)==count,(name,len(buckets))
    hist[name]=dict(sorted(collections.Counter(buckets.values()).items()))
assert hist['aggregate']=={1:9,2:18,4:9,6:18,9:6,12:18,18:9,36:3}
assert hist['sector']=={1:81,3:108,9:36}
assert hist['event']=={1:49,2:112,4:78,8:16,16:1}
assert hist['joint']=={1:729}
assert len({f[3] for f in F})==225
for f in F:
    n=f[0]
    assert f[1]==(sum(n),sum(n[k]*B(k,4) for k in range(4)))
    for k in range(4): assert B(k,0)==1 and B(k,2)==3*k
# Compare closed sign orbit with singleton gate at different rooted positions:
p=((0,0),(0,0),(1,1),(0,0))
q=((0,0),(0,0),(1,2),(0,0))
a,b=features(p),features(q)
assert a[2]==b[2] and a[4]!=b[4] and a[0]==b[0]
assert a[1]==(3,63)
for m in range(25):
    assert sum(a[0][k]*B(k,m) for k in range(4))==sum(b[0][k]*B(k,m) for k in range(4))
# Same permission table, different closure:
p2=((1,0),(0,0),(0,0),(0,0))
q2=((0,0),(0,0),(0,0),(0,0))
assert features(p2)[4]==features(q2)[4] and features(p2)[2]!=features(q2)[2]
# One baseline forces every one of the 4 closure + 8 gate point queries.
base=tuple((1,0) for _ in R)
baseJ=features(base)[5]
assert len(baseJ)==12
for i,r in enumerate(R):
    alt=list(base);alt[i]=(0,0)
    assert sum(x!=y for x,y in zip(baseJ,features(tuple(alt))[5]))==1
    for j in range(r):
        alt=list(base);alt[i]=(1,1<<j)
        assert sum(x!=y for x,y in zip(baseJ,features(tuple(alt))[5]))==1
out={
  "schema":"ENTERPRISE_MATH_R762CC_EXACT_POLICY_OBSERVER_CENSUS_V1",
  "scope":"conditional signed S6xC3 sign-only 729-laws of R762CA/R762CB; native event licensing unproved",
  "population":729,
  "orbit_sizes":[1,1,3,3],
  "options_per_orbit":[3,3,9,9],
  "quotient_class_counts":{name:n for name,(_,n) in targets.items()},
  "fiber_size_histograms":hist,
  "fixed_index_bits":{"aggregate":7,"sector":8,"event":8,"joint":10},
  "rooted_event_query_worst_case":8,
  "joint_closure_event_query_worst_case":12,
  "two_count_sector_probe":"N_s(0), N_s(2)=3k for closed sector",
  "witness_1":{"policies": [str(p),str(q)],"same_sign_spectra":True,"different_rooted_gate":True,"N0_N4":list(a[1])},
  "witness_2":{"policies":[str(p2),str(q2)],"same_event_gates":True,"different_closure":True},
  "independent_review":"NOT_REVIEWED"}
print(json.dumps(out,indent=2,sort_keys=True,ensure_ascii=False))
