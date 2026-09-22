"""Reproduce finite design, failure, search and SAME-TASK performance checks.

Execute from repository root with PYTHONPATH=src. This sparse checkout is not
Enterprise Math's full repository suite. Compile-time setup for exhaustive design
is deliberately separate from online modular observations. No unseen order input.
"""
from __future__ import annotations
import argparse, hashlib, json, platform, statistics, subprocess, sys, tempfile, time, tracemalloc
from pathlib import Path
from itertools import combinations
from math import gcd
from random import Random

from enterprise_math.group_ring_support_design import *
from enterprise_math.group_ring_support_certificates import high_band_identifiable
from enterprise_math.group_ring_sparse_identifiability import (
    period_closures, sparse_ruler, labeled_collision_gcd, ruler_order,
)
from enterprise_math.group_ring_batch_response import compile_terminal_index

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
DEPENDENCIES={
    'group_ring_sparse_identifiability.py':'35567d80b1b0f1bb864f381cc0ee7b4613d0273a',
    'group_ring_support_certificates.py':'5a2fa6a7bd8e24a190709045365312ec7d307d29',
    'group_ring_batch_response.py':'82c87f779a07b84de601d54ebd04d3bfb1856f92',
}
def check_sources():
    for f,wanted in DEPENDENCIES.items():
        data=(ROOT/'src/enterprise_math'/f).read_bytes()
        got=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        assert got==wanted,(f,got,wanted)

