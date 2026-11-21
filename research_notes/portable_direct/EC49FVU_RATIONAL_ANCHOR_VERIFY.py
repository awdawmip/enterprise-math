#!/usr/bin/env python3
"""EC49FVU: exact mod-11 certificate and determinant-one rational anchor theorem.
Frozen BRC16943 -> EC49FVT mathematical inputs. Standard-library exact arithmetic.
"""
from collections import Counter
from fractions import Fraction
from math import gcd

p = 11
U = Fraction(4822040484, 8132285009)
Gamma = Fraction(141024, 1653649)
def red(x):
    return x.numerator * pow(x.denominator, -1, p) % p
u, g, inv = red(U), red(Gamma), pow(637, -1, p)
rows = []
for z in range(p):
    la, lb = (637 - 3*z)*inv % p, u*(1+g*z) % p
    aa, bb = (1-(1-z)*la) % p, (1-(1-z)*lb) % p
    rows.append((z, aa, bb, la, lb))
c, d = -3*inv % p, u*g % p

P10 = {
    (h, n) for h in range(10) for n in range(10)
    if all((pow(aa,h,p)*pow(la,n,p)-pow(bb,h,p)*pow(lb,n,p))
           * pow((la-lb)%p, -1, p) % p
           for z,aa,bb,la,lb in rows if z != 3)
    and (pow(c,h+n,p)-pow(d,h+n,p))*pow((c-d)%p,-1,p) % p
}
assert len(P10)==44 and (1,1) not in P10

def certified(h,n):
    return (h%10,n%10) in P10 and (9*h+10*n)%11 != 0

def direct_projective(h,n):
    for z,aa,bb,la,lb in rows:
        if z==3:
            v=pow(la,n-1,p)*pow(aa,h-1,p)*(n*aa-h*(1-z)*la)%p
        else:
            v=(pow(aa,h,p)*pow(la,n,p)-pow(bb,h,p)*pow(lb,n,p))\
              *pow((la-lb)%p,-1,p)%p
        if v==0:
            return False
    return (pow(c,h+n,p)-pow(d,h+n,p))*pow((c-d)%p,-1,p)%p != 0

assert all(certified(h,n)==direct_projective(h,n)
           for h in range(1,111) for n in range(1,111))
print('FROZEN_PROJECTIVE_DIRECT 12100/12100 PASS; P10=',len(P10))

# A determinant-one anchor produces a unimodular affine line (x,y)+t*(u,v).
# Its mod-10 mask, and the one excluded mod-11 t residue, govern all heights.
masks = {}
counts = Counter()
for u0 in range(10):
    for v0 in range(10):
        for x0 in range(10):
            for y0 in range(10):
                if (u0*y0-v0*x0)%10 not in (1,9):
                    continue
                T=tuple(t for t in range(10)
                        if ((x0+u0*t)%10, (y0+v0*t)%10) in P10)
                counts[len(T)] += 1
                masks[T]=(u0,v0,x0,y0)
assert sum(counts.values())==1440
assert counts == Counter({4:240,5:480,6:480,7:160,8:80})
assert len(masks)==300
print('UNIMODULAR_MOD10 1440/1440 PASS; mask_count=300; hits_distribution=',sorted(counts.items()))

def cyclic_gap(values,period):
    s=sorted(values)
    return max([b-a for a,b in zip(s,s[1:])] + [s[0]+period-s[-1]])

max_step=0
witness=None
step_counts=Counter()
for T,example in masks.items():
    for r in range(11):
        good=[t for t in range(110) if t%10 in T and t%11!=r]
        step=cyclic_gap(good,110)
        step_counts[step]+=1
        if step>max_step:
            max_step=step
            witness=(T,r,example)
assert max_step==8
assert cyclic_gap([t for t in range(110) if t%10 in witness[0] and t%11!=witness[1]],110)==8
assert max(cyclic_gap([t for t in range(110) if t%10 in T],110) for T in masks)==6
print('CRT_CYCLIC_GAP masks_x_exclusions=3300 MAX=8 (no-exclusion MAX=6); distribution=',sorted(step_counts.items()))
print('SHARP_MODULAR_WITNESS',witness)

def det1_denominator(a,b,sgn,H):
    # sgn=-1 -> left; +1 -> right; bh-ad=sgn.
    for q in range(H,max(H-8*b-1,0),-1):
        if (a*q+sgn)%b:
            continue
        h=(a*q+sgn)//b
        if 0<h<q and certified(h,q-h):
            return q
    raise AssertionError(('missing',a,b,sgn,H))

def direct_neighbors(a,b,H):
    x=Fraction(a,b)
    left=right=None
    for q in range(2,H+1):
        for h in range(1,q):
            if gcd(h,q)!=1 or not certified(h,q-h):
                continue
            y=Fraction(h,q)
            if y<x and (left is None or y>left): left=y
            if y>x and (right is None or y<right): right=y
    return left,right

anchors=[(a,b) for b in range(2,13) for a in range(1,b) if gcd(a,b)==1]
checks=0
for a,b in anchors:
    for H in (17*b+1,20*b+7):
        ql=det1_denominator(a,b,-1,H)
        qr=det1_denominator(a,b,+1,H)
        assert H-8*b <= min(ql,qr) <= H
        left,right=direct_neighbors(a,b,H)
        assert left==Fraction(a*ql-1,b*ql),(a,b,H,'left',left,ql)
        assert right==Fraction(a*qr+1,b*qr),(a,b,H,'right',right,qr)
        checks += 1
print('EXACT_ALL_FRACTIONS_CROSSCHECK',checks,'cases; b=2..12, both signs, 2 heights each: PASS')

# Explicit finite examples and one realized max-t-step witness.
for a,b,H in ((1,2,1000),(1,3,1000),(2,3,1000),(3,7,1000),(5,11,1000)):
    ql,qr=det1_denominator(a,b,-1,H),det1_denominator(a,b,1,H)
    print('ANCHOR',f'{a}/{b}', 'H',H, 'certified_anchor',certified(a,b-a),
          'qL',ql,'qR',qr,'H_scaled_bracket', str(Fraction(H,b)*(Fraction(1,ql)+Fraction(1,qr))))

a,b,sgn=3,7,-1
d0=next(q for q in range(1,b+1) if (a*q+sgn)%b==0)
h0=(a*d0+sgn)//b
hits=[t for t in range(110) if certified(h0+a*t,d0-h0+(b-a)*t)]
assert cyclic_gap(hits,110)==8
print('REALIZED_SHARP_STEP anchor=3/7 left', 'd0',d0,'h0',h0,'max_cyclic_step',cyclic_gap(hits,110))
print('THEOREM_STATUS AUTHOR_PROVED / EXACT_FINITE_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED')
print('ALL PASS')
