#!/usr/bin/env python3
"""End-to-end exact Python Fraction benchmark for R129 dense vs R131 quotient.
Both algorithms produce the full *set* of attained m-bit words. This is not a
controlled machine-wide benchmark or a complexity proof.
"""
from fractions import Fraction as F
from statistics import median
from time import perf_counter_ns
import json
from check_r131 import circle_log, quotient_words, direct_full_words


def timed(fn, samples=3):
    measurements=[]
    for _ in range(samples):
        start=perf_counter_ns()
        result=fn()
        measurements.append((perf_counter_ns()-start)/1_000_000)
    return median(measurements),result


def run():
    x=F(1,7); m=7; L=F(0); H=F(1)
    output=[]
    for k in (1,2,4,8,16,32,64,128):
        A,d,E=3*k,k,2*k
        dense_ms,(dense_set,dense_cuts)=timed(lambda:direct_full_words(x,A,d,E,m,L,H))
        quot_ms,(log,quot_set)=timed(lambda:(lambda v:(v,quotient_words(v,L,H)[0]))(circle_log(x,A,d,E,m)))
        assert dense_set == quot_set
        output.append({'scale':k,'dense_cuts':dense_cuts,
              'quotient_cuts':len(log['cuts']),'distinct_words':len(quot_set),
              'dense_median_ms':round(dense_ms,6),'quotient_median_ms':round(quot_ms,6),
              'ratio':round(dense_ms/quot_ms,4),'samples_each':3})
    record={'status':'R131_BENCHMARK_EXACT_WORDSET_MATCH','platform':'CPython stdlib Fraction; monotonic wall-clock; environment not thermally controlled',
        'input':'x=1/7, A=3K, d=K, E=2K, m=7, I=(0,1)',
        'dense':'R129-style complete event cut construction and independent full-word evaluation; set dedup',
        'quotient':'R131 cyclic sparse event construction plus integer-lift filtering; set dedup',
        'runs':output}
    with open('benchmark_r131.json','w') as fh: json.dump(record,fh,indent=2)
    print(json.dumps(record,indent=2))

if __name__=='__main__': run()
