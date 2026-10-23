#!/usr/bin/env python3
"""Author-side alternate checker for N14-46: backward absorption recursion.
Independent implementation (does not import main checker); same inherited sources.
"""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json
N=14
P=(F(1,8), F(1,24), F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
A=(8,7,1);B=(12,0,1)
stopP={(6,6,0),(7,6,0),(7,7,0),(8,6,0),(8,7,0),(8,8,0),
(9,6,0),(9,7,0),(9,7,1),(9,8,0),(9,8,1),
(10,5,0),(10,6,0),(10,7,0),(10,7,1),(10,8,1),
(11,5,0),(11,7,1),(11,8,2),(11,6,1)}
stopQ={(4,0,3),(4,0,4),(5,0,3),(5,0,4),(5,0,5),(5,1,4),
(6,0,3),(6,0,4),(6,1,4),(6,1,5),(6,2,4),
(7,0,3),(7,1,4),(7,2,4),(7,2,5),
(8,0,3),(8,1,3),(8,2,4),(8,3,4),(8,3,5),
(9,1,3),(9,3,4),(9,4,5),(10,0,2),(10,5,5)}

def cr(st,i):
 n,a,b=st
 return n+1,a+int(i==0),b+int(i==1)

def sel(st):
 if st in stopP:return 1
 if st in stopQ:return -1
 n,a,b=st
 if 8*3**a>=9*2**(a+b+14-n):return 1
 if 8*3**(a+14-n)<9*2**(a+b+14-n):return -1
 assert n<14
 return 0

def evaluate(u,s):
 @lru_cache(None)
 def ev(st):
  n,a,b=st
  directP=(F(),F(1),F(),F())
  directQ=(F(1),F(),F(),F())
  t=sel(st)
  if st==A: chanceP=u;chanceQ=F()
  elif st==B:chanceP=F();chanceQ=s
  elif t==1:return directP
  elif t==-1:return directQ
  else:chanceP=chanceQ=F()
  childs=[ev(cr(st,i)) for i in range(3)]
  cont=(sum((P[i]*childs[i][0] for i in range(3)),F()),
        sum((Q[i]*childs[i][1] for i in range(3)),F()),
        F(1)+sum((P[i]*childs[i][2] for i in range(3)),F()),
        F(1)+sum((Q[i]*childs[i][3] for i in range(3)),F()))
  return tuple(chanceP*directP[k]+chanceQ*directQ[k]+(1-chanceP-chanceQ)*cont[k] for k in range(4))
 return ev((0,0,0))

def compare():
 c=json.loads(Path(__file__).with_name('2026-10-23_N14_auxiliary_iid_46th_exact_affine_certificate.json').read_text())
 def f(s):return F(s)
 L=f(c['dual']['lambda_P']);M=f(c['dual']['lambda_Q'])
 z00=evaluate(F(),F())
 z10=evaluate(F(1),F())
 z01=evaluate(F(),F(1))
 z11=evaluate(F(1),F(1))
 assert all(z11[i]-z10[i]-z01[i]+z00[i]==0 for i in range(4))
 def interpolate(u,s):return tuple(z00[i]+(z10[i]-z00[i])*u+(z01[i]-z00[i])*s for i in range(4))
 s0=f(c['compensation']['s45']);h=f(c['compensation']['h46'])
 eta=f(c['compensation']['eta46'])
 al=f(c['interval']['alpha45']);val=f(c['interval']['V45'])
 root=f(c['dual']['root']);G=L+M
 for u in (F(),F(1,7),F(1,3),F(2,3),F(1)):
  ans=interpolate(u,s0+h*u)
  assert ans[0]==ans[1]==al+eta*u
  assert ans[2]==val-G*eta*u and ans[2]>=ans[3]
  assert ans[2]+L*ans[0]+M*ans[1]==root
 assert interpolate(F(1),s0+h)[0]==f(c['interval']['alpha46'])
 assert interpolate(F(1),s0+h)[2]==f(c['interval']['V46'])
 print('Independent backward absorption / corner interpolation PASS')
 print('bilinear interaction absent; A and B prefix-incomparable')
 print('alpha46',f(c['interval']['alpha46']))
 print('V46',f(c['interval']['V46']))

if __name__=='__main__':compare()
