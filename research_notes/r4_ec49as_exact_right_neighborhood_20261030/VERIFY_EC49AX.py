"""EC49AX: independent exact-fraction end-to-end certificate; stdlib Python 3."""
from fractions import Fraction as F
from itertools import combinations
from collections import defaultdict
from math import comb
import json
Z=F(0); E0=F(75,206); E1=F(2,5); C=F(13,16)
co=(1,1,2,2,0); B=(16,16,16,43)
A=[[int(j//5==i) if i<3 else co[j%5] for j in range(15)] for i in range(4)]
h=lambda e:F(77,688)+(674*e-175)/16512

def vertices():
 out=set()
 for ids in combinations(range(15),4):
  m=[[F(A[i][j]) for j in ids]+[F(B[i])] for i in range(4)]
  for k in range(4):
   r=next((i for i in range(k,4) if m[i][k]),None)
   if r is None:break
   m[k],m[r]=m[r],m[k];v=m[k][k];m[k]=[w/v for w in m[k]]
   for i in range(4):
    if i!=k:
     v=m[i][k];m[i]=[u-v*w for u,w in zip(m[i],m[k])]
  else:
   v=[m[i][4]/16 for i in range(4)]
   if min(v)<0:continue
   x=[Z]*15
   for j,w in zip(ids,v):x[j]=w
   x=tuple(x)
   assert sum(z!=0 for z in x)==4
   out.add(x)
 assert len(out)==168
 return out

def edges(vs):
 d=defaultdict(set)
 for x in vs:
  s={i for i,v in enumerate(x) if v}
  for j in range(15):
   if j not in s:d[tuple(sorted(s|{j}))].add(x)
 assert len(d)==924 and all(len(v)==2 for v in d.values())
 return [(s,*sorted(pair)) for s,pair in sorted(d.items())]

def paid(x):return sum(x[5*w+c] for w in range(3) for c in range(4))/3

def clip(x,y):
 p,q=paid(x),paid(y)
 if max(p,q)<C:return None
 if min(p,q)>=C:return (x,y)
 if p<q:x,y,p,q=y,x,q,p
 t=(C-q)/(p-q)
 z=tuple(t*a+(1-t)*b for a,b in zip(x,y))
 assert paid(z)==C
 return (x,z)

def qval(x,e,c,u,w):return x[5*w+c]*(F(1,2)+(2*u-1)*(1-w)*e)/3

def fibers(x,e):
 T=[];V=[]
 for c in range(4):
  for u in range(2):
   q=[qval(x,e,c,u,w) for w in range(3)];t=sum(q)
   T.append(t);V.append(sum(max(Z,(43*v-16*t)/172) for v in q))
 return T,V

def dual(x,e,L):
 T,V=fibers(x,e)
 return L*C+sum(max(Z,v-L*t) for v,t in zip(V,T))

def price_interval(x,e):
 T,V=fibers(x,e);knots=sorted({Z,F(1)}|{v/t for v,t in zip(V,T) if t})
 assert all(Z<=z<=1 for z in knots)
 spans=[]
 for a,b in zip(knots,knots[1:]):
  fa=dual(x,e,a);fb=dual(x,e,b)
  if fa<=h(e) and fb<=h(e):spans.append((a,b))
  elif fa<=h(e)<fb:spans.append((a,a+(b-a)*(h(e)-fa)/(fb-fa)))
  elif fb<=h(e)<fa:spans.append((a+(b-a)*(h(e)-fa)/(fb-fa),b))
 return (min(v[0] for v in spans),max(v[1] for v in spans)) if spans else None

def signature(pair):
 a,b=pair
 return tuple(sorted(tuple(sorted((qval(a,E0,c,u,w),qval(a,E1,c,u,w),
                                      qval(b,E0,c,u,w),qval(b,E1,c,u,w))
                                      for w in range(3))) for c in range(4) for u in range(2)))

def conv(a,b):
 c=[Z]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c

def bern(poly,lo,hi):
 n=len(poly)-1
 power=[sum(poly[j]*comb(j,k)*lo**(j-k)*(hi-lo)**k for j in range(k,n+1)) for k in range(n+1)]
 return [sum(power[k]*F(comb(i,k),comb(n,k)) for k in range(i+1)) for i in range(n+1)]

def poly(poly,x):return sum(v*x**i for i,v in enumerate(poly))

def certify():
 es=edges(vertices());unusable=0;regular=[];special=[]
 for supp,x,y in es:
  pair=clip(x,y)
  if pair is None:unusable+=1;continue
  ints=[price_interval(z,e) for e in (E0,E1) for z in pair]
  if all(i is not None for i in ints) and max(i[0] for i in ints)<=min(i[1] for i in ints):
   L=max(i[0] for i in ints)
   assert all(dual(z,e,L)<=h(e) for e in (E0,E1) for z in pair)
   regular.append((supp,L))
  else:special.append((supp,pair))
 assert (unusable,len(regular),len(special))==(720,196,8)
 sig=signature(special[0][1]);assert all(signature(p)==sig for s,p in special)
 a=[344,0,-1376];b=[-1201,1568,2436];c=[1769,-5096,2060]
 D=[u-4*v for u,v in zip(conv(b,b),conv(a,c))]
 assert D==[-991743,3245760,3509368,-20409088,17272336]
 deriv=[(i+1)*D[i+1] for i in range(4)]
 derb=bern(deriv,E0,E1);assert all(v>0 for v in derb)
 lo=F(3942483,10000000);hi=F(3942484,10000000)
 assert poly(D,E0)<0<poly(D,E1) and poly(D,lo)<0<poly(D,hi)
 outer=F(197,500);assert poly(D,outer)<0
 minus_b=[-v for v in b]
 Fpoly=[u+v for u,v in zip(conv(a,[-4,19]),conv(b,[1,2]))]
 assert Fpoly==[-2577,5702,11076,-21272]
 assert all(v>0 for v in bern(minus_b,outer,E1))
 assert all(v>0 for v in bern(Fpoly,outer,E1))
 high,low=special[0][1]
 # All score signs (apart from fiber 1, latent z=2) are unchanged on rectangle.
 for f in range(8):
  c0,u=divmod(f,2)
  for w in range(3):
   vals=[]
   for e in (E0,E1):
    for x in (high,low):
     q=[qval(x,e,c0,u,z) for z in range(3)]
     vals.append(43*q[w]-16*sum(q))
   if (f,w)==(1,2):assert min(vals)<0<=max(vals)
   else:assert min(vals)>=0 or max(vals)<=0
 # The rational identities below imply positivity for eta<=the root of D
 # and strict improvement afterwards at t*=-b/(2a). Verify algebra by
 # 3x3 exact evaluation: cross-multiplied identities have bidegree <=(2,2).
 for e in (E0,(E0+E1)/2,E1):
  for t in (Z,F(1,2),F(1)):
   x=tuple((1-t)*v+t*w for v,w in zip(high,low))
   T,V=fibers(x,e);q0=qval(x,e,0,1,0);q2=qval(x,e,0,1,2)
   ss0=43*q0-16*T[1];ss2=43*q2-16*T[1]
   base=V[0]+V[2]+V[3]+V[4]+V[5];excess=(1-t)/12
   m=(344-1376*e*e)*t*t+(2436*e*e+1568*e-1201)*t+(2060*e*e-5096*e+1769)
   assert h(e)-(base+ss0/172-excess*ss0/(172*T[1]))==m/(2064*(27-10*e-8*t-16*e*t))
   v=(ss0+ss2)/172
   assert h(e)-(base+v-excess*v/T[1])==(43-54*e)*(1-t)/2064
 # A strictly lawful rational counterexample at eta=2/5.
 x=(F(5,16),Z,F(3,16),Z,F(1,2),Z,F(1),Z,Z,Z,F(1),Z,Z,Z,Z)
 T,V=fibers(x,E1);p=[F(1)]*8;p[1]=F(51,61)
 assert T[1]==F(61,480) and sum(t*v for t,v in zip(T,p))==C
 alpha=beta=Z;events=[]
 for c0 in range(4):
  for u in range(2):
   q=[qval(x,E1,c0,u,z) for z in range(3)];Tcu=sum(q)
   for z in range(3):
    if 43*q[z]-16*Tcu>0:
     events.append((c0,u,z))
     alpha+=p[2*c0+u]*(Tcu+q[z])/4
     beta+=p[2*c0+u]*Tcu/3
 H=alpha-F(177,172)*beta
 assert (alpha,beta,H,H-h(E1))==(F(46459,117120),F(13,48),F(594127,5036160),F(19,58560))
 assert events==[(0,0,2),(0,1,0),(1,0,1),(1,1,1),(2,0,0),(2,1,0)]
 print(json.dumps({'schema':'EC49AX_EXACT_CHECK','vertices':168,'edges':924,
     'infeasible_edges':unusable,'four_corner_edges':len(regular),
     'residual_edges':len(special),'fourcorner_prices':{','.join(map(str,s)):str(L) for s,L in regular},
     'residual_supports':[list(s) for s,p in special],
     'D_coefficients':list(map(int,D)),'Dprime_Bernstein_positive':list(map(str,derb)),
     'eta_star_bracket':[str(lo),str(hi)],'counterexample_H':str(H),
     'counterexample_gain':str(H-h(E1)),
     'status':'AUTHOR_EXACT_CHECK_UNREVIEWED_NOT_ADMITTED'},indent=2))
if __name__=='__main__':certify()
