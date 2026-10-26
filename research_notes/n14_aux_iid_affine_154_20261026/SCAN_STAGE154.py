"""Stage154 exact next dual scan following the Stage153 B Q/C tie."""
from fractions import Fraction as F
from pathlib import Path
import json
N=14;P=(F(1,8),F(1,24),F(5,6));K0,L0=F(5994,17),F(5960,17)
B,Z=(11,0,1),(12,2,2)
S=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
def child(s):
 n,a,b=s;return((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def lr(s):return F(2**(s[1]+s[2]),3**s[1])
H={};C={};A={};D={}
for s in reversed(S):
 v={'P':K0*lr(s),'Q':L0}
 c={'P':(F(),lr(s),F()),'Q':(F(),F(),F(1))}
 if s[0]<N:
  ch=child(s)
  v['C']=1+sum((P[i]*H[ch[i]] for i in range(3)),F())
  c['C']=tuple((F(1) if j==0 else F())+sum((P[i]*C[ch[i]][j] for i in range(3)),F()) for j in range(3))
 m=min(v.values());opts=[k for k in v if v[k]==m]
 if s in (B,Z):assert opts==['Q','C'];a='Q'
 else:assert len(opts)==1;a=opts[0]
 H[s]=m;C[s]=c[a];A[s]=a;D[s]=(v,c,a,m)
cb=D[B][1]['C'];dK=F(-1);dL=-(cb[1]*dK)/(cb[2]-1)
assert dL==-F(112,129)
zeros=[];negative=[]
for s in S:
 v,c,a,m=D[s]
 for other,val in v.items():
  if other==a:continue
  gap=val-m
  slope=(c[other][1]-c[a][1])*dK+(c[other][2]-c[a][2])*dL
  if gap==0:zeros.append((s,other,slope))
  elif gap>0 and slope<0:negative.append((gap/(-slope),s,other,gap,slope))
assert len(zeros)==2
assert next(t for s,a,t in zeros if s==B)==0
assert next(t for s,a,t in zeros if s==Z)==F(17,13932)
t,s,a,gap,slope=min(negative)
assert t==F(30922074,3386893) and s==(10,5,4) and a=='C'
K,L=K0+t*dK,L0+t*dL
assert K==F(68426856,199229) and L==F(68268104,199229)
print('PASS Stage154 dual ray first closure',t,s,'dual',K,L,'gap',gap,'slope',slope)
