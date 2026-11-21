#!/usr/bin/env python3
"""R93 author check: two-parameter low-T sharp-loss wedge, exact rational arithmetic."""
from itertools import product
from fractions import Fraction as Q
import json
from pathlib import Path

s=(10,-5,1); b=(14,-9,2); c=(24,-14,3)

def port(a):return max(sum(max(x,0) for x in a),sum(max(-x,0) for x in a))
def moments(a):
    x,y,z=a
    return x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z

def score(a,S,T):
    u,v,h=moments(a)
    return max(Q(g)/den for g,den in zip((abs(u),abs(v),abs(h),abs(v-u),abs(h-u),abs(h-v)),(Q(2),1+S,1+T,1+S,1+T,S+T)))

def expect(p,S,T):
    R=1/(1+T)
    A=5+6*T; B=6+5*T
    if p>=27 and S>B:return 'improved',None
    ties={s}
    if S>=A and p>=16: ties.add(b)
    if S==B and p>=27: ties.add(c)
    return 'flat',ties

def check(qmax=27):
    cases=[]
    for T in (Q(1,3),Q(1,2),Q(3,4)):
        A,B=5+6*T,6+5*T
        for S in (Q(5),A-Q(1,10),A,(A+B)/2,B,B+Q(1,10)):
            for p in (11,15,16,26,27):cases.append((p,S,T))
    tied={i:[] for i in range(len(cases))}; below=[0]*len(cases); count=0
    for a in product(range(-qmax,qmax+1),repeat=3):
        if a==(0,0,0) or next((v for v in a if v),0)<=0:continue
        if port(a)>qmax:continue
        count+=1
        for i,(p,S,T) in enumerate(cases):
            if port(a)>p:continue
            z=score(a,S,T)-1/(1+T)
            if z<0:below[i]+=1
            elif z==0:tied[i].append(a)
    for i,(p,S,T) in enumerate(cases):
        typ,ties=expect(p,S,T)
        if typ=='flat':
            assert below[i]==0,(p,S,T,below[i])
            assert set(tied[i])==ties,(p,S,T,tied[i],ties)
        else:
            assert below[i]>0,(p,S,T)
            assert score(c,S,T)<1/(1+T),(p,S,T)
    return {'schema':'EM_X6_R93_LOW_T_WEDGE_AUTHOR_CHECK_V1',
      'frozen_input':'enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json',
      'tested_T':['1/3','1/2','3/4'],'sigma_cases_per_T':6,
      'port_cases':[11,15,16,26,27],'q_limit':qmax,
      'unoriented_directions':count,'parameter_port_cases':len(cases),
      'upper_bound_comparisons':count*len(cases),
      'flat_cases':sum(expect(*v)[0]=='flat' for v in cases),
      'improved_cases':sum(expect(*v)[0]=='improved' for v in cases),
      'all_assertions_pass':True,
      'scope':'Finite q<=27 exact crosscheck; unbounded claims rely on congruence and Port lemmas in companion note.',
      'review':'AUTHOR_CHECKED_NOT_INDEPENDENTLY_REVIEWED'}

if __name__=='__main__':
    out=check()
    Path(__file__).with_name('x6_r93_lowT_wedge_results.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(out,indent=2,ensure_ascii=False))
