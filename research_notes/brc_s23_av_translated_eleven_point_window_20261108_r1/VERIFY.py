#!/usr/bin/env python3
"""Exact eleven-point translation window after H=2|q2|; finite scaled model exhaustive verification."""
from fractions import Fraction as F

def log_box(x):
    s=2*sum((x**(2*i+1)/(2*i+1) for i in range(45)),F(0))
    return s,s+2*x**91/(91*(1-x*x))
a,b=log_box(F(1,3));c,d=log_box(F(1,15));e,f=log_box(F(3,17))
lo,hi=(3*a-d)/f,(3*b-c)/e
assert F(545569623581288298975349314,10**26)<lo<hi<F(545569623581288298975349315,10**26)

def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def mul(n,a):return n*a[0],n*a[1]
def sz(a):return sum(a)
def inside(p,h):return min(p)>=0 and sz(p)<=h
def T(n):return (n+1)*(n+2)//2 if n>=0 else 0
def tri(h):return ((i,s-i) for s in range(h+1) for i in range(s+1))

def blocks(u,w,H):
    d=sz(u);M=sz(w)
    q2=add(u,mul(2,w));q3=add(q2,w);q4=add(q3,w)
    H3=2*sz(q2);a=H-H3
    assert 0<=a<d<M
    z=d+a;t=M+z;s=2*M+z
    w2=mul(2,w); u2=mul(2,u)
    out=[]
    for x in tri(a):
        old=[w2,w,(0,0),q4,q3,q2,add(u,w),u,mul(2,q2),add(u2,mul(3,w)),add(u2,mul(2,w))]
        new=[q4,w2,q3,w,mul(2,q2),q2,(0,0),add(u2,mul(3,w)),add(u,w),add(u2,mul(2,w)),u]
        out.append(('eleven', [add(x,y) for y in old], [add(x,y) for y in new]))
    for x in tri(z):
        if inside(x,a) or inside(sub(x,u),a):continue
        old=[w2,w,(0,0),q4,q3,q2]
        new=[q4,w2,q3,w,q2,(0,0)]
        out.append(('six',[add(x,y) for y in old],[add(x,y) for y in new]))
    for y in tri(t):
        if inside(y,z) or inside(sub(y,w),z):continue
        old=[w,(0,0),q3,q2]
        new=[q3,w,q2,(0,0)]
        out.append(('four',[add(y,v) for v in old],[add(y,v) for v in new]))
    for x in tri(s):
        if inside(x,t) or inside(sub(x,w),t):continue
        out.append(('pair',[x,add(x,q2)],[add(x,q2),x]))
    return out

def verify(u,w,r):
    assert u[0]*w[1]-u[1]*w[0]==1
    eps=r*u[0]-u[1];eta=w[1]-r*w[0]
    assert F(3,2)*eta<eps<2*eta
    H3=2*sz(add(u,mul(2,w)))
    for H in range(H3,H3+sz(u)):
        pts=[(v,j) for v in range(H+1) for j in range(H-v+1)]
        old=sorted(pts,key=lambda p:(w[1]*p[0]-w[0]*p[1],-p[0]))
        true=sorted(pts,key=lambda p:r*p[0]-p[1])
        pos={p:i for i,p in enumerate(old)}
        transformed={};seen=set();counts={'eleven':0,'six':0,'four':0,'pair':0}
        for label,bl,bnew in blocks(u,w,H):
            assert all(p in pos for p in bl)
            loc=[pos[p] for p in bl]
            assert loc==list(range(loc[0],loc[0]+len(bl))), (H,label,bl,loc)
            assert set(bl)==set(bnew), (H,label,bl,bnew)
            assert all(p not in seen for p in bl), (H,label)
            seen.update(bl)
            transformed.update(zip(bl,bnew));counts[label]+=1
        result=[transformed.get(p,p) for p in old]
        assert result==true, (u,w,H,next((i for i,(x,y) in enumerate(zip(result,true)) if x!=y),None))
        a=H-H3; d=sz(u);M=sz(w);z=d+a
        expect={'eleven':T(a),'six':T(z)-2*T(a),'four':T(M+z)-2*T(z),'pair':M*M}
        assert counts==expect,(counts,expect)
        inversions=13*counts['eleven']+6*counts['six']+3*counts['four']+counts['pair']
        assert inversions==T(2*M+z)+T(M+z)+T(z)+T(a)
        print('PASS_SCALED_FULL_SORT',u,w,'H',H,'POINTS',len(pts),'COUNTS',counts,'INVERSIONS',inversions)

verify((1,1),(2,3),F(61,44))
verify((2,1),(5,3),F(61,105))
verify((1,1),(5,6),F(46,39))

u=(79,431);w=(380295,2074774); d=sz(u);M=sz(w)
q2=add(u,mul(2,w));q3=add(q2,w);q4=add(q3,w)
H3=2*sz(q2)
assert (d,M,H3,sz(q4))==(510,2455069,9821296,9820786)
for r in (lo,hi):
    eps=r*u[0]-u[1];eta=w[1]-r*w[0]
    assert F(3,2)*eta<eps<2*eta
inv=[]
for B in range(1,(H3+d-1)//M+1):
    for A in range(1,(H3+d-1-B*M)//d+1):
        v=[A*(u[0]*r-u[1])-B*(w[1]-w[0]*r) for r in (lo,hi)]
        if max(v)<0:inv.append((A,B))
        else:assert min(v)>0
assert inv==[(1,2),(1,3),(1,4),(2,4)],inv
print('PASS_EXACT_INVERSION_TYPES_THROUGH',H3+d-1,inv)
for a in (0,1,100,509):
    H=H3+a;z=d+a;t=M+z;s=2*M+z
    c11=T(a); c6=T(z)-2*T(a); c4=T(t)-2*T(z); c2=M*M
    assert min(c11,c6,c4,c2)>=0
    assert 13*c11+6*c6+3*c4+c2==T(s)+T(t)+T(z)+T(a)
    print('PASS_ACTUAL_SYMBOLIC_ENDPOINT','H',H,'ELEVEN',c11,'SIX',c6,'FOUR',c4,'PAIR',c2,'INV',T(s)+T(t)+T(z)+T(a))
print('PASS_S23_AV_ELEVEN_POINT_TRANSLATION_WINDOW_H9821296_TO_H9821805')
