#!/usr/bin/env python3
"""Independent backward-risk and explicit first-hit enumeration, shared stop table only."""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
import json
import verify_n14_74 as spec

P,Q=spec.P,spec.Q
A,B=spec.A,spec.B
N=14
zero=F(0)

def transition(st, symbol):
    n,a,b=st
    return (n+1,a+(symbol==0),b+(symbol==1))

def decision(st):
    n,a,b=st
    if st in spec.SP:return 'P'
    if st in spec.SQ:return 'Q'
    t=N-n
    if 8*pow(3,a)>=9*pow(2,a+b+t):return 'P'
    if 8*pow(3,a+t)<9*pow(2,a+b+t):return 'Q'
    if n>=N:raise AssertionError(st)
    return 'C'

def backward(u,s):
    @lru_cache(None)
    def f(st):
        n=st[0]
        if st not in (A,B):
            v=decision(st)
            if v=='P':return (zero,F(1),zero,zero)
            if v=='Q':return (F(1),zero,zero,zero)
        kids=tuple(f(transition(st,i)) for i in range(3))
        cont=(sum((P[i]*kids[i][0] for i in range(3)),zero),
              sum((Q[i]*kids[i][1] for i in range(3)),zero),
              F(1)+sum((P[i]*kids[i][2] for i in range(3)),zero),
              F(1)+sum((Q[i]*kids[i][3] for i in range(3)),zero))
        if st==A:return tuple(u*x+(1-u)*v for x,v in zip((zero,F(1),zero,zero),cont))
        if st==B:return tuple(s*x+(1-s)*v for x,v in zip((F(1),zero,zero,zero),cont))
        return cont
    return f((0,0,0))

def enumerate_first_hit(target):
    total=0;pa=qa=F(0)
    def rec(st,x,y):
        nonlocal total,pa,qa
        if st==target:
            total+=1;pa+=x;qa+=y;return
        if st[0]>=target[0] or decision(st)!='C':return
        for i in range(3):rec(transition(st,i),x*P[i],y*Q[i])
    rec((0,0,0),F(1),F(1))
    return total,pa,qa

def descendants(st):
    counts=defaultdict(int)
    mass=defaultdict(lambda:(zero,zero))
    def rec(t,p,q):
        d=decision(t)
        if d!='C':
            tag=f'{t[0]},{t[1]},{t[2]}:{d}'
            counts[tag]+=1
            pp,qq=mass[tag];mass[tag]=(pp+p,qq+q)
            return
        for i in range(3):rec(transition(t,i),p*P[i],q*Q[i])
    rec(st,F(1),F(1))
    return [{'state_action':k,'suffix_words':counts[k],
             'suffix_P_prob':str(v[0]),'suffix_Q_prob':str(v[1])}
            for k,v in sorted(mass.items())]

def check():
    hits,pA,qA=enumerate_first_hit(A)
    b_hits,pB,qB=enumerate_first_hit(B)
    r00=backward(F(0),F(0));r10=backward(F(1),F(0));r01=backward(F(0),F(1));r11=backward(F(1),F(1))
    assert tuple(r11[i]-r10[i]-r01[i]+r00[i] for i in range(4))==(zero,)*4
    dA=[r10[i]-r00[i] for i in range(4)]
    dB=[r01[i]-r00[i] for i in range(4)]
    h=(dA[1]-dA[0])/(dB[0]-dB[1])
    eta=dA[0]+h*dB[0]
    S=spec.S
    e0=backward(F(0),S)
    e1=backward(F(1),S+h)
    assert (hits,b_hits)==(4158,12)
    assert (pA,qA)==(F(1203125,679477248), F(1203125,2579890176))
    assert h==F(345807,108800000)
    assert eta==F(6015625,22455364091904)
    assert e0[0]==e0[1]==spec.AL and e0[2]==spec.V
    assert e1[0]==e1[1]==spec.AL+eta and e1[2]==spec.V-spec.G*eta
    desc=descendants(A)
    assert sum(row['suffix_words'] for row in desc)==5
    assert sum(F(row['suffix_P_prob']) for row in desc)==1
    assert sum(F(row['suffix_Q_prob']) for row in desc)==1
    return {'method':'BACKWARD_BELLMAN_RISK_AND_EXPLICIT_DFS_FIRST_HITS',
     'status':'PASS','first_hit_A':hits,'first_hit_B':b_hits,
     'mass_A_P':str(pA),'mass_A_Q':str(qA),'mass_B_P':str(pB),'mass_B_Q':str(qB),
     'h74':str(h),'eta74':str(eta),'mixed_terms':[str(r11[i]-r10[i]-r01[i]+r00[i]) for i in range(4)],
     'r0':[str(x) for x in e0],'r1':[str(x) for x in e1],
     'descendants_of_A74':desc,
     'total_truncated_full_history_count':sum(x['suffix_words'] for x in desc)*hits,
     'claims':'author exact auxiliary finite model; shared inherited stop set; no independent Driver'}

if __name__=='__main__':print(json.dumps(check(),ensure_ascii=False,indent=2))
