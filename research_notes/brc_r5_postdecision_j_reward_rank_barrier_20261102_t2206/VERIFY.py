#!/usr/bin/env python3
"""Exact rational verification for R5 affine J-reward rank barrier (author-side)."""
from fractions import Fraction as F
from itertools import permutations, product

ZERO, ONE = F(0), F(1)

def par(which):
    p = dict(k=F(2, 5), lam=F(1, 3),
             alpha=(F(5, 4), F(4, 3), F(3, 2), F(5, 3)))
    if which == "rank4":
        p.update(aB=F(3, 5), aI=F(1, 2), bB=F(7, 12), bI=F(1, 2),
                 uB=F(1, 2), uI=F(1, 4), vB=F(1, 3), vI=F(1, 3))
    else:
        p.update(aB=F(3, 5), aI=F(1, 2), bB=F(2, 5), bI=F(1, 3),
                 uB=F(1), uI=F(1, 2), vB=F(1), vI=F(1, 2))
        p["alpha"] = (F(4, 3), F(5, 3), F(3, 2), F(5, 4))
    return p

def matrix(p):
    return ((ZERO, -p['aB']/8, -p['aI']/8, -p['k']),
            (ZERO, p['bB']/8, p['bI']/8, p['lam']),
            (-F(3,4), (2+p['uB'])/8, (2+p['uI'])/8, ONE),
            (-F(3,4), (2+p['vB'])/8, (2+p['vI'])/8, F(8,9)))

def det(a):
    n = len(a)
    result = ZERO
    for s in permutations(range(n)):
        inversions = sum(s[i] > s[j] for i in range(n) for j in range(i+1,n))
        term = F(-1 if inversions % 2 else 1)
        for i in range(n):
            term *= a[i][s[i]]
        result += term
    return result

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)), ZERO)

def coordinates(x,jB,jI,ks,p):
    b, i = ONE-jB, (ONE-x)*(ONE-jI)
    masses = (F(1,4), (ONE-x)/4, b/8, i/8)
    r = sum((a*w*(ONE-k) for a,w,k in zip(p['alpha'],masses,ks)), ZERO)
    return x,b,i,r

def obs(x,jB,jI,ks,p):
    xx,b,i,r = coordinates(x,jB,jI,ks,p)
    dB,dI = b/8,i/8
    base = F(5,2)-F(3,4)*xx+2*(dB+dI)
    return (ONE-p['aB']*dB-p['aI']*dI-p['k']*r,
            p['bB']*dB+p['bI']*dI+p['lam']*r,
            base+r+p['uB']*dB+p['uI']*dI,
            base+F(8,9)*r+p['vB']*dB+p['vI']*dI)

def affine(u,p):
    m=matrix(p)
    constant=(ONE,ZERO,F(5,2),F(5,2))
    return tuple(c+dot(row,u) for c,row in zip(constant,m))

def transpose(a):
    return tuple(tuple(row[j] for row in a) for j in range(len(a[0])))

def linear_solve(a,b):
    rows=[list(row)+[v] for row,v in zip(a,b)]
    n=len(rows)
    for c in range(n):
        pivot=next((r for r in range(c,n) if rows[r][c]),None)
        if pivot is None: raise ValueError('singular')
        rows[c],rows[pivot]=rows[pivot],rows[c]
        inv=ONE/rows[c][c]
        rows[c]=[z*inv for z in rows[c]]
        for r in range(n):
            if r != c:
                f=rows[r][c]
                rows[r]=[u-f*v for u,v in zip(rows[r],rows[c])]
    return tuple(row[-1] for row in rows)

def full_corners(p):
    for bits in product((ZERO,ONE),repeat=7):
        yield bits,obs(bits[0],bits[1],bits[2],bits[3:],p)

def lr_corners(p):
    for x,y,z in product((ZERO,ONE),repeat=3):
        yield (x,y,z),obs(x,y,y,(z,)*4,p)

