#!/usr/bin/env python3
"""F7 B=10: numerical discovery followed by an exact integer certificate check.

Requires numpy/scipy for discovery; proof check uses integer arithmetic only.
This checker is deterministic for the recorded HiGHS solution; a different
solver basis is accepted only if it independently passes the integer tests.
"""
from itertools import product
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

B, DEN = 10, 100000000
A = ((2,-2,-1,2),(1,-1,-1,2),(-1,2,2,-2),(-1,2,1,-1))

def scalar(x,y):
    a=abs(x)
    if a==0 and y==0:return None,0.0
    if y==0:return None,1.0
    if (a,y) in ((2,1),(1,-1)):return None,0.5
    return (a,y),0.0

def form(a,b,w):
    x,x0=scalar(w+a-b,w-b)
    y,y0=scalar(w+b-a,w-a)
    terms={}
    if x is not None:terms[x]=terms.get(x,0)+1
    if y is not None:terms[y]=terms.get(y,0)-1
    return terms,x0-y0

cons=[];keys=set();pairs=[]
for a in range(-2*B,2*B+1):
    Ia=range(max(-B,-B-a),min(B,B-a)+1)
    for b in range(a+1,2*B+1):
        Ib=range(max(-B,-B-b),min(B,B-b)+1)
        pid=len(pairs);pairs.append((a,b))
        for m in Ia:
            terms,k=form(a,b,m+b);keys.update(terms)
            cons.extend(((pid,0,-1,terms,k,0.5),(pid,1,+1,terms,k,0.0)))
        for ell in Ib:
            terms,k=form(a,b,ell+a);keys.update(terms)
            cons.extend(((pid,0,+1,terms,k,0.0),(pid,1,-1,terms,k,0.5)))
keylist=sorted(keys);index={k:i for i,k in enumerate(keylist)}
nq=len(keylist);r=[];c=[];v=[];rhs=[]
for i,(pid,aux,sign,terms,const,limit) in enumerate(cons):
    r.append(i);c.append(nq+2*pid+aux);v.append(-sign)
    for k,t in terms.items():
        if t:r.append(i);c.append(index[k]);v.append(sign*t)
    rhs.append(limit-sign*const)
M=coo_matrix((np.array(v,dtype=np.int8),(np.array(r,dtype=np.int32),np.array(c,dtype=np.int32))),shape=(len(rhs),nq+2*len(pairs))).tocsr()
assert len(rhs)==8*B*(2*B+1)**2==35280
res=linprog(np.zeros(M.shape[1]),A_ub=M,b_ub=np.asarray(rhs),bounds=[(.5,1.)]*nq+[(-2.,2.)]*(2*len(pairs)),method='highs',options={'presolve':True,'time_limit':115})
assert res.status==0, (res.status,res.message)
T={k:int(round(float(res.x[i])*DEN)) for i,k in enumerate(keylist)}
assert len(T)==2128 and all(DEN//2<=u<=DEN for u in T.values())

def q(x,y):
    a=abs(x)
    if a==0 and y==0:return 0
    if y==0:return DEN
    if (a,y) in ((2,1),(1,-1)):return DEN//2
    return T.get((a,y),DEN//2)

assert q(0,0)==0 and q(2,1)==q(-1,-1)==DEN//2
# Full integer verification over all 21^4 four-tuples, independent of
# the epigraph inequalities and of floating-point row tolerances.
worst=0;witness=None;equal=0
for z in product(range(-B,B+1),repeat=4):
    w=[sum(row[i]*z[i] for i in range(4)) for row in A]
    d=q(w[0],w[1])+q(w[2],w[3])-q(z[0],z[1])-q(z[2],z[3])
    if abs(d)>worst:worst=abs(d);witness=z
    if abs(d)==50000001:equal+=1
assert worst==50000001,(worst,witness)
assert equal==180,equal
print(f'PASS: B={B}, q_classes={nq}, inputs={(2*B+1)**4}, max_abs_D={worst}/{DEN}, equality_count={equal}, witness={witness}')
print(f'Exact E_{B} bounds: 1/2 <= E_{B} <= {worst}/{DEN}')
