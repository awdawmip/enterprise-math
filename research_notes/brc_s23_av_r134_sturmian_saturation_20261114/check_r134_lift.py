#!/usr/bin/env python3
"""Construct all R134 rational certificates with exact Fraction arithmetic."""
from fractions import Fraction as Q
from math import gcd
import json

def farey(m):
    return sorted({Q(p,q) for q in range(1,m+1) for p in range(q+1)})

def W(a,r,m):
    return ''.join(str((r+(i+1)*a).__floor__()-(r+i*a).__floor__()) for i in range(m))

def S(K,t,m):
    return ''.join(str(((K+i)*t).__floor__()-((K+i-1)*t).__floor__()) for i in range(m))

def lift(a,r,K):
    L=K-1
    N=(L*a-r+Q(1,2)).__floor__()
    return (N+r)/L

def F(m):
    def phi(n):return sum(gcd(i,n)==1 for i in range(1,n+1))
    return 1+sum((m+1-q)*phi(q) for q in range(1,m+1))

def run():
    rows=[];checks=0;bits=0
    for m in range(1,13):
        ff=farey(m); K0=4*m**3+2; ks=(K0,10**80+K0)
        observed={K0:set(),ks[1]:set()};cells=0
        for p,q in zip(ff,ff[1:]):
            a=(p+q)/2
            assert a.denominator<=2*m*m
            cuts=sorted({Q(0),Q(1)}|{(-j*a)%1 for j in range(m+1)})
            for lo,hi in zip(cuts,cuts[1:]):
                r=(lo+hi)/2
                w=W(a,r,m)
                margin=min(min((r+j*a)%1,1-(r+j*a)%1) for j in range(m+1))
                assert margin>=Q(1,4*m*m)
                cells+=1
                for K in ks:
                    t=lift(a,r,K)
                    assert 0<t<1
                    assert abs(t-a)<=Q(1,2*(K-1))<Q(1,8*m**3)
                    assert S(K,t,m)==w
                    observed[K].add(w)
                    bits=max(bits,t.numerator.bit_length(),t.denominator.bit_length())
                    checks+=1
        assert len(observed[K0])==len(observed[ks[1]])==F(m)
        rows.append({'m':m,'Farey_chambers':len(ff)-1,'certificates':cells,
                     'words':F(m),'K_threshold':K0})
    return {'result':'R134_CONSTRUCTIVE_ALL_WORDS_LIFT_PASS','m_range':'1..12',
            'certificate_checks':checks,'max_certificate_bits':bits,
            'K_bound':'4*m^3+2','rows':rows}

if __name__=='__main__':print(json.dumps(run(),indent=2))
