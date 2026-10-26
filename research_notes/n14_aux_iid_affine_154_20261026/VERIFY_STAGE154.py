#!/usr/bin/env python3
"""Author-side exact Stage154 verification. Only standard-library integer/Fraction arithmetic.
External ternary iid N14 model, NOT P000/X6.
Run: python VERIFY_STAGE154.py; emits certificate154_recomputed.json in current directory.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
PW=(3,1,20);QW=(1,1,10);N=14
B=(11,0,1);S=(10,5,4)
K=F(68426856,199229);L=F(68268104,199229)
a153=F(18373341781933759925,52808422392537808896)
v153=F(318626572163909741813,26404211196268904448)
def child(s,i):
 n,a,b=s;return n+1,a+(i==0),b+(i==1)
def states():
 for n in range(15):
  for a in range(n+1):
   for b in range(n-a+1):yield(n,a,b)
def rho(s):
 _,a,b=s;return F(2**(a+b),3**a)
@lru_cache(None)
def dual(s):
 acts={'P':K*rho(s),'Q':L}
 if s[0]<N:acts['C']=1+sum(P[i]*dual(child(s,i))[0] for i in range(3))
 v=min(acts.values());return v,tuple(a for a,x in acts.items() if x==v),acts
I={s:dual(s) for s in states()}
T={s:a for s,(_,a,_) in I.items() if len(a)>1}
G=[x-v for v,a,acts in I.values() for x in acts.values() if x>v]
assert len(I)==680 and T=={B:('Q','C'),S:('Q','C')}
assert len(G)==1238 and min(G)==F(4439,398458)
H=dual((0,0,0))[0]
assert H==F(1824690544010408840595299,7275912299338115579904)
# b,s are binary Q-stop coins at the two Q/continue ties
def action(st,b,s):
 if st==B:return 'Q' if b else 'C'
 if st==S:return 'Q' if s else 'C'
 return dual(st)[1][0]
@lru_cache(None)
def obs(st,b,s):
 a=action(st,b,s)
 if a=='P':return(F(0),F(1),F(0),F(0))
 if a=='Q':return(F(1),F(0),F(0),F(0))
 v=[obs(child(st,i),b,s) for i in range(3)]
 return(sum(P[i]*v[i][0] for i in range(3)),
        sum(Q[i]*v[i][1] for i in range(3)),
        1+sum(P[i]*v[i][2] for i in range(3)),
        1+sum(Q[i]*v[i][3] for i in range(3)))
M={(b,s):obs((0,0,0),b,s) for b,s in product((0,1),repeat=2)}
def add(*lst):return tuple(sum(t) for t in zip(*lst))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(k,v):return tuple(k*x for x in v)
m00=M[(0,0)];dB=sub(M[(1,0)],m00);dS=sub(M[(0,1)],m00)
assert M[(1,1)]==add(m00,dB,dS)
# Literally enumerate ordered tree prefixes. No state memoization.
def dfs(b,s):
 vals=[F(0)]*4;stack=[((0,0,0),1,1)];nodes=0
 while stack:
  st,pn,qn=stack.pop();nodes+=1
  a=action(st,b,s);n=st[0]
  if a=='C':
   for i in range(3):stack.append((child(st,i),pn*PW[i],qn*QW[i]))
  else:
   p=F(pn,24**n);q=F(qn,12**n)
   if a=='Q':vals[0]+=p
   else:vals[1]+=q
   vals[2]+=n*p;vals[3]+=n*q
 return tuple(vals),nodes
DFS={}
for k in M:
 v,n=dfs(*k);assert v==M[k];DFS[k]=n
assert [DFS[k] for k in [(0,0),(0,1),(1,0),(1,1)]]==[473212,466012,473080,465880]
# Literal first-hit prefixes stop before either tie can be traversed.
hits={B:[0,F(0),F(0)],S:[0,F(0),F(0)]};stack=[((0,0,0),1,1)]
while stack:
 st,pn,qn=stack.pop()
 if st in hits:
  hits[st][0]+=1;hits[st][1]+=F(pn,24**st[0]);hits[st][2]+=F(qn,12**st[0]);continue
 if dual(st)[1][0]=='C':
  for i in range(3):stack.append((child(st,i),pn*PW[i],qn*QW[i]))
assert hits[B]==[11,F(107421875,1451188224),F(107421875,725594112)]
assert hits[S]==[300,F(125,5435817984),F(125,2579890176)]
# Equal-error affine mixing, legal for every real 0<=s<=1.
D0=m00[0]-m00[1];Db=dB[0]-dB[1];Ds=dS[0]-dS[1]
b0=-D0/Db;beta=-Ds/Db
assert b0==F(7483738461750611,8143872000000000)
assert beta==-F(1149859,2714624000000)
def mix(s):
 b=b0+beta*s
 m=add(m00,mul(b,dB),mul(s,dS))
 assert m[0]==m[1] and 0<b<1
 assert m[2]+L*m[0]+K*m[1]==H
 return b,m
b_left,left=mix(F(1));b_right,right=mix(F(0))
eta=right[0]-left[0]
assert left[0]==a153 and left[2]==v153
assert eta==F(24903625,2200350933022408704)
assert right[0]==F(18373341782531446925,52808422392537808896)
assert right[2]==F(318626571958867301813,26404211196268904448)
assert left[2]>left[3] and right[2]>right[3]
assert K+L==F(136694960,199229)
def fr(x):return str(x.numerator)+'/'+str(x.denominator)
def vec(v):return [fr(x) for x in v]
cert={
 'model':'EXTERNAL_AUXILIARY_IID_TERNARY_N14','status':'AUTHOR_EXACT','stage':154,
 'K':fr(K),'L':fr(L),'H':fr(H),'states':len(I),
 'ties':{str(k):list(v) for k,v in T.items()},
 'strict_gap_count':len(G),'strict_gap_min':fr(min(G)),
 'M00':vec(m00),'dB':vec(dB),'dS':vec(dS),
 'mixed_fourvector':vec(sub(M[(1,1)],add(m00,dB,dS))),
 'corners':{str(k):vec(v) for k,v in M.items()},
 'DFS_nodes':{str(k):DFS[k] for k in M},
 'first_hits':{str(k):{'ordered_count':v[0],'P_mass':fr(v[1]),'Q_mass':fr(v[2])} for k,v in hits.items()},
 'b0':fr(b0),'beta':fr(beta),
 'stage153':{'alpha':fr(left[0]),'value':fr(left[2]),'b':fr(b_left)},
 'stage154':{'alpha':fr(right[0]),'value':fr(right[2]),'b':fr(b_right)},
 'eta':fr(eta),'slope':fr(K+L)}
with open('certificate154_recomputed.json','w') as f:json.dump(cert,f,indent=2)
print('PASS stage154 N14, full-real support, two exact observer methods')
print(json.dumps(cert,indent=2))
