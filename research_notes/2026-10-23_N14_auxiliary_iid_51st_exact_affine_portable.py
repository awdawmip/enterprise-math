from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
import itertools, json
N=14
# Finite *auxiliary* iid problem, not native X6/BRC/Heartbeat dynamics.
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
A50=(9,5,0); A=(10,4,4);B=(12,0,1)
SP={(6,6,0),(7,6,0),(7,7,0),(8,6,0),(8,7,0),(8,8,0),
(9,6,0),(9,7,0),(9,7,1),(9,8,0),(9,8,1),
(10,5,0),(10,6,0),(10,7,0),(10,7,1),(10,8,1),
(11,5,0),(11,7,1),(11,8,2),(11,6,1),(8,7,1),(11,4,0),A50}
SQ={(4,0,3),(4,0,4),(5,0,3),(5,0,4),(5,0,5),(5,1,4),
(6,0,3),(6,0,4),(6,1,4),(6,1,5),(6,2,4),
(7,0,3),(7,1,4),(7,2,4),(7,2,5),
(8,0,3),(8,1,3),(8,2,4),(8,3,4),(8,3,5),
(9,1,3),(9,3,4),(9,4,5),(10,0,2),(10,5,5),(10,2,3),(7,1,3)}
K=F(3779136,217); LP=F(72)+F(8,9)*K;LQ=K;G=LP+LQ
AL=F(5171825736073354397,14900301753911083008)
V=F(12376506639448300069,931268859619442688)
S=F(8831125038893923,13926400000000000)
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
def reached(target):
 cur={(0,0):(F(1),F(1),1)}
 for n in range(target[0]):
  nxt=defaultdict(lambda:(F(),F(),0))
  for (a,b),(p,q,v) in cur.items():
   if act((n,a,b))!='C':continue
   for i in range(3):
    k=(a+(i==0),b+(i==1));x,y,w=nxt[k]
    nxt[k]=(x+p*P[i],y+q*Q[i],w+v)
  cur=dict(nxt)
 return cur.get(target[1:],(F(),F(),0))
@lru_cache(None)
def suffix(st):
 z=act(st)
 if z=='P':return F(),F(1),F(),F()
 if z=='Q':return F(1),F(),F(),F()
 xs=[suffix(child(st,i)) for i in range(3)]
 return (sum((P[i]*xs[i][0] for i in range(3)),F()),
         sum((Q[i]*xs[i][1] for i in range(3)),F()),
         F(1)+sum((P[i]*xs[i][2] for i in range(3)),F()),
         F(1)+sum((Q[i]*xs[i][3] for i in range(3)),F()))
def dual():
 d={};ties=[];checked=0;negative=[]
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    st=(n,a,b)
    opts={'P':LQ*F(2**(a+b),3**a),'Q':LP}
    if n<N:opts['C']=F(1)+sum((P[i]*d[child(st,i)] for i in range(3)),F())
    z=act(st);chosen=opts[z]
    for mode,value in opts.items():
     if mode==z:continue
     checked+=1
     if value<chosen:negative.append((st,z,mode,value-chosen))
     if value==chosen:ties.append((st,z,mode))
    d[st]=chosen
 return d[(0,0,0)],ties,checked,negative

def forward(u,s):
 cur={(0,0):(F(1),F(1))};ep=eq=tp=tq=F()
 for n in range(N+1):
  nxt=defaultdict(lambda:(F(),F()))
  for (a,b),(p,q) in cur.items():
   st=(n,a,b)
   if st==A: ep+=p*u;p*=1-u;q*=1-u
   elif st==B: ep+=p*s;p*=1-s;q*=1-s
   elif act(st)=='P':eq+=q;continue
   elif act(st)=='Q':ep+=p;continue
   assert n<N,st
   tp+=p;tq+=q
   for i in range(3):
    k=(a+(i==0),b+(i==1));x,y=nxt[k]
    nxt[k]=(x+p*P[i],y+q*Q[i])
  cur=dict(nxt)
 assert not cur
 return ep,eq,tp,tq

