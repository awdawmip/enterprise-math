#!/usr/bin/env python3
"""R127.5 exact modular two-integer reduction checker; Python 3 Fraction-only."""
from fractions import Fraction as F
from math import gcd,floor
from random import Random
from check_r127 import shortest_relation,full_reference,member,floor_range,exact_interval,add_interval
import json

def oracle(x,A,d,E,m,l,h,bits):
    g=gcd(A,d)
    if not g: raise ValueError('A=d=0 has a separate one-floor route')
    q=g//gcd(g,E)
    U,V=shortest_relation(A,d,q*E)
    assert U*A+V*d==q*E
    L=min(0,U)+min(0,V)-U*x
    H=max(0,U)+max(0,V)-U*x
    s_vals=range(floor(L),floor(H)+1)
    vocab=[]
    for mask in range(1<<(m-1)):
        w=[0]
        for i in range(m-1):w.append(w[-1]+((mask>>i)&1))
        vocab.append(w)
    checked=0
    for n in floor_range(A,x,l,h):
      for k in floor_range(d,F(0),l,h):
       for s in s_vals:
        T=U*n+V*k+s
        zeta=T%q  # the unique surviving residue among q modular branches
        assert 0<=zeta<q and (T-zeta)%q==0
        r=(T-zeta)//q
        for w in vocab:
            checked+=1
            conditions=[]
            add_interval(conditions,A,x-n,0,1)
            add_interval(conditions,d,-F(k),0,1)
            add_interval(conditions,E,-F(r),0,1)
            for i in range(m):
                slope=A+i*d;intercept=x-n-i*k-w[i]
                add_interval(conditions,slope,intercept,0,1)
                b_slope=E-slope;b_intercept=-r-intercept
                if bits[i]:conditions.append((b_slope,b_intercept,True))
                else:conditions.append((-b_slope,-b_intercept,False))
            theta=exact_interval(conditions,l,h)
            if theta is not None:
                assert member(x,A,d,E,m,theta)==bits
                return theta,checked,q,U,V
    return None,checked,q,U,V

def run():
    rr=Random(127052026)
    stat={'random_cases':0,'word_queries':0,'positive_witnesses':0,'critical_representatives':0,'checked_candidate_systems':0,'nontrivial_denominator_cases':0,'max_q':0,'large_signed_forward':0}
    for _ in range(90):
        A=rr.randint(-7,7);d=rr.randint(-7,7);E=rr.randint(-10,10)
        if gcd(A,d)==0: continue
        x=F(rr.randint(-4,4),rr.randint(1,9))
        l=F(rr.randint(-6,-1),6);h=F(rr.randint(1,6),6)
        m=rr.randint(2,4)
        ref,count=full_reference(x,A,d,E,m,l,h)
        stat['critical_representatives']+=count
        for mask in range(1<<m):
            bits=tuple((mask>>i)&1 for i in range(m))
            witness,checked,q,U,V=oracle(x,A,d,E,m,l,h,bits)
            stat['word_queries']+=1
            stat['checked_candidate_systems']+=checked
            assert (witness is not None)==(bits in ref),(x,A,d,E,m,l,h,bits,q,U,V)
            if witness is not None:stat['positive_witnesses']+=1
        stat['max_q']=max(stat['max_q'],q)
        if q>1:stat['nontrivial_denominator_cases']+=1
        stat['random_cases']+=1
    for sign in (1,-1):
        A=sign*(10**90+3)*6
        d=sign*(10**90+3)*10
        E=sign*(10**90+3)*3
        g=gcd(A,d);q=g//gcd(g,E)
        assert q==2
        U,V=shortest_relation(A,d,q*E)
        assert U*A+V*d==q*E
        theta=F(1,10**93+13);x=F(1,7)
        n=floor(x+A*theta);k=floor(d*theta)
        alpha=x+A*theta-n;beta=d*theta-k
        s=floor(U*alpha+V*beta-U*x)
        r=(U*n+V*k+s-((U*n+V*k+s)%q))//q
        assert r==floor(E*theta)
        stat['large_signed_forward']+=1
    print('R127_MODULAR_TWO_INTEGER_PASS')
    print(json.dumps(stat,indent=2))
    with open('verification_modq_r127.json','w') as f:
        json.dump({'status':'R127_MODULAR_TWO_INTEGER_PASS','seed':127052026,'result':stat,'scope':'exact small signed full critical-atom comparisons; huge signed positive modular certificates; no production 2D ILP solver'},f,indent=2)
if __name__=='__main__':run()
