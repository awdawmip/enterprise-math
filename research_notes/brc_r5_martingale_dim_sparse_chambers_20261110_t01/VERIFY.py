"""Exact witnesses for full-dimensional sparse P/Q-BRC Blackwell chambers."""
from fractions import Fraction as Q
R=tuple(map(Q,'1/10 1/2 3/4 1 5/4 3/2 19/10'.split()))
CASES=(
 ('FULL12',((0,0),(1,1),(2,2),(3,3),(6,6))+tuple((i,5) for i in range(7)),(6,5),Q(39,4),(0,1,2,3,4,5,6,7,8,9,10,12),10),
 ('ZERO11',((0,0),(2,2),(3,3),(5,5),(6,6))+tuple((i,1) for i in (0,2,3,4,5,6)),(0,1),Q(39,4),(0,2,3,4,5,6,7,8,9,10,12),9))
def col(e):
 i,j=e;v=[Q(0)]*21;v[i]=Q(1);v[7+j]=Q(1);v[14+j]=R[i];return v
def determinant(A):
 A=[row[:] for row in A];n=len(A);d=Q(1)
 for k in range(n):
  p=next((i for i in range(k,n) if A[i][k]),None)
  assert p is not None
  if p!=k:A[k],A[p]=A[p],A[k];d=-d
  t=A[k][k];d*=t
  for i in range(k+1,n):
   f=A[i][k]/t
   if f:A[i]=[a-f*b for a,b in zip(A[i],A[k])]
 return d
for name,S,pivot,value,rows,dimension in CASES:
 assert len(S)==len(set(S)) and len(rows)==len(S)
 w={e:Q(1) for e in S};w[pivot]=value
 z=sum(w.values());w={e:v/z for e,v in w.items()}
 mu=tuple(sum((w.get((i,j),Q(0)) for j in range(7)),Q(0)) for i in range(7))
 nu=tuple(sum((w.get((i,j),Q(0)) for i in range(7)),Q(0)) for j in range(7))
 H=tuple(sum(((R[i]-R[j])*w.get((i,j),Q(0)) for i in range(7)),Q(0)) for j in range(7))
 rhs=mu+nu+tuple(R[j]*nu[j] for j in range(7))
 lhs=tuple(sum((w[e]*col(e)[k] for e in S),Q(0)) for k in range(21))
 assert min(w.values())>0 and z>0 and sum(mu)==sum(nu)==1
 assert H==(Q(0),)*7 and lhs==rhs and nu[4]==0
 assert min(nu[j] for j in (0,1,2,3,5,6))>0
 assert all(mu[i]>0 for i in range(7) if name=='FULL12' or i!=1)
 assert mu[1]==0 if name=='ZERO11' else mu[1]>0
 # An integer determinant of 1 certifies full column rank of the 21 x k matrix.
 det=determinant([[col(e)[i] for e in S] for i in rows])
 assert det==1
 # On S, only source column 5 (FULL12), respectively 1 (ZERO11),
 # has nonzero martingale defect coefficients; its defect-row rank is one.
 active=5 if name=='FULL12' else 1
 assert all(R[i]==R[j] for i,j in S if j!=active)
 assert any(R[i]!=R[j] for i,j in S if j==active)
 assert len(S)-1-1==dimension
 print(name,'k',len(S),'det',det,'defect_rank',1,'normalized_dim',dimension)
 print('min_positive',min(w.values()),'mu',','.join(map(str,mu)),'nu',','.join(map(str,nu)))
print('PASS_EXACT_11_AND_12_EDGE_FULL_DIMENSIONAL_CHAMBERS')
