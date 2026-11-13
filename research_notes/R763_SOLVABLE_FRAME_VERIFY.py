#!/usr/bin/env python3
"""R763: exact finite tests for the auxiliary F_m -> S_(m+1) star frame."""
from collections import deque
from itertools import combinations
from math import factorial
import json

def mul(a,b):
    return tuple(a[b[i]] for i in range(len(a)))

def inv(a):
    return tuple(a.index(i) for i in range(len(a)))

def star(n,i):
    p=list(range(n));p[0],p[i]=p[i],p[0];return tuple(p)

def cyc(n,*a):
    p=list(range(n))
    for x,y in zip(a,a[1:]+a[:1]):p[x]=y
    return tuple(p)

def comm(a,b):
    return mul(mul(mul(a,b),inv(a)),inv(b))

def even(p):
    return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2==0

def group(gens,n):
    ident=tuple(range(n));ext=list(gens)+[inv(g) for g in gens]
    seen={ident};q=deque([ident])
    while q:
        g=q.popleft()
        for h in ext:
            z=mul(g,h)
            if z not in seen:seen.add(z);q.append(z)
    return seen

def derived_word(i,j,r,m):
    """A raw signed word W_r(0,i,j) in the r-th derived subgroup."""
    assert r>=1 and m>=4 and i!=j and i>0 and j>0
    if r==1:return (i,j,-i,-j)
    k,l=next((k,l) for k in range(1,m+1) for l in range(1,m+1) if len({i,j,k,l})==4)
    u=derived_word(i,k,r-1,m);v=derived_word(j,l,r-1,m)
    return u+v+tuple(-x for x in reversed(u))+tuple(-x for x in reversed(v))

def phi(w,m):
    n=m+1;g=tuple(range(n))
    for s in w:g=mul(g,star(n,abs(s)))
    return g

def verify():
    rows=[]
    for m in range(2,7):
        n=m+1;t=[star(n,i) for i in range(1,n)]
        S=group(t,n)
        assert len(S)==factorial(n)
        triples=[cyc(n,*x) for tup in combinations(range(n),3)
                 for x in (tup,(tup[0],tup[2],tup[1]))]
        A=group(triples,n)
        assert len(A)==factorial(n)//2
        assert all(even(p) for p in A)
        assert all((p in A)==even(p) for p in S)
        triple_comm=[comm(a,b) for a in triples for b in triples]
        A_derived=group(set(triple_comm),n)
        sizes={3:1,4:4,5:60,6:360,7:2520}
        assert len(A_derived)==sizes[n]
        witness=[]
        if n>=5:
            assert comm(cyc(n,0,1,3),cyc(n,0,2,4))==cyc(n,0,1,2)
            assert A_derived==A
            for r in range(1,5):
                w=derived_word(1,2,r,m)
                assert len(w)==4**r
                assert phi(w,m)==cyc(n,0,1,2)
                witness.append({'derived_level':r,'raw_length':len(w),
                                'frame_three_cycle':list(phi(w,m))})
        rows.append({'m_axes':m,'n_aux_labels':n,
                     'S_n_size':len(S),'A_n_size':len(A),
                     'derived_A_n_size':len(A_derived),'A_n_perfect':A_derived==A,
                     'parity_fiber_min_states':len(A),
                     'parity_fiber_fixed_bits':(len(A)-1).bit_length(),
                     'unrestricted_fiber_max_states':len(S),
                     'unrestricted_fiber_fixed_bits':(len(S)-1).bit_length(),
                     'constructive_derived_word_checks':witness})
    return {'schema':'R763_SOLVABLE_OBSERVER_FRAME_RESIDUAL_EXACT_V1',
            'candidate':'SIGNED_X6_PATH_FREE_GROUP_STAR_FRAME',
            'input':'m=2..6; complete S_(m+1), A_(m+1), and commutator subgroup checks',
            'result':'PASS','rows':rows,
            'claim_scope':'Finite group checks; general solvable-observer theorem is algebraic.',
            'native_interface':'UNESTABLISHED_P000_TRIADIC_CLOSURE_OR_V29_V39_MAP'}

if __name__=='__main__':print(json.dumps(verify(),indent=2,ensure_ascii=False))
