#!/usr/bin/env python3
"""R91 finite exact crosscheck, including an unbounded-lattice finite-box tie certificate.
The infinite parameter-strip theorem is proved symbolically in the companion note.
"""
from fractions import Fraction as Q
from itertools import product
from math import lcm
import json

MAX_Q=30
SIGMAS=[Q(1),Q(2),Q(4),Q(49,10)]
TS=[Q(1,2),Q(1),Q(11),Q(13),Q(22),Q(23),Q(24),Q(100)]
S=(10,-5,1); J=(4,-1,0); R=(6,-4,1)

def port(a):
    return max(sum(max(i,0) for i in a),sum(max(-i,0) for i in a))

def gaps(a):
    x,y,z=a
    u=x+3*y+6*z; v=3*x+12*y+30*z; h=7*x+39*y+126*z
    return abs(u),abs(v),abs(h),abs(v-u),abs(h-u),abs(h-v)

def target(t):
    if t<=1: return 1/(1+t)
    if t<=23: return Q(1,2)
    return 12/(1+t)

def expected(t):
    return sorted([S] if t<23 else ([S,J,R] if t==23 else [R]))

def params(s,t):
    k=lcm(s.denominator,t.denominator)
    w=(k,k,int(s*k),int(t*k))
    return k,(w[0]+w[1],w[0]+w[2],w[0]+w[3],
              w[1]+w[2],w[1]+w[3],w[2]+w[3])

def compare(g,k,ds,bound):
    # F(a;(1,1,s,t)) compared to exact bound, with no floating point.
    cm=max(x*k*bound.denominator-bound.numerator*d for x,d in zip(g,ds))
    return -1 if cm<0 else (0 if cm==0 else 1)

def directions(n):
    for a in product(range(-n,n+1),repeat=3):
        if a!=(0,0,0) and next(i for i in a if i)>0 and port(a)<=n:
            yield a

def boundary_box(k,ds):
    # For s=5,t=13 and F<=1/2, all lattice candidates have:
    # |u|<=1, |v|<=3 (v multiple of 3), |h|<=7.
    out=[]
    for u in (-1,0,1):
        for v in (-3,0,3):
            for h in range(-7,8):
                if abs(v-u)>3 or abs(h-u)>7 or abs(h-v)>9:
                    continue
                nx=19*u-8*v+h
                ny=-14*u+7*v-h
                nz=11*u-6*v+h
                if nx%2 or ny%3 or nz%12:
                    continue
                a=(nx//2,ny//3,nz//12)
                if a==(0,0,0) or next(i for i in a if i)<0:
                    continue
                assert compare(gaps(a),k,ds,Q(1,2))==0
                out.append(a)
    return sorted(out)

def run():
    cases=[]
    for s in SIGMAS:
        for t in TS:
            k,ds=params(s,t)
            cases.append(dict(s=s,t=t,k=k,ds=ds,bound=target(t),ties=[],below=0))
    b_k,b_ds=params(Q(5),Q(13))
    b_ties=[];b_below=0;n=0
    for a in directions(MAX_Q):
        n+=1;g=gaps(a)
        for c in cases:
            z=compare(g,c['k'],c['ds'],c['bound'])
            if z<0:c['below']+=1
            if z==0:c['ties'].append(a)
        zb=compare(g,b_k,b_ds,Q(1,2))
        if zb<0:b_below+=1
        if zb==0:b_ties.append(a)
    assert n==47305,n
    out=[]
    for c in cases:
        assert c['below']==0
        assert sorted(c['ties'])==expected(c['t']),(c['s'],c['t'],c['ties'])
        out.append(dict(sigma=str(c['s']),T=str(c['t']),value=str(c['bound']),
                        below=c['below'],ties=[list(x) for x in sorted(c['ties'])]))
    box=boundary_box(b_k,b_ds)
    assert b_below==0
    assert sorted(b_ties)==box
    assert box==sorted([(1,0,0),(5,-4,1),(9,-5,1),(10,-5,1),(15,-9,2)])
    ok,ods=params(Q(6),Q(1,10))
    assert compare(gaps(S),ok,ods,Q(10,11))==0
    assert compare(gaps((14,-9,2)),ok,ods,Q(10,11))==0
    return dict(schema='EM_X6_R91_EXACT_AUTHOR_CHECK_V1',
        q_limit=MAX_Q,unoriented_directions=n,interior_parameter_points=len(cases),
        direction_parameter_checks=n*(len(cases)+1),
        interior_results=out,
        sharp_boundary=dict(sigma='5',T='13',value='1/2',below=b_below,
                            all_lattice_ties=[list(x) for x in box],
                            q_threshold_for_fifth_tie=17),
        outside_strip=dict(sigma='6',T='1/10',value='10/11',
                           tied=[list(S),[14,-9,2]]),
        scope='Finite exact check plus complete moment-box certificate at S=5,T=13; infinite strip follows from companion symbolic proof.')

if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,indent=2))
