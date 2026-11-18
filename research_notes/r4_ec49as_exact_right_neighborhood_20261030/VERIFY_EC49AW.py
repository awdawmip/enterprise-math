"""EC49AW: exact edgewise dual and analytic residual certificate. Pure standard-library Fraction."""
from fractions import Fraction as F
from itertools import combinations
from collections import defaultdict
import json
B=(16,16,16,43); C2=F(13,16); TARGET=F(14401,123840)
COST=(1,1,2,2,0); TICKS=((4,26),(15,15),(26,4))
A=tuple(tuple(int(i//5==r) if r<3 else COST[i%5] for i in range(15)) for r in range(4))
Z=F(0)
def solve4(cols):
 m=[[F(A[i][j]) for j in cols]+[F(B[i])] for i in range(4)]
 for k in range(4):
  r=next((i for i in range(k,4) if m[i][k]),None)
  if r is None:return None
  m[k],m[r]=m[r],m[k]
  d=m[k][k];m[k]=[v/d for v in m[k]]
  for i in range(4):
   if i!=k:
    v=m[i][k]
    if v:m[i]=[a-v*b for a,b in zip(m[i],m[k])]
 return [m[i][4]/16 for i in range(4)]
def vertices():
 vs=set()
 for s in combinations(range(15),4):
  sol=solve4(s)
  if sol is None or min(sol)<0:continue
  x=[Z]*15
  for j,v in zip(s,sol):x[j]=v
  x=tuple(x)
  assert all(sum(A[i][j]*x[j] for j in range(15))==F(B[i],16) for i in range(4))
  assert sum(v!=0 for v in x)==4
  vs.add(x)
 assert len(vs)==168
 return vs
def edges(vs):
 group=defaultdict(set)
 for x in vs:
  supp={i for i,v in enumerate(x) if v}
  for i in range(15):
   if i not in supp:group[tuple(sorted(supp|{i}))].add(x)
 assert len(group)==924 and all(len(v)==2 for v in group.values())
 return [(s,*sorted(pair)) for s,pair in sorted(group.items())]
def fibers(x):
 T=[];V=[]
 for c in range(4):
  for u in range(2):
   q=[x[5*w+c]*F(TICKS[w][u],90) for w in range(3)]
   t=sum(q)
   T.append(t);V.append(sum(max(Z,(43*qq-16*t)/172) for qq in q))
 return tuple(T),tuple(V)
def paid(x):return sum(x[5*w+c] for w in range(3) for c in range(4))/3
def dual(x,lam):
 T,V=fibers(x)
 return lam*C2+sum(max(Z,v-lam*t) for v,t in zip(V,T))
def interval(x):
 T,V=fibers(x)
 pts=sorted({Z,F(1)}|{v/t for v,t in zip(V,T) if t})
 assert all(Z<=a<=1 for a in pts)
 good=[]
 for a,b in zip(pts,pts[1:]):
  fa,fb=dual(x,a),dual(x,b)
  if fa<=TARGET and fb<=TARGET:good.append((a,b))
  elif fa<=TARGET<fb:good.append((a,a+(b-a)*(TARGET-fa)/(fb-fa)))
  elif fb<=TARGET<fa:good.append((a+(b-a)*(TARGET-fa)/(fb-fa),b))
 return (min(a for a,b in good),max(b for a,b in good)) if good else None
def clip(x,y):
 a,b=paid(x),paid(y)
 if max(a,b)<C2:return None
 if min(a,b)>=C2:return x,y
 if a<b:x,y,a,b=y,x,b,a
 v=(C2-b)/(a-b)
 z=tuple(v*u+(1-v)*w for u,w in zip(x,y))
 assert paid(z)==C2
 return x,z
def signature(pair):
 x,y=pair
 return tuple(sorted(tuple(sorted((x[5*w+c]*F(TICKS[w][u],90),y[5*w+c]*F(TICKS[w][u],90)) for w in range(3))) for c in range(4) for u in range(2)))
def exceptional(pair):
 high,low=pair
 assert high==(F(11,16),Z,Z,Z,F(5,16),Z,F(1),Z,Z,Z,F(1),Z,Z,Z,Z)
 assert low==(F(3,16),Z,F(1,4),Z,F(9,16),Z,F(1),Z,Z,Z,F(1),Z,Z,Z,Z)
 r=F(89,104);cross=[]
 for f in range(8):
  c,u=divmod(f,2)
  a=[high[5*w+c]*F(TICKS[w][u],90) for w in range(3)]
  b=[low[5*w+c]*F(TICKS[w][u],90) for w in range(3)]
  for w in range(3):
   x=43*a[w]-16*sum(a);y=43*b[w]-16*sum(b)
   if x*y<0:cross.append((f,w,x/(x-y)))
 assert cross==[(1,2,r)]
 for t in (Z,r,F(1)):
  xx=tuple((1-t)*a+t*b for a,b in zip(high,low))
  T,V=fibers(xx)
  assert T[0]==(115-8*t)/360 and T[1]==(175-104*t)/720
  assert V[0]==(16*t+329)/(45*172)
  assert V[2]==V[3]==F(9,344) and V[4]+V[5]==9*t/688
  v1=((3349-2808*t) if t<=r else (1925-1144*t))/(720*172)
  assert V[1]==v1
  excess=paid(xx)-C2
  assert excess==(1-t)/12
  H=sum(V)-excess*V[1]/T[1]
  gap=((4472*t*t-8397*t+4990)/(7740*(175-104*t)) if t<=r else 29*(1-t)/2580)
  assert H==TARGET-gap
 assert 8397**2-4*4472*4990==-18751511
 # The all-real proof of score signs, density ordering and gap positivity
 # is explicit in PROOF_EC49AW.md; no finite grid is used to infer it.
def main():
 vs=vertices();es=edges(vs);no=0;covered=0;res=[]
 for supp,x,y in es:
  pair=clip(x,y)
  if pair is None:no+=1;continue
  a,b=(interval(z) for z in pair)
  if a and b and max(a[0],b[0])<=min(a[1],b[1]):
   lam=max(a[0],b[0])
   assert dual(pair[0],lam)<=TARGET and dual(pair[1],lam)<=TARGET
   covered+=1
  else:res.append((supp,pair))
 assert (len(vs),len(es),no,covered,len(res))==(168,924,720,196,8)
 canonical=next(pair for supp,pair in res if supp==(0,2,4,6,10))
 exceptional(canonical)
 sig=signature(canonical)
 assert all(signature(pair)==sig for _,pair in res)
 print(json.dumps({'schema':'EC49AW_GLOBAL_ALL_REAL_CERT_V1','eta':'11/30','C1':'43/48','C2':'13/16','k':'177/172','vertices':len(vs),'edges':len(es),'cost_infeasible_edges':no,'dual_price_certified_edges':covered,'analytically_certified_edges':len(res),'residual_supports':[list(s) for s,_ in res],'sign_crossing':'89/104','left_gap_discriminant':-18751511,'global_optimum':'14401/123840','status':'AUTHOR_PROOF_EXACT_FRACTION_PASS_UNREVIEWED_NOT_ADMITTED'},indent=2))
if __name__=='__main__':main()
