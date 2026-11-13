#!/usr/bin/env python3
"""PREFIX-617: exact native BRC eight-state positive lift of every 48 phase sum."""
import json
from pathlib import Path
import sympy as s
STAR=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c): return tuple(-v if c>0 else v for v in STAR[a] if v!=abs(c))
P=tuple((a,p,sgn*c) for a in range(4) for c in STAR[a] for sgn in (-1,1) for p in near(a,sgn*c))
I={v:i for i,v in enumerate(P)}
def nxt(i):
 a,p,c=P[i]
 b=next(j for j in range(4) if j!=a and abs(c) in STAR[j])
 return [I[k] for k in [(a,c,v) for v in near(a,c) if v!=p]+[(b,c,v) for v in near(b,c)]]
N=[nxt(i) for i in range(48)]
gate_index=I[(0,1,-3)]
assert len(P)==48 and gate_index==4
def Q(g):
 M=s.zeros(48)
 for i,ns in enumerate(N):
  if abs(P[i][2]) in (5,6): continue
  for j in ns: M[i,j]=1 if i==gate_index else (g+3 if j==gate_index else 2)
 return M
A=Q(0);D=Q(1)-A;g=s.symbols('g')
assert Q(g)==A+g*D
d=s.zeros(48,1)
for i in (4,11,14,32): d[i]=1
HC=s.zeros(48,4)
groups=((2,3,15),(5,28,29),(27,38,39),(16,17,41))
for j,rows in enumerate(groups):
 for i in rows: HC[i,j]=1
HB=s.zeros(48,4)
gate_rows={0:{3:1,14:1,15:1},1:{17:2,40:2,41:2},2:{26:4,27:4,39:4},3:{4:4,5:8,29:8}}
for j,rows in gate_rows.items():
 for i,weight in rows.items(): HB[i,j]=weight
H=HC.row_join(HB)
cycle=s.Matrix([[0,0,0,1],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
C=2*cycle
B=lambda g:s.Matrix([[0,0,0,4*(g+3)],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
M8=lambda g:s.diag(C,B(g))
assert A*HC==HC*C and D*HC==s.zeros(48,4)
assert A*HB==HB*B(0) and D*HB==HB*(B(1)-B(0))
assert Q(g)*H==H*M8(g)
assert H.rank()==8 and all(v>=0 for v in H) and all(v>=0 for v in M8(0))
ell=s.Matrix([[-1,1,-1,1,0,0,0,0]])
assert ell*M8(g)==-2*ell
def u0(a,b,lam=1):return lam*s.Matrix([0,0,4,4,3+b,3+a,1,s.Rational(1,2)])
a,b,lam=s.symbols('a b lam')
assert s.simplify(H*u0(a,b,lam)-lam*Q(b)*Q(a)*d)==s.zeros(48,1)
assert ell*u0(a,b,lam)==s.zeros(1,1)
E=s.Matrix.hstack(A*A*d,D*A*d,A*D*d,A**3*d,A*A*D*d,A**4*d,A**3*D*d)
rows=[2,3,4,5,16,17,26]
minor=E[rows,:].det()
assert minor==-16384
K=E[rows,:].inv()*s.eye(48)[rows,:]
T0=K*A*E;T1=K*D*E
assert A*E==E*T0 and D*E==E*T1
h=s.eye(48)[3,:]
O=s.Matrix.vstack(*[h*E*W for W in (s.eye(7),T0,T1,T0*T0,T1*T0,T0**3,T1*T0*T0)])
assert O.det()==-2097152 and s.trace(T0*T0)==-4
R0=s.Matrix.hstack(E[:,0],E[:,1],E[:,2])
R1=s.Matrix.hstack(R0,A*R0,D*R0)
R2=s.Matrix.hstack(R1,A*R1,D*R1)
assert (R0.rank(),R1.rank(),R2.rank())==(3,5,7)
initials=[(0,0),(1,2),(s.Rational(2,3),s.Rational(9,7)),(5,0)]
words=[[0,1,2,3,4,0,1,7,3,2,0,9],
 [s.Rational(1,2),2,s.Rational(7,3),0,5,s.Rational(13,7),1,0,3,6],
 [0]*11,[s.Rational(13,5),s.Rational(1,17),0,1,s.Rational(7,11),5,0,2]]
scales=[1,s.Rational(2,3),s.Rational(7,5)]
checks=0; phases=0; nonneg=0; maxbits=0
for av,bv in initials:
 for word in words:
  for scale in scales:
   x=scale*Q(bv)*Q(av)*d; z=u0(av,bv,scale)
   for gate in [None]+word:
    if gate is not None: x=Q(gate)*x;z=M8(gate)*z
    assert H*z==x
    assert all(v>=0 for v in z) and all(v>=0 for v in x)
    checks+=1;phases+=48;nonneg+=56
    for v in list(x)+list(z):
     v=s.Rational(v);maxbits=max(maxbits,int(v.p).bit_length(),int(v.q).bit_length())
out={'schema':'PREFIX617_R2_NATIVE48_POSITIVE_EIGHT_STATE_V1',
 'freeze_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'probe_support':[4,11,14,32],
 'baseline_output_groups':[list(x) for x in groups],
 'gate_output_sparse_rows':{str(k):{str(i):w for i,w in r.items()} for k,r in gate_rows.items()},
 'symbolic_Qg_H_equals_H_Mg':True,'symbolic_initial_48_equals_H_u8':True,
 'H_rank':int(H.rank()),'H_nonzero_entries':sum(int(bool(v)) for v in H),
 'Q0_nonzero_entries':sum(int(bool(v)) for v in A),
 'accessible_invariant_hyperplane':'-c0+c1-c2+c3=0',
 'full48_signed_linear_minimum':7,'full48_positive_linear_minimum':8,
 'signed_reachable_minor':str(minor),'scalar_phase3_observability_minor':str(O.det()),
 'seven_state_trace_square':str(s.trace(T0*T0)),'tests':len(initials)*len(words)*len(scales),
 'complete_native_states_checked':checks,'exact_phase_equalities':phases,
 'nonnegative_value_checks':nonneg,'max_rational_bit_length':maxbits,
 'status':'ALL_EXACT_ASSERTIONS_PASSED; AUTHOR_SIDE; INDEPENDENT_REVIEW_PENDING'}
Path(__file__).with_name('PREFIX617_R2_native48_positive_eight_state_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
