#!/usr/bin/env python3
"""Second author-side exact checker: ordered first-hit words, independent
Bellman minimization, backward risk DP and four-corner interpolation.
Shares historical stop sets; this is NOT external independent mathematical review.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import runpy
m=runpy.run_path(str(Path(__file__).with_name('2026-10-23_N14_auxiliary_iid_54th_exact_affine_portable.py')))
P,Q,N,A,B,S,AL,V,K,G=[m[z] for z in ('P','Q','N','A','B','S','AL','V','K','G')]
act=m['act'];child=m['child'];check=m['check']
EXPECTED=check()
H=F(EXPECTED['h54']);ETA=F(EXPECTED['eta54'])
def exact_words(target):
 total=alive=0;ps=qs=F()
 for word in product(range(3),repeat=target[0]):
  if word.count(0)!=target[1] or word.count(1)!=target[2]:continue
  total+=1;st=(0,0,0);p=q=F(1)
  for sym in word:
   if act(st)!='C':break
   st=child(st,sym);p*=P[sym];q*=Q[sym]
  else:
   assert st==target
   alive+=1;ps+=p;qs+=q
 return total,alive,ps,qs
def backward(u,s):
 @lru_cache(None)
 def value(st):
  if st==A:ps,qs=F(),u
  elif st==B:ps,qs=F(),s
  else:
   mode=act(st)
   if mode=='P':return F(),F(1),F(),F()
   if mode=='Q':return F(1),F(),F(),F()
   ps=qs=F()
  assert st[0]<N
  vals=[value(child(st,i)) for i in range(3)]
  pe=sum((P[i]*vals[i][0] for i in range(3)),F())
  qe=sum((Q[i]*vals[i][1] for i in range(3)),F())
  pt=1+sum((P[i]*vals[i][2] for i in range(3)),F())
  qt=1+sum((Q[i]*vals[i][3] for i in range(3)),F())
  return (qs+(1-ps-qs)*pe,ps+(1-ps-qs)*qe,(1-ps-qs)*pt,(1-ps-qs)*qt)
 return value((0,0,0))
def independent_bellman():
 lp=72+F(8,9)*K;lq=K
 @lru_cache(None)
 def d(st):
  n,a,b=st
  choices=[lq*F(2**(a+b),3**a),lp]
  if n<N:choices.append(1+sum((P[i]*d(child(st,i)) for i in range(3)),F()))
  return min(choices)
 ties=[];strict=0
 for n in range(N+1):
  for a in range(n+1):
   for b in range(n-a+1):
    st=(n,a,b)
    opts={'P':lq*F(2**(a+b),3**a),'Q':lp}
    if n<N:opts['C']=1+sum((P[i]*d(child(st,i)) for i in range(3)),F())
    best=min(opts.values());eq=[mode for mode,v in opts.items() if v==best]
    strict+=len(opts)-len(eq)
    if len(eq)>1:ties.append((st,eq))
 return d((0,0,0)),ties,strict,d.cache_info().currsize
def nested_A51():
 target=(10,4,4);total=live=through=0
 for word in product(range(3),repeat=target[0]):
  if word.count(0)!=target[1] or word.count(1)!=target[2]:continue
  total+=1;st=(0,0,0);visited=False
  for sym in word:
   if act(st)!='C':break
   st=child(st,sym)
   if st==A:visited=True
  else:
   assert st==target
   live+=1
   if visited:through+=1
 return total,live,through

def main():
 assert exact_words(A)==(35,19,F(19,169869312),F(19,35831808))
 assert exact_words(B)==(12,12,F(48828125,725594112),F(48828125,362797056))
 assert nested_A51()==(3150,1549,19),nested_A51()
 root,ties,strict,states=independent_bellman()
 assert (states,strict)==(680,1238)
 assert {st for st,eq in ties}=={A,B}
 assert root==V+G*AL
 corners={(u,s):backward(F(u),F(s)) for u in (0,1) for s in (0,1)}
 assert all(corners[1,1][j]-corners[1,0][j]-corners[0,1][j]+corners[0,0][j]==0 for j in range(4))
 for u in (F(),F(1,4),F(1,2),F(3,4),F(1)):
  s=S-H*u
  exact=backward(u,s)
  interp=tuple(corners[0,0][j]+u*(corners[1,0][j]-corners[0,0][j])+s*(corners[0,1][j]-corners[0,0][j]) for j in range(4))
  assert exact==interp
  assert exact[0]==exact[1]==AL+ETA*u
  assert exact[2]==V-G*ETA*u>exact[3]
 assert backward(F(1),S-H)[:3]==(F(EXPECTED['alpha54']),F(EXPECTED['alpha54']),F(EXPECTED['V54']))
 print('PASS: 2187 words at A54 (19/35 live), 531441 at B (12 live), 59049 at nested A51')
 print('PASS: 680-state independent Bellman minimization, two ties and 1238 strict slacks')
 print('PASS: four backward corners and five exact interpolation settings')
if __name__=='__main__':main()
