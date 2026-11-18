"""Sparse butterfly cost, geometric collisions, and order-sensitive memo keys.

Default uses only Python's standard library. --source ROOT additionally runs
the pinned SE/MeterRing on its original fixed-window file and compares every
coefficient to an independent integer implementation. --cost saves optional
machine-dependent timings (scientific stdout is deterministic).
"""
import argparse
import hashlib
import itertools
import json
import platform
import random
import statistics
import tempfile
import sys
import time
from collections import Counter
from pathlib import Path

FIVE = ('copied_terms', 'coefficient_visits', 'shifted_terms',
        'merge_row_visits', 'transform_row_visits')
PINS = {
    'FIXED_WINDOW_CONTEXT.json': 'c182293428506f7ca927f10b791a42a77f47ad34e9031f0b5a1f7c4fe7e482a9',
    'test_hierarchy.py': '6046f656e74fb67852bf441d4961e8c23de21f258e30691a4d0d812f38bab623',
    'test_blocks.py': '1dcf4ee3802b8a9fe2cce3969b265b00186f8eb33c38dd6077b5b9f02c91c8cb',
    'shor_exact.py': '1e89417ec27bbb209130aadd818dd98ac62a2ff1d8e17a4dfae2447f5cf21ad4',
    'test_mod7_only.py': 'b0fa9b4f9b96480d5cf409f15d5f7f07afc993b6ca57b74bce7811e93adb93c7',
    'wave_compare.py': 'fd2f6f73d3d0af1df9b4a2bf771b8574c06d03e9df5bd33310394967f5d2cfd2',
    'brc_weighted_recurrent.py': '7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26',
    'brc_division_excerpt.py': 'db9a41d7087e6e042f5330d39815dedd504a49fcb2db30048f0e3f55b8472bb4',
    'division.py': '4421c6dc9acfaa61492137951e543973c010c6a127655126152cc18763cc35e9',
}
NAMES = ['layer6_plus', 'layer6_minus', 'layer7_129_plus', 'layer7_129_minus',
         'layer7_161_plus', 'layer7_161_minus']


def dump(obj):
    return (json.dumps(obj, sort_keys=True, indent=2) + '\n').encode()


