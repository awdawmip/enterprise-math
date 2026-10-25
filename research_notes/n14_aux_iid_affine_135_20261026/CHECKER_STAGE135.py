"""Independent continuation of published Stage134: author Stage135 exact Fraction Bellman/moment proof checker."""
from fractions import Fraction as F
from functools import lru_cache
import json
N=14
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
K=F(119895901488,209680375);L=F(113419128664,209680375)
B=(11,0,1);A=(7,3,0);R=(0,0,0)
def child(s):
 n,a,b=s;return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
H={};ACT={};TIES={};GAPS=[]
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);costs={'P':K*F(2**(a+b),3**a),'Q':L}
   if n<N: costs['C']=1+sum(P[j]*H[t] for j,t in enumerate(child(s)))
   v=min(costs.values());H[s]=v
   opts=[act for act in ('P','Q','C') if act in costs and costs[act]==v]
   ACT[s]=opts[0]
   if len(opts)>1:TIES[s]=opts
   GAPS.extend(x-v for x in costs.values() if x>v)
assert len(H)==680 and len(GAPS)==1238
assert TIES=={B:['Q','C'],A:['P','C']},TIES
assert min(GAPS)==F(8101984967,271745766000)
assert H[R]==F(1222494294337487125572330743,3063040058209052550758400)
add=lambda u,v:tuple(x+y for x,y in zip(u,v))
sub=lambda u,v:tuple(x-y for x,y in zip(u,v))
scale=lambda u,t:tuple(x*t for x in u)
QDEC=(F(1),F(0),F(0),F(0));PDEC=(F(0),F(1),F(0),F(0))
@lru_cache(None)
def M(s,w,u):
 def cont():
  xs=[M(t,w,u) for t in child(s)]
  return (sum(P[j]*xs[j][0] for j in range(3)),sum(Q[j]*xs[j][1] for j in range(3)),
          1+sum(P[j]*xs[j][2] for j in range(3)),1+sum(Q[j]*xs[j][3] for j in range(3)))
 if s==B:return add(scale(QDEC,w),scale(cont(),1-w))
 if s==A:return add(scale(PDEC,u),scale(cont(),1-u))
 if ACT[s]=='P':return PDEC
 if ACT[s]=='Q':return QDEC
 return cont()
M00=M(R,F(0),F(0));dB=sub(M(R,F(1),F(0)),M00);dA=sub(M(R,F(0),F(1)),M00)
assert M(R,F(1),F(1))==add(add(M00,dB),dA)
D=lambda x:x[0]-x[1]
w0=-D(M00)/D(dB);sl=-D(dA)/D(dB)
assert w0==F(29128806260109437,81438720000000000),w0
alpha134=F(36703016772992738695,105616844785075617792)
V134=F(656399729826573779227,52808422392537808896)
def pt(u):
 w=w0+sl*u
 assert F(0)<=u<=F(1) and F(0)<=w<=F(1),(u,w)
 m=add(add(M00,scale(dB,w)),scale(dA,u))
 assert m[0]==m[1] and m[2]>m[3]
 assert m[2]+(K+L)*m[0]==H[R]
 return m
lo=pt(F(0))
assert lo[0]==alpha134 and lo[2]==V134
u_max=min(F(1),((F(1)-w0)/sl if sl>0 else (F(0)-w0)/sl)) if sl else F(1)
assert u_max>0
hi=pt(u_max);eta=hi[0]-lo[0]
assert eta>0
assert hi[2]==V134-(K+L)*eta
if __name__=='__main__':
 print(json.dumps({'status':'PASS','states':len(H),'positive_gaps':len(GAPS),'min_positive_gap':str(min(GAPS)),
 'root':str(H[R]),'K':str(K),'L':str(L),'S':str(K+L),'ties':{str(k):v for k,v in TIES.items()},
 'M00':list(map(str,M00)),'dB':list(map(str,dB)),'dA':list(map(str,dA)),
 'w0':str(w0),'slope':str(sl),'umax':str(u_max),'wmax':str(w0+sl*u_max),
 'eta135':str(eta),'alpha134':str(lo[0]),'V134':str(lo[2]),'alpha135':str(hi[0]),'V135':str(hi[2]),
 'left_margin':str(lo[2]-lo[3]),'right_margin':str(hi[2]-hi[3])},indent=2))
