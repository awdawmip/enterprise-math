#!/usr/bin/env python3
"""Exact finite regressions for the unreviewed auxiliary four-label BRC one-episode theorem.
Finite tests are not a substitute for the adjacent infinite symbolic proof.
"""
from fractions import Fraction as F
from itertools import product
import json

GOOD = (0b0011,0b0110,0b1010,0b1100)
ZS=[F(i,8) for i in range(9)]+[F(99,100),F(999,1000),F(1,7),F(5,9)]

def occ(a,b,z):
    n=a+b
    if n==0: return F(0)
    if a==0:
        v=2**b+(2+z)**b+(2-z)**b-2*(1+z)**b-2*(1-z)**b-2
    elif b==0:
        v=2**(a+1)-4
    else:
        v=(2**a-3)*(1+z)**b+2**a*(2+z)**b+2**b+(2-z)**b-2
    return F(v,3**n)

def mask_dp(word,z):
    v=[F(0)]*16
    v[0]=F(1)
    q={0:(F(0),(1+z)/3,(1-z)/3,F(1,3)),2:(F(1,3),F(1,3),F(0),F(1,3))}
    for action in word:
        w=[F(0)]*16
        for mask,mass in enumerate(v):
            if mass:
                for i,p in enumerate(q[action]):
                    if p: w[mask|(1<<i)]+=mass*p
        v=w
    return sum((v[i] for i in GOOD),F(0))

def E(n,z):
    m=n-1
    return 4-2**m-(1-z)*(2+z)**m-(1+z)*(2-z)**m+2*(2-z)*(1+z)**m+2*(2+z)*(1-z)**m

def Z(n,z):
    m=n-2
    return 4-2**m-2*(1-z)*(2+z)**m-(1+z)*(2-z)**m+(2-z)*(1+z)**m

def check_word(word,z):
    a=b=0
    old=M=S=Rold=F(0)
    gains=[]
    second=None
    for n,action in enumerate(word,1):
        if action==2:
            a+=1
            if a==2:second=n
        else:b+=1
        d=occ(a,b,z)
        D=d-old
        S+=max(F(0),D)
        M=max(M,d)
        R=S-M
        assert R>=Rold>=0
        if n>=2 and R>Rold:gains.append(n)
        if a==0:assert R==0
        if second is not None and n>=second:assert R==Rold
        old,Rold=d,R
    assert gains==list(range(gains[0],gains[-1]+1)) if gains else True
    return bool(gains)

def main():
    counts={'parameters':len(ZS),'zero_increment_recurrences':0,'zero_action_exact_values':0,
            'post_pulse_monotonicity':0,'masked_dp_crosschecks':0,
            'whole_word_residual_cases':0,'words_with_positive_residual_growth':0,
            'single_growth_episode_pass':True}
    for z in ZS:
        for n in range(2,81):
            r,s,u,v=1+z,1-z,2+z,2-z
            m=n-1
            h=r*v**m-s*u**m
            assert h<=2*z
            diff=E(n+1,z)-2*E(n,z)
            assert diff==-4+z*h-2*v*s*r**m-2*u*r*s**m
            assert diff<=-2
            assert E(n,z)==3**n*(occ(0,n,z)-occ(0,n-1,z))
            counts['zero_increment_recurrences']+=1
            counts['zero_action_exact_values']+=1
        assert E(2,z)==6-2*z*z>0
        for n in range(3,81):
            gap=Z(n,z)-Z(n+1,z)
            if z==1:assert gap==0
            else:assert gap>0
            counts['post_pulse_monotonicity']+=1
        for n in range(1,12):
            for word in product((0,2),repeat=n):
                if check_word(word,z):counts['words_with_positive_residual_growth']+=1
                counts['whole_word_residual_cases']+=1
        for n in range(1,9):
            for word in product((0,2),repeat=n):
                assert occ(word.count(2),word.count(0),z)==mask_dp(word,z)
                counts['masked_dp_crosschecks']+=1
    print(json.dumps(counts,sort_keys=True))
    return counts

if __name__=='__main__':main()
