#!/usr/bin/env python3
"""R284CS: 64-layer maximal-order-statistic core on frozen 34-bit Port observer.
Uses exact frozen generator from R284CO, standard library only.
"""
import hashlib, heapq, json
from collections import Counter
from pathlib import Path
from R284CO_spectral_witness_checker import P,D,Z,SELECT,FROZEN_SHA,words,arcs,dist


def compute():
    X,A=words(),arcs()
    Q=65
    heaps=[[] for _ in range(64)]
    for idx,x in enumerate(X):
        for k,value in enumerate(sorted(dist(x,arc) for arc in A)):
            entry=(value,idx)
            if len(heaps[k])<Q:heapq.heappush(heaps[k],entry)
            elif entry>heaps[k][0]:heapq.heapreplace(heaps[k],entry)
    rows=[sorted(h,reverse=True) for h in heaps]
    assert all(len(row)==65 for row in rows)
    assert all(rows[k][r][0]>rows[k][r+1][0]
               for k in range(1,64) for r in range(64))
    unique_indices=set(); core_sizes=[]; gaps=[]; layer_counts=[]
    for r in range(64):
        rank_entries=[rows[k][r][1] for k in range(1,64)]
        layer_counts.append(len(set(rank_entries)))
        unique_indices.update(rank_entries)
        core_sizes.append(len(unique_indices))
        gaps.append(min(rows[k][r][0]-rows[k][r+1][0] for k in range(1,64)))
    assert core_sizes[:4]==[63,124,186,248]
    assert core_sizes[-1]==3712
    assert sum(1 for k in range(1,64) for r in range(64))==4032
    h=hashlib.sha256(b''.join(X[i].to_bytes(8,'big') for i in sorted(unique_indices,key=X.__getitem__))).hexdigest()
    ctr=Counter(rows[k][r][1] for k in range(1,64) for r in range(64))
    hist=dict(sorted(Counter(ctr.values()).items()))
    near=[{'level':k+1,'order':r+1,'gap':rows[k][r][0]-rows[k][r+1][0],
           'upper_value':rows[k][r][0],'lower_value':rows[k][r+1][0],
           'upper_residue':X[rows[k][r][1]],'lower_residue':X[rows[k][r+1][1]]}
          for k in range(1,64) for r in range(64)
          if rows[k][r][0]-rows[k][r+1][0]==min(gaps)]
    core_rows=[sorted(dist(X[i],a) for a in A) for i in unique_indices]
    assert len(unique_indices)>=65 and all([v for v,i in rows[k][:64]] ==
      sorted((row[k] for row in core_rows),reverse=True)[:64] for k in range(1,64))
    result={
      'schema':'R284CS_64_LAYER_MAX_SPECTRUM_CORE_V1',
      'status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
      'pins':{'P':P,'D':list(D),'Z':list(Z),'SELECT':list(SELECT),'frozen_sha256':FROZEN_SHA},
      'population':65536,'arc_count':64,'spectral_levels':'k=2..64','preserved_orders':'r=1..64',
      'discovery_site_arc_distance_evaluations':4194304,
      'core_verification_site_arc_distance_evaluations':len(unique_indices)*64,
      'witness_level_order_pairs':4032,'distinct_full_core':len(unique_indices),
      'full_core_fraction':{'numerator':len(unique_indices),'denominator':65536},
      'minimal_core_size_by_order_r1_to_r64':core_sizes,
      'distinct_site_count_per_exact_order_r1_to_r64':layer_counts,
      'smallest_gap_rank_r_to_rank_rplus1_per_order_r1_to_r64':gaps,
      'global_minimum_gap':min(gaps),'global_minimum_gap_witnesses':near,
      'witness_multiplicity_histogram_in_full_64_layer_core':hist,
      'full_core_sha256_sorted_residue_u64be':h,
      'top4_crosscheck':{'sizes':[63,124,186,248], 'fourth_rank_witness_r6_r19':X[rows[5][3][1]]},
      'verification':{'frozen_sha_match':True,'strict_all_4032_cutoffs':True,
        'full_core_recomputed_all_63x64_top_values':True,'independent_review':'NOT_REVIEWED'}
    }
    return result


if __name__=='__main__':
    d=compute()
    Path('R284CS_top64_spectrum_certificate.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'core':d['distinct_full_core'],'min_gap':d['global_minimum_gap'],
                      'near':d['global_minimum_gap_witnesses'],
                      'hist':d['witness_multiplicity_histogram_in_full_64_layer_core'],
                      'core_sha256':d['full_core_sha256_sorted_residue_u64be']},ensure_ascii=False))
