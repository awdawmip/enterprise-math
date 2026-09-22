"""Reproduce bounded exact checks and cost accounting, without order inputs."""
from __future__ import annotations
import argparse
from collections import defaultdict
from itertools import combinations, product
from math import gcd
from pathlib import Path
import hashlib
import json
import platform
import random
import statistics
import time
import tracemalloc

from enterprise_math.group_ring_sparse_identifiability import (
    sparse_ruler, difference_set, period_closures, structural_alias,
    collision_spectrum, compile_sparse_codebook, verify_codebook,
    collision_readouts, labeled_collision_gcd, ruler_order,
)
from enterprise_math.group_ring_batch_response import compile_terminal_index


def brute_mass(s,w,r):
    buckets=defaultdict(int)
    for x,weight in zip(s,w):buckets[x%r]+=weight
    return sum(x*x for x in buckets.values())


def brute_order(n,a):
    u=1
    for r in range(1,n+1):
        u=u*a%n
        if u==1:return r
    raise AssertionError('invalid unit')


def med_ms(f):
    f()
    values=[]
    for _ in range(7):
        t=time.perf_counter_ns();f();values.append((time.perf_counter_ns()-t)/1e6)
    return statistics.median(values)


def peak(f):
    tracemalloc.start();f();value=tracemalloc.get_traced_memory()[1];tracemalloc.stop()
    return value


def validate():
    root=Path(__file__).resolve().parents[2]
    deps={'src/enterprise_math/group_ring_affine_character.py':'61adb8c7ed2d610dbd924871e35c3e315c927c06',
          'src/enterprise_math/group_ring_batch_response.py':'82c87f779a07b84de601d54ebd04d3bfb1856f92'}
    for path,expected in deps.items():
        data=(root/path).read_bytes()
        got=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        assert got==expected,(path,got)
    counts=defaultdict(int);rng=random.Random(20260922)
    for H in range(1,11):
        for mask in range(1,1<<(H+1)):
            s=tuple(x for x in range(H+1) if mask>>x&1)
            D=difference_set(s,H);closures=period_closures(s,H)
            signatures=tuple(tuple(sorted(d for d in D if d%r==0)) for r in range(1,H+2))
            counts['support_configurations']+=1
            for i,j in combinations(range(H+1),2):
                assert (closures[i]==closures[j])==(signatures[i]==signatures[j])
                counts['closure_signature_pair_checks']+=1
            for r,c in enumerate(closures[:-1],1):
                if c:
                    assert c%r==0 and closures[c-1]==c
                for s2 in range(r,H+1,r):
                    if c:assert closures[s2-1]%c==0
            w=tuple(rng.randrange(1,30) for _ in s)
            spec=collision_spectrum(s,w,H)
            for r in range(1,H+2):
                assert spec[r-1]==brute_mass(s,w,r)
                counts['independent_weighted_period_masses']+=1
    for H in range(1,129):
        support=sparse_ruler(H)
        assert difference_set(support,H)==frozenset(range(1,H+1))
        for alphabet in ('large','binary'):
            comp=compile_sparse_codebook(H,alphabet=alphabet)
            assert comp.status=='COMPLETE'
            book=comp.codebook;assert verify_codebook(book)
            counts['compiled_codebooks']+=1
            for r,code in enumerate(book.codes,1):
                assert code==tuple(brute_mass(support,w,r) for w in book.profiles)
                assert book.decode(code).order==(r if r<=H else None)
                counts['codebook_period_roundtrips']+=1
    horizons=(4,9,16,32,64)
    books={H:compile_sparse_codebook(H).codebook for H in horizons}
    for n in range(3,151):
        for a in range(1,n):
            if gcd(a,n)!=1:continue
            r=brute_order(n,a)
            for H in horizons:
                wanted=r if r<=H else None
                book=books[H]
                obs=book.observe(n,a)
                assert obs==book.codes[min(r,H+1)-1]
                assert book.decode(obs).order==wanted
                assert ruler_order(n,a,H).order==wanted
                classical=compile_terminal_index(n,a,H,(1,))
                assert classical.status=='COMPLETE' and classical.index.order==wanted
                counts['modular_group_horizon_checks']+=1
    probability=[]
    for s,H in [((0,1,2,4),4),((0,1,5,7,9),9),((0,4,5,6),6)]:
        closures=period_closures(s,H)
        grid=tuple(collision_spectrum(s,w,H) for w in product((1,2),repeat=len(s)))
        worst=0
        for i,j in combinations(range(H+1),2):
            equal=sum(row[i]==row[j] for row in grid)
            if closures[i]==closures[j]:assert equal==len(grid)
            else:
                assert 4*equal<=3*len(grid)
                worst=max(worst,equal)
                counts['binary_grid_distinct_pair_checks']+=1
        probability.append({'support':s,'H':H,'grid_size':len(grid),'worst_alias_count':worst})
    bench=[]
    for n,a,H in [(10007,5,4096),(10007,5,16384),(65537,3,65536),(100160063,2,65536)]:
        book=compile_sparse_codebook(H).codebook
        def cold():
            b=compile_sparse_codebook(H).codebook
            return b.decode(b.observe(n,a)).order
        def warm():return book.decode(book.observe(n,a)).order
        def direct():return ruler_order(n,a,H).order
        def classical():return compile_terminal_index(n,a,H,(1,)).index.order
        assert cold()==warm()==direct()==classical()
        times={name:med_ms(f) for name,f in [('cold_codebook',cold),('warm_codebook',warm),
                ('labeled_ruler_gcd',direct),('unchanged_bounded_bsgs',classical)]}
        allocations={name:peak(f) for name,f in [('cold_codebook',cold),('warm_codebook',warm),
                ('labeled_ruler_gcd',direct),('unchanged_bounded_bsgs',classical)]}
        bench.append({'n':n,'a':a,'horizon':H,'support_marks':len(book.support),
            'decoder_entries':len(book.codes),'result_order_or_none':warm(),
            'max_weight_bits':max(w.bit_length() for w in book.profiles[0]),
            'max_mass_bits':max(code[0].bit_length() for code in book.codes),
            'median7_ms':times,'peak_python_bytes':allocations})
    binary=compile_sparse_codebook(4096,alphabet='binary').codebook
    return {'status':'RESEARCH_CANDIDATE_NOT_ADMITTED','environment':{'python':platform.python_version(),
            'platform':platform.platform()},'counts':dict(counts),'binary_grid_checks':probability,
            'binary_4096':{'marks':len(binary.support),'channels':len(binary.profiles),
                'max_weight':2,'decoder_entries':len(binary.codes),
                'max_mass_bits':max(v.bit_length() for code in binary.codes for v in code)},
            'example_h6':{'support':[0,1,2,3,6],'bad_weights':[1,2,3,4,7],
                'bad_mass_orders_2_3':157,'good_profile':compile_sparse_codebook(6).codebook.profiles[0],
                'good_codes':compile_sparse_codebook(6).codebook.codes},'benchmarks':bench,
            'cost_scope':'Cold includes compilation and observation; warm reuses an explicitly charged O(H) decoder. Seven full calls after warmup; tracing separate, not RSS. Direct gcd and classical BSGS compute bounded order, not the weighted scalar. No order input or modulus factorization.',
            'unchanged_dependencies':deps}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,default=Path(__file__).with_name('results.json'))
    args=parser.parse_args();result=validate()
    args.out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2))
