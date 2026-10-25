"""Exact one-sided affine Bellman gap sweep from Stage122 saturated F/Q edge."""
from fractions import Fraction as Q
N=14;K=Q(27085186670001462,35130967563833);L=Q(25607353643447976,35130967563833)
D_K=-Q(1);D_L=-Q(608000,474363)
P=(Q(1,8),Q(1,24),Q(5,6))
A=(9,3,0);FSTATE=(3,0,2)
def nxt(s):
 n,a,b=s
 return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
H={}; HD={}; chosen={}; crossings=[]; tied_slopes={}
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);R=Q(2**(a+b),3**a)
   vals=[K*R,L];dvals=[D_K*R,D_L]
   if n<N:
    ch=nxt(s);vals.append(Q(1)+sum(P[i]*H[ch[i]] for i in range(3)))
    dvals.append(sum(P[i]*HD[ch[i]] for i in range(3)))
   mn=min(vals);opts=[j for j in range(len(vals)) if vals[j]==mn]
   if s==A: idx=0
   elif s==FSTATE:idx=1
   elif len(opts)==1:idx=opts[0]
   else: raise RuntimeError(f'unexpected tie {s}: {opts}')
   assert idx in opts
   H[s]=mn;HD[s]=dvals[idx];chosen[s]=idx
   for j in range(len(vals)):
    if j==idx:continue
    gap=vals[j]-mn; dgap=dvals[j]-dvals[idx]
    if gap==0: tied_slopes[(s,j)]=dgap
    if dgap<0 and gap>0:crossings.append((gap/(-dgap),s,idx,j,gap,dgap))
print('A/F tie slopes',tied_slopes)
print('one-sided valid?',all(v>=0 for v in tied_slopes.values()))
if crossings:
 crossings.sort(key=lambda z:z[0]); print('candidate count',len(crossings),'earliest',crossings[0], 'equals', [x for x in crossings if x[0]==crossings[0][0]])
 t=crossings[0][0];print('K_next=',K+D_K*t,'L_next=',L+D_L*t)
 K1=K+D_K*t;L1=L+D_L*t;h={}; ties={};gaps=[]
 for n in range(N,-1,-1):
  for a in range(n+1):
   for b in range(n-a+1):
    s=(n,a,b);v=[K1*Q(2**(a+b),3**a),L1]
    if n<N:v.append(Q(1)+sum(P[i]*h[nxt(s)[i]] for i in range(3)))
    m=min(v);h[s]=m
    ids=[j for j in range(len(v)) if v[j]==m]
    if len(ids)>1:ties[s]=ids
    gaps.extend(q-m for q in v if q>m)
 print('next DP ties',ties,'numpos',len(gaps),'min',min(gaps),'root',h[(0,0,0)])