def test():
    assertions=0
    def check(expr,label):
        nonlocal assertions
        assertions+=1
        if not expr: raise AssertionError(label)
    p=par('rank4')
    M=matrix(p)
    check(det(M)==F(1,11520),'rank4 det')
    ell=(-ONE,ONE,-ONE,ZERO)
    n=linear_solve(transpose(M),ell)
    check(n==(F(90),F(80),F(220,3),F(-72)),'rank4 exact normal')
    check(tuple(dot(col,n) for col in transpose(M))==ell,'dual normal identity')
    fc=list(full_corners(p)); lc=list(lr_corners(p))
    for bits,o in fc:
        check(o==affine(coordinates(bits[0],bits[1],bits[2],bits[3:],p),p),'full affine')
    for bits,o in lc:
        check(o==affine(coordinates(bits[0],bits[1],bits[1],(bits[2],)*4,p),p),'lr affine')
    fh=max(dot(n,o) for _,o in fc)
    lh=max(dot(n,o) for _,o in lc)
    check(fh-lh==ONE,'rank4 support gap')
    witness=obs(ZERO,ZERO,ONE,(ONE,)*4,p)
    check(dot(n,witness)==fh,'rank4 FULL witness')
    norm=sum(map(abs,n),ZERO)
    check(norm==F(946,3),'dual l1 norm')
    check(p['k']*p['uB']-p['aB']==p['k']*p['uI']-p['aI'], 'P-answer/J-time compensation')
    check(p['bB']-p['lam']*p['uB']==p['bI']-p['lam']*p['uI'], 'Q-answer/J-time compensation')
    print('RANK4 determinant=',det(M),'dual_n=',n,
          'FULL_witness=',witness,'support_gap=',fh-lh,
          'Linf_distance_lower_bound=',ONE/norm)
    q=par('rank3'); N=matrix(q)
    check(det(N)==ZERO,'rank3 det zero')
    minor=det(tuple(tuple(N[r][c] for c in (0,1,3)) for r in (0,1,2)))
    check(minor!=ZERO,'rank3 nonzero 3x3 minor')
    betaB,betaI=q['alpha'][2],q['alpha'][3]
    for row in N:
        check(row[1]*betaI==row[2]*betaB,'J columns weighted equality')
    check(q['aB']!=q['aI'] and q['bB']!=q['bI'] and betaB!=betaI,
          'genuinely distinct sources')
    examples=0
    cases=list(full_corners(q))
    for ix in range(160):
        den=11
        xx=F(ix%11,10) if ix%11<11 else ZERO
        if xx>1: xx=ONE
        jB=F((ix*3)%11,10); jI=F((ix*7)%11,10)
        ks=tuple(F(((ix*(j+2)+3*j)%11),10) for j in range(4))
        cases.append(((xx,jB,jI,*ks),obs(xx,jB,jI,ks,q)))
    for bits,o in cases:
        x,jB,jI,*ks=bits
        ux,b,i,r=coordinates(x,jB,jI,ks,q)
        check(o==affine((ux,b,i,r),q),'rank3 affine')
        den=betaB+betaI*(ONE-x)
        t=(betaB*b+betaI*i)/den
        check(0<=t<=1,'aggregated LR J probability')
        rmax=q['alpha'][0]/4+q['alpha'][1]*(ONE-x)/4+den*t/8
        check(0<=r<=rmax,'R flow bound')
        z=ONE-r/rmax
        check(0<=z<=1,'aggregated LR K probability')
        lo=obs(x,ONE-t,ONE-t,(z,)*4,q)
        check(o==lo,'exact real-policy aggregation')
        examples+=1
    print('RANK3 determinant=',det(N),'nonzero_3x3_minor=',minor,
          'beta=',(betaB,betaI),'exact_real_aggregations=',examples)
    h=par('rank3')
    h['alpha']=(F(4,3),F(5,3),F(3,2),F(4,3))
    # Keeping rank=3 and the observer columns fixed, change only the final
    # IJ positive continuation coefficient; the exact upper-face gap reappears.
    check(matrix(h)==N and det(matrix(h))==ZERO,'same rank3 readout')
    normal=(F(755,33),F(335,11),ZERO,ZERO)
    c=F(17,528)
    check(tuple(dot(col,normal) for col in transpose(N))==
          (ZERO,-6*c,-5*c,ONE),'misaligned dual normal')
    hf=list(full_corners(h)); hl=list(lr_corners(h))
    diff=max(dot(normal,o) for _,o in hf)-max(dot(normal,o) for _,o in hl)
    check(diff==F(1,176),'rank3 misalignment support gap')
    misw=obs(ZERO,ONE,ZERO,(ZERO,)*4,h)
    check(dot(normal,misw)==max(dot(normal,o) for _,o in hf),
          'rank3 misalignment witness')
    print('RANK3_MISALIGNED beta=',h['alpha'][2:], 'normal=',normal,
          'FULL_witness=',misw,'support_gap=',diff)
    print('assertions=',assertions)
    print('PASS_EXACT_R5_AFFINE_J_REWARD_RANK_BARRIER')

if __name__=='__main__':
    test()
