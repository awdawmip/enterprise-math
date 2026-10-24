#!/usr/bin/env python3
"""Exact-rational author verifier for N=14 auxiliary iid 78th affine interval.
Inherited 77th stopping table, Source commit a4880ba6486d150077c3c8acbf99c7ded0fd6ebd.
No native CLAIM, formal Result or independent Driver review is asserted."""
from fractions import Fraction as F
from collections import defaultdict
from functools import lru_cache
import json
N=14
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
SP={(6,6,0),(7,6,0),(7,7,0),(8,6,0),(8,7,0),(8,8,0),(9,6,0),(9,7,0),(9,7,1),(9,8,0),(9,8,1),(10,5,0),(10,6,0),(10,7,0),(10,7,1),(10,8,1),(11,5,0),(11,7,1),(11,8,2),(11,6,1),(8,7,1),(11,4,0),(9,5,0),(10,8,2),(12,7,2),(8,5,0),(10,6,1),(7,5,0)}
SQ={(4,0,3),(4,0,4),(5,0,3),(5,0,4),(5,0,5),(5,1,4),(6,0,3),(6,0,4),(6,1,4),(6,1,5),(6,2,4),(7,0,3),(7,1,4),(7,2,4),(7,2,5),(8,0,3),(8,1,3),(8,2,4),(8,3,4),(8,3,5),(9,1,3),(9,3,4),(9,4,5),(10,0,2),(10,5,5),(10,2,3),(7,1,3),(10,4,4),(3,0,3),(7,3,4),(9,0,2),(6,1,3),(11,6,5)}
SP.add((5,5,0))  # endpoint A69 now a deterministic P decision
SP.add((9,4,0))  # 72nd endpoint now deterministic P
SP.add((10,4,0))
SP.add((6,5,0))  # proven 64th interval
SP.add((9,6,1))  # inherited 65th interval
SP.add((11,7,2)) # inherited 66th interval
SQ.add((9,2,3))  # already proven 63rd decision
SQ.add((5,1,3))  # inherited 67th stop
SQ.add((8,0,2))  # inherited 68th Q stop
SQ.add((9,4,4))  # 70th decision, deterministic Q
SQ.add((11,1,2))  # 71st decision, deterministic Q
SP.add((8,6,1))  # 73rd endpoint fixed P
SP.add((12,5,1)) # 74th endpoint fixed P
SQ.add((4,1,3))  # 75th endpoint fixed Q
SQ.add((8,2,3))  # 77th endpoint now fixed Q
SP.add((10,7,2)) # 76th endpoint now frozen to P
A=(7,6,1);B=(12,0,1)
AL=F(5171945831199762833,14900301753911083008)
V=F(24565111516140071249,1862537719238885376)
S=F(23988151419202381,41779200000000000)
K=F(42971052258,12859537);LP=F(72)+F(8,9)*K;LQ=K;G=LP+LQ

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
 """First potential action crossing as K decreases: exploratory successor only."""
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
    X=pa*ca[0];Y=qa*(1-ca[1])
    E=pb*(1-cb[0]);H=qb*cb[1]
    h=(X+Y)/(E+H);eta=-X+E*h
    assert eta==Y-H*h
    root,ties,pos,neg,comp,states,margin=dual()
    f0=forward(F(),S);f1=forward(F(1),S+h)
    nxt,errors=next_dual()
    assert (states,comp,pos,len(neg))==(680,1240,1238,0)
    assert set(ties)=={(A,'C','P'),(B,'C','Q')}
    assert (pa,qa,live)==(F(5,6291456),F(5,35831808),5)
    assert (pb,qb,liveb)==(F(48828125,725594112),F(48828125,362797056),12)
    assert ca==(F(923453,1146617856),F(5935061,5971968),F(56174843,47775744),F(2071663,1492992))
    assert (h,eta)==(F(526741223,696320000000000),F(64297685,413897270941974528))
    assert root==V+G*AL and f0[0]==f0[1]==AL and f0[2]==V and f0[2]>f0[3]
    assert 0<S<S+h<1 and eta>0
    assert f1[0]==f1[1]==AL+eta and f1[2]==V-G*eta and f1[2]>f1[3]
    assert not errors and nxt==(F(776081412,242449),(8,4,0),'C','P')
    for u in (F(),F(1,7),F(1,4),F(1,2),F(3,4),F(6,7),F(1)):
        ep,eq,tp,tq=forward(u,S+h*u)
        assert ep==eq==AL+eta*u and tp==V-G*eta*u and tp>tq
        assert tp+LP*ep+LQ*eq==root
    return {'status':'AUTHOR_EXACT_FINITE_MODEL_UNREVIEWED',
      'states':states,'nonchosen':comp,'strict_positive':pos,'negative':len(neg),
      'ties':ties,'minimum_positive_gap':str(margin),'root':str(root),
      'K78':str(K),'lambdaP':str(LP),'lambdaQ':str(LQ),'Gamma78':str(G),
      'A':A,'B':B,'A_firsthit_P':str(pa),'A_firsthit_Q':str(qa),'A_live_histories':live,
      'B_firsthit_P':str(pb),'B_firsthit_Q':str(qb),'B_live_histories':liveb,
      'A_suffix':list(map(str,ca)),'B_suffix':list(map(str,cb)),
      'X':str(X),'Y':str(Y),'E':str(E),'H':str(H),
      'h78':str(h),'eta78':str(eta),'s78':str(S+h),
      'alpha78':str(AL+eta),'V78':str(V-G*eta),
      'time_gap_start':str(f0[2]-f0[3]),'time_gap_end':str(f1[2]-f1[3]),
      'next_candidate':(str(nxt[0]),nxt[1],nxt[2],nxt[3])}
if __name__=='__main__':print(json.dumps(check(),indent=2))
