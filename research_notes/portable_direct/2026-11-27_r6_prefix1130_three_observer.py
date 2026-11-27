from pathlib import Path
exec(Path('root_joint_compact.py').read_text().split('# Point enclosure')[0])
from itertools import combinations, product
from math import isqrt,floor
import json,sys
old=json.load(open('root_8800_result.json')); dj=tuple(F(int(v),10**85) for v in old['d']); d0=sum(dj)/2
jetgrid=[[[grid_pair(v) for v in dp(p,j)] for p in pp] for j in range(5)]
jettail=[[sum(comb(j,k)*rowbound[k]*trr[j-k] for k in range(j+1)) for trr in tails] for j in range(5)]
def mid(v):return (v.a+v.b)/2
def radv(v):return (v.b-v.a)/2
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def muljet(a,b):return [sum(a[j]*b[i-j] for j in range(i+1)) for i in range(5)]
def binomhalf(n):return prod(F(1,2)-i for i in range(n))/factorial(n)
# map F derivatives to auxiliary density derivatives, discarding F(t) term only on root fiber
# row_j = derivative j, not Taylor coefficient

def rows_at(tr):
 R=tr*tr; b=R/36; u=[I(0)]+[tr*binomhalf(i)*(36/R)**i for i in range(1,5)]
 pw=[I(1)]+[I(0)]*4; poly=[comb(3,i)*R**(3-i)*36**i if i<=3 else I(0) for i in range(5)]
 for v in (4,16):poly=muljet(poly,[comb(i+2,2)*36**i/(v-R)**(i+3) for i in range(5)])
 # precompute linear transformation from F derivatives to density derivatives
 trans=[]
 for j in range(5):
  trans.append([v*factorial(k)/factorial(j) for k,v in enumerate(muljet(poly,pw))]);pw=muljet(pw,u)
 fs=[[grid_horner(jetgrid[j][i],tr)+I(-jettail[j][i],jettail[j][i]) for i in range(6)] for j in range(5)]
 rows=[[sum((trans[j][k]*fs[j][i] for j in range(1,k+1)),I(0)) for i in range(6)] for k in range(5)]
 return b,fs,rows

def obs(rows):
 centers=[sum((a*v for a,v in zip(cc,row)),I(0)) for row in rows]
 colI=[tuple(sum((row[i]*inv[i][j] for i in range(6)),I(0)) for row in rows) for j in range(6)] + [tuple(row[i]*dr[i] for row in rows) for i in range(6)]
 return tuple(map(mid,centers)),[tuple(map(mid,v)) for v in colI],tuple(radv(centers[i])+sum(radv(v[i]) for v in colI) for i in range(len(rows)))

def one(q,p,h):
 L=10**114
 rl,ru=F(p,q),F(p,q)+dj[1]/L**2;cl,cu=F(h,q)-2*dj[1]/L,F(h,q)
 l=isqrt(floor(36*G*G/(1+ru)));u=isqrt(floor(36*G*G/(1+rl)))+1
 tr=I(F(l,G),F(u,G));cs=I(cl,cu)
 assert tr.a**2<=36/(1+ru)<=36/(1+rl)<=tr.b**2
 assert t.a<=tr.a<=tr.b<=t.b
 b,fs,rows=rows_at(tr);v=b*(1-b);ell=1-2*b;A=1-b*(cs+2)
 # impose r2=-2A/v on common root fiber; third row eliminates r2 using this equality
 row1=fs[0];row2=[v*R2+2*A*R1 for R2,R1 in zip(rows[2],rows[1])]
 base=-(cs+2)*A-A/v*(A*ell-(cs+3)*v+A*A)
 a3=v*(2*ell+3*A)/6;a4=v*v/8
 m,C,e=obs([row1,row2]);
 # select an interior point on the nominal 2D fiber by scaling the radial boundary.
 # Try two columns first; else enumerate all choices with the remaining columns at endpoints
 def det(a,b):return a[0]*b[1]-a[1]*b[0]
 target=tuple(-x for x in m)
 # radial intersection with edge: t*target=sum fixed signs + z*column
 best=None
 for j,col in enumerate(C):
  if not any(col):continue
  n=(-col[1],col[0]);den=dot(n,target)
  if not den:continue
  support=sum(abs(dot(n,w)) for w in C);scale=support/abs(den)
  if best is None or scale<best[0]:best=(scale,j,n if den>0 else tuple(-x for x in n))
 scale,j,n=best;assert scale>1
 z=[F(1 if dot(n,w)>0 else -1 if dot(n,w)<0 else 0) for w in C]
 # parallel columns may exist; distribute residual proportionally to signs in a nonzero coordinate
 k=0 if C[j][0] else 1
 parallel=[i for i,w in enumerate(C) if dot(n,w)==0 and w[k]]
 rem=scale*target[k]-sum(z[i]*C[i][k] for i in range(12));tot=sum(abs(C[i][k]) for i in parallel)
 assert abs(rem)<=tot
 for i in parallel:z[i]=rem/tot*(1 if C[i][k]>0 else -1)
 z=[u/scale for u in z];assert max(map(abs,z))<1
 assert all(m[k]+sum(z[i]*C[i][k] for i in range(12))==0 for k in range(2))
 coeff=[cc[i]+sum(inv[i][j]*z[j] for j in range(6))+dr[i]*z[6+i] for i in range(6)]
 D1=sum(a*mid(w) for a,w in zip(coeff,rows[1]));D3=sum(a*mid(w) for a,w in zip(coeff,rows[3]));D4=sum(a*mid(w) for a,w in zip(coeff,rows[4]));assert D1<0
 # d reference is computed from this nominal interior point, then rounded to 10^-150.
 d=F(floor((mid(base)+(mid(a3)*D3+mid(a4)*D4)/D1)*10**150),10**150)
 assert dj[0]<d<dj[1]
 row3=[(base-d)*R1+a3*R3+a4*R4 for R1,R3,R4 in zip(rows[1],rows[3],rows[4])]
 m,C,e=obs([row1,row2,row3]);ns=[cross(x,y) for x,y in combinations(C,2)];ns=[tuple(a/max(map(abs,w)) for a in w) for w in ns if any(w)]
 assert any(dot(n,col) for n in ns for col in C)
 margin=min(sum(abs(dot(n,col)) for col in C)-abs(dot(n,m))-dot(tuple(map(abs,n)),e) for n in ns)
 s=sum((a*w for a,w in zip(cc,rows[1])),I(0));sr=sum(r*w.mag() for r,w in zip(rad,rows[1]));s=s+I(-sr,sr);assert s.b<0
 return dict(q=str(q),p=str(p),h=str(h),d=str(d),L=str(L),rho=[str(rl),str(ru)],c=[str(cl),str(cu)],t=[str(tr.a),str(tr.b)],m=list(map(str,m)),cols=[list(map(str,w)) for w in C],error=list(map(str,e)),margin=str(margin),slope=[str(s.a),str(s.b)])
lines=json.load(open('prefix1128_result.json'))['runs'][-1]['lines'];assert len(lines)==115
count=int(sys.argv[1]) if len(sys.argv)>1 else 1
with open('three_result.jsonl','w') as out:
 for i,line in enumerate(lines[:count]):
  rr=one(*map(int,line));out.write(json.dumps(rr,separators=(',',':'))+'\n');out.flush();print(i+1,float(F(rr['margin'])),float(F(rr['d'])),flush=True)
