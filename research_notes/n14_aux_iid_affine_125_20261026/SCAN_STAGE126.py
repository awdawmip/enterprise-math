"""Stage126 first-event scan: exact dual candidate only, not primal theorem."""
from fractions import Fraction as F
import json
N=14;p=(F(1,8),F(1,24),F(5,6))
K0=F(3579845625,4855672);L0=F(416181048,606959);m=F(608000,474363)
A=(9,3,0);U=(12,7,5)
kids=lambda s:((s[0]+1,s[1]+1,s[2]),(s[0]+1,s[1],s[2]+1),(s[0]+1,s[1],s[2]))
V={};D={};events=[];tie_slopes=[]
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);r=F(2**(a+b),3**a)
   costs={'P':(K0*r,-r),'Q':(L0,-m)}
   if n<N:costs['C']=(1+sum(p[j]*V[x] for j,x in enumerate(kids(s))),sum(p[j]*D[x] for j,x in enumerate(kids(s))))
   best=min(v for v,d in costs.values())
   opt=[x for x in ('P','Q','C') if x in costs and costs[x][0]==best]
   chosen='Q' if s==U else 'P' if s==A else opt[0]
   assert chosen in opt
   V[s],D[s]=costs[chosen]
   for alt,(v,d) in costs.items():
    if alt==chosen:continue
    gap=v-best;dg=d-D[s]
    if gap==0:tie_slopes.append((s,chosen,alt,dg))
    elif dg<0:events.append((gap/(-dg),s,chosen,alt,gap,dg))
assert len(V)==680
assert tie_slopes==[(U,'Q','C',F(2427836,345810627)),(A,'P','C',F(0))]
t,s,old,alt,_,_=min(events)
assert (s,old,alt)==((11,0,1),'C','Q')
assert t==F(6957293798889,2559682061816)
K1=K0-t;L1=L0-m*t
assert K1==F(387210888,527153) and L1==F(359623016,527153)
W={};ties={};gaps=[]
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);cost={'P':K1*F(2**(a+b),3**a),'Q':L1}
   if n<N:cost['C']=1+sum(p[j]*W[x] for j,x in enumerate(kids(s)))
   v=min(cost.values());W[s]=v
   os=[x for x in ('P','Q','C') if x in cost and cost[x]==v]
   if len(os)>1:ties[str(s)]=os
   gaps.extend(x-v for x in cost.values() if x>v)
assert len(W)==680 and len(gaps)==1238
assert ties=={'(11, 0, 1)':['Q','C'],'(9, 3, 0)':['P','C']}
assert min(gaps)==F(8171681291077,1813329127931904)
print(json.dumps({'status':'DUAL_CANDIDATE_ONLY','K126':str(K1),'L126':str(L1),'t':str(t),'ties':ties,'root':str(W[(0,0,0)]),'positive_gaps':len(gaps)},indent=2))
