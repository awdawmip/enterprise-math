#!/usr/bin/env python3
"""Frozen Port: sharp 4-color/2-bit injective residual label code.
Depends on pinned R284CO words/arcs and R284DD attributed farthest envelope.
All computations are exact Python integers, no external packages.
"""
import hashlib, json
from collections import defaultdict, Counter
from itertools import combinations
from R284CO_spectral_witness_checker import words, arcs, dist, FROZEN_SHA
from R284DD_attributed_envelope_checker import attributed_envelope, labeled_farthest

COLORS = (2,0,2,0,0,1,2,2,1,3,1,0,1,0,0,1,0,0,0,1,1,0,0,0,0,0,2,0,0,1,1,0,
          2,0,1,0,2,1,0,0,1,0,0,0,0,1,0,3,3,1,0,0,0,1,1,2,0,0,1,0,2,0,2,3)
CLIQUE=(1,8,62,63)

def main():
    X,A=words(),arcs()
    T,prof=attributed_envelope(A)
    data=[labeled_farthest(x,T,prof,len(A)) for x in X]
    assert all(len(y)==1 for _,y in data)
    # Independent exact baseline for each distance and winner label.
    for x,(d,labels) in zip(X,data):
        ds=[dist(x,a) for a in A]
        v=max(ds)
        assert (d,labels)==(v,tuple(k for k,z in enumerate(ds) if z==v))
    groups=defaultdict(list)
    for i,(d,labels) in enumerate(data):groups[d].append(i)
    assert len(groups)==65139
    edge_witness={}; collision_pairs=0
    for ids in groups.values():
        for i,j in combinations(ids,2):
            collision_pairs+=1
            u,v=data[i][1][0],data[j][1][0]
            assert u!=v, ('same winning arc conflict',i,j,u)
            a,b=sorted((u,v));edge_witness.setdefault((a,b),(i,j,data[i][0]))
    assert collision_pairs==420 and len(edge_witness)==84
    # Sufficiency of a fixed 4-color winner-label-only code.
    assert len(COLORS)==64 and set(COLORS)==set(range(4))
    assert all(COLORS[u]!=COLORS[v] for u,v in edge_witness)
    assert len({(d,COLORS[labels[0]]) for d,labels in data})==len(X)==65536
    # K4 witnesses establish a sharp lower bound.
    assert all(tuple(sorted((u,v))) in edge_witness for u,v in combinations(CLIQUE,2))
    clique_certificate=[]
    for u,v in combinations(CLIQUE,2):
        i,j,d=edge_witness[(u,v)]
        clique_certificate.append({'labels':[u,v],'site_indices':[i,j],'distance':d})
    # Each surjective affine 2-bit readout has two independent parity masks.
    tested_linear=0; admissible_linear=0
    for a in range(1,64):
        for b in range(a+1,64):
            tested_linear+=1
            good=all((((u&a).bit_count()&1,(u&b).bit_count()&1)!=
                      ((v&a).bit_count()&1,(v&b).bit_count()&1))
                     for u,v in edge_witness)
            if good:admissible_linear+=1
    assert tested_linear==1953 and admissible_linear==0
    cert={
      'schema':'R284DF_SHARP_TWO_BIT_WINNER_LABEL_RESIDUAL_CODE_V1',
      'frozen_sha256':FROZEN_SHA,'codewords':len(X),'arcs':len(A),
      'verified_exact_distances_and_winning_labels':len(X)*len(A),
      'distinct_D_values':len(groups),'equal_D_unordered_pairs':collision_pairs,
      'same_D_same_winning_label_pairs':0,
      'distinct_winning_label_collision_edges':len(edge_witness),
      'minimal_label_code_alphabet_size':4,
      'minimal_side_information_bits':2,
      'four_color_label_lookup':list(COLORS),
      'color_histogram':dict(sorted(Counter(COLORS).items())),
      'four_clique_labels':list(CLIQUE),
      'four_clique_six_actual_collision_witnesses':clique_certificate,
      'two_independent_parity_mask_pairs_tested':tested_linear,
      'successful_two_bit_affine_linear_codes':admissible_linear,
      'status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
      'scope':'frozen Port auxiliary observation only; no native X6 promotion'
    }
    with open('R284DF_two_bit_residual_label_certificate.json','w',encoding='utf8') as f:
        json.dump(cert,f,ensure_ascii=False,indent=2);f.write('\n')
    print(json.dumps(cert,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
