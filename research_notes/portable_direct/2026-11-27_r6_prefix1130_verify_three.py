import json,sys
from fractions import Fraction as F
from itertools import combinations
from math import floor,ceil,gcd

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def margins(m,C,e):
 ns=[cross(a,b) for a,b in combinations(C,2)];ns=[tuple(a/max(map(abs,n)) for a in n) for n in ns if any(n)]
 assert any(dot(n,c) for n in ns for c in C)
 return min(sum(abs(dot(n,c)) for c in C)-abs(dot(n,m))-dot(tuple(map(abs,n)),e) for n in ns)
def verify(r):
 G=10**r['digits']; m=tuple(F(x,G) for x in r['m']);C=[tuple(F(x,G) for x in c) for c in r['cols']];e=tuple(F(x,G) for x in r['error']);margin=margins(m,C,e);assert margin>F(2,10**92)
 q,p,h=map(int,r['line']);d=F(r['d']);L0=10**114;E=400000
 assert gcd(p,q)==1 and q<L0//3
 # check full rectangular scope using inherited interval for d
 dj=tuple(F(int(v),10**85) for v in json.load(open('root_8800_result.json'))['d']);assert dj[0]<d<dj[1]
 lines=json.load(open('prefix1128_result.json'))['runs'][-1]['lines'];assert len(lines)==115 and min(map(lambda l:int(l[0]),lines))==q and any(tuple(map(int,l))==(q,p,h) for l in lines)
 rl,ru=F(p,q),F(p,q)+dj[1]/L0**2;cl,cu=F(h,q)-2*dj[1]/L0,F(h,q)
 def dyad(predicate):
  L=10**8
  while not predicate(L):L*=2
  return L
 L3=dyad(lambda L:4*E*L>dj[0]*q*q);L2=dyad(lambda L:L>=q*q)
 def witness(L,tri):
  assert L>=L0;res=(-h*pow(p,-1,q))%q;z=2*L-1-((2*L-1-res)%q);a=z-(2 if tri else 1)*q;b=a+q
  assert L<=a<z<2*L
  lam=d*q*q/(2*a*b*z) if tri else F(0)
  rho=F(p,q)+d/(a*z);c=F(h,q)-d*(F(1,a)+F(1,z))+lam
  assert rl<=rho<=ru and cl<=c<=cu
  ms=[a,b,z] if tri else [a,z];rs=[]
  for m0 in ms:
   j=F(p*m0+h,q);assert j.denominator==1
   e0=rho*m0+c+d/m0-j;rs.append(e0);assert abs(e0)*m0*m0<=E
  assert rs==([lam,-lam,lam] if tri else [0,0]);assert tri or q*q<=L
  return max(abs(e0)*m0*m0/E for e0,m0 in zip(rs,ms))
 print('margin',float(margin),'L3',float(L3),'L2',float(L2),'triple budget',float(witness(L3,True)),'pair budget',float(witness(L2,False)))
 print('all assertions passed')
if __name__=='__main__':
 r=json.loads(open('three_result.jsonl').readline());G=10**125
 m=list(map(F,r['m']));C=[list(map(F,c)) for c in r['cols']];e=list(map(F,r['error']))
 assert margins(m,C,e)==F(r['margin']);assert F(r['slope'][1])<0
 out=dict(digits=125,line=[r[k] for k in ('q','p','h')],d=r['d'],m=[floor(x*G) for x in m],cols=[[floor(x*G) for x in c] for c in C],error=[ceil(x*G)+13 for x in e])
 json.dump(out,open('three_compact.json','w'),separators=(',',':'));verify(out)
