"""Exact arithmetic for address-dependent scaling of the native single-walker row."""
import argparse
from collections import defaultdict
from fractions import Fraction as F
import gzip
import hashlib
from itertools import combinations, product
import json
from math import comb
import os
from pathlib import Path
import sys


def bit(x, y):
    if not x and not y:
        return F(1, 2)
    return F((x+y)**2, 2*(x*x+y*y))


def levels(d, t):
    k, r = divmod(2**t, d)
    return [k + int(i < r) for i in range(d)]


def phases(d):
    x, result = 1, []
    while min(x, d-x) not in result:
        result.append(min(x, d-x))
        x = 2*x % d
    assert x in (1, d-1)
    return result


def all_signs(d, t):
    raw = levels(d, t)
    order = [(i*pow(2, -1, d)) % d for i in range(d)]
    edge = [(order[i], order[(i+1) % d]) for i in range(d)]
    unequal = [i for i,(x,y) in enumerate(edge) if raw[x] != raw[y]]
    k, r = divmod(2**t, d)
    j = min(r, d-r)
    assert len(unequal) == 2*j and k
    reference = [bit(raw[x],raw[y]) for x,y in edge]
    distinct = set()
    for up in combinations(unequal, j):
        signs = set(up)
        h = 0
        exponents = []
        for i in range(d):
            exponents.append(h)
            if i in unequal:
                h += (1 if i in signs else -1)
        assert h == 0
        row = [F(k+1,k)**v for v in exponents]
        assert [bit(row[i],row[(i+1)%d]) for i in range(d)] == reference
        distinct.add(tuple(exponents))
    assert len(distinct) == comb(2*j,j)
    return [d,t,r,j,len(distinct)]


def support(d, t):
    raw = levels(d, t)
    assert 2**t < d
    shift = pow(2,-1,d)
    positive = set(i for i,x in enumerate(raw) if x)
    edges = [(i,(i+shift)%d) for i in positive if (i+shift)%d in positive]
    remaining = set(positive)
    components = 0
    while remaining:
        stack = [remaining.pop()]
        components += 1
        while stack:
            i = stack.pop()
            neighbors = {(i+shift)%d,(i-shift)%d} & remaining
            stack.extend(neighbors)
            remaining.difference_update(neighbors)
    Q = 2**t
    assert len(edges) == max(0,2*Q-d)
    assert components == min(Q,d-Q)
    return components


def portable():
    sparse = [support(d,t) for d in range(3,66,2) for t in range(d.bit_length())
              if 2**t<d]
    dense = [all_signs(d,t) for d in (3,5,7,9,11,13)
             for t in range(d.bit_length(),d.bit_length()+3)]
    for d in range(3,200,2):
        phase = phases(d)
        assert len(phase) == len(set(phase))
        for s in range(len(phase)):
            r = pow(2, s+2*len(phase), d)
            assert min(r,d-r) == phase[s]
    cases = 0
    for k in range(1,12):
        for a,b in product(range(-12,13),repeat=2):
            lo, hi = a+b*k, a+b*(k+1)
            if min(lo,hi) <= 0:
                continue
            assert (bit(lo,hi)==bit(k,k+1)) == (a==0 or a==-b*(2*k+1))
            cases += 1
    # A second, direct enumeration of all possible bounded height walks with no balance assumption.
    d, t = 5, 3
    base = levels(d,t)
    shift = pow(2,-1,d)
    gauges = {h for h in product(range(-2,3),repeat=d-1)
              if all(abs(((0,)+h)[i]-((0,)+h)[(i+shift)%d])
                     ==abs(base[i]-base[(i+shift)%d]) for i in range(d))}
    assert len(gauges)==6
    return dict(sparse_instances=len(sparse), sparse_components_total=sum(sparse),
                dense_columns=['d','t','r','j','count'],dense_rows=dense,
                direct_anchored_heights_d5=sorted(gauges),
                phase_cases=99,affine_positive_checks=cases,
                large_s_examples=[[s,2**s-1,2*s-1,2**(s-1)-1,
                                   comb(2**s-2,2**(s-1)-1)] for s in range(3,8)])


