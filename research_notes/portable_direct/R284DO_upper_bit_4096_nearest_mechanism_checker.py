#!/usr/bin/env python3
"""R284DO: upper bit XOR-4096 mechanism for exact four-read minimizing pairs."""
from collections import Counter
from hashlib import sha256
import json
from R284DM_joint_orbit_code_checker import frozen_words,frozen_arcs,arc_dist,P,G

def lower(i):
    return [1+((i>>(11-k))&1) for k in range(12)]

def q3(i):
    u1,a,x,y,u2,w,b,z,u3,g,h,r=lower(i)
    t,s=6-a,13-b
    u=t*s-x*w
    p1=s*u1+x*u2
    p2=t*u2+w*u1
    return u*u3+p1*g+p2*h

def verify():
    words=frozen_words();arcs=frozen_arcs()
    distances=[];labels=[]
    for x in words:
        ds=[arc_dist(x,arc) for arc in arcs]
        best=max(ds)
        assert ds.count(best)==1
        distances.append(best)
        labels.append(ds.index(best))
    U=[tuple(distances[i^t] for t in G) for i in range(65536)]
    order=sorted(range(65536),key=lambda i:U[i][0])
    pairs=[]
    for n,i in enumerate(order):
        jpos=n+1
        while jpos<len(order) and U[order[jpos]][0]-U[i][0]<=60:
            j=order[jpos]
            gaps=tuple(abs(U[i][k]-U[j][k]) for k in range(4))
            if max(gaps)==60:
                pairs.append((min(i,j),max(i,j),gaps))
            jpos+=1
    pairs.sort()
    assert len(pairs)==256
    keysha=sha256(b''.join(i.to_bytes(2,'big')+j.to_bytes(2,'big')
                            for i,j,_ in pairs)).hexdigest()
    assert keysha=='7c05864095ba5cde368002e67764bc772ca1bfe3fabbcf26af4fb090b7d0996a'
    assert all(i^j==4096 for i,j,_ in pairs)
    qpatterns=Counter()
    arc_labels=Counter()
    signed_gap=Counter()
    records=0
    for i,j,gaps in pairs:
        qpatterns[(q3(i),q3(i^64))]+=1
        for t in G:
            a,b=i^t,j^t
            q=q3(a)
            assert (words[b]-words[a])%P==(-q)%P
            assert labels[a]==labels[b]
            assert abs(distances[b]-distances[a])==q
            assert q in (59,60)
            arc_labels[labels[a]]+=1
            signed_gap[(q,distances[b]-distances[a])]+=1
            records+=1
    assert qpatterns==Counter({(60,60):128,(60,59):64,(59,60):64})
    assert records==1024 and len(arc_labels)==7
    return {
        'schema':'R284DO_4096_UPPER_BIT_NEAREST_MECHANISM_V1',
        'date':'2026-11-22',
        'status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
        'frozen_source_commit':'acba2d8667903434aaa2a10720f43637fcc2421b',
        'source_sha256':'b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4',
        'matched_R284DN_minimum_pair_sha256':keysha,
        'pairs':len(pairs),'upper_flip_xor':4096,
        'four_translated_pairs_checked':records,
        'same_unique_winning_arc_each_pair':True,
        'exact_modular_increment_all_pairs':True,
        'exact_scalar_distance_change_abs_equals_q3':True,
        'q3_of_pair_base_and_wflip':{str(k):v for k,v in sorted(qpatterns.items())},
        'winning_arc_label_frequency':dict(sorted(arc_labels.items())),
        'q3_and_signed_distance_change_frequency':{str(k):v for k,v in sorted(signed_gap.items())},
        'independent_review':'NOT_REVIEWED'
    }

if __name__=='__main__':
    cert=verify()
    with open('R284DO_upper_bit_4096_nearest_mechanism_certificate.json','w',encoding='utf-8') as out:
        json.dump(cert,out,ensure_ascii=False,indent=2)
        out.write('\n')
    print(json.dumps(cert,ensure_ascii=False,indent=2))
