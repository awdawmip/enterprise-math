"""Stage127 exact dual first-event scan, candidate only, after A saturates P."""
from fractions import Fraction as F
import json
N=14;p=(F(1,8),F(1,24),F(5,6))
K0=F(387210888,527153);L0=F(359623016,527153)
A=(9,3,0);B=(11,0,1)
kids=lambda s:((s[0]+1,s[1]+1,s[2]),(s[0]+1,s[1],s[2]+1),(s[0]+1,s[1],s[2]))
val={};coef={};opts={}
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);r=F(2**(a+b),3**a);v={'P':K0*r,'Q':L0}
   c={'P':(F(0),r,F(0)),'Q':(F(0),F(0),F(1))}
   if n<N:
    cs=kids(s);v['C']=1+sum(p[j]*val[x] for j,x in enumerate(cs))
    c['C']=tuple((F(1) if i==0 else F(0))+sum(p[j]*coef[x][i] for j,x in enumerate(cs)) for i in range(3))
   m=min(v.values());op=[x for x in ('P','Q','C') if x in v and v[x]==m];opts[s]=op
   action='P' if s==A else 'Q' if s==B else op[0]
   assert action in op
   val[s],coef[s]=v[action],c[action]
cB=tuple(F(1 if i==0 else 0)+sum(p[j]*coef[t][i] for j,t in enumerate(kids(B))) for i in range(3))
m=cB[1]/(1-cB[2]);assert m==F(112,129)
events=[];old_ties=[];positive=0
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);r=F(2**(a+b),3**a);v={'P':K0*r,'Q':L0}
   c={'P':(F(0),r,F(0)),'Q':(F(0),F(0),F(1))}
   if n<N:
    cs=kids(s);v['C']=1+sum(p[j]*val[x] for j,x in enumerate(cs))
    c['C']=tuple((F(1) if i==0 else F(0))+sum(p[j]*coef[x][i] for j,x in enumerate(cs)) for i in range(3))
   chosen='P' if s==A else 'Q' if s==B else opts[s][0]
   dc=-c[chosen][1]-m*c[chosen][2]
   for alt,cost in v.items():
    if alt==chosen:continue
    gap=cost-v[chosen];dg=-c[alt][1]-m*c[alt][2]-dc
    assert gap>=0
    if gap==0:old_ties.append((s,chosen,alt,dg))
    else:
     positive+=1
     if dg<0:events.append((gap/-dg,s,chosen,alt))
assert positive==1238
assert old_ties==[(B,'Q','C',F(0)),(A,'P','C',F(527153,288893952))]
t,s,old,alt=min(events)
assert t==F(11764115784,554037803) and s==(11,6,2) and old=='C' and alt=='P'
K1=K0-t;L1=L0-m*t
assert K1==F(8246448,11561) and L1==F(7673768,11561)
V={};ties={};gaps=[]
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   st=(n,a,b);cost={'P':K1*F(2**(a+b),3**a),'Q':L1}
   if n<N:cost['C']=1+sum(p[j]*V[x] for j,x in enumerate(kids(st)))
   v=min(cost.values());V[st]=v
   os=[x for x in ('P','Q','C') if x in cost and cost[x]==v]
   if len(os)>1:ties[str(st)]=os
   gaps.extend(x-v for x in cost.values() if x>v)
assert len(V)==680 and len(gaps)==1238
assert ties=={'(11, 0, 1)':['Q','C'],'(11, 6, 2)':['P','C']}
assert min(gaps)==F(71,9459)
print(json.dumps({'status':'DUAL_CANDIDATE_ONLY','m':str(m),'t':str(t),'K127':str(K1),'L127':str(L1),'root':str(V[(0,0,0)]),'ties':ties,'positive_gaps':len(gaps),'min_gap':str(min(gaps))},indent=2))
