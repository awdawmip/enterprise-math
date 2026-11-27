"""Exact standard-library replay of the finite PREFIX-1141 auxiliary certificate.
Input: fixture1141.json (outward vertex cells + original observer rows).
No floating point is used to decide any assertion.
"""
from fractions import Fraction as F
from itertools import product
from math import ceil, floor, gcd
from pathlib import Path
import json
D=json.loads(Path(__file__).with_name('fixture1141.json').read_text())
G,L,q0=D['G'],D['L'],D['q0'];K,H,aj,am,dj,r,u=[F(D[k]) for k in ('K','H','aj','am','dj','r0','u')];d0=F(D['d'][0]);V=D['V'];m=D['m'];cols=D['cols'];e=D['e']
assert G==10**125 and L==10**114 and H==2*K

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def solve(A,b):
 M=[list(map(F,r))+[F(v)] for r,v in zip(A,b)];n=len(M)
 for j in range(n):
  k=next(k for k in range(j,n) if M[k][j]);M[j],M[k]=M[k],M[j];z=M[j][j];M[j]=[x/z for x in M[j]]
  for k in range(n):
   if k!=j:
    z=M[k][j];M[k]=[x-z*y for x,y in zip(M[k],M[j])]
 return [row[-1] for row in M]

def hull(pts):
 pts=sorted(set(pts))
 def turn(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
 def half(pts):
  h=[]
  for p in pts:
   while len(h)>=2 and turn(h[-2],h[-1],p)<=0:h.pop()
   h.append(p)
  return h
 return half(pts)[:-1]+half(pts[::-1])[:-1]
S=int(D['Pgrid_scale']);assert S==10**140
P=hull([(r+F(a+i,S),u+F(b+j,S)) for a,b in D['Pgrid'] for i,j in product((0,1),repeat=2)])
W=list(zip(*(solve(V,[int(j==i) for j in range(3)]) for i in range(3))))
assert all(t.denominator==1 for row in W for t in row);assert all(dot(a,b)==(i==j) for i,a in enumerate(V) for j,b in enumerate(zip(*W)))
Q=2*10**69;box=[]
for a,b,c in V:
 lo=min(a+b*x+c*y for x,y in P)+min(0,-b*K/L**2)+min(0,c*H/L);hi=max(a+b*x+c*y for x,y in P)+max(0,-b*K/L**2)+max(0,c*H/L)
 box.append((ceil(min(q0*lo,Q*lo)),floor(max(q0*hi,Q*hi))))
assert box==[(0,0),(-2,0),(1,18)]
dirs=[(v-y,x-w) for (x,y),(w,v) in zip(P,P[1:]+P[:1])]+[(1,0),(-1,0),(0,1),(0,-1)]
ineq=[(a,b,max(a*x+b*y for x,y in P)+max(0,-a)*K/L**2+max(0,b)*H/L) for a,b in dirs]
lines=[];count=0
for n in product(*(range(a,b+1) for a,b in box)):
 q,p,h=[int(dot(w,n)) for w in W]
 if q0<=q<=Q and all(a*p+b*h<=q*z for a,b,z in ineq):
  count+=1
  if gcd(p,q)==1:lines.append((q,p,h))
lines.sort();assert count==25 and len(lines)==8
U=cols+[[e[i] if i==j else 0 for i in range(10)] for j in range(10)]
n=list(map(int,D['normal']));a=-G*(n[0]*aj+n[1]*dj);b=G*n[1]*am;z=dot(n,m);sup=sum(abs(dot(n,v)) for v in U);q,p,h=lines[0];val=a*(F(p,q)-r)+b*(F(h,q)-u)-z
ratio=max(val/(sup+max(0,-a)*K/L**2+max(0,b)*H/L),-val/(sup+max(0,a)*K/L**2+max(0,-b)*H/L));assert ratio>F(105,100);assert any(dot(n,c) for c in cols[:6]);print('strict separation',float(ratio))
piv=D['pivot'];free=[i for i in range(22) if i not in piv];A=[[U[j][i] for j in piv] for i in range(10)]
assert len(D['free_ints'])==7
for (q,p,h),nums in zip(lines[1:],D['free_ints']):
 x,y=F(p,q)-r,F(h,q)-u;tgt=[-G*aj*x,G*(am*y-dj*x)]+[F(0)]*8
 z=[F(0)]*22
 for j,t in zip(free,nums):z[j]=F(t,10**12)
 b0=[tgt[i]-m[i]-sum(z[j]*U[j][i] for j in free) for i in range(10)]
 for j,t in zip(piv,solve(A,b0)):z[j]=t
 assert all(m[i]+sum(z[j]*U[j][i] for j in range(22))==tgt[i] for i in range(10))
 slack=1-max(map(abs,z));assert slack>F(12,100);print(q,'exact interior slack',float(slack))
q=lines[1][0];L3=L2=10**8
while L3<=d0*q*q/(4*400000):L3*=2
while L2<q*q:L2*=2
assert q==1165623432270214220404883113745300873367119564109373807481147732125067
print('new denominator lower bound',q,'first unexcluded',float(L3),float(L2))
print('PASS: outward grid complete enumeration and exact full-observer certificates')
