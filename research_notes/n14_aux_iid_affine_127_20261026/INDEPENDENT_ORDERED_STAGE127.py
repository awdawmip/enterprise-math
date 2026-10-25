"""Stage127 independent top-down Bellman and literal ordered integer-weight DFS."""
from functools import lru_cache
from fractions import Fraction as F
from collections import defaultdict
import json
N=14;PN=(3,1,20);QN=(1,1,10);P=tuple(F(x,24) for x in PN)
K=F(8246448,11561);L=F(7673768,11561)
B=(11,0,1);C=(11,6,2)
@lru_cache(None)
def val(n,a,b):
 costs={'P':K*F(2**(a+b),3**a),'Q':L}
 if n<N:costs['C']=1+sum(P[j]*val(n+1,a+(j==0),b+(j==1))[0] for j in range(3))
 v=min(costs.values())
 return v,tuple(k for k in ('P','Q','C') if k in costs and costs[k]==v)
def corner(w,u):
 acc=[0,0,0,0,0];hit=defaultdict(lambda:[0,0,0])
 def dfs(n,a,b,pw,qw):
  acc[4]+=1;s=(n,a,b)
  if s in (B,C):
   h=hit[s];h[0]+=1;h[1]+=pw*24**(N-n);h[2]+=qw*12**(N-n)
  options=val(n,a,b)[1]
  act=('Q' if w else 'C') if s==B else ('P' if u else 'C') if s==C else options[0]
  assert act in options,(s,act,options)
  if act=='C':
   for j in range(3):dfs(n+1,a+(j==0),b+(j==1),pw*PN[j],qw*QN[j])
  else:
   wp=pw*24**(N-n);wq=qw*12**(N-n)
   if act=='Q':acc[0]+=wp
   else:acc[1]+=wq
   acc[2]+=n*wp;acc[3]+=n*wq
 dfs(0,0,0,1,1)
 v=(F(acc[0],24**N),F(acc[1],12**N),F(acc[2],24**N),F(acc[3],12**N))
 hits={str(s):{'words':h[0],'P':str(F(h[1],24**N)),'Q':str(F(h[2],12**N))} for s,h in hit.items()}
 return v,acc[4],hits
M00,n00,h=corner(0,0);M10,n10,_=corner(1,0);M01,n01,_=corner(0,1);M11,n11,_=corner(1,1)
assert val.cache_info().currsize==680
assert val(*B)[1]==('Q','C') and val(*C)[1]==('P','C')
assert h[str(B)]=={'words':11,'P':'107421875/1451188224','Q':'107421875/725594112'}
assert h[str(C)]=={'words':2201,'P':'275125/32614907904','Q':'275125/92876046336'}
dB=tuple(x-y for x,y in zip(M10,M00))
dC=tuple(x-y for x,y in zip(M01,M00))
assert M11==tuple(M00[i]+dB[i]+dC[i] for i in range(4))
assert dB==(F(4619140625,2229025112064),-F(751953125,417942208512),-F(25673828125,278628139008),-F(17939453125,104485552128))
assert dC==(-F(3026375,112717121716224),F(3026375,80244904034304),-F(42644375,4696546738176),-F(22835375,6687075336192))
D=lambda x:x[0]-x[1]
w0=-D(M00)/D(dB);slope=-D(dC)/D(dB)
assert w0==F(1232366013208259,13573120000000000)
assert slope==F(3858353,231360000000)
assert 0<w0<w0+slope<1
M=lambda u:tuple(M00[i]+(w0+slope*u)*dB[i]+u*dC[i] for i in range(4))
lo,hi=M(F(0)),M(F(1));eta=hi[0]-lo[0]
assert lo[0]==lo[1]==F(18340838011402083499,52808422392537808896)
assert lo[2]==F(335279238082246223695,26404211196268904448)
assert eta==F(3180720125,412565799941701632)>0
assert hi[0]==hi[1]==F(18340838418534259499,52808422392537808896)
assert hi[2]==F(335278957759082895695,26404211196268904448)
assert lo[2]>lo[3] and hi[2]>hi[3]
assert hi[2]==lo[2]-(K+L)*eta
print(json.dumps({'status':'PASS','states':val.cache_info().currsize,'visits':{'00':n00,'10':n10,'01':n01,'11':n11},
'first_hits':h,'corners':{k:list(map(str,v)) for k,v in [('00',M00),('10',M10),('01',M01),('11',M11)]},
'eta127':str(eta),'alpha127':str(hi[0]),'V127':str(hi[2])},indent=2))
