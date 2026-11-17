#!/usr/bin/env python3
from fractions import Fraction
from math import log
p,m=101,11
tau=Fraction(3,8)
A=set(range(m,p))
S={(x+m)%p for x in A}
assert len(A)==len(S)==p-m and len(A&S)==p-2*m
a=tau*Fraction(p-m,p)
assert a==Fraction(135,404)
def exceptional(q):
    return [u for u in range(p) if (
        (Fraction(1)-q if u in A else Fraction(0))+
        (q if u in S else Fraction(0)))/ (p-m) < tau/p]
assert len(exceptional(a))==0
assert len(exceptional(Fraction(1,2)))==0
assert len(exceptional(1-a))==0
assert len(exceptional(a-Fraction(1,1000)))==m
assert len(exceptional(1-a+Fraction(1,1000)))==m
q=float(a)
print({'p':p,'m':m,'q_min':str(a),
       'minimum_shared_entropy_nats':-q*log(q)-(1-q)*log(1-q),
       'inside_exception_count':0,'outside_exception_count':m})
