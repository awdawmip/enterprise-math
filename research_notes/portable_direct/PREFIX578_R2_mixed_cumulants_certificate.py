#!/usr/bin/env python3
"""PREFIX-578-R2 exact X6-BRC axis/gate third cumulants.

Rebuilds PREFIX565 native edges and PREFIX566 future-exact 37-state quotient.
Requires SymPy for rational matrix inversion. Observer weights are exact.
Scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from collections import Counter
from itertools import product
from math import factorial
import json
import sympy as sp

STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(star,c):
    return tuple((-1 if c>0 else 1)*k for k in STARS[star] if k!=abs(c))
PHASES=tuple((a,p,sgn*k) for a in range(4) for k in STARS[a]
             for sgn in (-1,1) for p in near(a,sgn*k))
PHASE_INDEX={x:i for i,x in enumerate(PHASES)}
def successors(phase):
    a,p,c=PHASES[phase]
    b=next(b for b in range(4) if b!=a and abs(c) in STARS[b])
    return tuple(PHASE_INDEX[t] for t in
      [(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)])
NEXT=tuple(successors(i) for i in range(48))
TARGET=PHASE_INDEX[(0,1,-3)]
ACTIONS=tuple(product(range(3),(0,1)))
ROOT=(0,)*6

def sg(phase,k):
    c=PHASES[phase][2]
    return (1 if c>0 else -1) if abs(c)==k else 0

def edge(port,action,root=ROOT):
    phase,bit=divmod(port,2)
    slot,newbit=action
    nxt=NEXT[phase][slot]
    weights=[]
    for k in range(1,7):
        left=sg(phase,k); right=sg(nxt,k); z=root[k-1]
        v=abs(left)+abs(right)-abs(right-z)+abs(left-z)
        assert v in (0,2)
        weights.append(v//2)
    gate=int(bit==newbit==1 and nxt==TARGET)
    return 2*nxt+newbit,tuple(weights)+(gate,)

def weighted_quotient(rows):
    ids=[0]*len(rows)
    growth=[1]
    for _ in range(len(rows)):
        keys=[]
        for row in rows:
            out=Counter()
            for (j,a,b,g),m in row.items():
                out[(ids[j],a,b,g)]+=m
            keys.append(tuple(sorted(out.items())))
        lookup={}
        nxt=[lookup.setdefault(k,len(lookup)) for k in keys]
        if nxt==ids: break
        ids=nxt
        growth.append(len(lookup))
    else:
        raise AssertionError('nonconvergent partition')
    quotient={}
    for i,row in enumerate(rows):
        q=Counter()
        for (j,a,b,g),m in row.items():
            q[ids[j],a,b,g]+=m
        if ids[i] in quotient:
            assert quotient[ids[i]]==q
        else:
            quotient[ids[i]]=q
    return tuple(ids),tuple(quotient[i] for i in range(len(quotient))),growth

def main():
    rows=[Counter((j,w[4],w[5],w[6]) for action in ACTIONS
            for j,w in [edge(i,action)]) for i in range(96)]
    gate_edges=sorted((i,j) for i,row in enumerate(rows)
         for (j,a,b,g),m in row.items() if g for _ in range(m))
    assert gate_edges==[(7,9),(29,9),(31,9)]
    ids,Q,growth=weighted_quotient(rows)
    assert len(Q)==37 and growth==[1,4,13,21,33,37]
    sizes=[Counter(ids)[i] for i in range(37)]
    assert sizes==[8,4,2,1,1,2,2,8,4,2,4,4,2,4,1,1,1,1,2,2,4,
        2,4,4,2,2,2,2,2,2,2,2,2,2,2,2,2]
    n=len(Q)
    pi=sp.Matrix(1,n,lambda i,j:sp.Rational(sizes[j],96))
    ones=sp.ones(n,1)
    P=sp.zeros(n,n)
    for i,row in enumerate(Q):
        for (j,a,b,g),m in row.items():
            P[i,j]+=sp.Rational(m,6)
    assert P*ones==ones and pi*P==pi
    Z=sp.eye(n)-P+ones*pi
    Zinv=Z.inv()
    assert Z*Zinv==sp.eye(n)
    def directional(a,b,c):
        M=[None]+[sp.zeros(n,n) for k in range(3)]
        for i,row in enumerate(Q):
            for (j,x,y,g),m in row.items():
                r=a*x+b*y+c*g
                for k in range(1,4):
                    M[k][i,j]+=sp.Rational(m*r**k,6*factorial(k))
        vec=[ones]
        ell=[sp.Integer(1)]
        for k in range(1,4):
            rhs=sp.zeros(n,1)
            for j in range(1,k+1):
                rhs+=M[j]*vec[k-j]
            l=(pi*rhs)[0]
            ell.append(l)
            for j in range(1,k):
                rhs-=ell[j]*vec[k-j]
            rhs-=l*ones
            v=Zinv*rhs
            assert (pi*v)[0]==0 and (sp.eye(n)-P)*v==rhs
            vec.append(v)
        l1,l2,l3=ell[1:]
        c3=6*l3-6*l1*l2+2*l1**3
        return c3,l1,2*l2-l1*l1
    ds={'K':(0,0,1),'S':(1,1,0),'D':(1,-1,0),
        'S+K':(1,1,1),'S-K':(1,1,-1),
        'D+K':(1,-1,1),'D-K':(1,-1,-1),
        'axis5':(1,0,0),'axis6':(0,1,0),
        'axis5+K':(1,0,1),'axis5-K':(1,0,-1)}
    out={name:directional(*v) for name,v in ds.items()}
    def c3(name): return out[name][0]
    mixed={
        'S_K_K':(c3('S+K')+c3('S-K')-2*c3('S'))/6,
        'S_S_K':(c3('S+K')-c3('S-K')-2*c3('K'))/6,
        'D_D_K':(c3('D+K')-c3('D-K')-2*c3('K'))/6,
        'D_K_K':(c3('D+K')+c3('D-K')-2*c3('D'))/6,
        'axis5_K_K':(c3('axis5+K')+c3('axis5-K')-2*c3('axis5'))/6,
        'axis5_axis5_K':(c3('axis5+K')-c3('axis5-K')-2*c3('K'))/6}
    assert out['K'][0]==sp.Rational(206963,42467328)
    assert out['K'][1]==sp.Rational(1,192)
    assert out['K'][2]==sp.Rational(1127,221184)
    assert out['S'][1]==sp.Rational(1,3)
    assert out['S'][2]==sp.Rational(1,27)
    assert out['D'][1]==0 and out['D'][2]==sp.Rational(1,6)
    assert mixed['S_K_K']==sp.Rational(-6053,5308416)
    assert mixed['S_S_K']==sp.Rational(1,5184)
    assert mixed['D_D_K']==sp.Rational(5,6912)
    assert mixed['D_K_K']==0
    assert mixed['axis5_K_K']==sp.Rational(-6053,10616832)
    assert mixed['axis5_axis5_K']==sp.Rational(19,82944)
    result={
        'status':'ALL_ASSERTIONS_PASS',
        'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
        'model':'96 native four-STAR X6-BRC ports; future-exact 37-class q5,q6,gate observer',
        'quotient_growth':growth,'native_gates':gate_edges,
        'directional_third_cumulants':{
            k:{'kappa3':str(v[0]),'mean':str(v[1]),'variance':str(v[2])}
            for k,v in out.items()},
        'mixed':{k:str(v) for k,v in mixed.items()}}
    print(json.dumps(result,indent=2))
    return result

if __name__=='__main__':
    main()
