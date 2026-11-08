#!/usr/bin/env python3
"""Original frozen 96-port X6-BRC: exact block AB/BA intertwiner test (stdlib)."""
import json
from itertools import product
from pathlib import Path
STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple((-1 if c>0 else 1)*k for k in STARS[a] if k!=abs(c))
PHASE=tuple((a,p,s*k) for a in range(4) for k in STARS[a] for s in (-1,1) for p in near(a,s*k))
IX={x:i for i,x in enumerate(PHASE)}
def nexts(i):
 a,p,c=PHASE[i];b=next(b for b in range(4) if b!=a and abs(c) in STARS[b])
 return tuple(IX[t] for t in [(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)])
NEXT=tuple(nexts(i) for i in range(48));TARGET=IX[(0,1,-3)]
ALPHA=(3,4,1,2,5,6)
def flip(x):return (-1 if x>0 else 1)*ALPHA[abs(x)-1]
THETA=[]
for a,p,c in PHASE:
 u,v=flip(c),flip(p)
 aa=next(j for j,S in enumerate(STARS) if abs(u) in S and abs(v) in S)
 THETA.append(IX[(aa,u,v)])
assert len(set(THETA))==48 and all(THETA[THETA[i]]==i for i in range(48)) and THETA[TARGET]==TARGET
edges={(i,j) for i in range(48) for j in NEXT[i]}
assert len(edges)==144
assert all((THETA[j],THETA[i]) in edges and abs(PHASE[THETA[j]][2])==ALPHA[abs(PHASE[i][2])-1] for i,j in edges)
def construct(x,z):
 A=[{} for _ in range(96)];B=[{} for _ in range(96)];D=[{} for _ in range(96)]
 H=[2*THETA[i//2]+i%2 for i in range(96)]
 for i in range(48):
  t=int(i==TARGET)
  for u,v in product((0,1),repeat=2):D[2*i+u][2*i+v]=z if t and u==v==1 else 1
 for i in range(48):
  for j in NEXT[i]:
   a=x[abs(PHASE[i][2])-1]
   for u,v in product((0,1),repeat=2):A[2*i+u][2*j+v]=a*D[2*j+u][2*j+v]
   for u in (0,1):B[2*i+u][2*j+u]=a
 def clean(M):return [{j:v for j,v in row.items() if v} for row in M]
 return clean(A),clean(B),clean(D),H
def trans(A):
 R=[{} for _ in A]
 for i,row in enumerate(A):
  for j,v in row.items():R[j][i]=v
 return R
def mul(A,B):
 R=[{} for _ in A]
 for i,row in enumerate(A):
  for k,a in row.items():
   for j,b in B[k].items():R[i][j]=R[i].get(j,0)+a*b
 return [{j:v for j,v in row.items() if v} for row in R]
def conjugate(A,H):
 R=[{} for _ in A]
 for i,row in enumerate(A):
  for j,v in row.items():R[H[i]][H[j]]=v
 return R
CASES=[((2,3,5,7,11,13),17),((1,1,1,1,1,1),1),((0,1,2,0,4,7),0)]
for x,z in CASES:
 A,B,D,H=construct(x,z)
 ax=tuple(x[ALPHA[i]-1] for i in range(6))
 Aa,Ba,Da,Ha=construct(ax,z)
 assert H==Ha and D==Da and A==mul(B,D) and Ba==conjugate(trans(B),H)
 U=[{} for _ in A]
 for i,row in enumerate(trans(B)):U[H[i]]=row.copy()
 V=[{} for _ in A]
 for i,row in enumerate(D):
  for j,val in row.items():V[i][H[j]]=val
 assert Aa==mul(U,V)
 assert trans(A)==mul(V,U)
result={'schema':'PREFIX585_R2_96PORT_POLYNOMIAL_UV_VU_CERTIFICATE_V1',
 'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'phase_count':48,'port_count':96,'original_native_action_count':576,'phase_edges':144,
 'phase_involution':THETA,
 'symbolic_structural_inputs':'all 144 directed phase-edge rewrites; gate target fixed',
 'identity':'A(alpha*x,z)=U V, A(x,z)^T=V U; U=H B(x)^T, V=D(z) H^-1, A=B(x) D(z)',
 'integer_specializations':[{'axis_variables':list(x),'gate':z} for x,z in CASES],
 'general_identity_proof':'symbolic block multiplication and exact native phase anti-isomorphism; see proof',
 'status':'ALL_ASSERTIONS_PASS_AUTHOR_SIDE_UNREVIEWED'}
Path(__file__).with_name('PREFIX585_R2_96port_ABBA_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(result['status'])
