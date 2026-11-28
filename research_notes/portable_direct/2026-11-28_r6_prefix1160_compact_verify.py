# Exact compact verifier; run inside extracted PREFIX-1159 evidence.
from fractions import Fraction as F
from itertools import combinations, product
from math import ceil, floor, gcd, lcm, prod
import json
import compact1159 as prev
from check_extra_core import normal, dot
D=prev.D; K,H,r,u,aj,am,dj=prev.K,prev.H,prev.r,prev.u,prev.aj,prev.am,prev.dj
G0=10**150; G=10**155; N=15
old=json.load(open('grid1159.json')); assert old['G']==G0
m=[x*(G//G0) for x in old['m'][:2]]; e=[x*(G//G0) for x in old['e'][:2]]; C=[[x*(G//G0) for x in c[:2]] for c in old['cols']]
for i,(rec,R) in enumerate(zip(prev.rows,prev.raw),2):
 k,j=rec['k'],rec.get('channel',0);assert (k,j)==(R['k'],R['channel']);row=list(map(F,rec['row']));center=dot(row,prev.cc)-F(2*int(R['raw'])+1,2*10**150)
 cols=[sum(row[t]*prev.W0[t][l] for t in range(6)) for l in range(6)]+[row[t]*prev.dr[t] for t in range(6)]
 tail=(F(6**(j+1),j+1) if j else F(1))*F(35,36)**k;err=tail+F(1,2*10**150)+F(1,10**180)+F(1205,10**155)
 assert floor(center*G0)==old['m'][i] and [floor(x*G0) for x in cols]==[c[i] for c in old['cols']] and ceil(err*G0)+13==old['e'][i]
 m.append(floor(center*G));e.append(ceil(err*G)+13)
 for c,x in zip(C,cols):c.append(floor(x*G))
 if i>=10:
  assert F(2733,100)<F(old['e'][i]*(G//G0),e[-1])<F(2734,100)
  assert F(976,1000)<F(50000,e[-1])<F(977,1000)
assert len(m)==15
U=C+[[e[i] if i==j else 0 for i in range(N)] for j in range(N)];A=[-G*aj,-G*dj]+[0]*13;B=[0,G*am]+[0]*13
piv=[5,0,14,15,16,17,18,19,20,21,3,23,1,4,2];ns=prev.normals(U,piv)
P0=[tuple(map(F,v)) for v in json.load(open('section1159.json'))['vertices']];assert {(x+r,y+u) for x,y in P0}==prev.P
J=[(v-y,x-w,(v-y)*x+(x-w)*y) for (x,y),(w,v) in zip(P0,P0[1:]+P0[:1])];assert all(a*x+b*y<=z for a,b,z in J for x,y in P0)
for I in combinations((0,1,9,10,11,12,13,14),7):
 n0=normal([[c[i] for i in I] for c in C[:6]]);assert n0;n=[0]*N
 for i,x in zip(I,n0):n[i]=x
 assert all(dot(n,c)==0 for c in C[:6]);ns.append(n)
for n in ns:
 a,b=dot(n,A),dot(n,B);z=dot(n,m);S=sum(abs(dot(n,c)) for c in U)
 if a or b:J.extend([(a,b,z+S),(-a,-b,S-z)])
P=set()
for (a,b,z),(c,d,t) in combinations(J,2):
 det=a*d-b*c
 if det:
  x,y=(z*d-b*t)/det,(a*t-z*c)/det
  if all(aa*x+bb*y<=zz for aa,bb,zz in J):P.add((x,y))
assert len(P)==16
width=[max(x[i] for x in P)-min(x[i] for x in P) for i in range(2)]
assert width[0]<F(2014,10**136) and width[1]<F(9658,10**136)
V=[[358371237814035307054199652553501795303904177990,-466222375538354462639725952456459584802674472506,97209556076298053451501367429727380103898952703],[6153784338506684855768678311308943188453852036921,-8005253293821539268783398699468988083271186591488,1669129046664158958810961759185055202945435695149],[-553593710017890686584436823969149184868162815186,720141792255007818225200603851538857806425896985,-150152522090592333296396879047994205998226712031]]
W=list(zip(*(prev.solve(V,[int(i==j) for j in range(3)]) for i in range(3))));assert all(x.denominator==1 for row in W for x in row);W=[list(map(int,row)) for row in W];assert all(dot(a,b)==(i==j) for i,a in enumerate(V) for j,b in enumerate(zip(*W)))
def search(L,Q):
 HP=[(x-d,y+f) for (x,y),d,f in product(P,(0,K/L**2),(0,H/L))];J1=[(a,b,max(a*x+b*y for x,y in HP)) for a,b,_ in J]+[(a,b,max(a*x+b*y for x,y in HP)) for a,b in ((1,0),(-1,0),(0,1),(0,-1))]
 # For the Minkowski sum of a polygon and a rectangle all facet normals are in this set.
 box=[]
 for a,b,c in V:
  vals=[q*(a+b*(x+r)+c*(y+u)) for q,(x,y) in product((prev.q0,Q),HP)];box.append((ceil(min(vals)),floor(max(vals))))
 def ints(row):
  d=lcm(*(F(x).denominator for x in row));return [int(x*d) for x in row]
 tests=[ints([-z-a*r-b*u,a,b]) for a,b,z in J1];ls=[];pts=0
 for n in product(*(range(a,b+1) for a,b in box)):
  q,p,h=[dot(w,n) for w in W]
  if prev.q0<=q<=Q and all(dot(t,(q,p,h))<=0 for t in tests):
   pts+=1
   if gcd(q,p)==1:ls.append((q,p,h))
 ls.sort();print('PASS search',L,Q,'box volume',prod(max(0,b-a+1) for a,b in box),'points',pts,'primitive',len(ls),'min',ls[0][0]);return pts,ls
qstar=1809754881531112186904694767481139172491414761359983491189786084567209150450511632496318670
pts,ls=search(10**142,3*10**91);assert pts==797 and len(ls)==477 and ls[0][0]==qstar
pts2,ls2=search(10**152,3*10**91);assert pts2==795 and len(ls2)==476 and ls2[0][0]==qstar
q,p,h=ls[0];target=[a*(F(p,q)-r)+b*(F(h,q)-u)-c for a,b,c in zip(A,B,m)]
free=[i for i in range(27) if i not in piv];co=[F(0)]*27
for j,sign in zip(free,[1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,1]):co[j]=F(443862349609*sign,10**12)
rem=[target[i]-sum(co[j]*U[j][i] for j in free) for i in range(N)]
for j,n in zip(piv,prev.normals(U,piv)):co[j]=dot(n,rem)
assert [dot(co,row) for row in zip(*U)]==target and 1-max(map(abs,co))>F(556,1000)
q,p,h=1453108788683279458746971083142301765111381877116130690887157247121933310897371353649740211,31154705788112223773941193274162285052614917219356422370971449644454981361766166766462689117,144062673585934501523940974670417541741550550033732020959109857080461500341712876561136219871
v=[a*(F(p,q)-r)+b*(F(h,q)-u)-c for a,b,c in zip(A,B,m)]
rat=[]
for n in prev.normals(U,piv):
 if dot(n,v)<0:n=[-x for x in n]
 S=sum(abs(dot(n,c)) for c in U);S+=max(0,-dot(n,A))*K/10**280+max(0,dot(n,B))*H/10**140
 rat.append(dot(n,v)/S)
print("oriented ratio",float(max(rat)));assert max(rat)>1
print('PASS previous zero-scale candidate excluded at L>=1e140, ratio',float(max(rat)))
a=b=c=d=10**8;dlo=prev.dlo;E=prev.E
while a<=dlo*10**178/(4*E):a*=2
while b<10**178:b*=2
assert min(a,b)>10**142
while c<=dlo*qstar*qstar/(4*E):c*=2
while d<qstar*qstar:d*=2
assert c//a==256 and d//b==512
print('PASS stitched windows',c,d,'factors',c//a,d//b)
