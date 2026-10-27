"""Exact Fraction witness and zonotope-support certificate; finite checks do not prove universal real theorem."""
from fractions import Fraction as F
from random import Random
import json
N={'':(0,('a','b')),'a':(1,('ax','ay')),'b':(1,('bu','bv')),
'ax':(2,('axL','axM','axH')),'ay':(2,('ayT',)),
'bu':(2,('buL','buM','buH')),'bv':(2,('bvT',))}
for h in ('axL','axM','axH','ayT','buL','buM','buH','bvT'):N[h]=(3,())
R={'':F(1),'a':F(3,2),'b':F(1,2),'ax':F(1),'ay':F(2),
'bu':F(1),'bv':F(1,3),'axL':F(1,2),'axM':F(1),'axH':F(3,2),
'buL':F(1,2),'buM':F(1),'buH':F(3,2),'ayT':F(2),'bvT':F(1,3)}
RS=sorted(set(R[h] for h in N if N[h][0]==3))
def qmass(sa,sb):
 q={'':F(1),'a':F(1,2),'b':F(1,2),'ax':F(1,4),'ay':F(1,4),
 'bu':F(1,8),'bv':F(3,8),'ayT':F(1,4),'bvT':F(3,8)}
 for h,s,v in [('ax',sa,F(1,4)),('bu',sb,F(1,8))]:
  for c,x in zip('LMH',(s,1-2*s,s)):q[h+c]=v*x
 for h,(t,ch) in N.items():
  assert q[h]>0 and R[h]*q[h]>0
  if ch:
   assert sum((q[c] for c in ch),F())==q[h]
   assert sum((R[c]*q[c] for c in ch),F())==R[h]*q[h]
 return q
def pi_random(rng):
 def act(k):
  x=[rng.randrange(9) for _ in range(k)]
  if sum(x)==0:x[0]=1
  return tuple(F(v,sum(x)) for v in x)
 return {h:act(2 if t==3 else 3) for h,(t,_) in N.items()}
def visits(pi,q):
 v={}
 def go(h,z):
  v[h]=q[h]*z
  for k in N[h][1]:go(k,z*pi[h][2])
 go('',F(1))
 return v
def early(pi,q):
 v=visits(pi,q);A={}
 for h,(t,_) in N.items():
  if t==3:continue
  z=(t,R[h]);A.setdefault(z,[F()]*3)
  for j in range(3):A[z][j]+=v[h]*pi[h][j]
 return {h:tuple(A[(t,R[h])][j]/sum(A[(t,R[h])]) for j in range(3))
  if sum(A[(t,R[h])]) else (F(1),F(),F())
  for h,(t,_) in N.items() if t<3}
def terminal_target(pi,q):
 v=visits(pi,q)
 return (sum((v[h]*pi[h][1] for h in N if N[h][0]==3),F()),
  sum((R[h]*v[h]*pi[h][1] for h in N if N[h][0]==3),F()))
def terminal_mass(pi,q):
 v=visits(pi,q);m={r:F() for r in RS}
 for h,(t,_) in N.items():
  if t==3:m[R[h]]+=v[h]
 return m
def distance(m,u,p):
 # Exact distance of (u,p) to a 2D zonotope in Linfty.
 # Only normals perpendicular to generators and coordinate axes can support Z+epsilon Binf.
 normals=[(F(1),F()),(F(-1),F()),(F(),F(1)),(F(),F(-1))]
 for r in RS:normals.extend([(-r,F(1)),(r,F(-1))])
 return max([F()]+[(a*u+b*p-sum((m[r]*max(F(),a+b*r) for r in RS),F()))/(abs(a)+abs(b))
  for a,b in normals])
def main():
 rng=Random(202610272132)
 params=[(F(2,5),F(1,3)),(F(1,3),F(2,5)),(F(1,6),F(1,5)),
 (F(1,3),F(1,3)),(F(49,100),F(1,100)),(F(1,100),F(49,100))]
 checks=zeros=0
 for sa,sb in params:
  q=qmass(sa,sb)
  for _ in range(128):
   pi=pi_random(rng);sig=early(pi,q)
   sig.update({h:(F(1),F()) for h,(t,_) in N.items() if t==3})
   m=terminal_mass(sig,q);u,p=terminal_target(pi,q)
   d=distance(m,u,p)
   v=visits(pi,q);wa,wb=v['ax'],v['bu']
   k=wa*wb/(wa+wb) if wa+wb else F()
   tau=k*(pi['ax'][2]-pi['bu'][2])*(sb-sa)
   assert k<=F(1,12)
   assert d<=max(F(),-tau)/4
   assert d<=abs(sa-sb)/48
   if tau>=0:assert d==0;zeros+=1
   checks+=1
 # Independently check sharp published rational witness.
 sa,sb=F(2,5),F(1,3);q=qmass(sa,sb)
 pi={h:((F(1),F()) if t==3 else (F(1),F(),F())) for h,(t,_) in N.items()}
 for h in ('','a','b','ax','bv'):pi[h]=(F(),F(),F(1))
 pi['bu']=(F(),F(1),F())
 for h in ('axL','axM','bvT'):pi[h]=(F(),F(1))
 sig=early(pi,q);sig.update({h:(F(1),F()) for h,(t,_) in N.items() if t==3})
 assert distance(terminal_mass(sig,q),*terminal_target(pi,q))==F(1,720)
 v=visits(pi,q);k=v['ax']*v['bu']/(v['ax']+v['bu'])
 assert k==F(1,12) and k*(sb-sa)==-F(1,180)
 for h,(t,_) in N.items():
  if t==3:
   r=R[h]
   x=F(1) if r in (F(1,2),F(1,3)) else (F(39,44) if r==1 else F())
   sig[h]=(1-x,x)
 old=terminal_target(pi,q);new=terminal_target(sig,q)
 assert abs(old[0]-new[0])==abs(old[1]-new[1])==F(1,720)
 print(json.dumps({'status':'PASS_EXACT_FRACTION_ZONOTOPE','sampled_policies':checks,
 'zero_direction_examples':zeros,'parameters':[[str(a),str(b)] for a,b in params],
 'upper':'1/48','sharp_witness_distance':'1/720','sharp_witness_k':'1/12',
 'scope':'finite exact implementation verification; universal proof is analytic'},
 indent=2,sort_keys=True))
if __name__=='__main__':main()
