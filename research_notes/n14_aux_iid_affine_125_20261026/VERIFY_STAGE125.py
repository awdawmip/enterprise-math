"""Stage125 author exact Fraction Bellman/four-observer checker."""
from fractions import Fraction as F
from functools import lru_cache
import json
N=14; P=(F(1,8),F(1,24),F(5,6)); Q=(F(1,12),F(1,12),F(5,6))
K=F(3579845625,4855672); L=F(416181048,606959)
A=(9,3,0);U=(12,7,5);root=(0,0,0)
kids=lambda s:((s[0]+1,s[1]+1,s[2]),(s[0]+1,s[1],s[2]+1),(s[0]+1,s[1],s[2]))
H={};act={};ties={};gaps=[]
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);c={'P':K*F(2**(a+b),3**a),'Q':L}
   if n<N:c['C']=1+sum(P[j]*H[t] for j,t in enumerate(kids(s)))
   v=min(c.values());H[s]=v
   opt=[k for k,x in c.items() if x==v];act[s]=opt[0]
   if len(opt)>1:ties[s]=opt
   gaps.extend(x-v for x in c.values() if x>v)
assert len(H)==680 and len(gaps)==1238
assert ties=={A:['P','C'],U:['Q','C']}
assert min(gaps)==F(578968738307,115991671209984)
assert H[root]==F(16854019707653693377319545,33249530339162194968576)
PDEC=(F(0),F(1),F(0),F(0));QDEC=(F(1),F(0),F(0),F(0))
add=lambda u,v:tuple(a+b for a,b in zip(u,v))
sub=lambda u,v:tuple(a-b for a,b in zip(u,v))
mul=lambda v,t:tuple(t*a for a in v)
@lru_cache(None)
def moment(s,y,w):
 def cont():
  cs=[moment(t,y,w) for t in kids(s)]
  return (sum(P[j]*cs[j][0] for j in range(3)),sum(Q[j]*cs[j][1] for j in range(3)),
          1+sum(P[j]*cs[j][2] for j in range(3)),1+sum(Q[j]*cs[j][3] for j in range(3)))
 if s==A:return add(mul(PDEC,y),mul(cont(),1-y))
 if s==U:return add(mul(QDEC,w),mul(cont(),1-w))
 if act[s]=='P':return PDEC
 if act[s]=='Q':return QDEC
 return cont()
M=moment(root,F(0),F(0));dA=sub(moment(root,F(1),F(0)),M);dU=sub(moment(root,F(0),F(1)),M)
assert moment(root,F(1),F(1))==add(add(M,dA),dU)
assert dU==(F(71,534362651099136),-F(71,641959232274432),-F(71,7421703487488),-F(923,53496602689536))
D=lambda m:m[0]-m[1]
y0=-D(M)/D(dA);slope=-D(dU)/D(dA)
assert y0==F(151548960415319,415627392000000)
assert slope==F(2560757,5818783488000000)
assert 0<y0<y0+slope<1
def point(w):
 m=add(add(M,mul(dA,y0+slope*w)),mul(dU,w))
 assert m[0]==m[1] and m[2]>m[3] and m[2]+(K+L)*m[0]==H[root]
 return m
v0=point(F(0));v1=point(F(1))
assert v0[0]==F(2573845372952647230925,7411551152237344456704)
assert v0[2]==F(377878009388672358128945,29646204608949377826816)
eta=v1[0]-v0[0]
assert eta==F(43094089,1647011367163854323712)
assert v1[2]==v0[2]-(K+L)*eta
print(json.dumps({'status':'PASS','states':680,'positive_gaps':1238,'ties':{str(k):v for k,v in ties.items()},'root':str(H[root]),'M00':list(map(str,M)),'dA':list(map(str,dA)),'dU':list(map(str,dU)),'balance_y0':str(y0),'balance_slope':str(slope),'eta125':str(eta),'alpha125':str(v1[0]),'V125':str(v1[2]),'time_margin_left':str(v0[2]-v0[3]),'time_margin_right':str(v1[2]-v1[3])},indent=2))
