#!/usr/bin/env python3
"""Full 48-root polynomial outputs: shared 28-class gauge vs PREFIX-542 49-coordinate implementation. Requires adjacent PREFIX545_compact_exact_certificate.py, PREFIX542_exact_certificate.py, PREFIX546_shared_gauge_certificate.py."""
import gc,json,statistics,time,tracemalloc
import PREFIX545_compact_exact_certificate as b
import PREFIX542_exact_certificate as ref
import PREFIX546_shared_gauge_certificate as g

def all28(D,classes,Q):
    out=[[None]*(D+1) for _ in range(48)]
    for r in (-1,0,1):
        roots=[i for i in range(48) if b.sign(i)==r]
        v=[{(0,0):1} for _ in range(28)]
        for depth in range(D+1):
            for i in roots:out[i][depth]=v[classes[2*i]]
            if depth<D:v=b.qstep(Q[r],v)
    return out

def measure(fn,repetitions=5):
    times=[];memory=[];result=None
    for _ in range(repetitions):
        gc.collect();tracemalloc.start();start=time.perf_counter()
        result=fn();times.append(time.perf_counter()-start)
        _,peak=tracemalloc.get_traced_memory();tracemalloc.stop();memory.append(peak)
    return statistics.median(times),statistics.median(memory),result

def run():
    prep,prep_peak,_=measure(g.shared)
    labels,Q,_=g.shared()
    results=[]
    for depth in (8,16,24):
        t28,m28,out=measure(lambda:all28(depth,labels,Q))
        t49,m49,baseline=measure(lambda:ref.rank49_all(depth))
        assert out==baseline
        results.append({'depth':depth,'exact_output_polynomials':48*(depth+1),'28_core_sec':t28,'28_plus_precompute_sec':t28+prep,'49_core_sec':t49,'28_core_peak_bytes':m28,'49_core_peak_bytes':m49,'end_to_end_speedup_49_over_28':t49/(t28+prep)})
    return {'status':'ALL_CHECKS_PASS','benchmark':'same CPython process; tracemalloc; gc; 5-run medians','gauge_precompute_sec':prep,'gauge_precompute_peak_bytes':prep_peak,'results':results}
if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
