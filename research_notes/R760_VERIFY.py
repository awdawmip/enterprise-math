#!/usr/bin/env python3
"""Exact independent finite checks for R760, candidate auxiliary star-transposition frame."""
from collections import deque
from itertools import combinations
from math import factorial
import json

AXES=tuple(range(1,7)); PAIRS=tuple(combinations(AXES,2)); E=tuple(range(7))

def mult(a,b): return tuple(a[b[i]] for i in E)
def swap(i):
    p=list(E); p[0],p[i]=p[i],p[0]; return tuple(p)
T={i:swap(i) for i in AXES}

def invword(w): return tuple((i,-s) for i,s in reversed(w))
def comm(w,v): return w+v+invword(w)+invword(v)
def nested(i,j,order):
    w=comm(((i,1),),((j,1),))
    for _ in range(2,order): w=comm(w,((i,1),))
    return w

def frame_hom(w):
    g=E
    for i,s in w: g=mult(g,T[i]) # T_i^{-1}=T_i, right composition
    return g

def displacement_area(w):
    x=[0]*7; a={p:0 for p in PAIRS}
    for i,s in w:
        for j in range(1,i): a[(j,i)]+=x[j]*s
        x[i]+=s
    return (tuple(x[1:]),tuple(a.values()))

def poly_mul(a,b,d):
    out={}
    for u,au in a.items():
        for v,bv in b.items():
            uv=u+v
            if len(uv)<=d: out[uv]=out.get(uv,0)+au*bv
    return {k:v for k,v in out.items() if v}

def magnus(w,d):
    p={():1}
    for i,s in w:
        if s==1: f={():1,(i,):1}
        else: f={():1}; f.update({(i,)*j:(-1)**j for j in range(1,d+1)})
        p=poly_mul(p,f,d)
    return p

def closure(gens):
    gi=[g for g in gens]+[tuple(g.index(i) for i in E) for g in gens]
    seen={E}; q=deque([E])
    while q:
        g=q.popleft()
        for h in gi:
            z=mult(g,h)
            if z not in seen: seen.add(z); q.append(z)
    return len(seen)

def verify():
    orders={}; maxword=0; checks=0; area_zero=0
    for d in range(1,7):
        gs=[]
        for i,j in PAIRS:
            w=nested(i,j,d+1)
            maxword=max(maxword,len(w)); checks+=1
            assert len(w)==6*(2**(d-1))-2
            assert magnus(w,d)=={():1}, (d,i,j)
            x,a=displacement_area(w)
            assert x==(0,)*6
            if d>=2: assert a==(0,)*15; area_zero+=1
            g=frame_hom(w)
            assert g!=E
            assert mult(mult(g,g),g)==E
            assert {k for k in E if g[k]!=k}=={0,i,j}
            gs.append(g)
        orders[str(d)]={"word_length":len(w),"nontrivial_pair_witnesses":len(gs),"generated_aux_frame_group":closure(gs)}
        assert orders[str(d)]["generated_aux_frame_group"]==factorial(7)//2
    return {"schema":"R760_FINITE_MAGNUS_FRAME_EXACT_V1","candidate":"X6_SIGNED_WORDS_TO_AUXILIARY_S7_STAR_TRANSPOSITIONS", "max_truncation_degree":6,"degree_pair_tests":checks,"degree_ge_2_zero_area_witnesses":area_zero,"max_constructed_word_length":maxword,"group_sizes_by_truncation_degree":orders,"result":"PASS","scope_note":"Finite verification of algebraically proved all-finite-degree theorem; not native V39/triadic physics."}
if __name__=='__main__': print(json.dumps(verify(),ensure_ascii=False,indent=2))
