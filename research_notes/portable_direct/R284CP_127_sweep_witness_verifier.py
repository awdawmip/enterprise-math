#!/usr/bin/env python3
"""R284CP: verify all 63 unique Port spectral witnesses using 127 event sweeps.
Run in the folder containing the frozen R284CO checker and JSON certificate.
"""
from bisect import bisect_left
from collections import defaultdict
import json
import time
from R284CO_spectral_witness_checker import P, arcs, words, dist


def deficiencies(sites, circles, radius, k):
    """Number of population sites with fewer than k covering arcs at integer radius."""
    assert 0 <= radius <= (P-1)//2
    events = defaultdict(int)
    events[0] += 0
    events[P] += 0
    fixed = 0
    for a, width in circles:
        if width + 2*radius >= P-1:
            fixed += 1
            continue
        lo = (a-radius) % P
        hi = (a+width+radius) % P
        if lo <= hi:
            events[lo] += 1
            events[hi+1] -= 1
        else:
            events[0] += 1
            events[hi+1] -= 1
            events[lo] += 1
            events[P] -= 1
    cnt=0
    deficient_sites=[]
    coverage=fixed
    e=sorted(events.items())
    for (lo, change), (hi, _) in zip(e,e[1:]):
        coverage += change
        if coverage >= k or lo == hi:
            continue
        left=bisect_left(sites, lo)
        right=bisect_left(sites, hi)
        if right>left:
            cnt += right-left
            deficient_sites.extend(sites[left:min(right,left+3-len(deficient_sites))])
    return cnt, deficient_sites


def verify(candidate):
    t=time.perf_counter()
    A=arcs()
    W=words()  # SHA256 validates frozen 65,536-codeword population
    sites=sorted(W)
    assert len(sites)==65536 and len(A)==64
    prep=time.perf_counter()-t
    U=candidate['U_all_64']
    indices=candidate['winner_index_k2_to_k64']
    residues=candidate['winner_residue_k2_to_k64']
    margins=candidate['strict_margin_k2_to_k64']
    assert len(U)==64 and len(indices)==len(residues)==len(margins)==63
    assert len(set(residues))==len(set(indices))==63
    assert U[0]==0
    t=time.perf_counter()
    n0,_=deficiencies(sites,A,0,1)
    assert n0==0  # all actual residues have some zero-radius fiber
    below=[]
    runners=[]
    for j in range(1,64):
        k=j+1
        index=indices[j-1]
        witness=residues[j-1]
        margin=margins[j-1]
        u=U[j]
        assert W[index]==witness and 0<margin<u
        # One independently evaluated order statistic, not an assumed value.
        assert sorted(dist(witness,a) for a in A)[j]==u
        v=u-margin
        cnt, misses=deficiencies(sites,A,v,k)
        assert cnt==1 and misses==[witness], (k,v,cnt,misses,witness)
        earlier,misses2=deficiencies(sites,A,v-1,k)
        assert earlier==2 and witness in misses2, (k,v-1,earlier,misses2)
        runner=next(x for x in misses2 if x!=witness)
        assert sorted(dist(runner,a) for a in A)[j]==v
        runners.append(runner)
        below.append(earlier)
    assert len(set(runners))==63
    winners=set(residues)
    shared=sorted(winners & set(runners))
    assert len(shared)==2
    elapsed=time.perf_counter()-t
    assert min(margins)==64 and [j+2 for j,z in enumerate(margins) if z==64]==[15,16]
    return {
       'schema':'R284CP_127_SWEEP_WITNESS_VERIFIER_V1',
       'source_candidate_schema':candidate['schema'],
       'scope':'frozen 65536-residue auxiliary Port observer',
       'status':'EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
       'counts':{'preparation_codewords':len(W),'arcs':len(A),
                 'integer_event_sweeps':127,'direct_winner_and_runner_arc_distances':2*63*64,
                 'full_population_pairwise_distance_enumeration':0,
                 'essential_witnesses_verified':63},
       'k1_deficit_at_zero':n0,
       'one_deficit_at_all_63_proposed_runner_up_radii':True,
       'exactly_two_deficits_one_before_runner_up_all_63':True,
       'deficit_counts_one_before_runner_up_k2_to_k64':below,
       'unique_runner_up_residues_k2_to_k64':runners,
       'runner_up_residues_pairwise_distinct':True,
       'runner_up_overlap_with_winner_residues':shared,
       'unique_winner_indices_k2_to_k64':indices,
       'minimum_margin':min(margins),
       'timings_single_host_seconds':{'population_generation_and_sort':round(prep,6),
                                      '127_sweeps_and_witness_checks':round(elapsed,6)},
       'validation':{'candidate_threshold_and_winner_checks':'exhaustive-via-127-event-sweeps',
                     'integer_closed_interval_events':'right-end-plus-one',
                     'original_frozen_sha_verified':True,'independent_peer_review':'NOT_REVIEWED'}
    }

if __name__=='__main__':
    with open('R284CO_spectral_witness_certificate.json',encoding='utf-8') as f:
        c=json.load(f)
    record=verify(c)
    with open('R284CP_127_sweep_witness_certificate.json','w',encoding='utf-8') as f:
        json.dump(record,f,indent=2,ensure_ascii=False);f.write('\n')
    print(json.dumps({'sweeps':record['counts']['integer_event_sweeps'],
                      'verified':record['counts']['essential_witnesses_verified'],
                      'time':record['timings_single_host_seconds']}))
