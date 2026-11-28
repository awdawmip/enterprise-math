from fractions import Fraction as F
from itertools import combinations, product
from math import ceil, floor, gcd, lcm, prod
import json
from check_extra_core import normal, dot
D=json.load(open('fixture1141.json')); L=int(D['L']); K,H,r,u,aj,am,dj=map(F,(D['K'],D['H'],D['r0'],D['u'],D['aj'],D['am'],D['dj']));q0=int(D['q0']); E=400000; dlo=F(D['d'][0]);assert L==10**114
O=json.load(open('grid1157.json'));G=O['G'];m,e,C=[O[t] for t in ('m','e','cols')];N=len(m); assert G==10**145 and N==15 and len(C)==12
U=C+[[e[i] if i==j else 0 for i in range(N)] for j in range(N)];A=[-G*aj,-G*dj]+[0]*(N-2);B=[0,G*am]+[0]*(N-2)
P=[(F(x)+r,F(y)+u) for x,y in json.load(open('section1154.json'))['vertices']]
J=[(v-y,x-w,(v-y)*x+(x-w)*y) for (x,y),(w,v) in zip(P,P[1:]+P[:1])]; assert all(a*x+b*y<=z for a,b,z in J for x,y in P)
# Only eight normals are needed. All 27 generator contributions are retained.
for I in combinations((0,1,9,10,11,12,13,14),7):
 n0=normal([[c[i] for i in I] for c in C[:6]]);assert n0
 n=[0]*N
 for i,x in zip(I,n0):n[i]=x
 assert all(dot(n,c)==0 for c in C[:6]);a,b=dot(n,A),dot(n,B);z=dot(n,m)+a*r+b*u;S=sum(abs(dot(n,c)) for c in U);J.extend([(a,b,z+S),(-a,-b,S-z)])
# Independent exact pairwise boundary intersection, not iterative clipping.
P=[]
for (a,b,z),(c,d,t) in combinations(J,2):
 det=a*d-b*c
 if det:
  x,y=(z*d-b*t)/det,(a*t-z*c)/det
  if all(aa*x+bb*y<=zz for aa,bb,zz in J):P.append((x,y))
