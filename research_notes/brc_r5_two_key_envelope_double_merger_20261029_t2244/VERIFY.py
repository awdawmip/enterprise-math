#!/usr/bin/env python3
"""Exact rational verification for the two-key envelope / double-merger lemma.
No nonstandard dependencies. All outcomes use Fraction, not floats.
"""
from fractions import Fraction as F
from itertools import product

HALF=F(1,2)
BIT_KERNEL={
    ('via','P'):F(1,4), ('via','Q'):F(3,4),
    ('bypass','P'):F(3,4), ('bypass','Q'):F(1,4),
}
NEW_KERNEL={
    ('via','P'):F(1,4), ('via','Q'):F(1,16),
    ('bypass','P'):F(3,8), ('bypass','Q'):F(1,32),
}
W=(F(1),F(-8),F(1),F(1))

def obs(choices,mode):
    """(e_P,e_Q,T_P,T_Q) for all strictly positive stochastic kernels."""
    ans={law:[F(0),F(0)] for law in ('P','Q')}
    for law in ('P','Q'):
        for source in ('via','bypass'):
            mass=HALF
            k=choices[0]
            if source=='via' and not k:
                ans[law][1]+=mass
                continue
            l=choices[1] if mode=='LR' else choices[1 if source=='via' else 2]
            if not l:
                ans[law][1]+=mass*2
                continue
            p=BIT_KERNEL[(source,law)]
            for bit,prob in ((0,1-p),(1,p)):
                r=F(3) if (source=='via' and bit==0) or (source=='bypass' and bit==1) else F(1,3)
                if mode=='LR':
                    z=choices[3] if r==3 else choices[2]
                else:
                    z=choices[3+(0 if source=='via' else 2)+bit]
                branch_mass=mass*prob
                if not z:
                    err=F(bit); t=3
                else:
                    err=NEW_KERNEL[(source,law)];t=4
                ans[law][0]+=branch_mass*err
                ans[law][1]+=branch_mass*t
    return (ans['P'][0],ans['Q'][0],ans['P'][1],ans['Q'][1])

def dot(w,o):
    return sum((u*v for u,v in zip(w,o)),F(0))


def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]

def minus(a,b):
    return (a[0]-b[0],a[1]-b[1])

def plus(*xs):
    return (sum(x[0] for x in xs),sum(x[1] for x in xs))

def integer_hull(points):
    points=sorted(set(points))
    if len(points)<=1:return points
    lower=[];upper=[]
    for p in points:
        while len(lower)>1 and cross(minus(lower[-1],lower[-2]),minus(p,lower[-1]))<=0:
            lower.pop()
        lower.append(p)
    for p in reversed(points):
        while len(upper)>1 and cross(minus(upper[-1],upper[-2]),minus(p,upper[-1]))<=0:
            upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]

def in_integer_hull(point,points):
    polygon=integer_hull(points)
    if len(polygon)==1:return point==polygon[0]
    if len(polygon)==2:
        return cross(minus(polygon[1],polygon[0]),minus(point,polygon[0]))==0 and all(
            min(a,b)<=t<=max(a,b) for t,a,b in zip(point,polygon[0],polygon[1]))
    return all(cross(minus(polygon[(i+1)%len(polygon)],polygon[i]),minus(point,polygon[i]))>=0
               for i in range(len(polygon)))

def geometry_grid_test():
    values=list(product(range(-2,3),repeat=2))
    passing=0
    for X,Y,Z in product(values,repeat=3):
        corners=((0,0),Y,X,plus(X,Y,Z))
        if not in_integer_hull(plus(X,Y),corners):continue
        if not in_integer_hull(plus(X,Z),corners):continue
        passing+=1
        rank2=any(cross(a,b)!=0 for a,b in ((X,Y),(X,Z),(Y,Z)))
        if rank2:
            assert cross(Y,Z)==0 and Y[0]*Z[0]+Y[1]*Z[1]>=0,(X,Y,Z)
    return len(values)**3,passing

def main():
    for table in (BIT_KERNEL, NEW_KERNEL):
        assert all(F(0)<p<F(1) for p in table.values())
    # At x=y=1: m_3 receives via(bit0),bypass(bit1); m_1/3 receives the complementary origins.
    for r,branches in ((F(3),(('via',0),('bypass',1))),
                       (F(1,3),(('via',1),('bypass',0)))):
        for origin,bit in branches:
            mp=HALF*(BIT_KERNEL[(origin,'P')] if bit else (1-BIT_KERNEL[(origin,'P')]))
            mq=HALF*(BIT_KERNEL[(origin,'Q')] if bit else (1-BIT_KERNEL[(origin,'Q')]))
            assert mp>0 and mq>0 and mp/mq==r
    # Continuation at m strictly increases W-cost for every source/bit and both measures.
    for origin,bit in product(('via','bypass'),(0,1)):
        pp=NEW_KERNEL[(origin,'P')];qq=NEW_KERNEL[(origin,'Q')]
        assert (1+pp-bit)>0 and (1-8*qq+8*bit)>0
    lr=[(bits,obs(bits,'LR')) for bits in product((0,1),repeat=4)]
    full=[(bits,obs(bits,'FULL')) for bits in product((0,1),repeat=7)]
    lrmin=min(dot(W,o) for _,o in lr)
    fullmin=min(dot(W,o) for _,o in full)
    assert len(lr)==16 and len(full)==128
    assert lrmin==F(5,2),lrmin
    assert fullmin==F(17,8),fullmin
    witness=(1,1,0,0,0,0,0)
    ow=obs(witness,'FULL')
    assert ow==(F(1,8),F(3,8),F(5,2),F(5,2)),ow
    assert dot(W,ow)==fullmin
    assert all(8*dot(W,o)>=20 for _,o in lr)
    gap=lrmin-fullmin
    assert gap==F(3,8)
    gridtotal,gridpass=geometry_grid_test()
    print(f'GEOMETRY_GRID={gridtotal};HULL_EQUAL={gridpass};VIOLATIONS=0')
    print('MODEL_POSITIVE_KERNELS=PASS')
    print('SECOND_STAGE_COLLISIONS=3_AND_1/3_BOTH_ORIGINS_POSITIVE')
    print('EXHAUSTIVE_LR_DETERMINISTIC=16')
    print('EXHAUSTIVE_FULL_DETERMINISTIC=128')
    print('LR_MIN='+str(lrmin))
    print('FULL_MIN='+str(fullmin))
    print('FULL_WITNESS='+repr(tuple(map(str,ow))))
    print('SUPPORT_GAP='+str(gap))
    print('LINF_DISTANCE_LOWER='+str(gap/sum(map(abs,W))))
    print('PASS_EXACT_R5_TWO_KEY_ENVELOPE_DOUBLE_MERGER')

if __name__=='__main__':
    main()
