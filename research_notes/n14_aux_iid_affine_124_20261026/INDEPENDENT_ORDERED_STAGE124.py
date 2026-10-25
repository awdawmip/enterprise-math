"""Stage124 independently written top-down DP + literal-word integer DFS, author evidence."""
from fractions import Fraction as F
from functools import cache
from collections import defaultdict
import json
N=14;pn=(3,1,20);qn=(1,1,10);p=tuple(F(i,24) for i in pn)
K=F(1245231873,1658336);L=F(36440256,51823)
A=(9,3,0);T=(14,7,4)
@cache
def best(n,a,b):
 costs={'P':K*F(2**(a+b),3**a),'Q':L}
 if n<N:costs['C']=1+sum(p[j]*best(n+1,a+(j==0),b+(j==1))[0] for j in range(3))
 z=min(costs.values())
 return z,tuple(k for k,v in costs.items() if v==z)
corners={};visited={};firsthits={}
for x in (0,1):
 for z in (0,1):
  acc=[0,0,0,0,0];hit=defaultdict(lambda:[0,0,0])
  def walk(n,a,b,pw,qw):
   acc[4]+=1;s=(n,a,b)
   if s in (A,T):
    hit[s][0]+=1
    hit[s][1]+=pw*24**(N-n)
    hit[s][2]+=qw*12**(N-n)
   options=best(n,a,b)[1]
   if s==A:action='P' if x else 'C'
   elif s==T:action='Q' if z else 'P'
   else:action=options[0]
   assert action in options,(s,action,options)
   if action=='C':
    for j in range(3):
     walk(n+1,a+(j==0),b+(j==1),pw*pn[j],qw*qn[j])
   else:
    wp=pw*24**(N-n);wq=qw*12**(N-n)
    if action=='Q':acc[0]+=wp
    else:acc[1]+=wq
    acc[2]+=n*wp;acc[3]+=n*wq
  walk(0,0,0,1,1)
  vector=tuple(F(acc[i],(24 if i in (0,2) else 12)**N) for i in range(4))
  corners[f'{x}{z}']=list(map(str,vector));visited[f'{x}{z}']=acc[4]
  if x==z==0:
   firsthits={str(s):{'ordered_words':t[0],'P_mass':str(F(t[1],24**N)),
     'Q_mass':str(F(t[2],12**N))} for s,t in hit.items()}
assert best.cache_info().currsize==680
assert firsthits[str(A)]=={'ordered_words':84,'P_mass':'109375/1990656','Q_mass':'109375/6718464'}
assert firsthits[str(T)]=={'ordered_words':7962,'P_mass':'165875/25048249270272','Q_mass':'165875/26748301344768'}
get=lambda tag:tuple(map(F,corners[tag]))
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
mul=lambda a,t:tuple(x*t for x in a)
M=get('00');dA=sub(get('10'),M);dT=sub(get('01'),M)
assert get('11')==add(add(M,dA),dT)
assert dT[2:]==(0,0)
D=lambda v:v[0]-v[1]
y0=-D(M)/D(dA);slope=-D(dT)/D(dA)
assert y0==F(151539326395319,415627392000000)
assert slope==F(160567,6927123200)
left=add(M,mul(dA,y0))
right=add(add(M,mul(dA,y0+slope)),dT)
assert 0<y0<y0+slope<1
assert left[0]==left[1] and right[0]==right[1]
assert left[2]>left[3] and right[2]>right[3]
assert left[0]==F(2573845365525582162925,7411551152237344456704)
assert left[2]==F(377878052586265662571445,29646204608949377826816)
assert right[0]==F(2573845372952647230925,7411551152237344456704)
assert right[2]==F(377878009388672358128945,29646204608949377826816)
eta=right[0]-left[0]
assert eta==F(8596140125,8578184203978407936)
assert right[2]==left[2]-(K+L)*eta
print(json.dumps({'status':'PASS','states':680,'corners':corners,'prefix_visits':visited,
 'first_hits':firsthits,'M00':list(map(str,M)),
 'dA':list(map(str,dA)),'dT':list(map(str,dT)),
 'balance_intercept':str(y0),'balance_slope':str(slope),
 'eta124':str(eta),'alpha124':str(right[0]),'V124':str(right[2])},indent=2))
