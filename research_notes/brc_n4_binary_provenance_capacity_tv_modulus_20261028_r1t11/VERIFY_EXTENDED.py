#!/usr/bin/env python3
"""Exact Fraction verifier for a two-law N4 BRC provenance-capacity bound.
Only finite tests are executed. The all-real theorem is proved in PROOF.md.
"""
from fractions import Fraction as F
from random import Random
import json

Z, O = F(0), F(1)
N = {1: {'A': (F(1,2), F(1,2)), 'B':(F(1,2),F(3,2))},
     2: {'AU':(F(1,6),O), 'AV':(F(1,3),F(1,4)),
         'BU':(F(1,4),O), 'BV':(F(1,4),F(2))}}
for t in (3,4):
    N[t]={}
    for h,(q,r) in N[t-1].items():
        e=({'AU':F(1,10),'AV':Z,'BU':F(4,5),'BV':Z}[h]
           if t==3 else Z if h=='AV0' else F(3,50) if h=='AV1' else F(1,20))
        for j,sgn in (('0',-1),('1',1)):
            N[t][h+j]=(q/2,r*(1+sgn*e))
for t in N:
    assert sum((q for q,r in N[t].values()),Z)==O
    assert sum((q*r for q,r in N[t].values()),Z)==O
    assert min(q for q,r in N[t].values())>Z
    assert min(r for q,r in N[t].values())>Z

def target(a,b,ca,cb):
    p={(1,'A'):(Z,O-a,a),(1,'B'):(Z,O-b,b)}
    for h,c in (('AU',ca),('BU',cb),('AV',Z),('BV',Z)):
        p[2,h]=(Z,O-c,c)
    for h in N[3]:p[3,h]=(O,Z,Z) if h.startswith('AU') else (Z,O,Z)
    for h in N[4]:p[4,h]=(Z,O,Z)
    return p

def upper(a,b,ca,cb):
    alpha,beta=a/6,b/4
    c=(alpha*ca+beta*cb)/(alpha+beta)
    return target(a,b,c,c),alpha*beta*abs(ca-cb)/(alpha+beta)

def law(p,tag):
    out={'Q':{},'P':{}}
    for leaf,(q,r) in N[4].items():
        alive=O
        for t in range(1,5):
            h=leaf[:t]
            pp,qq,cc=p[t,h]
            assert pp>=0 and qq>=0 and cc>=0 and pp+qq+cc==O
            assert (t!=4 or cc==Z)
            z=int(t>=3 and h.startswith(tag))
            for d,v in (('P',pp),('Q',qq)):
                k=(t,d,z)
                out['Q'][k]=out['Q'].get(k,Z)+q*alive*v
                out['P'][k]=out['P'].get(k,Z)+q*r*alive*v
            alive*=cc
        assert alive==Z
    for m in out:assert sum(out[m].values(),Z)==O
    return out

def TV(p,q,m):
    return sum((abs(p[m].get(k,Z)-q[m].get(k,Z))
                for k in p[m].keys()|q[m].keys()),Z)/2

def mass(p,m,pred):
    return sum((v for k,v in p[m].items() if pred(k)),Z)

def randrow(rng,terminal=False):
    pp=F(rng.randrange(15),14)
    qq=(O-pp)*F(rng.randrange(15),14)
    return (pp,O-pp,Z) if terminal else (pp,qq,O-pp-qq)

def random_strategy(rng):
    p={}
    p[1,'A']=randrow(rng);p[1,'B']=randrow(rng)
    shared=randrow(rng)
    for h in N[2]:p[2,h]=shared if h in ('AU','BU') else randrow(rng)
    for t in (3,4):
        byratio={}
        for h,(q,r) in N[t].items():
            if r not in byratio:byratio[r]=randrow(rng,t==4)
            p[t,h]=byratio[r]
    return p

def constants(a,b):
    r,R=b/a,a/b
    cqA=max((4+6*r)/7,F(8,7))
    cpA=max(F(2,3),(6*r+4)/21)
    cqB=(3+2*R)/7+max(F(1,7),(2*R+3)/28)
    cpB=max(F(4,7),(2*R+3)/14)
    return cqA,cpA,cqB,cpB

