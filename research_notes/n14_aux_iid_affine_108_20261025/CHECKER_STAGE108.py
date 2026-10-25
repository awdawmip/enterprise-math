from fractions import Fraction as F
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6));N=14
K0=F(778896,767); L0=F(747576,767); A=(10,3,0);B=(12,0,1)
a107=F(91588670614917102449,263775056922062880768);v107=F(13541383133505475882195,1055100227688251523072)
u0=F(1115808042440821,1479206400000000)
def ch(z):
 n,a,b=z;return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
def r(z):return F(2**(z[1]+z[2]),3**z[1])
D={};O={};state=[]
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   z=n,a,b;cc={'P':K0*r(z),'Q':L0}
   if n<N:cc['C']=1+sum((P[i]*D[w] for i,w in enumerate(ch(z))),F(0))
   val=min(cc.values());D[z]=val;O[z]=tuple(k for k,v in cc.items() if v==val);state.append(z)
assert {z for z in O if len(O[z])>1}=={A,B}
policy={z:('C' if z==A else 'Q' if z==B else O[z][0]) for z in O}
coef={}; gaps=[]
def actioncoeff(z,act):
 if act=='P':return (F(0),r(z),F(0))
 if act=='Q':return (F(0),F(0),F(1))
 c=[coef[w] for w in ch(z)]
 return (1+sum(P[i]*c[i][0] for i in range(3)),sum(P[i]*c[i][1] for i in range(3)),sum(P[i]*c[i][2] for i in range(3)))
for z in state:
 v=actioncoeff(z,policy[z]);coef[z]=v
 for act in (('P','Q','C') if z[0]<14 else ('P','Q')):
  if act==policy[z]:continue
  alt=actioncoeff(z,act); g=tuple(alt[i]-v[i] for i in range(3))
  assert g[0]+g[1]*K0+g[2]*L0>=0
  gaps.append((z,act,g))
gA=next(g for z,act,g in gaps if z==A and act=='P')
assert gA[2]!=0
m=-gA[1]/gA[2];c=-gA[0]/gA[2]
assert c==F(-185064,635) and m==F(21376,17145) and c+m*K0==L0
lower=F(0);limit_states=[]
for z,act,g in gaps:
 d0=g[0]+g[2]*c;d1=g[1]+g[2]*m
 assert d0+d1*K0>=0
 if d1>0:
  k=-d0/d1
  if k>lower:lower=k;limit_states=[(z,act)]
  elif k==lower:limit_states.append((z,act))
K1=F(208946709,206588);L1=c+m*K1;Z=(11,5,4)
assert lower==K1 and (Z,'C') in limit_states
assert L1==F(50075544,51647) and K1+L1==F(409248885,206588)
D1={};opts1={};gmin=[]
for z in state:
 cs={'P':K1*r(z),'Q':L1}
 if z[0]<N:cs['C']=1+sum((P[i]*D1[q] for i,q in enumerate(ch(z))),F(0))
 lo=min(cs.values());D1[z]=lo;opts1[z]=tuple(k for k,v in cs.items() if v==lo)
 gmin.extend(v-lo for v in cs.values())
assert len(D1)==680 and sum(len(row) for row in opts1.values())>=680
assert {z for z in opts1 if len(opts1[z])>1}=={A,Z}
assert sum(x>0 for x in gmin)==1238 and min(x for x in gmin if x>0)==F(37821,1652704)
assert D1[0,0,0]==v107+(K1+L1)*a107
pol={z:('C' if z in (A,Z) else opts1[z][0]) for z in opts1}
count={(0,0,0):1};mp={(0,0,0):F(1)};mq={(0,0,0):F(1)}
for n in range(N):
 for a in range(n+1):
  for b in range(n-a+1):
   z=n,a,b
   if z not in count or z in (A,Z) or pol[z]!='C':continue
   for i,w in enumerate(ch(z)):
    count[w]=count.get(w,0)+count[z];mp[w]=mp.get(w,F(0))+mp[z]*P[i];mq[w]=mq.get(w,F(0))+mq[z]*Q[i]
