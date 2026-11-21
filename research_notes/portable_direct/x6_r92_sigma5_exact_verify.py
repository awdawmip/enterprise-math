#!/usr/bin/env python3
"""R92 author check: sigma=5 exact T-atlas, q>=11, and complete moment boxes.
No floating-point; equal positive/negative directions represented once.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json

S=Q(5)
S0=(10,-5,1)
R=(6,-4,1)
WALL={
    'a':(1,0,0), 'j':(4,-1,0), 'b':(5,-4,1), 'r':R,
    'c':(9,-5,1), 's':S0, 'd':(15,-9,2),
}

def canonical(a):
    return next((t for t in a if t),0)>0

def port(a):
    return max(sum(max(x,0) for x in a), sum(max(-x,0) for x in a))

def moments(a):
    x,y,z=a
    return x+3*y+6*z, 3*x+12*y+30*z, 7*x+39*y+126*z

def inverse(u,v,h):
    xx=19*u-8*v+h; yy=-14*u+7*v-h; zz=11*u-6*v+h
    if xx%2 or yy%3 or zz%12: return None
    return xx//2, yy//3, zz//12

def F(a,t):
    u,v,h=moments(a)
    gaps=(abs(u),abs(v),abs(h),abs(v-u),abs(h-u),abs(h-v))
    ds=(Q(2),Q(6),1+t,Q(6),1+t,S+t)
    return max(Q(g)/d for g,d in zip(gaps,ds))

def theory_value(t):
    if t<=1:return 1/(1+t)
    if t<=23:return Q(1,2)
    return 12/(1+t)

def full_ties(t,p):
    if t<11: return {S0}
    if t<13: return {S0,WALL['b'],WALL['c']}
    if t<23: return {S0,WALL['b'],WALL['c'],WALL['a']} | ({WALL['d']} if p>=17 else set())
    if t==23: return {S0,WALL['b'],WALL['c'],WALL['a'],WALL['j'],WALL['r']} | ({WALL['d']} if p>=17 else set())
    return {R}

def box_at_23():
    """Exhaust all F<=1/2 possibilities at (5,23) using the exact inverse."""
    out=[]
    for u,v,h in product(range(-1,2),(-3,0,3),range(-12,13)):
        if abs(v-u)>3 or abs(h-u)>12 or abs(h-v)>14:continue
        a=inverse(u,v,h)
        if a is not None and canonical(a) and F(a,Q(23))<=Q(1,2):out.append(a)
    return sorted(out)

def critical_t(a):
    u,v,h=moments(a)
    if abs(u)>1 or abs(v)>3 or abs(v-u)>3:return None
    return max(Q(0),2*max(abs(h),abs(h-u))-1,2*abs(h-v)-5)

def exhaustive(qmax=30):
    ts=[Q(1,2),Q(1),Q(10),Q(11),Q(12),Q(13),Q(20),Q(23),Q(24),Q(100)]
    cases=[(p,t) for p in [11,16,17,30] for t in ts]
    ties={case:[] for case in cases}; below={case:0 for case in cases}; count=0
    for a in product(range(-qmax,qmax+1),repeat=3):
        if a==(0,0,0) or not canonical(a):continue
        pa=port(a)
        if pa>qmax:continue
        count+=1
        for p,t in cases:
            if pa>p:continue
            f=F(a,t);opt=theory_value(t)
            if f<opt: below[p,t]+=1
            if f==opt: ties[p,t].append(a)
    for p,t in cases:
        assert below[p,t]==0, (p,t,below[p,t])
        assert set(ties[p,t])==full_ties(t,p),(p,t,ties[p,t],full_ties(t,p))
    return count, len(cases),len(cases)*count, [(p,str(t),len(ties[p,t])) for p,t in cases]

if __name__=='__main__':
    b=box_at_23()
    assert b==sorted(WALL.values()), (b,WALL)
    thresholds={k:critical_t(a) for k,a in WALL.items()}
    assert thresholds=={'a':13,'j':23,'b':11,'r':23,'c':11,'s':1,'d':13},thresholds
    cnt,ncases,upper,table=exhaustive()
    result={'schema':'EM_X6_R92_AUTHOR_EXACT_SIGMA5_ATLAS_V1',
      'frozen_input':'enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json',
      'domain':'conditional degree-four positive-count BRC star observer, weights (1,1,5,T), real T>0, integer p>=11',
      'moment_box_F_le_half_at_T23': [list(a) for a in b],
      'critical_t_for_F_le_half':{k:str(v) for k,v in thresholds.items()},
      'q_budgets':{k:port(v) for k,v in WALL.items()},
      'q_max_author_check':30,'tested_parameters':10,'port_cases':[11,16,17,30],
      'tested_direction_count_q_le_30':cnt,'total_case_count':ncases,
      'upper_bound_direction_case_comparisons':upper,
      'case_tie_counts':[list(z) for z in table],
      'all_case_assertions_pass':True,
      'logic':'moment-box enumeration covers all F<=1/2 in T in [1,23]; 0<T<1 and T>23 handled by integer congruence lemmas in note',
      'review':'AUTHOR_CHECKED_NOT_INDEPENDENTLY_REVIEWED'}
    with Path(__file__).with_name('x6_r92_sigma5_results.json').open('w') as f:
        json.dump(result,f,indent=2,ensure_ascii=False)
    print(json.dumps({k:result[k] for k in ('moment_box_F_le_half_at_T23','critical_t_for_F_le_half','tested_direction_count_q_le_30','total_case_count','upper_bound_direction_case_comparisons','all_case_assertions_pass')},indent=2))
