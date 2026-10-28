#!/usr/bin/env python3
"""Exact Fraction verification of the R5 two-level overlap/Bellman support gap.

No network, numerical approximations, or external dependencies.
The infinite-real-policy argument is in RESEARCH.md (multi-affinity).
"""
from fractions import Fraction as F
from itertools import product

s = tuple(map(F, ('1/2', '1', '2', '3')))
t = tuple(map(F, ('1', '2', '4', '5')))
zA = tuple(map(F, ('3/8', '1/8', '1/8', '3/8')))
zB = tuple(map(F, ('1/8', '3/8', '3/8', '1/8')))
m = F(1, 4)
threshold = F(2)
time_weight = F(1, 4)


def family(g):
    assert F(0) < g < F(4, 25)
    c = (F(3, 2) * g, F(1, 5) - F(5, 4) * g,
         F(1, 5) - F(5, 4) * g, g)
    a = (F(9,25), F(0), F(0), F(6,25))
    b = (F(0), F(3,10), F(3,10), F(0))
    qA = tuple(ci+ai for ci,ai in zip(c,a))
    qB = tuple(ci+bi for ci,bi in zip(c,b))
    assert all(x > 0 for x in qA+qB+zA+zB)
    assert sum(qA) == sum(qB) == sum(zA) == sum(zB) == 1
    assert sum(x*y for x,y in zip(s,qA)) == sum(x*y for x,y in zip(s,qB)) == F(3,2)
    assert sum(x*y for x,y in zip(t,zA)) == sum(x*y for x,y in zip(t,zB)) == F(3)
    assert tv(qA,qB)==tv_weight(qA,qB,s,F(3,2))==F(3,5)
    assert tv(zA,zB)==tv_weight(zA,zB,t,F(3))==F(1,2)
    assert min(qA[3],qB[3]) == g
    return qA,qB


def tv(x,y):
    return sum((abs(a-b) for a,b in zip(x,y)),F(0))/2


def tv_weight(x,y,signatures,r):
    return sum((ss*abs(a-b) for ss,a,b in zip(signatures,x,y)),F(0))/(2*r)


def observe(g, upA,upB, downA,downB):
    """Output (eP,eQ,TP,TQ) of deterministic policies.

    At error ties r==2, choose declare Q, one permissible optimum.
    P,Q conditional probabilities are built from exact likelihood ratio signatures.
    """
    qA,qB=family(g)
    eP=eQ=TP=TQ=F(0)

    def leaf(q, ratio, tau):
        nonlocal eP,eQ,TP,TQ
        p=q*ratio
        declareP = ratio > threshold
        if declareP: eQ+=q
        else: eP+=p
        TP+=p*tau
        TQ+=q*tau

    leaf(F(1,2), F(1,2),1)  # O terminal at t=1
    for q_parent,q,up,down in ((m,qA,upA,downA),(m,qB,upB,downB)):
        if not up:
            leaf(q_parent,F(3,2),1)
            continue
        for k,(signature,prob) in enumerate(zip(s,q)):
            qnode=q_parent*prob
            if k != 3 or not down:
                leaf(qnode,signature,2)
            else:
                kernels=zA if q is qA else zB
                for tt,prob2 in zip(t,kernels):
                    leaf(qnode*prob2,tt,3)
    assert eP >= 0 and eQ>=0
    return(eP,eQ,TP,TQ)


def loss(obs):
    eP,eQ,TP,TQ=obs
    return eP + 2*eQ + TQ/4


def analytic(g):
    a=g+F(6,25)
    vfull=F(249,200)-F(9,32)*g
    vlr=F(5,4)+F(1,4)*min(F(0),F(23,100)-2*g)
    gap=F(1,200)+F(9,32)*g if g<=F(23,200) else F(1,16)-F(7,32)*g
    assert vlr-vfull==gap
    return vfull,vlr,gap


def validate(g):
    full_candidates=[(loss(observe(g,*x)),x) for x in product((0,1),repeat=4)]
    lr_candidates=[(loss(observe(g,x,x,y,y)),(x,y)) for x,y in product((0,1),repeat=2)]
    exact_full=min(x[0] for x in full_candidates)
    exact_lr=min(x[0] for x in lr_candidates)
    vf,vl,gap=analytic(g)
    assert (vf,vl)==(exact_full,exact_lr)
    assert gap>0
    assert min(x[0] for x in full_candidates if x[1]==(1,0,1,0))==exact_full
    assert loss(observe(g,0,0,0,0))==F(5,4)
    return exact_full,exact_lr,gap


def main():
    gs=(F(1,100),F(1,20),F(1,10),F(23,200),F(1,8),F(19,125),F(159,1000))
    for g in gs:
        vf,vl,gap=validate(g)
        print(f'g={g} full={vf} LR={vl} gap={gap}')
    g=F(23,200)
    qA,qB=family(g)
    assert qA==(F(213,400),F(9,160),F(9,160),F(71,200))
    assert qB==(F(69,400),F(57,160),F(57,160),F(23,200))
    obs=observe(g,1,0,1,0)
    assert obs==(F(5051,6400), F(71,1600), F(1313,800), F(1071,800))
    assert loss(obs)==F(7761,6400)
    assert min(loss(observe(g,x,x,y,y)) for x,y in product((0,1),repeat=2))==F(5,4)
    assert analytic(g)[2] == F(239,6400)
    assert analytic(g)[2]/F(13,4)==F(239,20800)
    print('WITNESS qA=',qA,'qB=',qB)
    print('WITNESS O*=',obs,'L_full=',loss(obs),'L_LR=',F(5,4))
    print('WITNESS L_inf separation >=',F(239,20800))
    n=0
    for i in range(1,160):
        g=F(i,1000)
        validate(g)
        n+=1
    print('EXACT_FAMILY_CASES=',n)
    print('PASS_EXACT_R5_TWO_COLLISION_OCCUPATION_BELLMAN')


if __name__=='__main__':
    main()
