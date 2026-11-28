from fractions import Fraction as F
from itertools import combinations,product
from math import floor,ceil,gcd,lcm
import json
from check_extra_core import normal,dot
D=json.load(open('fixture1141.json')); K,H,r,u,aj,am,dj=map(F,(D['K'],D['H'],D['r0'],D['u'],D['aj'],D['am'],D['dj'])); q0=int(D['q0']); dlo=F(D['d'][0]); E=400000
O=json.load(open('grid1157.json')); G0=O['G']; G=10**150; N=15; assert G0==10**145
pkt=json.load(open('anchor_compact.json')); cc=[F(int(v),10**120) for v in pkt['center']]; W0=[[F(int(v),10**140) for v in row] for row in pkt['weighted_columns_rows']]; dr=[F(int(v),10**140) for v in pkt['rounding_radii']]
assert max(abs(cc[i])+sum(map(abs,W0[i]))+dr[i] for i in range(6))<1
m=[v*(G//G0) for v in O['m'][:2]]; e=[v*(G//G0) for v in O['e'][:2]]; C=[[v*(G//G0) for v in c[:2]] for c in O['cols']]
raw=json.load(open('refine1148.json'))['rows']; rows=sum([json.load(open(p)) for p in ['radial1146_low.json','coupled1146.json','radial1146_high.json','extra_radial1144_tight.json','extra_coupled1144_tight.json']],[]); assert len(rows)==len(raw)==13
for i,(rec,R) in enumerate(zip(rows,raw),2):
 k,j=rec['k'],rec.get('channel',0); assert (k,j)==(R['k'],R['channel']); row=list(map(F,rec['row'])); center=dot(row,cc)-F(2*int(R['raw'])+1,2*10**150); cols=[sum(row[i]*W0[i][l] for i in range(6)) for l in range(6)]+[row[i]*dr[i] for i in range(6)]
 err=(F(6**(j+1),j+1) if j else F(1))*F(35,36)**k+F(1,2*10**150)+F(1,10**180)+F(1205,10**155)
 assert floor(center*G0)==O['m'][i] and [floor(x*G0) for x in cols]==[c[i] for c in O['cols']] and ceil(err*G0)+13==O['e'][i]
 m.append(floor(center*G));e.append(ceil(err*G)+13)
 for c,x in zip(C,cols):c.append(floor(x*G))
assert all(O['e'][i]*(G//G0)==100000*e[i] for i in range(10,15))
U=C+[[e[i] if i==j else 0 for i in range(N)] for j in range(N)]; A=[-G*aj,-G*dj]+[0]*13;B=[0,G*am]+[0]*13; L=10**134
s=[-a*K/(2*L**2) for a in A];t=[b*H/(2*L) for b in B]; Us=U+[s,t]
def solve(M,b):
 M=[list(map(F,row))+[F(x)] for row,x in zip(M,b)];n=len(M)
 for i in range(n):
  j=next(j for j in range(i,n) if M[j][i]);M[i],M[j]=M[j],M[i];x=M[i][i];M[i]=[v/x for v in M[i]]
  for j in range(n):
   if i!=j:
    x=M[j][i];M[j]=[v-x*w for v,w in zip(M[j],M[i])]
 return [row[-1] for row in M]
def normals(U,piv):
 ns=[solve([U[j] for j in piv],[int(i==j) for j in range(N)]) for i in range(N)];assert all(dot(n,U[j])==(i==k) for i,n in enumerate(ns) for k,j in enumerate(piv));return ns
piv=[5,0,14,15,16,17,18,19,20,21,3,28,1,4,2];ns=normals(Us,piv)
P0=[(F(x)+r,F(y)+u) for x,y in json.load(open('section1158.json'))['vertices']];J=[(v-y,x-w,(v-y)*x+(x-w)*y) for (x,y),(w,v) in zip(P0,P0[1:]+P0[:1])];assert all(a*x+b*y<=z for a,b,z in J for x,y in P0)
for I in combinations((0,1,9,10,11,12,13,14),7):
 n0=normal([[c[i] for i in I] for c in C[:6]]);assert n0;n=[0]*N
 for i,x in zip(I,n0):n[i]=x
 assert all(dot(n,c)==0 for c in C[:6]);ns.append(n)
for n in ns:
 a,b=dot(n,A),dot(n,B);z=dot(n,m)+a*r+b*u;S=sum(abs(dot(n,c)) for c in U)
 if a or b:J.extend([(a,b,z+S),(-a,-b,S-z)])
P=set()
for (a,b,z),(c,d,t0) in combinations(J,2):
 det=a*d-b*c
 if det:
  x,y=(z*d-b*t0)/det,(a*t0-z*c)/det
  if all(aa*x+bb*y<=zz for aa,bb,zz in J):P.add((x,y))
assert len(P)==16
width=[max(x[i] for x in P)-min(x[i] for x in P) for i in range(2)];assert width[0]<F(2272,10**136) and width[1]<F(1090,10**135)
V=[[106115122536399327323867092716187254834877071,-460663226548771243745356434662724990844971749,98551763062280074016778043506393595428730902],[2552298759210102861034033967170503590581220488,204272655898547410803128641414352409314729495,-69919723150359588275908309850946004628124737],[-7035909179931678596066160941500995759063483192,126818222752599626565440632755001029391932785,43543250247717353528464190323844986897733080]]
W=list(zip(*(solve(V,[int(i==j) for j in range(3)]) for i in range(3))));assert all(x.denominator==1 for row in W for x in row);W=[list(map(int,row)) for row in W];assert all(dot(a,b)==(i==j) for i,a in enumerate(V) for j,b in enumerate(zip(*W)))
HP=[(x-d,y+f) for (x,y),d,f in product(P,(0,K/L**2),(0,H/L))];J1=[(a,b,max(a*x+b*y for x,y in HP)) for a,b,_ in J]+[(a,b,max(a*x+b*y for x,y in HP)) for a,b in ((1,0),(-1,0),(0,1),(0,-1))]
Q=10**89;box=[]
for a,b,c in V:
 vals=[q*(a+b*x+c*y) for q,(x,y) in product((q0,Q),HP)];box.append((ceil(min(vals)),floor(max(vals))))
assert box==[(0,1),(-4,-1),(-5,3)]
ls=[];pts=0
for n in product(*(range(a,b+1) for a,b in box)):
 q,p,h=[dot(w,n) for w in W]
 if q0<=q<=Q and all(a*p+b*h<=z*q for a,b,z in J1):
  pts+=1
  if gcd(q,p)==1:ls.append((q,p,h))
ls.sort();assert pts==13 and len(ls)==5 and ls[0][0]==68790978239103168622833661446969269397288471328988298766514185061790924582086475186280559
print('PASS 72 box points, 13 feasible, 5 primitive',float(width[0]),float(width[1]))
p0=[5,0,14,15,16,17,18,19,20,21,3,23,1,4,2];zn=normals(U,p0);sn=normals(Us,piv); free=[j for j in range(29) if j not in piv]
values=[(842693309878,[-1,1,1,-1,-1,-1,-1,-1,1,-1,1,-1,1,-1]),(184516337015,[-1,1,1,1,-1,1,-1,-1,1,-1,1,1,-1,-1]),(631334591320,[1,-1,-1,1,-1,1,-1,-1,-1,1,-1,1,-1,-1]),(884727877463,[1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1]),(964025818607,[1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1])]
for (q,p,h),(mag,signs) in zip(ls,values):
 v=[a*(F(p,q)-r)+b*(F(h,q)-u)-c for a,b,c in zip(A,B,m)]; n=max(zn,key=lambda n:abs(dot(n,v))/sum(abs(dot(n,c)) for c in U));d=dot(n,v);n=[x*(1 if d>0 else -1) for x in n];d=abs(d);S=sum(abs(dot(n,c)) for c in U);assert d>11000*S
 aa=max(0,-dot(n,A))*K/L**2;bb=max(0,dot(n,B))*H/L;assert 9*(d-S)>3*bb+aa
 target=[x-y-z for x,y,z in zip(v,s,t)];co=[F(0)]*29
 for j,sign in zip(free,signs):co[j]=F(mag*sign,10**12)
 rem=[target[i]-sum(co[j]*Us[j][i] for j in free) for i in range(N)]
 for j,n0 in zip(piv,sn):co[j]=dot(n0,rem)
 assert [dot(co,row) for row in zip(*Us)]==target and 1-max(map(abs,co))>F(35,1000)
 print('PASS candidate',q,'slack',float(1-max(map(abs,co))))
oldq=858356652145570229340015752537013296844119325710283911057636179903360525779249418264558
old3=old2=new3=new2=10**8
while old3<=dlo*oldq**2/(4*E):old3*=2
while old2<oldq**2:old2*=2
assert min(old3,old2)>3*L
while new3<=dlo*Q**2/(4*E):new3*=2
while new2<Q**2:new2*=2
assert new3//old3==new2//old2==16384
print('PASS L>=3e134 q>1e89, windows',new3,new2)
