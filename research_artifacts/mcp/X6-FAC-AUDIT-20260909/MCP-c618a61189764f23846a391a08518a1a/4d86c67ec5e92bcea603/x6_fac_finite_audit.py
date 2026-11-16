#!/usr/bin/env python3
"""Deterministic exploratory X6-FAC cyclic observer audit (small-prime windows)."""
import json, math, hashlib
from collections import Counter
from sympy import primerange, cyclotomic_poly, symbols, divisors, Poly

x=symbols('x')

class Counts:
    def __init__(self): self.mul=0; self.add=0; self.gcd=0

def cyclic_mul(a,b,n,ct):
    R=len(a); z=[0]*R
    for i,ai in enumerate(a):
        if not ai: continue
        for j,bj in enumerate(b):
            if not bj: continue
            k=(i+j)%R
            z[k]=(z[k]+ai*bj)%n
            ct.mul+=1; ct.add+=1
    return z

def cyclic_pow(seed, n, R, ct):
    out=[1]+[0]*(R-1); b=seed[:]; e=n
    while e:
        if e&1: out=cyclic_mul(out,b,n,ct)
        e//=2
        if e: b=cyclic_mul(b,b,n,ct)
    return out

def quotient(a,r,n,ct=None):
    z=[0]*r
    for k,c in enumerate(a):
        z[k%r]=(z[k%r]+c)%n
        if ct is not None: ct.add+=1
    return z

def poly_mul_mod(a,b,monic,n):
    d=len(monic)-1
    v=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,w in enumerate(b): v[i+j]=(v[i+j]+u*w)%n
    for k in range(len(v)-1,d-1,-1):
        u=v[k]
        if not u: continue
        for j in range(d):
            v[k-d+j]=(v[k-d+j]-u*monic[j])%n
    return (v[:d]+[0]*d)[:d]

def poly_mod(a,monic,n,ct=None):
    d=len(monic)-1
    v=a[:]
    for k in range(len(v)-1,d-1,-1):
        u=v[k]%n
        if u:
            for j in range(d):
                v[k-d+j]=(v[k-d+j]-u*monic[j])%n
                if ct is not None: ct.mul+=1;ct.add+=1
    return v[:d]

def poly_pow(seed,n,monic):
    d=len(monic)-1;out=[1]+[0]*(d-1);b=poly_mod(seed,monic,n);e=n
    while e:
        if e&1: out=poly_mul_mod(out,b,monic,n)
        e//=2
        if e: b=poly_mul_mod(b,b,monic,n)
    return out

def witness(coords,n,ct):
    ret=[]
    for z in coords:
        ct.gcd+=1
        g=math.gcd(int(z),n)
        if 1<g<n:ret.append(g)
    return sorted(set(ret))

def evaluate(p,q,R,seed):
    N=p*q
    ct=Counts()
    seed_vec=[0]*R
    for d in seed: seed_vec[d%R]=(seed_vec[d%R]+1)%N
    fine=cyclic_pow(seed_vec,N,R,ct)
    fine_g=witness(fine,N,ct)
    merged=set(fine_g)
    divs=divisors(R)
    for r in divs:
        obs=quotient(fine,r,N,ct)
        assert obs==cyclic_pow([sum(1 for d in seed if d%r==i)%N for i in range(r)],N,r,Counts())
        merged.update(witness(obs,N,ct))
    div_g=sorted(merged)
    cyclo=set(merged)
    phi_sum=0
    for d in divs:
        poly=Poly(cyclotomic_poly(d,x),x)
        deg=int(poly.degree()); phi_sum+=deg
        phi=[int(poly.nth(i)) for i in range(deg+1)]
        obs=poly_mod(fine,phi,N,ct)
        assert obs==poly_pow([sum(1 for v in seed if v==i)%N for i in range(max(seed)+1)],N,phi)
        cyclo.update(witness(obs,N,ct))
    assert phi_sum==R
    return {"N":N,"p":p,"q":q,"R":R,"seed_degrees":seed,"fine":bool(fine_g),"divisor":bool(div_g),"cyclotomic_union":bool(cyclo),"factors_fine":fine_g,"factors_divisor":div_g,"factors_cyclotomic_union":sorted(cyclo),"cost":{"modular_multiplications":ct.mul,"modular_additions":ct.add,"gcd_calls":ct.gcd},"num_divisors":len(divs)}

if __name__=='__main__':
    # Fixed test plan: 16 ordered semiprimes from two small prime sets, seeds x+1 and x^2+x+1, widths 12,18,24.
    pset=[11,13,17,19]
    gaps=[6,12,18,24]
    trials=[]
    for p in pset:
        for g in gaps:
            q=next(primerange(p+g,p+g+100))
            for R in (12,18,24):
                for seed in ((0,1),(0,1,2)):
                    trials.append(evaluate(p,q,R,seed))
    summary={}
    for R in (12,18,24):
        for seed in ((0,1),(0,1,2)):
            a=[t for t in trials if t['R']==R and tuple(t['seed_degrees'])==seed]
            key=f'R={R},seed={seed}'
            summary[key]={"trials":len(a),"fine":sum(t['fine'] for t in a),"divisor":sum(t['divisor'] for t in a),"cyclotomic_union":sum(t['cyclotomic_union'] for t in a),"total_multiplications":sum(t['cost']['modular_multiplications'] for t in a),"total_additions":sum(t['cost']['modular_additions'] for t in a),"total_gcd_calls":sum(t['cost']['gcd_calls'] for t in a)}
    payload={"scope":"SMALL_FINITE_EXPLORATION_NOT_SCALE_LAW_PROOF","algorithm":"cyclic repeated-squaring with mod N; quotient compare independent direct re-exponentiation; cyclotomic compare independent direct mod Phi_d exponentiation","sampling":"p in [11,13,17,19], gap g in [6,12,18,24], q = smallest prime >=p+g, widths R=[12,18,24], two fixed seeds","trial_count":len(trials),"summary":summary,"trials":trials}
    raw=json.dumps(payload,sort_keys=True,ensure_ascii=False,indent=2)
    with open('/mnt/data/x6_fac_finite_audit_results.json','w') as f:f.write(raw+'\n')
    print(json.dumps(summary,indent=2));print('trials',len(trials),'sha256',hashlib.sha256((raw+'\n').encode()).hexdigest())
