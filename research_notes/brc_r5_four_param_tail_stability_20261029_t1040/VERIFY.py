#!/usr/bin/env python3
"""Exact Fraction verification for four-parameter BRC LR tail stability.

Universal result follows from the vertex proof in RESEARCH.md; finite grids here
are exact regression checks, not substitutes for all-real quantifiers.
"""
from fractions import Fraction as F
from itertools import product

S = (F(1,2), F(1), F(3,2), F(5,2))
ORIGINS = ('A','B')
MU = {'A':(F(7,50),F(11,75),F(1,2),F(16,75)),
      'B':(F(17,200),F(23,150),F(3,5),F(97,600))}
NU = {('A','L'):(F(1,2),F(1,6),F(1,4),F(1,12)),
      ('B','L'):(F(5,12),F(1,3),F(1,6),F(1,12)),
      ('A','R'):(F(17,100),F(23,75),F(1,5),F(97,300)),
      ('B','R'):(F(31,120),F(5,18),F(1,15),F(143,360))}
ETA0 = {'A':(F(1,8), F(1,4), F(3,8), F(1,4)),
        'B':(F(5,32), F(3,16), F(13,32), F(1,4))}
D1 = (F(1),F(-2),F(1),F(0))
D2 = (F(1),F(0),F(-2),F(1))
Q = {'A':F(1,4),'B':F(1,4)}
RHO = {i: Q[i]*(MU[i][1]*NU[i,'L'][2] + MU[i][2]*NU[i,'R'][2]) for i in ORIGINS}
R = F(1,1000)
THETA0=F(787,5824)
BASEGAP=F(2419,6988800)


def tail(i,a,b):
    return tuple(x + a*y + b*z for x,y,z in zip(ETA0[i],D1,D2))


def g(s):
    return min(F(0),F(2)-2*s)


def f(t,s,theta):
    return t*theta + g(s)


def threshold(i,a,b):
    return (F(1,8) if i=='A' else F(5,32)) + a+b


def tail_increment(i,a,b,theta):
    return sum((x*f(4,s,theta) for x,s in zip(tail(i,a,b),S)),F(0))-f(3,S[2],theta)


def upstream_margins(i,a,b,theta,gl,gr):
    d=tail_increment(i,a,b,theta)
    lower={}
    for name,gamma,idx in (('L',gl,1),('R',gr,2)):
        continuation=sum((prob*(f(3,s,theta)+(gamma*d if k==2 else F(0)))
                          for k,(prob,s) in enumerate(zip(NU[i,name],S))),F(0))
        lower[name] = (f(2,S[idx],theta),continuation)
    root_cont = sum((prob*(lower['L'][1] if k==1 else lower['R'][1]
                            if k==2 else f(2,s,theta))
                    for k,(prob,s) in enumerate(zip(MU[i],S))),F(0))
    return (lower['L'][0]-lower['L'][1], lower['R'][0]-lower['R'][1],
            f(1,S[2],theta)-root_cont)


def lr_terminal(params,root,left,right,merged):
    z={}
    def add(t,s,v): z[(t,s)] = z.get((t,s),F(0))+v
    add(1,S[0],F(1,2));add(1,S[2],F(1,2)*(1-root))
    for i in ORIGINS:
        a,b=params[i]
        for j,s in enumerate(S):
            m = root*Q[i]*MU[i][j]
            if j not in (1,2): add(2,s,m)
            else:
                name = 'L' if j==1 else 'R';gamma=left if j==1 else right
                add(2,s,m*(1-gamma))
                for k,sv in enumerate(S):
                    n = m*gamma*NU[i,name][k]
                    if k != 2: add(3,sv,n)
                    else:
                        add(3,sv,n*(1-merged))
                        for prob,t in zip(tail(i,a,b),S): add(4,t,n*merged*prob)
    return z


def full_terminal_B(params):
    """Root, both paths continue; only hidden origin B continues at the merge."""
    z={}
    def add(t,s,v):z[(t,s)]=z.get((t,s),F(0))+v
    add(1,S[0],F(1,2))
    for i in ORIGINS:
        a,b=params[i]
        for j,s in enumerate(S):
            m=Q[i]*MU[i][j]
            if j not in (1,2):add(2,s,m)
            else:
                name='L' if j==1 else 'R'
                for k,sv in enumerate(S):
                    n=m*NU[i,name][k]
                    if k != 2 or i=='A':add(3,sv,n)
                    else:
                        for prob,t in zip(tail(i,a,b),S):add(4,t,n*prob)
    return z