def case(a,b,ca,cb,n,rng):
    F0=target(a,b,ca,cb)
    G0,k=upper(a,b,ca,cb)
    cqA,cpA,cqB,cpB=constants(a,b)
    excessA=(3*b*(cb-ca)-7*a)/21
    excessB=(2*a*(ca-cb)-7*b)/28
    lowerA=max(Z,excessA)/(cqA+cpA)
    lowerB=max(Z,excessB)/(cqB+cpB)
    assert lowerA<=k and lowerB<=k
    for tag in ('AU','BU'):
        f=law(F0,tag);g=law(G0,tag)
        assert TV(f,g,'Q')==TV(f,g,'P')==k
    for _ in range(n):
        G=random_strategy(rng)
        aa,bb,c=G[1,'A'][2],G[1,'B'][2],G[2,'AU'][2]
        assert G[2,'BU']==G[2,'AU']
        x=aa*G[2,'AV'][2]/3
        y=bb*G[2,'BV'][2]/4
        s=(aa-a+bb-b)/2
        t=(aa-a+3*(bb-b))/4
        for tag in ('AU','BU'):
            f,g=law(F0,tag),law(G,tag)
            h=mass(f,'Q',lambda k:k[2]==1)-mass(g,'Q',lambda k:k[2]==1)
            zq=mass(f,'Q',lambda k:k[0]==2)-mass(g,'Q',lambda k:k[0]==2)
            zp=mass(f,'P',lambda k:k[0]==2)-mass(g,'P',lambda k:k[0]==2)
            assert s==mass(f,'Q',lambda k:k[0]==1)-mass(g,'Q',lambda k:k[0]==1)
            assert t==mass(f,'P',lambda k:k[0]==1)-mass(g,'P',lambda k:k[0]==1)
            M=max(TV(f,g,'Q'),TV(f,g,'P'))
            if tag=='AU':
                r= b/a
                gcap=excessA
                eq=gcap+(4+6*r)*h/7+(1+c*(3*r+1))*s/7 \
                    +(2-6*c*(r+1))*t/21+8*zq/7-4*zp/7
                assert x-aa/3==eq
                assert M>=lowerA
            else:
                R=a/b
                gcap=excessB
                eq=gcap+(3+2*R)*h/7+(F(3,28)-c*(R+3)/14)*s \
                    +(F(1,14)+c*(R+1)/7)*t+4*zp/7-zq/7
                assert y-bb/4==eq
                assert M>=lowerB
    return {'input':list(map(str,(a,b,ca,cb))),
            'AU_lower':str(lowerA),'BU_lower':str(lowerB),'upper_both':str(k),
            'random_complete_S23_policies':n}

def main():
    rng=Random(202610282255)
    sample=[(F(1,20),O,Z,O),(O,F(1,20),O,Z),
            (F(3,4),F(3,4),F(5,12),F(1,3)),
            (F(3,4),F(3,4),F(1,3),F(5,12))]
    output=[case(*a,220,rng) for a in sample]
    for _ in range(60):
        a=F(rng.randrange(1,21),20)
        b=F(rng.randrange(1,21),20)
        ca=F(rng.randrange(0,21),20)
        cb=F(rng.randrange(0,21),20)
        case(a,b,ca,cb,7,rng)
    assert output[0]['AU_lower']=='53/9920'
    assert output[1]['BU_lower']=='33/6020'
    print(json.dumps({'status':'PASS_EXACT_N4_BINARY_CAPACITY_TV_MODULUS',
        'witnesses':output,'additional_parameter_cases':60,
        'total_random_complete_S23_policies':4*220+60*7,
        'exact_arithmetic':'Python Fraction',
        'real_domain_proof':'PROOF.md, not inferred from sampling',
        'native_X6_bridge':'NOT_ESTABLISHED',
        'admission':'AUTHOR_UNREVIEWED_NOT_ADMITTED'},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
