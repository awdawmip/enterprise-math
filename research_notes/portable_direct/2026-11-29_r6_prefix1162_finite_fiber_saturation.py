# Reproduce the finite saturation theorem from the PREFIX-1161 archive.
from fractions import Fraction as F
from itertools import combinations
from math import gcd,lcm
import json
import fiber1154 as f
import scale1160 as s
from check_extra_core import normal,dot
D=json.load(open('grid1161.json'));G=D['G'];f.m,f.e,f.C=[D[k] for k in ('m','e','cols')]
f.A=[-G*f.aj,-G*f.dj]+[0]*13;f.B=[0,G*f.am]+[0]*13
f.U=f.C+[[f.e[i] if i==j else 0 for i in range(15)] for j in range(15)]
old=json.load(open('section1161.json'));s.P=[tuple(map(F,v)) for v in old['vertices']]
r,V=s.search(10**148,10**94,old['runs'][-1]['V']);ls=r['records']
assert r['independent_checked']==187 and len(ls)==116
assert ls[0][0]==3772445413589803964864238812178282480338202865472119599071419685810699454648106071600757936751
_,_,ns,_,_=f.maxvol(f.U)
for I in combinations((0,1,9,10,11,12,13,14),7):
 n0=normal([[c[i] for i in I] for c in f.C[:6]]);assert n0;n=[0]*15
 for i,x in zip(I,n0):n[i]=x
 assert all(dot(n,c)==0 for c in f.C[:6]);ns.append(n)
NN=[]
for n in ns:
 d=lcm(*(F(x).denominator for x in n));n=[int(x*d) for x in n];g=gcd(*n);n=[x//g for x in n]
 for sign in (1,-1):
  v=[sign*x for x in n];a,b,z=dot(v,f.A),dot(v,f.B),dot(v,f.m);S=sum(abs(dot(v,c)) for c in f.U);NN.append((v,a,b,z,S))
allruns=[]
for L,count in [(10**148,0),(2*10**148,41),(5*10**148,67),(10**149,76),(10**150,83),(10**152,85)]:
 cs=[]
 for n,a,b,z,S in NN:
  t=-(z+a*f.r+b*f.u+S+max(0,-a)*f.K/L**2+max(0,b)*f.H/L)
  d=lcm(*(F(x).denominator for x in (t,a,b)));cs.append([int(x*d) for x in (t,a,b)])
 left=[];excluded=[]
 for line in ls:
  i=next((i for i,c in enumerate(cs) if dot(c,line)>0),None)
  if i is None:left.append(line)
  else:excluded.append([line,i])
 assert len(excluded)==count
 allruns.append(dict(L=L,remaining=left,excluded=excluded));print('PASS scale',L,'excluded',count,flush=True)
f.lines=left;out=f.solve(False)
assert len(out['records'])==31 and all(t['kind']=='feasible' and F(t['slack'])>F(68,10000) for t in out['records'])
# Independent direct witness checks, with no dependence on LP solver status.
for t in out['records']:
 q,p,h=map(int,t['line']);z=list(map(F,t['z']));v=[a*(F(p,q)-f.r)+b*(F(h,q)-f.u)-c for a,b,c in zip(f.A,f.B,f.m)]
 assert max(map(abs,z))<1 and [dot(z,row) for row in zip(*f.U)]==v
json.dump(dict(search=r,normals=[n for n,*_ in NN],runs=allruns,fibers=out),open('verify1162.json','w'))
print('PASS exact saturation: 85 monotone exclusions and 31 zero-scale witnesses')
