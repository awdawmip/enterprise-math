"""Deterministic checks and matched single-host costs. PYTHONPATH=src required."""
import argparse
from collections import Counter
import gc
import hashlib
import importlib.util
import json
from math import gcd, isqrt
from pathlib import Path
import platform
import statistics
import sys
import time
import tracemalloc
from enterprise_math.group_ring_terminal_response import (
    terminal_responses, cyclic_terminal_value, terminal_class_count,
    collision_order_search, invert_collision_mass,
)
from enterprise_math.group_ring_inverse_quotient import inverse_collision_mass


def blob(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()


def load_power(path):
    assert blob(path.read_bytes())=='11d4adf3ff6e56c440cfdd7974be6c28f8ff068a'
    spec=importlib.util.spec_from_file_location('power_reference',path)
    mod=importlib.util.module_from_spec(spec); sys.modules[spec.name]=mod
    spec.loader.exec_module(mod)
    return mod.compute_group_ring_collision_mass


def bounded_bsgs_order(n,a,bound):
    """Classical reference: smallest positive exponent <=bound with a**exponent=1.

    Never given the true order. Baby powers are unique unless they close the
    cycle; that first closure itself gives the exact order. Otherwise giant
    blocks are scanned in increasing exponent order, and a first match is minimal.
    This reference is not copied from Sage; Sage documents the classical method.
    """
    width=isqrt(bound)+1; table={}; p=1
    for j in range(width):
        if j and p==1: return j
        table[p]=j; p=p*a % n
    step=pow(p,-1,n); v=1
    for i in range(bound//width+1):
        j=table.get(v)
        if j is not None and 0<i*width+j<=bound: return i*width+j
        v=v*step % n
    return None


def adaptive_bsgs_order(n,a):
    for bits in range(1,n.bit_length()+1):
        r=bounded_bsgs_order(n,a,(1 << bits)-1)
        if r is not None: return r
    raise ArithmeticError('unit order bound violated')


def median(fn):
    samples=[]
    for _ in range(5):
        gc.collect(); start=time.perf_counter_ns(); fn()
        samples.append((time.perf_counter_ns()-start)/1e6)
    return statistics.median(samples)


def peak(fn):
    gc.collect(); tracemalloc.start(); fn(); _,out=tracemalloc.get_traced_memory()
    tracemalloc.stop(); return out


def measured(fn):
    return {'median_ms':median(fn),'peak_traced_bytes':peak(fn)}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--power-source',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args(); original=load_power(args.power_source)
    reference_cases=window_cases=pair_observers=0
    for n in range(3,201):
        for a in [x for x in range(2,n) if gcd(x,n)==1][:3]:
            r,k,_=original(n,a)
            new=collision_order_search(n,a)
            assert new.status=='COMPLETE' and new.order==r
            assert adaptive_bsgs_order(n,a)==r
            default_bits=max(4,(n*n-1).bit_length())
            assert terminal_responses(n,a,1 << default_bits).values==(k,)
            reference_cases+=1
            for m in range(11):
                _,mass,_=original(n,a,m)
                assert terminal_responses(n,a,1 << m).values==(mass,)
                window_cases+=1
    # Independent occupancy/autocorrelation definition, not triangular recurrence.
    for n in range(3,71):
        for b in [x for x in range(1,n) if gcd(x,n)==1][:3]:
            for length in range(1,26):
                occupancy=Counter(pow(b,x,n) for x in range(length))
                states=tuple(range(n))
                expected=tuple(sum(c*occupancy.get(u*v % n,0) for v,c in occupancy.items())
                               if gcd(u,n)==1 else 0 for u in states)
                assert terminal_responses(n,b,length,states).values==expected
                pair_observers+=n
    # Larger formula/inversion domain checked independently through first moments.
    class_checks=inverse_checks=0
    for r in range(1,151):
        for L in range(1,201):
            values=[cyclic_terminal_value(r,L,j) for j in range(r)]
            assert sum(values)==L*L
            assert len(set(values))==terminal_class_count(r,L)
            class_checks+=1
            assert invert_collision_mass(L,values[0])==(r if r<L else None)
            inverse_checks+=1
    benches=[]
    for n,a in [(1009,11),(10007,5),(65537,3),(10403,2)]:
        search=collision_order_search(n,a); assert search.status=='COMPLETE'
        r=search.order; L=search.history[-1][0]; m=L.bit_length()-1
        terminal=terminal_responses(n,a,L)
        old=inverse_collision_mass(n,a,m,max_states=100_000)
        ref=original(n,a,m)
        assert old.status=='COMPLETE' and old.collision_mass==terminal.values[0]==ref[1]
        assert adaptive_bsgs_order(n,a)==r
        # all fixed-window variants compute precisely K_L, no order pre-supplied
        full=lambda: original(n,a,m)
        orbit=lambda: inverse_collision_mass(n,a,m,max_states=100_000)
        term=lambda: terminal_responses(n,a,L)
        new_order=lambda: collision_order_search(n,a)
        classical=lambda: adaptive_bsgs_order(n,a)
        benches.append(dict(n=n,a=a,order=r,window=L,collision_mass=terminal.values[0],
            full_states=ref[2],inverse_states=old.orbit_states_by_depth[-1],
            moment_table_entries=terminal.table_entries,baby_width=terminal.baby_width,
            terminal_scans=terminal.executed_scan_steps,adaptive_mass_scans=search.scans,
            full_fixed_window=measured(full),inverse_fixed_window=measured(orbit),
            terminal_fixed_window=measured(term),adaptive_mass_order=measured(new_order),
            classical_adaptive_bsgs_order=measured(classical)))
    n,a=100160063,2
    large=collision_order_search(n,a); reference=adaptive_bsgs_order(n,a)
    assert large.status=='COMPLETE' and large.order==reference
    bigger=dict(n=n,a=a,order=reference,last_window=large.history[-1][0],
                max_table_entries=max(row[3] for row in large.history),scans=large.scans,
                adaptive_mass_order=measured(lambda:collision_order_search(n,a)),
                classical_adaptive_bsgs_order=measured(lambda:adaptive_bsgs_order(n,a)),
                full_state_baseline='NOT_RUN_AT_THIS_SIZE')
    out=dict(python=sys.version,platform=platform.platform(),
             reference_default_cases=reference_cases,explicit_window_cases=window_cases,
             independent_pair_observers=pair_observers,terminal_class_checks=class_checks,
             inversion_checks=inverse_checks,benchmarks=benches,larger_order_case=bigger,
             limitations=['one host; 5 timings, median; tracing measured separately',
                          'Python allocations, not process RSS',
                          'no generic speed claim over classical BSGS',
                          'no RSA-270, independent review, Lean, or full repository tests'])
    args.out.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))


if __name__=='__main__': main()
