#!/usr/bin/env python3
"""Independent SciPy/HiGHS 0-1 MILP check for EC49FAV early-edge optima."""
import json
from itertools import product
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix

OP={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
    'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
START=((0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(3,0),(4,0))
def steps(w):return tuple(s for a in w for s in OP[a])
def obs(w):
    out=[]
    for q,p in START:
        for s in steps(w):
            if p==1 and s==2:
                if q==0:q=1
                elif q==2:q=4
            elif p==2 and s==1:
                if q==0:q=2
                elif q==1:q=3
            p=s
        out.append(q)
    return tuple(out)
S={obs(w):1<<i for i,w in enumerate(('de','ed','ce','ec','feg','gef'))}
assert len(S)==6
def net(w):
    x=[0]*6
    for s in steps(w):x[abs(s)-1]+=1 if s>0 else -1
    return tuple(x)
def key(w):
    x=[0]*6
    for s in steps(w):
        if s>0:x[s-1]+=1
    return tuple(x)
def pref(ws):
    p=set()
    for w in ws:
        t=()
        for s in steps(w):t+=(s,);p.add(t)
    return p

W=[(h,''.join(t)) for h in (2,3) for t in product('acdefg',repeat=h)
   if net(''.join(t))==(2,0,0,0,0,0) and obs(''.join(t)) in S]
assert len(W)==44
P=sorted(pref(w for h,w in W),key=lambda x:(len(x),x))
K=sorted({key(w) for h,w in W})
assert len(K)==8
NW,NP,NK=len(W),len(P),len(K)
PI={p:i+NW for i,p in enumerate(P)}
KI={k:i+NW+NP for i,k in enumerate(K)}
N=NW+NP+NK
C=[]
def add(row,low,high):C.append((row,low,high))
# A selected word requires all its ordered native primitive prefix edges.
for i,(h,w) in enumerate(W):
    t=()
    for s in steps(w):
        t+=(s,)
        add({i:1,PI[t]:-1},float('-inf'),0)
    add({i:1,KI[key(w)]:-1},float('-inf'),0)
# Four horizon-specific rank clauses, represented as exact covering constraints.
for h in (2,3):
    for clause in (2|16,4|16,1|32,8|32):
        add({i:1 for i,(hh,w) in enumerate(W) if hh==h and S[obs(w)]&clause},1,float('inf'))
objective=[0.0]*NW+[1.0]*NP+[0.0]*NK
reports=[]
for budget in (1,2,3,4,5):
    constraints=C+[({KI[k]:1 for k in K},float('-inf'),budget)]
    A=lil_matrix((len(constraints),N));lb=[];ub=[]
    for j,(row,lo,hi) in enumerate(constraints):
        for i,value in row.items():A[j,i]=value
        lb.append(lo);ub.append(hi)
    r=milp(objective,integrality=[1]*N,
           bounds=Bounds([0]*N,[1]*N),
           constraints=LinearConstraint(A.tocsr(),lb,ub),
           options={'time_limit':120})
    assert r.status==0 and r.mip_gap==0
    chosen={str(h):[w for i,(hh,w) in enumerate(W) if hh==h and r.x[i]>.5] for h in (2,3)}
    assert len(pref(chosen['2']+chosen['3']))==int(r.fun)
    reports.append({'max_keys':budget,'minimum_edges':int(r.fun),
                    'status':int(r.status),'gap':float(r.mip_gap),
                    'dual_bound':int(r.mip_dual_bound),'selected':chosen})
assert [d['minimum_edges'] for d in reports]==[42,31,16,16,16]
print(json.dumps({'status':'PASS_INDEPENDENT_MILP','legal_words':len(W),
                  'native_candidate_prefixes':len(P),'key_classes':len(K),
                  'results':reports},indent=2,sort_keys=True))
