#!/usr/bin/env python3
"""PREFIX-627: online finite-lag provenance recovery using the native X6 BRC actions.
Scientific source: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
The 96-port transition and tagged path weights are the original 576-action rule.
"""
from collections import deque
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple(-k if c>0 else k for k in STARS[a] if k!=abs(c))
P=tuple((a,p,s*k) for a in range(4) for k in STARS[a]
        for s in (-1,1) for p in near(a,s*k))
IX={p:i for i,p in enumerate(P)}
def neighbors(i):
    a,p,c=P[i];b=next(j for j in range(4) if j!=a and abs(c) in STARS[j])
    return tuple(IX[x] for x in ([(a,c,k) for k in near(a,c) if k!=p]
                                  + [(b,c,k) for k in near(b,c)]))
N=tuple(neighbors(i) for i in range(48)); G=IX[(0,1,-3)]
AXIS=tuple(abs(c)-1 for a,p,c in P)
WEIGHTS=(1,1,1,1,0,0)
ACTIONS=[]
for i in range(48):
    for j in N[i]:
        for u,v in product((0,1),repeat=2):
            gated=(j==G and u==v==1)
            weight=F(0) if gated else F(WEIGHTS[AXIS[i]])
            ACTIONS.append((2*i+u,2*j+v,weight,gated))
assert len(P)==48 and len(ACTIONS)==576 and G==4
ARCS={(src,dst):(weight,gated) for dst,src,weight,gated in ACTIONS}
assert len(ARCS)==576

def embed(lam):
    r=[F(0)]*96
    for i in (4,11,14,32):
        r[2*i]=lam
        if i==G:r[2*i+1]=lam
    return r

def step(r,g):
    out=[F(0)]*96
    for dst,src,w,gated in ACTIONS:
        out[dst]+=(g if gated else w)*r[src]
    return out

def lagrange_last(r,n):
    assert n>=2
    v=[r[2*i] if i==G else r[2*i]+r[2*i+1] for i in range(48)]
    t=n-2
    pure=(2,28,38,16)
    lam=v[pure[(t+2)%4]]/F(4*2**t)
    ell=v[3]+v[14]+v[15]-2*v[2]
    delta=r[29]-r[28]
    assert lam>0 and ell>0 and ell-3*delta>0
    return lam,(ell+9*delta)/(ell-3*delta)

PRE={0:(9,),1:(22,9),2:(64,52,9),3:(28,80,52,9)}
CYCLE1=(9,28,80,52,9)
CYCLE2=(29,80,52,8,29)
def tagged_path(n,k):
    q=k-1;rem=q%4
    p=list(PRE[rem])
    for _ in range((q-rem)//4):p.extend(CYCLE1[1:])
    p.append(29)
    for j in range(n-k):p.append(CYCLE2[(j+1)%4])
    assert len(p)==n+1
    return p

def tagged_mass(path,gates,lam):
    z=lam
    for a,b,g in zip(path,path[1:],gates):
        w,gated=ARCS[(a,b)]
        z*=g if gated else w
    return z

# Maintains the complete native endpoint plus at most L-1 previous-gate
# registers. The immediately previous gate is decoded from the endpoint
# before it is overwritten. First stored index is k=5 as in PREFIX-626.
def online(gates,lam,L):
    n=len(gates)
    assert L>=1 and n>=L+4
    r=embed(lam); buf=deque(maxlen=max(1,L-1)); max_regs=0
    for j,g in enumerate(gates,1):
        if j>=6 and L>1:
            _,previous=lagrange_last(r,j-1)
            assert previous==gates[j-2]
            buf.append(previous)
            max_regs=max(max_regs,len(buf))
        r=step(r,g)
    observed_lam,last=lagrange_last(r,n)
    assert observed_lam==lam and last==gates[-1]
    tail=list(buf)+[last]
    assert tail==list(gates[n-L:])
    labels=list(range(n-L+1,n+1))
    fast=[observed_lam*z for z in tail]
    full=[tagged_mass(tagged_path(n,k),gates,lam) for k in labels]
    assert fast==full
    return r,fast,max_regs

# An explicit positive collision: keep each mod-4 (g+3) product and g_n
# fixed while changing a late gate and compensating the same-residue gate
# among positions 1..4. Thus the native 96-port endpoint is unchanged.
def collide(gates,L):
    n=len(gates)
    assert L>=2 and n>=L+4
    changed=n-1
    rr=changed%4
    earliest=rr if rr else 4
    clone=list(gates)
    old=clone[changed-1]
    new=old+F(1,3)  # small enough for all-positive base gates >=1
    initial=clone[earliest-1]
    clone[earliest-1]=(initial+3)*(old+3)/(new+3)-3
    assert clone[earliest-1]>0
    clone[changed-1]=new
    return tuple(clone),changed,earliest

trials=[]; collision_cases=0; coordinate_equalities=0
for n in (6,7,8,9,12,16,24,32,48):
    for L in (1,2,3,4,5,8,16,32):
        if L>n-4:continue
        for seed in (0,1,2):
            lam=F(2*seed+3,seed+2)
            gates=tuple(F(2+(7*k+seed)%7,1+(k+seed)%3) for k in range(1,n+1))
            # For the strict positive collision, use a separate all-one base.
            r,fast,regs=online(gates,lam,L)
            assert regs<=L-1
            coordinate_equalities+=L
            trials.append({'n':n,'lag':L,'seed':seed,'registers':regs,
                           'native_port_support':sum(v!=0 for v in r),
                           'all_suffix_path_mass_verified':True})
        if L>=2:
            base=(F(1),)*n
            other,j,i=collide(base,L)
            r1,_f,_m=online(base,F(3,2),L)
            r2,_f2,_m2=online(other,F(3,2),L)
            assert r1==r2
            assert tagged_mass(tagged_path(n,j),base,F(3,2)) != tagged_mass(tagged_path(n,j),other,F(3,2))
            collision_cases+=1

res={'schema':'PREFIX627_NATIVE_X6_ONLINE_FINITE_LAG_PROVENANCE_V1',
     'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
     'domain':'n>=L+4; L>=1 integer; lambda>0 and all gates>=0',
     'claim':'Native endpoint plus L-1 continuous scalar registers suffices and is sharp for W(n,k), k=n-L+1..n; fixed-lag online rolling exact implementation',
     'operator':'original 48 phase, 96 port, 576 typed labelled positive X6-BRC actions',
     'backend':'Python stdlib Fraction, exact rational validation',
     'trials':len(trials),'coordinate_equalities':coordinate_equalities,
     'explicit_same_endpoint_different_path_cases':collision_cases,
     'tested_horizons':sorted(set(x['n'] for x in trials)),
     'tested_lags':sorted(set(x['lag'] for x in trials)),
     'explanation':'Native endpoint admits lambda, final gate, and four modulo-4 shifted gate products. Store just preceding L-1 gates; lower bound by compensated first-four gates and invariance of domain.',
     'review':'AUTHOR_SIDE_UNREVIEWED','status':'ALL_ASSERTIONS_PASS',
     'validation_cases':trials}
Path(__file__).with_name('PREFIX627_native_streaming_lag_results.json').write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({k:res[k] for k in ('status','trials','coordinate_equalities','explicit_same_endpoint_different_path_cases','tested_horizons','tested_lags')},ensure_ascii=False))
