#!/usr/bin/env python3
"""Exact Fraction certificate for EC49FUB phase-interface mass and Wasserstein jump.
Independent of native Bellman execution; verifies algebra of the inherited price chart.
Python standard library only.
"""
import json
from fractions import Fraction as F

M = F(1469,64)
E = F(1048576,18958647)
L = (8*M + 173)/480
U = F(3,4)
C = F(16,945)
D = F(49,64) - (740-M)/945
ALPHA, BETA = F(525,8), F(35,32)

def integral_pow(k):
    return (U**(k+1)-L**(k+1))/(k+1)

A0 = C*integral_pow(0)
A1 = C*M*integral_pow(1)
B0 = D/54
P_ATOM = M*U + (M*BETA + U*ALPHA)*D/2 + ALPHA*BETA*D**2/3
B1 = B0*P_ATOM
J0 = C*(U*integral_pow(0)-integral_pow(1))
J1 = C*M*(U*integral_pow(1)-integral_pow(2))

def prob_atom(e):
    return (B0-e*B1)/((A0+B0)-e*(A1+B1))

def cont_mean(e):
    return (C*integral_pow(1)-e*C*M*integral_pow(2))/(A0-e*A1)

def jump_w1(e):
    return prob_atom(e)*(U-cont_mean(e))

# Exact polynomial arithmetic, coefficient list ascending degree.
def p_mul(a,b):
    c = [F(0)]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b): c[i+j]+=ai*bj
    return c

def p_sub(a,b):
    return [(a[i] if i<len(a) else F(0))-(b[i] if i<len(b) else F(0)) for i in range(max(len(a),len(b)))]

def p_der(a):
    return [a[i]*i for i in range(1,len(a))]

Q_NUM = [F(-575*2359296),F(575*41217719)]
Q_DEN = [F(-2630615040),F(45529434409)]
W_NUM = p_mul([F(-40960),F(700713)],[F(-2359296),F(41217719)])
W_DEN = p_mul([F(-163840),F(2807259)],[F(-2630615040),F(45529434409)])
W_FACTOR = F(1035,128)

assert p_mul([B0,-B1],Q_DEN) == p_mul([A0+B0,-A1-B1],Q_NUM)
assert p_mul(p_mul([B0,-B1],[J0,-J1]),W_DEN) == [v*W_FACTOR for v in p_mul(p_mul([A0+B0,-A1-B1],[A0,-A1]),W_NUM)]

DNUM = p_sub(p_mul(p_der(W_NUM),W_DEN),p_mul(W_NUM,p_der(W_DEN)))
Q_POLY = [F(230358520503572889600),F(-7863342704812535316480),F(67100590040566349370337)]
assert [W_FACTOR*x for x in DNUM[:3]] == [-198720*x for x in Q_POLY]
assert all(x==0 for x in DNUM[3:])

def eval_poly(a,e):
    return sum((coef*e**i for i,coef in enumerate(a)),F(0))

assert E<F(1,18)
assert eval_poly(Q_POLY,F(1,18)) == F(196581997098329904097,324)>0
assert Q_POLY[1]+2*Q_POLY[2]*F(1,18) <0
assert A0-E*A1>0 and B0-E*B1>0
assert A0>0 and B0>0
assert P_ATOM > M*U
assert A1/A0 < M*U
assert prob_atom(F(0))==F(115,223)
assert prob_atom(E)==F(3310244525,8132285009)
assert jump_w1(F(0))==F(207,114176)
assert jump_w1(E)==F(10133262941675265,6885347826098094592)

q_inf = B1/(A1+B1)
w_inf = B1*J1/(A1*(A1+B1))
assert q_inf == F(23700188425,45529434409)
assert w_inf == F(6782993927235,3712287963972224)
assert prob_atom(E) < prob_atom(F(0)) < q_inf
assert jump_w1(E) < jump_w1(F(0)) < w_inf

checks=0
for e in [F(-10000),F(-100),F(-1),F(0),E/3,E/2,E]:
    assert 0<prob_atom(e)<1 and jump_w1(e)>0
    assert (B0-e*B1)>0 and A0-e*A1>0
    assert jump_w1(e) == (B0-e*B1)*(J0-e*J1)/(((A0+B0)-e*(A1+B1))*(A0-e*A1))
    checks += 1

record = {
  'schema':'EC49FUB_CLIP_INTERFACE_EXACT_CERT_V1',
  'parent':'EC49FUA; GitHub PR #2815 @71564c619d245e007634c9dd80bc8ed4fe052fb1',
  'frozen_science_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
  'm_interface':str(M), 'continuous_L':str(L), 'U':str(U), 'fiber_width':str(U-L),
  'clipping_fiber_length':str(D),
  'A0':str(A0),'A1':str(A1),'B0':str(B0),'B1':str(B1),
  'J0':str(J0),'J1':str(J1),'atom_mean_price_weight':str(P_ATOM),
  'top_atom_probability_epsilon_0':str(prob_atom(F(0))),
  'top_atom_probability_epsilon_E':str(prob_atom(E)),
  'top_atom_probability_epsilon_minus_infinity_limit':str(q_inf),
  'W1_jump_epsilon_0':str(jump_w1(F(0))),
  'W1_jump_epsilon_E_sharp_uniform_lower_bound':str(jump_w1(E)),
  'W1_jump_epsilon_minus_infinity_limit':str(w_inf),
  'epsilon_domain':'(-infinity,1048576/18958647]',
  'Q_at_1_over_18':str(eval_poly(Q_POLY,F(1,18))),
  'symbolic_rational_identity_verified':True,
  'symbolic_derivative_identity_verified':True,
  'finite_regression_cases':checks,
  'proof_scope':'conditional one-sided law at m2 under inherited price-chart and native Bellman branch',
  'scientific_status':'AUTHOR_PROVED_EXACT_RATIONAL_CHECKED_PARENT_DEPENDENT_NOT_REVIEWED',
  'native_BRC_recomputed':False,
  'formal_result_or_review':False
}
print(json.dumps(record,ensure_ascii=False,indent=2,sort_keys=True))
