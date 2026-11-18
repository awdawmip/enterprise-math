from math import isqrt
from dataclasses import dataclass
from time import perf_counter_ns
from statistics import median
from os import environ
from pathlib import Path
import sys
import tracemalloc

source_root = Path(environ["EM_SOURCE_ROOT"]).resolve()
sys.path.insert(0, str(source_root / "src"))
from enterprise_math import brc_table_free_tail as original
from enterprise_math import brc_pairwise_multiplier_transport as pair
import shared_tail as shared

@dataclass
class State:
    n: int
    multiplier: int
    root: int
    remainder: int

def state(n,m):
    j=isqrt(m*n)
    return State(n,m,j,m*n-j*j)

def direct(s,t,k):
    assert s.n>0 and s.multiplier>0 and t-s.multiplier in (1,2)
    assert s.root*s.root+s.remainder==s.multiplier*s.n and 0<=s.remainder<=2*s.root
    out=state(s.n,t)
    assert out.root**2+out.remainder==t*s.n and 0<=out.remainder<=2*out.root
    return out.root,out.remainder

def step(mod,s,t,k):
    out=mod.transport_certified_tail(s,t,degree=k)
    return out.root,out.remainder

ref=lambda s,t,k: step(original,s,t,k)
new=lambda s,t,k: step(shared,s,t,k)
def pairwise(s,t,k):
    out=pair.transport_multiplier_root_state(s,t)
    return out.root,out.remainder

def reset():
    for mod in (original,shared):
        mod.binomial_half_coefficients.cache_clear()
        mod.scaled_even_truncation.cache_clear()
    pair.pairwise_scale_constant.cache_clear()

def threshold(n,k,h):
    m=h
    while not original.two_correction_certificate(isqrt(n*m),m,h,k):
        m*=2
    lo=h-1
    while m>lo+1:
        v=(lo+m)//2
        if original.two_correction_certificate(isqrt(n*v),v,h,k):
            m=v
        else:
            lo=v
    return m

def samples(n,k):
    inputs=[]
    for h in (1,2):
        first=threshold(n,k,h)
        for i in range(16):
            m=first+i
            s=state(n,m)
            assert original.two_correction_certificate(s.root,m,h,k)
            inputs.append((s,m+h,k))
    return inputs

def bench(cases):
    funcs=[ref,new,direct]
    if max(t for s,t,k in cases)<=pair.MAX_MULTIPLIER:
        funcs.append(pairwise)
    assert all(fn(*args)==direct(*args) for args in cases for fn in funcs)
    warm={fn:[] for fn in funcs}
    cold={fn:[] for fn in funcs}
    peak={}
    for rep in range(11):
        for fn in funcs[rep%len(funcs):]+funcs[:rep%len(funcs)]:
            reset()
            start=perf_counter_ns()
            for args in cases: fn(*args)
            cold[fn].append((perf_counter_ns()-start)/len(cases))
            start=perf_counter_ns()
            for j in range(20):
                for args in cases: fn(*args)
            warm[fn].append((perf_counter_ns()-start)/(len(cases)*20))
    for fn in funcs:
        reset()
        for args in cases: fn(*args)
        peaks=[]
        for args in cases:
            tracemalloc.start()
            fn(*args)
            peaks.append(tracemalloc.get_traced_memory()[1])
            tracemalloc.stop()
        peak[fn]=max(peaks)
    return [(round(median(warm[fn])),round(median(cold[fn])),peak[fn]) for fn in funcs]

def verify():
    passed=rejected=0; counts=[0,0,0]
    primes=[3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    ns=sorted({p*q for p in primes for q in primes if p<=q})
    for n in ns:
        for h in (1,2):
            for m in range(h,64):
                s=state(n,m)
                for k in (2,4,8,16):
                    a=original.two_correction_certificate(s.root,m,h,k)
                    assert a==shared.two_correction_certificate(s.root,m,h,k)
                    if not a:
                        try: shared.transport_certified_tail(s,m+h,degree=k)
                        except ValueError: pass
                        else: assert False
                        rejected+=1
                        continue
                    x=original.transport_certified_tail(s,m+h,degree=k)
                    y=shared.transport_certified_tail(s,m+h,degree=k)
                    assert vars(x)==vars(y) and (y.root,y.remainder)==direct(s,m+h,k)
                    counts[y.correction_steps]+=1
                    passed+=1
    return passed,rejected,counts

print(sys.version)
print('checks',verify())
for a,b in ((61,127),(521,607),(1279,2203)):
    n=(2**a-1)*(2**b-1)
    for k in (2,8,32):
        cases=samples(n,k)
        hs=[threshold(n,k,h) for h in (1,2)]
        print('measurement',n.bit_length(),k,[m.bit_length() for m in hs],max((m.multiplier**k).bit_length() for m,t,k in cases),bench(cases),flush=True)
