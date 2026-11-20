#!/usr/bin/env python3
"""Unit196: pinned native signed-X6 weighted BRC versus independent lazy/nonlazy A5 DPs."""
from __future__ import annotations
import hashlib, importlib.util, json
from collections import defaultdict
from fractions import Fraction
from math import comb
from pathlib import Path

HERE=Path(__file__).resolve().parent
SRC=HERE/'signed_brc.py'
EXPECTED_BLOB='300a96e3dc24bf6fff73743037a0347a8bc83176'
raw=SRC.read_bytes()
actual=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
if actual != EXPECTED_BLOB:
    raise RuntimeError(f'frozen native production blob mismatch: {actual}')
spec=importlib.util.spec_from_file_location('x6_unit196_pinned_signed_brc',SRC)
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)

ZERO=(0,)*6

def ensure(cond,message):
    if not cond: raise RuntimeError(message)

def dp_weighted_pairs(nmax,u,v,allow_zero):
    d={ZERO:Fraction(1)}
    out=[d]
    choices=[]
    for i in range(6):
        for j in range(6):
            if not allow_zero and i==j: continue
            move=[0]*6;move[i]+=1;move[j]-=1
            choices.append((tuple(move),u[i]*v[j]))
    for _ in range(nmax):
        nd=defaultdict(Fraction)
        for z,prev in d.items():
            for step,w in choices:
                zz=tuple(a+b for a,b in zip(z,step))
                nd[zz]+=prev*w
        d=dict(nd)
        out.append(d)
    return out

def native_weight_dp(length,u,v):
    d={ZERO:Fraction(1)}
    for _ in range(length):
        nd=defaultdict(Fraction)
        for z,mass in d.items():
            for i in range(6):
                a=list(z);a[i]+=1;nd[tuple(a)]+=mass*u[i]
                b=list(z);b[i]-=1;nd[tuple(b)]+=mass*v[i]
        d=dict(nd)
    return d

def fstr(x):
    x=Fraction(x)
    return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'

weights=[
    ('distinct_integers',list(map(Fraction,[2,3,5,7,11,13])),list(map(Fraction,[17,19,23,29,31,37])),4),
    ('positive_fractions',list(map(Fraction,['1/2','2/3','3/4','4/5','5/6','6/7'])),list(map(Fraction,['7/6','6/5','5/4','4/3','3/2','2'])),3),
    ('unit_weights',[Fraction(1)]*6,[Fraction(1)]*6,3)
]
result={'schema':'X6_UNIT196_WEIGHTED_LAZY_A5_EXACT_CHECK_V1','date':'2026-11-20',
        'pinned_producer':{'repo':'awdawmip/enterprise-math','commit':'fd2bcff10ca6e147348b6c1236027fc0d2877df3',
           'path':'experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py',
           'blob_sha1':actual,'source_sha256':hashlib.sha256(raw).hexdigest(),
           'function':'endpoint_weight'},
        'checks':[],'total_endpoint_length_comparisons':0,'total_native_dp_endpoint_checks':0,'violations':0,'native_R063_benchmark_rerun':False}
for name,u,v,nmax in weights:
    lazy=dp_weighted_pairs(nmax,u,v,True)
    nonlazy=dp_weighted_pairs(nmax,u,v,False)
    c=sum((u[i]*v[i] for i in range(6)),Fraction(0))
    one={'weight_id':name,'u':list(map(fstr,u)),'v':list(map(fstr,v)),
         'zero_pair_mass_c':fstr(c),'max_n':nmax,'layers':[]}
    for n in range(nmax+1):
        checks=0
        for z,lv in lazy[n].items():
            from_producer=mod.endpoint_weight(2*n,z,u,v)
            ensure(from_producer == comb(2*n,n)*lv,f'producer/lazy mismatch {name} n={n} z={z}')
            inverted=sum((Fraction(comb(n,k))*(-c)**(n-k)*lazy[k].get(z,Fraction(0)) for k in range(n+1)),Fraction(0))
            ensure(inverted == nonlazy[n].get(z,Fraction(0)),f'nonlazy inversion mismatch {name} n={n} z={z}')
            checks+=1
        for z in nonlazy[n]:
            ensure(z in lazy[n],f'nonlazy support missing in lazy {name} n={n} z={z}')
        total_lazy=sum(lazy[n].values(),Fraction(0))
        total_nonlazy=sum(nonlazy[n].values(),Fraction(0))
        ensure(total_lazy==(sum(u)*sum(v))**n,'total lazy mass mismatch')
        ensure(total_nonlazy==(sum(u)*sum(v)-c)**n,'total nonlazy mass mismatch')
        native_checks=0
        if (name=='distinct_integers' and n<=3) or (name=='positive_fractions' and n<=2):
            dist=native_weight_dp(2*n,u,v)
            ensure(sum(dist.values(),Fraction(0))==(sum(u)+sum(v))**(2*n),'native full total mass mismatch')
            for z in lazy[n]:
                ensure(dist[z] == comb(2*n,n)*lazy[n][z],f'native signed DP mismatch {name} n={n} z={z}')
                native_checks+=1
        result['total_endpoint_length_comparisons']+=checks
        result['total_native_dp_endpoint_checks']+=native_checks
        one['layers'].append({'n':n,'distinct_balanced_endpoints':len(lazy[n]),
              'coefficient_checks':checks,'independent_native_DP_endpoint_checks':native_checks,
              'weighted_lazy_total':fstr(total_lazy),'weighted_nonlazy_total':fstr(total_nonlazy)})
    samples=[ZERO,(1,-1,0,0,0,0),(2,-2,0,0,0,0)]
    one['example_n2']={str(z):{'native_E4':fstr(mod.endpoint_weight(4,z,u,v)),
                                     'lazy_L2':fstr(lazy[2].get(z,0)),
                                     'nonlazy_A2':fstr(nonlazy[2].get(z,0))} for z in samples}
    result['checks'].append(one)

serialized=json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False)+'\n'
outfile=HERE/'X6_UNIT196_WEIGHTED_LAZY_A5_INVERSION_RESULTS_20261120.json'
outfile.write_text(serialized,encoding='utf-8')
print(json.dumps({'profiles':len(result['checks']),
              'endpoint_length_comparisons':result['total_endpoint_length_comparisons'],
              'native_DP_endpoint_checks':result['total_native_dp_endpoint_checks'],
              'violations':result['violations'],
              'output_sha256':hashlib.sha256(serialized.encode()).hexdigest(),
              'data':str(outfile)},sort_keys=True))
