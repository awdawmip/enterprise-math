#!/usr/bin/env python3
"""R284DN: exact sharp separation and common-phase atlas of four Port reads."""
from collections import Counter
from hashlib import sha256
import json

from R284DM_joint_orbit_code_checker import frozen_arcs, frozen_words, arc_dist, G

def verify():
    arcs, words = frozen_arcs(), frozen_words()
    scalar=[max(arc_dist(x, arc) for arc in arcs) for x in words]
    reads=[(scalar[i],scalar[i^1],scalar[i^64],scalar[i^65]) for i in range(65536)]

    # For steps s<=101, any bin collision has every coordinate gap <=100.
    # A pair closer than the exhibited 60 has first-coordinate gap <=100.
    indices=sorted(range(65536), key=lambda i:reads[i][0])
    candidates=[]
    first_gap_pairs=0
    for pos,i in enumerate(indices):
        jpos=pos+1
        while jpos<len(indices) and reads[indices[jpos]][0]-reads[i][0]<=100:
            j=indices[jpos]
            first_gap_pairs+=1
            gaps=tuple(abs(reads[i][k]-reads[j][k]) for k in range(4))
            if max(gaps)<=100:
                candidates.append((min(i,j),max(i,j),gaps))
            jpos+=1
    candidates.sort()
    delta=min(max(g) for _,_,g in candidates)
    minima=[(i,j,g) for i,j,g in candidates if max(g)==delta]
    assert delta==60 and len(minima)==256
    patterns=Counter(g for _,_,g in minima)
    xors=Counter(i^j for i,j,_ in minima)
    assert xors==Counter({4096:256})
    assert patterns==Counter({(60,60,60,60):128,(59,59,60,60):64,(60,60,59,59):64})
    pair_orbits={tuple(sorted((min(i^t,j^t),max(i^t,j^t)) for t in G))
                 for i,j,_ in minima}
    assert len(pair_orbits)==64
    digest=sha256(b''.join(i.to_bytes(2,'big')+j.to_bytes(2,'big')
                            for i,j,_ in minima)).hexdigest()

    phase_bad_count={}
    first_witness=None
    for s in range(1,102):
        bad=0
        for phase in range(s):
            for i,j,gaps in candidates:
                if max(gaps)>=s: continue
                if all((reads[i][k]-phase)//s==(reads[j][k]-phase)//s
                       for k in range(4)):
                    bad+=1
                    if first_witness is None:
                        first_witness={'step':s,'phase':phase,'source_pair':[i,j],
                                       'reads_i':reads[i],'reads_j':reads[j]}
                    break
        phase_bad_count[s]=bad
    assert all(phase_bad_count[s]==0 for s in range(1,69))
    assert phase_bad_count[69]==1
    assert [phase_bad_count[s] for s in (70,71,72,73,74,75)]==[7,1,0,0,31,0]
    return {
        'schema':'R284DN_FOUR_READ_PRECISION_V1',
        'date':'2026-11-22',
        'status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
        'frozen_source':'awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py',
        'ordered_residue_sha256':'b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4',
        'states':len(words), 'arcs':len(arcs),
        'sweep_first_coordinate_gap_max':100,
        'pairs_with_first_coordinate_gap_le100':first_gap_pairs,
        'candidate_pairs_with_all_gaps_le100':len(candidates),
        'four_read_min_Linfty_distance':delta,
        'minimum_pair_count':len(minima),
        'minimum_pair_G_orbits':len(pair_orbits),
        'minimum_pair_xor_histogram':dict(xors),
        'minimum_pair_gap_patterns':{str(k):v for k,v in sorted(patterns.items())},
        'minimum_pairs_sha256':digest,
        'max_correctable_integer_error_per_register':(delta-1)//2,
        'quantization_shared_phase_s_1_to_101_bad_phase_counts':phase_bad_count,
        'first_shared_phase_collision':first_witness,
        'independent_phase_max_universally_safe_integer_step':delta,
        'method':'Exact integer sweep + exhaustive phase bin checks; no floating point',
        'independent_review':'NOT_REVIEWED'
    }

if __name__=='__main__':
    result=verify()
    with open('R284DN_joint_four_read_precision_certificate.json','w',encoding='utf-8') as out:
        json.dump(result,out,ensure_ascii=False,indent=2)
        out.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k in (
        'four_read_min_Linfty_distance','minimum_pair_count',
        'minimum_pair_G_orbits','first_shared_phase_collision',
        'pairs_with_first_coordinate_gap_le100',
        'candidate_pairs_with_all_gaps_le100')},ensure_ascii=False,indent=2))
