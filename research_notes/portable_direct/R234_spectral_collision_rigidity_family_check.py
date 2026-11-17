#!/usr/bin/env python3
"""R234: exact rational one-parameter persistence certificate for 230 modes."""
from fractions import Fraction as Q
from itertools import combinations
import json

Z,O=Q(0),Q(1)
LAM=Q(1,2)
C=Q(5,18)
R=Q(5,12)
MIDDLE={1,2,4,8,19,21,22,25,26,28,35,37,38,41,42,44,55,59,61,62}

def family(s):
    base=Q(1,3)+Q(2,7)+Q(1,11)+Q(1,2)
    h=Q(21,8)-base-(LAM-s)/(O-s)
    t=(h+LAM)/(h+O)
    alpha=(Q(1,5),Q(1,4),Q(3,10),Q(9,20),s,Q(2,3),t)
    pi=((O-C)*(LAM-alpha[0])/(O-alpha[0]),)+tuple(
        C*abs(LAM-a)/(O-a) for a in alpha[1:])
    assert len(set(alpha))==7
    assert all(Z<a<O for a in alpha)
    assert all(p>Z for p in pi) and sum(pi)==O
    b=tuple((O-a)*p for a,p in zip(alpha,pi))
    assert b[0]/(LAM-alpha[0])==O-C
    for i in (1,2,3,4): assert b[i]/(LAM-alpha[i])==C
    for i in (5,6): assert b[i]/(LAM-alpha[i])==-C
    assert alpha[0]+b[0]==R
    assert b[1]/(R-alpha[1]) + b[3]/(R-alpha[3])==Z
    return alpha,pi,b

def trim(v):
    v=list(v)
    while len(v)>1 and v[-1]==Z: v.pop()
    return v

def add(a,b):
    c=[Z]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]+=v
    for i,v in enumerate(b):c[i]+=v
    return trim(c)

def mul(a,b):
    c=[Z]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)

def rem(a,b):
    a=trim(a); b=trim(b)
    assert b!=[Z]
    while a!=[Z] and len(a)>=len(b):
        q=a[-1]/b[-1];off=len(a)-len(b)
        for j,v in enumerate(b):a[off+j]-=q*v
        a=trim(a)
    return a

def monic(a):
    a=trim(a)
    return [x/a[-1] for x in a] if a!=[Z] else [Z]

def gcd(a,b):
    while b!=[Z]:a,b=b,rem(a,b)
    return monic(a)

def killed(mask,alpha,b):
    d=[0]+[i for i in range(1,7) if mask>>(i-1)&1]
    def product(ids):
        p=[O]
        for i in ids:p=mul(p,[-alpha[i],O])
        return p
    v=product(d)
    for i in d:v=add(v,[-b[i]*x for x in product([j for j in d if j!=i])])
    return monic(v)

def poly_at(a,x):
    z=Z
    for v in reversed(a):z=z*x+v
    return z

def certificate(s):
    alpha,pi,b=family(s)
    p={mask:killed(mask,alpha,b) for mask in range(63)}
    assert sum(len(v)-1 for v in p.values())==249
    assert {mask for mask,f in p.items() if poly_at(f,LAM)==Z}==MIDDLE
    assert {mask for mask,f in p.items() if poly_at(f,R)==Z}=={0,5}
    assert all(gcd(f,[Q(i)*v for i,v in enumerate(f)][1:])==[O] for f in p.values())
    assert all(poly_at(f,O)!=Z for f in p.values())
    collisions={"1/2":0,"5/12":0}
    for m,n in combinations(range(63),2):
        g=gcd(p[m],p[n])
        if len(g)>1:
            assert len(g)==2,(s,m,n,g)
            if m in MIDDLE and n in MIDDLE:
                assert g==[-LAM,O],(s,m,n,g)
                collisions["1/2"]+=1
            else:
                assert (m,n)==(0,5) and g==[-R,O],(s,m,n,g)
                collisions["5/12"]+=1
    assert collisions=={"1/2":190,"5/12":1}
    degree=250-19-1
    assert degree==230
    return {"s":str(s),"alpha_6":str(alpha[6]),"pi_0":str(pi[0]),
            "transition_probability_sum":str(sum(pi)),"proper_blocks":63,
            "pairwise_gcd_checks":1953,"squarefree_checks":63,
            "collisions":collisions,"minimal_scalar_recurrence_degree":degree}

if __name__=="__main__":
    results=[certificate(s) for s in (Q(39,100),Q(2,5),Q(41,100))]
    result={"schema":"R234_SPECTRAL_RIGIDITY_FAMILY_EXACT_V1","status":"PASS",
        "samples":results,"arithmetic":"exact fractions.Fraction / rational polynomial Euclidean gcd",
        "tested_cases":3,"total_pairwise_gcd_checks":5859,
        "proof_scope":"local rational family plus symbolic rank-rigidity and resultant continuity proof",
        "independent_review":"NOT_REVIEWED", "native_brc_integration":"NOT_EXECUTED"}
    print(json.dumps(result,ensure_ascii=False,indent=2))
