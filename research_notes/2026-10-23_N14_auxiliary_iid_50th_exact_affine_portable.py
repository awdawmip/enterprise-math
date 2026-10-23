#!/usr/bin/env python3
"""Exact Fraction author certificate, auxiliary iid N14 50th interval."""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6));N=14
A=(9,5,0);B=(12,0,1)
SP={(6,6,0),(7,6,0),(7,7,0),(8,6,0),(8,7,0),(8,8,0),(9,6,0),(9,7,0),(9,7,1),(9,8,0),(9,8,1),(10,5,0),(10,6,0),(10,7,0),(10,7,1),(10,8,1),(11,5,0),(11,7,1),(11,8,2),(11,6,1),(8,7,1),(11,4,0)}
SQ={(4,0,3),(4,0,4),(5,0,3),(5,0,4),(5,0,5),(5,1,4),(6,0,3),(6,0,4),(6,1,4),(6,1,5),(6,2,4),(7,0,3),(7,1,4),(7,2,4),(7,2,5),(8,0,3),(8,1,3),(8,2,4),(8,3,4),(8,3,5),(9,1,3),(9,3,4),(9,4,5),(10,0,2),(10,5,5),(10,2,3),(7,1,3)}
K=F(137448576,7601);LP=72+F(8,9)*K;LQ=K;G=LP+LQ
AL=F(5171824816656394397,14900301753911083008)
V=F(12378473542489900069,931268859619442688)
S=F(8822627424173923,13926400000000000)
def child(st,i):
 n,a,b=st;return n+1,a+(i==0),b+(i==1)
def act(st):
 if st in SP:return 'P'
 if st in SQ:return 'Q'
 n,a,b=st;t=N-n
 if 8*3**a>=9*2**(a+b+t):return 'P'
 if 8*3**(a+t)<9*2**(a+b+t):return 'Q'
 assert n<N
 return 'C'
def reached(target):
 cur={(0,0):(F(1),F(1),1)}
 for n in range(target[0]):
  nxt=defaultdict(lambda:(F(),F(),0))
  for (a,b),(p,q,w) in cur.items():
   if act((n,a,b))!='C':continue
   for i in range(3):
    z=(a+(i==0),b+(i==1));x,y,v=nxt[z]
    nxt[z]=(x+p*P[i],y+q*Q[i],v+w)
  cur=dict(nxt)
 return cur.get(target[1:],(F(),F(),0))
@lru_cache(None)
def suffix(st):
 z=act(st)
 if z=='P':return F(),F(1),F(),F()
 if z=='Q':return F(1),F(),F(),F()
 xs=[suffix(child(st,i)) for i in range(3)]
 return (sum((P[i]*xs[i][0] for i in range(3)),F()),sum((Q[i]*xs[i][1] for i in range(3)),F()),1+sum((P[i]*xs[i][2] for i in range(3)),F()),1+sum((Q[i]*xs[i][3] for i in range(3)),F()))
def dual():
 d={};ties=[];c=0
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    st=(n,a,b);opts={'P':LQ*F(2**(a+b),3**a),'Q':LP}
    if n<N:opts['C']=1+sum((P[i]*d[child(st,i)] for i in range(3)),F())
    z=act(st)
    for mode,value in opts.items():
     if mode==z:continue
     c+=1
     assert value>=opts[z],(st,z,mode)
     if value==opts[z]:ties.append((st,z,mode))
    d[st]=opts[z]
 assert len(d)==680 and c==1240
 assert set(ties)=={(A,'C','P'),(B,'C','Q')}
 return d[(0,0,0)]
def forward(u,s):
 cur={(0,0):(F(1),F(1))};ep=eq=tp=tq=F()
 for n in range(N+1):
  nxt=defaultdict(lambda:(F(),F()))
  for (a,b),(p,q) in cur.items():
   st=(n,a,b)
   if st==A:eq+=q*u;p*=1-u;q*=1-u
   elif st==B:ep+=p*s;p*=1-s;q*=1-s
   elif act(st)=='P':eq+=q;continue
   elif act(st)=='Q':ep+=p;continue
   assert n<N
   tp+=p;tq+=q
   for i in range(3):
    z=(a+(i==0),b+(i==1));x,y=nxt[z];nxt[z]=(x+p*P[i],y+q*Q[i])
  cur=dict(nxt)
 assert not cur
 return ep,eq,tp,tq
def check():
 pa,qa,live=reached(A);pb,qb,liveb=reached(B)
 assert (live,pa,qa)==(126,F(4375,2359296),F(4375,17915904))
 assert (liveb,pb,qb)==(12,F(48828125,725594112),F(48828125,362797056))
 ca=suffix(A);cb=suffix(B)
 assert ca==(F(415,1327104),F(62047,62208),F(61603,55296),F(6461,5184))
 assert cb==(F(63,64),F(1,144),F(9,8),F(13,12))
 X=pa*ca[0];Y=qa*(1-ca[1]);E=pb*(1-cb[0]);H=qb*cb[1]
 h=(X+Y)/(E+H);eta=-X+E*h
 assert h==F(13277523,21760000000)
 assert eta==Y-H*h==F(33254375,538928738205696)
 root=dual();assert root==V+G*AL
 for u in (F(),F(1,4),F(1,2),F(3,4),F(1)):
  s=S+h*u;ep,eq,tp,tq=forward(u,s)
  assert 0<=s<=1
  assert ep==eq==AL+eta*u
  assert tp==V-G*eta*u and tp>=tq
  assert tp+LP*ep+LQ*eq==root
 assert AL+eta==F(5171825736073354397,14900301753911083008)
 assert V-G*eta==F(12376506639448300069,931268859619442688)
 print('PASS: N14 exact 50th author-side certificate; 680 states, 1240 actions')
if __name__=='__main__':check()
