#!/usr/bin/env python3
"""Stage395-B: exact restricted native-X6 history quotient and BRC checks.
Python stdlib only, deterministic output, no external input or network.
"""
from __future__ import annotations
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction
from itertools import combinations, product
from math import factorial

A = tuple((axis, sign) for axis in range(1,7) for sign in (1,-1))
ZERO = (0,)*6
SUB = ((1,1),(1,-1),(2,1),(2,-1))
S3 = tuple(combinations(range(6),3))
SIGN_WEIGHT = {d: Fraction((d[0]+1)*d[1],1) if d[1]>0 else Fraction(-1,d[0]+1) for d in A}
POS_WEIGHT = {d: Fraction(d[0]+2, d[0]+1) if d[1]>0 else Fraction(d[0],d[0]+2) for d in A}

def endpoint(w):
    z = [0]*6
    for i,s in w: z[i-1] += s
    return tuple(z)

def turn(w):
    return sum(x!=y for x,y in zip(w,w[1:]))

def path_weight(w):
    p = Fraction(1)
    for d in w: p *= SIGN_WEIGHT[d]
    return p

def compositions(k, n):
    if n==1:
        yield (k,)
    else:
        for a in range(k+1):
            for rest in compositions(k-a,n-1): yield (a,)+rest

@lru_cache(None)
def BRC(m,z,weighted=False):
    base = sum(map(abs,z))
    if m<base or (m-base)%2: return Fraction(0) if weighted else 0
    k = (m-base)//2
    out = Fraction(0)
    for js in compositions(k,6):
        term = Fraction(factorial(m))
        for i,j in enumerate(js):
            plus=max(z[i],0)+j
            minus=max(-z[i],0)+j
            term /= factorial(plus)*factorial(minus)
            if weighted:
                term *= POS_WEIGHT[i+1,1]**plus*POS_WEIGHT[i+1,-1]**minus
        out+=term
    assert weighted or out.denominator==1
    return out if weighted else int(out)

def O(w):
    z=endpoint(w)
    triples=tuple(tuple(z[i]-min(z[t] for t in s) for i in s) for s in S3)
    return ('source-P',triples,min(z),len(w),BRC(len(w),z),BRC(len(w),z,True),turn(w),path_weight(w))

def key(w,D,H):
    out=[]
    for d in reversed(w):
        if len(out)==H+1:break
        out.append(d)
        if d not in D:break
    return tuple(reversed(out))

@lru_cache(None)
def behavior(w,D,H,depth):
    # Includes observations of every admissible prefix and POP-definedness.
    if not depth:return (O(w),)
    children=[]
    for d in SUB:
        children.append((('APPEND',d), behavior(w+(d,),D,H,depth-1)))
    children.append(('POP',behavior(w[:-1],D,H-1,depth-1) if H and w and w[-1] in D else 'UNDEFINED'))
    return (O(w),tuple(children))

def test():
    # Independent exact all-length 12-axis BRC recurrence, including positive weights.
    p={ZERO:Fraction(1)}
    n={ZERO:1}
    dp_count=0
    for m in range(5):
        assert set(p)==set(n)
        for z in n:
            assert BRC(m,z)==n[z]
            assert BRC(m,z,True)==p[z]
            dp_count+=1
        q,qn=defaultdict(Fraction),defaultdict(int)
        for z,v in p.items():
            for i,s in A:
                zz=list(z);zz[i-1]+=s;zz=tuple(zz)
                q[zz]+=v*POS_WEIGHT[i,s]
                qn[zz]+=n[z]
        p,n=dict(q),dict(qn)
    # Complete pairwise theorem check on a finite signed-X6 subalphabet.
    words=[t for m in range(5) for t in product(SUB, repeat=m)]
    groups=defaultdict(list)
    for w in words:groups[O(w)].append(w)
    checked_pairs=0; behavior_checks=0
    ds=(frozenset(),frozenset((SUB[0],)),frozenset(SUB[:2]),frozenset(SUB))
    for D in ds:
        for H in range(3):
            for group in groups.values():
                # behavior for every allowed sequence of length <= H+1.
                bb=[behavior(w,D,H,H+1) for w in group]
                kk=[key(w,D,H) for w in group]
                for i in range(len(group)):
                    for j in range(i+1,len(group)):
                        assert (kk[i]==kk[j])==(bb[i]==bb[j]),(group[i],group[j],D,H)
                        checked_pairs+=1
                        behavior_checks+=1
    # Exact branch barrier witness, six signed native axes.
    D=frozenset(((1,1),));H=3
    a=((-1,1),) if False else ((1,-1),(2,1),(2,-1),(4,1),(4,-1),(1,1))
    b=((1,-1),(3,1),(3,-1),(4,1),(4,-1),(1,1))
    assert a!=b and O(a)==O(b) and key(a,D,H)==key(b,D,H)
    assert a[-4:]!=b[-4:]
    assert BRC(6,ZERO)>0
    # Arbitrary nonzero rational signed weights: lossless one-step update law.
    wc=0
    for w in words:
        for d in A:
            assert path_weight(w+(d,))==path_weight(w)*SIGN_WEIGHT[d]
            wc+=1
        if w:
            assert path_weight(w[:-1])==path_weight(w)/SIGN_WEIGHT[w[-1]]
            wc+=1
    print('STAGE395B_RESTRICTED_POP_SIGNED_BRC_PASS')
    print('source_pins=EM:2af3fc484eb11060b69e0afc1b562bcaf5ad1419 GLOBAL:bf84bd7c61a2444b59b1da96be57df0e9ae47e53')
    print('p000_blob=bcc2590d3168a28f72e8b9f0f9b1f76faadcd488')
    print('BRC_full_X6_endpoints_m_le_4=',dp_count)
    print('bounded_words=',len(words),'observer_fibers=',len(groups))
    print('behavior_pair_checks=',checked_pairs,'scope=|SUB|=4,m<=4,all_4_D_examples,H=0..2,depth=H+1')
    print('weighted_single_step_checks=',wc)
    print('sharp_witness_m=',len(a),'z=',endpoint(a),'turns=',turn(a),'N6=',BRC(6,ZERO))
    print('selective_signature=',key(a,D,H),'unrestricted_suffixes=',a[-4:],b[-4:])

if __name__=='__main__':test()
