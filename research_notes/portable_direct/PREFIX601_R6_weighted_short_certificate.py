#!/usr/bin/env python3
"""PREFIX-601: exact 12-incidence weighted phase discriminant. Run in portable_direct."""
import io, runpy, json
from contextlib import redirect_stdout
from fractions import Fraction as F
with redirect_stdout(io.StringIO()): d=runpy.run_path('PREFIX600_R6_compact_native_certificate.py')
W,U,V,J,Wi,E,ei,plus=d['W'],d['U'],d['V'],d['J'],d['Wi'],d['E'],d['ei'],d['plus']
assert len(E)==12 and d['mul'](V,d['mul'](Wi,U))==[[2*x for x in row] for row in J]
pairs=[(i,row.index(1)) for i,row in enumerate(J) if i<row.index(1)]
assert len(pairs)==6

def mul(A,B):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)]
def test(t):
 B=[[F(W[i][j])+sum(F(U[i][e])*t[e]*V[e][j] for e in range(12)) for j in range(24)] for i in range(24)]
 A=[[F(i==j)+2*J[i][j]*t[j] for j in range(12)] for i in range(12)]
 assert mul(V,mul(Wi,[[U[i][e]*t[e] for e in range(12)] for i in range(24)]))==[[A[i][j]-F(i==j) for j in range(12)] for i in range(12)]
 D=F(1);k=0
 for i,j in pairs:
  f=1-4*t[i]*t[j];D*=f;k+=(f==0)
 s=[1+2*t[next(e for e in range(12) if U[i][e])] for i in range(24)]
 assert [sum(row) for row in B]==s and all(x>=0 for row in B for x in row)
 if k==0:
  H=[[F(i==j) for j in range(12)] for i in range(12)]
  for i,j in pairs:
   f=1-4*t[i]*t[j]
   H[i][i]=H[j][j]=1/f;H[i][j]=-2*t[j]/f;H[j][i]=-2*t[i]/f
  Inv=[[F(Wi[i][j])-x for j,x in enumerate(row)] for i,row in enumerate(mul(mul(mul(Wi,U),[[t[i]*x for x in r] for i,r in enumerate(H)]),mul(V,Wi)))]
  assert mul(B,Inv)==[[F(i==j) for j in range(24)] for i in range(24)]
 else:
  for i,j in pairs:
   if 4*t[i]*t[j]==1:
    z=[F(0)]*12;z[i]=1;z[j]=-2*t[i]
    assert [sum(A[r][c]*z[c] for c in range(12)) for r in range(12)]==[0]*12
    x=[-sum(Wi[r][q]*U[q][e]*t[e]*z[e] for q in range(24) for e in range(12)) for r in range(24)]
    assert any(x) and [sum(B[r][c]*x[c] for c in range(24)) for r in range(24)]==[0]*24
 return {'det_B':str(D),'rank_B':24-k,'rank_M':48-2*k}

one=[F(1)]*12
critical=one.copy()
for i,j in pairs[:2]:critical[i]=critical[j]=F(1,2)
r=[test(t) for t in (one,[F(0)]*12,[F(i+1,i+3) for i in range(12)],critical,[F(1,2)]*12)]
assert r[0]['det_B']=='729' and r[3]['rank_M']==44 and r[4]['rank_M']==36
print(json.dumps({'status':'ALL_CHECKS_PASS','science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d','source':'PREFIX565 via PREFIX600','cases':r},indent=2))
