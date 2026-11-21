#!/usr/bin/env python3
"""R284DJ: recover a frozen source state from two D reads without a full inverse index."""
import hashlib
import json
import random
from itertools import product
from R284CO_spectral_witness_checker import words, arcs, dist, det, P, D, Z, FROZEN_SHA

CORE_POS = (0,1,2,4,5,6)  # u1,a,x,u2,w,b
FREE_POS = (3,7,8,9,10)  # y,z,u3,g,h; upper beta3 is sixth free bit

def kappa(top3, lower):
    u1,a,x,y,u2,w,b,z,u3,g,h,r = lower
    t,s=6-a,13-b
    u=t*s-x*w
    p1,p2=s*u1+x*u2,t*u2+w*u1
    return ((1-D[0]+(top3&1))*u
            +(Z[1]+1+((top3>>1)&1))*p1
            +(Z[2]+1+((top3>>2)&1))*p2)

def core_table():
    table={}
    for top3 in range(8):
        for vals in product((1,2),repeat=6):
            l=[1]*12
            for p,v in zip(CORE_POS,vals):l[p]=v
            key=kappa(top3,l)
            assert key not in table
            table[key]=(top3,vals)
    assert len(table)==512 and min(table)==-58690413 and max(table)==-29955930
    return table

def max_dist(x, arcs64):
    return max(dist(x,a) for a in arcs64)

def inverse_D_candidates(d, arcs64):
    assert d>0
    seeds=set()
    for a,w in arcs64:
        seeds.add((a-d)%P)
        seeds.add((a+w+d)%P)
    assert len(seeds)<=128
    return sorted(x for x in seeds if max_dist(x,arcs64)==d)

def decode(d0,d1,arcs64,table):
    c0=inverse_D_candidates(d0,arcs64)
    c1=inverse_D_candidates(d1,arcs64)
    found=[]
    matched=0
    detcalls=0
    for x in c0:
        for xp in c1:
            delta=(xp-x)%P
            if delta==0:continue
            if delta<P//2: r,k=2,-delta
            else: r,k=1,delta-P
            core=table.get(k)
            if core is None:continue
            matched+=1
            top3, six=core
            for b3 in (0,1):
                top=top3|(b3<<3)
                for five in product((1,2),repeat=5):
                    lower=[1]*12
                    for p,v in zip(CORE_POS,six): lower[p]=v
                    for p,v in zip(FREE_POS,five):lower[p]=v
                    lower[-1]=r
                    detcalls+=1
                    if det(lower,top)%P==x:
                        ui=sum(((top>>j)&1)<<(3-j) for j in range(4))
                        li=sum((v-1)<<(11-j) for j,v in enumerate(lower))
                        found.append((ui<<12)|li)
    assert len(found)==len(set(found))
    return found,{'root0':len(c0),'root1':len(c1),
                  'candidate_pairs':len(c0)*len(c1),
                  'kappa_pairs':matched,'det_calls':detcalls}

def check():
    X,A=words(),arcs()
    table=core_table()
    assert len(X)==65536 and len(A)==64
    rng=random.Random(20261121)
    ids=sorted(set((0,1,19204,53981,10751,62016,64831,1024,50000)
                   +tuple(rng.sample(range(65536),100))))
    counters=[]
    for idx in ids:
        d0=max_dist(X[idx],A)
        d1=max_dist(X[idx^1],A)
        result,cost=decode(d0,d1,A,table)
        assert result==[idx],(idx,result)
        counters.append(cost)
    metrics={key:{'min':min(c[key] for c in counters),
                  'max':max(c[key] for c in counters),
                  'total':sum(c[key] for c in counters)}
             for key in counters[0]}
    return {'schema':'R284DJ_INDEX_FREE_TWO_READ_RECOVERY_V1',
            'status':'AUTHOR_PROVED / FINITE_CORE_CERTIFIED / SAMPLE_EXECUTED / NOT_REVIEWED',
            'frozen_sha256':FROZEN_SHA,
            'precomputed_kappa_keys':512,
            'kappa_min':min(table),'kappa_max':max(table),
            'possible_core_assignments':512,'free_assignments_per_core_and_r':64,
            'max_inverse_D_candidates_each':128,
            'max_candidate_residue_pairs':16384,
            'tested_samples':len(ids),'sample_seed':20261121,
            'test_indices_sha256':hashlib.sha256(b''.join(i.to_bytes(4,'big') for i in ids)).hexdigest(),
            'all_sample_recoveries_exact':True,
            'sample_costs':metrics,
            'full_domain_correctness_basis':'R284DI all-state two-read injectivity + exact determinant increment + exhaustive 512-core kappa separation + full 64 remainder enumeration + endpoint inverse-D lemma; no all-state decoder run claimed',
            'runtime_lookup':'512-key core table; no 65536-entry x-to-source inverse map',
            'independent_review':'NOT_REVIEWED'}

if __name__=='__main__':
    result=check()
    with open('R284DJ_index_free_two_read_decoder_certificate.json','w',encoding='utf-8') as f:
        json.dump(result,f,ensure_ascii=False,indent=2)
        f.write('\n')
    print(json.dumps({'tested_samples':result['tested_samples'],
                      'all_exact':result['all_sample_recoveries_exact'],
                      'sample_costs':result['sample_costs']}))
