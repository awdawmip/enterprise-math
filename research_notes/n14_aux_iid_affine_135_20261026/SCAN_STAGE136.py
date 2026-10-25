"""Stage136 exact dual-ray first-event scan only, holding B Q/C tie (no primal theorem)."""
from fractions import Fraction as F
import json
N=14;P=(F(1,8),F(1,24),F(5,6))
K0=F(119895901488,209680375);L0=F(113419128664,209680375)
B=(11,0,1);A=(7,3,0)
def kids(s):
 n,a,b=s;return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
V={};C={};O={}
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);r=F(2**(a+b),3**a)
   cost={'P':K0*r,'Q':L0};coeff={'P':(F(0),r,F(0)),'Q':(F(0),F(0),F(1))}
   if n<N:
    ch=kids(s);cost['C']=1+sum(P[j]*V[t] for j,t in enumerate(ch))
    coeff['C']=tuple((F(1) if i==0 else F(0))+sum(P[j]*C[t][i] for j,t in enumerate(ch)) for i in range(3))
   q=min(cost.values());opts=[act for act in ('P','Q','C') if act in cost and cost[act]==q]
   chosen='Q' if s==B else 'P' if s==A else opts[0]
   assert chosen in opts
   V[s],C[s],O[s]=cost[chosen],coeff[chosen],opts
bb=tuple((F(1) if i==0 else F(0))+sum(P[j]*C[t][i] for j,t in enumerate(kids(B))) for i in range(3))
m=bb[1]/(1-bb[2]);assert m==F(112,129)
oldties=[];events=[];pg=0
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);r=F(2**(a+b),3**a)
   cost={'P':K0*r,'Q':L0};coeff={'P':(F(0),r,F(0)),'Q':(F(0),F(0),F(1))}
   if n<N:
    ch=kids(s);cost['C']=1+sum(P[j]*V[t] for j,t in enumerate(ch))
    coeff['C']=tuple((F(1) if i==0 else F(0))+sum(P[j]*C[t][i] for j,t in enumerate(ch)) for i in range(3))
   chosen='Q' if s==B else 'P' if s==A else O[s][0]
   chosenSlope=-C[s][1]-m*C[s][2]
   for act,value in cost.items():
    if act==chosen:continue
    gap=value-V[s];derivative=-coeff[act][1]-m*coeff[act][2]-chosenSlope
    assert gap>=0
    if gap==0:oldties.append((s,chosen,act,derivative))
    else:
     pg+=1
     if derivative<0:events.append((gap/-derivative,s,chosen,act))
assert pg==1238
first=min(events)
t=first[0];K1=K0-t;L1=L0-m*t
values={};T={};gaps=[]
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);cost={'P':K1*F(2**(a+b),3**a),'Q':L1}
   if n<N:cost['C']=1+sum(P[j]*values[t] for j,t in enumerate(kids(s)))
   v=min(cost.values());values[s]=v
   opts=[act for act in ('P','Q','C') if act in cost and cost[act]==v]
   if len(opts)>1:T[str(s)]=opts
   gaps.extend(x-v for x in cost.values() if x>v)
if __name__=='__main__':
 print(json.dumps({'status':'DUAL_CANDIDATE_ONLY','m':str(m),'t':str(t),'K136':str(K1),'L136':str(L1),'old_ties':[(str(s),o,a,str(d)) for s,o,a,d in oldties],
 'first_event':(str(first[1]),first[2],first[3]),'root':str(values[(0,0,0)]),'ties':T,'strictly_positive_gaps':len(gaps),'min_positive_gap':str(min(gaps))},indent=2))
