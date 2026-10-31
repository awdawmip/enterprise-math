"""Exact Fraction endpoint certificate for EC49AS; Python >=3.8, no packages."""
from fractions import Fraction as Q
from itertools import combinations, product
import json
Z=Q(0); A=(1,1,2,2,0); I=tuple(product(range(3),range(5)))
E0=Q(175,674); E1=Q(32,103); COST=Q(13,16); K=Q(177,172)
W=((Z,Q(3,16),Q(1,4),Z,Q(9,16)),(Q(1),Z,Z,Z,Z),(Z,Q(1),Z,Z,Z))
X=((Z,Q(11,16),Z,Z,Q(5,16)),(Q(1),Z,Z,Z,Z),(Z,Q(1),Z,Z,Z))
def solve(s,boundary):
 n=5 if boundary else 4; rhs=[Q(1)]*3+[Q(43,16)]
 if boundary: rhs += [Q(39,16)]
 a=[[Q(w==i) for w,c in s]+[rhs[i]] for i in range(3)]
 a.append([Q(A[c]) for w,c in s]+[rhs[3]])
 if boundary: a.append([Q(c<4) for w,c in s]+[rhs[4]])
 for k in range(n):
  p=next((i for i in range(k,n) if a[i][k]),None)
  if p is None: return None
  a[k],a[p]=a[p],a[k]; f=a[k][k]; a[k]=[v/f for v in a[k]]
  for i in range(n):
   if i!=k:
    f=a[i][k];a[i]=[a[i][j]-f*a[k][j] for j in range(n+1)]
 v=[a[i][-1] for i in range(n)]
 if any(t<=0 for t in v): return None
 out=[[Z]*5 for _ in range(3)]
 for (w,c),t in zip(s,v):out[w][c]=t
 return tuple(tuple(row) for row in out)
def mass(x):return sum((x[w][c] for w in range(3) for c in range(4)),Z)/3
def delta(x,e,c,u,z):
 p=q=Z
 for w in range(3):
  t=Q(1,2)+(2*u-1)*(1-w)*e
  p+=x[w][c]*t*(Q(1,6) if w==z else Q(1,12))
  q+=x[w][c]*t/9
 return p-K*q,p,q
def env(x,e):return sum((max(Z,delta(x,e,c,u,z)[0]) for c,u,z in product(range(4),range(2),range(3))),Z)
def witness(e):
 a=b=Z
 for c,u,z in product(range(4),range(2),range(3)):
  if (c,z) in {(0,1),(1,2),(2,0)} or (c,u,z)==(1,1,0):
   _,p,q=delta(W,e,c,u,z); a+=p; b+=q
 return a,b,a-K*b
v4={v for s in combinations(I,4) if (v:=solve(s,False)) is not None}
v5={v for s in combinations(I,5) if (v:=solve(s,True)) is not None}
high={v for v in v4 if mass(v)>=COST}
assert (len(v4),len(v5),len(high))==(168,144,24)
assert len(high|v5)==168 and all(mass(x)==COST for x in v5)
assert sum((A[c]*W[w][c] for w,c in I),Z)/3==Q(43,48)
assert mass(W)==COST and all(sum(row)==1 for row in W)
assert mass(X)==Q(43,48) and all(sum(row)==1 for row in X)
reports=[]
for e,mh,mb,ht,bt in [(E0,Q(36,337),Q(77,688),4,24),(E1,Q(1503,13184),Q(1503,13184),4,8)]:
 h=[env(x,e) for x in high];b=[env(x,e) for x in v5]
 assert (max(h),max(b))==(mh,mb)
 assert (sum(t==mh for t in h),sum(t==mb for t in b))==(ht,bt)
 line=Q(77,688)+(674*e-175)/16512
 assert max(mh,mb)==line and witness(e)[2]==line
 a,q,_=witness(e)
 reports.append(dict(eta=str(e),high_max=str(mh),boundary_max=str(mb),high_ties=ht,boundary_ties=bt,alpha=str(a),beta=str(q),H=str(line)))
assert witness(Q(3,10))==(Q(83,192),Q(223,720),Q(293,2580))
assert witness(E1)==(Q(1423,3296),Q(3053,9888),Q(1503,13184))
for e in (E0,E1,Q(3,10)):
 assert delta(W,e,1,1,0)[0]==(674*e-175)/16512
for c,u,z in product(range(4),range(2),range(3)):
 assert delta(X,E1,c,u,z)[0]*delta(X,Q(1,3),c,u,z)[0]>=0
for e in (E1,Q(1,3)):
 assert env(X,e)==Q(9,128)+Q(9,64)*e
assert Q(9,64)-Q(337,8256)==Q(103,1032)
print(json.dumps(dict(schema='EC49AS_EXACT_FRACTION_CERT_V1',status='AUTHOR_EXACT_CHECK_PASS_UNREVIEWED_NOT_ADMITTED',interval='175/674 <= eta <= 32/103',global_optimum='77/688+(674*eta-175)/16512',C1='43/48',C2='13/16',k='177/172',v4=len(v4),v5=len(v5),high=len(high),endpoints=reports,example_eta_3_10='293/2580',upper_envelope_barrier='32/103; high-x F=9/128+9*eta/64 on [32/103,1/3]'),indent=2,sort_keys=True))