def load_native(repo, stage):
    rec = repo/'research_notes/directed_recovery'
    pack = rec/'20260926_C6438C'
    prev = rec/'20260926_0C08F0'
    walker = rec/'20260927_C6438C/qft_row_queries/gram_research'
    pins = {
        walker/'single_walker.py':'19ec66c4453d8ca5168d0f8fe7950ff85b297562e8625bfb73c9b40142ac3f74',
        pack/'optimization/streaming/lazy_streaming.py':'635d0c4aee0aaa8d58bb0244835e08e5caa0f6a94926a5213519f40db992a257',
        pack/'new_word_compiler/certified_word_compiler.py':'e8f7048e2e73292bda230a2adad4aaa76f0b3cd5525f8f0899628bd649d1d81d',
        pack/'optimization/lazy_modular/lazy_modular.py':'08df3595a2a56dc2501bb481828093481bf76e4ac53c8b966990d233fefac1e4',
        stage/'stage80/fixed_phase.py':'d9981004a89c651f072ff88732c8b402baf83c16690a0cfacfa9c32199fde254'}
    for filename, digest in pins.items():
        assert hashlib.sha256(filename.read_bytes()).hexdigest()==digest
    os.environ.update(BRC_STAGE87_SOURCE=str(stage), BRC_STREAMING_PREVIOUS=str(prev),
                      BRC_ZERO_ENDPOINT_SOURCE=str(prev/'adversarial/zero_endpoint_extension.py'))
    for path in (stage,pack/'new_word_compiler',pack/'optimization/streaming',walker):
        sys.path.insert(0,str(path))
    from compiled_streaming import bank_from_compilation
    from lazy_streaming import LazyStreamingProgram
    from single_walker import PointRowOracle, normalize_row
    from stage45.brc_loop_recheck import verify_vendor, CALLS
    verify_vendor()
    record = gzip.decompress((pack/'direct_word_integration/DIRECT_WORD_INTEGRATION_RESULTS.json.gz').read_bytes())
    assert hashlib.sha256(record).hexdigest()=='79491e65feec104f2cdc9de510263efef749d8a1174f9cab4c20146a0171615c'
    bank = bank_from_compilation(json.loads(record)['phase_compilation'],t=4,epsilon=F(1))['bank']
    return LazyStreamingProgram(7,2,4,bank,61),PointRowOracle,normalize_row,CALLS


def native_five(program,oracle_type,normalize,calls):
    """Check every distinct normalized gauge on a source instance with five actual work tags."""
    inspection = type(program)(31,2,4,program.bank,61)
    start = len(calls)
    oracle = oracle_type(inspection,(0,0,0),query_budget=1000)
    tags = [pow(2, 2*i, 31) for i in range(5)]
    reference = [oracle.query(3,z) for z in range(32)]
    inverse = oracle.inverse_table(3)
    for z,row in enumerate(reference):
        n = levels(5,3)[tags.index(z)] if z in tags else 0
        assert [F(x,row.den) for x in row.values] == [F(n,8)]+[0]*60

    def probabilities(rows):
        output = []
        for z in tags:
            x = rows[z]
            y = oracle.apply_feedback(3,rows[inverse[z]])
            denom = 2*(oracle.norm_observation(x)+oracle.norm_observation(y))
            output.append(oracle.norm_observation(oracle.combine(x,y,halve=False))/denom)
        return output

    expected = probabilities(reference)
    order = [(i*pow(2,-1,5))%5 for i in range(5)]
    n = levels(5,3)
    changes = [i for i,z in enumerate(order) if n[z]!=n[order[(i+1)%5]]]
    words = []
    for up in combinations(changes,2):
        heights = [0]*5
        h = 0
        for i,z in enumerate(order):
            heights[z]=h
            if i in changes:
                h += 1 if i in up else -1
        assert h==0
        smallest=min(heights)
        code=[2**(v-smallest) for v in heights]
        rows = list(reference)
        for z,a in zip(tags,code):
            rows[z]=normalize((a,)+(0,)*60,8)
        assert probabilities(rows)==expected
        words.append(code)
    assert len(set(map(tuple,words)))==6
    return dict(N=31,a=2,rounds=4,history='000',all_32_true_rows=True,ordered_work_tags=tags,
                zero_bit_at_orbit_tags=list(map(str,expected)),six_dyadic_numerators_over_8=words,
                source_observer_invocations=len(calls)-start)


