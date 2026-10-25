"""Stage126 independently implemented ordered-prefix integer-mass DFS."""
from functools import cache
from fractions import Fraction as F
from collections import defaultdict
import json
N=14;pn=(3,1,20);qn=(1,1,10);p=tuple(F(x,24) for x in pn)
K=F(387210888,527153);L=F(359623016,527153)
A=(9,3,0);B=(11,0,1)
@cache
def value(n,a,b):
 c={'P':K*F(2**(a+b),3**a),'Q':L}
 if n<N:c['C']=1+sum(p[j]*value(n+1,a+(j==0),b+(j==1))[0] for j in range(3))
 v=min(c.values());return v,tuple(k for k in ('P','Q','C') if k in c and c[k]==v)
corners={};visits={};hits={}
for y in (0,1):
 for w in (0,1):
  accum=[0,0,0,0,0];hit=defaultdict(lambda:[0,0,0])
  def dfs(n,a,b,pw,qw):
   accum[4]+=1;s=(n,a,b)
   if s in (A,B):
    hit[s][0]+=1;hit[s][1]+=pw*24**(N-n);hit[s][2]+=qw*12**(N-n)
   opts=value(n,a,b)[1]
   act=('P' if y else 'C') if s==A else ('Q' if w else 'C') if s==B else opts[0]
   assert act in opts,(s,act,opts)
   if act=='C':
    for j in range(3):dfs(n+1,a+(j==0),b+(j==1),pw*pn[j],qw*qn[j])
   else:
    wp=pw*24**(N-n);wq=qw*12**(N-n)
    if act=='Q':accum[0]+=wp
    else:accum[1]+=wq
    accum[2]+=n*wp;accum[3]+=n*wq
  dfs(0,0,0,1,1)
  tag=f'{y}{w}'
  corners[tag]=tuple(F(accum[j],(24 if j in (0,2) else 12)**N) for j in range(4))
  visits[tag]=accum[4]
  if tag=='00':hits={str(k):{'words':v[0],'P':str(F(v[1],24**N)),'Q':str(F(v[2],12**N))} for k,v in hit.items()}
assert value.cache_info().currsize==680
assert hits[str(A)]=={'words':84,'P':'109375/1990656','Q':'109375/6718464'}
assert hits[str(B)]=={'words':11,'P':'107421875/1451188224','Q':'107421875/725594112'}
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
mul=lambda a,t:tuple(x*t for x in a)
base=corners['00'];dA=sub(corners['10'],base);dB=sub(corners['01'],base)
assert corners['11']==add(add(base,dA),dB)
assert dB==(F(4619140625,2229025112064),-F(751953125,417942208512),-F(25673828125,278628139008),-F(17939453125,104485552128))
D=lambda x:x[0]-x[1]
y0=-D(base)/D(dA);slope=-D(dB)/D(dA)
assert y0==F(707228482791741,1939594496000000) and slope==F(53020000,7576541)
wcap=(1-y0)/slope
assert wcap==F(1232366013208259,13573120000000000)
M=lambda w:add(add(base,mul(dA,y0+slope*w)),mul(dB,w))
lo,hi=M(F(0)),M(wcap);eta=hi[0]-lo[0]
assert lo[0]==lo[1] and hi[0]==hi[1] and lo[2]>lo[3] and hi[2]>hi[3]
assert lo[0]==F(5147690745905682308651,14823102304474688913408)
assert lo[2]==F(1511512037550274393644029,118584818435797511307264)
assert eta==F(649645440960773356627,19052627495351466816700416)
assert hi[0]==F(18340838011402083499,52808422392537808896)
assert hi[2]==F(335279238082246223695,26404211196268904448)
assert hi[2]==lo[2]-(K+L)*eta
print(json.dumps({'status':'PASS','states':680,'literal_first_hits':hits,'visited':visits,'corners':{k:list(map(str,v)) for k,v in corners.items()},'M00':list(map(str,base)),'dA':list(map(str,dA)),'dB':list(map(str,dB)),'wcap':str(wcap),'eta126':str(eta),'alpha126':str(hi[0]),'V126':str(hi[2])},indent=2))
