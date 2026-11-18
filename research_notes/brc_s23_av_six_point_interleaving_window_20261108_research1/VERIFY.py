#!/usr/bin/env python3
"""S23/AV third inversion window exact certificate (Python 3 stdlib)."""
from fractions import Fraction as Q

def log_box(x):
    s=2*sum((x**(2*i+1)/(2*i+1) for i in range(45)),Q(0))
    return s,s+2*x**91/(91*(1-x*x))

a,b=log_box(Q(1,3))
c,d=log_box(Q(1,15))
e,f=log_box(Q(3,17))
lo,hi=(3*a-d)/f,(3*b-c)/e
assert Q(545569623581288298975349314,10**26)<lo<hi<Q(545569623581288298975349315,10**26)

u=(79,431); w=(380295,2074774)
add=lambda a,b:(a[0]+b[0],a[1]+b[1])
sub=lambda a,b:(a[0]-b[0],a[1]-b[1])
mul=lambda n,a:(n*a[0],n*a[1])
size=lambda x:x[0]+x[1]
inside=lambda x,h:min(x)>=0 and size(x)<=h
tri=lambda n:(n+1)*(n+2)//2 if n>=0 else 0
q2=add(u,mul(2,w));q3=add(q2,w);q4=add(q3,w)
M=size(w);H0=size(q2);H1=size(q3);H2=size(q4);H3=2*H0
assert u[0]*w[1]-u[1]*w[0]==1
assert (M,H0,H1,H2,H3)==(2455069,4910648,7365717,9820786,9821296)
for r in (lo,hi):
    eps=u[0]*r-u[1];eta=w[1]-w[0]*r
    assert 0<eta<eps<2*eta and 2*eps>3*eta
inv=[]
for B in range(1,(H3-1)//M+1):
    for A in range(1,(H3-1-B*M)//510+1):
        if all(A*(u[0]*r-u[1])-B*(w[1]-w[0]*r)<0 for r in (lo,hi)):
            inv.append((A,B))
assert inv==[(1,2),(1,3),(1,4)],inv
print('PASS_EXACT_INVERSION_CLASSES',inv)

def correction(p,H,u,w):
    q2=add(u,mul(2,w));q3=add(q2,w);q4=add(q3,w)
    s2=H-size(q2);t3=H-size(q3);z=H-size(q4)
    assert 0<=z<size(u)
    if inside(p,z):return add(p,q3)
    if inside(sub(p,w),z):return add(p,w)
    if inside(sub(p,mul(2,w)),z):return add(sub(p,mul(2,w)),q4)
    if inside(sub(p,q4),z):return add(sub(p,q4),w)
    if inside(sub(p,q3),z):return add(sub(p,q3),q2)
    if inside(sub(p,q2),z):return sub(p,q2)
    def four_start(y):
        return inside(y,t3) and not inside(y,z) and not inside(sub(y,w),z)
    if four_start(sub(p,w)):return add(sub(p,w),q3)
    if four_start(p):return add(p,w)
    if four_start(sub(p,q3)):return add(sub(p,q3),q2)
    if four_start(sub(p,q2)):return sub(p,q2)
    def swap_start(x):
        return inside(x,s2) and not inside(x,t3) and not inside(sub(x,w),t3)
    if swap_start(p):return add(p,q2)
    if swap_start(sub(p,q2)):return sub(p,q2)
    return p

for uu,ww,rr in (((1,1),(2,3),Q(61,44)),((1,1),(5,6),Q(46,39))):
    assert uu[0]*ww[1]-uu[1]*ww[0]==1
    eps=rr*uu[0]-uu[1];eta=ww[1]-rr*ww[0]
    assert Q(3,2)<eps/eta<2
    h2=size(add(uu,mul(4,ww)));h3=2*size(add(uu,mul(2,ww)))
    for H in range(h2,h3):
        S=[(v,j) for v in range(H+1) for j in range(H-v+1)]
        old=sorted(S,key=lambda p:(ww[1]*p[0]-ww[0]*p[1],-p[0]))
        true=sorted(S,key=lambda p:rr*p[0]-p[1])
        assert [correction(p,H,uu,ww) for p in old]==true,(uu,ww,H)
    print('PASS_EXHAUSTIVE_SCALED',uu,ww,'H',h2,'..',h3-1)

for H in (H2,H2+1,H2+509):
    s2=H-H0;t3=H-H1;z=H-H2
    c6=tri(z);c4=tri(t3)-2*c6;c2=tri(s2)-2*tri(t3)+c6
    assert c6>=0 and c4>=0 and c2==M*M
    for x in {(0,0),(min(1,z),0),(0,min(1,z)),(z,0),(0,z)}:
        lex=[add(x,mul(2,w)),add(x,w),x,add(x,q4),add(x,q3),add(x,q2)]
        true=[add(x,q4),add(x,mul(2,w)),add(x,q3),add(x,w),add(x,q2),x]
        assert [correction(p,H,u,w) for p in lex]==true
        for r in (lo,hi):
            vals=[r*p[0]-p[1] for p in true]
            assert all(vals[i]<vals[i+1] for i in range(5))
    print('H',H,'SIX_BLOCKS',c6,'FOUR_BLOCKS',c4,
          'ISOLATED_SWAPS',c2,'INVERSIONS',tri(s2)+tri(t3)+tri(z))
print('PASS_S23_AV_SIX_POINT_INTERLEAVING_H9820786_TO_H9821295')
