#!/usr/bin/env python3
"""X6 Unit200: exact K<=2 closed form for the frozen regression consumer."""
from __future__ import annotations
from fractions import Fraction
from math import factorial
import hashlib, subprocess, importlib.util, json, os, sys, tempfile, statistics, time, gc
from pathlib import Path
PIN='fd2bcff10ca6e147348b6c1236027fc0d2877df3'
SOURCE='experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py'
BLOB='300a96e3dc24bf6fff73743037a0347a8bc83176'
SHA='6f0d79a519c53fed1300b3fabf500c34e30aa46cdd63b409fa6ecc115071ecb4'

def load_original():
    override=os.environ.get('PINNED_SOURCE_FILE')
    b=Path(override).read_bytes() if override else subprocess.check_output(['git','show',f'{PIN}:{SOURCE}'])
    assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==BLOB
    assert hashlib.sha256(b).hexdigest()==SHA
    with tempfile.TemporaryDirectory() as d:
        p=Path(d)/'signed_brc_original_unit200.py';p.write_bytes(b)
        spec=importlib.util.spec_from_file_location('signed_brc_original_unit200',p)
        m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
    return m

def lowk_endpoint_weight(length,z,positive_weights,negative_weights):
    """Exact K=0,1,2; larger K is explicitly outside this specialized evaluator."""
    z=tuple(z);u=tuple(map(Fraction,positive_weights));v=tuple(map(Fraction,negative_weights))
    if len(z)!=6 or any(type(x) is not int for x in z):raise ValueError('six signed integer coordinates required')
    if len(u)!=6 or len(v)!=6 or any(x<=0 for x in u+v):raise ValueError('positive six-axis weights required')
    if type(length) is not int or length<0:raise ValueError('nonnegative integer length required')
    a=[max(x,0) for x in z]; b=[max(-x,0) for x in z];gap=length-sum(map(abs,z))
    if gap<0 or gap%2:return Fraction(0)
    K=gap//2
    if K>2:raise ValueError('K>2: outside proven low-pair algorithm')
    prefix=Fraction(factorial(length))
    for ai,bi,ui,vi in zip(a,b,u,v):
        prefix*=ui**ai*vi**bi/Fraction(factorial(ai)*factorial(bi))
    if K==0:return prefix
    r=[u[i]*v[i]/Fraction((a[i]+1)*(b[i]+1)) for i in range(6)]
    if K==1:return prefix*sum(r,Fraction(0))
    s=[(u[i]*v[i])**2/Fraction((a[i]+1)*(a[i]+2)*(b[i]+1)*(b[i]+2)) for i in range(6)]
    return prefix*(sum(s,Fraction(0))+sum((r[i]*r[j] for i in range(6) for j in range(i+1,6)),Fraction(0)))

def main():
    source=load_original()
    profile=[((1,)*6,(1,)*6),((1,2,3,4,5,6),(6,5,4,3,2,1)),
       ((Fraction(1,2),Fraction(2,3),Fraction(3,5),1,2,3),(Fraction(3,2),Fraction(5,4),1,Fraction(7,3),1,2))]
    zs=((0,)*6,(1,-1,0,0,0,0),(2,0,-1,0,0,0))
    checks=0
    for u,v in profile:
        for z in zs:
            n=sum(map(abs,z))
            for offset in range(5):
                args=(n+offset,z,u,v)
                x=source.endpoint_weight(*args)
                y=lowk_endpoint_weight(*args)
                assert x==y,(args,x,y)
                checks+=1
    args=[(sum(map(abs,z))+offset,z,profile[0][0],profile[0][1]) for z in zs for offset in range(5)]
    results={}
    for name,fun in [('original',source.endpoint_weight),('low_k_closed_form',lowk_endpoint_weight)]:
        samples=[]
        for _ in range(7):
            gc.collect();t=time.perf_counter_ns()
            for i in range(100):
                for a in args:fun(*a)
            samples.append((time.perf_counter_ns()-t)//100)
        results[name]={'median_ns_per_15_call_sweep':int(statistics.median(samples)),'samples_ns_per_sweep':samples}
    out={'schema':'X6_UNIT200_LOW_K_CLOSED_FORM_EXACT_V1','source_commit':PIN,'source_blob_sha1':BLOB,
         'consumer_exact_cases':15,'weight_profiles':3,'exact_comparisons':checks,'mismatches':0,
         'K_domain':[0,1,2],'odd_gap_cases_per_consumer':6,'consumer_repeats':7,
         'samples_per_repeat':100,'results':results,
         'r063_original_benchmark_rerun':False,'source_modified':False}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
