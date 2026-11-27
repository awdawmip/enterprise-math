import itertools,math
from fractions import Fraction as F
def det(A):
 A=[list(r) for r in A];n=len(A);s=1;prev=1
 for i in range(n-1):
  j=next((j for j in range(i,n) if A[j][i]),None)
  if j is None:return 0
  if j!=i:A[i],A[j]=A[j],A[i];s=-s
  p=A[i][i]
  for j in range(i+1,n):
   for k in range(i+1,n):A[j][k]=(A[j][k]*p-A[j][i]*A[i][k])//prev
  prev=p
 return s*A[-1][-1]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def normal(rows):
 n=len(rows)+1; v=[(-1)**i*det([r[:i]+r[i+1:] for r in rows]) for i in range(n)];g=math.gcd(*v);return tuple(x//g for x in v) if g else None
def exclude(m,C,e,ex):
 m=m+[r['m'] for r in ex]; C=[col+[r['cols'][j] for r in ex] for j,col in enumerate(C)];e=e+[r['error'] for r in ex];n=len(m)
 U=C+[[e[i] if i==j else 0 for i in range(n)] for j in range(n)]
 best=None;count=0
 for rows in itertools.combinations(U,n-1):
  v=normal(rows)
  if not v:continue
  count+=1;sup=sum(abs(dot(v,c)) for c in U);val=abs(dot(v,m));gap=val-sup
  score=F(gap,val+sup) if val+sup else F(0)
  if best is None or score>best[0]:best=score,v,gap,val,sup
 score,v,gap,val,sup=best
 return dict(ks=[r['k'] for r in ex],count=count,normal=list(v),gap=str(gap),center_abs=str(val),support=str(sup),score=str(score))
