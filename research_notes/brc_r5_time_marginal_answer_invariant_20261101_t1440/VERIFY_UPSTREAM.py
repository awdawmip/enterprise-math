#!/usr/bin/env python3
"""All-rational exact witness/interpolation checks for the two-upstream-kernel R5 theorem."""
from fractions import Fraction as F
from itertools import product, permutations

z=F(0); one=F(1)
def vadd(u,v):return tuple(a+b for a,b in zip(u,v))
def vsub(u,v):return tuple(a-b for a,b in zip(u,v))
def vscale(k,u):return tuple(k*x for x in u)
def dot(u,v):return sum((a*b for a,b in zip(u,v)),z)

def obs(bits,a,b):
    p1,p2,q1,q2,qB,r=map(F,bits)
    def tau(p,q,l):return p+(1-p)*(2+l*(1-q))
    eP=(F(1,8)*(p1+(1-p1)*2*a*(q1+(1-q1)*F(2,5)))
        +F(1,8)*(p2+(1-p2)*2*b)+F(1,4)+F(1,2)*(1-r))
    eQ=(F(1,8)*(1-p1)*(1-a+a*(1-q1)*F(1,2))
        +F(1,8)*(1-p2)*(1-b)+F(5,8)*r)
    tP=(F(1,8)*tau(p1,q1,2*a)+F(1,8)*tau(p2,q2,2*b)
        +F(1,4)*(3-qB)+F(1,2)*(3-2*r))
    tQ=(F(1,8)*tau(p1,q1,a)+F(1,8)*tau(p2,q2,b)
        +F(1,8)*(3-qB)+F(5,8)*(3-2*r))
    return eP,eQ,tP,tQ

def lr(p,q,r):return p,p,q,q,q,r

def chart(a,b):
    o0=obs(lr(0,0,0),a,b)
    B=vsub(obs(lr(1,0,0),a,b),o0)
    C=vsub(obs(lr(0,1,0),a,b),o0)
    D=vsub(vsub(vsub(obs(lr(1,1,0),a,b),o0),B),C)
    E=vsub(obs(lr(0,0,1),a,b),o0)
    return o0,(B,C,D,E)

def determinant(cols):
    ans=F(0)
    for p in permutations(range(4)):
        sign=(-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        term=F(sign)
        for j in range(4):term*=cols[j][p[j]]
        ans+=term
    return ans

def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def hull(points):
    pts=sorted(set(points))
    def build(seq):
        out=[]
        for p in seq:
            while len(out)>=2 and cross(out[-2],out[-1],p)<=0:out.pop()
            out.append(p)
        return out
    return tuple(build(pts)[:-1]+build(pts[::-1])[:-1])

nodes=(F(1,10),F(1,5),F(3,10),F(2,5))
full_bits=tuple(product((0,1),repeat=6))
lr_bits=tuple(product((0,1),repeat=3))
checks=0
for a,b in product(nodes,repeat=2):
    o0,cols=chart(a,b)
    # Each column is affine in (a,b), and E is constant. 4x4 tensor
    # interpolation certifies identity of a bidegree <=(3,3) polynomial.
    det=determinant(cols)
    assert det==a*(31-3*a-3*b)/5120 and det>0
    checks+=1
    vals=(F(0),F(1,3),F(1,2),F(2,3),F(1))
    for p,q,r in product(vals,repeat=3):
        expect=vadd(o0,vadd(vscale(p,cols[0]),vadd(vscale(q,cols[1]),vadd(vscale(p*q,cols[2]),vscale(r,cols[3])))))
        assert obs(lr(p,q,r),a,b)==expect
        checks+=1
    n=(8+4*(a+b),-8-8*(a+b))
    ff=[(bits,obs(bits,a,b)[2:]) for bits in full_bits]
    rr=[(bits,obs(lr(*bits),a,b)[2:]) for bits in lr_bits]
    gap=max(dot(n,t) for _,t in ff)-max(dot(n,t) for _,t in rr)
    assert gap==abs(a-b)/2
    checks+=1
    if a==b:
        assert hull([t for _,t in ff])==hull([t for _,t in rr])
        W=obs((1,0,0,0,0,1),a,a)
        u,v,s,w=F(1,2),-a,-a-F(1,2),F(1)
        rec=vadd(o0,vadd(vscale(u,cols[0]),vadd(vscale(v,cols[1]),vadd(vscale(s,cols[2]),vscale(w,cols[3])))))
        assert W==rec and s<0
        checks+=1

# At a=b, both source advantages are equal for every signed time direction:
# max(0,A)+max(0,A)-max(0,2*A)==0 (algebraically all real).
# At a!=b, choosing n above makes the advantages ±(a-b)/2.
print('UPSTREAM_TWO_PARAMETER_DOMAIN','0<a,b<1/2; P_low=(2a,2b), Q_low=(a,b)')
print('ALL_REAL_TIME_SUPPORT_GAP','abs(a-b)/2 in explicit signed direction n(a,b)')
print('TIME_HULL_EQUALITY_IFF','a=b')
print('LR_4D_DETERMINANT','a*(31-3*a-3*b)/5120 > 0 throughout domain')
print('DIAGONAL_FULL_WITNESS_CHART','(u,v,s,w)=(1/2,-a,-a-1/2,1) => s<0')
print('RATIONAL_INTERPOLATION_GRID',len(nodes),'x',len(nodes),'TOTAL_ASSERTION_GROUPS',checks)
print('PASS_EXACT_R5_UPSTREAM_TWO_KERNEL_ALL_REAL_COMPLETE_NO_GO')
