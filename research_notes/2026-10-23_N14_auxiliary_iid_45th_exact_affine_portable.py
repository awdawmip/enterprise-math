#!/usr/bin/env python3
"""Self-contained exact N=14 auxiliary iid 45th affine certificate.
No external packages, prior certificate, native BRC bridge, or Driver review.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
from math import comb
N=14
P=(F(3,24),F(1,24),F(20,24))
Q=(F(2,24),F(2,24),F(20,24))
A=(11,6,1); B=(12,0,1)
SP={tuple(x) for x in (
 (6,6,0),(7,6,0),(7,7,0),(8,6,0),(8,7,0),(8,8,0),
 (9,6,0),(9,7,0),(9,7,1),(9,8,0),(9,8,1),
 (10,5,0),(10,6,0),(10,7,0),(10,7,1),(10,8,1),
 (11,5,0),(11,7,1),(11,8,2))}
SQ={tuple(x) for x in (
 (4,0,3),(4,0,4),(5,0,3),(5,0,4),(5,0,5),(5,1,4),
 (6,0,3),(6,0,4),(6,1,4),(6,1,5),(6,2,4),
 (7,0,3),(7,1,4),(7,2,4),(7,2,5),
 (8,0,3),(8,1,3),(8,2,4),(8,3,4),(8,3,5),
 (9,1,3),(9,3,4),(9,4,5),(10,0,2),(10,5,5))}
K=F(1320948,47); LP=F(1177560,47); LQ=K; G=LP+LQ
alpha44=F(5171815348217925797,14900301753911083008)
V44=F(193782614607902809,14551075931553792)
s44=F(26391957913028113,41779200000000000)

def child(st,i):
 n,a,b=st
 return n+1,a+(i==0),b+(i==1)

def act(st):
 if st in SP:return 'P'
 if st in SQ:return 'Q'
 n,a,b=st;t=N-n
 if 8*3**a>=9*2**(a+b+t):return 'P'
 if 8*3**(a+t)<9*2**(a+b+t):return 'Q'
 assert n<N,st
 return 'C'

def reached(st):
 cur={(0,0):(F(1),F(1),1)}
 for n in range(st[0]):
  nxt=defaultdict(lambda:(F(),F(),0))
  for (a,b),(p,q,m) in cur.items():
   if act((n,a,b))!='C':continue
   for i in range(3):
    x=(a+(i==0),b+(i==1));pa,qa,m0=nxt[x]
    nxt[x]=pa+p*P[i],qa+q*Q[i],m0+m
  cur=dict(nxt)
 return cur.get(st[1:],(F(),F(),0))

@lru_cache(None)
def cond(st):
 x=act(st)
 if x=='P':return (F(),F(1),F(),F())
 if x=='Q':return (F(1),F(),F(),F())
 rows=[cond(child(st,i)) for i in range(3)]
 return (sum((P[i]*rows[i][0] for i in range(3)),F()),
         sum((Q[i]*rows[i][1] for i in range(3)),F()),
         1+sum((P[i]*rows[i][2] for i in range(3)),F()),
         1+sum((Q[i]*rows[i][3] for i in range(3)),F()))

def run(u,s):
 cur={(0,0):(F(1),F(1))};ep=eq=tp=tq=F()
 for n in range(N+1):
  nxt=defaultdict(lambda:(F(),F()))
  for (a,b),(p,q) in cur.items():
   st=(n,a,b)
   if st==A:eq+=q*u;p*=1-u;q*=1-u
   elif st==B:ep+=p*s;p*=1-s;q*=1-s
   elif act(st)=='P':eq+=q;continue
   elif act(st)=='Q':ep+=p;continue
   assert n<N,st
   tp+=p;tq+=q
   for i in range(3):
    x=(a+(i==0),b+(i==1));pa,qa=nxt[x]
    nxt[x]=pa+p*P[i],qa+q*Q[i]
  cur=dict(nxt)
 assert not cur
 return ep,eq,tp,tq

def dual():
 dp={};neg=[];ties=[];nchecks=0
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    st=(n,a,b);opts={'P':LQ*F(2**(a+b),3**a),'Q':LP}
    if n<N:opts['C']=1+sum((P[i]*dp[child(st,i)] for i in range(3)),F())
    m=act(st);v=opts[m];dp[st]=v
    for alternative,value in opts.items():
     if alternative==m:continue
     nchecks+=1
     if value<v:neg.append((st,m,alternative,value-v))
     if value==v:ties.append((st,m,alternative))
 assert not neg and len(dp)==680 and nchecks==1240
 assert set(ties)=={(A,'C','P'),(B,'C','Q')},ties
 return dp[(0,0,0)]

def check():
 pA,qA,mA=reached(A);pB,qB,mB=reached(B)
 assert mA==1980 and mB==12
 assert mA<comb(11,6)*comb(5,1)==2310
 assert (pA,qA)==(F(34375,226492416),F(34375,1289945088))
 assert (pB,qB)==(F(48828125,725594112),F(48828125,362797056))
 ca=cond(A);cb=cond(B)
 assert ca==(F(1,13824),F(1727,1728),F(601,576),F(157,144))
 assert cb==(F(63,64),F(1,144),F(9,8),F(13,12))
 d=pA*ca[0];w=qA*(1-ca[1]);e=pB*(1-cb[0]);h0=qB*cb[1]
 h=(d+w)/(e+h0);eta=-d+h*e
 assert h==F(57849,4352000000)
 assert eta==w-h*h0==F(1615625,538928738205696)
 root=dual()
 assert root==V44+G*alpha44
 base=run(F(),s44)
 assert base[0]==base[1]==alpha44 and base[2]==V44
 for u in map(F,(0,F(1,4),F(1,2),F(3,4),1)):
  s=s44+h*u
  ep,eq,tp,tq=run(u,s)
  assert 0<s<1 and ep==eq==alpha44+eta*u
  assert tp==V44-G*eta*u and tp>=tq
  assert tp+LP*ep+LQ*eq==root
 a45=alpha44+eta;v45=V44-G*eta
 assert a45==F(5171815392886725797,14900301753911083008)
 assert v45==F(193780295680165309,14551075931553792)
 assert run(F(1),s44+h)[2]-run(F(1),s44+h)[3]==F(1805488840366522333,3725075438477770752)
 print('CERTIFIED exact auxiliary interval 45')
 print('alpha45',a45,'V45',v45)
 print('eta45',eta,'h45',h,'slope',-G,'dual-root',root)
 print('A live/nominal',mA,'/ 2310 ; B live',mB)
 print('Bellman states=680 comparisons=1240 zero-slack=2')
 print('This is an author computational proof only, not independent review or native transfer.')

if __name__=='__main__':check()
