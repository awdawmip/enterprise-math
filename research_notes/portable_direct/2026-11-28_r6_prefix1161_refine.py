from fractions import Fraction as F
from math import floor,ceil
from itertools import combinations
import json
import fiber1154 as f
import scale1160 as s
from check_extra_core import normal,dot
from replay_9600_n300_gmp import basis,N,integ,IV
assert N==300 and sum(b[3] for b in basis)<F(1,10**180)
old=json.load(open('grid1160.json')); G0=old['G'];G=10**170;J=10**170;Hraw=10**165
pkt=json.load(open('anchor_compact.json'));cc=[F(int(x),10**120) for x in pkt['center']]; W0=[[F(int(x),10**140) for x in row] for row in pkt['weighted_columns_rows']];dr=[F(int(x),10**140) for x in pkt['rounding_radii']]
assert max(abs(cc[i])+sum(map(abs,W0[i]))+dr[i] for i in range(6))<1
m=[v*(G//G0) for v in old['m']];e=[v*(G//G0) for v in old['e']];C=[[v*(G//G0) for v in c] for c in old['cols']]
raw=json.load(open('refine1148.json'))['rows'];rows=sum([json.load(open(p)) for p in ['radial1146_low.json','coupled1146.json','radial1146_high.json','extra_radial1144_tight.json','extra_coupled1144_tight.json']],[]);assert len(rows)==len(raw)==13
ks=[(14400,0),(16000,0),(20000,0),(14400,1),(14400,2)];values=list(map(int,open('moments1161.txt').read().split()));assert len(values)==5
new=[]
def make_row(k,j,J):
 ints={i:integ(k,i,N+5) for i in (0,1)}
 def down(x):
  if isinstance(x,IV):x=x*1
  a,b=x;v=floor(a*J);assert v==floor(b*J);return F(v,J)
 rr=[]
 for a,z,h,err,T in basis:
  off=int(a);half=int(2*(a-off));rr.append(sum(down((c[0] if not j else c)*ints[half][off+n+bool(j)]) for n,c in enumerate(z if not j else h[j-1])))
 row=rr+[F(0)]*2
 if j:row[3+j]=down(ints[0][j])
 return row
for i,((k,j),v) in enumerate(zip(ks,values),10):
 rec,R=rows[i-2],raw[i-2];assert (k,j)==(R['k'],R['channel']);assert v//10**15==int(R['raw'])
 assert make_row(k,j,10**155)==list(map(F,rec['row']))
 row=make_row(k,j,J);center=dot(row,cc)-F(2*v+1,2*Hraw);cols=[sum(row[t]*W0[t][l] for t in range(6)) for l in range(6)]+[row[t]*dr[t] for t in range(6)]
 tail=(F(6**(j+1),j+1) if j else F(1))*F(35,36)**k;err=tail+F(1,2*Hraw)+F(1,10**180)+F(1205,J)
 m[i]=floor(center*G);e[i]=ceil(err*G)+13
 for c,x in zip(C,cols):c[i]=floor(x*G)
 ratio=F(old['e'][i]*(G//G0),e[i]);print('ROW',i,k,j,'ratio',float(ratio),flush=True);new.append(dict(i=i,k=k,channel=j,raw=str(v),row=list(map(str,row)),radius=e[i],ratio=str(ratio)))
json.dump(dict(G=G,m=m,e=e,cols=C,rows=new),open('grid1161.json','w'))
f.m,f.e,f.C=m,e,C;f.A=[-G*f.aj,-G*f.dj]+[0]*13;f.B=[0,G*f.am]+[0]*13;f.U=C+[[e[i] if i==j else 0 for i in range(15)] for j in range(15)]
L=10**142;f.scale=[[-a*f.K/(2*L**2) for a in f.A],[b*f.H/(2*L) for b in f.B]]
oldr=json.load(open('refined1160.json'));f.lines=oldr['runs'][2]['records'][:1]
zero=f.solve(False);signed=f.solve(True)
_,_,ns,_,swaps=f.maxvol(f.U);ns=ns.copy()
for I in combinations((0,1,9,10,11,12,13,14),7):
 n0=normal([[c[i] for i in I] for c in C[:6]]);assert n0;n=[0]*15
 for i,x in zip(I,n0):n[i]=x
 assert all(dot(n,c)==0 for c in C[:6]);ns.append(n)
P0=[tuple(map(F,v)) for v in oldr['vertices']];J0=s.edges(P0);P=P0[:]
def clip(P,a,b,z):
 out=[]
 for X,Y in zip(P,P[1:]+P[:1]):
  t=a*X[0]+b*X[1]-z;v=a*Y[0]+b*Y[1]-z
  if t<=0:out.append(X)
  if t*v<0:out.append(tuple(x+(y-x)*t/(t-v) for x,y in zip(X,Y)))
 return s.hull(out)
for n in ns:
 a,b=dot(n,f.A),dot(n,f.B);z=dot(n,m);S=sum(abs(dot(n,c)) for c in f.U)
 if a or b:
  for j in [(a,b,z+S),(-a,-b,S-z)]:J0.append(j);P=clip(P,*j);assert len(P)>=3
P2=set()
for (a,b,z),(c,d,t) in combinations(J0,2):
 det=a*d-b*c
 if det:
  x,y=(z*d-b*t)/det,(a*t-z*c)/det
  if all(aa*x+bb*y<=zz for aa,bb,zz in J0):P2.add((x,y))
assert set(P)==P2
width=lambda P:[max(x[i] for x in P)-min(x[i] for x in P) for i in range(2)]
print('SECTION',len(P),list(map(float,width(P))),[float(a/b) for a,b in zip(width(P0),width(P))],flush=True)
s.P=P;V=oldr['runs'][2]['V'];out=[]
for L,Q in [(10**142,3*10**91),(10**144,10**93),(10**146,10**94),(10**148,10**95),(10**152,10**96),(10**156,10**97)]:
 res,V=s.search(L,Q,V)
 if res:out.append(res)
 json.dump(dict(vertices=[[str(x),str(y)] for x,y in P],widths=[str(x) for x in width(P)],zero=zero,signed=signed,runs=out),open('section1161.json','w'))
