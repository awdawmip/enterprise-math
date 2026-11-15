#!/usr/bin/env python3
"""Exact finite certificates for the R5 mixed-core separated-star theorem.
Python standard library; exact bit arithmetic and exhaustive minimum set cover.
"""
from itertools import product
from functools import lru_cache
import json

O = tuple(frozenset(map(int, x)) for x in ('0125','0135','0235','0245','0246'))
A = tuple((frozenset(map(int,c)), s) for c,s in
          [('1235',1),('1245',1),('1246',1),('1345',0),('1346',0)])
AB = A + ((frozenset(map(int,'1236')),1),)

def core_distance(a,b): return len(a-b)
def h(x,y): return (x^y).bit_count()
def rho(new, old):
    C,s,v = new
    j,t,u = old
    return core_distance(C,O[j]) + (s!=t) + h(v,u)

def old_space(X):
    return [(j,t,u) for u in sorted(X) for j in range(5) for t in (0,1)]
def targets(new_cores,Y):
    return [(C,s,y) for y in sorted(Y) for C,s in new_cores]
def masks(X,Y,core_set):
    T=targets(core_set,Y)
    raw=[]
    for o in old_space(X):
        mask=sum(1<<i for i,n in enumerate(T) if rho(n,o)<=2)
        if mask:raw.append((o,mask))
    return T,raw

def exact_min_cover(T, raw):
    """Entire finite set-cover space, memoized and branching on a target."""
    universe=(1<<len(T))-1
    mask_to_old={}
    for o,mask in raw:
        mask_to_old.setdefault(mask,o)
    choices=list(mask_to_old.items())
    options=[[j for j,(m,o) in enumerate(choices) if m>>i&1]
             for i in range(len(T))]
    assert all(options)
    @lru_cache(None)
    def solve(uncovered):
        if not uncovered:return (0,())
        rarest=None
        for i in range(len(T)):
            if uncovered>>i&1:
                if rarest is None or len(options[i])<len(rarest):
                    rarest=options[i]
        best=(len(T)+1,())
        for j in sorted(rarest,
                        key=lambda j:(choices[j][0]&uncovered).bit_count(),
                        reverse=True):
            mask,_=choices[j]
            k,idx=solve(uncovered&~mask)
            if 1+k<best[0]:best=(1+k,(j,)+idx)
        return best
    number,indices=solve(universe)
    witness=[choices[j][1] for j in indices]
    assert len(set(witness))==number
    assert all(any(rho(n,o)<=2 for o in witness) for n in T)
    return number,witness

def library(Y, center=None):
    if center is None:
        return [(1,0,y) for y in Y]+[(0,1,y) for y in Y]
    return [(1,0,y) for y in Y]+[(0,1,center),(4,1,center)]

out={'core_distances':
     {''.join(map(str,sorted(C))):[core_distance(C,o) for o in O]
      for C,s in AB},
     'cube_d3':{}, 'two_stars':{}}
assert out['core_distances']=={
    '1235':[1,1,1,2,3], '1245':[1,2,2,1,2],
    '1246':[2,3,3,2,1], '1345':[2,1,2,2,3],
    '1346':[3,2,3,3,2], '1236':[2,2,2,3,2]}

Y={1,2,4}
rows=[]
for mask in range(1<<8):
    X={i for i in range(8) if mask>>i&1}
    if not Y<=X:continue
    T,raw=masks(X,Y,A)
    ka,wa=exact_min_cover(T,raw)
    assert ka==(5 if 0 in X else 6)
    T2,raw2=masks(X,Y,AB)
    kab,wab=exact_min_cover(T2,raw2)
    assert kab==6
    rows.append({'mask':mask,'ka':ka,'kab':kab})
out['cube_d3']={
    'old_languages':len(rows),
    'zero_present':sum(bool(x['mask']&1) for x in rows),
    'count_by_ka':{str(k):sum(x['ka']==k for x in rows) for k in (5,6)}}
assert out['cube_d3']=={
    'old_languages':32,'zero_present':16,
    'count_by_ka':{'5':16,'6':16}}

centers=[0,31] # Q6: Hamming separation five
stars=[{c^(1<<i) for i in range(3)} for c in centers]
Yall=set.union(*stars)
assert len(Yall)==6
assert min(h(u,v) for u in stars[0] for v in stars[1])>=3
for presence in product((False,True),repeat=2):
    X=Yall|{centers[i] for i,p in enumerate(presence) if p}
    for core_set in (A,AB):
        _,raw=masks(X,Yall,core_set)
        for o,cover_mask in raw:
            near=[i for i,S in enumerate(stars)
                  if min(h(o[2],v) for v in S)<=1]
            assert len(near)<=1
    expected_a=sum(len(stars[i])+
                   (2 if presence[i] else len(stars[i]))
                   for i in range(2))
    expected_ab=2*len(Yall)
    L=sum((library(S,centers[i] if presence[i] else None)
           for i,S in enumerate(stars)),[])
    assert len(L)==expected_a
    assert all(any(rho(n,o)<=2 for o in L)
               for n in targets(A,Yall))
    Lab=sum((library(S) for S in stars),[])
    assert len(Lab)==expected_ab
    assert all(any(rho(n,o)<=2 for o in Lab)
               for n in targets(AB,Yall))
    out['two_stars'][str(presence)]={
        'old_suffixes':len(X),'a_library':expected_a,
        'ab_library':expected_ab,
        'a_cover_certificate':True,'ab_cover_certificate':True}

# All 3^4 - 2^4 = 65 nonempty nested X,Y in the two-bit cube.
count=0
for labels in product((0,1,2),repeat=4):
    X={i for i,v in enumerate(labels) if v>=1}
    Y={i for i,v in enumerate(labels) if v==2}
    if not Y:continue
    T,raw=masks(X,Y,AB)
    Lab=[(1,0,y) for y in Y]+[(0,1,y) for y in Y]
    assert len(Lab)==2*len(Y)
    assert all(any(rho(n,o)<=2 for o in Lab) for n in T)
    for y in Y:
        n1=next(n for n in T if n[0]==frozenset((1,3,4,6)) and n[2]==y)
        n2=next(n for n in T if n[0]==frozenset((1,2,3,6)) and n[2]==y)
        w1=[o for o,m in raw if rho(n1,o)<=2]
        w2=[o for o,m in raw if rho(n2,o)<=2]
        assert w1 and w2
        assert all(o[1]==0 and o[2]==y for o in w1)
        assert all(o[1]==1 and o[2]==y for o in w2)
    count+=1
assert count==65
out['all_two_bit_language_pairs']={
    'count':count,'ab_exact_min_verified_via_forced_targets':True}
print(json.dumps(out,sort_keys=True,ensure_ascii=False,indent=2))
print('PASS_R5_SEPARATED_STAR_AND_AB_UNIVERSAL')
