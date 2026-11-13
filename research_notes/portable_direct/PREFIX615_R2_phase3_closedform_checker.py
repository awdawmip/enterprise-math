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
# PREFIX-615 extension: 1+2+4 splitting and one-residue closed-form.
# Parent code above reconstructs frozen original 48-phase Q, E, T0/T1.
S7=S.Matrix([
 [S.Rational(1,2),S.Rational(1,2),-1,0,0,0,0],
 [-3,0,0,1,0,0,0],
 [-S.Rational(9,4),-S.Rational(3,4),S.Rational(3,2),0,1,0,0],
 [0,0,1,0,0,0,0],
 [-S.Rational(7,8),-S.Rational(1,8),-S.Rational(5,4),0,0,1,0],
 [S.Rational(1,8),-S.Rational(1,8),-S.Rational(1,4),0,0,0,0],
 [-S.Rational(5,8),S.Rational(1,8),S.Rational(1,4),0,0,0,1]])
assert S7.det()==-S.Rational(1,8)
z=S.symbols('z')
block=S.diag(S.Matrix([[2]]),S.Matrix([[0,-4],[1,0]]),
 S.Matrix([[0,0,0,4*(z+3)],[1,0,0,0],[0,1,0,0],[0,0,1,0]]))
assert S7.inv()*(T0+z*T1)*S7==block
assert c*S7==S.Matrix([[2,-2,4,1,0,0,0]])
a,b=S.symbols('a b')
assert S7.inv()*S.Matrix([1,b,a,0,0,0,0])==S.Matrix([1,1,0,3+b,3+a,1,S.Rational(1,2)])
x=S.symbols('x')
assert S.factor((T0+z*T1).charpoly(x).as_expr())==(x-2)*(x*x+4)*(x**4-4*z-12)

def scalar_formula(a,b,word,lam):
 t=len(word);r=t%4;w=(3+b,3+a,S.Integer(1),S.Rational(1,2))
 product=S.Integer(1)
 for s,q in enumerate(word,1):
  if s%4==r:product*=4*(q+3)
 return S.expand(lam*((0,8,16,0)[r]*16**(t//4)+w[(-t)%4]*product))

def streaming_formula(a,b,word,lam):
 p=[S.Integer(1)]*4;out=[];w=(3+b,3+a,S.Integer(1),S.Rational(1,2))
 for t,q in enumerate(word,1):
  r=t%4;p[r]*=4*(q+3)
  out.append(S.expand(lam*((0,8,16,0)[r]*16**(t//4)+w[(-t)%4]*p[r])))
 return out

cases=[(S.Integer(0),S.Integer(1),S.Integer(1),[S.Integer(v) for v in (1,0,7,4,3,0,1,6,2,5,1,4,0,2)]),
 (S.Rational(2,3),S.Rational(7,4),S.Rational(3,5),[S.Rational(n,d) for n,d in ((3,7),(4,5),(0,1),(1,3),(15,8),(4,1),(0,1),(11,5),(2,9),(0,1),(17,6))]),
 (S.Integer(3),S.Integer(0),S.Rational(9,7),[S.Integer(0)]*12),
 (S.Rational(11,5),S.Rational(7,2),S.Integer(2),[S.Rational(i+1,i+2) for i in range(19)])]
full_checks=scalar_checks=stream_checks=0
for aa,bb,lam,word in cases:
 full=Q(bb)*Q(aa)*(lam*d)
 coord=lam*S.Matrix([1,bb,aa,0,0,0,0])
 prefix=streaming_formula(aa,bb,word,lam)
 for t in range(len(word)+1):
  if t:
   full=Q(word[t-1])*full
   coord=(T0+word[t-1]*T1)*coord
  assert E*coord==full
  full_checks+=48
  assert full[3]==scalar_formula(aa,bb,word[:t],lam)
  scalar_checks+=1
  if t:
   assert full[3]==prefix[t-1]
   stream_checks+=1
assert (full_checks,scalar_checks,stream_checks)==(2880,60,56)
result={
 'schema':'PREFIX615_R2_1PLUS2PLUS4_PHASE3_EXACT_V1',
 'frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'input_probe_support':[4,11,14,32],
 'matrix_nonzeros_original_Q0':sum(bool(v) for v in A),
 'matrix_nonzeros_T0_T1':[sum(bool(v) for v in T0),sum(bool(v) for v in T1)],
 'S7_determinant':str(S7.det()),
 'phase3_row_in_block':['2','-2','4','1','0','0','0'],
 'tail_coordinates':['1','1','0','3+b','3+a','1','1/2'],
 'characteristic_polynomial':'(x-2)(x^2+4)(x^4-4z-12)',
 'phase3_baseline_mod4':['0','8*16^k','16*16^k','0'],
 'exact_full_48_phase_equality_checks':full_checks,
 'exact_phase3_scalar_checks':scalar_checks,
 'exact_streaming_prefix_checks':stream_checks,
 'status':'AUTHOR_SIDE_EXECUTED_ALL_EXACT_ASSERTIONS_PASS;INDEPENDENT_REVIEW_PENDING'}
Path(__file__).with_name('PREFIX615_R2_phase3_closedform_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps(result,indent=2))