def band(s,H,full=False):
    D={y-x for i,x in enumerate(s) for y in s[i+1:]}
    return all(d in D for d in range(1 if full else H//3+1,H+1))

def brute_break(s,H,p):
    allowed=tuple(x for x in s if x not in p)
    for e in range(len(allowed)+1):
        for deletion in combinations(allowed,e):
            rest=tuple(x for x in s if x not in deletion)
            if not band(rest,H):return e
    return None

def brute_min(H,mode):
    for k in range(2,H+2):
        for inner in combinations(range(1,H),k-2):
            s=(0,)+inner+(H,)
            if not band(s,H,mode==1):continue
            if mode==2 and any(not band(tuple(y for y in s if y!=x),H) for x in inner):continue
            return k
    return None

def order_brute(n,a):
    r,z=1,a%n
    while z!=1:z=z*a%n;r+=1
    return r

def timing(call):
    call();times=[]
    for _ in range(7):
        t=time.perf_counter_ns();call();times.append(time.perf_counter_ns()-t)
    tracemalloc.start();call();peak=tracemalloc.get_traced_memory()[1];tracemalloc.stop()
    return {'median_ms':statistics.median(times)/1e6,'samples_ns':times,'peak_python_bytes':peak}

def validate():
    check_sources();counts={};t=time.perf_counter()
    construction=0
    for H in range(1,1001):
        s=tail_ruler(H)
        assert high_band_identifiable(s,H)
        assert len(s)<=tail_ruler_parameters(H).mark_upper_bound
        construction+=1
    counts['construction_horizons']=construction
    closures=0
    for H in range(1,151):
        assert period_closures(tail_ruler(H),H)==tuple(range(1,H+1))+(0,)
        closures+=H
    counts['inherited_period_closures']=closures
    failures=0;unprotected=0
    for H in range(1,10):
        for bits in range(1,1<<(H+1)):
            s=tuple(i for i in range(H+1) if bits>>i&1)
            options=[(),tuple(x for x in (0,H) if x in s),s[::2],s]
            for p in options:
                c=certify_mark_erasures(s,H,protected=p).certificate
                assert c.minimum_deletions==brute_break(s,H,p)
                assert verify_mark_erasure_certificate(c)
                if c.minimum_deletions is not None:
                    assert not band(tuple(x for x in s if x not in c.erased_marks),H)
                failures+=1
            if band(s,H):
                assert certify_mark_erasures(s,H).certificate.minimum_deletions==1
                unprotected+=1
    counts['exhaustive_support_protection_cases']=failures
    counts['unprotected_endpoint_checks']=unprotected
    rng=Random(16243626);reductions=0
    for H in range(1,301):
        for start in [sparse_ruler(H),tail_ruler(H)]:
            scan=list(start);rng.shuffle(scan)
            out=prune_identifying_support(start,H,order=scan)
            assert verify_support_reduction(out)
            assert all(not band(tuple(y for y in out.support if y!=x),H) for x in out.support)
            reductions+=1
    counts['verified_inclusion_minimal_reductions']=reductions
    modular=0
    for n in range(2,71):
        for a in range(1,n):
            if gcd(n,a)>1:continue
            r=order_brute(n,a)
            for H in (1,2,3,5,10,20,max(1,r-1),r,r+1,2*r):
                out=tail_ruler_order(n,a,H)
                assert out.order==(r if r<=H else None)
                modular+=1
    counts['actual_modular_horizons']=modular
    # Standalone C++ exhaustive enumerator; budgets are NOT interpreted as UNSAT.
    with tempfile.TemporaryDirectory() as td:
        executable=Path(td)/'exact_search'
        subprocess.run(['g++','-O3','-std=c++17',str(HERE/'exact_search.cpp'),'-o',str(executable)],check=True)
        raw=subprocess.check_output([str(executable),'34','100000000'],timeout=35)
        minima=json.loads(raw)
        (HERE/'exact_minima.json').write_text(json.dumps(minima,indent=2)+'\n')
        truncated=json.loads(subprocess.check_output([str(executable),'12','1']))
        assert any(row['status']=='BUDGET_EXHAUSTED' for row in truncated)
        assert all(row['minimum'] is None for row in truncated if row['status']=='BUDGET_EXHAUSTED')
    brute_matches=0
    for row in minima:
        assert row['status']=='MINIMUM_FOUND'
        H,mode,s=row['H'],row['mode'],tuple(row['support'])
        assert len(s)==row['minimum']
        assert band(s,H,mode==1)
        if mode==2:
            cert=certify_mark_erasures(s,H,protected=(0,H)).certificate
            assert cert.minimum_deletions>=2
        else:assert high_band_identifiable(s,H)
        if H<=13:
            assert brute_min(H,mode)==row['minimum'];brute_matches+=1
    counts['exhaustive_minima_records']=len(minima)
    counts['exact_search_nodes']=sum(t['nodes'] for r in minima for t in r['trials'])
    counts['independent_python_minima']=brute_matches
    suboptimal=[]
    for r in minima:
        if r['mode']==0:
            greedy=prune_identifying_support(tail_ruler(r['H']),r['H']).support
            if len(greedy)>r['minimum']:
                suboptimal.append({'H':r['H'],'greedy':list(greedy),'minimum_support':r['support']})
    # Same task and no supplied order; pow-based rows count each actual modular pow.
    costs=[]
    for n,a,H in [(100160063,2,4096),(100160063,2,65536),(65537,3,65536)]:
        def old_pow():
            return labeled_collision_gcd(n,a,sparse_ruler(H),H).gcd_multiple
        def new_pow():return tail_ruler_order(n,a,H).order or 0
        def old_block():return ruler_order(n,a,H).order or 0
        def bsgs():
            idx=compile_terminal_index(n,a,H,(1,)).index
            assert idx is not None
            return idx.order or 0
        answers=[f() for f in (old_pow,new_pow,old_block,bsgs)]
        assert len(set(answers))==1,answers
        costs.append({'n':n,'a':a,'H':H,'old_marks':len(sparse_ruler(H)),
                      'tail_marks':len(tail_ruler(H)),'answer':answers[0],
                      'old_pow':timing(old_pow),'tail_pow':timing(new_pow),
                      'old_block':timing(old_block),'bounded_bsgs':timing(bsgs)})
    return {'status':'FINITE_CHECKS_PASS_NOT_ADMITTED','python':sys.version,
            'platform':platform.platform(),'counts':counts,'unchanged_dependencies':DEPENDENCIES,
            'suboptimal_greedy_witnesses':suboptimal,'same_task_costs':costs,
            'seconds':time.perf_counter()-t,
            'cost_scope':'7 complete-call medians; construction inside; tracing separate, not RSS; no warm table',
            'excluded':'full EM suite; formal proof/admission; RSA; physical failure model; asymptotic optimality'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=HERE/'results.json')
    args=p.parse_args();result=validate();args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