def objective(z,theta):
    return F(2)+sum((m*f(t,s,theta) for (t,s),m in z.items()),F(0))


def obs(z):
    return (F(1)-sum((m*s for (t,s),m in z.items() if s>1),F(0)),
            sum((m for (t,s),m in z.items() if s>1),F(0)),
            sum((t*s*m for (t,s),m in z.items()),F(0)),
            sum((t*m for (t,s),m in z.items()),F(0)))


def theta_star(params):
    return sum((RHO[i]*threshold(i,*params[i]) for i in ORIGINS),F(0))/sum(RHO.values())


def expected_gap(params):
    return RHO['A']*RHO['B']/(RHO['A']+RHO['B'])*(threshold('B',*params['B'])-threshold('A',*params['A']))


def verify():
    assert RHO=={'A':F(41,1200),'B':F(59,3600)}
    assert sum(RHO.values()) == F(91,1800)
    assert RHO['A']*RHO['B']/(RHO['A']+RHO['B']) == F(2419,218400)
    assert sum(D1)==sum(D2)==0
    assert sum(x*s for x,s in zip(D1,S)) == sum(x*s for x,s in zip(D2,S)) == 0
    assert sum(x*g(s) for x,s in zip(D1,S)) == sum(x*g(s) for x,s in zip(D2,S)) == -1
    for i in ORIGINS:
        for row,parent in ((MU[i],F(3,2)),(NU[i,'L'],F(1)),(NU[i,'R'],F(3,2))):
            assert min(row)>0 and sum(row)==1 and sum((s*q for s,q in zip(S,row)),F(0))==parent
        for a,b in product((-R,R),repeat=2):
            row=tail(i,a,b)
            assert min(row)>0 and sum(row)==1 and sum((s*q for s,q in zip(S,row)),F(0))==F(3,2)
            assert tail_increment(i,a,b,THETA0)==THETA0-threshold(i,a,b)
    minima={}
    # Each M is multi-affine separately in a,b,theta,gl,gr; hence corners suffice.
    for i in ORIGINS:
        vals=[upstream_margins(i,a,b,theta,gl,gr)
              for a,b in product((-R,R),repeat=2)
              for theta in (F(1,8),F(5,32))
              for gl,gr in product((F(0),F(1)),repeat=2)]
        minima[i]=tuple(min(t[k] for t in vals) for k in range(3))
        assert all(x>0 for x in minima[i])
    print('EXACT_PARAMETRIC_CORNER_MINIMA',minima)
    lower=F(2419,218400)*F(109,4000)
    upper=F(2419,218400)*F(141,4000)
    assert lower == F(263671,873600000)
    assert upper == F(341079,873600000)
    print('UNIFORM_MAX_GAP_RANGE',lower,upper)
    samples=(-R, F(-1,2000), F(0), F(1,2000), R)
    checked=0
    corner_count=0
    for aa,ab,ba,bb in product(samples,repeat=4):
        params={'A':(aa,ab),'B':(ba,bb)}
        center=theta_star(params)
        assert F(1,8)<center<F(5,32)
        assert threshold('A',aa,ab)<center<threshold('B',ba,bb)
        gap=expected_gap(params)
        assert lower<=gap<=upper
        assert gap>0
        zf=full_terminal_B(params)
        of=obs(zf)
        expected_o=(F(98731,230400)+RHO['B']*(-3*ba+bb)/2,
                    F(627,2560)+RHO['B']*(ba-bb),
                    F(5429,2400),F(6719,3600))
        assert of == expected_o
        assert objective(zf,center)==2*of[0]+2*of[1]+center*of[3]
        v0=F(2429,1800)+F(37,20)*center
        full=v0 + RHO['B']*(center-threshold('B',ba,bb))
        lr=v0
        assert objective(zf,center)==full
        best=min(objective(lr_terminal(params,*coins),center)
                 for coins in product((F(0),F(1)),repeat=4))
        assert best==lr and best-full==gap
        checked +=1
        if aa in (-R,R) and ab in (-R,R) and ba in (-R,R) and bb in (-R,R):corner_count+=1
    print('PARAMETER_SETS_EXACTLY_VERIFIED',checked,'including',corner_count,'four-cube vertices')
    print('LR_DETERMINISTIC_STRATEGIES_PER_POINT',16)
    params={'A':(-R,-R),'B':(R,R)}
    assert expected_gap(params)==upper
    params={'A':(R,R),'B':(-R,-R)}
    assert expected_gap(params)==lower
    print('PASS_EXACT_R5_FOUR_PARAMETER_COLLISION_STABILITY')

if __name__=='__main__':verify()
