#!/usr/bin/env python3
"""Exact rational 128-slab certificate for n=30 second mixed-support window (K=10)."""
from fractions import Fraction as F
from EC49FUS_N30_MIXED_WINDOW_VERIFY import Interval, E, mass, tail, derivative_tail, mix
A, C = F(93,500), F(49,250)
ENTER_L, ENTER_R = F(186867177194,10**12), F(186867177196,10**12)
EXIT_L, EXIT_R = F(194151512437,10**12), F(194151512439,10**12)

def gap(x):return tail(10,x,E)-tail(10,x,F(0))
def h(x):return tail(11,x,E)-tail(11,x,F(0))
def verify():
    assert gap(ENTER_L)<0<gap(ENTER_R)
    assert mass(10,EXIT_L,E)>0>mass(10,EXIT_R,E)
    assert gap(A)<0 and gap(C)>0
    margins={k:None for k in ('E9neg','Z10neg','Z11neg','E11pos','M3_4_10neg','M1_3_11pos','Hneg','Gprimepos')}
    for i in range(128):
        x=Interval(A+(C-A)*i/128,A+(C-A)*(i+1)/128)
        d={
          'E9neg':-mass(9,x,E).hi,
          'Z10neg':-mass(10,x,F(0)).hi,
          'Z11neg':-mass(11,x,F(0)).hi,
          'E11pos':mass(11,x,E).lo,
          'M3_4_10neg':-mix(10,x,F(3,4)).hi,
          'M1_3_11pos':mix(11,x,F(1,3)).lo,
          'Hneg':-F(1,100)-h(x).hi,
          'Gprimepos':(derivative_tail(10,x,E)-derivative_tail(10,x,F(0))).lo-F(1,4),
        }
        for k,v in d.items():
            assert v>0,(i,k,float(v))
            if margins[k] is None or v<margins[k]:margins[k]=v
    print('PASS second n30 mixed window; 128 exact slabs')
    print({k:round(float(v),12) for k,v in margins.items()})
    print('entry',float(ENTER_L),float(ENTER_R),'exit',float(EXIT_L),float(EXIT_R))
    for x in (A,F(19,100),F(194,1000)):
        d=mass(10,x,E)-mass(10,x,F(0))
        lam=-mass(10,x,F(0))/d;gam=-h(x)/d
        print('x',float(x),'lambda',round(float(lam),12),'gamma',round(float(gam),12))
if __name__=='__main__':verify()
