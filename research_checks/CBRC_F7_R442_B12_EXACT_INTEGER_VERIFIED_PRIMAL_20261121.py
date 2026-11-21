#!/usr/bin/env python3
"""F7 B=12: numerical primal search, then exhaustive integer-only certificate check.

The numerical solver proposes q; only the exact 25^4 integer scan establishes
the stated finite-cube upper bound for that candidate. A different basis is
allowed only if its own exact scan passes.
"""
from itertools import product
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

B, DEN = 12, 100_000_000
A = ((2,-2,-1,2),(1,-1,-1,2),(-1,2,2,-2),(-1,2,1,-1))

def scalar(x,y):
    a=abs(x)
    if a==0 and y==0: return None,0.
    if y==0: return None,1.
    if (a,y) in ((2,1),(1,-1)): return None,.5
    return (a,y),0.

def form(a,b,w):
    x,x0=scalar(w+a-b,w-b)
    y,y0=scalar(w+b-a,w-a)
    terms={}
    if x is not None: terms[x]=terms.get(x,0)+1
    if y is not None: terms[y]=terms.get(y,0)-1
    return terms,x0-y0

cons=[]; keys=set(); pairs=[]
for a in range(-2*B,2*B+1):
    Ia=range(max(-B,-B-a),min(B,B-a)+1)
    for b in range(a+1,2*B+1):
        Ib=range(max(-B,-B-b),min(B,B-b)+1)
        pid=len(pairs);pairs.append((a,b))
        for m in Ia:
            t,k=form(a,b,m+b);keys.update(t)
            cons.extend(((pid,0,-1,t,k,.5),(pid,1,1,t,k,0.)))
        for ell in Ib:
            t,k=form(a,b,ell+a);keys.update(t)
            cons.extend(((pid,0,1,t,k,0.),(pid,1,-1,t,k,.5)))
kl=sorted(keys); ix={k:i for i,k in enumerate(kl)}
n=len(kl); r=[]; c=[]; v=[]; rhs=[]
for i,(pid,aux,sgn,t,k,lim) in enumerate(cons):
    r.append(i);c.append(n+2*pid+aux);v.append(-sgn)
    for kk,tt in t.items():
        if tt: r.append(i);c.append(ix[kk]);v.append(sgn*tt)
    rhs.append(lim-sgn*k)
M=coo_matrix((np.asarray(v,dtype=np.int8),
             (np.asarray(r,dtype=np.int32),np.asarray(c,dtype=np.int32))),
             shape=(len(rhs),n+2*len(pairs))).tocsr()
assert len(rhs)==8*B*(2*B+1)**2==60000
assert n==3046
res=linprog(np.zeros(M.shape[1]),A_ub=M,b_ub=np.asarray(rhs),
            bounds=[(.5,1.)]*n+[(-2.,2.)]*(2*len(pairs)),
            method="highs",options={"presolve":True,"time_limit":120})
assert res.status==0,(res.status,res.message)
T={key:int(round(float(res.x[i])*DEN)) for i,key in enumerate(kl)}
assert len(T)==3046
assert all(DEN//2<=v<=DEN for v in T.values())

def q(x,y):
    a=abs(x)
    if a==0 and y==0: return 0
    if y==0: return DEN
    if (a,y) in ((2,1),(1,-1)): return DEN//2
    return T.get((a,y),DEN//2)

worst=0; witness=None; equal=0
for z in product(range(-B,B+1),repeat=4):
    az=[sum(row[i]*z[i] for i in range(4)) for row in A]
    d=q(az[0],az[1])+q(az[2],az[3])-q(z[0],z[1])-q(z[2],z[3])
    if abs(d)>worst:
        worst=abs(d);witness=z;equal=0
    if abs(d)==worst:equal+=1
assert worst<=50_000_001,(worst,witness)
print(f"PASS: B={B}, free_classes={n}, inputs={(2*B+1)**4}, "
      f"max_abs_D={worst}/{DEN}, equality_count={equal}, witness={witness}")
print(f"Proved finite bound: 1/2 <= E_{B} <= {worst}/{DEN}")
