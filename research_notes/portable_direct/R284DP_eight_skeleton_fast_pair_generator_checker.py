#!/usr/bin/env python3
"""R284DP exact construction of all 256 sharp Port pairs from eight lower skeletons."""
import hashlib, json
from collections import Counter
from R284DM_joint_orbit_code_checker import (
    P, FROZEN_SHA256, det, frozen_arcs, arc_dist, G,
)

def bits_lower(low):
    return [1 + ((low >> (11-j)) & 1) for j in range(12)]

def q3(low):
    u1,a,x,y,u2,w,b,z,u3,g,h,r=bits_lower(low)
    t,s=6-a,13-b
    u=t*s-x*w
    p1=s*u1+x*u2
    p2=t*u2+w*u1
    return u*u3+p1*g+p2*h

def residue(i):
    upper=i>>12
    lower=i&4095
    top=sum(((upper>>(3-j))&1)<<j for j in range(4))
    return det(bits_lower(lower),top)%P

def verify():
    arcs=frozen_arcs()
    lower_reps=[x for x in range(4096) if (x&65)==0]
    assert len(lower_reps)==1024
    pairs_q={i:(q3(i),q3(i^64)) for i in lower_reps}
    assert min(max(p) for p in pairs_q.values())==60
    low_candidates=[i for i in lower_reps if max(pairs_q[i])<=60]
    assert low_candidates==[1056,1072,1312,1328,1568,1584,1824,1840]
    representatives=[(up<<12)|low for up in range(0,16,2) for low in low_candidates]
    assert len(representatives)==64
    candidate_states=set()
    for i in representatives:
        for t in G:
            candidate_states.add(i^t)
            candidate_states.add((i^4096)^t)
    assert len(candidate_states)==512
    values={};labels={}
    for i in sorted(candidate_states):
        x=residue(i)
        ds=[arc_dist(x,a) for a in arcs]
        values[i]=max(ds)
        assert ds.count(values[i])==1
        labels[i]=ds.index(values[i])
    pairs=set()
    patterns=Counter();winning=Counter()
    for base in representatives:
        gaps=[]
        for t in G:
            a=base^t;b=(base^4096)^t
            pairs.add((min(a,b),max(a,b)))
            assert labels[a]==labels[b]
            assert (residue(b)-residue(a))%P==(-q3(a&4095))%P
            gap=abs(values[a]-values[b])
            assert gap==q3(a&4095) and gap in (59,60)
            gaps.append(gap)
            winning[labels[a]]+=1
        assert max(gaps)==60
        patterns[tuple(gaps)]+=1
    assert len(pairs)==256
    assert patterns==Counter({(60,60,60,60):32,(60,60,59,59):32})
    digest=hashlib.sha256(b''.join(i.to_bytes(2,'big')+j.to_bytes(2,'big')
                                    for i,j in sorted(pairs))).hexdigest()
    assert digest=='7c05864095ba5cde368002e67764bc772ca1bfe3fabbcf26af4fb090b7d0996a'
    return {
       'schema':'R284DP_EIGHT_SKELETON_FAST_EXACT_NEAREST_PAIR_GENERATOR_V1',
       'date':'2026-11-22','status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
       'frozen_commit':'acba2d8667903434aaa2a10720f43637fcc2421b',
       'ordered_word_sha256_reference':FROZEN_SHA256,
       'parent_exact_minimum_pair_certificate':'R284DN; delta=60, exactly 256 unordered minimum pairs',
       'lower_representatives_scanned':len(lower_reps),
       'q3_pair_evaluations':2*len(lower_reps),
       'lower_skeletons':low_candidates,
       'top_bit3_zero_8_values':[0,2,4,6,8,10,12,14],
       'candidate_G_orbits':len(representatives),
       'candidate_states_evaluated':len(candidate_states),
       'arc_distance_evaluations':len(candidate_states)*len(arcs),
       'constructed_pair_count':len(pairs),
       'pair_list_sha256':digest,
       'representative_gap_patterns':{str(k):v for k,v in sorted(patterns.items())},
       'winning_label_counts':dict(sorted(winning.items())),
       'correctness':'All candidate pairs at Chebyshev 60; R284DN independently certifies exactly 256 global pairs at this minimum',
       'independent_review':'NOT_REVIEWED'
    }

if __name__=='__main__':
    c=verify()
    with open('R284DP_eight_skeleton_fast_pair_generator_certificate.json','w',encoding='utf-8') as f:
        json.dump(c,f,ensure_ascii=False,indent=2);f.write('\n')
    print(json.dumps(c,ensure_ascii=False,indent=2))
