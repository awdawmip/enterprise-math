"""Exact Stage128 first-event scan after Stage127 C-stop saturation; candidate only."""
from fractions import Fraction as F
import json
N=14;P=(F(1,8),F(1,24),F(5,6))
K0=F(8246448,11561);L0=F(7673768,11561)
B=(11,0,1);C=(11,6,2)
kids=lambda s:((s[0]+1,s[1]+1,s[2]),(s[0]+1,s[1],s[2]+1),(s[0]+1,s[1],s[2]))
V={};act={};coeff={}
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);r=F(2**(a+b),3**a)
   cost={'P':K0*r,'Q':L0}
   if n<N:cost['C']=1+sum(P[j]*V[t] for j,t in enumerate(kids(s)))
   opts=[k for k in ('P','Q','C') if k in cost and cost[k]==min(cost.values())]
   chosen='Q' if s==B else 'P' if s==C else opts[0]
   assert chosen in opts
   act[s]=chosen;V[s]=cost[chosen]
   fc={'P':(F(0),r,F(0)),'Q':(F(0),F(0),F(1))}
   if n<N:fc['C']=tuple(F(i==0)+sum(P[j]*coeff[t][i] for j,t in enumerate(kids(s))) for i in range(3))
   coeff[s]=fc[chosen]
cB=tuple(F(i==0)+sum(P[j]*coeff[t][i] for j,t in enumerate(kids(B))) for i in range(3))
m=cB[1]/(1-cB[2]);assert m==F(112,129)
events=[];ties=[];positive=0
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);r=F(2**(a+b),3**a)
   cost={'P':K0*r,'Q':L0}
   fc={'P':(F(0),r,F(0)),'Q':(F(0),F(0),F(1))}
   if n<N:
    cost['C']=1+sum(P[j]*V[t] for j,t in enumerate(kids(s)))
    fc['C']=tuple(F(i==0)+sum(P[j]*coeff[t][i] for j,t in enumerate(kids(s))) for i in range(3))
   chosen=act[s];v=cost[chosen];f=fc[chosen];dv=-f[1]-m*f[2]
   for alt,x in cost.items():
    if alt==chosen:continue
    gap=x-v;fg=fc[alt];dg=-fg[1]-m*fg[2]-dv
    assert gap>=0
    if gap==0:ties.append((s,chosen,alt,dg));assert dg>=0
    else:
     positive+=1
     if dg<0:events.append((gap/-dg,s,chosen,alt,gap,dg))
assert positive==1238
assert ties==[(B,'Q','C',F(0)),(C,'P','C',F(11561,6770952))]
t,s,old,alt,gap,dg=min(events)
assert (t,s,old,alt,gap,dg)==(F(54954,11561),(12,2,0),'C','P',F(71,9459),-F(11,6966))
K1=K0-t;L1=L0-m*t
assert K1==F(7794,11) and L1==F(7256,11)
W={};tm={};gaps=[]
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);r=F(2**(a+b),3**a)
   cost={'P':K1*r,'Q':L1}
   if n<N:cost['C']=1+sum(P[j]*W[z] for j,z in enumerate(kids(s)))
   v=min(cost.values());W[s]=v
   opts=[k for k in ('P','Q','C') if k in cost and cost[k]==v]
   if len(opts)>1:tm[str(s)]=opts
   gaps.extend(x-v for x in cost.values() if x>v)
assert len(W)==680 and len(gaps)==1238 and min(gaps)==F(71,8748)
assert tm=={'(11, 0, 1)':['Q','C'],'(12, 2, 0)':['P','C']}
print(json.dumps({'status':'DUAL_CANDIDATE_ONLY','t':str(t),'K128':str(K1),'L128':str(L1),
'root':str(W[(0,0,0)]),'ties':tm,'positive_gaps':len(gaps),'min_positive_gap':str(min(gaps))},indent=2))
