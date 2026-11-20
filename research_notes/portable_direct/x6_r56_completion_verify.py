#!/usr/bin/env python3
"""R56: named BRC four-word mass enumeration and exact rational interval certificates.
Checks finite rational inputs, not the universal argument in the accompanying paper.
"""
from fractions import Fraction as Q
import json

WORDS = ('F', 'FT', 'FF', 'FRF')

def step(s, evt):
    a,b,occup,turned = s
    if evt == 'R':
        return (a,b,0,turned) if occup else None
    if evt == 'T':
        if turned or occup or ((a<0)==(b<0)):
            return None
        v = a if a>=0 else b
        return (a,b,(1 if a>=0 else 2) if v==0 else 0,1)
    side,i=evt[0],int(evt[1:])
    if side=='A':
        if a>=0 or (i==0 and occup):return None
        return (i,b,1 if i==0 else occup,turned)
    if b>=0 or (i==0 and occup):return None
    return (a,i,2 if i==0 else occup,turned)

def named_mass(word,p):
    frontier=[((-1,-1,0,0),0,0)]
    for e in word:
        choices=([f'A{i}' for i in range(p)]+[f'B{i}' for i in range(p)]) if e=='F' else [e]
        new=[]
        for st,a,b in frontier:
            for choice in choices:
                nxt=step(st,choice)
                if nxt is not None:new.append((nxt,a+(choice.startswith('A')),b+(choice.startswith('B'))))
        frontier=new
    count={}
    for _,a,b in frontier:count[(a,b)]=count.get((a,b),0)+1
    return count

def mass(p,S,P):
    return (p*S,(p-1)*S,2*(p*p-1)*P,2*p*P)

def B(q,P):
    C=q*q-q-1
    return Q(abs(4-q),1)*(C+2*P*(4*q+1))/(4*q*q*(q-1))

checks=0
for p in range(1,13):
    expected=[{(1,0):p,(0,1):p},
              {(1,0):p-1,(0,1):p-1} if p>1 else {},
              {(1,1):2*(p*p-1)} if p>1 else {},
              {(1,1):2*p}]
    for word, ref in zip(WORDS,expected):
        got=named_mass(word,p)
        assert got==ref,(p,word,got,ref)
        checks+=1

# Five exact rational points on q=5 equal-source witness locus P=(19/44)*s^2.
rational_s=[Q(73,100),Q(731,1000),Q(37,50),Q(3,4),Q(19,25)]
rows=[]
for s in rational_s:
    P=Q(19,44)*s*s
    assert Q(23,100)<=P<=Q(1,4)
    t=s*s/4
    r=[x-y for x,y in zip(mass(4,Q(1),P),mass(5,s,t))]
    eta=(max(r)-min(r))/4
    expected=s-Q(3,4)+Q(21,38)*P
    assert eta==expected and r[2]==r[3] and r[1]<=r[0]<=r[2]
    assert eta<Q(3,20)
    for q in [2,3,8,9,10,12,30,100]:
        assert B(q,P)>Q(3,20),(P,q,B(q,P))
    assert (Q(357,380)-Q(21,38)*P)<Q(41,50)
    rows.append({'P':str(P),'s_5':str(s),'t_5':str(t),'eta':str(eta),'residuals':list(map(str,r))})

# Exact rational endpoint/certificate checks; universal inequalities in manuscript.
assert Q(3087,3800)<Q(41,50)
assert Q(2191,3625)<Q(61,100)
assert Q(169,2500)<Q(223,2900)
assert Q(5743,12300)<Q(1,2)
assert Q(46,25)>Q(44,25)
assert Q(3509,22400)>Q(3,20)
assert Q(61,400)>Q(3,20)
assert Q(841,577600)>0
assert Q(6210161,361000000)>0

out={'schema':'X6_R56_GLOBAL_PORT_RADIUS_COMPLETION_V1','status':'PASS',
     'scope':'conditional R44 positive named whole-triad BRC four-word observer; 23/100<=P<=1/4; rational sample checks, not independent review',
     'named_polynomial_checks':checks,'rational_q5_witnesses':rows,
     'exact_bound_checks':'PASS',
     'theorem':'eta_crit(P)=2*sqrt(11P/19)-3/4+21P/38 on 23/100<=P<=1/4',
     'other_port_proof':'q=1,2,3 and q>=8: contrast; q=6,7: positivity+residual contradictions; universal proof in manuscript',
     'native_admission':'NOT_PROVED','independent_review':'NOT_REVIEWED'}
print(json.dumps(out,ensure_ascii=False,indent=2))
