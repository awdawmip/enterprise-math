#!/usr/bin/env python3
"""Exact Boolean BRC support for conditional X6 signed-port vacancy dynamics.
No physical triadic permission or signed amplitudes are inferred.
"""
from itertools import product, permutations
from math import comb, ceil, log2, factorial
import json
from collections import defaultdict

D=6
V = tuple((axis,sgn) for axis in range(D) for sgn in (-1,1))

def unit(axis, sgn, d=D):
    v=[0]*d;v[axis]=sgn;return tuple(v)
def add(a,v): return tuple(x+y for x,y in zip(a,v))
def norm(a): return sum(map(abs,a))

def two_language(d,h):
    zero=(0,)*len(d)
    states={((),d)}
    words={()}
    for depth in range(h):
        next_states=set()
        for w,r in states:
            for who in (0,1):
                for axis in range(len(d)):
                    for sgn in (-1,1):
                        v=unit(axis,sgn,len(d))
                        z=tuple(x-vv for x,vv in zip(r,v)) if who==0 else add(r,v)
                        if z != zero:
                            nw=w+((who,axis,sgn),)
                            next_states.add((nw,z));words.add(nw)
        states=next_states
    return frozenset(words)

def grid_ball(d,h):
    for tup in product(range(-h,h+1),repeat=d):
        if 0<norm(tup)<=h: yield tup

def lattice_ball_count(d,h):
    return sum(2**k*comb(d,k)*comb(h,k) for k in range(min(h,d)+1))

def two_check(d,h):
    points=list(grid_ball(d,h))
    far=[(h+1,)+(0,)*(d-1), (0,h+1)+(0,)*(d-2),(-(h+2),)+(0,)*(d-1)]
    groups=defaultdict(set)
    signatures={}
    for x in points+far:
        L=two_language(x,h)
        sig=tuple(x) if norm(x)<=h else ('FAR',)
        groups[L].add(str(sig));signatures.setdefault(str(sig),L)
    assert len(groups)==lattice_ball_count(d,h),(d,h,len(groups),lattice_ball_count(d,h))
    assert all(len(z)==1 for z in groups.values()),(d,h,'distinct signature collision')
    return {'dimension':d,'horizon':h,'distinct_languages':len(groups),'expected_minimal_classes':lattice_ball_count(d,h),'checked_displacements':len(points)+len(far),'max_support_words':max(map(len,groups))}

def native_config(perm):
    labels=('LEFT',)+tuple(sorted(perm))+('RIGHT',)
    assign=('LEFT',)+perm+('RIGHT',)
    sites={name:(pos,0,0,0,0,0) for pos,name in enumerate(assign)}
    return labels,sites

def multi_language(labels,sites,h):
    states={((),tuple(sites[s] for s in labels))}
    words={()}
    for depth in range(h):
        next_states=set()
        for w,position in states:
            occ=set(position)
            for idx,s in enumerate(labels):
                for axis,sgn in V:
                    new=add(position[idx],unit(axis,sgn))
                    if new in occ: continue
                    newpositions=list(position);newpositions[idx]=new
                    nw=w+((s,axis,sgn),)
                    next_states.add((nw,tuple(newpositions)));words.add(nw)
        states=next_states
    return frozenset(words)

def alias_check(q):
    mid=tuple('M'+str(i) for i in range(q))
    results1=set();results2=set()
    for perm in permutations(mid):
        labels,places=native_config(perm)
        results1.add(multi_language(labels,places,1))
        results2.add(multi_language(labels,places,2))
    assert len(results1)==1,(q,'L1 differ')
    assert len(results2)==factorial(q),(q,'L2 not full injective',len(results2))
    return {'inner_labels':q,'histories':factorial(q),'L1_classes':len(results1),'L2_classes':len(results2)}

def main():
    twobody=[two_check(2,h) for h in (0,1,2,3)]+[two_check(6,h) for h in (0,1,2)]
    aliases=[alias_check(q) for q in range(1,6)]
    result={'schema':'EM_X6_R14_EXACT_SIGNED_PORT_BRC_V1','result':'PASS',
    'scope':'Boolean support of successful labelled moves, vacancy-only full signed six-axis ports; no native TRIADIC_CLOSURE_E permission',
    'two_body_checks':twobody,'factorial_alias_checks':aliases,
    'X6_closed_form_counts_h_0_6':[lattice_ball_count(6,h) for h in range(7)],
    'theorem_two_body':'C6(h)=sum_(k=0..min(h,6)) 2^k binom(6,k)binom(h,k)',
    'theorem_factorial_alias':'q! same one-event languages but pairwise different two-event languages at all q>=1',
    'unbounded_proofs_not_inferred_from_finite_test':True}
    print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
if __name__=='__main__':main()
