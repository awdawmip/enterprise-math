#!/usr/bin/env python3
"""Author exact affine-gap scan along the Stage161 R-retaining ray.
External finite iid N14; next result is DUAL-ONLY, not a primal claim.
"""
from fractions import Fraction as F
from functools import lru_cache
import json
from pathlib import Path
P=(F(1,8),F(1,24),F(5,6)); N=14
K=F(168193485,554801);L=F(162528200,554801)
J=(10,2,0);R=(10,0,1)
ACTS='PQC'
def lr(x):return F(2)**(x[1]+x[2])/F(3)**x[1]
def nexts(x,a):return (x[0]+1,x[1]+(a==0),x[2]+(a==1))
def add(x,y):return tuple(x[i]+y[i] for i in range(3))
def scale(c,x):return tuple(c*z for z in x)
@lru_cache(None)
def aff(s):
    options=[(F(0),lr(s),F(0)),(F(0),F(0),F(1))]
    if s[0]<N:
        opts=[aff(nexts(s,x)) for x in range(3)]
        cont=(F(1),F(0),F(0))
        for x in range(3):cont=add(cont,scale(P[x],opts[x]))
        options.append(cont)
    def ev(vec):return vec[0]+vec[1]*K+vec[2]*L
    m=min(map(ev,options)); inds=[i for i,z in enumerate(options) if ev(z)==m]
    if s==J:idx=0
    elif s==R:idx=2
    else:
        assert len(inds)==1, (s,inds)
        idx=inds[0]
    assert idx in inds
    return options[idx]

def options_for(s):
    seq=[(F(0),lr(s),F(0)),(F(0),F(0),F(1))]
    if s[0]<N:
        seq.append(add((F(1),F(0),F(0)),sum_vec([scale(P[k],aff(nexts(s,k))) for k in range(3)])))
    return seq

def sum_vec(vecs):
    out=(F(0),F(0),F(0))
    for v in vecs:out=add(out,v)
    return out

def ev(x,k=K,l=L):return x[0]+x[1]*k+x[2]*l
# Keep R's Q/continue tie while J saturates at P.
rc=options_for(R)[2]
dK=-F(1)
dL=(rc[1]/(F(1)-rc[2]))*dK
assert dL<0
assert (rc[1])*dK+(rc[2]-1)*dL==0
jc=options_for(J)[2]
jp=options_for(J)[0]
dJ=(jc[1]-jp[1])*dK+(jc[2]-jp[2])*dL
assert dJ>0,('J must become strict P',dJ)

cand=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   st=n,a,b;v=aff(st)
   for i,o in enumerate(options_for(st)):
    delta=ev(o)-ev(v)
    der=(o[1]-v[1])*dK+(o[2]-v[2])*dL
    assert delta>=0
    if delta>0 and der<0:
        cand.append((-delta/der,st,ACTS[i],delta,der))
assert cand
first=min(c[0] for c in cand)
closures=[x for x in cand if x[0]==first]
K2=K+first*dK;L2=L+first*dL
@lru_cache(None)
def ev2(st):
    opts=[K2*lr(st),L2]
    if st[0]<N:opts.append(1+sum(P[k]*ev2(nexts(st,k))[0] for k in range(3)))
    return min(opts),tuple(opts)
ties={};strictg=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   st=n,a,b;v,opt=ev2(st)
   selected=tuple(ACTS[i] for i,y in enumerate(opt) if y==v)
   if len(selected)>1:ties[str(st)]=selected
   strictg.extend(y-v for y in opt if y>v)
assert len(strictg)>0 and all(x>0 for x in strictg)
fmt=lambda v:str(v.numerator)+('/'+str(v.denominator) if v.denominator!=1 else '')
print('dual-ray dK',fmt(dK),'dL',fmt(dL),'R=Q/C remains tied; J=P strict after t0')
print('t162',fmt(first),'K162',fmt(K2),'L162',fmt(L2))
print('closures',[(s,label,fmt(g),fmt(d)) for _,s,label,g,d in closures])
print('ties',ties,'nonminimal positive gaps',len(strictg),'minimum',fmt(min(strictg)))
print('enumerated gap closures',len(cand))
data={'status':'AUTHOR_DUAL_ONLY','N':N,'base_K':fmt(K),'base_L':fmt(L),'direction':{'dK':fmt(dK),'dL':fmt(dL)},'t162':fmt(first),'K162':fmt(K2),'L162':fmt(L2),'closures':[{'state':list(s),'action':lab,'gap0':fmt(g),'gap_derivative':fmt(d)} for _,s,lab,g,d in closures],'ties':ties,'positive_gaps':len(strictg),'min_gap':fmt(min(strictg)),'candidate_gap_count':len(cand)}
with open(Path(__file__).with_name('candidate162.json'),'w') as f:json.dump(data,f,indent=2)