assert (count[A],mp[A],mq[A])==(120,F(390625,5971968),F(390625,20155392))
assert (count[Z],mp[Z],mq[Z])==(2258,F(28225,195689447424),F(28225,92876046336))
S={}
for z in state:
 act=pol[z]
 if act=='P':S[z]=(F(0),F(1),F(0),F(0),1)
 elif act=='Q':S[z]=(F(1),F(0),F(0),F(0),1)
 else:
  cc=[S[w] for w in ch(z)]
  S[z]=(sum((P[i]*v[0] for i,v in enumerate(cc)),F(0)),sum((Q[i]*v[1] for i,v in enumerate(cc)),F(0)),1+sum((P[i]*v[2] for i,v in enumerate(cc)),F(0)),1+sum((Q[i]*v[3] for i,v in enumerate(cc)),F(0)),sum(v[4] for v in cc))
assert S[A]==(F(635,165888),F(10201,10368),F(7711,6912),F(1069,864),21)
assert S[Z]==(F(1493,1536),F(7,576),F(239,192),F(167,144),9)
x=-mp[A]*S[A][0];y=mq[A]*(1-S[A][1]);zP=mp[Z]*(1-S[Z][0]);zQ=-mq[Z]*S[Z][1]
d=(zP-zQ)/(y-x);eta=x*d+zP
assert d==F(67761451,4930688000000)
assert eta==y*d+zQ==F(1457736575,2442361638167248896)
assert 0<u0<u0+d<1

def outcomes(u,w):
 memo={}
 for z in state:
  acts={'P':u,'C':1-u} if z==A else {'Q':w,'C':1-w} if z==Z else {pol[z]:F(1)}
  row=[F(0)]*4
  for act,wt in acts.items():
   if act=='P':rv=(F(0),F(1),F(0),F(0))
   elif act=='Q':rv=(F(1),F(0),F(0),F(0))
   else:
    cc=[memo[t] for t in ch(z)]
    rv=(sum((P[i]*cc[i][0] for i in range(3)),F(0)),sum((Q[i]*cc[i][1] for i in range(3)),F(0)),1+sum((P[i]*cc[i][2] for i in range(3)),F(0)),1+sum((Q[i]*cc[i][3] for i in range(3)),F(0)))
   for j in range(4):row[j]+=wt*rv[j]
  memo[z]=tuple(row)
 return memo[(0,0,0)]
for w in (F(0),F(1,2),F(1)):
 got=outcomes(u0+d*w,w)
 assert got[0]==got[1]==a107+eta*w
 assert got[2]==v107-(K1+L1)*eta*w and got[2]>got[3]
assert a107+eta==F(13084095824621807507,37682150988866125824)
assert v107-(K1+L1)*eta==F(1934483126570299962385,150728603955464503296)
# Dual-only next candidate after the Q action at Z is selected, preserving the A tie.
post_policy=pol.copy();post_policy[Z]='Q';cc={};cg={};next_roots=[]
for z in state:
 op=post_policy[z]
 if op=='P':v0,v1=F(0),r(z)
 elif op=='Q':v0,v1=c,m
 else:
  v0=1+sum((P[i]*cc[t] for i,t in enumerate(ch(z))),F(0))
  v1=sum((P[i]*cg[t] for i,t in enumerate(ch(z))),F(0))
 cc[z],cg[z]=v0,v1
 for alt in (('P','Q','C') if z[0]<N else ('P','Q')):
  if alt==op:continue
  if alt=='P':s0,s1=F(0),r(z)
  elif alt=='Q':s0,s1=c,m
  else:
   s0=1+sum((P[i]*cc[t] for i,t in enumerate(ch(z))),F(0))
   s1=sum((P[i]*cg[t] for i,t in enumerate(ch(z))),F(0))
  d0,d1=s0-v0,s1-v1
  if d1>0 and d0+d1*K1>0 and -d0/d1<K1:next_roots.append((-d0/d1,z,alt))
assert max(next_roots)==(F(491857029,506348),(10,3,3),'Q')
print('PASS_STAGE108_EXACT_RATIONAL', a107+eta, v107-(K1+L1)*eta)
