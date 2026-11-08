#!/usr/bin/env python3
"""R5 low-ratio mixed prism; exact corner witnesses, no third-party packages.
For support bit k, Q[k//7,k%7] may be positive. Constraint bit k (0..4)
marks a tight target physical inequality; zero bit k sets coordinate k to 0.
The checker reconstructs each rational witness via exact Gaussian elimination.
"""
from fractions import Fraction as F
from itertools import product
R = (F(1,10),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(19,10))
TAU=F(3,4)
# Product order: p=(0,1); q=(0,3/4); t=(0,1/5);
# theta=(1/4,3/4); kappa=(1/4,3/4).
MASKS='''
1800281c30007:18:0 1010001010101:5:1a 1800281c30007:18:0 1010001010101:5:1a
1800281838007:18:0 1810005018103:4:0 1800281c30007:18:0 1010001010101:5:18
1a00085c30007:18:2 1010001010101:5:a 1a00085c30007:18:2 1010001010101:5:a
1a00085c30007:19:0 1810005018103:4:0 1a00085c30007:19:0 1010001010101:5:8
1a00201830005:18:0 1010001010001:d:12 1a00201830005:18:0 1010001010001:d:12
1a0024101000d:18:0 1814201010009:8:0 1a0024101000d:18:0 1010001010001:d:10
190028101002d:18:2 1010001010001:d:2 190028101002d:18:2 1010001010001:d:2
1800281010029:18:0 1810201810201:0:0 1800281010029:18:0 1010001010001:d:0
'''.split()

def source(p,q,t,theta,kappa):
    return (F(1),t,F(1),(F(13,40)*t+F(1,80))*p,
            t*theta/10+F(9,40)*kappa,
            (F(3,40)*t+F(21,80))*q,t*theta/10)

def face(v):
    g,a,b,u,w=v
    z=TAU*a/10
    return (g,a,b,u,z+F(9,40)*TAU*b,w,z)

def mass(f):
    g,a,b,u,v,w,z=f
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
        F(13,40)*a+b/80-u,(g-a)/2,
        1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
        (g-b)/2,F(3,40)*a+F(21,80)*b-w,
        u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)

def tp(f):
    g,a,b,u,v,w,z=f
    return 1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w

def tq(f):
    g,a,b,u,v,w,z=f
    return 1+g+(a+b)/2+u+v+w

def bounds(v):
    g,a,b,u,w=v
    return (1-g,g-a,g-b,F(13,40)*a+b/80-u,F(3,40)*a+F(21,80)*b-w)

def exact_unique(rows,n):
    a=[row[:] for row in rows]; m=len(a); piv=[]; j=0
    for k in range(n):
        piv_row=next((i for i in range(j,m) if a[i][k]),None)
        if piv_row is None: continue
        a[j],a[piv_row]=a[piv_row],a[j]
        z=a[j][k];a[j]=[u/z for u in a[j]]
        for i in range(m):
            if i!=j and a[i][k]:
                z=a[i][k];a[i]=[u-z*v for u,v in zip(a[i],a[j])]
        piv.append(k);j+=1
    assert all(any(row[:n]) or row[n]==0 for row in a), 'inconsistent support'
    assert len(piv)==n,'nonunique support certificate'
    ans=[F(0)]*n
    for i,k in enumerate(piv):ans[k]=a[i][n]
    assert all(sum(row[k]*ans[k] for k in range(n))==row[n] for row in rows)
    return ans

