#!/usr/bin/env python3
"""EC49K exact rational evidence. Only auxiliary positive-weight BRC models."""
from fractions import Fraction as F
from itertools import product
from math import isqrt
import json

Z, O = F(0), F(1)

def sources(theta, w, y1, y2):
    pw = (F(1, 4), F(3, 4)) if theta == 'P' else (F(1, 2), F(1, 2))
    py1 = F(3, 4) if theta == 'P' else F(1, 2)
    py2 = ((F(3, 4), F(1, 4)) if theta == 'P'
           else (F(1, 4), F(3, 4)))[w]
    return pw[w] * (py1 if y1 else O-py1) * (py2 if y2 else O-py2)

def expected(theta, q0, q1, a0, a1):
    accept = time = Z
    for w, y1, y2 in product((0, 1), repeat=3):
        mass = sources(theta, w, y1, y2)
        q, a = ((q0, a0), (q1, a1))[w]
        accept += mass * q * y1 * a * y2
        time += mass * (q + q * y1 * a)
    return accept, time

def out(q0, q1, a0, a1):
    alpha, tp = expected('P', q0, q1, a0, a1)
    beta, tq = expected('Q', q0, q1, a0, a1)
    return (alpha, beta, tp, tq)

def flow(q0, q1, a0, a1):
    x0, x1 = q0 / 4, q1 / 4
    return x0, x1, x0 * a0, x1 * a1

def linear_flow(x0, x1, y0, y1):
    return (F(9,16)*(y0+y1), F(1,4)*y0+F(3,4)*y1,
            x0+3*x1+F(3,4)*y0+F(9,4)*y1,
            2*x0+2*x1+y0+y1)

def inverse_flow(v):
    a,b,tp,tq = v
    return (-F(4,3)*a+F(3,2)*b-F(1,2)*tp+F(3,4)*tq,
            F(4,9)*a-F(3,2)*b+F(1,2)*tp-F(1,4)*tq,
            F(8,3)*a-2*b,
            -F(8,9)*a+2*b)

def witness(v):
    a,b,tp,tq = v
    return 4*a-F(11,2)*b+F(1,2)*tp-F(1,4)*tq

def encode(x):
    if isinstance(x, F): return str(x)
    if isinstance(x, (tuple, list)): return [encode(v) for v in x]
    if isinstance(x, dict): return {k:encode(v) for k,v in x.items()}
    return x

leaves = {t:[sources(t,*v) for v in product((0,1),repeat=3)] for t in ('P','Q')}
assert all(len(v)==8 and all(z>0 for z in v) and sum(v)==1 for v in leaves.values())

full_det, coarse_det = [], []
for q0,q1,a0,a1 in product((Z,O),repeat=4):
    o = out(q0,q1,a0,a1)
    assert o==linear_flow(*flow(q0,q1,a0,a1))
    assert inverse_flow(o)==flow(q0,q1,a0,a1)
    full_det.append(witness(o))
for q0,q1,r in product((Z,O),repeat=3):
    o=out(q0,q1,r,r)
    assert witness(o)<=F(1,4)
    coarse_det.append(witness(o))
assert max(full_det)==F(1,2) and max(coarse_det)==F(1,4)

points=[F(i,5) for i in range(6)]
full_grid=coarse_grid=0
for q0,q1,a0,a1 in product(points,repeat=4):
    o=out(q0,q1,a0,a1)
    x0,x1,y0,y1=flow(q0,q1,a0,a1)
    assert o==linear_flow(x0,x1,y0,y1)
    assert inverse_flow(o)==(x0,x1,y0,y1)
    assert witness(o)==x1+y0-y1
    full_grid+=1
for q0,q1,r in product(points,repeat=3):
    o=out(q0,q1,r,r)
    assert witness(o)<=F(1,4)
    coarse_grid+=1

piA=out(O,F(1,2),O,Z)
piMax=out(O,O,O,Z)
assert piA==(F(9,64),F(1,16),F(13,16),O)
assert witness(piA)==F(3,8)
assert piMax==(F(9,64),F(1,16),F(19,16),F(5,4))
assert witness(piMax)==F(1,2)

# Auxiliary hidden-branch fixed-acceptance two-action model.
wp={'P':(F(3,4),F(1,8),F(1,8)), 'Q':(F(1,4),F(3,8),F(3,8))}
assert all(all(z>0 for z in w) and sum(w)==1 for w in wp.values())
def hidden_output(u,v):
    return (wp['P'][0]*u+(wp['P'][1]+wp['P'][2])*v,
            wp['Q'][0]*u+(wp['Q'][1]+wp['Q'][2])*v,
            F(2),F(2))
target=hidden_output(F(1,8),F(1,2))
assert target==(F(7,32),F(13,32),F(2),F(2))
a,b,_,_=target
u=(3*a-b)/2
v=(3*b-a)/2
assert u==F(1,8) and v==F(1,2)
# p+q=1, pq=1/8 implies (p-q)^2=1/2; not a rational square.
D=(2*v)**2-4*u
assert D==F(1,2)
assert isqrt(D.numerator)**2!=D.numerator or isqrt(D.denominator)**2!=D.denominator
# exact Q(sqrt(2)) multiplication: (a+b sqrt2)*(c+d sqrt2).
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y): return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
p=(F(1,2), F(1,4))
q=(F(1,2),-F(1,4))
assert add(p,q)==(F(1),Z) and mul(p,q)==(F(1,8),Z)
# Restoring the first action as memory permits a wholly rational joint law.
p1, q_when_1, q_when_0=F(1,2),F(1,4),F(3,4)
assert p1*q_when_1==u
assert p1*q_when_1+(1-p1)*q_when_0==v

report={
 'status':'EXACT_FRACTION_PASS',
 'model':'EC49J strict-positive 8 P and 8 Q latent leaves; W initially readable, forgotten only at second stage for compressed policy',
 'base_leaf_weights':leaves,
 'deterministic_full':len(full_det),'deterministic_compressed':len(coarse_det),
 'full_rational_grid':full_grid,'compressed_rational_grid':coarse_grid,
 'linear_separator':'4 alpha - 11/2 beta + 1/2 E_P T - 1/4 E_Q T',
 'compressed_max':max(coarse_det),'full_max':max(full_det),
 'sharp_support_gap':max(full_det)-max(coarse_det),
 'EC49J_piA_observation':piA,'EC49J_piA_separator':witness(piA),
 'EC49K_full_max_observation':piMax,
 'irrational_only_restricted_model':{'target':target,'implied_sum':2*v,'implied_product':u,
   'difference_squared':D,'exact_parameters':{'p':'(2+sqrt(2))/4','q':'(2-sqrt(2))/4'},
   'rational_history_aware_repair':{'p1':p1,'q_after_action_1':q_when_1,'q_after_action_0':q_when_0}},
 'scope':'Auxiliary positive rational source kernels, finite two-stage fresh behavioral randomization; not signed-BRC, native X6 or unrestricted perfect-recall policy.'}
print(json.dumps(encode(report),ensure_ascii=False,sort_keys=True,indent=2))
