#!/usr/bin/env python3
"""PREFIX-602-R6: exact minimal repair coordinates for weighted native BRC phase observer."""
import io,runpy,json
from contextlib import redirect_stdout
from fractions import Fraction as F
with redirect_stdout(io.StringIO()): d=runpy.run_path('PREFIX601_R6_weighted_short_certificate.py')
W,U,V,J,Wi,pairs=d['W'],d['U'],d['V'],d['J'],d['Wi'],d['pairs']
N=24

def mul(A,B):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*B)] for r in A]
def rank(A):
 if not A:return 0
 a=[[F(x) for x in r] for r in A];i=0
 for col in range(len(a[0])):
  p=next((j for j in range(i,len(a)) if a[j][col]),None)
  if p is None:continue
  a[i],a[p]=a[p],a[i];pivot=a[i][col]
  for j in range(i+1,len(a)):
   if a[j][col]:
    q=a[j][col]/pivot
    for c in range(col,len(a[0])):a[j][c]-=q*a[i][c]
  i+=1
  if i==len(a):break
 return i

def verify(t,tag):
 B=[[F(W[i][j])+sum(U[i][e]*t[e]*V[e][j] for e in range(12)) for j in range(N)] for i in range(N)]
 s=[sum(row) for row in B]
 assert all(x>0 for x in s)
 Q=[[v/s[i] for v in B[i]] for i in range(N)]
 P=[[F(0)]*(2*N) for _ in range(2*N)]
 for i in range(N):
  for j in range(N):P[i][N+j]=P[N+i][j]=Q[i][j]
 assert all(sum(row)==1 for row in P)
 VWi=mul(V,Wi)
 local=[]
 for e,f in pairs:
  if 4*t[e]*t[f]!=1:continue
  u=[F(0)]*12;u[e]=1;u[f]=-2*t[e]
  w=[-sum(u[h]*t[h]*VWi[h][q] for h in range(12)) for q in range(N)]
  assert any(w)
  a=[w[i]*s[i] for i in range(N)]
  assert [sum(a[i]*Q[i][j] for i in range(N)) for j in range(N)]==[0]*N
  assert sum(a)==0
  local.append(a)
 basis=[[F(0)]*N+a for a in local]+[a+[F(0)]*N for a in local]
 k=len(local)
 assert rank(basis)==2*k
 assert rank(P)==2*N-2*k
 # Rows of P give the 48 output columns of the map pi -> pi P.
 aug=[P[i]+[b[i] for b in basis] for i in range(2*N)]
 assert rank(aug)==2*N
 witness=None
 if basis:
  h=basis[0];base=[F(1,2*N)]*(2*N);eps=F(1,2*N*(max(abs(x) for x in h)+1))
  a=[base[i]+eps*h[i] for i in range(2*N)];b=[base[i]-eps*h[i] for i in range(2*N)]
  assert min(a)>0 and min(b)>0 and sum(a)==sum(b)==1
  assert [sum(a[i]*P[i][j] for i in range(2*N)) for j in range(2*N)]==[sum(b[i]*P[i][j] for i in range(2*N)) for j in range(2*N)]
  witness={'signed_support':{str(i):str(x) for i,x in enumerate(h) if x},'epsilon':str(eps)}
 return {'case':tag,'critical_pairs':k,'phase_rank':rank(P),'minimal_extra_linear_coordinates':2*k,'augmented_rank':rank(aug),'explicit_law_collision':witness is not None,'witness':witness}

one=[F(1)]*12
t1=one.copy()
for e,f in pairs[:1]:t1[e]=t1[f]=F(1,2)
t2=one.copy()
for e,f in pairs[:2]:t2[e]=F(1,4);t2[f]=F(1)
res=[verify(one,'original_frozen_all_one'),verify(t1,'one_critical_pair'),verify(t2,'two_asymmetric_critical_pairs'),verify([F(1,2)]*12,'all_six_critical_pairs')]
print(json.dumps({'status':'ALL_CHECKS_PASS','science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d','claim':'minimal 2*k additional linear phase-observer repairs', 'cases':res},indent=2))
