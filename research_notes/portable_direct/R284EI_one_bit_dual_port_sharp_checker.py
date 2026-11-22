#!/usr/bin/env python3
"""R284EI exact independent-source-bit repair on frozen R284CO Port model.
Run alongside R284CO_spectral_witness_checker.py. Python standard library only.
All states and distances are integers, and all claims are finite-domain.
"""
from collections import Counter
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
from R284CO_spectral_witness_checker import P, FROZEN_SHA, det, arcs, dist

N = 1 << 16
OFFSETS = (0, 65)
FULL_OFFSETS = (0, 1, 64, 65)
BIT = 12

def source_reads():
    arc_list = arcs()
    digest = sha256()
    values = []
    for upper in product((1, 2), repeat=4):
        top = sum((x-1) << j for j,x in enumerate(upper))
        for lower in product((1, 2), repeat=12):
            residue = det(lower,top) % P
            digest.update(residue.to_bytes(8, 'big'))
            values.append(max(dist(residue, arc) for arc in arc_list))
    assert digest.hexdigest() == FROZEN_SHA
    assert len(arc_list) == 64 and len(values) == N
    return values

def exact_min_same_bit(values, offsets):
    """Exhaust pairs using |first coord difference|<=current best pruning."""
    order = sorted(range(N), key=lambda i: (values[i], i))
    best = P
    winners = []
    comparisons = 0
    for k, i in enumerate(order):
        j = k-1
        while j >= 0 and values[i] - values[order[j]] <= best:
            other = order[j]
            if not ((i ^ other) & (1 << BIT)):
                comparisons += 1
                delta = max(abs(values[i ^ o] - values[other ^ o]) for o in offsets)
                if delta < best:
                    best = delta
                    winners = [tuple(sorted((i,other)))]
                elif delta == best:
                    winners.append(tuple(sorted((i,other))))
            j -= 1
    winners.sort()
    assert best == 9394 and winners == [(17336,33446),(17401,33511)], (best,winners)
    return {'distance':best,'minimizer_pairs':[list(x) for x in winners],
            'comparisons_same_bit':comparisons}

def close_pair_xors(values, bound=100):
    order = sorted(range(N), key=lambda i:(values[i],i))
    left=0
    hist=Counter()
    total=0
    for k,i in enumerate(order):
        while values[i] - values[order[left]] > bound:
            left+=1
        for j in range(left,k):
            other=order[j]
            if max(abs(values[i^o]-values[other^o]) for o in FULL_OFFSETS)<=bound:
                total+=1
                hist[i^other]+=1
    assert total == 11264 and hist == Counter({4096:11264})
    return {'bound_inclusive':bound,'full_port_close_pairs':total,
            'xor_histogram':{str(k):v for k,v in sorted(hist.items())}}

def quantum(values,i,offsets,s,t):
    return tuple((values[i^q]-t)//s for q in offsets)

def direct_phase_checks(values):
    examples = []
    for s,t in ((69,67),(70,25),(74,0),(94,0),(101,0),(9395,58)):
        seen={}
        collisions=[]
        for i in range(N):
            code=quantum(values,i,OFFSETS,s,t)
            key=(i>>BIT&1,code)
            old=seen.get(key)
            if old is not None:
                collisions.append([old,i])
            else:
                seen[key]=i
        if s<=101:
            assert not collisions,(s,t,collisions[:3])
        elif s==9395:
            assert [17401,33511] in collisions
        examples.append({'width':s,'phase':t,
                         'same_bit_dual_read_collision_count':len(collisions),
                         'example_collision':collisions[0] if collisions else None})
    i,j,s,t=17401,33511,9395,58
    assert (i>>12&1)==(j>>12&1)
    assert quantum(values,i,OFFSETS,s,t)==quantum(values,j,OFFSETS,s,t)
    assert [abs(values[i^q]-values[j^q]) for q in OFFSETS]==[2164,9394]
    assert i^j==49438
    return examples

def main():
    values=source_reads()
    same_bit=exact_min_same_bit(values,OFFSETS)
    close=close_pair_xors(values)
    direct=direct_phase_checks(values)
    assert all(((i^q)>>BIT&1)==(i>>BIT&1) for i in range(N) for q in (1,64,65))
    proof_cert={
        'schema':'R284EI_SHARP_ONE_SOURCE_BIT_DUAL_PORT_REPAIR_V1',
        'source_repo':'awdawmip/enterprise-math',
        'frozen_source_commit':'acba2d8667903434aaa2a10720f43637fcc2421b',
        'frozen_source_path':'research_notes/portable_direct/R284CO_spectral_witness_checker.py',
        'frozen_source_blob_sha1':'b46e0f682b58e47c27094b4bea6fa4e55119a3ee',
        'frozen_codeword_sha256':FROZEN_SHA,
        'source_states':N,
        'source_bit':'(i >> 12) & 1',
        'read_offsets':list(OFFSETS),
        'maximal_uniform_all_phase_integer_width':9394,
        'first_failing_width':9395,
        'first_failure_phase':58,
        'finite_domain_same_bit_minimum_Linf':same_bit,
        'full_port_near_pairs':close,
        'selected_direct_checks':direct,
        'update_invariance_offsets':[1,64,65],
        'evidence_class':'AUTHOR_EXACT_CHECKED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
        'independent_review':'NOT_REVIEWED'}
    out=Path(__file__).with_name('R284EI_one_bit_dual_port_sharp_certificate.json')
    out.write_text(json.dumps(proof_cert,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'same_bit':same_bit,'near_pairs':close,
                      'selected_checks':direct,'certificate':str(out)},ensure_ascii=False))
if __name__=='__main__':main()
