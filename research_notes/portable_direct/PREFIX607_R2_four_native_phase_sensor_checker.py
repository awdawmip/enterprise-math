#!/usr/bin/env python3
"""PREFIX607 exact native-derived 4-phase-sensor observability with a single nonnegative probe."""
import json
from pathlib import Path
import sympy as sp
STAR=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple(-k if c>0 else k for k in STAR[a] if k!=abs(c))
phases=tuple((a,p,sgn*k) for a in range(4) for k in STAR[a] for sgn in (-1,1) for p in near(a,sgn*k))
index={p:i for i,p in enumerate(phases)}
def N(i):
 a,p,c=phases[i];b=next(k for k in range(4) if k!=a and abs(c) in STAR[k]);return tuple(index[x] for x in ([(a,c,v) for v in near(a,c) if v!=p]+[(b,c,v) for v in near(b,c)]))
g=index[(0,1,-3)];assert g==4 and len(phases)==48
neigh=[N(i) for i in range(48)]
def Q(z):
 M=sp.zeros(48)
 for i,js in enumerate(neigh):
  if abs(phases[i][2]) in (5,6):continue
  for j in js:M[i,j]=1 if i==g else (3+z if j==g else 2)
 return M
A=Q(1);G=Q(2)-A;A2=A*A
cols=list(A2.rref()[1]);assert len(cols)==16
E=A2[:,cols]
rows=list(E.T.rref()[1]);K=E.extract(rows,range(16)).inv()*sp.eye(48).extract(rows,range(48))
T=K*A*E;H=K*G*E
assert E*K*A2==A2 and T**4==16*sp.eye(16)
r,c=next((i,j) for i in range(16) for j in range(16) if H[i,j])
u=H[:,c];h=H[r,:]/H[r,c]
W=sp.Matrix.hstack(u,T*u,T**2*u,T**3*u)
O=sp.Matrix.vstack(h,h*T,h*T**2,h*T**3)
L=(O*W).inv()*O
P=W*L
assert L*W==sp.eye(4) and P*P==P
z=sp.symbols('z')
B=lambda q:sp.Matrix([[0,0,0,4*(q+3)],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
assert L*(T+(z-1)*H)*W==B(z)
assert (sp.eye(16)-P)*H==sp.zeros(16) and H*(sp.eye(16)-P)==sp.zeros(16)
assert (sp.eye(16)-P)*T*P==sp.zeros(16) and P*T*(sp.eye(16)-P)==sp.zeros(16)
assert A*E==E*T and G*E==E*H
probe=sp.ones(48,1)
y0=Q(0)*Q(1)*probe
v0=K*y0;w0=L*v0;f=(sp.eye(16)-P)*v0
assert w0==sp.Matrix([sp.Rational(9,2),4,sp.Rational(3,2),sp.Rational(3,4)])
sensors=(3,4,17,26)
assert (E*W).extract(sensors,range(4))==sp.Matrix([[2,0,0,0],[0,0,0,8],[0,4,0,0],[0,0,8,0]])
for t in range(16):
 b=E*(T**t)*f
 assert tuple(b[i] for i in sensors)==(12*2**t,0,12*2**t,0)
def from_sensors(y,t):
 return sp.Matrix([(y[3]-12*2**t)/2,(y[17]-12*2**t)/4,y[26]/8,y[4]/8])
def prefix_products(u_t,t):
 p=[None]*4
 for j in range(4):
  r=(3-j)%4;count=len(range(r,t,4))
  p[r]=sp.cancel(u_t[(j+t)%4]/(4**count*w0[j]))
 return tuple(p)
def product_direct(q,t):
 p=[sp.Integer(1)]*4
 for j in range(t):p[j%4]*=q[j]+3
 return tuple(p)
words=[tuple(sp.Rational((5*j+1)%11,j%3+1) for j in range(15)),tuple(sp.Integer((7*j+3)%13) for j in range(15)),tuple(sp.Rational(0) if j%4==0 else sp.Rational(7,3) for j in range(15))]
checks=0
for word in words:
 y=y0;u=w0;prev=(sp.Integer(1),)*4
 recovered=[None]*len(word);minimum_recovered=[None]*len(word);min_scalar_readings=0
 for t,q in enumerate(word,1):
  y=Q(q)*y;u=B(q)*u
  assert u==from_sensors(y,t)
  assert prefix_products(from_sensors(y,t),t)==product_direct(word,t)
  checks+=1
  if t%4==0 or t==len(word):
   p=prefix_products(from_sensors(y,t),t)
   lo=t-4 if t%4==0 else 4*(t//4)
   new_prev=list(prev)
   for j in range(lo,t):
    recovered[j]=sp.cancel(p[j%4]/prev[j%4]-3)
    r=j%4;source_coordinate=(3-r)%4;final_coordinate=(source_coordinate+t)%4
    phase_sensor=(3,17,26,4)[final_coordinate]
    raw=y[phase_sensor]
    baseline=12*2**t if phase_sensor in (3,17) else 0
    multiplier=(2,4,8,8)[final_coordinate]
    gate_coordinate=sp.cancel((raw-baseline)/multiplier)
    shift_count=len(range(r,t,4))
    p_r=sp.cancel(gate_coordinate/(4**shift_count*w0[source_coordinate]))
    minimum_recovered[j]=sp.cancel(p_r/prev[r]-3)
    new_prev[r]=p_r;min_scalar_readings+=1
   assert tuple(new_prev)==p
   prev=p
 assert tuple(recovered)==word
 assert tuple(minimum_recovered)==word and min_scalar_readings==len(word)
assert checks==45
out={
 'schema':'PREFIX607_R2_FOUR_NATIVE_PHASE_SENSOR_EXACT_V1',
 'frozen_science':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'source_phase_probe':'48 phase-sum coordinates all 1; nonnegative source implementable by one unit per native port-pair',
 'common_first_two_gates':[0,1],
 'native_phase_sensor_indices_zero_based':list(sensors),
 'gate_sensitive_initial_coordinates':[str(v) for v in w0],
 'native_to_gate_sensitive_sensor_formula':{'u0':'(y3-12*2^t)/2','u1':'(y17-12*2^t)/4','u2':'y26/8','u3':'y4/8'},
 'EW_sensor_matrix':[[int(v) for v in (E*W)[r,:]] for r in sensors],
 'word_lengths':[len(w) for w in words],
 'full_48_phase_probe_state_checks':checks,'prefix_product_checks':checks,
 'min_scalar_sensor_readings_per_word':15,'min_scalar_checkpoints':[4,8,12,15],
 'recovered_complete_gate_words':len(words),
 'theorem':'one fixed nonnegative native-derived phase source + four raw phase sensors at any prefix recover all four products; one per-new-gate reading in gaps <=4 exactly reconstructs n gates',
 'minimality':'n real scalar readings for n independent real gates, optimal among differentiable exact encoding/decoding schemes',
 'status':'AUTHOR_SIDE_EXACT_PROOF_AND_EXECUTED_CHECKS; INDEPENDENT_REVIEW_PENDING',
 'boundary':'phase observer only; not raw tagged source history; initial two gates fixed at 0 and 1'
}
Path(__file__).with_name('PREFIX607_R2_four_native_phase_sensor_results.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print('PREFIX607 PASSED',checks,'native 48-phase probe checks; three recovered 15-gate words')
