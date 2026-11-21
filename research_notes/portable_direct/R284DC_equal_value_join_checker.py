#!/usr/bin/env python3
"""R284DC: reconstruct frozen Port 307 source-neighbor ties by equal-value bucket join."""
from R284CO_spectral_witness_checker import P,FROZEN_SHA,words,arcs,dist
from R284DA_envelope_checker import envelope,farthest
from itertools import combinations
from collections import defaultdict, Counter
from pathlib import Path
import hashlib,json

EXPECTED_EDGE_SHA='251a3ca8d2d72cf6f7ca19869f174eb9e370f330533e484faf13dcb2a68dab8b'

def main():
    X=words(); A=arcs()
    T,up,dn,_=envelope(A)
    D=[farthest(x,T,up,dn) for x in X]
    assert len(D)==65536
    buckets=defaultdict(list)
    for i,v in enumerate(D): buckets[v].append(i)
    group_hist=Counter(len(bucket) for bucket in buckets.values())
    assert group_hist==Counter({1:64760,2:366,3:8,4:5})
    candidate_total=sum(len(ids)*(len(ids)-1)//2 for ids in buckets.values())
    assert candidate_total==420

    same_upper=0; cross_upper=0
    allowed=[]; disallowed=Counter(); mutation_hist=Counter()
    for v,idxs in buckets.items():
        for i,j in combinations(idxs,2):
            assert i<j and D[i]==D[j]==v
            if i//4096!=j//4096:
                cross_upper+=1
                disallowed['different_upper']+=1
                continue
            same_upper+=1
            lower_i=i%4096;lower_j=j%4096
            mask=lower_i^lower_j
            bits=mask.bit_count()
            if bits==1:
                p=11-(mask.bit_length()-1)
                allowed.append(('flip',str(p),i,j,v,p,-1))
                mutation_hist[f'flip:{p}']+=1
            elif bits==2 and (lower_i&mask).bit_count()==1:
                p,q=[p for p in range(12) if mask&(1<<(11-p))]
                allowed.append(('swap',f'{p},{q}',i,j,v,p,q))
                mutation_hist[f'swap:{p},{q}']+=1
            else:
                disallowed[f'{bits}_bit_non_neighbor']+=1

    assert (same_upper,cross_upper)==(367,53)
    assert len(allowed)==307 and sum(disallowed.values())==113
    assert mutation_hist==Counter({'flip:0':3,'flip:1':14,'flip:2':228,
                                  'flip:4':16,'flip:6':45,'swap:0,1':1})
    # Reproduce the R284CZ canonical order: source index, flip position, then swap pair.
    allowed.sort(key=lambda e:(e[2],0 if e[0]=='flip' else 1,e[5],e[6]))
    involved={i for e in allowed for i in (e[2],e[3])}
    assert len(involved)==612
    winners={}
    for i in involved:
        ds=[dist(X[i],a) for a in A]
        winning=[k for k,d in enumerate(ds) if d==D[i]]
        assert len(winning)==1
        winners[i]=winning[0]
    canonical=[[kind,mutation,i,j,v,winners[i],winners[j]]
               for kind,mutation,i,j,v,_,_ in allowed]
    sha=hashlib.sha256(json.dumps(canonical,separators=(',',':'),ensure_ascii=False)
                       .encode('utf8')).hexdigest()
    assert sha==EXPECTED_EDGE_SHA
    cert={
        'schema':'R284DC_EQUAL_VALUE_JOIN_EXACT_EDGE_GENERATOR_V1',
        'status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
        'frozen_codeword_sha256':FROZEN_SHA,'modulus_P':P,'codewords':len(X),
        'labeled_arcs':len(A),'distinct_farthest_values':len(buckets),
        'farthest_value_group_histogram':{str(k):group_hist[k] for k in sorted(group_hist)},
        'repeated_value_groups':sum(n for size,n in group_hist.items() if size>=2),
        'within_bucket_unordered_site_pairs':candidate_total,
        'same_upper_pairs':same_upper,'different_upper_pairs':cross_upper,
        'same_upper_non_neighbor_pairs':same_upper-len(allowed),
        'excluded_pairs':dict(sorted(disallowed.items())),
        'allowed_equal_distance_source_edges':len(allowed),
        'source_mutation_counts':dict(sorted(mutation_hist.items())),
        'source_indexed_equal_edge_endpoint_count':len(involved),
        'winner_label_arc_distance_evaluations':len(involved)*len(A),
        'canonical_307_edge_sha256':sha,
        'original_full_graph_edges_not_enumerated':1474560,
        'scope':'Frozen 65536-codeword Port D=d64 and original lower flip/unequal swap graph; no other rank claims'
    }
    target=Path(__file__).with_name('R284DC_equal_value_join_certificate.json')
    target.write_text(json.dumps(cert,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps(cert,ensure_ascii=False))

if __name__=='__main__':main()