def next_dual_candidate():
 vals={};points=[]
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    st=(n,a,b)
    z='Q' if st==A else act(st)
    opts={'P':(F(),F(2**(a+b),3**a)),'Q':(F(72),F(8,9))}
    if n<N:
     opts['C']=(F(1)+sum((P[i]*vals[child(st,i)][0] for i in range(3)),F()),
                sum((P[i]*vals[child(st,i)][1] for i in range(3)),F()))
    vals[st]=opts[z]
    for move,v in opts.items():
     if move==z or st in (A,B):continue
     c0=v[0]-opts[z][0];c1=v[1]-opts[z][1];slack=c0+c1*K
     assert slack>0,(st,z,move)
     if c1>0:
      k=-c0/c1
      if k<K:points.append((k,st,z,move))
 return max(points)

def check():
 pa,qa,live=reached(A);pb,qb,liveb=reached(B)
 ca=suffix(A);cb=suffix(B)
 print('A reach',live,pa,qa, 'B',liveb,pb,qb)
 assert (live,pa,qa)==(1565,F(39125,48922361856),F(39125,15479341056))
 print('A suffix',ca,'B suffix',cb)
 X=pa*(1-ca[0]);Y=qa*ca[1];E=pb*(1-cb[0]);H=qb*cb[1]
 h=(X+Y)/(E+H)
 eta=X-E*h
 print('X,Y,E,H',X,Y,E,H,'h',h,'eta',eta,'s_end',S-h)
 assert h==F(3335641,20889600000000) and eta==F(8490125,310422953206480896) and S>=h
 root,ties,checked,negative=dual()
 print('root',root,'ties',ties,'checked',checked,'negative',negative[:10]);assert not negative
 assert set(ties)=={(A,'C','Q'),(B,'C','Q')} and checked==1240
 print('baseline=',forward(F(0),S));print('corner_end=',forward(F(1),S-h))
 print('root identity',root,V+G*AL,root==V+G*AL)
 for u in (F(),F(1,4),F(1,2),F(3,4),F(1)):
  s=S-h*u;ep,eq,tp,tq=forward(u,s)
  print('u',u,'s',s,'ep',ep,'eq',eq,'tp',tp,'tq',tq,'margin',tp-tq)
  assert F()<=s<=F(1)
  assert ep==eq==AL+eta*u,(u,ep,eq,AL+eta*u)
  assert tp==V-G*eta*u and tp>=tq,(u,tp,tq,V-G*eta*u)
  assert tp+LP*ep+LQ*eq==root
 endpoint=(AL+eta,V-G*eta)
 print('endpoint=',endpoint,'P-Q=',forward(F(1),S-h)[2]-forward(F(1),S-h)[3])
 assert endpoint==(F(5171825736480880397,14900301753911083008), F(12376505799748489069,931268859619442688))
 nxt=next_dual_candidate();print('next_candidate',nxt)
 assert nxt==(F(280418092213968,16640988557),(3,0,3),'C','Q')
 return {'A':A,'A_live':live,'pA':pa,'qA':qa,'B_live':liveb,'pB':pb,'qB':qb,'conditional_A':ca,'conditional_B':cb,'X':X,'Y':Y,'E':E,'H':H,'h':h,'eta':eta,'K':K,'lambdaP':LP,'lambdaQ':LQ,'gamma':G,'root':root,'s51':S-h,'alpha50':AL,'V50':V,'alpha51':endpoint[0],'V51':endpoint[1],'PminusQ':forward(F(1),S-h)[2]-forward(F(1),S-h)[3],'nextK':nxt[0],'nextA':nxt[1],'next_actions':nxt[2:]}
if __name__=='__main__':
 r=check()
 import pprint;pprint.pp(r)