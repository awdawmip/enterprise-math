from fractions import Fraction as F
from itertools import product
from math import ceil,floor,gcd,lcm,prod
from pathlib import Path
import json
from check_extra_core import dot,det
# Reconstruct 43-direction section from frozen source, not merely saved vertices.
ns={};exec(Path('point_section_targeted1138.py').read_text().split('# verify previous basis')[0],ns)
P=ns['P'];r0=ns['r0'];u=ns['cref'];d=ns['d'];q0=544447235321021556325566186117974922693;E=400000;K=d[1]+F(2*E,q0);H=2*K
old=json.load(open('extend_targeted1138.json'));V=old['V'];W=old['W'];assert abs(det(V))==1 and [[dot(v,w) for w in zip(*W)] for v in V]==[[1,0,0],[0,1,0],[0,0,1]]
hullns={};exec('def hull(pts):'+Path('verify_section.py').read_text().split('def hull(pts):')[1].split('P=hull(pts)')[0],hullns);hull=hullns['hull']
def edges(poly):
 out=[]
 for (x,y),(v,w) in zip(poly,poly[1:]+poly[:1]):
  a=w-y;b=x-v;z=a*x+b*y;assert all(a*r+b*t<=z for r,t in poly);out.append((a,b,z))
 return out
# Minkowski sum support normal set is the union of edge normals, including rectangle axes.
base=hull([(x+r0,y+u) for x,y in P]);supports=edges(base)+[(F(a),F(b),max(a*x+b*y for x,y in base)) for a,b in [(1,0),(-1,0),(0,1),(0,-1)]]
def integral(a):
 den=lcm(*(x.denominator for x in a));v=[int(x*den) for x in a];g=gcd(*v);return tuple(x//g for x in v) if g else tuple(v)
def scan(L,Q):
 HP=hull([(r-x,c+y) for (r,c),x,y in product(base,(0,K/L**2),(0,H/L))]);ineq=edges(HP)
 box=[]
 for a,b,f in V:
  vs=[q*(a+b*r+f*c) for q,(r,c) in product((q0,Q),HP)];box.append((ceil(min(vs)),floor(max(vs))))
 # Exact inequalities in n, of form A*n<=B. Select two smallest axes to loop over.
 cs=[(tuple(W[0]),Q),(tuple(-x for x in W[0]),-q0)]
 for a,b,z in ineq:cs.append((integral([a*W[1][i]+b*W[2][i]-z*W[0][i] for i in range(3)]),0))
 i,j,k=sorted(range(3),key=lambda i:box[i][1]-box[i][0]);ans=[];tested=0;outer=0
 for x,y in product(range(box[i][0],box[i][1]+1),range(box[j][0],box[j][1]+1)):
  outer+=1;lo,hi=box[k]
  for a,b in cs:
   rhs=b-a[i]*x-a[j]*y
   if a[k]>0:hi=min(hi,rhs//a[k])
   elif a[k]<0:lo=max(lo,-((-rhs)//a[k]))
   elif rhs<0:break
   if lo>hi:break
  else:
   for z in range(lo,hi+1):
    n=[0]*3;n[i]=x;n[j]=y;n[k]=z;q,p,h=map(lambda w:dot(w,n),W);tested+=1
    assert q0<=q<=Q and all(a*p+b*h<=z*q for a,b,z in ineq)
    if gcd(p,q)==1:ans.append((q,p,h))
 ans.sort();print('L',len(str(L))-1,'Q',f'{float(Q):.3g}','box',box,'vol',prod(max(0,b-a+1) for a,b in box),'outer',outer,'tested',tested,'primitive',len(ans),'min',ans[:1],flush=True)
 return ans,dict(L=str(L),Q=str(Q),box=box,outer=outer,tested=tested,lines=[list(map(str,l)) for l in ans])
def feasible(line,L):
 q,p,h=line
 return all((a*p+b*h-z*q)*L**2<=q*(max(0,-a)*K+max(0,b)*H*L) for a,b,z in supports)
runs=[]
for L,Q in [(10**104,10**68),(10**114,10**68),(10**114,3*10**68),(10**114,10**69),(10**140,10**69)]:
 ans,rr=scan(L,Q);runs.append(rr)
 if L==10**104:small=ans
 if L==10**140:tail=ans
# Exact integer cutoff on each smaller-scale line, using monotonically shrinking region.
cut=[]
for line in small:
 assert feasible(line,10**104) and not feasible(line,10**114)
 l,r=10**104,10**114
 while r-l>1:
  m=(l+r)//2
  if feasible(line,m):l=m
  else:r=m
 assert feasible(line,l) and not feasible(line,l+1)
 cut.append(dict(line=list(map(str,line)),last_L=str(l),first_excluded=str(r)));print('cutoff',f'{float(l):.12g}',str(l),flush=True)
# Tail minimum (if no survivors, use strict Q lower bound). Retain earlier tail if no improvement.
q=tail[0][0] if tail else 10**69
print('tail minimum',q,flush=True)
# L>=1e114 scan gives safe global tail (cannot apply L>=1e140 only to smaller L).
last=runs[-2];qt=int(last['lines'][0][0]) if last['lines'] else int(last['Q']);L3=L2=10**8
while L3<=d[0]*qt*qt/(4*E):L3*=2
while L2<qt*qt:L2*=2
print('new boundaries',L3,L2,flush=True)
json.dump(dict(V=V,W=W,runs=runs,cutoffs=cut,q=str(qt),L3=str(L3),L2=str(L2)),open('extend1139.json','w'),indent=2)
