#!/usr/bin/env python3
"""PREFIX-600-R6 native 48-phase determinant/inverse and 49/50 linear codec.
Run beside the Git-blob-verified PREFIX565_positive_marginal_certificate.py.
"""
import hashlib, json
from collections import Counter
from fractions import Fraction
from pathlib import Path
from PREFIX565_positive_marginal_certificate import PHASES,PHASE_INDEX,STARS,NEXT,TARGET,ACTIONS,ROOTS,SCIENCE_PIN,edge
assert SCIENCE_PIN=='f42f2906d77f24085c123f3ccfe9667d41caa96d'
b=Path(__file__).with_name('PREFIX565_positive_marginal_certificate.py').read_bytes()
assert hashlib.sha1(('blob %d\0'%len(b)).encode()+b).hexdigest()=='7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41'

def mul(A,B):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*B)] for r in A]
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def neg(p):
 a,x,y=PHASES[p];return PHASE_INDEX[a,-x,-y]
plus=[p for p in range(48) if PHASES[p][2]>0];minus=[neg(p) for p in plus]
index={p:i for i,p in enumerate(plus)}
B=[[0]*24 for _ in plus];W=[[0]*24 for _ in plus]
for i,p in enumerate(plus):
 for q in NEXT[p]:
  j=index[neg(q)];B[i][j]+=1
  if PHASES[p][0]==PHASES[q][0]:W[i][j]+=1
assert all(sum(r)==1 for r in W) and all(sum(c)==1 for c in zip(*W))
cycs=set();seen=set()
for i in range(24):
 if i in seen:continue
 k=i;orbit=[]
 while k not in seen:
  seen.add(k);orbit.append(k);k=W[k].index(1)
 assert k==i and len(orbit)==3
 cycs.add(tuple(orbit))
assert len(cycs)==8
E=sorted({(PHASES[p][0],abs(PHASES[p][2])) for p in plus});ei={e:i for i,e in enumerate(E)}
assert len(E)==12
U=[[0]*12 for _ in range(24)];V=[[0]*24 for _ in range(12)];J=[[0]*12 for _ in range(12)]
for i,p in enumerate(plus):U[i][ei[PHASES[p][0],abs(PHASES[p][2])]]=1
for (a,c),i in ei.items():
 other=next(j for j in range(4) if j!=a and c in STARS[j]);J[i][ei[other,c]]=1
 for j,p in enumerate(plus):V[i][j]=int(PHASES[p][0]==other and abs(PHASES[p][1])==c)
assert all(sum(r)==2 for r in V) and mul(J,J)==eye(12)
Wi=[list(c) for c in zip(*W)]
assert B==[[W[i][j]+mul(U,V)[i][j] for j in range(24)] for i in range(24)]
assert mul(V,mul(Wi,U))==[[2*x for x in r] for r in J]
H=[[2*J[i][j]-int(i==j) for j in range(12)] for i in range(12)]
Z=mul(mul(mul(Wi,U),H),mul(V,Wi))
D=[[3*Wi[i][j]-Z[i][j] for j in range(24)] for i in range(24)] # D=3B^{-1}
assert mul(B,D)==[[3*x for x in r] for r in eye(24)]
assert mul(D,B)==[[3*x for x in r] for r in eye(24)]
assert all(sorted(x for x in r if x)==[-2,1,1,1] for r in D)
M=[[0]*48 for _ in range(48)];N=[[0]*48 for _ in range(48)]
for p in range(48):
 for q in NEXT[p]:M[p][q]+=1
for i,p in enumerate(plus):
 for j,q in enumerate(minus):
  assert M[p][q]==B[i][j] and M[minus[i]][plus[j]]==B[i][j]
  N[p][q]=D[i][j];N[minus[i]][plus[j]]=D[i][j]
assert mul(M,N)==[[3*x for x in r] for r in eye(48)]
assert all(sorted(x for x in r if x)==[-2,1,1,1] for r in N)
for p in range(48):
 q=[Fraction(x,3) for x in M[p]]
 assert [sum(q[k]*N[k][i] for k in range(48)) for i in range(48)]==[int(i==p) for i in range(48)]
P=[p for p in range(48) if TARGET in NEXT[p]]
assert P==[3,14,15] and [NEXT[p].index(TARGET) for p in P]==[0,1,1]
checks=0
for root in ROOTS:
 for keep_action in (False,True):
  for port in range(96):
   p,bit=divmod(port,2)
   def lab(a,j,w):return (a,j,w) if keep_action else (j,w)
   actual=Counter(lab(a,*edge(port,a,root)) for a in ACTIONS)
   basis=Counter(lab(a,*edge(2*p,a,root)) for a in ACTIONS)
   if bit and p in P:
    a=(NEXT[p].index(TARGET),1);j,w=edge(2*p,a,root)
    assert j==9 and w[-1]==0
    basis[lab(a,j,w)]-=1;basis[lab(a,j,w[:-1]+(1,))]+=1
   assert +basis==+actual
   checks+=1
assert checks==9*2*96
print(json.dumps({'status':'ALL_CHECKS_PASS','source_blob':'7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41',
 'det_B':729,'det_M':531441,'inverse_row_pattern':[-2,1,1,1],
 'phase_reconstruction_tests':48,'native_output_tests':checks,
 'one_step_rank_hidden_action':49,'one_step_rank_with_action':50,
 'proof':'B=W+UV; V(W^-1)U=2J; J^2=I; det(W)=1; det(I+2J)=3^6'},indent=2))
