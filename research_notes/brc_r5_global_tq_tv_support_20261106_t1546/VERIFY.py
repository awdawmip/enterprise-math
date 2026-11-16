#!/usr/bin/env python3
"""Exact rational regression for the R5 global time-budget TV support certificate.
The universal real theorem is algebraic, not inferred from this finite sample.
"""
from fractions import Fraction as F
from itertools import product

R = (F(1,10), F(1,2), F(3,4), F(1), F(5,4), F(3,2), F(19,10))
Q3 = ((F(13,20),F(1,5),F(3,20)),
      (F(1,40),F(9,20),F(21,40)))
ALPHA, BETA = F(47,180),F(67,162)
Q4OUT0=(F(509,900),F(382,900),F(9,900))
Q4OUT2=(F(9,900),F(382,900),F(509,900))
Q4MID0=(ALPHA,F(43,90),ALPHA)
Q4MID1=(BETA,F(14,81),BETA)

def check_kernel():
    for i,row in enumerate(Q3):
        assert sum(row)==1 and min(row)>0
        assert sum(row[j]*R[(1,3,5)[j]] for j in range(3))==(F(3,4),F(5,4))[i]
    for row,root in zip((Q4OUT0,Q4MID0,Q4OUT2,Q4MID1),
                        (F(1,2),F(1),F(3,2),F(1))):
        assert sum(row)==1 and min(row)>0
        assert sum(row[j]*R[(0,3,6)[j]] for j in range(3))==root

def calc(g,u0,u1,x):
    assert 0<=u0<=g<=1 and 0<=u1<=g
    cap=tuple(tuple(ui*Q3[i][j]/2 for j in range(3)) for i,ui in enumerate((u0,u1)))
    assert all(0<=x[i][j]<=cap[i][j] for i in range(2) for j in range(3))
    V=tuple(sum(cap[i][j] for i in range(2)) for j in range(3))
    X=tuple(sum(x[i][j] for i in range(2)) for j in range(3))
    J=ALPHA*x[0][1]+BETA*x[1][1]
    masses={
        F(1,10):(509*X[0]+9*X[2])/900+J,
        F(1,2):V[0]-X[0],
        F(3,4):(g-u0)/2,
        F(1):1-g+V[1]+F(382,900)*(X[0]+X[2])-2*J,
        F(5,4):(g-u1)/2,
        F(3,2):V[2]-X[2],
        F(19,10):(9*X[0]+509*X[2])/900+J,
    }
    assert min(masses.values())>=0 and sum(masses.values())==1
    assert sum(r*masses[r] for r in R)==1
    TQ=1+g+(u0+u1)/2+sum(X)
    TP=1+g+(3*u0+5*u1)/8+X[0]/2+X[1]+3*X[2]/2
    S=sum((1-r)*masses[r] for r in R if r<1)
    assert S==g/8+3*u0/80+u1/160+F(9,1000)*(X[0]+X[2])+F(9,10)*J
    gap=u0/3600+u1/1600+F(29,250)*(X[0]+X[2])+F(89,360)*(V[1]-X[1])+F(9,10)*(BETA*X[1]-J)
    assert gap==(TQ-1)/8-S and gap>=0
    if gap==0:
        assert (u0,u1)==(0,0) and X==(0,0,0) and TP==TQ
    return TQ,TP,S,gap,masses

def main():
    check_kernel()
    n=0
    max_gap=0
    for g_num in (0,1,2):
        g=F(g_num,2)
        for u_frac0,u_frac1 in product((F(0),F(1,2),F(1)),repeat=2):
            u0,u1=u_frac0*g,u_frac1*g
            cap=tuple(tuple(ui*Q3[i][j]/2 for j in range(3)) for i,ui in enumerate((u0,u1)))
            for z in product((F(0),F(1,2),F(1)), repeat=6):
                x=((z[0]*cap[0][0],z[1]*cap[0][1],z[2]*cap[0][2]),
                   (z[3]*cap[1][0],z[4]*cap[1][1],z[5]*cap[1][2]))
                tq,tp,S,gap,m=calc(g,u0,u1,x)
                max_gap=max(max_gap,gap)
                assert 0<=S<=F(1,2)
                for choice in (tuple(F(1) if r<1 else F(0) for r in R),
                               tuple(F(1) if r>1 else F(0) for r in R)):
                    ep=1-sum(r*m[r]*v for r,v in zip(R,choice))
                    eq=sum(m[r]*v for r,v in zip(R,choice))
                    assert abs(ep+eq-1)==S<=(tq-1)/8
                n+=1
    assert n==3*3**2*3**6
    sat=0
    for g in (F(0),F(1,8),F(1,4),F(1,2),F(7,8),F(1)):
        x=((F(0),)*3,)*2
        tq,tp,S,gap,m=calc(g,F(0),F(0),x)
        assert (tq,tp,S,gap)==(1+g,1+g,g/8,F(0))
        for q in (F(-1),F(-1,2),F(0),F(1,2),F(1)):
            v={r:F(1,2) for r in R}
            if g:
                v[F(3,4)]=F(1,2)+q/2
                v[F(5,4)]=F(1,2)-q/2
            ep=1-sum(r*m[r]*v[r] for r in R)
            eq=sum(m[r]*v[r] for r in R)
            assert ep+eq-1==q*g/8
            sat+=1
    print('PASS_EXACT_R5_GLOBAL_TQ_TV_SUPPORT_AND_RIGIDITY')
    print('policy grid full-history exact cases=',n)
    print('sharp LR family exact cases=',sat)
    print('nonnegative identity: (TQ-1)/8-TV = u0/3600+u1/1600+29(X0+X2)/250+89(V1-X1)/360+9(beta*X1-J)/10')
    print('beta=',BETA,'alpha=',ALPHA)
    print('time interval with attained maximum: 1<=TQ<=2, TP=TQ')
    print('max gap over grid=',max_gap)
    print('example at TQ=TP=15/8: sharp TV =',F(7,64),'with g=7/8 and no later continuation')

if __name__=='__main__':main()
