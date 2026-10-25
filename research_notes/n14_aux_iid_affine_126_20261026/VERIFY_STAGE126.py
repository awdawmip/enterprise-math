"""Author Stage126 exact Fraction Bellman and four-observer proof checker."""
from fractions import Fraction as F
from functools import lru_cache
import json
N=14; P=(F(1,8),F(1,24),F(5,6)); Q=(F(1,12),F(1,12),F(5,6))
K=F(387210888,527153);L=F(359623016,527153)
A=(9,3,0);B=(11,0,1);R=(0,0,0)
kids=lambda s:((s[0]+1,s[1]+1,s[2]),(s[0]+1,s[1],s[2]+1),(s[0]+1,s[1],s[2]))
H={};ACT={};TIES={};GAPS=[]
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);c={'P':K*F(2**(a+b),3**a),'Q':L}
   if n<N:c['C']=1+sum(P[j]*H[si] for j,si in enumerate(kids(s)))
   v=min(c.values());H[s]=v
   opts=[key for key,x in c.items() if x==v];ACT[s]=opts[0]
   if len(opts)>1:TIES[s]=opts
   GAPS.extend(x-v for x in c.values() if x>v)
assert len(H)==680 and len(GAPS)==1238
assert TIES=={B:['Q','C'],A:['P','C']}
assert min(GAPS)==F(8171681291077,1813329127931904)
assert H[R]==F(9717182964780466957407421,19251810711959532208128)
add=lambda u,v:tuple(x+y for x,y in zip(u,v))
sub=lambda u,v:tuple(x-y for x,y in zip(u,v))
scale=lambda u,f:tuple(x*f for x in u)
PDEC=(F(0),F(1),F(0),F(0));QDEC=(F(1),F(0),F(0),F(0))
@lru_cache(None)
def M(s,y,w):
 def C():
  xs=[M(t,y,w) for t in kids(s)]
  return (sum(P[j]*xs[j][0] for j in range(3)),sum(Q[j]*xs[j][1] for j in range(3)),
          1+sum(P[j]*xs[j][2] for j in range(3)),1+sum(Q[j]*xs[j][3] for j in range(3)))
 if s==A:return add(scale(PDEC,y),scale(C(),1-y))
 if s==B:return add(scale(QDEC,w),scale(C(),1-w))
 if ACT[s]=='P':return PDEC
 if ACT[s]=='Q':return QDEC
 return C()
base=M(R,F(0),F(0));dA=sub(M(R,F(1),F(0)),base);dB=sub(M(R,F(0),F(1)),base)
assert M(R,F(1),F(1))==add(add(base,dA),dB)
assert dA==(-F(1921609375,7925422620672),F(259765625,835884417024),-F(20758609375,330225942528),-F(1476453125,69657034752))
assert dB==(F(4619140625,2229025112064),-F(751953125,417942208512),-F(25673828125,278628139008),-F(17939453125,104485552128))
D=lambda v:v[0]-v[1]
y0=-D(base)/D(dA);slope=-D(dB)/D(dA)
assert y0==F(707228482791741,1939594496000000)
assert slope==F(53020000,7576541)
wcap=(1-y0)/slope
assert wcap==F(1232366013208259,13573120000000000) and 0<wcap<1
alpha125=F(5147690745905682308651,14823102304474688913408)
V125=F(1511512037550274393644029,118584818435797511307264)
def pt(w):
 y=y0+slope*w
 assert 0<=w<=wcap and 0<=y<=1
 v=add(add(base,scale(dA,y)),scale(dB,w))
 assert v[0]==v[1] and v[2]>v[3]
 assert v[2]+(K+L)*v[0]==H[R]
 return v
lo,hi=pt(F(0)),pt(wcap)
eta=hi[0]-lo[0]
assert lo[0]==alpha125 and lo[2]==V125
assert eta==F(649645440960773356627,19052627495351466816700416)>0
assert hi[0]==F(18340838011402083499,52808422392537808896)
assert hi[2]==F(335279238082246223695,26404211196268904448)
assert hi[2]==V125-(K+L)*eta
assert hi[2]-hi[3]==F(16916724390710645177,26404211196268904448)
print(json.dumps({'status':'PASS','states':len(H),'positive_gaps':len(GAPS),'min_positive_gap':str(min(GAPS)),'root':str(H[R]),'K':str(K),'L':str(L),'ties':{str(k):v for k,v in TIES.items()},'M00':list(map(str,base)),'dA':list(map(str,dA)),'dB':list(map(str,dB)),'y0':str(y0),'slope':str(slope),'wcap':str(wcap),'eta126':str(eta),'alpha126':str(hi[0]),'V126':str(hi[2]),'left_margin':str(lo[2]-lo[3]),'right_margin':str(hi[2]-hi[3])},indent=2))
