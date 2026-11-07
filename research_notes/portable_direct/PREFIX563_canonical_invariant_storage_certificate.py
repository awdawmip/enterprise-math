#!/usr/bin/env python3
"""PREFIX-563: positive coefficient canonical half-orbit storage on fixed native ports.
Frozen X6 BRC pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
import argparse,json,time,tracemalloc
from collections import Counter
import PREFIX562_semilinear_generic_axis_certificate as a

FIXED=frozenset(k for k,o in enumerate(a.ORBS) if len(o)==1)

def canonical(m):return m[4] <= m[5]

def expand_value(items,fixed,flip=False):
    if fixed:
        for m,c in items.items():
            yield (m,c)
            if m[4]!=m[5]:yield (a.sigmamon(m),c)
    else:
        for m,c in items.items():yield (a.sigmamon(m) if flip else m,c)

def step_encoded(rows, vector):
    output=[]
    for k,row in enumerate(rows):
        keep_canonical=k in FIXED
        acc=Counter()
        for (j,fl,w),mult in row.items():
            for m,c in expand_value(vector[j],j in FIXED,fl):
                mm=tuple(m[l]+w[l] for l in range(7))
                if keep_canonical and not canonical(mm):continue
                acc[mm]+=c*mult
        output.append(acc)
    return output

def full_at(v,k):
    return Counter({m:c for m,c in expand_value(v[k],k in FIXED)})

def verify(depth=12):
    r=a.b.ZERO_ROOT;rows=a.rows64_twisted(r)
    baseline=[Counter({a.ZERO:1}) for _ in range(64)]
    encoded=[Counter({a.ZERO:1}) for _ in range(64)]
    polynomial_equalities=0
    history=[]
    for d in range(depth+1):
        for k in range(64):
            assert full_at(encoded,k)==baseline[k],(d,k)
            polynomial_equalities+=1
        tot=sum(len(x) for x in baseline)
        enc=sum(len(x) for x in encoded)
        if d in (8,12,14,16):history.append({'depth':d,'regular_terms':tot,'encoded_terms':enc,'saved_terms':tot-enc})
        if d<depth:
            baseline=a.step64(rows,baseline)
            encoded=step_encoded(rows,encoded)
    return {'status':'ALL_CHECKS_PASS','depth':[0,depth], 'polynomial_equalities':polynomial_equalities,
            'representative_states':64,'invariant_fixed_orbits':len(FIXED),'term_counts':history,
            'proof':'invariant fixed polynomial under tau; retaining canonical exponent orbits; exact coefficient selection without division'}

def bench(method,depth=16):
    rows=a.rows64_twisted(a.b.ZERO_ROOT)
    vec=[Counter({a.ZERO:1}) for _ in range(64)]
    step=a.step64 if method=='plain64' else step_encoded
    start=time.perf_counter();tracemalloc.start();out_positions=0
    for d in range(depth+1):
        for i in range(96):
            k=a.IDX[i]
            if method=='plain64':out_positions+=len(vec[k])
            elif k in FIXED:out_positions+=2*len(vec[k])-sum(m[4]==m[5] for m in vec[k])
            else:out_positions+=len(vec[k])
        if d<depth:vec=step(rows,vec)
    elapsed=time.perf_counter()-start;cur,peak=tracemalloc.get_traced_memory();tracemalloc.stop()
    return {'algorithm':method,'depth':depth,'time_sec':round(elapsed,5),'tracemalloc_peak_bytes':peak,
            'final_resident_term_positions':sum(len(x) for x in vec),
            'full96_output_support_traversal':out_positions}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--bench',choices=['plain64','canonical64']);p.add_argument('--depth',type=int,default=12);arg=p.parse_args()
    print(json.dumps(bench(arg.bench,arg.depth) if arg.bench else verify(arg.depth),indent=2))
