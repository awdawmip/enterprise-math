#!/usr/bin/env python3
"""R762CH exact X6 closed-path pair-cocycle and all-frame BRC tests.
Only discrete integer arithmetic; author-side finite checks, not independent review.
"""
from itertools import combinations, permutations, product
from math import comb, ceil, log2
import json, hashlib

AXES=range(6)
PAIRS=list(combinations(AXES,2))

def step(axis,sign):
    a=[0]*6; a[axis]=sign; return tuple(a)
def bloop(i,j):
    return [step(i,+1),step(i,-1),step(j,+1),step(j,-1)]
def lloop(i,j):
    return [step(i,+1),step(j,+1),step(i,-1),step(j,-1)]
def rloop(i,j):
    return [step(j,+1),step(i,+1),step(j,-1),step(i,-1)]
def displacement_and_area(path):
    x=[0]*6; area={(i,j):0 for i,j in PAIRS}
    for d in path:
        for i,j in PAIRS: area[(i,j)] += x[i]*d[j]
        for i in AXES: x[i]+=d[i]
    return tuple(x),area
def component(area,i,j):
    return area[(i,j)] if i<j else -area[(j,i)]
def rooted(area,frame,signs=(1,1,1)):
    return tuple(signs[k]*signs[(k+1)%3]*component(area,frame[k],frame[(k+1)%3]) for k in range(3))
def histogram(path):
    return tuple(sum(1 for d in path if d[i]==s) for i in AXES for s in (-1,1))
def permute_path(path,p):
    out=[]
    for d in path:
        e=[0]*6
        for i in AXES:e[p[i]]=d[i]
        out.append(tuple(e))
    return out
def f(q,a):
    return 2 if a==0 else comb(q,a)

def run():
    tests=0
    for i,j in PAIRS:
        for make,expected in ((bloop,0),(lloop,1),(rloop,-1)):
            p=make(i,j); delta,a=displacement_and_area(p)
            assert delta==(0,)*6
            assert component(a,i,j)==expected
            assert all(a[k]==0 for k in PAIRS if k!=(i,j))
            assert histogram(p)==histogram(bloop(i,j))
            tests+=1
    for pi in permutations(AXES):
        for i,j in PAIRS:
            _,a=displacement_and_area(permute_path(lloop(i,j),pi))
            assert component(a,pi[i],pi[j])==1
            tests+=1
    for frame in combinations(AXES,3):
        for signs in product((-1,1),repeat=3):
            _,a=displacement_and_area(lloop(frame[0],frame[1]))
            assert rooted(a,frame,signs)==(signs[0]*signs[1],0,0)
            tests+=1
    old=(0,1,2); new=(0,1,3)
    _,aB=displacement_and_area(bloop(1,2))
    _,aL=displacement_and_area(lloop(1,2))
    assert rooted(aB,old)==(0,0,0)
    assert rooted(aL,old)==(0,1,0)
    assert rooted(aB,new)==rooted(aL,new)==(0,0,0)
    assert rooted(aB,old)[1]==0 and rooted(aL,old)[1]==1
    tests+=1
    qrange=list(range(2,11))
    for q in qrange:
        base=[]
        for i,j in PAIRS:base.extend(bloop(i,j)*q)
        dx,baseline=displacement_and_area(base)
        assert dx==(0,)*6 and len(base)==60*q
        assert all(v==0 for v in baseline.values())
        common=histogram(base)
        assert all(common[2*i]==common[2*i+1]==5*q for i in AXES)
        for i,j in PAIRS:
            w=[]
            for a,b in PAIRS:
                if (a,b)==(i,j):w.extend(bloop(a,b)*(q-1)+lloop(a,b))
                else:w.extend(bloop(a,b)*q)
            disp,area=displacement_and_area(w)
            assert disp==dx and histogram(w)==common and len(w)==len(base)
            assert area[(i,j)]==1
            assert all(v==0 for pair,v in area.items() if pair!=(i,j))
            tests+=1
        weights=[f(q,a) for a in range(q)]
        assert sum(weights)==2**q
        assert q**15>0 and (2**q)**15==2**(15*q)
        tests+=1
    for q in (2,3,5):
        samples=[tuple((i*3+1)%q for i in range(15)),tuple((i*i+2)%q for i in range(15))]
        for a in samples:
            w=[]
            for t,(i,j) in enumerate(PAIRS):
                w.extend(bloop(i,j)*(q-a[t])+lloop(i,j)*a[t])
            delta,area=displacement_and_area(w)
            assert delta==(0,)*6
            assert histogram(w)==tuple(5*q for _ in range(12))
            assert len(w)==60*q
            assert tuple(area[k]%q for k in PAIRS)==a
            tests+=1
    evidence={
        'id':'R762CH','model':'P000-compatible six-axis primitive closed paths with prospective all-rooted-pair readouts',
        'result':'For any set E of unordered axis pairs, the exact mod-q pair-cocycle observer quotient on the common loop-slot coarse fibre has q^|E| classes and ceil(log2(q^|E|)) bits.',
        'global_pairs':15,'permutations_checked':720,'pair_covariance_checks':720*15,
        'signed_frames_checked':20*8,'q_range':qrange,'tests_passed':tests,
        'q2':{'classes':2**15,'bits':15,'ordered_source_histories':2**30},
        'q3':{'classes':3**15,'bits':24,'ordered_source_histories':2**45},
        'q7':{'classes':7**15,'bits':ceil(log2(7**15)),'ordered_source_histories':2**105},
        'one_port_weight':'f_q(0)=2; f_q(a)=binomial(q,a) for 1<=a<q',
        'total_all_pair_weight':'2^(15q)',
        'no_go':'B23 and L23 have old roots 000 and 010; after 3->4 both path-area roots 000; after reversing 4->3 their old area roots re-emerge; dropping dormant pair area is not all-future safe.',
        'scope':'conditional mathematical observer and candidate event interface; native TRIADIC_CLOSURE_E and V17/V29/V39 licensing not established',
        'review':'NOT_REVIEWED'
    }
    return evidence

if __name__=='__main__':
    print(json.dumps(run(),indent=2,ensure_ascii=False,sort_keys=True))
