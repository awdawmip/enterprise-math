#!/usr/bin/env python3
"""Exact rational R5 interacting serial merger obstruction. No external modules."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product

R=(F(1,2),F(1),F(3,2))
PA,PB,P0=F(1,4),F(1,8),F(1,4)
THETA=F(27,496)
LEFT,RIGHT=F(13,272),F(1,16)

def qrow(p):
    return (p,1-2*p,p)

def stop(t,r,theta):
    return min(r,F(1))+t*theta*(r+1)

def tail_value(theta):
    @lru_cache(None)
    def val(t,r):
        if t==4:
            return stop(t,r,theta)
        cont=sum(q*val(t+1,r*s) for s,q in zip(R,qrow(P0)))
        return min(stop(t,r,theta),cont)
    return val

def source_values(theta):
    val=tail_value(theta)
    s=stop(1,F(1),theta)
    ca=sum(q*val(2,r) for r,q in zip(R,qrow(PA)))
    cb=sum(q*val(2,r) for r,q in zip(R,qrow(PB)))
    full=(min(s,ca)+min(s,cb))/2
    lr=min(s,(ca+cb)/2)
    return (s,ca,cb,full,lr,lr-full)

def observer(terminal):
    assert sum(q for t,r,q,d in terminal)==1
    assert sum(r*q for t,r,q,d in terminal)==1
    ep=sum(r*q for t,r,q,d in terminal if d=='Q')
    eq=sum(q for t,r,q,d in terminal if d=='P')
    tp=sum(t*r*q for t,r,q,d in terminal)
    tq=sum(t*q for t,r,q,d in terminal)
    return (ep,eq,tp,tq)

def declaration(r):
    return 'P' if r>=1 else 'Q'

def full_witness():
    val=tail_value(THETA)
    terminal=[(1,F(1),F(1,2),'P')]
    def descend(t,r,qm):
        if t==4:
            terminal.append((t,r,qm,declaration(r)))
            return
        cont=sum(q*val(t+1,r*s) for s,q in zip(R,qrow(P0)))
        if cont<stop(t,r,THETA):
            for ss,qq in zip(R,qrow(P0)):
                descend(t+1,r*ss,qm*qq)
        else:
            terminal.append((t,r,qm,declaration(r)))
    for ss,qq in zip(R,qrow(PA)):
        descend(2,ss,F(1,2)*qq)
    return observer(terminal)

def lr_enumeration():
    keys=[(1,F(1))]
    keys += [(2,r) for r in R]
    keys += [(3,r) for r in sorted({a*b for a,b in product(R,repeat=2)})]
    assert len(keys)==10
    idx={k:i for i,k in enumerate(keys)}
    scores=[]
    for mask in range(1<<len(keys)):
        terminal=[]
        def descend(t,r,qm):
            if t==4 or not ((mask>>idx[(t,r)])&1):
                terminal.append((t,r,qm,declaration(r)))
                return
            for ss,qq in zip(R,qrow(P0)):
                descend(t+1,r*ss,qm*qq)
        if mask&1:
            for p in (PA,PB):
                for ss,qq in zip(R,qrow(p)):
                    descend(2,ss,F(1,2)*qq)
        else:
            terminal.append((1,F(1),F(1),'P'))
        o=observer(terminal)
        scores.append(o[0]+o[1]+THETA*(o[2]+o[3]))
    return len(scores),min(scores)

def main():
    for p in (PA,PB,P0):
        q=qrow(p)
        qp=tuple(s*x for s,x in zip(R,q))
        assert all(x>0 for x in q+qp)
        assert sum(q)==sum(qp)==1
    qa,qb=qrow(PA),qrow(PB)
    pa,pb=(tuple(s*x for s,x in zip(R,q)) for q in (qa,qb))
    assert sum(abs(x-y) for x,y in zip(qa,qb))/2==F(1,4)
    assert sum(abs(x-y) for x,y in zip(pa,pb))/2==F(1,4)
    route1=sum(F(1,2)*qrow(p)[0]*qrow(P0)[2] for p in (PA,PB))
    route2=sum(F(1,2)*qrow(p)[2]*qrow(P0)[0] for p in (PA,PB))
    assert route1==route2==F(3,64)
    s,ca,cb,full,lr,gap=source_values(THETA)
    assert (s,ca,cb,full,lr,gap)==(F(275,248),F(67,62),F(141,124),
                                    F(543,496),F(275,248),F(7,496))
    o=full_witness()
    assert o==(F(7,64),F(25,32),F(15,8),F(15,8))
    assert o[0]+o[1]+THETA*(o[2]+o[3])==full
    count,lrmin=lr_enumeration()
    assert count==1024 and lrmin==lr
    for i in range(101):
        theta=LEFT+(RIGHT-LEFT)*F(i,100)
        s,ca,cb,ff,ll,gg=source_values(theta)
        assert ca==F(25,32)+F(11,2)*theta
        assert cb==F(51,64)+F(25,4)*theta
        assert s==1+2*theta
        assert gg==min(F(7,4)*(RIGHT-theta),F(17,8)*theta-F(13,128))>=0
    assert LEFT<THETA<RIGHT
    assert F(7,4)*(RIGHT-THETA)==F(17,8)*THETA-F(13,128)==F(7,496)
    print('P_Q_ALL_ROWS_STRICT_POSITIVE_AND_NORMALIZED=PASS')
    print('SOURCE_TV_Q=1/4 SOURCE_TV_P=1/4')
    print('SECOND_MERGER_ALL_CONTINUE_Q_ROUTE_MASSES=3/64,3/64')
    print('THETA_STAR=27/496')
    print('S=275/248 C_A=67/62 C_B=141/124')
    print('FULL_MIN=543/496 LR_MIN=275/248 GAP=7/496')
    print('FULL_WITNESS_O=(7/64,25/32,15/8,15/8)')
    print('FARKAS_INTEGER_HYPERPLANE=496eP+496eQ+27TP+27TQ>=550')
    print('FULL_WITNESS_HYPERPLANE_VALUE=543')
    print('LINF_SEPARATION_LOWER_BOUND=7/1046')
    print('LR_DETERMINISTIC_STOP_CONTINUE_MASKS_CHECKED=1024')
    print('EXACT_RATIONAL_THETA_CHECKPOINTS=101')
    print('PASS_EXACT_R5_SERIAL_SOURCE_FARKAS')

if __name__=='__main__':
    main()
