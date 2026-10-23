#!/usr/bin/env python3
"""Second author-side check: ordered histories, independent Bellman minimum,
backward risk recursion, four corners. Shares historical stop sets; not Driver."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import runpy
m=runpy.run_path(str(Path(__file__).with_name('2026-10-24_N14_auxiliary_iid_58th_exact_affine_portable.py')))
P,Q,N,A,B,K,AL,V,S,G=[m[z] for z in ('P','Q','N','A','B','K','AL','V','S','G')]
act,child=m['act'],m['child']
def ordered_firsthit(target):
 n,a,b=target;nominal=alive=0;pp=qq=F()
 for word in product(range(3),repeat=n):
  if word.count(0)!=a or word.count(1)!=b:continue
  nominal+=1;st=(0,0,0);p=q=F(1)
  for sym in word:
   if act(st)!='C':break
   st=child(st,sym);p*=P[sym];q*=Q[sym]
  else:
   assert st==target
   alive+=1;pp+=p;qq+=q
 return nominal,alive,pp,qq
@lru_cache(None)
def d(st):
 n,a,b=st;opts=[K*F(2**(a+b),3**a),F(72)+F(8,9)*K]
 if n<N:opts.append(1+sum((P[i]*d(child(st,i)) for i in range(3)),F()))
 return min(opts)
def independent_bellman():
 ties=[];positive=0;bad=[]
 for n in range(N+1):
  for a in range(n+1):
   for b in range(n-a+1):
    st=(n,a,b);opts={'P':K*F(2**(a+b),3**a),'Q':F(72)+F(8,9)*K}
    if n<N:opts['C']=1+sum((P[i]*d(child(st,i)) for i in range(3)),F())
    v=min(opts.values());zs={x for x,y in opts.items() if y==v}
    positive+=len(opts)-len(zs)
    if len(zs)>1:ties.append((st,zs))
    if act(st) not in zs:bad.append(st)
 return d((0,0,0)),ties,positive,d.cache_info().currsize,bad
def backward(u,s):
 @lru_cache(None)
 def f(st):
  if st==A:decide_p=F(u);decide_q=F()
  elif st==B:decide_p=F();decide_q=F(s)
  else:
   z=act(st)
   if z=='P':return F(),F(1),F(),F()
   if z=='Q':return F(1),F(),F(),F()
   decide_p=decide_q=F()
  assert st[0]<N
  kids=[f(child(st,i)) for i in range(3)];remain=1-decide_q-decide_p
  ep=sum((P[i]*kids[i][0] for i in range(3)),F())
  eq=sum((Q[i]*kids[i][1] for i in range(3)),F())
  tp=1+sum((P[i]*kids[i][2] for i in range(3)),F())
  tq=1+sum((Q[i]*kids[i][3] for i in range(3)),F())
  return decide_q+remain*ep,decide_p+remain*eq,remain*tp,remain*tq
 return f((0,0,0))
def main():
 cert=m['check']();h=F(cert['h58']);eta=F(cert['eta58'])
 assert ordered_firsthit(A)==(840,664,F(10375,169869312),F(10375,967458816))
 assert ordered_firsthit(B)==(12,12,F(48828125,725594112),F(48828125,362797056))
 root,ties,positive,states,bad=independent_bellman()
 assert root==F(cert['root']) and positive==1238 and states==680 and not bad
 assert {st for st,_ in ties}=={A,B}
 corners={(u,s):backward(F(u),F(s)) for u in (0,1) for s in (0,1)}
 for i in range(4):
  assert corners[1,1][i]-corners[1,0][i]-corners[0,1][i]+corners[0,0][i]==0
 for u in (F(),F(1,7),F(1,4),F(1,2),F(3,4),F(6,7),F(1)):
  s=S+h*u;val=backward(u,s)
  affine=tuple(corners[0,0][i]+u*(corners[1,0][i]-corners[0,0][i])+s*(corners[0,1][i]-corners[0,0][i]) for i in range(4))
  assert val==affine and val[0]==val[1]==AL+eta*u and val[2]==V-G*eta*u and val[2]>val[3]
 assert backward(F(1),S+h)[:3]==(F(cert['alpha58']),F(cert['alpha57']),F(cert['V58']))
 print('PASS: 59049 ordered length-10 words; 664/840 A58 first hits; 531441 length-12 words; B first hits 12/12')
 print('PASS: 680-state independent minimization, 1238 strict gaps, exactly two tied states')
 print('PASS: four backward corners, seven rational mixtures, optimality and tP dominance')
if __name__=='__main__':main()
