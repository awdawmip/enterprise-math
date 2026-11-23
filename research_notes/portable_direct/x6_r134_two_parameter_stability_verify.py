#!/usr/bin/env python3
"""Exact finite certificate for conditional BRC six-pair Port-10 R134.

Only integer/Fraction arithmetic; no physical X6/time evolution is computed.
"""
from fractions import Fraction as Q
from itertools import combinations, product

PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
BANK18 = (
    (1,0,0),(0,2,-1),(1,-3,1),(2,-3,1),(3,-1,0),
    (1,3,-1),(3,-4,1),(4,-1,0),(3,2,-1),(4,-4,1),
    (5,-1,0),(5,-4,1),(6,-1,0),(3,-7,2),(6,-4,1),
    (7,-1,0),(7,2,-1),(9,-5,1),
)

def port(a):
    return max(sum(max(t, 0) for t in a), sum(max(-t, 0) for t in a))

def gaps(a):
    x,y,z = a
    h = (0, x+3*y+6*z, 3*x+12*y+30*z, 7*x+39*y+126*z)
    return tuple(abs(h[j]-h[i]) for i,j in PAIRS)

def caps(w):
    return tuple(w[i]+w[j] for i,j in PAIRS)

def leq(a,b):
    return all(x <= y for x,y in zip(a,b))

def first_sign_positive(a):
    return next(t for t in a if t) > 0

POP = sorted(a for a in product(range(-10,11),repeat=3)
             if 0 < port(a) <= 10 and first_sign_positive(a))
assert len(POP) == 1935
assert len(BANK18) == 18 and len(set(BANK18)) == 18
assert all(a in POP for a in BANK18)
assert all(any(leq(gaps(b),gaps(a)) for b in BANK18) for a in POP)
E20 = sorted(a for a in POP if not any(
    all(2*x >= 3*y for x,y in zip(gaps(a),gaps(b))) for b in BANK18))
assert len(E20) == 20
assert sum(a not in E20 for a in POP) == 1915

def score(a,w):
    return max(Q(g,s) for g,s in zip(gaps(a),caps(w)))

def base_near(w):
    eta = min(score(b,w) for b in BANK18)
    return tuple(a for a in E20 if 2*score(a,w) < 3*eta)

def affine(a,j,k,A,C):
    # L(B,D) = 9*s_j(B,D) - 2*g_j(a)*s_k(B,D)
    g = gaps(a)[j]
    s0, sB, sD = (caps(w) for w in ((A,0,C,0),(0,1,0,0),(0,0,0,1)))
    return tuple(Q(9*u-2*g*v) for u,v in zip(
        (s0[j],sB[j],sD[j]),(s0[k],sB[k],sD[k])))

def eval_line(L,xy):
    B,D=xy
    return L[0]+L[1]*B+L[2]*D

def vertices(box, extra):
    lo,hi,dl,dh=map(Q,box)
    boundary=((-lo,1,0),(hi,-1,0),(-dl,0,1),(dh,0,-1), *extra)
    out=set()
    for L,M in combinations(boundary,2):
        a,b,c=map(Q,L);d,e,f=map(Q,M)
        det=b*f-c*e
        if det == 0:continue
        B=(c*d-a*f)/det
        D=(a*e-b*d)/det
        if all(eval_line(T,(B,D))>=0 for T in boundary):out.add((B,D))
    return tuple(sorted(out))

def certify(title,w0,k,box,basis,expected,facet_witnesses):
    A,_,C,_=w0
    near=base_near(w0)
    assert len(near)==8
    assert min(score(b,w0) for b in BANK18)==Q(3,caps(w0)[k])
    B0,B1,D0,D1=box
    corners=[(A,B,C,D) for B in (B0,B1) for D in (D0,D1)]
    assert all(all(s>0 for s in caps(w)) for w in corners)
    anchor=(6,-1,0)
    assert all(gaps(anchor)[j]*caps(w)[k] <= 3*caps(w)[j]
               for w in corners for j in range(6))
    # One fixed witnessing pair for every bank row (on all four corners).
    bank_witness={b:next((j for j in range(6) if all(
        gaps(b)[j]*caps(w)[k]>=3*caps(w)[j] for w in corners)),None)
                  for b in BANK18}
    assert all(j is not None for j in bank_witness.values())
    # One fixed exclusion pair for each outsider from the 20-row envelope.
    outsider_witness={a:next((j for j in range(6) if all(
        2*gaps(a)[j]*caps(w)[k]>=9*caps(w)[j] for w in corners)),None)
                      for a in E20 if a not in near}
    assert len(outsider_witness)==12
    assert all(j is not None for j in outsider_witness.values())
    poly=vertices(box,basis)
    assert poly == tuple(sorted((Q(x),Q(y)) for x,y in expected)),(poly,expected)
    assert all(eval_line(L,(Q(w0[1]),Q(w0[3])))>0 for L in basis)
    # All 48 interior-member inequalities follow from the stated bases
    # and box. A zero face must lie inside a face of a stated *strict* base.
    vanish_counts={}
    for a in near:
        for j in range(6):
            L=affine(a,j,k,A,C)
            vals=[eval_line(L,p) for p in poly]
            assert min(vals)>=0,(title,a,j,vals)
            zeros=[p for p,v in zip(poly,vals) if v==0]
            assert (not zeros or any(all(eval_line(H,p)==0 for p in zeros)
                                      for H in basis)),(title,a,j,zeros)
            if zeros:vanish_counts[(a,j)]=len(zeros)
    # Each listed strict base is forced by a specific near row/pair,
    # hence failure at equality removes that row from strict nearness.
    for L,(a,j) in zip(basis,facet_witnesses):
        H=affine(a,j,k,A,C)
        ref=tuple(map(Q,L))
        t=next((i for i in range(3) if ref[i]),None)
        assert t is not None
        multiplier=H[t]/ref[t]
        assert multiplier>0 and H==tuple(multiplier*z for z in ref), (title,L,a,j,H)
        assert a in near
        assert any(eval_line(L,p)==0 for p in poly)
    print(title, 'PASS', 'population',len(POP),'bank',len(BANK18),
          'envelope',len(E20),'near',len(near),'vertices',len(poly),
          'facet_planes',len(basis),'vanishing_comparisons',len(vanish_counts))
    print('  vertices:', ' '.join('(%s,%s)' % p for p in poly))
    print('  bank witness indices:', [bank_witness[b] for b in BANK18])
    print('  outsider witness indices:', [(a,outsider_witness[a]) for a in sorted(outsider_witness)])

certify('CENTER_I', (136,8,176,185), 0, (0,20,150,220),
        ((20,-1,0),(-544,-1,3),(-1496,-20,9)),
        ((0,220),(0,Q(544,3)),(8,184),(20,Q(632,3)),(20,220)),
        (((1,3,-1),1),((1,0,0),4),((7,-1,0),2)))
certify('CENTER_II', (722,465,240,48), 5, (350,600,1,200),
        ((243,0,-5),(-2640,9,-20)),
        ((350,1),(350,Q(51,2)),(Q(1204,3),Q(243,5)),
         (600,1),(600,Q(243,5))),
        (((3,3,-1),1),((7,-8,2),3)))
print('R134 TWO-PARAMETER EXACT NONRADIAL CHAMBER CERTIFICATE PASS')
