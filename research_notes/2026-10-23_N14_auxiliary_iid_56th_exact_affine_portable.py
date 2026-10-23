#!/usr/bin/env python3
"""Exact N14 auxiliary iid 56th interval checker; AUTHOR only; Python stdlib."""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
import json
N=14
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
A=(9,0,2);B=(12,0,1)
SP={(6,6,0),(7,6,0),(7,7,0),(8,6,0),(8,7,0),(8,8,0),(9,6,0),(9,7,0),(9,7,1),(9,8,0),(9,8,1),(10,5,0),(10,6,0),(10,7,0),(10,7,1),(10,8,1),(11,5,0),(11,7,1),(11,8,2),(11,6,1),(8,7,1),(11,4,0),(9,5,0),(10,8,2),(12,7,2)}
SQ={(4,0,3),(4,0,4),(5,0,3),(5,0,4),(5,0,5),(5,1,4),(6,0,3),(6,0,4),(6,1,4),(6,1,5),(6,2,4),(7,0,3),(7,1,4),(7,2,4),(7,2,5),(8,0,3),(8,1,3),(8,2,4),(8,3,4),(8,3,5),(9,1,3),(9,3,4),(9,4,5),(10,0,2),(10,5,5),(10,2,3),(7,1,3),(10,4,4),(3,0,3),(7,3,4)}
AL=F(1292956447084044215,3725075438477770752)
V=F(24752806046065630757,1862537719238885376)
S=F(6623137289528539,10444800000000000)
K=F(1211436,91);LP=72+F(8,9)*K;LQ=K;G=LP+LQ
def child(st,i):
 n,a,b=st;return (n+1,a+(i==0),b+(i==1))
def act(st):
 if st in SP:return 'P'
 if st in SQ:return 'Q'
 n,a,b=st;t=N-n
 if 8*3**a>=9*2**(a+b+t):return 'P'
 if 8*3**(a+t)<9*2**(a+b+t):return 'Q'
 assert n<N,st
 return 'C'
def firsthit(st):
 cur={(0,0):(F(1),F(1),1)}
 for n in range(st[0]):
  nxt=defaultdict(lambda:(F(),F(),0))
  for (a,b),(p,q,k) in cur.items():
   if act((n,a,b))!='C':continue
   for i in range(3):
    key=(a+(i==0),b+(i==1));x,y,l=nxt[key];nxt[key]=(x+p*P[i],y+q*Q[i],l+k)
  cur=dict(nxt)
 return cur.get(st[1:],(F(),F(),0))
@lru_cache(None)
def suffix(st):
 z=act(st)
 if z=='P':return F(),F(1),F(),F()
 if z=='Q':return F(1),F(),F(),F()
 kids=[suffix(child(st,i)) for i in range(3)]
 return (sum((P[i]*kids[i][0] for i in range(3)),F()),
         sum((Q[i]*kids[i][1] for i in range(3)),F()),
         F(1)+sum((P[i]*kids[i][2] for i in range(3)),F()),
         F(1)+sum((Q[i]*kids[i][3] for i in range(3)),F()))
def dual():
 D={};ties=[];pos=neg=checked=0;bad=[]
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    st=(n,a,b);opts={'P':LQ*F(2**(a+b),3**a),'Q':LP}
    if n<N:opts['C']=F(1)+sum((P[i]*D[child(st,i)] for i in range(3)),F())
    z=act(st);base=opts[z]
    for mode,value in opts.items():
     if mode==z:continue
     checked+=1
     if value<base:neg+=1;bad.append((st,z,mode,value-base))
     elif value==base:ties.append((st,z,mode))
     else:pos+=1
    D[st]=base
 return D[(0,0,0)],ties,pos,neg,checked,len(D),bad
def forward(u,s):
 cur={(0,0):(F(1),F(1))};ep=eq=tp=tq=F()
 for n in range(N+1):
  nxt=defaultdict(lambda:(F(),F()))
  for (a,b),(p,q) in cur.items():
   st=(n,a,b)
   if st==A:
    ep+=p*u;p*=1-u;q*=1-u
   elif st==B:
    ep+=p*s;p*=1-s;q*=1-s
   else:
    z=act(st)
    if z=='P':eq+=q;continue
    if z=='Q':ep+=p;continue
   assert n<N,st
   tp+=p;tq+=q
   for i in range(3):
    key=(a+(i==0),b+(i==1));x,y=nxt[key];nxt[key]=(x+p*P[i],y+q*Q[i])
  cur=dict(nxt)
 assert not cur
 return ep,eq,tp,tq
def next_dual():
 vals={};points=[];bad=[]
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    st=(n,a,b);z='Q' if st==A else act(st)
    opts={'P':(F(),F(2**(a+b),3**a)),'Q':(F(72),F(8,9))}
    if n<N:opts['C']=(F(1)+sum((P[i]*vals[child(st,i)][0] for i in range(3)),F()),sum((P[i]*vals[child(st,i)][1] for i in range(3)),F()))
    vals[st]=opts[z]
    for mode,v in opts.items():
     if mode==z or st in (A,B):continue
     c0=v[0]-opts[z][0];c1=v[1]-opts[z][1]
     if c0+c1*K<=0:bad.append((st,z,mode))
     if c1>0:
      nk=-c0/c1
      if nk<K:points.append((nk,st,z,mode))
 return max(points),bad
def check():
 pa,qa,live=firsthit(A);pb,qb,liveb=firsthit(B)
 ca=suffix(A);cb=suffix(B)
 X=pa*(1-ca[0]);Y=qa*ca[1];E=pb*(1-cb[0]);H=qb*cb[1]
 h=(X+Y)/(E+H);eta=X-E*h
 root,ties,pos,neg,compared,states,bad=dual()
 assert (states,compared,pos,neg)==(680,1240,1238,0) and not bad
 assert set(ties)=={(A,'C','Q'),(B,'C','Q')}
 assert root==V+G*AL
 assert (pa,qa,live)==(F(78125,4478976),F(78125,1119744),36)
 assert (pb,qb,liveb)==(F(48828125,725594112),F(48828125,362797056),12)
 assert ca==(F(98221,98304),F(41,248832),F(15703,12288),F(24331,20736))
 assert cb==(F(63,64),F(1,144),F(9,8),F(13,12))
 assert h==F(35913,2720000) and eta==F(7109375,8420761534464)==H*h-Y
 assert 0<S-h<S<1
 for u in (F(),F(1,4),F(1,2),F(3,4),F(1)):
  ep,eq,tp,tq=forward(u,S-h*u)
  assert ep==eq==AL+eta*u and tp==V-G*eta*u and tp>tq
  assert tp+LP*ep+LQ*eq==root
 assert (AL+eta,V-G*eta)==(F(1292959592044044215,3725075438477770752),F(24713151556465630757,1862537719238885376))
 crossing,bad=next_dual()
 assert not bad and crossing==(F(6854544972,576215),(8,5,0),'C','P')
 return {'K56':str(K),'Gamma56':str(G),'eta56':str(eta),'alpha56':str(AL+eta),'V56':str(V-G*eta),'h56':str(h),'s56':str(S-h),'root':str(root),'A56_firsthits':live,'A56_p':str(pa),'A56_q':str(qa),'A56_conditional':list(map(str,ca)),'B_firsthits':liveb,'next_crossing':str(crossing),'bellman_states':states,'comparisons':compared,'positive_slacks':pos,'ties':str(ties)}
if __name__=='__main__':
 print(json.dumps(check(),indent=2))
