#!/usr/bin/env python3
"""Wall-clock benchmark: dense exact signatures, sparse exact trace, and expansion.
Single Python runtime, non-performance-guarantee; no external dependencies.
"""
from fractions import Fraction as F
from time import perf_counter_ns
from statistics import median
from pathlib import Path
import json
from check_r130 import integer_roots,word,sparse_sweep

def dense(x,A,d,E,m,l,h):
    cuts=set(integer_roots(F(0),E,l,h))
    for i in range(m):
        s=A+i*d
        cuts.update(integer_roots(x,s,l,h))
        cuts.update(integer_roots(x,s-E,l,h))
    cuts=sorted(cuts)
    seq=[]
    seq.append(word(x,A,d,E,m,(l+cuts[0])/2 if cuts else (l+h)/2))
    for j,p in enumerate(cuts):
        seq.append(word(x,A,d,E,m,p))
        seq.append(word(x,A,d,E,m,(p+(cuts[j+1] if j+1<len(cuts) else h))/2))
    return seq

def expand(log):
    state=log['initial_word'][:]
    out=[tuple(state)]
    for e in log['events']:
        c=state[:]
        for i,v in e['cut_delta']:
            c[i]=v
        out.append(tuple(c))
        for i,v in e['right_delta']:
            state[i]=v
        out.append(tuple(state))
    return out

def measured(fn,repeat=3):
    results=[];ret=None
    for j in range(repeat):
        t0=perf_counter_ns();ret=fn();t1=perf_counter_ns()
        results.append((t1-t0)/1e6)
    return median(results),ret

def main():
    rows=[]
    for m in (16,32,64):
        args=(F(0),0,1,1,m,F(0),F(1))
        dms,ds=measured(lambda:dense(*args))
        sms,sp=measured(lambda:sparse_sweep(*args))
        ems,ex=measured(lambda:expand(sp))
        assert ds==ex
        rows.append({'m':m,'cuts':sp['cuts'],'signatures':len(ds),
                     'dense_median_ms':round(dms,3),'sparse_median_ms':round(sms,3),
                     'expand_median_ms':round(ems,3),
                     'dense_indicator_evaluations':m*len(ds),
                     'sparse_indicator_evaluations':sp['evaluations']})
    result={'status':'R130_BENCHMARK_MATCH','method':'CPython Fraction perf_counter_ns, median of 3 independent builds, no warmup',
            'environment':'local container, no CPU frequency pinning','rows':rows,
            'warning':'wall times are machine- and representation-dependent; exact correctness checked separately'}
    print(json.dumps(result,indent=2,sort_keys=True))
    Path(__file__).with_name('benchmark_r130.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
if __name__=='__main__':main()
