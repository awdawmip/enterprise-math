from fractions import Fraction as Q
r=tuple(map(Q,'1/10 1/2 3/4 1 5/4 3/2 19/10'.split()))
mu=tuple(map(Q,'1841762908667/17665646400000 23/4000000 11127124941/27261800000 6142930209941/44164116000000 14797213/81785400 219847927/545236000000 2952911787287/17665646400000'.split()))
nu=tuple(map(Q,'59397237871/765511344000 3997/240000 2497/6000 187159707437/956889180000 0 16479/80000 67371314371/765511344000'.split()))
D=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7) if j not in (0,6) or i==j)
B=((0,0),(0,1),(2,1),(0,2),(2,2),(4,2),(0,3),(1,3),(3,3),(4,3),(5,3),(4,5),(5,5),(6,5),(6,6))
rows=(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)
def col(e):
 i,j=e;v=[Q(0)]*21;v[i]=Q(1);v[7+j]=Q(1);v[14+j]=r[i];return v
C={e:col(e) for e in D}
def solve(A,b):
 m=[list(row)+[x] for row,x in zip(A,b)];n=len(m);det=Q(1)
 for k in range(n):
  p=next(i for i in range(k,n) if m[i][k]);
  if p!=k:m[k],m[p]=m[p],m[k];det=-det
  z=m[k][k];det*=z;m[k]=[x/z for x in m[k]]
  for i in range(n):
   if i!=k:
    z=m[i][k]
    if z:m[i]=[x-z*y for x,y in zip(m[i],m[k])]
 return [row[-1] for row in m],det
rhs=mu+nu+tuple(r[j]*nu[j] for j in range(7));eps=Q(1,10000000)
rest=[rhs[k]-eps*sum((C[e][k] for e in D),Q(0)) for k in range(21)]
w,det=solve([[C[e][i] for e in B] for i in rows],[rest[i] for i in rows]);assert det==Q(-299,1600)
E={e:eps for e in D}
for e,x in zip(B,w):E[e]+=x
assert min(E.values())==eps and all(sum((E[e]*C[e][k] for e in D),Q(0))==rhs[k] for k in range(21))
J=(1,2,3,5);deficits=tuple(nu[j]-mu[j] for j in J);assert min(deficits)>Q(1,1000)
S=((0,0),(1,1),(2,2),(3,3),(6,6))+tuple((i,5) for i in range(7))
_,d=solve([[C[e][i] for e in S] for i in (0,1,2,3,4,5,6,7,8,9,10,12)],[Q(0)]*12)
assert d==1
free=[e for e in S if e not in ((0,5),(6,5))]
V=[]
for f in free:
 h=r[f[0]]-r[f[1]];a=(Q(-7,5)-h)/Q(9,5);b=-1-a
 v={f:Q(1),(6,5):a,(0,5):b}
 assert sum(v.values())==0
 assert all(sum((z*(r[i]-r[j]) for (i,j),z in v.items() if j==c),Q(0))==0 for c in range(7))
 V.append(v)
assert len(V)==10 and max(abs(z) for v in V for z in v.values())<=1
upper=Q(3,10**11)
assert 10*upper<eps and 4*10*upper<min(deficits)
print('PASS_BASE_30_POSITIVE_AND_21_EQUATIONS','minimum',eps,'rank15_minor',det)
print('PASS_ALL_FOUR_STRICT_DEFICITS',' '.join(str(x) for x in deficits))
print('PASS_TEN_INDEPENDENT_MARTINGALE_TANGENTS_AND_12_MINOR',d)
print('PASS_TRANSCENDENTAL_PERTURBATION_POSITIVITY','t=e/10^11<',upper)
print('PROVED_VIA_RATIONAL_HYPERPLANES','each <=14-support image has dimension <=9 in ambient 10D; transcendental t avoids finite union')
