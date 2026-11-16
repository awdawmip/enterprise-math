#!/usr/bin/env python3
"""Exact rational verification of sharp asymmetric time-gap/TV certificates in frozen R5 model.
Analytic identities in RESEARCH.md establish all-real theorem; enumeration checks finite vertices.
"""
from fractions import Fraction as Q
from itertools import product

Q3 = ((Q(13,20), Q(1,5), Q(3,20)),
      (Q(1,40), Q(9,20), Q(21,40)))
ALPHA, BETA = Q(47,180), Q(67,162)
R = (Q(1,10), Q(1,2), Q(3,4), Q(1), Q(5,4), Q(3,2), Q(19,10))

def check(g, u0, u1, x):
    assert Q(0) <= g <= Q(1) and Q(0) <= u0 <= g and Q(0) <= u1 <= g
    cap = tuple(tuple(ui*Q3[i][j]/2 for j in range(3)) for i,ui in enumerate((u0,u1)))
    assert all(Q(0) <= x[i][j] <= cap[i][j] for i in range(2) for j in range(3))
    X = tuple(sum(x[i][j] for i in range(2)) for j in range(3))
    V = tuple(sum(cap[i][j] for i in range(2)) for j in range(3))
    J = ALPHA*x[0][1]+BETA*x[1][1]
    m = {
      Q(1,10): (509*X[0]+9*X[2])/900+J,
      Q(1,2): V[0]-X[0],
      Q(3,4): (g-u0)/2,
      Q(1): 1-g+V[1]+Q(382,900)*(X[0]+X[2])-2*J,
      Q(5,4): (g-u1)/2,
      Q(3,2): V[2]-X[2],
      Q(19,10): (9*X[0]+509*X[2])/900+J,
    }
    assert min(m.values()) >= 0 and sum(m.values())==1
    assert sum(r*m[r] for r in R)==1
    TQ=1+g+(u0+u1)/2+sum(X)
    TP=1+g+(3*u0+5*u1)/8+X[0]/2+X[1]+3*X[2]/2
    d=TP-TQ
    assert d==(u1-u0)/8+(X[2]-X[0])/2
    S = sum((1-r)*m[r] for r in R if r<1)
    assert S==g/8+3*u0/80+u1/160+Q(9,1000)*(X[0]+X[2])+Q(9,10)*J
    G=(TQ-1)/8-S
    a=u0/10-x[0][1]
    b=9*u1/40-x[1][1]
    assert a>=0 and b>=0
    assert G==Q(7,500)*u0+Q(1,1600)*u1+Q(29,250)*(X[0]+X[2])+Q(11,100)*a+Q(89,360)*b
    plus=Q(117,8000)*u0+Q(237,2000)*X[0]+Q(227,2000)*X[2]+Q(11,100)*a+Q(89,360)*b
    minus=Q(117,8000)*u1+Q(3,50)*X[0]+Q(43,250)*X[2]+Q(11,100)*a+Q(89,360)*b
    assert G-d/200==plus>=0
    assert G+Q(14,125)*d==minus>=0
    assert S <= (TQ-1)/8-Q(1,200)*max(d,0)-Q(14,125)*max(-d,0)
    return S, TQ, TP, G, plus, minus, m

def main():
    # All extreme deterministic stopping decisions at the 1+2+6 continuation nodes.
    count=0
    nzpos=nzneg=0
    bestpos=None
    bestneg=None
    for g,u0k,u1k in product((Q(0),Q(1)),repeat=3):
        u0,u1=g*u0k,g*u1k
        caps=tuple(tuple(ui*Q3[i][j]/2 for j in range(3)) for i,ui in enumerate((u0,u1)))
        for bits in product((0,1),repeat=6):
            x=((bits[0]*caps[0][0],bits[1]*caps[0][1],bits[2]*caps[0][2]),
               (bits[3]*caps[1][0],bits[4]*caps[1][1],bits[5]*caps[1][2]))
            S,tq,tp,G,P,M,_=check(g,u0,u1,x)
            if tp>tq:
                nzpos+=1
                rat=G/(tp-tq)
                bestpos=rat if bestpos is None else min(bestpos,rat)
            elif tp<tq:
                nzneg+=1
                rat=G/(tq-tp)
                bestneg=rat if bestneg is None else min(bestneg,rat)
            count+=1
    assert count == 512 and bestpos==Q(1,200) and bestneg==Q(14,125)
    # Explicit sharpness examples. Declare P at every stopped ratio r<1 and Q at r>=1.
    for side,g,u0,u1 in (('positive',Q(1),Q(0),Q(1)),('negative',Q(1),Q(1),Q(0))):
        caps=tuple(tuple(ui*Q3[i][j]/2 for j in range(3)) for i,ui in enumerate((u0,u1)))
        x=((Q(0),caps[0][1],Q(0)),(Q(0),caps[1][1],Q(0)))
        S,tq,tp,G,P,M,m=check(g,u0,u1,x)
        eq=sum(m[r] for r in R if r<1)
        ep=1-sum(r*m[r] for r in R if r<1)
        assert ep+eq-1==S and eq>=0 and ep>=0
        if side=='positive':
            assert (tq,tp,S,G,P)==(Q(109,40),Q(57,20),Q(43,200),Q(1,1600),Q(0))
        else:
            assert (tq,tp,S,G,M)==(Q(13,5),Q(99,40),Q(93,500),Q(7,500),Q(0))
        print(side, 'time_Q=',tq,'time_P=',tp,'S=',S,'gap=',G,'error_P=',ep,'error_Q=',eq)
    # Non-extreme interior, including different x histories at same LR.
    fractions=(Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1))
    randomchecks=0
    for g,u0f,u1f in product((Q(1,3),Q(2,3)),repeat=3):
        u0,u1=g*u0f,g*u1f
        caps=tuple(tuple(ui*Q3[i][j]/2 for j in range(3)) for i,ui in enumerate((u0,u1)))
        for k in range(250):
            z=[fractions[(k+j*(3+j)+k//(j+2))%5] for j in range(6)]
            x=tuple(tuple(z[3*i+j]*caps[i][j] for j in range(3)) for i in range(2))
            check(g,u0,u1,x)
            randomchecks+=1
    assert randomchecks==2000
    print('PASS_EXACT_R5_SHARP_ASYMMETRIC_TIME_GAP_TV_CERTIFICATES')
    print('deterministic checks=',count,'interior rational checks=',randomchecks)
    print('positive time-gap ratio min=',bestpos,'negative time-gap ratio min=',bestneg)
    print('certificates: G-(TP-TQ)/200 >= 0 ; G+14(TP-TQ)/125 >= 0')

if __name__=='__main__':main()
