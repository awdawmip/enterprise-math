#!/usr/bin/env python3
"""R5 seven-node martingale coupling: exact 11-edge witness and 19-edge sparsifier.
No third-party dependencies; uses fractions.Fraction only.
"""
from fractions import Fraction as F

R = tuple(F(s) for s in ('1/10','1/2','3/4','1','5/4','3/2','19/10'))
N=len(R)
X=tuple(F(s) for s in ('1','1/6','1','0','31/240','0','1/60'))
Y=tuple(F(s) for s in ('403649/517950','462959/2071800',
    '403649/517950','455051/5524800','20479/103590',
    '279431/1841600','462959/20718000'))
# (target row, source column, exact Q mass). Zero entries are omitted.
EDGES = (
 (0,0,'1099/21600'),(0,1,'1/39'),(0,2,'3227713/64640160'),
 (2,1,'8/195'),(2,2,'1417929/5985200'),
 (3,2,'3227713/24861600'),(3,3,'1511/10800'),
 (3,5,'94567/1035900'),(5,5,'32043/460400'),
 (6,5,'94567/828720'),(6,6,'1099/21600'),
)

def masses(f):
 g,a,b,u,v,w,z=f
 return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
  F(13,40)*a+b/80-u,(g-a)/2,
  1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
  (g-b)/2,F(3,40)*a+F(21,80)*b-w,
  u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)

def stops(f):
 g,a,b,u,v,w,z=f
 return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
         1+g+(a+b)/2+u+v+w)

def lawful(f):
 g,a,b,u,v,w,z=f
 assert 0<=a<=g<=1 and 0<=b<=g
 assert 0<=u<=F(13,40)*a+b/80
 assert 0<=w<=F(3,40)*a+F(21,80)*b
 assert 0<=z<=a/10 and 0<=v-z<=F(9,40)*b
 p=masses(f)
 assert min(p)>=0 and sum(p)==1 and sum(a*b for a,b in zip(p,R))==1
 return p

def calibrated(E, target, source, ratios=R):
 n=len(ratios)
 assert len(E)==n*n and all(v>=0 for v in E)
 for i in range(n):
  assert sum(E[i*n+j] for j in range(n))==target[i]
 for j in range(n):
  assert sum(E[i*n+j] for i in range(n))==source[j]
  assert sum(ratios[i]*E[i*n+j] for i in range(n))==ratios[j]*source[j]
 assert sum(E)==1

def column_null_direction(ratios, indices):
 """An exact kernel vector for any 3*n-1 chosen transport columns."""
 n=len(ratios); k=len(indices)
 A=[]
 for i in range(n):
  A.append([F((v//n)==i) for v in indices])
 for j in range(n):
  A.append([F((v%n)==j) for v in indices])
 for j in range(n):
  A.append([ratios[v//n] if v%n==j else F(0) for v in indices])
 pivot=[]; rank=0
 for col in range(k):
  which=next((rr for rr in range(rank,len(A)) if A[rr][col]),None)
  if which is None:continue
  A[rank],A[which]=A[which],A[rank]
  scale=A[rank][col]
  A[rank]=[x/scale for x in A[rank]]
  for rr in range(len(A)):
   if rr!=rank and A[rr][col]:
    mul=A[rr][col]
    A[rr]=[x-mul*y for x,y in zip(A[rr],A[rank])]
  pivot.append(col);rank+=1
 free=next((col for col in range(k) if col not in pivot),None)
 assert free is not None, 'Expected rank <= 3n-2'
 d=[F(0)]*k;d[free]=F(1)
 for rr,col in enumerate(pivot):d[col]=-A[rr][free]
 assert any(v>0 for v in d) and any(v<0 for v in d)
 return d

def sparsify(E,ratios=R):
 """Given any exact feasible martingale coupling, reduce positive edges to <=3n-2."""
 n=len(ratios); M=list(E);passes=0
 while sum(bool(v) for v in M)>3*n-2:
  sup=[k for k,v in enumerate(M) if v>0][:3*n-1]
  d=column_null_direction(ratios,sup)
  step=min(M[sup[j]]/(-v) for j,v in enumerate(d) if v<0)
  for j,v in enumerate(d): M[sup[j]]+=step*v
  assert min(M)>=0
  passes+=1
 return tuple(M),passes

def dense_benchmark():
 """37-edge exact seven-grid martingale kernel, without a FULL_HIST assertion."""
 source=[F(1,N)]*N
 E=[F(0)]*(N*N)
 for j in range(N):
  if j in (0,N-1):E[j*N+j]=source[j];continue
  E[j*N+j]+=source[j]/2
  pairs=[(lo,hi) for lo in range(j) for hi in range(j+1,N)]
  for lo,hi in pairs:
   batch=source[j]/(2*len(pairs))
   E[lo*N+j]+=batch*(R[hi]-R[j])/(R[hi]-R[lo])
   E[hi*N+j]+=batch*(R[j]-R[lo])/(R[hi]-R[lo])
 target=[sum(E[i*N+j] for j in range(N)) for i in range(N)]
 calibrated(E,target,source)
 return tuple(E),tuple(target),tuple(source)

def main():
 mx,my=lawful(X),lawful(Y)
 assert Y[6]*9*Y[2]==4*Y[1]*(Y[4]-Y[6])
 assert X[6]*9*X[2]!=4*X[1]*(X[4]-X[6])
 assert stops(X)==stops(Y)
 E=[F(0)]*(N*N)
 for i,j,weight in EDGES:E[i*N+j]=F(weight)
 calibrated(E,my,mx)
 print('PASS_EXACT_11_EDGE_NONZERO_RESIDUAL_PHYSICAL_R5_CERTIFICATE')
 D,target,source=dense_benchmark()
 assert sum(bool(v) for v in D)==37
 Q,passes=sparsify(D)
 calibrated(Q,target,source)
 assert sum(bool(v) for v in Q)<=19
 print('PASS_EXACT_DENSE_TO_SPARSE_MARTINGALE_37_TO_'+str(sum(bool(v) for v in Q)))
 print('SPARSIFY_PASSES',passes)
 print('PROVED_GENERAL_7_NODE_COUPLING_SUPPORT_UPPER_BOUND_19')

if __name__=='__main__':main()
