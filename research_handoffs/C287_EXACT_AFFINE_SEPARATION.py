#!/usr/bin/env python3
"""C287 exact pairwise affine separation. Uses C275 and C284 frozen inputs."""
from fractions import Fraction
from itertools import combinations
from collections import Counter
import hashlib,json,base64
import C275_STANDALONE_EXACT_REPLAY as src

EXPECTED_RECORDS_SHA256 = 'fcdad45cb2ed5df659b1a153762d358e2b7fa4df3e14c1be3eb505d4209ef576'
COORD2 = tuple(combinations(range(4),2))
COORD3 = tuple(combinations(range(4),3))

def det2(u,v,idx):
    a,b=idx
    return u[a]*v[b]-u[b]*v[a]

def det3(u,v,w,idx):
    a,b,c=idx
    return (u[a]*(v[b]*w[c]-v[c]*w[b])
           -u[b]*(v[a]*w[c]-v[c]*w[a])
           +u[c]*(v[a]*w[b]-v[b]*w[a]))

def main():
    data=json.load(open('C284_187_EXACT_DYADIC_BRACKETS.json',encoding='utf-8'))
    raw=json.dumps(data['records'],ensure_ascii=False,separators=(',',':')).encode('utf-8')
    assert hashlib.sha256(raw).hexdigest()==EXPECTED_RECORDS_SHA256
    assert data['certificate_sha256']==EXPECTED_RECORDS_SHA256
    records=data['records']
    assert len(records)==187
    hs=src.hulls()
    paths={}
    multiplicities=Counter()
    labels=[]
    for i,j,wid,k in records:
        assert wid in (1,2) and (i,j) in hs and 0<=k<4096
        lo,hi,kind=hs[(i,j)]
        assert kind in ('cross','touch')
        w=src.WITNESSES[wid-1]
        h=src.high_point(lo,hi)
        assert src.valid(w) and src.valid(h)
        assert src.inside(w,lo,hi) and src.inside(h,lo,hi)
        paths[(wid,h)]=(w,h)
        multiplicities[(wid,h)]+=1
        labels.append((i,j))
    assert len(set(labels))==187
    assert len(paths)==125
    assert dict(Counter(multiplicities.values()))=={1:100,2:16,3:3,5:1,6:2,7:1,8:1,14:1}
    paths=sorted(paths.items(),key=lambda item:item[0])
    sizes=Counter(k[0] for k,v in paths)
    assert sizes==Counter({1:122,2:3}),sizes

    minors=bytearray()
    counts=Counter()
    witnesses=Counter()
    for i in range(len(paths)):
        (wid1,h1),(w1,_)=paths[i]
        d1=tuple(y-x for x,y in zip(w1,h1))
        for j in range(i+1,len(paths)):
            (wid2,h2),(w2,_)=paths[j]
            d2=tuple(y-x for x,y in zip(w2,h2))
            delta=tuple(y-x for x,y in zip(w1,w2))
            if wid1==wid2:
                assert w1==w2 and delta==(0,0,0,0)
                choices=[z for z,rows in enumerate(COORD2) if det2(d1,d2,rows)]
                assert choices,(i,j)
                typ='COMMON_WITNESS_DISTINCT_RAYS'; idx=choices[0]
                counts[typ]+=1
            else:
                choices=[z for z,rows in enumerate(COORD3) if det3(d1,d2,delta,rows)]
                assert choices,(i,j)
                typ='SKEW_DISTINCT_WITNESSES'; idx=choices[0]
                counts[typ]+=1
            witnesses[(typ,idx)]+=1
            minors.append(idx)
    assert len(minors)==7750
    assert counts=={'COMMON_WITNESS_DISTINCT_RAYS':7384,'SKEW_DISTINCT_WITNESSES':366},counts
    result={
        'schema':'EM_C287_EXACT_AFFINE_SEPARATION_V1',
        'model':'C195_H168_79_NODE_POSITIVE_RATIONAL_AUXILIARY',
        'upstream_c284_record_sha256':EXPECTED_RECORDS_SHA256,
        'labeled_regions':187,
        'unique_endpoint_defined_paths':len(paths),
        'path_counts_by_witness':dict(sizes),
        'path_label_multiplicity_histogram':dict(sorted(Counter(multiplicities.values()).items())),
        'unordered_path_pairs':len(minors),
        'pairwise_geometry':dict(counts),
        'coordinate_mirror_minor_hists':{
          f'{typ}/{idx}':n for (typ,idx),n in sorted(witnesses.items())},
        'minor_choice_encoding':'base64 of 7750 bytes in lexicographic sorted (witness_id, high_endpoint) path-pair order; byte = lexicographically first nonzero 2x2 or 3x3 minor index; indices 0..5 for coordinate pairs, 0..3 for coordinate triples',
        'minor_choice_base64':base64.b64encode(minors).decode('ascii'),
        'minor_choice_sha256':hashlib.sha256(minors).hexdigest(),
        'logical_dependency':'C284 strict endpoint crossing and C286 full-line strict monotonicity/unique interior root are reused; geometry is separately proved here.',
        'scope':'At least 125 geometrically distinct roots of F(v)=2^128, one per certified path; no assertion of all roots in the four-variable domain or native X6/BRC.'
    }
    with open('C287_125_DISTINCT_GEOMETRIC_ROOTS_CERTIFICATE.json','w',encoding='utf-8') as f:
        json.dump(result,f,ensure_ascii=False,indent=2);f.write('\n')
    print('C287_AFFINE_ROOT_SEPARATION_PASS',len(paths),'paths',len(minors),'pairs',dict(counts),dict(sorted(witnesses.items())))
    print('fingerprint',result['minor_choice_sha256'])
    return result

if __name__=='__main__':main()