def rotate(a, k, n):
    return {(j+k) % n: v * (-1)**((j+k)//n) for j, v in a.items()}


def ref_butterfly(a, b, k, n):
    t = rotate(b, k, n)
    return [{j: v for j in a.keys() | t.keys() if (v := a.get(j,0) + s*t.get(j,0))}
            for s in (1, -1)]


def measure(c, d):
    return [96+2*(int(c != 0)+int(c != d)+int(c != -d)),
            100+2*(d != 0), 50+(d != 0), 0, 0]


def scalar_query(c, d):
    if not d:
        return 252 if c else 246
    if not c:
        return 253
    return 253 if abs(c) == abs(d) else 255


def lengths(c, d):
    return [(10+bool(c), 9+bool(d)), (19+(c != d), 21), (19+(c != -d), 20)]


def plan_cost(c, d, mask):
    v=measure(c,d)
    for i,(left,right) in enumerate(lengths(c,d)):
        if mask & (1 << i):
            v[0] += right-left
            v[1] += left-right
    return v


def generic_check():
    # Independent direct signed dense/sparse calculation and complete offset sweep.
    vectors = [{i:x for i,x in enumerate(v) if x}
               for v in itertools.product((-1,0,1,2), repeat=3)]
    n=3
    checks=0
    for p,q in itertools.product(vectors, repeat=2):
        l,r=len(p),len(q)
        sum_i=sum_j=0
        for k in range(2*n):
            shifted=rotate(q,k,n)
            inter=p.keys() & shifted.keys()
            i=len(inter)
            j=sum(abs(p[x])==abs(shifted[x]) for x in inter)
            plus,minus=ref_butterfly(p,q,k,n)
            assert len(plus)+len(minus)==2*(l+r-i)-j
            rev=ref_butterfly(p,q,(k+n)%(2*n),n)
            assert [plus,minus]==rev[::-1]
            sum_i+=i
            sum_j+=j
            checks+=1
        assert sum_i==2*l*r
        assert sum_j==2*sum(abs(v)==abs(w) for v in p.values() for w in q.values())
    return checks


def portable():
    n=8
    old={(-2,1),(-1,1),(0,1),(1,1),(2,1)}
    ids=Counter()
    for c,d in itertools.product(range(-n,n+1),repeat=2):
        f=measure(c,d)
        assert scalar_query(c,d)==sum(f)
        ids[sum(f)]+=1
        options=[plan_cost(c,d,k) for k in range(8)]
        assert all(sum(v)==sum(f) for v in options)
        assert options[1][0]==min(v[0] for v in options)
        assert options[6][1]==min(v[1] for v in options)
    assert ids=={246:1,252:2*n,253:6*n,255:4*n*(n-1)}
    mixed=list(itertools.product(range(1,9),repeat=2))
    # Gap memo uses a distinct op and sorts its arguments.
    canonical={(min(a,b),max(a,b)) for a,b in mixed}
    assert len(canonical)==36 and len(set(mixed))==64
    return dict(box_halfwidth=n,box_histogram=dict(sorted(ids.items())),
                generic_offset_checks=generic_check(),new_box_inputs=(2*n+1)**2-len(old),
                all_orientations_per_point=8, never_replayed_old_source_inputs=sorted(old),
                counts_ordered_stream_1_to_8=dict(windows=64,distinct_ordered=64,
                 distinct_unordered=36, gap_keys=36, saved_parent_brc_sum=28),
                signed_ring='Z[u]/(u^256+1)', source_pins=PINS)


def operands(context,c,d):
    p,q=dict(context['p']),dict(context['q'])
    for poly,index,coeff in ((p,0,c),(q,248,d)):
        if coeff:
            poly[index]=coeff
        else:
            poly.pop(index,None)
    return p,q


def reference(p,q,branches):
    left,right=ref_butterfly(p,q,8,256)
    return [left,right]+sum((ref_butterfly(poly,partner,k,256)
                              for poly,(partner,k) in zip((left,right),branches)),[])


def source_window(r,p,q,branches,mask):
    def one(p,q,k,bit):
        t=r.shift(q,k)
        positive=r.add(t,p) if mask & bit else r.add(p,t)
        return [positive,r.add(p,t,-1)]
    first=one(p,q,8,1)
    return first + one(first[0],*branches[0],2) + one(first[1],*branches[1],4)


def provenance(root):
    tree=root/'shor_blocks_S3'
    for name,digest in PINS.items():
        path=root/name if name=='FIXED_WINDOW_CONTEXT.json' else next(tree.rglob(name))
        assert hashlib.sha256(path.read_bytes()).hexdigest()==digest, path
    sys.path.insert(0,str(tree))
    from test_hierarchy import BRC, MeterRing
    return BRC, MeterRing, json.loads((root/'FIXED_WINDOW_CONTEXT.json').read_bytes())


def precompile(context):
    assert context['origin_twiddle']==8 and [b['twiddle'] for b in context['downstream']]==[4,132]
    p,q=operands(context,0,0)
    branches=[(dict(node['q']),node['twiddle']) for node in context['downstream']]
    shifted=rotate(q,8,256)
    base_left=p.keys()|shifted.keys()
    assert not p.keys() & shifted.keys() and len(base_left)==19
    assert rotate({248:1},8,256)=={0:-1}
    for b,k in branches:
        right=rotate(b,k,256)
        assert not (base_left|{0}) & right.keys()
    assert [len(p),len(q)]+[len(z) for z,_ in branches]==[10,9,21,20]
    return branches


def totals(counter,stage):
    return {k.split(':',1)[1]:int(v) for k,v in counter.items() if k.startswith(stage+':')}


def source_audit(root,cost_target):
    ns=time.perf_counter_ns
    start=ns()
    BRC,MeterRing,context=provenance(root)
    charged={'source_read_hash_import_ns':ns()-start}
    start=ns()
    branches=precompile(context)
    charged['four_supports_precompile_ns']=ns()-start
    start=ns()
    a=BRC();a.stage='setup';r=MeterRing(512,a)
    charged['first_ring_setup_ns']=ns()-start
    old={(-2,1),(-1,1),(0,1),(1,1),(2,1)}
    # Frozen d=1 was already certified. Audit only the 284 other inputs.
    checks=Counter()
    start=ns()
    for c,d in itertools.product(range(-8,9),repeat=2):
        if (c,d) in old: continue
        p,q=operands(context,c,d)
        wanted=reference(p,q,branches)
        for mask in range(8):
            a.stage='window'
            # Reuse the address-only ring calibration; isolate the scientific memo.
            a.cache={};a.requests.clear();a.hits.clear();a.core.counts.clear()
            a.core.entries.clear();a.core.max_bits.clear();r.metrics.clear()
            obtained=source_window(r,p,q,branches,mask)
            assert obtained==wanted
            metric=[r.metrics.get(name,0) for name in FIVE]
            assert metric==plan_cost(c,d,mask)
            n=totals(a.core.counts,'window')
            if c and d:
                assert n.get('verified_gap',0)==1 and n.get('brc_sum',0)==1+(abs(c)!=abs(d))
                assert n.get('zero_route',0)==(abs(c)==abs(d))
                assert a.core.max_bits['window']==(abs(c)+abs(d)).bit_length()
            else:
                assert n=={}
            for v in obtained:
                assert all(v.values())
            checks['source_windows']+=1;checks['full_output_comparisons']+=6
            checks['scientific_FIVE']+=sum(metric)
    charged['source_box_all_8_with_independent_check_ns']=ns()-start
    order=list(itertools.product(range(1,9),repeat=2))
    material={}
    for c,v in order:
        p,q=operands(context,c,-v)
        material[(c,v)]=(p,q)
    # Cost separately: both key retrievals and the single comparison are in
    # the selected policy's timed loop. Reference comparisons live outside.
    expected={cv:reference(*args,branches) for cv,args in material.items()}
    def stream(seq,method):
        a=BRC();a.stage='setup'
        start=ns();r=MeterRing(512,a);setup=ns()-start
        a.stage='run'
        start=ns()
        outputs=[]
        for cv in seq:
            p,q=material[cv]
            mask=int(p[0]>-q[248]) if method=='ordered' else 0
            outputs.append(source_window(r,p,q,branches,mask))
        elapsed=ns()-start
        counts=totals(a.core.counts,'run')
        assert outputs==[expected[k] for k in seq]
        assert totals(a.requests,'run')=={'add':64,'gap':64}
        keys=64 if method=='direct' else 36
        assert len([k for k in a.cache if k[0]=='add'])==keys
        assert totals(a.hits,'run').get('add',0)==64-keys
        assert counts=={'brc_sum':keys+28,'verified_gap':36,'zero_route':8}
        assert sum(r.metrics[k] for k in FIVE)==sum(sum(measure(c,-v)) for c,v in seq)
        return elapsed,setup,counts,dict(r.metrics),a.core.max_bits['run']
    bench=[]
    for i in range(9):
        seq=order[:];random.Random(9493+i).shuffle(seq)
        methods=['direct','ordered'];random.Random(23+i).shuffle(methods)
        row={'seed':9493+i,'execution_order':methods}
        for m in methods:
            val,setup,counts,metrics,bits=stream(seq,m)
            row[m]={'execute_ns':val,'ring_setup_ns':setup,'actual_core':counts,
                    'metrics':metrics,'max_scientific_integer_bits':bits}
        bench.append(row)
    # Metadata-only prices. Input polynomials already materialized.
    trials=128
    start=ns()
    buffer=[(p.get(0,0),q.get(248,0)) for _ in range(trials) for p,q in material.values()]
    charged['coefficient_get_pairs_8192_ns']=ns()-start
    start=ns()
    answers=[scalar_query(c,d) for c,d in buffer]
    charged['classified_8192_known_pairs_ns']=ns()-start
    assert set(answers)=={253,255}
    start=ns()
    payload=dump(expected[(1,2)])
    charged['one_six_output_json_encode_ns']=ns()-start
    charged['one_six_output_json_bytes']=len(payload)
    start=ns()
    with tempfile.TemporaryFile() as f:
        assert f.write(payload)==len(payload)
        f.flush()  # OS-buffered write; storage durability is not measured.
    charged['one_six_output_buffered_tempfile_ns']=ns()-start
    start=ns()
    swaps=[p[0]>-q[248] for _ in range(trials) for p,q in material.values()]
    charged['online_swap_decisions_including_two_fetches_8192_ns']=ns()-start
    assert sum(swaps)==28*trials
    stale=json.loads(json.dumps(context))
    stale['downstream'][0]['q'][0][0]=252  # after shift by 4: exponent 0
    try:
        precompile(stale)
    except AssertionError:
        pass
    else:
        raise AssertionError('new downstream overlap must invalidate the compiled proof')
    # Rebuilding the valid structural signature after explicit invalidation.
    start=ns()
    again=precompile(context)
    charged['first_recompile_on_explicit_invalidation_ns']=ns()-start
    assert again==branches
    if cost_target:
        obj=dict(python=platform.python_version(),platform=platform.platform(),
                 processor=platform.machine(),measurement='one machine, perf_counter_ns, no cache assumption across repetitions',
                 charged=charged, source_new_windows=dict(checks), samples=bench,
                 median_execute_ns={m:statistics.median(x[m]['execute_ns'] for x in bench)
                                    for m in ('direct','ordered')})
        cost_target.write_bytes(dump(obj))
    return dict(checks)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path)
    parser.add_argument('--cost',type=Path)
    args=parser.parse_args()
    if args.cost and not args.source:
        parser.error('--cost needs --source')
    result=portable()
    if args.source:
        counts=source_audit(args.source,args.cost)
        assert counts['source_windows']==8*result['new_box_inputs']
        assert counts['full_output_comparisons']==6*counts['source_windows']
    sys.stdout.buffer.write(dump(result))
