#!/usr/bin/env python3
"""7-state minimal linear native BRC phase-3 observer for 4-sparse probe.
Frozen input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
import json
from pathlib import Path
import sympy as S
STAR=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple(-v if c>0 else v for v in STAR[a] if v!=abs(c))
P=tuple((a,p,sgn*c) for a in range(4) for c in STAR[a] for sgn in(-1,1) for p in near(a,sgn*c))
I={p:i for i,p in enumerate(P)}
def nxt(i):
 a,p,c=P[i];b=next(j for j in range(4) if j!=a and abs(c) in STAR[j]);return [I[k] for k in [(a,c,v) for v in near(a,c) if v!=p]+[(b,c,v) for v in near(b,c)]]
N=[nxt(i) for i in range(48)];gate_index=I[(0,1,-3)];assert gate_index==4
def Q(z):
 M=S.zeros(48)
 for i,ns in enumerate(N):
  if abs(P[i][2]) in(5,6):continue
  for j in ns:M[i,j]=1 if i==gate_index else (z+3 if j==gate_index else 2)
 return M
A=Q(0);D=Q(1)-A;g=S.symbols('g');assert Q(g)==A+g*D
assert D*D==S.zeros(48)
d=S.zeros(48,1)
for i in (4,11,14,32):d[i]=1
# Basis of all reachable two-gate tails, then arbitrary future gate steps.
E=S.Matrix.hstack(A*A*d,D*A*d,A*D*d,A**3*d,A*A*D*d,A**4*d,A**3*D*d)
rows=(2,3,4,5,16,17,26)
C=E[list(rows),:];assert C.det()==-16384 and E.rank()==7
K=C.inv()*S.eye(48)[list(rows),:]
assert K*E==S.eye(7)
T0=K*A*E; T1=K*D*E
assert A*E==E*T0 and D*E==E*T1
assert sum(bool(x) for x in T0)==13 and sum(bool(x) for x in T1)==4
assert list(T1[1,:])==[2,0,0,4,0,12,4]
assert all(T1[i,j]==0 for i in range(7) if i!=1 for j in range(7))
assert list(S.eye(48)[3,:]*E)==[3,1,0,14,0,28,0]
# The arbitrary future phase-3 trace is jointly observable on the 7D reachable space.
c=S.eye(48)[3,:]*E
O=S.Matrix.vstack(c,c*T0,c*T1,c*T0*T0,c*T1*T0,c*T0*T0*T0,c*T1*T0*T0)
assert O.det()==-2097152
# The two-gate input family spans E1,E2,E3, and closure under T0,T1 spans E1..E7.
initial=S.Matrix.hstack(E[:,0],E[:,1],E[:,2]);assert initial.rank()==3
C1=S.Matrix.hstack(initial,A*initial,D*initial)
C2=S.Matrix.hstack(C1,A*C1,D*C1)
assert C1.rank()==5 and C2.rank()==7
scales=[S.Rational(1),S.Rational(2,3),S.Rational(7,5)]
words=[[S.Integer(k) for k in(0,1,2,3,4,0,1,7,3,2,0,9)],
       [S.Rational(x) for x in(S.Rational(1,2),2,S.Rational(7,3),0,5,S.Rational(13,7),1,0,3,6)]]
phase_equalities=0; phase3_equalities=0; two_step_checks=0
for lam in scales:
 for word in words:
  assert len(word)>=4
  full=lam*d
  for k,gk in enumerate(word):
   full=Q(gk)*full
   if k==1:
    # Q(g2) Q(g1) d = E1 + g2 E2 + g1 E3, since D^2=0.
    state=lam*S.Matrix([1,gk,word[0],0,0,0,0]);two_step_checks+=1
   if k>=1:
    if k>1:state=(T0+gk*T1)*state
    assert E*state==full
    assert (c*state)[0]==full[3]
    phase_equalities+=48;phase3_equalities+=1
assert Q(g)*E==E*(T0+g*T1)
out={
 'schema':'PREFIX614_R2_SEVEN_STATE_NATIVE_PHASE3_V1',
 'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'source_probe_nonzero_indices':[4,11,14,32],
 'basis_words':['AA','DA','AD','AAA','AAD','AAAA','AAAD'],
 'basis_pivot_rows':list(rows),'basis_minor_det':str(C.det()),
 'linear_state_dimension':7,
 'T0':[[str(T0[i,j]) for j in range(7)] for i in range(7)],
 'T1':[[str(T1[i,j]) for j in range(7)] for i in range(7)],
 'phase3_readout':list(map(str,c)),
 'observability_word_rows':['','A','D','AA','DA','AAA','DAA'],
 'observability_det':str(O.det()),
 'two_step_exact_checks':two_step_checks,
 'phase3_exact_checks':phase3_equalities,
 'original48_coordinate_exact_checks':phase_equalities,
 'result':'ALL_ASSERTIONS_PASSED; EXACT_LINEAR_MINIMALITY_CERTIFICATE; INDEPENDENT_REVIEW_PENDING'
}
Path(__file__).with_name('PREFIX614_R2_seven_state_results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k not in ('T0','T1')},indent=2))
