#!/usr/bin/env python3
"""Exact typed X6 atlas-transition diagnostic; author science, not a native benchmark.
Source gauges/unit91: frozen four-chart atlas. All arithmetic integer and exhaustive
in 20x20 sorted named-generator word pairs; 6 basis vectors per pair.
"""
from itertools import combinations
from collections import Counter
import json

N=6
TRIADS=tuple(combinations(range(6),3))
ATLAS=(( -1,-1,-1,-1, 1,-1),
       ( -1,-1, 1,-1, 1, 1),
       ( -1,-1, 1, 1,-1,-1),
       ( -1, 1,-1,-1,-1,-1))
ID=tuple(range(1,7))

def gauge(s): return tuple((i+1)*s[i] for i in range(N))
def comp(f,g): return tuple((1 if x>0 else -1)*f[abs(x)-1] for x in g)
def chain(*fs):
    x=ID
    for f in reversed(fs):x=comp(f,x)
    return x

def apply(f,z):
    out=[0]*N
    for i,x in enumerate(f):out[abs(x)-1]+=(1 if x>0 else -1)*z[i]
    return tuple(out)
def rho(z):
    m=min(z)
    return tuple(x-m for x in z)
def q(t):
    i,j,k=t; x=list(ID)
    x[i]=-(j+1);x[j]=-(k+1);x[k]=-(i+1)
    return tuple(x)
def g(t):
    i,j,k=t; x=list(ID)
    x[i]=j+1;x[j]=k+1;x[k]=-(i+1)
    return tuple(x)
def admissible(s,t):
    i,j,k=t
    return s[i]==s[k]==-s[j]

ASSIGN={t:next(i for i,s in enumerate(ATLAS) if admissible(s,t)) for t in TRIADS}
assert len(ASSIGN)==20
assert all(sum(admissible(s,t) for s in ATLAS)==1 for t in TRIADS)
metrics=Counter(); hist=Counter(); witness=None; sym={}
for a in TRIADS:
  for b in TRIADS:
    ia,ib=ASSIGN[a],ASSIGN[b]
    sa,sb=ATLAS[ia],ATLAS[ib]
    da,db=gauge(sa),gauge(sb)
    qa,qb=q(a),q(b)
    ga,gb=g(a),g(b)
    true=chain(qb,qa)
    corrected=chain(db,gb,db,da,ga,da)
    naive=chain(db,gb,ga,da)
    assert true==corrected
    assert chain(da,ga,da)==qa and chain(db,gb,db)==qb
    h=sum(x!=y for x,y in zip(sa,sb))
    assert sum(x!=y for x,y in zip(true,naive))==h
    assert (naive==true)==(ia==ib)
    metrics['pairs_checked']+=1
    metrics['corrected_pairs']+=corrected==true
    metrics['naive_good_pairs']+=naive==true
    metrics['naive_bad_pairs']+=naive!=true
    metrics['basis_vectors_checked']+=N
    metrics['mismatching_basis_images']+=h
    hist[h]+=1
    if ia!=ib and witness is None:
      for v in range(N):
        z=tuple(int(i==v) for i in range(N))
        u,w=apply(true,z),apply(naive,z)
        if u!=w:
          assert rho(u)!=rho(w)
          witness={'first_triad':a,'second_triad':b,
                   'first_chart':ia,'second_chart':ib,'basis_axis':v,
                   'true_raw':u,'naive_raw':w,'true_relative':rho(u),'naive_relative':rho(w)}
          break
for i in range(4):
 for j in range(i+1,4):
    sym[f'{i}{j}']=sum(x!=y for x,y in zip(ATLAS[i],ATLAS[j]))
assert metrics['pairs_checked']==400 and metrics['naive_good_pairs']==112 and metrics['naive_bad_pairs']==288
assert metrics['corrected_pairs']==400
for m in range(1,11):
    z0=(0,)*N; zm=(m,)*N
    assert (rho(z0),min(z0)%m)==(rho(zm),min(zm)%m)
    assert rho(apply(gauge(ATLAS[2]),z0))!=rho(apply(gauge(ATLAS[2]),zm))
report={'schema':'X6_UNIT92_TWO_GENERATOR_CHART_TRANSITION_EXACT_V1','date':'2026-11-17',
        'classification':'AUTHOR-EXACT / FINITE-EXECUTED / UNREVIEWED / NOT_ADMITTED',
        'scope':'20x20 ordered named triad pairs and 6 signed basis images; distinct-chart omission witness',
        'atlas':ATLAS,'triad_chart_sizes':tuple(sum(v==i for v in ASSIGN.values()) for i in range(4)),
        'metrics':dict(sorted(metrics.items())),
        'raw_mismatch_basis_count_histogram':{str(k):v for k,v in sorted(hist.items())},
        'chart_pair_hamming':sym,'first_witness':witness,
        'finite_depth_nonfactorization':'for every m>=1 via z=0,z=m*1 in mixed-sign chart C; exact analytic proof, tested m 1..10',
        'native_R063_Helly_reexecuted':False,
        'existing_source_consumer_misuse_proved':False}
print(json.dumps(report,sort_keys=True,ensure_ascii=False,indent=2))