P=sorted(set(P));assert len(P)==16
width=[max(v[i] for v in P)-min(v[i] for v in P) for i in range(2)]; assert width[0]<F(2715,10**132) and width[1]<F(13022,10**132)
print('vertices',len(P),'width',*map(float,width))
# Coordinates from the exact maximum-area observation basis reduction.
V=[[-41041470475681494275445681675933676933386453,24292255282177195512694310203934820363168577,-4839423894082973696109831936594342257135982],[215824778297921983430971791476835889278422880,-10331181974110378053908375973369128911033877,57253225150000317132441996129382054919420],[-95649339731287589915543164539074533658522813,-35247365832190514244550040752203753145161422,8587305633788587150841101955517637113029197]]
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
det=dot(V[0],cross(V[1],V[2]));assert abs(det)==1
W=[[det*x for x in row] for row in zip(cross(V[1],V[2]),cross(V[2],V[0]),cross(V[0],V[1]))];assert all(dot(v,w)==(i==j) for i,v in enumerate(V) for j,w in enumerate(zip(*W)))
# All old and eight new strip normals, enlarged by signed scale support. The true Minkowski sum is contained in this intersection; use exact Minkowski vertices for the box.
def search(l,Q):
 P1=[(x-d,y+f) for (x,y),d,f in product(P,(0,K/l**2),(0,H/l))];J1=[(a,b,max(a*x+b*y for x,y in P1)) for a,b,_ in J]+[(a,b,max(a*x+b*y for x,y in P1)) for a,b in ((1,0),(-1,0),(0,1),(0,-1))]
 def ints(row):
  d=lcm(*(F(x).denominator for x in row));row=[int(x*d) for x in row];g=gcd(*row);return [x//g for x in row] if g else row
 cs=[ints([a*W[1][i]+b*W[2][i]-z*W[0][i] for i in range(3)]) for a,b,z in J1];box=[]
 for a,b,c in V:
  vals=[q*(a+b*x+c*y) for q,(x,y) in product((q0,Q),P1)];box.append((ceil(min(vals)),floor(max(vals))))
 npts=0;ls=[]
 for n in product(*(range(x,y+1) for x,y in box)):
  q,p,h=[dot(w,n) for w in W]
  if q0<=q<=Q and all(dot(row,n)<=0 for row in cs):
   npts+=1
   if gcd(q,p)==1:ls.append((q,p,h))
 print('search',l,Q,box,npts,len(ls),flush=True);return sorted(ls)
q1=86698991798038315176050922901043031093643345222939680727576233093356971735647454491529
q2=406044965468180424331893298803987780123449435720896484343774664807727491767142580141989
q3=858356652145570229340015752537013296844119325710283911057636179903360525779249418264558
assert not search(10**130,3*10**85)
s1=search(10**130,10**86);assert len(s1)==1 and s1[0][0]==q1
assert not search(10**132,3*10**86)
s2=search(10**132,10**87);assert len(s2)==10 and s2[0][0]==q2
s3=search(10**134,10**87);assert len(s3)==1 and s3[0][0]==q3
assert search(10**152,10**87)==s3
# Reconstruct exact witnesses from a few integer free coefficients; no LP dependency.
def solve(M,b):
 M=[list(map(F,row))+[F(x)] for row,x in zip(M,b)];n=len(M)
 for i in range(n):
  j=next(j for j in range(i,n) if M[j][i]);M[i],M[j]=M[j],M[i];x=M[i][i];M[i]=[v/x for v in M[i]]
  for j in range(n):
   if i!=j:
    x=M[j][i];M[j]=[v-x*w for v,w in zip(M[j],M[i])]
 return [row[-1] for row in M]
p0=[5,0,14,15,16,17,18,19,20,3,22,23,1,4,2];p1=p0[:];p1[10]=28
def fiber(line,l,piv,freevals):
 q,p,h=line;cols=U[:];cen=m[:]
 if l:
  s=[-a*K/(2*l*l) for a in A];t=[b*H/(2*l) for b in B];cols+= [s,t];cen=[x+y+z for x,y,z in zip(cen,s,t)]
 tgt=[a*(F(p,q)-r)+b*(F(h,q)-u)-c for a,b,c in zip(A,B,cen)];free=[j for j in range(len(cols)) if j not in piv];assert len(free)==len(freevals);z=[F(0)]*len(cols)
 for j,x in zip(free,freevals):z[j]=F(x,10**12)
 v=solve([[cols[j][i] for j in piv] for i in range(N)],[tgt[i]-sum(z[j]*cols[j][i] for j in free) for i in range(N)])
 for j,x in zip(piv,v):z[j]=x
 assert [dot(z,row) for row in zip(*cols)]==tgt
 return 1-max(map(abs,z))
a=929857824078;b=857365496035;c=647178121591
s=fiber(s1[0],10**130,p1,[-a,-a,a,a,-a,a,-a,-a,a,-a,a,a,-a,-a]);assert s>F(7,100);print('q1 signed slack',float(s))
s=fiber(s3[0],None,p0,[b,b,-b,-b,b,-b,-b,-b,-b,-b,-b,b]);assert s>F(14,100);print('q3 zero slack',float(s))
s=fiber(s3[0],10**134,p1,[-c,-c,-c,-c,c,-c,-c,-c,-c,c,c,-c,c,-c]);assert s>F(35,100);print('q3 signed slack',float(s))
q,p,h=s1[0];v=[a*(F(p,q)-r)+b*(F(h,q)-u)-c for a,b,c in zip(A,B,m)];norms=[solve([U[j] for j in p0],[int(i==j) for j in range(N)]) for i in range(N)];n=max(norms,key=lambda n:abs(dot(n,v))/sum(abs(dot(n,c)) for c in U));d=dot(n,v);n=[x*(1 if d>0 else -1) for x in n];d=abs(d);S=sum(abs(dot(n,c)) for c in U);a,b=dot(n,A),dot(n,B);AA=max(0,-a)*K/10**260;BB=max(0,b)*H/10**130;f=lambda k:(d-S)*k*k-BB*k-AA
assert d>315*S and f(F(28688329,10**6))<0<f(F(28688330,10**6));print('q1 scale bracket 28.688329 28.688330')
# At all L>=29*10^130, no q<=10^86: nested domains and q1 separator.
old3=old2=new3=new2=10**8;oldQ=3*10**85
while old3<=dlo*oldQ**2/(4*E):old3*=2
while old2<oldQ**2:old2*=2
assert min(old3,old2)>10**134
while new3<=dlo*q3**2/(4*E):new3*=2
while new2<q3**2:new2*=2
assert new3//old3==1024 and new2//old2==512
print('windows',new3,new2,'factors',new3//old3,new2//old2)
