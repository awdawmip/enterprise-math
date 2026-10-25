"""Stage129 portable exact Fraction proof checker, author-side reconstruction."""
from fractions import Fraction as F
from collections import defaultdict
p=(F(1,8),F(1,24),F(5,6));q=(F(1,12),F(1,12),F(5,6))
K,L=F(14874456845932398,22082607358633),F(13896162810492616,22082607358633);B,T=(11,0,1),(2,0,2);N=14
def child(s):
 n,a,b=s
 return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
H={};best={};gaps=[]
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b)
   co={'P':K*F(2**(a+b),3**a),'Q':L}
   if n<N:co['C']=1+sum(p[i]*H[t] for i,t in enumerate(child(s)))
   h=min(co.values());H[s]=h;best[s]=sorted(x for x in co if co[x]==h)
   gaps.extend(x-h for x in co.values() if x>h)
assert len(H)==680 and len(gaps)==1238 and min(gaps)==F(2569217935604737,48294662293330371)
assert {s:x for s,x in best.items() if len(x)>1}=={B:['C','Q'],T:['C','Q']}
assert H[(0,0,0)]==F(2605243537319692868583967737169,5600447868272894163950764032)
def action(s,w,u):
 return ('Q' if w else 'C') if s==B else ('Q' if u else 'C') if s==T else best[s][0]
def obs(w,u):
 z={}
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    s=(n,a,b);act=action(s,w,u)
    if act=='P':z[s]=(F(0),F(1),F(0),F(0))
    elif act=='Q':z[s]=(F(1),F(0),F(0),F(0))
    else:
     v=[z[t] for t in child(s)]
     z[s]=(sum(p[i]*v[i][0] for i in range(3)),
           sum(q[i]*v[i][1] for i in range(3)),
           1+sum(p[i]*v[i][2] for i in range(3)),
           1+sum(q[i]*v[i][3] for i in range(3)))
 return z[(0,0,0)]
M=obs(0,0);M10=obs(1,0);M01=obs(0,1);M11=obs(1,1)
dB=tuple(M10[i]-M[i] for i in range(4))
dT=tuple(M01[i]-M[i] for i in range(4))
assert M11==tuple(M[i]+dB[i]+dT[i] for i in range(4))
w0=(M[1]-M[0])/(dB[0]-dB[1])
slope=-(dT[0]-dT[1])/(dB[0]-dB[1])
assert (w0,slope)==(F(12145777109752777,40719360000000000),-F(256958333767239,27146240000000000))
def m(u):
 w=w0+slope*u
 assert 0<=w<=1 and 0<=u<=1
 return tuple(M[i]+w*dB[i]+u*dT[i] for i in range(4))
m0,m1=m(F(0)),m(F(1))
a0=F(18348272658534259499,52808422392537808896)
v0=F(330193261759082895695,26404211196268904448)
a1=F(36696744060534746695,105616844785075617792)
v1=F(660257055729711878827,52808422392537808896)
assert m0[0]==m0[1]==a0 and m0[2]==v0 and m0[2]>m0[3]
assert m1[0]==m1[1]==a1 and m1[2]==v1 and m1[2]>m1[3]
assert a1-a0==F(22082607358633,11735204976119513088)
assert H[(0,0,0)]==v0+(K+L)*a0==v1+(K+L)*a1
first={s:[0,F(0),F(0)] for s in (B,T)}
cur={(0,0,0):(1,F(1),F(1))}
for n in range(N+1):
 nxt=defaultdict(lambda:[0,F(0),F(0)])
 for s,(c,mp,mq) in cur.items():
  if s in first:
   v=first[s];v[0]+=c;v[1]+=mp;v[2]+=mq
  if n<N and action(s,0,0)=='C':
   for i,t in enumerate(child(s)):
    v=nxt[t];v[0]+=c;v[1]+=mp*p[i];v[2]+=mq*q[i]
 cur=nxt
assert first[B]==[11,F(107421875,1451188224),F(107421875,725594112)]
assert first[T]==[1,F(1,576),F(1,144)]
print('PASS stage128: 680 states, 1238 positive gaps, exact full-real interval and endpoint',a1,v1)
