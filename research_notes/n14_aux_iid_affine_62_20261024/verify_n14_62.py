#!/usr/bin/env python3
"""Exact rational exploratory continuation of author N14 auxiliary iid segments: 62nd."""
from fractions import Fraction as F
from collections import defaultdict
from functools import lru_cache
import json
N=14
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
SP={(6,6,0),(7,6,0),(7,7,0),(8,6,0),(8,7,0),(8,8,0),(9,6,0),(9,7,0),(9,7,1),(9,8,0),(9,8,1),(10,5,0),(10,6,0),(10,7,0),(10,7,1),(10,8,1),(11,5,0),(11,7,1),(11,8,2),(11,6,1),(8,7,1),(11,4,0),(9,5,0),(10,8,2),(12,7,2),(8,5,0),(10,6,1),(7,5,0)}
SQ={(4,0,3),(4,0,4),(5,0,3),(5,0,4),(5,0,5),(5,1,4),(6,0,3),(6,0,4),(6,1,4),(6,1,5),(6,2,4),(7,0,3),(7,1,4),(7,2,4),(7,2,5),(8,0,3),(8,1,3),(8,2,4),(8,3,4),(8,3,5),(9,1,3),(9,3,4),(9,4,5),(10,0,2),(10,5,5),(10,2,3),(7,1,3),(10,4,4),(3,0,3),(7,3,4),(9,0,2),(6,1,3),(11,6,5)}
A=(10,4,0);B=(12,0,1)
AL=F(5171839990951598567,14900301753911083008)
V=F(12354545878161016789,931268859619442688)
S=F(25966041820097099,41779200000000000)
K=F(1850688,229);LP=F(72)+F(8,9)*K;LQ=K;G=LP+LQ

def child(st,i):
 n,a,b=st;return n+1,a+(i==0),b+(i==1)
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
    idx=(a+(i==0),b+(i==1));x,y,l=nxt[idx]
    nxt[idx]=(x+p*P[i],y+q*Q[i],l+k)
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
 D={}; ties=[];negative=[];strict=0;comp=0;min_margin=None
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    st=(n,a,b); z=act(st)
    opts={'P':LQ*F(2**(a+b),3**a),'Q':LP}
    if n<N:opts['C']=F(1)+sum((P[i]*D[child(st,i)] for i in range(3)),F())
    val=opts[z]
    for k,v in opts.items():
     if k==z:continue
     comp+=1
     gap=v-val
     if gap<0:negative.append((st,z,k,str(gap)))
     elif gap==0:ties.append((st,z,k))
     else:
      strict+=1
      if min_margin is None or gap<min_margin:min_margin=gap
    D[st]=val
 return D[(0,0,0)],ties,strict,negative,comp,len(D),min_margin

def forward(u,s):
 cur={(0,0):(F(1),F(1))};ep=eq=tp=tq=F()
 for n in range(N+1):
  nxt=defaultdict(lambda:(F(),F()))
  for (a,b),(p,q) in cur.items():
   st=(n,a,b)
   if st==A:
    eq+=q*u;p*=1-u;q*=1-u
   elif st==B:
    ep+=p*s;p*=1-s;q*=1-s
   else:
    z=act(st)
    if z=='P':eq+=q;continue
    if z=='Q':ep+=p;continue
   assert n<N,st
   tp+=p;tq+=q
   for i in range(3):
    idx=(a+(i==0),b+(i==1));x,y=nxt[idx]
    nxt[idx]=x+p*P[i],y+q*Q[i]
  cur=dict(nxt)
 assert not cur
 return ep,eq,tp,tq

def next_dual():
 vals={};cross=[];errors=[]
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    st=(n,a,b);z='P' if st==A else act(st)
    opts={'P':(F(),F(2**(a+b),3**a)),'Q':(F(72),F(8,9))}
    if n<N:opts['C']=(F(1)+sum((P[i]*vals[child(st,i)][0] for i in range(3)),F()),sum((P[i]*vals[child(st,i)][1] for i in range(3)),F()))
    vals[st]=opts[z]
    for m,v in opts.items():
     if m==z or st in (A,B):continue
     c0=v[0]-opts[z][0];c1=v[1]-opts[z][1]
     if c0+c1*K<0:errors.append((st,z,m,str(c0+c1*K)))
     if c1>0:
      nk=-c0/c1
      if nk<K:cross.append((nk,st,z,m))
 return max(cross),errors

def check():
 assert act(A)=='C' and act(B)=='C'
 pa,qa,live=firsthit(A);pb,qb,liveb=firsthit(B)
 ca=suffix(A);cb=suffix(B)
 X=pa*ca[0];Y=qa*(1-ca[1]);E=pb*(1-cb[0]);H=qb*cb[1]
 h=(X+Y)/(E+H);eta=E*h-X
 root,ties,pos,neg,comp,states,margin=dual()
 f0=forward(F(),S); f1=forward(F(1),S+h)
 ds=(f1[0]-f0[0], f1[1]-f0[1]);dv=f1[2]-f0[2]
 nxt,errors=next_dual()
 assert (states,comp)==(680,1240)
 assert not neg and set(ties)=={(A,'C','P'),(B,'C','Q')},ties
 assert root==V+G*AL
 assert f0[0]==f0[1]==AL and f0[2]==V
 assert S>0 and 0<=S+h<=1
 assert eta>0 and ds==(eta,eta) and dv==-G*eta
 assert (f0[2]-f0[3])>0 and (f1[2]-f1[3])>0
 assert not errors and nxt==(F(10902924,1475),(9,2,3),'C','Q'),(nxt,errors)
 for u in (F(),F(1,7),F(1,4),F(1,2),F(3,4),F(6,7),F(1)):
  ep,eq,tp,tq=forward(u,S+h*u)
  assert ep==eq==AL+eta*u
  assert tp==V-G*eta*u and tp>tq
  assert tp+LP*ep+LQ*eq==root
 return {'status':'AUTHOR_EXACT_RATIONAL_CHECKED_DRIVER_UNREVIEWED','K62':str(K),'lp':str(LP),'lq':str(LQ),'Gamma62':str(G),
  'p_A':str(pa),'q_A':str(qa),'live_A':live,'p_B':str(pb),'q_B':str(qb),'live_B':liveb,
  'ca':list(map(str,ca)),'cb':list(map(str,cb)), 'X':str(X),'Y':str(Y),'E':str(E),'H':str(H),
  'h62':str(h),'eta62':str(eta),'s62':str(S+h),'alpha62':str(AL+eta),'V62':str(V-G*eta),
  'root':str(root),'root_exp':str(V+G*AL),'min_positive_slack':str(margin),'states':states,'comparisons':comp,
  'strict':pos,'negative':len(neg),'ties':ties,'f0':list(map(str,f0)),'f1':list(map(str,f1)),
  't_margin0':str(f0[2]-f0[3]),'t_margin1':str(f1[2]-f1[3]),'next':str(nxt),'next_errors':errors[:5]}
if __name__=='__main__':print(json.dumps(check(),indent=2,ensure_ascii=False))
