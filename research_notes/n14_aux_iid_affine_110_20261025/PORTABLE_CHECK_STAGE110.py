"""Stage110 exact rational author-side verification; external ternary iid N=14."""
from fractions import Fraction as F
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
S=[(n,a,b) for n in range(14,-1,-1) for a in range(n+1) for b in range(n-a+1)]
A=(10,3,0);E=(13,6,4)
K0=F(491857029,506348);K1=F(6497577,6734)
def L(k):return -F(185064,635)+F(21376,17145)*k
def ch(z):n,a,b=z;return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def ratio(z):return F(2**(z[1]+z[2]),3**z[1])
def bell(k):
 v={};opts={};gaps=[]
 for z in S:
  cost={'P':k*ratio(z),'Q':L(k)}
  if z[0]<14:cost['C']=1+sum((P[i]*v[t] for i,t in enumerate(ch(z))),F(0))
  best=min(cost.values());v[z]=best;opts[z]=tuple(t for t in cost if cost[t]==best)
  gaps.extend(c-best for c in cost.values())
 return v,opts,gaps
v1,opts,gaps=bell(K1)
assert len(S)==680 and {z for z in opts if len(opts[z])>1}=={A,E}
assert sum(t>0 for t in gaps)==1238 and not any(t<0 for t in gaps)
assert min(t for t in gaps if t>0)==F(71796655,11490066432)
pol={z:('C' if z in (A,E) else opts[z][0]) for z in S}
for k in (K0,K1):
 v={}
 for z in S:
  cost={'P':k*ratio(z),'Q':L(k)}
  if z[0]<14:cost['C']=1+sum((P[i]*v[t] for i,t in enumerate(ch(z))),F(0))
  assert all(c>=cost[pol[z]] for c in cost.values())
  v[z]=cost[pol[z]]
 assert v[0,0,0]==bell(k)[0][0,0,0]
alpha0=F(13084102500820187507,37682150988866125824)
value0=F(1934432626777903782385,150728603955464503296)
assert v1[0,0,0]==value0+(K1+L(K1))*alpha0
hits={(0,0,0):1};pm={(0,0,0):F(1)};qm={(0,0,0):F(1)}
for z in reversed(S):
 if z not in hits or pol[z]!='C':continue
 for i,t in enumerate(ch(z)):
  hits[t]=hits.get(t,0)+hits[z]
  pm[t]=pm.get(t,F(0))+pm[z]*P[i]
  qm[t]=qm.get(t,F(0))+qm[z]*Q[i]
assert (hits[E],pm[E],qm[E])==(16254,F(37625,347892350976),F(37625,247669456896))
sub={}
for z in S:
 if pol[z]=='P':sub[z]=(F(0),F(1),F(0),F(0),1)
 elif pol[z]=='Q':sub[z]=(F(1),F(0),F(0),F(0),1)
 else:
  cs=[sub[t] for t in ch(z)]
  sub[z]=(sum((P[i]*cs[i][0] for i in range(3)),F(0)),
          sum((Q[i]*cs[i][1] for i in range(3)),F(0)),
          1+sum((P[i]*cs[i][2] for i in range(3)),F(0)),
          1+sum((Q[i]*cs[i][3] for i in range(3)),F(0)),sum(c[4] for c in cs))
assert sub[E]==(F(7,8),F(1,12),F(1),F(1),3)
x=-pm[A]*sub[A][0];y=qm[A]*(1-sub[A][1])
zp=pm[E]*(1-sub[E][0]);zq=-qm[E]*sub[E][1]
du=(zp-zq)/(y-x);eta=x*du+zp
assert du==F(327789,7043840000) and eta==F(18097625,9691911262568448)
u0=F(159859205042303,211315200000000)
assert u0+du<1
def moments(u,w):
 d={}
 for z in S:
  acts={'P':u,'C':1-u} if z==A else {'Q':w,'C':1-w} if z==E else {pol[z]:F(1)}
  v=[F(0)]*4
  for act,wt in acts.items():
   if act=='P':m=(F(0),F(1),F(0),F(0))
   elif act=='Q':m=(F(1),F(0),F(0),F(0))
   else:
    cs=[d[t] for t in ch(z)]
    m=(sum((P[i]*cs[i][0] for i in range(3)),F(0)),
       sum((Q[i]*cs[i][1] for i in range(3)),F(0)),
       1+sum((P[i]*cs[i][2] for i in range(3)),F(0)),
       1+sum((Q[i]*cs[i][3] for i in range(3)),F(0)))
   for i in range(4):v[i]+=wt*m[i]
  d[z]=tuple(v)
 return d[0,0,0]
for w in (F(0),F(1,2),F(1)):
 ep,eq,tp,tq=moments(u0+du*w,w)
 assert ep==eq==alpha0+eta*w
 assert tp==value0-(K1+L(K1))*eta*w and tp>tq
 print('EXACT',w,'alpha=',ep,'tP=',tp,'tQ=',tq)
assert alpha0+eta==F(13084102571183753507,37682150988866125824)
assert value0-(K1+L(K1))*eta==F(1934432098641265410385,150728603955464503296)
print('PASS_STAGE110_PORTABLE_EXACT')
