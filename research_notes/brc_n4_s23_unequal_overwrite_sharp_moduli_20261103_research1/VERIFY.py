#!/usr/bin/env python3
"""Independent exact Fraction verification, Enterprise Math S23 N4 frozen science."""
from fractions import Fraction as F
from itertools import product
import random, json

A = (0,0,0,1,1,1)
B = (2,2,3,2,2,4)
C = (5,6,7,8,9,10)
M = ((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
     (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
PAIRS = ((3,31),(27,7),(11,23),(19,15)) # (non-2, containing-2)
BETA = (F(0), F(1,5), F(1,2), F(3,4), F(9,10), F(1))

def br(p,q,r):
    return (p,(1-p)*q,(1-p)*(1-q)*r,(1-p)*(1-q)*(1-r))

def observe(z,mask,beta):
    raw = [br(beta if mask & (1<<A[i]) else z[A[i]],
              beta if mask & (1<<B[i]) else z[B[i]], z[C[i]]) for i in range(6)]
    return [tuple(sum(F(M[j][i],20)*raw[i][k] for i in range(6)) for k in range(4)) for j in range(6)]

def tv(p,q): return sum(abs(x-y) for x,y in zip(p,q))/2

def dist(z,w,n,e,bn,be):
    return max(tv(p,q) for m,b in ((0,F(0)),(n,bn),(e,be))
                  for p,q in zip(observe(z,m,b),observe(w,m,b)))

def sup(z,w): return max(abs(x-y) for x,y in zip(z,w))

def inv(o,n,e,bn,be):
    # o = (baseline, non2, exposing) arrays of 6x4, all exact
    a,b=1-bn,1-be
    if not a or not b: raise ValueError('singular endpoint')
    base,N,E=o
    z=[None]*11
    z[0]=base[0][0];z[1]=base[3][0]
    z[2]=N[0][1]/a
    for mid,source in ((3,2),(4,5)):
        use=N if not n & (1<<mid) else E
        beta=bn if use is N else be
        z[mid]=use[source][1]/(1-beta)
    z[5]=(11*E[0][2]-10*E[1][2])/b**2
    z[6]=(10*E[1][2]-9*E[0][2])/b**2
    z[8]=(9*E[3][2]-5*E[4][2])/(4*b**2)
    z[9]=(5*E[4][2]-E[3][2])/(4*b**2)
    for out,mid,source in ((7,3,2),(10,4,5)):
        use=N if n & (1<<mid) else E
        beta=bn if use is N else be
        z[out]=use[source][2]/(1-beta)**2
    return tuple(z)

def witness_mix():
    z=[F(1)]*5+[F(0)]*6;w=z.copy()
    z[5]=F(1);w[6]=F(19,21)
    return z,w

def witness_middle():
    z=[F(1)]*5+[F(0)]*6;w=z.copy();w[2]=F(0)
    return z,w

def witness_late(n):
    z=[F(1)]*5+[F(0)]*6;w=z.copy()
    assert (n&8 or n&16), n
    j=7 if n&8 else 10
    z[j]=F(1)
    return z,w

rng=random.Random(202611030901)
counts={'witness':0,'inverse':0,'global_inequality':0,'zero_endpoint':0}
samples=[]
for n,e in PAIRS:
    assert not(n&4) and (e&7)==7 and (n&3)==3
    for bn,be in product(BETA,repeat=2):
        a,b=1-bn,1-be
        coefficient=min(a if n==3 else a*a,b*b/21)
        witnesses=[('mix',witness_mix(),b*b/21),('middle',witness_middle(),a)]
        if n!=3:witnesses.append(('late',witness_late(n),a*a))
        for name,(z,w),expected in witnesses:
            d=dist(z,w,n,e,bn,be)
            assert d==expected, (n,e,bn,be,name,d,expected)
            assert sup(z,w)==1
            counts['witness']+=1
            if name=='mix' and coefficient==expected: samples.append((n,e,str(bn),str(be),str(coefficient)))
        if not a or not b:
            assert coefficient==0
            counts['zero_endpoint']+=1
        else:
            for _ in range(5):
                z=[F(rng.randint(0,12),12) for j in range(11)]
                w=[F(rng.randint(0,12),12) for j in range(11)]
                obs=(observe(z,0,F(0)),observe(z,n,bn),observe(z,e,be))
                assert inv(obs,n,e,bn,be)==tuple(z), ('inverse',n,e,bn,be,z)
                counts['inverse']+=1
                d=dist(z,w,n,e,bn,be)
                assert d>=coefficient*sup(z,w), ('bound',n,e,bn,be,d,coefficient,sup(z,w))
                counts['global_inequality']+=1
result={
  'status':'PASS_BRC_S23_UNEQUAL_OVERWRITE_EXACT_MODULI_20261103',
  'frozen_science':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
  'metric':'maximum labeled source total variation across baseline and two overwritten views',
  'coefficient':{'non2_mask_3':'min(a,b*b/21)','non2_masks_27_11_19':'min(a*a,b*b/21)','a':'1-beta_non2','b':'1-beta_exposing2'},
  'mask_order':PAIRS,'beta_values':[str(b) for b in BETA],
  'counts':counts,
  'proof':'symbolic inversion and witnesses establish global all-real theorem; finite exact tests check implementation'
}
print(json.dumps(result,indent=2))
