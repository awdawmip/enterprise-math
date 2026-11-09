from fractions import Fraction as F
from itertools import product, combinations

R=tuple(map(F,'1/10 1/2 3/4 1 5/4 3/2 19/10'.split()))
X=tuple(map(F,'999/1000 1/6 999/1000 1/20 29/240 11/160 1/120'.split()))
Y=tuple(map(F,'1 2002911/10904720 26095487/40892700 442758619/6542832000 11037627/68154500 394502727/2180944000 2002911/109047200'.split()))
S=((0,0),(0,1),(3,1),(5,1),(0,2),(2,2),(3,2),(2,3),(3,3),(4,3),(4,5),(5,5),(6,5),(6,6))
T=((6,1),(6,2),(6,3),(0,5),(2,5),(3,5))
E0=tuple(map(F,'33553/432000 3997/432000 3997/540000 0 510479933/29442744000 2893155797/8178540000 6636239129/147213720000 222511289/4089270000 318755011/3680343000 222511289/4089270000 172449787/1363090000 219439/545236000 172449787/2180944000 38053/432000'.split()))
U=tuple(tuple(map(F,s.split())) for s in (
'1/2 -7/2 1/2 1 0 0 0','-1/2 -1/2 -1/2 0 1 0 0','-3/2 5/2 -3/2 0 0 1 0','0 0 0 0 0 0 1'))
V=tuple(tuple(map(F,s.split())) for s in (
'509/900 -1013/900 -19997/18000 421/4000 14/25 -2/125 182/125 2/125 -6211/18000 2/125 -2/125 -421/4000 -1/100 1/100',
'67/162 -871/1458 77869/58320 -11749/12960 134/729 -268/405 1742/3645 268/405 -11749/6480 268/405 -268/405 11749/12960 -67/162 67/162',
'1/100 2383/8100 123727/162000 -9511/36000 -616/2025 -1018/1125 -8008/10125 1018/1125 163/6000 1018/1125 -1018/1125 9511/36000 -509/900 509/900',
'-247/1620 3211/14580 -22477/36450 3211/8100 -247/3645 494/2025 -3211/18225 -494/2025 3211/4050 -494/2025 494/2025 -3211/8100 247/1620 -247/1620'))
HI=F(17774559,17507527960)
rho_star=F(17774559,225414193300)
dmax=F(904888979,2817677416250)
c=F(16537,12960)
j55=S.index((5,5))

def combine(base,ds,ps):
 return tuple(v+sum((p*ds[k][i] for k,p in enumerate(ps)),F(0)) for i,v in enumerate(base))

def mass(f):
 g,a,b,u,v,w,z=f
 return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,F(13,40)*a+b/80-u,(g-a)/2,1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),(g-b)/2,F(3,40)*a+F(21,80)*b-w,u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)

def times(f):
 g,a,b,u,v,w,z=f
 return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,1+g+(a+b)/2+u+v+w)

def slack(f):
 g,a,b,u,v,w,z=f
 return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,w,F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)

def col(e):
 i,j=e
 v=[F(0)]*21
 v[i]=F(1);v[7+j]=F(1);v[14+j]=R[i]
 return tuple(v)

def solve(edge):
 M=[[col(S[k])[i] for k in range(14)]+[col(edge)[i]] for i in range(21)]
 piv=0;lead=[]
 for j in range(14):
  ii=next((t for t in range(piv,21) if M[t][j]),None)
  if ii is None: continue
  M[piv],M[ii]=M[ii],M[piv]
  d=M[piv][j];M[piv]=[v/d for v in M[piv]]
  for ii in range(21):
   if ii!=piv and M[ii][j]:
    d=M[ii][j];M[ii]=[v-d*w for v,w in zip(M[ii],M[piv])]
  lead.append(j);piv+=1
 assert piv==14 and all(M[i][-1]==0 for i in range(piv,21))
 out=[F(0)]*14
 for i,j in enumerate(lead):out[j]=M[i][-1]
 return tuple(out)

