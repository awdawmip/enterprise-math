"""Exact R5 K3 exposed-clock-face obstruction; standard-library rationals only."""
from fractions import Fraction as F
from itertools import product

C = (F(1,8), F(1,6), F(1,16), F(3,32))
FULL_UP = ((0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,1,0))
LR_UP = ((0,0,0),(0,1,1),(1,0,0),(1,1,0))
STAGES = ((0,0,0),(1,0,0),(1,1,0),(1,1,1))
CHECKS = 0

def check(actual, expected):
    global CHECKS
    CHECKS += 1
    assert actual == expected, (CHECKS,actual,expected)

def obs(corner, ks, p, q, r, v):
    x,y,i = corner
    d = F(y,16)+F(3*i,32)
    carriers = (C[0],F(1-x,6),F(y,16),F(3*i,32))
    M = [carriers[s]*STAGES[ks[s]][0] for s in range(4)]
    S = [F(2,3)*M[s]*STAGES[ks[s]][1] for s in range(4)]
    U = [S[s]*STAGES[ks[s]][2] for s in range(4)]
    return (F(107,128)-F(21*x,128)+d/4-sum(S)/2+sum((p[s]*S[s]/8 for s in range(4)),F(0)),
            F(13,64)+F(3*x,64)-d/2+sum(S)/8+sum((q[s]*S[s]/32 for s in range(4)),F(0)),
            F(3)+sum(M)+F(3,2)*sum(S)+sum((r[s]*U[s] for s in range(4)),F(0)),
            F(3)+sum(M)/2+F(3,8)*sum(S)+sum((v[s]*U[s]/4 for s in range(4)),F(0)))

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F(0))

def threshold(t,k):
    return (9+2*k*t)/(8*(3+t))

def certify(R,L,k,p,q,explicit=False):
    assert 0<L<R<1 and 0<k<=1 and k*R<1
    assert all(0<x<1 for x in p+q)
    r=(R,R,L,L); v=tuple(k*x for x in r)
    full=[obs(up,ks,p,q,r,v) for up in FULL_UP for ks in product(range(4),repeat=4)]
    lr=[obs(up,(j,)*4,p,q,r,v) for up in LR_UP for j in range(4)]
    check(len(full),1536);check(len(lr),16)
    lo=threshold(R,k);hi=threshold(L,k);m=(lo+hi)/2
    check(lo<m<hi,True)
    check(k/4<lo<hi<F(3,8),True)
    A=2*m-F(3,4)+R*(4*m-k)/6
    B=2*m-F(3,4)+L*(4*m-k)/6
    check(A>0 and B<0,True)
    n0=(F(0),F(0),m,-F(1))
    W=obs((0,1,1),(3,3,0,0),p,q,r,v)
    H=obs((0,0,0),(3,3,3,3),p,q,r,v)
    check(tuple(W[j]-H[j] for j in range(4)),(F(5,128),-F(5,64),F(0),F(0)))
    hw=dot(n0,W);check(hw,dot(n0,H))
    check(max(dot(n0,z) for z in full),hw)
    check(max(dot(n0,z) for z in lr),hw)
    check(sum(dot(n0,z)==hw for z in lr),1)
    margin=min(dot(n0,H)-dot(n0,z) for z in lr if z!=H)
    check(margin,min(A/6,-F(5,32)*B))
    spread=max(abs(z[0]-H[0]) for z in lr)
    epsilon=margin/(2*(1+spread))
    n=(epsilon,F(0),m,-F(1))
    check(max(dot(n,z) for z in lr),dot(n,H))
    check(sum(dot(n,z)==dot(n,H) for z in lr),1)
    gap=dot(n,W)-dot(n,H)
    check(gap,epsilon*F(5,128))
    check(max(dot(n,z) for z in full)>=dot(n,W),True)
    if explicit:
        ne=(F(1,16),F(0),F(1,3),-F(1))
        fmax=max(dot(ne,z) for z in full);lmax=max(dot(ne,z) for z in lr)
        check(W,(F(455,576),F(39,256),F(673,180),F(4663,1440)))
        check(H,(F(865,1152),F(59,256),F(673,180),F(4663,1440)))
        check(fmax,-F(53707,27648));check(lmax,-F(107549,55296))
        check(fmax-lmax,F(5,2048))
        check(dot(ne,W),fmax)
        check(dot(ne,H),lmax)
        check((fmax-lmax)/sum(map(abs,ne)),F(15,8576))
        print('EXPLICIT', 'normal',ne,'hFULL',fmax,'hLR',lmax,'gap',fmax-lmax,'distance_lower',F(15,8576))
    print('CERTIFIED', 'R',R,'L',L,'k',k,'m',m,'time_margin',margin,'epsilon',epsilon,'mixed_lower_gap',gap)

certify(F(4,5),F(1,5),F(1,2),(F(1,2),)*4,(F(1,2),)*4,True)
certify(F(3,4),F(1,4),F(1,3),(F(1,4),F(1,2),F(3,4),F(1,2)),(F(3,4),F(1,2),F(1,4),F(1,2)))
certify(F(9,10),F(1,10),F(1),(F(1,10),F(9,10),F(1,7),F(5,8)),(F(2,5),F(3,8),F(5,6),F(7,9)))
print('assertions',CHECKS)
print('PASS_EXACT_R5_K3_NONUNIFORM_CLOCK_FACE_4D_NO_GO')
