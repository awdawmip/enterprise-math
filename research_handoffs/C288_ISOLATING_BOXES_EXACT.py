#!/usr/bin/env python3
"""C288 exact disjoint root-containing boxes for 125 auxiliary threshold witnesses.
Needs frozen C275_STANDALONE_EXACT_REPLAY.py and C284_187_EXACT_DYADIC_BRACKETS.json.
Only standard-library exact Fraction comparisons. Author-level geometry.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
import hashlib, json
import C275_STANDALONE_EXACT_REPLAY as source

SOURCE_CERT_SHA='fcdad45cb2ed5df659b1a153762d358e2b7fa4df3e14c1be3eb505d4209ef576'

def build_paths():
    cert=json.load(open('C284_187_EXACT_DYADIC_BRACKETS.json',encoding='utf-8'))
    payload=json.dumps(cert['records'],separators=(',',':'),ensure_ascii=False).encode('utf-8')
    assert hashlib.sha256(payload).hexdigest()==cert['certificate_sha256']==SOURCE_CERT_SHA
    assert len(cert['records'])==187 and cert['denominator']==4096
    hulls=source.hulls()
    paths={}; labels=set(); multiplicity=Counter()
    for i,j,wid,k in cert['records']:
        assert (i,j) not in labels and wid in (1,2) and 0<=k<4096
        labels.add((i,j))
        lo,hi,kind=hulls[i,j]
        assert kind in ('touch','cross')
        w=source.WITNESSES[wid-1]
        h=source.high_point(lo,hi)
        assert source.inside(w,lo,hi) and source.inside(h,lo,hi)
        key=(wid,h)
        if key in paths:
            assert paths[key]['k']==k
        else:
            d=tuple(h0-w0 for w0,h0 in zip(w,h))
            a,b=F(k,4096),F(k+1,4096)
            p0=tuple(w0+a*d0 for w0,d0 in zip(w,d))
            p1=tuple(w0+b*d0 for w0,d0 in zip(w,d))
            assert 0<a<b<1 and source.valid(p0) and source.valid(p1)
            box=tuple((min(x,y),max(x,y)) for x,y in zip(p0,p1))
            paths[key]={'wid':wid,'w':w,'h':h,'d':d,'k':k,'box':box}
        multiplicity[key]+=1
    assert len(paths)==125
    assert Counter(k[0] for k in paths)==Counter({1:122,2:3})
    return [v for _,v in sorted(paths.items(),key=lambda kv:kv[0])],multiplicity

def coordinate_gap(a,b):
    return max(F(0),a[0]-b[1],b[0]-a[1])

def verify():
    paths,multiplicity=build_paths()
    best=None; best_pair=None; coord_winners=Counter()
    threshold=F(1,2**23)
    tested=0
    for i,j in combinations(range(len(paths)),2):
        gaps=[coordinate_gap(x,y) for x,y in zip(paths[i]['box'],paths[j]['box'])]
        g=max(gaps)
        assert g>threshold,(i,j,g)
        best_coord=gaps.index(g)
        coord_winners[best_coord]+=1
        tested+=1
        if best is None or g<best:
            best=g;best_pair=[i,j,best_coord]
    assert tested==7750
    max_l1=max(sum(abs(x) for x in p['d']) for p in paths)
    assert max_l1==F(25437513,1103011000) and 40*max_l1<1
    assert best==F(518383,3360752136192) and best_pair==[34,59,0]
    assert Counter(multiplicity.values())==Counter({1:100,2:16,3:3,5:1,6:2,7:1,8:1,14:1})
    result={
        'schema':'EM_C288_EXACT_ROOT_BOXES_V1',
        'model':'C195_H168_79_NODE_POSITIVE_RATIONAL_AUXILIARY',
        'source_c284_record_sha256':SOURCE_CERT_SHA,
        'n_labeled_c284_records':187,
        'n_unique_paths_and_root_containing_boxes':125,
        'n_unordered_box_pairs_checked':tested,
        'pair_winning_coordinate_counts':dict(sorted(coord_winners.items())),
        'exact_minimum_infinity_gap':str(best),
        'minimum_gap_pair_sorted_path_indices':best_pair[:2],
        'minimum_gap_witness_coordinate':best_pair[2],
        'uniform_consequence':'all pairwise l_inf distances exceed 1/8388608',
        'maximum_path_direction_l1':str(max_l1),
        'exact_direction_bound':'max_l1 < 1/40',
        'conditional_on_c285_gradient_bound':'reusing C285 F_prime > Q/56 on each C284 bracket, at each root ||grad F||_infinity > 5Q/7',
        'distinct_root_count_dependency':'C284 IVT endpoint certificates only, NOT C286 uniqueness or C287 affine separation',
        'native_transfer':'NO GF(2)-BRC phase/sign/port/provenance or X6 bridge inferred',
        'formal_admission':False
    }
    with open('C288_AUTHOR_EXACT_AUDIT_20261025.json','w',encoding='utf-8') as out:
        json.dump(result,out,ensure_ascii=False,indent=2)
        out.write('\n')
    print('C288_EXACT_ISOLATING_BOXES_PASS',len(paths),'paths',tested,'pairs')
    print('minimum gap:',best,'bound > 2^-23: PASS; witness',best_pair)
    print('maximum direction L1:',max_l1,'< 1/40: PASS')
    print('coordinate witnesses:',dict(sorted(coord_winners.items())))
    return result

if __name__=='__main__':verify()