def native(repo,stage):
    program,oracle_type,normalize,calls = load_native(repo,stage)
    initial_calls = len(calls)
    exact, gauge, defect = ({('',1): F(1)} for _ in range(3))
    visits = set()
    feedback = set()
    errors = defaultdict(F)
    table = []
    tv_by_depth = []
    for depth in range(4):
        result = [defaultdict(F) for _ in range(3)]
        for bits in product((0,1),repeat=depth):
            h = ''.join(map(str,bits))
            oracle = oracle_type(program,bits,query_budget=1000)
            inverse = oracle.inverse_table(depth)
            true = [oracle.query(depth,i) for i in range(8)]
            gauged, altered = list(true), list(true)
            if h=='1':
                # Native quarter-turn sends e0 to -e1. Every proposal is fair.
                assert program.bank[2].apply_numer((1,)+(0,)*60)[1]==-program.bank[2].den
                for i in range(8):
                    gauged[i] = normalize((0,)*61,1)
            if h=='00':
                for i,row in enumerate(true):
                    shape = (2 if i==1 else 1) if i in (1,2,4) else 0
                    assert [F(x,row.den) for x in row.values]==[F(shape,4)]+[0]*60
                    new = 3-shape if shape else 0
                    gauged[i] = normalize((new,)+(0,)*60,4)
                altered[1] = normalize((16,)+(0,)*60,4)
            for z in range(8):
                if h in ('1','00'):
                    errors[h] += sum((F(x,true[z].den)-F(y,gauged[z].den))**2
                                     for x,y in zip(true[z].values,gauged[z].values))
                probs = []
                for rows in (true,gauged,altered):
                    x = rows[z]
                    y = oracle.apply_feedback(depth,rows[inverse[z]])
                    norms = oracle.norm_observation(x)+oracle.norm_observation(y)
                    prob = oracle.norm_observation(oracle.combine(x,y,halve=False))/(2*norms) if norms else F(1,2)
                    probs.append(prob)
                assert probs[0]==probs[1]
                if h in ('1','00') and z in (1,2,4):
                    table.append([h,z,*map(str,probs)])
                for lane,field in enumerate((exact,gauge,defect)):
                    q = (field.get((h,z),0)+field.get((h,inverse[z]),0))/2
                    if q:
                        visits.add((h,z))
                        if '1' in h:
                            feedback.add((h,z))
                        result[lane][h+'0',z] += q*probs[lane]
                        result[lane][h+'1',z] += q*(1-probs[lane])
        exact,gauge,defect = result
        assert exact==gauge and sum(exact.values())==1 and sum(defect.values())==1
        joint_tv = sum(abs(exact.get(k,0)-defect.get(k,0)) for k in exact.keys()|defect.keys())/2
        prefix_gap = defaultdict(F)
        for (h,z) in exact.keys()|defect.keys():
            prefix_gap[h] += exact.get((h,z),0)-defect.get((h,z),0)
        bit_tv = sum(map(abs,prefix_gap.values()))/2
        tv_by_depth.append([str(joint_tv),str(bit_tv)])
    prediction = F(5,16)*(F(9,10)-F(289,514))
    assert tv_by_depth[-1]==[str(prediction)]*2
    assert errors=={'1':F(1,2),'00':F(3,16)}
    assert len(calls)>initial_calls
    primary_calls=len(calls)-initial_calls
    five=native_five(program,oracle_type,normalize,calls)
    return dict(instance=dict(N=7,a=2,rounds=4,dimension=61,work_labels=8),
                tested_proposals_including_zero=8*(2**4-1),reachable_proposals=len(visits),
                reachable_with_nonzero_history=len(feedback),source_observer_invocations=primary_calls,second_orbit=five,
                changed_prefix_probabilities=table,
                raw_epsilon_by_depth=['0','1/2','3/16','0'],unconditional_bad_history_mass=['0']*4,
                gauge_joint_tv=['0']*4,defect_joint_and_bits_tv=tv_by_depth)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo', type=Path)
    parser.add_argument('--stage', type=Path)
    parser.add_argument('--verify', type=Path)
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    if bool(args.repo)!=bool(args.stage):
        parser.error('--repo and --stage must be provided together')
    result = dict(portable=portable())
    if args.repo:
        result['native']=native(args.repo.resolve(),args.stage.resolve())
    # Round-trip tuples for exact comparison with the published JSON.
    data = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
    if args.verify:
        expected = json.loads(args.verify.read_text())
        assert all(expected[key]==value for key,value in json.loads(data).items())
        print('verified '+', '.join(result))
    elif args.out:
        args.out.write_text(data)
    else:
        print(data,end='')


if __name__=='__main__':
    main()
