#!/usr/bin/env python3
"""R284DK: exact two-read noise radii and constructive w-flip Port decoder.
Requires the frozen R284CO_spectral_witness_checker.py in this directory.
Python standard library only. No native X6 inference.
"""
from bisect import bisect_left, insort
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product
import json, random
from R284CO_spectral_witness_checker import words, arcs, dist, det, P, D, Z, FROZEN_SHA

CORE=(0,2,3,8,10,11)  # u1,x,y,u3,h,r
FREE=(1,4,6,7,9)     # a,u2,b,z,g; beta1 also free

def near(points):
    order=sorted((a,b,i) for i,(a,b) in enumerate(points))
    window=[]; left=0; bound=10**30
    for pos,(a,b,i) in enumerate(order):
        while left<pos and a-order[left][0]>=bound:
            aa,bb,j=order[left]
            window.pop(bisect_left(window,(bb,j)));left+=1
        k=bisect_left(window,(b-bound+1,-1))
        while k<len(window) and window[k][0]<b+bound:
            bb,j=window[k]
            bound=min(bound,max(a-points[j][0],abs(b-bb)))
            k+=1
        insort(window,(b,i))
    hits=[]
    for pos,(a,b,i) in enumerate(order):
        k=pos+1
        while k<len(order) and order[k][0]-a<=bound:
            aa,bb,j=order[k]
            if max(aa-a,abs(bb-b))==bound:
                hits.append((min(i,j),max(i,j)))
            k+=1
    return bound,sorted(set(hits))

def first_collision(points,k):
    found={}
    for i,(a,b) in enumerate(points):
        key=(a//(1<<k),b//(1<<k))
        if key in found:return [found[key],i]
        found[key]=i
    return None

def kw(top,L):
    u1,a,x,y,u2,w,b,z,u3,g,h,r=L
    return ((D[0]-1-(top&1))*(-x*D[3]+r*x-y*h)
            +(-Z[2]-1-((top>>2)&1))*(u1*D[3]-r*u1+y*u3)
            +(-Z[3]-1-((top>>3)&1))*(-x*u3+u1*h))

def kernel():
    index=defaultdict(list);values=[]
    for b0,b2,b3 in product((0,1),repeat=3):
        top=b0|(b2<<2)|(b3<<3)
        for six in product((1,2),repeat=6):
            L=[1]*12
            for p,v in zip(CORE,six):L[p]=v
            k=kw(top,L);values.append(k)
            for w in (1,2):index[((3-2*w)*k)%P].append((top,six,w))
    assert len(values)==512 and len(set(values))==366
    assert len(index)==732
    assert Counter(map(len,index.values()))==Counter({1:608,2:72,4:36,6:8,8:4,12:4})
    return index,values

def inv_D(d,A):
    assert d>0
    seeds=set()
    for a,w in A:
        seeds.add((a-d)%P);seeds.add((a+w+d)%P)
    return sorted(x for x in seeds if max(dist(x,arc) for arc in A)==d)

def decode(d0,d1,A,index):
    roots0=inv_D(d0,A);roots1=inv_D(d1,A)
    found=[];hit=0;dets=0
    for x in roots0:
        for xp in roots1:
            for partial,six,w in index.get((xp-x)%P,()):
                hit+=1
                for b1 in (0,1):
                    top=partial|(b1<<1)
                    for vals in product((1,2),repeat=5):
                        L=[1]*12
                        for p,v in zip(CORE,six):L[p]=v
                        for p,v in zip(FREE,vals):L[p]=v
                        L[5]=w;dets+=1
                        if det(L,top)%P==x:
                            ui=sum(((top>>j)&1)<<(3-j) for j in range(4))
                            li=sum((v-1)<<(11-j) for j,v in enumerate(L))
                            found.append((ui<<12)|li)
    assert len(found)==len(set(found))
    return found,{'candidate_pairs':len(roots0)*len(roots1),'kernel_matches':hit,'det_calls':dets}

def check():
    X,A=words(),arcs()
    obs=[max(dist(x,arc) for arc in A) for x in X]
    output={'schema':'R284DK_SHARP_ROBUST_W_DECODER_V1',
            'source':'enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py',
            'source_blob_sha1':'b46e0f682b58e47c27094b4bea6fa4e55119a3ee',
            'frozen_sha256':FROZEN_SHA,'states':len(X),'arcs':len(A),
            'status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / SAMPLE_DECODER_EXECUTED / NOT_REVIEWED'}
    for bit in (0,6):
        points=[(obs[i],obs[i^(1<<bit)]) for i in range(len(X))]
        assert len(set(points))==65536
        sep,wits=near(points)
        assert sep=={0:14,6:53}[bit]
        assert len(wits)=={0:4,6:2}[bit]
        k=4 if bit==0 else 5
        assert first_collision(points,k) is None
        collision=first_collision(points,k+1)
        assert collision is not None
        output['flip_'+str(bit)]={
            'min_linf':sep,'nearest_pairs':wits,
            'nearest_pair_signatures':[[list(points[a]),list(points[b])] for a,b in wits],
            'integer_error_radius':(sep-1)//2,
            'largest_safe_floor_power2':1<<k,
            'next_power2_collision':collision,
            'pair_sha256':sha256(b''.join(v.to_bytes(8,'big') for pair in points for v in pair)).hexdigest()}
    index,kvals=kernel()
    for i in range(65536):
        ui,li=divmod(i,4096)
        top=sum(((ui>>(3-j))&1)<<j for j in range(4))
        L=tuple(1+((li>>(11-j))&1) for j in range(12))
        assert (X[i]+(3-2*L[5])*kw(top,L))%P==X[i^64]
    rng=random.Random(20261121)
    test=sorted(set([0,1,19204,53981,10751,62016,64831,1024,50000]
                    +rng.sample(range(65536),100)))
    costs=[]
    for i in test:
        decoded,cost=decode(obs[i],obs[i^64],A,index)
        assert decoded==[i],(i,decoded)
        costs.append(cost)
    output['w_decoder']={
        'core_configurations':512,'distinct_raw_kappa':len(set(kvals)),
        'kappa_range':[min(kvals),max(kvals)],
        'mod_increment_keys':len(index),
        'mod_key_size_histogram':dict(sorted(Counter(map(len,index.values())).items())),
        'all_state_w_increment_verified':65536,
        'sample_seed':20261121,'sample_count':len(test),
        'sample_indices_sha256':sha256(b''.join(i.to_bytes(4,'big') for i in test)).hexdigest(),
        'sample_all_exact':True,
        'sample_total':{v:sum(z[v] for z in costs) for v in costs[0]},
        'sample_max':{v:max(z[v] for z in costs) for v in costs[0]},
        'full_domain_decoder_run':False,
        'full_domain_correctness_basis':'exact w increment and endpoint inverse lemma; enumerate all core and free bits; all-state w two-read injectivity'}
    return output

if __name__=='__main__':
    z=check()
    with open('R284DK_sharp_robust_w_decoder_certificate.json','w',encoding='utf-8') as f:
        json.dump(z,f,indent=2,ensure_ascii=False);f.write('\n')
    print(json.dumps({'flip_0':z['flip_0']['min_linf'],
                      'flip_6':z['flip_6']['min_linf'],
                      'decoder':z['w_decoder']['sample_total']},ensure_ascii=False))
