"""N14 Stage122 exact Fraction proof checker; external iid model, author code."""
from fractions import Fraction as R
from functools import lru_cache
N=14;P=(R(1,8),R(1,24),R(5,6));Q=(R(1,12),R(1,12),R(5,6))
K=R(27085186670001462,35130967563833);L=R(25607353643447976,35130967563833)
A=(9,3,0);F=(3,0,2);O=(0,0,0)
a121=R(2573764738946831699425,7411551152237344456704)
v121=R(378361775997993165503285,29646204608949377826816)
def nxt(s):
 n,a,b=s;return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
h={};pol={};gaps=[];ties={}
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);v=[K*R(2**(a+b),3**a),L]
   if n<N:v.append(1+sum(P[j]*h[t] for j,t in enumerate(nxt(s))))
   m=min(v);h[s]=m;opt=[j for j,x in enumerate(v) if x==m]
   if len(opt)>1:ties[s]=opt
   pol[s]=opt[0];gaps.extend(x-m for x in v if x>m)
assert len(h)==680 and len(gaps)==1238 and ties=={A:[0,2],F:[1,2]}
assert min(gaps)==R(968911136726508551639,90634038091307409604608)
assert h[O]==v121+(K+L)*a121
@lru_cache(None)
def moments(y,r):
 @lru_cache(None)
 def calc(s):
  if s in (A,F):
   prob,act=(y,0) if s==A else (r,1)
   term=(R(0),R(1),R(0),R(0)) if act==0 else (R(1),R(0),R(0),R(0))
   cont=follow(s)
   return tuple(prob*x+(1-prob)*z for x,z in zip(term,cont))
  act=pol[s]
  if act==0:return R(0),R(1),R(0),R(0)
  if act==1:return R(1),R(0),R(0),R(0)
  return follow(s)
 def follow(s):
  cs=[calc(t) for t in nxt(s)]
  return (sum(P[j]*cs[j][0] for j in range(3)),sum(Q[j]*cs[j][1] for j in range(3)),1+sum(P[j]*cs[j][2] for j in range(3)),1+sum(Q[j]*cs[j][3] for j in range(3)))
 return calc(O)
m0=moments(R(0),R(0));ma=moments(R(1),R(0));mf=moments(R(0),R(1));m11=moments(R(1),R(1))
da=tuple(ma[i]-m0[i] for i in range(4));df=tuple(mf[i]-m0[i] for i in range(4))
assert all(m11[i]==m0[i]+da[i]+df[i] for i in range(4))
diff=lambda m:m[0]-m[1]
y0=-diff(m0)/diff(da);dy=-diff(df)/diff(da)
assert y0==R(665696150804933,2909391744000000)
assert dy==R(5267621485201,38791889920000)
def mix(r):
 y=y0+dy*r;return tuple(m0[i]+da[i]*y+df[i]*r for i in range(4))
mstart=mix(R(0));mend=mix(R(1));eta=mend[0]-mstart[0]
assert 0<y0<y0+dy<1
assert mstart[0]==mstart[1]==a121 and mstart[2]==v121
assert mend[0]==mend[1]==R(80432667641168459255,231610973507417014272)
assert mend[2]==R(377878058477915699662445,29646204608949377826816)
assert eta==R(2986132242925805,274501894527309053952)
for m in (mstart,mend):assert m[2]>m[3] and m[2]+(K+L)*m[0]==h[O]
# Literal integer-weighted ordered-word walk, logically independent of moment recursion.
PN=(3,1,20);QN=(1,1,10);pwrs=[24**i for i in range(15)];qwrs=[12**i for i in range(15)]
visits=[]
for ay in (0,1):
 for fr in (0,1):
  out=[0,0,0,0];hits={A:[0,0,0],F:[0,0,0]};count=[0]
  def dfs(s,pw,qw):
   count[0]+=1;n,a,b=s
   if s in hits:
    hhit=hits[s];hhit[0]+=1;hhit[1]+=pw*pwrs[N-n];hhit[2]+=qw*qwrs[N-n]
   action=(0 if ay else 2) if s==A else (1 if fr else 2) if s==F else pol[s]
   if action!=2:
    p=pw*pwrs[N-n];q=qw*qwrs[N-n]
    if action==1:out[0]+=p
    else:out[1]+=q
    out[2]+=n*p;out[3]+=n*q;return
   for j,t in enumerate(nxt(s)):dfs(t,pw*PN[j],qw*QN[j])
  dfs(O,1,1)
  actual=(R(out[0],pwrs[N]),R(out[1],qwrs[N]),R(out[2],pwrs[N]),R(out[3],qwrs[N]))
  assert actual==moments(R(ay),R(fr))
  assert hits[A][0]==84 and R(hits[A][1],pwrs[N])==R(109375,1990656) and R(hits[A][2],qwrs[N])==R(109375,6718464)
  assert hits[F][0]==3 and R(hits[F][1],pwrs[N])==R(5,1152) and R(hits[F][2],qwrs[N])==R(5,288)
  visits.append(count[0])
assert visits==[840811,823333,835771,818293]
print('PASS Stage122: 680 rational states, 1238 positive gaps, full real interval, four literal DFS corners',visits)
