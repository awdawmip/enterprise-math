from pathlib import Path
exec(Path('root_joint_compact.py').read_text().split('# Point enclosure')[0])
from fractions import Fraction as F
from itertools import product
from math import isqrt,floor
import json
old=json.load(open('root_8800_result.json'));dj=tuple(F(int(v),10**85) for v in old['d']);d0=sum(dj)/2

jetgrid=[[ [grid_pair(v) for v in dp(p,j)] for p in pp] for j in range(3)]
jettail=[[sum(comb(j,k)*rowbound[k]*trr[j-k] for k in range(j+1)) for trr in tails] for j in range(3)]
def one(q,p,h):
 L=10**100
 rl,ru=F(p,q),F(p,q)+d0/L**2;cl,cu=F(h,q)-2*d0/L,F(h,q)
 l=isqrt(floor(36*G*G/(1+ru)));u=isqrt(floor(36*G*G/(1+rl)))+1
 tr=I(F(l,G),F(u,G));cs=I(cl,cu)
 assert tr.a**2<=36/(1+ru)<=36/(1+rl)<=tr.b**2
 def jets(j):
  out=[]
  for i in range(len(pp)):
   v=grid_horner(jetgrid[j][i],tr);e=jettail[j][i];out.append(v+I(-e,e))
  return out
 f0,f1,f2=(jets(j) for j in range(3))
 D=198/tr**2+216/(4-tr**2)+216/(16-tr**2);alpha=36/tr**2-2+(1-tr**2/36)*D/2;beta=9/tr-tr/4
 g0=[beta*v+(alpha-cs)*u for v,u in zip(f2,f1)]
 centers=[sum((a*v for a,v in zip(cc,row)),I(0)) for row in (f0,g0)]
 colI=[tuple(sum((row[i]*inv[i][j] for i in range(6)),I(0)) for row in (f0,g0)) for j in range(6)]
 colI += [tuple(row[i]*dr[i] for row in (f0,g0)) for i in range(6)]
 def mid(v):return (v.a+v.b)/2
 def radv(v):return (v.b-v.a)/2
 cent=tuple(map(mid,centers));cols=[tuple(map(mid,v)) for v in colI]
 error=tuple(radv(centers[i])+sum(radv(v[i]) for v in colI) for i in range(2))
 def dot(a,b):return sum(x*y for x,y in zip(a,b))
 ns=[]
 for u,v in cols+[(F(1),F(0)),(F(0),F(1))]:
  if u or v:
   m=max(abs(u),abs(v));ns.append((-v/m,u/m))
 margin=min(sum(abs(dot(n,z)) for z in cols)-abs(dot(n,cent))-dot(tuple(map(abs,n)),error) for n in ns)
 # keep result, including any nonpositive margin
 sc=sum((a*v for a,v in zip(cc,f1)),I(0));sr=sum(rad[i]*v.mag() for i,v in enumerate(f1));slope=sc+I(-sr,sr);assert slope.b<0
 
 result=dict(q=str(q),p=str(p),h=str(h),L=str(L),rho=[str(rl),str(ru)],c=[str(cl),str(cu)],t=[str(tr.a),str(tr.b)],cent=[str(a) for a in cent],cols=[[str(a) for a in v] for v in cols],error=[str(a) for a in error],margin=str(margin),slope=[str(slope.a),str(slope.b)])

 return result
lines=json.load(open('prefix1128_result.json'))['runs'][-1]['lines']
assert len(lines)==115
with open('direct_all.jsonl','w') as out:
 for i,line in enumerate(lines):
  rr=one(*map(int,line));out.write(json.dumps(rr,separators=(',',':'))+'\n');out.flush()
  print(i+1,float(F(rr['margin'])),flush=True)
