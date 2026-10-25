"""Exact Stage124 one-sided affine Bellman candidate, from Stage123 saturated J/Q."""
from fractions import Fraction as Q
N=14;K=Q(15175912302,20129609);L=Q(14232343848,20129609)
D_K=-Q(1);D_L=-Q(608000,474363);P=(Q(1,8),Q(1,24),Q(5,6))
A=(9,3,0);J=(10,5,4)
def nxt(s):
 n,a,b=s;return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
H={};HD={};cross=[];tie_slopes={}
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);ratio=Q(2**(a+b),3**a)
   vals=[K*ratio,L];dv=[D_K*ratio,D_L]
   if n<N:
    v=nxt(s);vals.append(Q(1)+sum(P[i]*H[v[i]] for i in range(3)))
    dv.append(sum(P[i]*HD[v[i]] for i in range(3)))
   mn=min(vals);opts=[i for i,x in enumerate(vals) if x==mn]
   if s==A:idx=0
   elif s==J:idx=1
   elif len(opts)==1:idx=opts[0]
   else:raise RuntimeError((s,opts))
   assert idx in opts
   H[s]=mn;HD[s]=dv[idx]
   for j in range(len(vals)):
    if j==idx:continue
    gap=vals[j]-mn;dgap=dv[j]-dv[idx]
    if gap==0:tie_slopes[(s,j)]=dgap
    elif dgap<0:cross.append((gap/(-dgap),s,idx,j))
assert len(H)==680 and tie_slopes=={(A,2):Q(0),(J,2):Q(20129609,1844323344)}
assert len(cross)==840
cross.sort()
t,s,old,new=cross[0]
assert (t,s,old,new)==(Q(100730985421815,33381655270624),(14,7,4),0,1)
K1=K+D_K*t;L1=L+D_L*t
assert K1==Q(1245231873,1658336) and L1==Q(36440256,51823)
h={};ties={};pos=[]
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);v=[K1*Q(2**(a+b),3**a),L1]
   if n<N:v.append(Q(1)+sum(P[i]*h[nxt(s)[i]] for i in range(3)))
   m=min(v);h[s]=m;opt=[i for i,x in enumerate(v) if x==m]
   if len(opt)>1:ties[s]=opt
   pos.extend(x-m for x in v if x>m)
assert ties=={A:[0,2],(14,7,4):[0,1]}
assert len(pos)==1238 and min(pos)==Q(294166217221,39614118100992)
assert h[(0,0,0)]==Q(5878829162353591081475135,11355563791072559628288)
print('PASS Stage124 exact dual-only candidate',s,'K',K1,'L',L1)
