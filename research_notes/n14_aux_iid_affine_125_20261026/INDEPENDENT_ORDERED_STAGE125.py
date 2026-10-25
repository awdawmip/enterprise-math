"""Independent literal ordered-prefix integer-weight DFS, Stage125."""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
import json
N=14;pn=(3,1,20);qn=(1,1,10);p=tuple(F(x,24) for x in pn)
K=F(3579845625,4855672);L=F(416181048,606959)
A=(9,3,0);U=(12,7,5)
@lru_cache(None)
def opt(n,a,b):
 c={'P':K*F(2**(a+b),3**a),'Q':L}
 if n<N:c['C']=1+sum(p[j]*opt(n+1,a+(j==0),b+(j==1))[0] for j in range(3))
 v=min(c.values())
 return v,tuple(k for k in ('P','Q','C') if k in c and c[k]==v)
corners={};visited={};hits={}
for y in (0,1):
 for w in (0,1):
  acc=[0,0,0,0,0];h=defaultdict(lambda:[0,0,0])
  def dfs(n,a,b,pw,qw):
   acc[4]+=1;s=(n,a,b)
   if s in (A,U):
    h[s][0]+=1;h[s][1]+=pw*24**(N-n);h[s][2]+=qw*12**(N-n)
   act=('P' if y else 'C') if s==A else ('Q' if w else 'C') if s==U else opt(n,a,b)[1][0]
   assert act in opt(n,a,b)[1],(s,act)
   if act=='C':
    for j in range(3):dfs(n+1,a+(j==0),b+(j==1),pw*pn[j],qw*qn[j])
   else:
    xp=pw*24**(N-n);xq=qw*12**(N-n)
    if act=='Q':acc[0]+=xp
    else:acc[1]+=xq
    acc[2]+=n*xp;acc[3]+=n*xq
  dfs(0,0,0,1,1)
  tag=f'{y}{w}'
  corners[tag]=tuple(F(acc[j],(24 if j in (0,2) else 12)**N) for j in range(4))
  visited[tag]=acc[4]
  if tag=='00':hits={str(k):{'words':v[0],'P':str(F(v[1],24**N)),'Q':str(F(v[2],12**N))} for k,v in h.items()}
assert opt.cache_info().currsize==680
assert hits[str(A)]=={'words':84,'P':'109375/1990656','Q':'109375/6718464'}
assert hits[str(U)]=={'words':142,'P':'71/8349416423424','Q':'71/4458050224128'}
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
mul=lambda a,t:tuple(x*t for x in a)
M=corners['00'];dA=sub(corners['10'],M);dU=sub(corners['01'],M)
assert corners['11']==add(add(M,dA),dU)
D=lambda m:m[0]-m[1]
y0=-D(M)/D(dA);slope=-D(dU)/D(dA)
assert y0==F(151548960415319,415627392000000)
assert slope==F(2560757,5818783488000000)
moment=lambda w:add(add(M,mul(dA,y0+slope*w)),mul(dU,w))
left,right=moment(F(0)),moment(F(1));eta=right[0]-left[0]
assert left[0]==left[1] and right[0]==right[1]
assert left[2]>left[3] and right[2]>right[3]
assert left[0]==F(2573845372952647230925,7411551152237344456704)
assert left[2]==F(377878009388672358128945,29646204608949377826816)
assert eta==F(43094089,1647011367163854323712)
assert right[2]==left[2]-(K+L)*eta
print(json.dumps({'status':'PASS','states':680,'firsthits':hits,'visited':visited,'corners':{k:list(map(str,v)) for k,v in corners.items()},'M00':list(map(str,M)),'dA':list(map(str,dA)),'dU':list(map(str,dU)),'eta125':str(eta),'alpha125':str(right[0]),'V125':str(right[2])},indent=2))
