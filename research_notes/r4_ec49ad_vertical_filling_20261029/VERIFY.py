"""EC49AD exact local terminal-policy filling; Python 3 stdlib Fraction.
Executed; finite checks support the algebraic all-real theorem in PROOF.md.
"""
from fractions import Fraction as F
from itertools import product
import json
Z=F(0); W=range(3); C=range(4); U=range(2); J=range(3)
X=[[F(1),Z,Z,Z],[Z,F(1),Z,Z],[F(9,16),Z,F(1,16),Z]]
K=[(F(0),F(0)),(F(17,288),F(17,96)),(F(3047,38400),F(3641,12800)),(F(19,192),F(25,64)),(F(1939,19200),F(3067,6400)),(F(59,576),F(109,192))]
D=K[-1][0]
def t(w,u): return F(1,2)+F(2*u-1,200)*(1-w)
def raw(w,u,j,s): return t(w,u)*(F(1,6) if w==j else F(1,12)) if s=="P" else t(w,u)*F(1,9)
def atom(c,u,j):
 p=sum((X[w][c]*raw(w,u,j,"P") for w in W),Z)
 q=sum((X[w][c]*raw(w,u,j,"Q") for w in W),Z)
 return (p,q,p-q)
A={(c,u,j):atom(c,u,j) for c,u,j in product(C,U,J)}
STOP=sum((1-sum(X[w]) for w in W),Z)/3
def lower(d):
 assert 0<=d<=D
 y={k:Z for k in A}; rem=d
 for ratio,k,di in sorted((p/di,k,di) for k,(p,q,di) in A.items() if di>0):
  take=min(F(1),rem/di); y[k]=take; rem-=take*di
 assert rem==0
 return y,Z
def upper(d):
 assert 0<=d<=D
 return {k:(1-d/D if di<0 else F(1)) for k,(p,q,di) in A.items()},F(1)
def outcome(policy):
 y,stop=policy
 a=sum((y[k]*p for k,(p,q,di) in A.items()),Z)+stop*STOP
 b=sum((y[k]*q for k,(p,q,di) in A.items()),Z)+stop*STOP
 return a,b,a-b
def interpolation(lo,hi,r):
 y0,s0=lo; y1,s1=hi
 return {k:(1-r)*y0[k]+r*y1[k] for k in A},(1-r)*s0+r*s1
def run():
 for s in ("P","Q"):
  ls=[raw(w,u,j,s) for w,u,j in product(W,U,J)]
  assert len(ls)==18 and min(ls)>0 and sum(ls)==1
 c1=(sum((sum(row) for row in X),Z)+sum((sum(row[2:]) for row in X),Z))/3
 c2=sum((sum(row) for row in X),Z)/3
 assert (c1,c2,STOP)==(F(43,48),F(7,8),F(1,8))
 assert sum((p for p,q,di in A.values()),Z)+STOP==1
 assert sum((q for p,q,di in A.values()),Z)+STOP==1
 assert all(4*p-3*q>=0 for p,q,di in A.values())
 pos=[(p,q,di) for p,q,di in A.values() if di>0]
 neg=[(p,q,di) for p,q,di in A.values() if di<0]
 assert (len(pos),len(neg))==(8,10)
 assert sum((v[2] for v in pos),Z)==D
 assert sum((v[2] for v in neg),Z)==-D
 assert all(p==-3*di for p,q,di in neg)
 assert sum((p for p,q,di in neg),Z)==3*D
 slopes=[(a1-a0)/(d1-d0) for (d0,a0),(d1,a1) in zip(K,K[1:])]
 assert slopes==[F(3),F(12369,2341),F(1359,251),F(567,13),F(5097,83)]
 targets=set(d for d,a in K)
 targets.update((K[i][0]+K[i+1][0])/2 for i in range(len(K)-1))
 targets.add(F(1,12));samples=[]
 for d in sorted(targets):
  lo,hi=lower(d),upper(d)
  a0,b0,dd0=outcome(lo); a1,b1,dd1=outcome(hi)
  assert dd0==dd1==d and (a1,b1)==(1-3*d,1-4*d)
  for (k0,v0),(k1,v1) in zip(K,K[1:]):
   if k0<=d<=k1:
    assert a0==v0+(v1-v0)*(d-k0)/(k1-k0);break
  for r in (F(0),F(1,3),F(2,3),F(1)):
   a,b,dd=outcome(interpolation(lo,hi,r))
   assert dd==d and a==(1-r)*a0+r*a1 and b==a-d
   if d==F(1,12): samples.append({"weight":str(r),"alpha":str(a),"beta":str(b)})
 return {"schema":"EC49AD_VERTICAL_FILLING_EXACT_V1","sources":2,"leaves_each":18,
 "costs":[str(c1),str(c2)],"STOP":str(STOP),"positive_atoms":len(pos),"negative_atoms":len(neg),
 "capacity":str(D),"negative_atom_identity":"P=-3(P-Q)",
 "lower_slopes":[str(x) for x in slopes],"delta_1_over_12_samples":samples,
 "status":"AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASS / UNREVIEWED / NOT_ADMITTED"}
if __name__=="__main__": print(json.dumps(run(),indent=2))
