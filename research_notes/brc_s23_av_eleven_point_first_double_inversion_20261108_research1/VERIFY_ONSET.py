#!/usr/bin/env python3
"""Exact S23/AV onset H=9_821_296: eleven-point merged block."""
from fractions import Fraction as Q

def log_box(x):
    s=2*sum((x**(2*i+1)/(2*i+1) for i in range(45)),Q(0))
    return s,s+2*x**91/(91*(1-x*x))
a,b=log_box(Q(1,3));c,d=log_box(Q(1,15));e,f=log_box(Q(3,17))
lo,hi=(3*a-d)/f,(3*b-c)/e
assert Q(545569623581288298975349314,10**26)<lo<hi<Q(545569623581288298975349315,10**26)
add=lambda a,b:(a[0]+b[0],a[1]+b[1])
sub=lambda a,b:(a[0]-b[0],a[1]-b[1])
mul=lambda n,a:(n*a[0],n*a[1])
size=lambda x:x[0]+x[1]
inside=lambda x,h:min(x)>=0 and size(x)<=h
tri=lambda n:(n+1)*(n+2)//2 if n>=0 else 0

def block11(u,w):
    q2=add(u,mul(2,w));q3=add(q2,w);q4=add(q3,w);uu=mul(2,u)
    old=[mul(2,w),w,(0,0),q4,q3,q2,add(u,w),u,mul(2,q2),add(uu,mul(3,w)),add(uu,mul(2,w))]
    new=[q4,mul(2,w),q3,w,mul(2,q2),q2,(0,0),add(uu,mul(3,w)),add(u,w),add(uu,mul(2,w)),u]
    assert len(set(old))==11 and len(set(new))==11 and set(old)==set(new)
    return dict(zip(old,new)),old,new

def select_at_old_lex_point(p,u,w):
    q2=add(u,mul(2,w));q3=add(q2,w);q4=add(q3,w)
    H=2*size(q2);s2=H-size(q2);t3=H-size(q3);z=H-size(q4)
    assert z==size(u) and z<size(w)
    mapping,_,_=block11(u,w)
    if p in mapping:return mapping[p]
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

u=(79,431);w=(380295,2074774);M=size(w)
q2=add(u,mul(2,w));H=2*size(q2)
assert (H,size(u),M)==(9821296,510,2455069)
for r in (lo,hi):
    eps=79*r-431;eta=w[1]-w[0]*r
    assert Q(3,2)*eta<eps<2*eta
inv=[]
for B in range(1,H//M+1):
    for A in range(1,(H-B*M)//510+1):
        if all(A*(79*r-431)-B*(w[1]-w[0]*r)<0 for r in (lo,hi)):
            inv.append((A,B))
assert inv==[(1,2),(1,3),(1,4),(2,4)]
print('PASS_EXACT_H3_INVERSION_CLASSES',inv)

for uu,ww,rr in (((1,1),(2,3),Q(61,44)),((1,1),(5,6),Q(46,39))):
    assert uu[0]*ww[1]-uu[1]*ww[0]==1
    eps=rr*uu[0]-uu[1];eta=ww[1]-rr*ww[0]
    assert Q(3,2)<eps/eta<2
    hh=2*size(add(uu,mul(2,ww)))
    S=[(v,j) for v in range(hh+1) for j in range(hh-v+1)]
    old=sorted(S,key=lambda p:(ww[1]*p[0]-ww[0]*p[1],-p[0]))
    true=sorted(S,key=lambda p:rr*p[0]-p[1])
    assert [select_at_old_lex_point(p,uu,ww) for p in old]==true
    print('PASS_EXHAUSTIVE_SCALED_ONSET',uu,ww,'H',hh,'THRESHOLDS',len(S))

mapping,old,new=block11(u,w)
assert sorted(old,key=lambda p:(w[1]*p[0]-w[0]*p[1],-p[0]))==old
for r in (lo,hi):
    vals=[r*p[0]-p[1] for p in new]
    assert all(vals[i]<vals[i+1] for i in range(10))
assert [mapping[p] for p in old]==new
z=H-size(add(u,mul(4,w)));t=H-size(add(u,mul(3,w)));s=H-size(q2)
c11=1;c6=tri(z)-2;c4=tri(t)-2*tri(z);c2=tri(s)-2*tri(t)+tri(z)
assert (z,c6,c2)==(510,130814,M*M)
assert 13+6*c6+3*c4+c2==tri(s)+tri(t)+tri(z)+1
print('H',H,'ELEVEN_BLOCKS',c11,'SIX_BLOCKS',c6,'FOUR_BLOCKS',c4,'ISOLATED_SWAPS',c2,'INVERSIONS',tri(s)+tri(t)+tri(z)+1)
print('PASS_S23_AV_EXACT_ONSET_ELEVEN_POINT_H9821296')
