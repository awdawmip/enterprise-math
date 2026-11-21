#!/usr/bin/env python3
"""R284DL: exact w-orbit code and common-phase quantization atlas.
Requires pinned R284CO_spectral_witness_checker.py in this directory.
"""
from collections import Counter
from hashlib import sha256
import json
from R284CO_spectral_witness_checker import words,arcs,dist,FROZEN_SHA

N=65536
W_BIT=64
MAX_STEP=70

def near_pairs(points,cutoff):
    order=sorted((a,b,i) for i,(a,b) in enumerate(points))
    hits=[]
    for p,(a,b,i) in enumerate(order):
        k=p+1
        while k<len(order) and order[k][0]-a<cutoff:
            aa,bb,j=order[k]
            if abs(bb-b)<cutoff:
                hits.append((min(i,j),max(i,j),aa-a,abs(bb-b)))
            k+=1
    return sorted(hits)

def scan_phases(points,pairs,s):
    bad={}
    cand=0
    for i,j,da,db in pairs:
        if da>=s or db>=s:continue
        cand+=1
        u,v=points[i],points[j]
        for t in range(s):
            if t in bad:continue
            if (u[0]-t)//s==(v[0]-t)//s and (u[1]-t)//s==(v[1]-t)//s:
                bad[t]=(i,j)
    return cand,bad

def direct_check(points,s):
    bad=set()
    for t in range(s):
        seen=set()
        for a,b in points:
            key=((a-t)//s,(b-t)//s)
            if key in seen:
                bad.add(t)
                break
            seen.add(key)
    return bad

def check():
    X=words()  # asserts original ordered SHA-256 and all words distinct
    A=arcs()
    assert len(X)==N and len(A)==64
    values=[max(dist(x,arc) for arc in A) for x in X]
    E=[(values[i],values[i^W_BIT]) for i in range(N)]
    assert len(set(E))==N
    orbits=set()
    gaps=[]
    directions=Counter()
    for i in range(N):
        j=i^W_BIT
        if i>j:continue
        a,b=E[i]
        assert a!=b and E[j]==(b,a)
        key=(min(a,b),max(a,b))
        assert key not in orbits
        orbits.add(key)
        gaps.append((abs(a-b),i,a,b))
        directions['less' if a<b else 'greater']+=1
    assert len(orbits)==N//2
    assert min(gaps)[0]==59
    close=near_pairs(E,54)
    nearest=[(i,j) for i,j,da,db in close if max(da,db)==53]
    assert len(close)==2 and len(nearest)==2
    nearby=near_pairs(E,MAX_STEP+1)
    assert len(nearby)==1283
    atlas={}
    for s in range(1,MAX_STEP+1):
        candidates,bad=scan_phases(E,nearby,s)
        atlas[str(s)]={
            'near_candidate_pairs':candidates,
            'safe_phases':s-len(bad),
            'bad_phases':len(bad),
            'bad_phase_list':sorted(bad),
            'first_bad_example':None if not bad else {
                'phase':min(bad),'states':list(bad[min(bad)]),
                'signatures':[list(E[i]) for i in bad[min(bad)]]
            }
        }
    all_safe=[s for s in range(1,MAX_STEP+1) if atlas[str(s)]['bad_phases']==0]
    assert all_safe==list(range(1,56))+[59]
    assert atlas['56']['bad_phases']==3 and atlas['59']['bad_phases']==0
    assert atlas['64']['bad_phases']==38 and atlas['70']['bad_phases']==70
    independently={}
    for s in (53,54,55,56,59,64,70):
        actual=direct_check(E,s)
        expected=set(atlas[str(s)]['bad_phase_list'])
        assert actual==expected
        independently[str(s)]={'all_65536_states_checked_for_all_phases':True,'bad_phases':len(actual)}
    i,j=nearest[0]
    u,v=E[i],E[j]
    t0=next(t for t in range(54) if (u[0]-t)//54==(v[0]-t)//54)
    t1=next(t for t in range(54) if (u[1]-t)//54==(v[1]-t)//54)
    assert ((u[0]-t0)//54,(u[1]-t1)//54)==((v[0]-t0)//54,(v[1]-t1)//54)
    digest=sha256(b''.join(a.to_bytes(8,'big')+b.to_bytes(8,'big') for a,b in E)).hexdigest()
    return {
        'schema':'R284DL_W_FLIP_ORBIT_PHASE_QUANTIZATION_V1',
        'status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
        'source':'enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py',
        'source_blob_sha1':'b46e0f682b58e47c27094b4bea6fa4e55119a3ee',
        'frozen_word_sha256':FROZEN_SHA,
        'states':N,'arcs':64,'distance_evaluations':N*64,
        'two_read_signatures_distinct':len(set(E)),
        'scalar_distinct_values':len(set(values)),
        'w_orbits':len(orbits),'unordered_pair_keys':len(orbits),
        'within_orbit_equal_distance_count':0,
        'w_orbit_gap_min':min(gaps)[0],
        'w_orbit_gap_min_witness':list(min(gaps)),
        'canonical_lower_index_direction':dict(directions),
        'ordered_signature_sha256':digest,
        'ordered_min_linf':53,'ordered_min_pairs':[list(z) for z in nearest],
        'near_pairs_both_gaps_lt_71':len(nearby),
        'all_phases_safe_steps_1_to_70':all_safe,
        'step_atlas_53_to_70':{str(s):atlas[str(s)] for s in range(53,71)},
        'direct_independent_quantizer_checks':independently,
        'first_shared_phase_failure_step':56,
        'shared_phase_recovery_step':59,
        'independent_coordinate_phase_failure_step':54,
        'independent_phase_54_witness':{'states':[i,j],'signatures':[list(u),list(v)],'phases':[t0,t1]},
        'verification_scope':'entire frozen population; every w orbit; all candidate pairs with both coordinate gaps <71; all common integer phases for every step 1..70',
        'independent_review':'NOT_REVIEWED'
    }

if __name__=='__main__':
    out=check()
    with open('R284DL_w_flip_orbit_quantization_certificate.json','w',encoding='utf-8') as f:
        json.dump(out,f,indent=2,sort_keys=True,ensure_ascii=False)
        f.write('\n')
    print(json.dumps({
      'w_orbits':out['w_orbits'],
      'min_gap':out['w_orbit_gap_min'],
      'all_phase_safe_steps':out['all_phases_safe_steps_1_to_70'],
      'near_pairs':out['near_pairs_both_gaps_lt_71']
    }))
