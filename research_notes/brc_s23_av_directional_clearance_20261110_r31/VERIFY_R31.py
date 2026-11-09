"""R31 exact certificate. Optional R27 TSVs provide independent 9,472-event audit."""
from bisect import bisect_right
from fractions import Fraction as F
import csv,sys
L=F(262204504569236716045286,10**24);U=L+F(1,10**24)
T=(L+U)/2;M=128;H=164
ages=list(range(1,62))+list(range(98,165))
def frac(x):return x-(x.numerator//x.denominator)
def near(x):return (x+F(1,2)).numerator//(x+F(1,2)).denominator
def cuts(t):return sorted((frac(s*t),s) for s in range(M))
def owner(t,z,c):return (bisect_right(c,(frac(z*t),M))-1)%M
def templates(t):
 c=cuts(t);d={i:[] for i in range(M)};arcs=[]
 for r in range(1,H+1):
  o=owner(t,-r,c);x=frac(-r*t);p,ls=c[o];q,rs=c[(o+1)%M]
  d[o].append(r);arcs.append((r,ls,rs,frac(x-p),frac(q-x)))
 return c,d,arcs
def risk(t,n):
 a=sorted((frac(i*t),i) for i in range(n));c=cuts(t);mx=[F(0)]*M
 for k,(p,_) in enumerate(a):
  q=a[(k+1)%n][0]+(1 if k+1==n else 0)
  h=frac((p+q)/2);o=(bisect_right(c,(h,M))-1)%M
  mx[o]=max(mx[o],q-p)
 return 1-sum(mx)
for d in range(1,M+H):assert (d*L).__floor__()==(d*U).__floor__()
profiles=[templates(t) for t in (L,U,T)]
assert [v[1] for v in profiles].count(profiles[0][1])==3
for a,b in zip(profiles[0][2],profiles[1][2]):assert a[:3]==b[:3]
for t,(c,d,rr) in zip((L,U,T),profiles):
 p=164*t-43;v=59-225*t
 assert 0<p<v and all(x[4]>=p and x[3]>=v for x in rr)
 assert (37,24,127) in [(r,ls,rs) for r,ls,rs,dl,dr in rr if dr==p]
 assert (98,127,66) in [(r,ls,rs) for r,ls,rs,dl,dr in rr if dl==v]
 assert sorted(min(x) for x in d.values())==ages
 assert sum(any(r<=163 for r in x) for x in d.values())==127
rp=164*L-43;rm=59-225*U
assert rp==min(min(frac(i*t),1-frac(i*t)) for t in (L,U) for i in range(1,M+H))
for j in [389,553,25339,168319,10899111]:
 k=near(j*T);a=j*L-k;b=j*U-k
 s=1 if a>0 and b>0 else -1 if a<0 and b<0 else 0
 assert s and max(abs(a),abs(b))<(rp if s==1 else rm)
 for t,(c,d,rr) in zip((L,U,T),profiles):
  assert all(owner(t,j-r,c)==owner(t,-r,c) for r in range(1,H+1))
assert max(abs(389*L-102),abs(389*U-102))>rp
# Exact fresh partition reconstruction at the new negative-return stage.
for t in [L,U]:
 for n in (390,456,457,492,493,553):
  expected=164*t-43 if n in (390,456,493,553) else F(0)
  assert risk(t,n)-risk(t,n-1)==expected
if len(sys.argv)==3:
 with open(sys.argv[1]) as f:reg=list(csv.DictReader(f,delimiter='\t'))
 with open(sys.argv[2]) as f:ev={int(x['n']):(int(x['delta_A']),int(x['delta_B'])) for x in csv.DictReader(f,delimiter='\t')}
 stages=full=total=symmetric=0;added=[]
 for row in reg:
  q,j,n0,n1=map(int,(row['i'],row['j'],row['n0'],row['n1']))
  if q<H or j<M+H:continue
  k=near(j*T);dl=j*L-k;du=j*U-k
  s=1 if dl>0 and du>0 else -1 if dl<0 and du<0 else 0
  if not s or max(abs(dl),abs(du)) >= (rp if s==1 else rm):continue
  stages+=1
  if max(abs(dl),abs(du))<rp:symmetric+=1
  pos={q+j-r+1 for r in ages if n0<=q+j-r+1<=n1}
  assert pos=={n for n in ev if n0<=n<=n1}
  if max(abs(dl),abs(du))>=rp:added.append((q,j,n0,n1,len(pos)))
  if not pos:continue
  p=near(q*T);uL=abs(q*L-p);uU=abs(q*U-p);vL=abs(dl);vU=abs(du)
  sq=1 if q*T>p else -1
  assert sq==-s
  if max(uL,uU)<min(vL,vU):amp=(-sq*p,sq*q)
  elif max(vL,vU)<min(uL,uU):amp=(-s*k,s*j)
  else:raise AssertionError('amplitude switch inside frozen theta interval')
  for n in pos:assert ev[n]==amp
  full+=1;total+=len(pos)
 assert (stages,full,total,symmetric)==(75,74,9472,74)
 assert added==[(164,389,390,553,128)]
 print('R27 cross-check: 75 stages, 74 event-bearing, 9472 signed-affine events; directional-only stage q=164,j=389')
print('PASS_R31_EXACT_DIRECTIONAL_RADIUS and 12 independent risk checks')
print('rho_plus >=',rp,'rho_minus >=',rm,'negative/positive ratio',rm/rp)
