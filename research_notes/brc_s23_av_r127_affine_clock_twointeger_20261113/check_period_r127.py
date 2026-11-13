#!/usr/bin/env python3
from fractions import Fraction as Q
from math import gcd
import random, json
rng=random.Random(127042026)
def obs(x,A,d,E,m,theta):
    L=(E*theta)%1
    return tuple(int(((x+(A+i*d)*theta)%1)<L) for i in range(m))
count=0
for _ in range(1000):
    A=rng.randint(-20,20); d=rng.randint(-20,20); E=rng.randint(-20,20)
    g=gcd(gcd(A,d),E)
    if g==0:
        assert obs(Q(2,7),A,d,E,3,Q(1,5))==(0,0,0)
        continue
    x=Q(rng.randint(-17,17),rng.randint(2,17))
    theta=Q(rng.randint(-100,100),rng.randint(1,47))
    t=rng.randint(-100000,100000)
    m=rng.randint(1,6)
    assert obs(x,A,d,E,m,theta)==obs(x,A,d,E,m,theta+Q(t,g))
    count+=1
assert obs(Q(0),0,1,1,1,Q(0))==(0,)
assert all(obs(Q(0),0,1,1,1,Q(k,100))==(1,) for k in range(1,100))
assert obs(Q(0),0,1,1,1,Q(1))==(0,)
summary={'status':'R127_GCD_PERIOD_PASS','exact_period_shift_checks':count,'critical_open_interval_example':{'A':0,'d':1,'E':1,'x':'0','m':1,'period':'1','open_J':'(0,1)','open_J_only_signature':[1],'full_period_signatures':[[0],[1]]}}
print('R127_GCD_PERIOD_PASS',count)
with open('verification_period_r127.json','w') as f:json.dump(summary,f,indent=2)
