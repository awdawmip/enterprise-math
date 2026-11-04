#!/usr/bin/env python3
"""CM(-24) Hasse first-jet transversality and unramified p^2 lift.
Author-side exact finite arithmetic only. No native H0/B0 Frobenius experiment.
"""
from math import comb, isqrt
import json
Q_ASC = (1, -140, 294, -140, 1)

def primes(n):
    a = bytearray(b'\1') * (n + 1)
    a[0] = a[1] = 0
    for k in range(2, isqrt(n) + 1):
        if a[k]:
            a[k*k:n+1:k] = b'\0' * (((n-k*k)//k)+1)
    return (p for p in range(5,n+1) if a[p] and p%8==5)

def R(mod):
    def add(x,y): return tuple((a+b)%mod for a,b in zip(x,y))
    def neg(x): return tuple(-a%mod for a in x)
    def scale(x,c): return tuple(a*c%mod for a in x)
    def mul(x,y):
        v=[0]*7
        for i in range(4):
            for j in range(4): v[i+j]+=x[i]*y[j]
        for k in range(6,3,-1):
            h=v[k]%mod
            for i in range(4): v[k-4+i]-=h*Q_ASC[i]
        return tuple(v[i]%mod for i in range(4))
    def power(x,n):
        y=(1,0,0,0)
        while n:
            if n&1: y=mul(y,x)
            x=mul(x,x); n>>=1
        return y
    def poly(c,x):
        ans=(0,0,0,0)
        for ci in reversed(c): ans=add(mul(ans,x),(ci%mod,0,0,0))
        return ans
    return add,neg,scale,mul,power,poly

def deriv(v): return [k*v[k] for k in range(1,len(v))]
def product(a,b):
    v=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): v[i+j]+=x*y
    return v
def at(v,i): return v[i] if i<len(v) else 0
def zip_longest(a,b):
    for i in range(max(len(a),len(b))): yield at(a,i),at(b,i)

def verify(p,mod):
    m=(p-1)//2;cs=[comb(m,k)**2 for k in range(m+1)]
    A=[0,16,0,-16];B=[1,2,-7];T=[1,18,-23]
    C=[x+y for x,y in zip_longest(product(A,deriv(cs)),product(B,cs))]
    Cp=deriv(C);ACp=product(A,Cp);TC=product(T,C)
    source=product([0,64,-128,64],cs);QH=product(Q_ASC,cs)
    n=max(map(len,[ACp,TC,source,QH]))
    for i in range(n):
        assert (at(ACp,i)-at(TC,i)+at(source,i)+at(QH,i))%p==0,(p,i,'syzygy')
    add,neg,scale,mul,powr,poly=R(mod)
    t=(0,1,0,0)
    h=poly(cs,t);c=poly(C,t);cp=poly(Cp,t)
    a=poly(A,t);tt=poly(T,t);source=poly([0,64,-128,64],t)
    assert all(x%p==0 for x in add(add(mul(a,cp),neg(mul(tt,c))),mul(source,h))),(p,'Q-jet_mod_p')
    return {'h':h,'c':c,'cp':cp,'cs':cs,'C_coeff':C,'A_coeff':A,'B_coeff':B}

def lift(p):
    assert p%24==5
    mod=p*p;result=verify(p,mod)
    add,neg,scale,mul,powr,poly=R(mod)
    c=result['c'];cp=result['cp']
    assert all(ci%p==0 for ci in c),(p,'hypothesis C mod p')
    bar=tuple(x%p for x in cp)
    p_add,p_neg,p_scale,p_mul,p_powr,p_poly=R(p)
    inv=p_powr(bar,p*p-2)
    assert p_mul(bar,inv)==(1,0,0,0),(p,'unit derivative')
    c_over_p=tuple((x//p)%p for x in c)
    delta=p_neg(p_mul(c_over_p,inv))
    z=add((0,1,0,0),tuple(p*x for x in delta))
    assert poly(result['C_coeff'],z)==(0,0,0,0),(p,'direct Hensel substitution')
    assert z[1]%p==1 and all(z[i]%p==0 for i in (0,2,3))
    return {'prime':p,'C_over_p':c_over_p,'lift_delta':delta,'H_mod_p':tuple(x%p for x in result['h'])}

def run(limit=5000,lift_limit=500):
    stats={'prime_count':0,'strong_polynomial_syzygy':0,'quartic_jet':0,'split_held_C_vanish':0,'inert_held_H_vanish':0,'inert_held_C_nonzero':0,'p2_lift_direct':0}
    examples=[]
    for p in primes(limit):
        r=verify(p,p)
        stats['prime_count']+=1
        stats['strong_polynomial_syzygy']+=1
        stats['quartic_jet']+=1
        if p%24==5:
            assert r['c']==(0,0,0,0),(p,'split observational input')
            stats['split_held_C_vanish']+=1
            if p<=lift_limit:
                v=lift(p);stats['p2_lift_direct']+=1
                if p in (5,29,53,101,149,173,197): examples.append(v)
        else:
            assert p%24==13
            assert r['h']==(0,0,0,0),(p,'inert Hasse CM check')
            assert r['c']!=(0,0,0,0),(p,'inert C nonzero')
            stats['inert_held_H_vanish']+=1
            stats['inert_held_C_nonzero']+=1
    return {'success':True,'counts':stats,'samples':examples}

if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