def certify(p,q,t,theta,kappa,pair):
    support,active,zero=(int(part,16) for part in pair.split(':'))
    spots=[k for k in range(49) if support & (1<<k)]
    n=5+len(spots)
    x=source(p,q,t,theta,kappa);mx=mass(x)
    v0=(F(0),)*5;y0=face(v0)
    V=[tuple(F(i==j) for i in range(5)) for j in range(5)]
    M0=mass(y0);coeff=[[mass(face(V[j]))[i]-M0[i] for j in range(5)] for i in range(7)]
    T0=(tp(y0),tq(y0));tc=[[fun(face(V[j]))-T0[i] for j in range(5)] for i,fun in enumerate((tp,tq))]
    B0=bounds(v0);bc=[[bounds(V[j])[i]-B0[i] for j in range(5)] for i in range(5)]
    rows=[]
    def add(a,b):rows.append([F(z) for z in a]+[F(b)])
    for i in range(7):
        add([-coeff[i][j] for j in range(5)]+[F(k//7==i) for k in spots],M0[i])
    for j in range(7):
        add([F(0)]*5+[F(k%7==j) for k in spots],mx[j])
        add([F(0)]*5+[R[k//7] if k%7==j else F(0) for k in spots],R[j]*mx[j])
    for i,fun in enumerate((tp,tq)):
        add(tc[i]+[F(0)]*len(spots),fun(x)-T0[i])
    for i in range(5):
        if active & (1<<i): add(bc[i]+[F(0)]*len(spots),-B0[i])
    for i in range(5):
        if zero & (1<<i):add([F(j==i) for j in range(5)]+[F(0)]*len(spots),F(0))
    sol=exact_unique(rows,n);v=sol[:5];y=face(v)
    Q=[[F(0)]*7 for _ in range(7)]
    for k,z in zip(spots,sol[5:]):Q[k//7][k%7]=z
    assert all(z>=0 for z in sol) and all(b>=0 for b in bounds(v))
    assert 9*y[2]*y[6]==4*y[1]*(y[4]-y[6])
    assert all(sum(Q[i])==mass(y)[i] for i in range(7))
    assert all(sum(Q[i][j] for i in range(7))==mx[j] for j in range(7))
    assert all(sum(R[i]*Q[i][j] for i in range(7))==R[j]*mx[j] for j in range(7))
    assert tp(y)==tp(x) and tq(y)==tq(x)
    assert sum(mx)==sum(mass(y))==1
    assert sum(R[i]*mx[i] for i in range(7))==sum(R[i]*mass(y)[i] for i in range(7))==1
    assert all(0<=mass(y)[i] for i in range(7))
    return v,Q

if __name__=='__main__':
    corners=list(product((F(0),F(1)),(F(0),F(3,4)),(F(0),F(1,5)),
                         (F(1,4),F(3,4)),(F(1,4),F(3,4))))
    assert len(corners)==len(MASKS)==32
    witnesses=[]
    for params,pair in zip(corners,MASKS):witnesses.append(certify(*params,pair))
    print('PASS_32_EXACT_RATIONAL_CORNER_BLACKWELL_CERTIFICATES',sum(sum(z>0 for z in row) for _,q in witnesses for row in q))
    p,q,t,theta,kappa=(F(7,13),F(7,11),F(3,25),F(7,13),F(5,11))
    scales=((p,F(0),F(1)),(q,F(0),F(3,4)),(t,F(0),F(1,5)),
            (theta,F(1,4),F(3,4)),(kappa,F(1,4),F(3,4)))
    weights=[]
    for bits in product((0,1), repeat=5):
        z=F(1)
        for bit,(val,lo,hi) in zip(bits,scales):
            a=(val-lo)/(hi-lo);z*=a if bit else 1-a
        weights.append(z)
    assert sum(weights)==1 and min(weights)>=0
    x=source(p,q,t,theta,kappa)
    assert all(sum(z*source(*param)[j] for z,param in zip(weights,corners))==x[j] for j in range(7))
    yvals=[sum(z*w[0][j] for z,w in zip(weights,witnesses)) for j in range(5)]
    y=face(yvals)
    Q=[[sum(z*witnesses[k][1][i][j] for k,z in enumerate(weights)) for j in range(7)] for i in range(7)]
    assert all(z>=0 for row in Q for z in row) and all(z>=0 for z in bounds(yvals))
    assert 9*y[2]*y[6]==4*y[1]*(y[4]-y[6])
    assert all(sum(Q[i])==mass(y)[i] for i in range(7))
    assert all(sum(Q[i][j] for i in range(7))==mass(x)[j] for j in range(7))
    assert all(sum(R[i]*Q[i][j] for i in range(7))==R[j]*mass(x)[j] for j in range(7))
    assert tp(y)==tp(x) and tq(y)==tq(x)
    print('PASS_ALL_REAL_MULTIAFFINE_CONVEXITY_AND_INTERIOR_EXACT_TEST')
    print('R5_NEW_THEOREM_FULL_FIVE_PARAMETER_LOW_RATIO_MIXED_PRISM')
