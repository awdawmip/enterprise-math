#!/usr/bin/env python3
"""Pure upper nuisance endpoint certificates near all n=30 E-Bayes count transitions K=17..29."""
from fractions import Fraction as F
from EC49FUT_N30_HIGH_COUNT_WINDOWS_VERIFY import I,E,delta,gap,deriv_tail,exact_bracket,DEN
WINDOWS={
 17:(472,477,474356338011,474356338012),
 18:(513,518,515357839408,515357839409),
 19:(554,559,556358678282,556358678283),
 20:(595,600,597318517188,597318517189),
 21:(636,641,638205356397,638205356398),
 22:(676,681,678993711821,678993711822),
 23:(717,722,719663237873,719663237874),
 24:(758,763,760197675211,760197675212),
 25:(798,803,800584038553,800584038554),
 26:(838,843,840811983841,840811983842),
 27:(878,883,880873310863,880873310864),
 28:(918,923,920761569134,920761569135),
 29:(958,963,960471743261,960471743262),
}
def verify_one(j,lo,hi,exit_lo,exit_hi,slabs=128):
    a,b=F(lo,1000),F(hi,1000)
    assert a<F(exit_lo,DEN)<F(exit_hi,DEN)<b
    exact_bracket(lambda x:delta(j,x,E),(exit_lo,exit_hi),False)
    assert gap(j,F(exit_hi,DEN))<0
    assert delta(j,a,E)>0>delta(j,b,E)
    minima={}
    for i in range(slabs):
        x=I(a+(b-a)*i/slabs,a+(b-a)*(i+1)/slabs)
        vals={'E_prev_negative':-delta(j-1,x,E).hi,
              'E_next_positive':delta(j+1,x,E).lo,
              'H_negative':-gap(j+1,x).hi,
              'Gprime_positive':(deriv_tail(j,x,E)-deriv_tail(j,x,F(0))).lo}
        for key,v in vals.items():
            assert v>0,(j,i,key,float(v))
            minima[key]=min(minima.get(key,v),v)
    print('PASS',j,'interval',lo,hi,'exit',exit_lo,exit_hi,
          'min-margins',','.join(f'{k}:{float(v):.8g}' for k,v in minima.items()))
if __name__=='__main__':
    for j,(a,b,l,r) in WINDOWS.items():verify_one(j,a,b,l,r)
    print('ALL PURE-E HIGH TAIL PASS')