ALPHA={e:solve(e) for e in T}
BETA={e:-ALPHA[e][j55] for e in T}
assert all(z>0 for z in BETA.values())
assert [sum(ALPHA[(3,5)][k]*col(S[k])[i] for k in range(14)) for i in range(21)]==list(col((3,5)))

def old(p):return combine(E0,V,p)
def src(p):return combine(X,U,p)
def variants(p):
 o=old(p)
 return {e:{**{v: o[k]-o[j55]/ALPHA[e][j55]*ALPHA[e][k] for k,v in enumerate(S) if k!=j55},e:o[j55]/ALPHA[e][j55]} for e in T}

def check(p,strict=True):
 x=src(p);o=old(p);mu=mass(Y);nu=mass(x)
 assert x[0]==x[2] and times(x)==times(Y)==(F(17609,6000),F(33857,12000))
 assert sum(mu)==sum(nu)==1 and min(nu+mu)>=0
 ss=slack(x)
 assert ss[4]==0 and min(z for i,z in enumerate(ss) if i!=4)>0 if strict else min(ss)>=0
 assert o[j55]<0 if strict else o[j55]<=0
 out=variants(p)
 for e,v in out.items():
  assert len(v)==14
  assert min(v.values())>0 if strict else min(v.values())>=0
  assert [sum((z*col(ed)[i] for ed,z in v.items()),F(0)) for i in range(21)]==list(mu)+list(nu)+[R[j]*nu[j] for j in range(7)]
 return min(z for i,z in enumerate(ss) if i!=4),min(z for v in out.values() for z in v.values())

p0=(rho_star+dmax/2,-rho_star-dmax/2,-rho_star-dmax/2,3*HI/4)
a0,b0=check(p0)
print('PIVOT_BETA',' '.join(f'{e}:{BETA[e]}' for e in T))
print('CENTRE_MIN_PHYSICAL',a0,'CENTRE_MIN_EDGE',b0)
# conservatively choose a rational 4-dimensional box about centre
for radius in (F(1,10**6),F(1,10**7),F(1,10**8),F(1,10**9),F(1,10**10)):
 try:
  minss=None;minw=None
  for signs in product((-1,1),repeat=4):
   p=tuple(a+s*radius for a,s in zip(p0,signs))
   a,b=check(p)
   minss=a if minss is None else min(minss,a)
   minw=b if minw is None else min(minw,b)
  print('CERTIFIED_RADIUS',radius,'MIN_PHYS',minss,'MIN_EDGE',minw)
  break
 except AssertionError:
  print('RADIUS_FAILED',radius)
else:raise AssertionError('no box')
for delta in (F(0),dmax/2,dmax):
 p=(rho_star+delta,-rho_star-delta,-rho_star-delta,3*HI/4)
 if delta:
  check(p,strict=delta!=dmax)
  vv=variants(p)
  assert len(vv)==6
  assert all(v[e]==c*delta/BETA[e] for e,v in vv.items())
  for k in range(1,7):
   for subset in combinations(T,k):
    lam=F(1,k)
    mix={edge:sum(lam*vv[e].get(edge,F(0)) for e in subset) for edge in set(S).union(T) if edge!=(5,5)}
    assert sum(v>0 for v in mix.values())==13+k
    assert [sum(z*col(ed)[i] for ed,z in mix.items()) for i in range(21)]==list(mass(Y))+list(mass(src(p)))+[R[j]*mass(src(p))[j] for j in range(7)]
 print('DELTA',delta,'BASE_G',src(p)[0],'PIVOT_NEW_MASSES',[(str(e),str(variants(p)[e][e])) for e in T])
print('PASS_SIX_PIVOT_COLUMNS_AND_BETA_POSITIVE')
print('PASS_COMMON_RATIONAL_4D_BOX_BY_16_VERTEX_CERTIFICATE')
print('PASS_63_SIMPLEX_FACES_AT_RAY_MIDPOINT_AND_ENDPOINT')
print('PASS_EXACT_5_SIMPLEX_CLASSIFICATION_ALGEBRA')
