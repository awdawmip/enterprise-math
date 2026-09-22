"""Reproduce exact observer tests and same-output cost comparisons (no network)."""
from __future__ import annotations
import hashlib, json, platform, random, statistics, sys, time, tracemalloc
from collections import defaultdict
from itertools import combinations_with_replacement
from math import gcd
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'src'))
from enterprise_math.group_ring_affine_character import (
    affine_correlation, affine_collision_from_order, affine_index_responses,
    compile_character_index, invert_affine_collision, jacobi_symbol)
from enterprise_math.group_ring_batch_response import compile_terminal_index


def blob(path):
    b=path.read_bytes()
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()


def hist(n,a,L,A=1,B=0):
    h=defaultdict(int);v=1
    for x in range(L):
        h[v]+=A+B*x;v=v*a%n
    return dict(h)


def observe(h,n,states):
    return tuple(sum(m*h.get(u*v%n,0) for v,m in h.items()) for u in states)


def brute_order(n,a):
    v=1
    for r in range(1,n+1):
        v=v*a%n
        if v==1:return r
    raise AssertionError('order bound failed')


def exact_checks():
    cases=windows=observers=inversions=cuts=0
    stats={'PARITY_PROGRESSION':0,'CHARACTER_ZERO_EXCLUSION':0,'EVEN_MODULUS':0,'NO_UNIT_TARGETS':0}
    for n in range(3,101):
        units=[a for a in range(1,n) if gcd(a,n)==1]
        selected=units[:4]
        if n%2:
            neg=next((a for a in units if jacobi_symbol(a,n)==-1),None)
            if neg is not None and neg not in selected:selected.append(neg)
        for a in selected:
            states=tuple(range(n))
            r=brute_order(n,a)
            for span in (1,3,8,17,32,65):
                f=compile_character_index(n,a,span,states)
                baseline=compile_terminal_index(n,a,span,states)
                assert f.status=='COMPLETE' and baseline.status=='COMPLETE'
                if f.index.order is not None:assert f.index.order==r
                stats[f.mode]+=1;cases+=1
                for L in {1,span,max(1,span//2)}:
                    for A,B in ((1,0),(1,1),(3,4)):
                        expected=observe(hist(n,a,L,A,B),n,states)
                        got=affine_index_responses(f.index,L,states,A,B)
                        assert got==expected
                        assert affine_index_responses(baseline.index,L,states,A,B)==expected
                        assert got[1]==affine_collision_from_order(L,r,A,B)
                        inv=invert_affine_collision(got[1],L,A,B)
                        assert inv.order==r if r<L else inv.order is None
                        inversions+=1;windows+=1;observers+=len(states)
                m=span.bit_length()-1
                output=f.index.cuts(m,range(m+1),states)
                for j,row in enumerate(output):
                    L=1<<(m-j);a2=pow(a,1<<j,n)
                    assert row==observe(hist(n,a2,L),n,states)
                    cuts+=len(states)
    profiles=0
    for L in range(1,11):
        for w in combinations_with_replacement(range(1,5),L):
            c=[sum(w[x]*w[x+d] for x in range(L-d)) for d in range(L)]+[0]
            ks=[c[0]+2*sum(c[d] for d in range(r,L,r)) for r in range(1,L+1)]
            assert all(x>y for x,y in zip(ks,ks[1:]))
            profiles+=1
    return dict(compilation_cases=cases,window_weight_profiles=windows,
                independently_counted_observers=observers,inversions=inversions,
                independently_counted_dyadic_cut_observers=cuts,
                monotone_positive_profiles=profiles,modes=stats)


def benchmark(n,a,L,states,A=3,B=2):
    def direct():return observe(hist(n,a,L,A,B),n,states)
    def plain():
        c=compile_terminal_index(n,a,L,states)
        assert c.index is not None
        return affine_index_responses(c.index,L,states,A,B)
    def filtered():
        c=compile_character_index(n,a,L,states)
        assert c.index is not None
        return affine_index_responses(c.index,L,states,A,B)
    def measure(fn):
        answer=fn()
        times=[]
        for _ in range(7):
            start=time.perf_counter_ns();value=fn();times.append(time.perf_counter_ns()-start)
            assert value==answer
        tracemalloc.start();fn();_,peak=tracemalloc.get_traced_memory();tracemalloc.stop()
        return answer,dict(median_ms=statistics.median(times)/1e6,peak_python_allocated_bytes=peak)
    answers=[];measurements={}
    for name,fn in [('direct_weighted_occupancy',direct),('unfiltered_bounded_bsgs',plain),('jacobi_filtered_bounded_bsgs',filtered)]:
        answer,measurements[name]=measure(fn);answers.append(answer)
    assert answers[0]==answers[1]==answers[2]
    p=compile_terminal_index(n,a,L,states);f=compile_character_index(n,a,L,states)
    return dict(n=n,a=a,length=L,states=list(states),intercept=A,slope=B,
                mode=f.mode,chi_base=jacobi_symbol(a,n) if n%2 else None,
                unfiltered_scans=p.executed_scans,filtered_scans=f.executed_scans,
                unfiltered_table=p.table_entries,filtered_table=f.table_entries,
                character_evaluations=f.character_evaluations,
                rejected_states=list(f.rejected_states),measurements=measurements,
                result_digest=hashlib.sha256(repr(answers[0]).encode()).hexdigest())


def main():
    dependencies={
        'group_ring_batch_response.py':'82c87f779a07b84de601d54ebd04d3bfb1856f92',
        'group_ring_terminal_response.py':'354633331b05f8c7f275e852ae04df85aad63004'}
    for p,expected in dependencies.items():assert blob(ROOT/'src/enterprise_math'/p)==expected
    results={'status':'RESEARCH_CANDIDATE_NOT_ADMITTED','environment':{'python':sys.version,'platform':platform.platform()},
             'timing_scope':'7 full-call medians after warmup; compile/query included; inputs preselected equally; tracemalloc separate, not RSS; no supplied order/log',
             'dependencies':dependencies,'checks':exact_checks()}
    print(json.dumps(results['checks']),flush=True)
    configs=[(100160063,5,262144,(1,)),(65537,3,65536,(1,)),
             (100160063,5,16384,tuple(pow(5,i*731,100160063) for i in range(16))),
             (10007,25,16384,tuple(range(1,33))),
             (100160063,2,32768,(1,)),(65537,3,131072,(1,))]
    results['benchmarks']=[]
    for cfg in configs:
        b=benchmark(*cfg);results['benchmarks'].append(b)
        print(cfg[:3],b['mode'],b['unfiltered_scans'],b['filtered_scans'],
              {name:round(m['median_ms'],4) for name,m in b['measurements'].items()},flush=True)
    out=Path(__file__).with_name('results.json')
    out.write_text(json.dumps(results,indent=2)+'\n')
    print(out)

if __name__=='__main__':main()
