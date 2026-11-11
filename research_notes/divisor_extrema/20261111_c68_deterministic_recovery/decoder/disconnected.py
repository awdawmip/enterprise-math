"""A finite-depth nonconvex first-gap decoder beyond convex-hull separation."""
from fractions import Fraction as F
import json
P=1<<90
M=20
R=10**8

def lower(x):return (x*P).__floor__()
def upper(x):return (x*P).__ceil__()
def quotient(lo,hi,bl,bh):
 assert bl>0
 return lo*P//bh,-(-hi*P//bl)
def merge(items):
 ans=[]
 for l,h in sorted(items):
  if ans and ans[-1][1]>=l:
   ans[-1][1]=max(ans[-1][1],h)
  else:ans.append([l,h])
 return ans
def make(xlo,xhi):
 # Divide finite-stock factors by K0=2r+1 of the very first active block.
 # Any of two following tested blocks can have spent <=M fives at each earlier step.
 eps=F(1,2*R+1)
 kl,kh=1-4*eps,F(1)
 nl,nh=xlo-(3*M+2)*eps,xhi
 def bounds(al,ah,bl,bh):return al/bh,ah/bl
 rl,rh=bounds(kl+4*nl,kh+4*nh,kl+nl,kh+nh)
 fl,fh=bounds(kl+4*nl,kh+4*nh,4*kl+nl,4*kh+nh)
 el,eh=bounds(kl-eps+4*nl,kh+4*nh,kl-eps+nl,kh+nh)
 return [(lower(28*el*fl**(m+1)/4**m),upper(28*eh*fh**(m+1)/4**m),
          lower(rl**(m+1)/4**m),upper(rh**(m+1)/4**m)) for m in range(M+1)]
def image(box,z):
 tl,th,pl,ph=box;l,h=z
 # take the extremes over independent t,z,rho by exact monotonicity at each fixed rho
 xl=tl*l;xh=th*h
 def value(p,x,up):
  n=(x+p*P)*P;d=x+P**2
  return -(-n//d) if up else n//d
 return value(pl,xh if pl>=P else xl,False),value(ph,xl if ph>=P else xh,True)
def dist(a,b):
 i=j=0;g=4*P
 while i<len(a) and j<len(b):
  l,h=a[i];v,w=b[j]
  if h<v:g=min(g,v-h);i+=1
  elif w<l:g=min(g,l-w);j+=1
  else:return 0
 return g
def certify(xlo,xhi):
 data=make(xlo,xhi)
 assert data[1][2]>P>data[2][3]
 assert data[M][3]<P
 cut=[(0,image(data[M],(0,4*P))[1])]
 spans=[[0,4*P]]
 for _ in range(2):spans=merge(cut+[image(d,z) for d in data[:M] for z in spans])
 a,b=[merge([image(data[i],z) for z in spans]) for i in (0,1)]
 gap=dist(a,b)
 assert gap>0,(str(xlo),str(xhi))
 # certify negative cases; later input z<=2.02 at stock no larger than c and r-1
 eps=F(1,2*R+1)
 assert (1-2*eps+4*xhi)/(1-2*eps+xhi)<F(202,100)
 assert image(data[3],(0,upper(F(202,100))))[1]<data[2][2]
 # For all m>=3 use (4) of C66 rigidity; each rational multiplier grows with e.
 q=(1+xhi)/(4+xhi)
 v=(1+4*xhi-eps)/(1+xhi-eps)
 assert F(202,100)*F(7,4)*q**4*4*(1+4*xhi)/(4+xhi)*v < 3/(4*(1+xhi))
 return dict(interval=[str(xlo),str(xhi)],descendant_components=len(spans),first_zero=len(a),first_one=len(b),
             minimum_gap_lower_1e_minus9_units=gap*10**9//P)
if __name__=='__main__':
 # two disjoint stock bands, above the simultaneous two-column hull-overlap transition
 ranges=[(F(5108,10000),F(1,10**5)),(F(5105,10000),F(2,10**6)),(F(51,100),F(1,10**8))]
 print(json.dumps(dict(minimum_r=R,first_gap_depth=3,long_digit_cut=M,records=[certify(x-e,x+e) for x,e in ranges]),indent=2))
