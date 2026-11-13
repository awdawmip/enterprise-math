#!/usr/bin/env python3
"""EC49J: exact positive-rational, two-adaptive-sensor policy-dependent LR check."""
from fractions import Fraction as F
from itertools import product
import json

W_Q = (F(1,2), F(1,2))
W_P = (F(1,4), F(3,4))
Y1_Q = F(1,2)
Y1_P = F(3,4)
Y2_Q = (F(1,4), F(3,4))
Y2_P = (F(3,4), F(1,4))

def fmt(x):
    return f"{x.numerator}/{x.denominator}"

def path_mass(source, w, y1, y2):
    ww = W_P if source == 'P' else W_Q
    k1 = Y1_P if source == 'P' else Y1_Q
    k2 = Y2_P if source == 'P' else Y2_Q
    return ww[w] * (k1 if y1 else 1-k1) * (k2[w] if y2 else 1-k2[w])

def run(source, q, a):
    """q[w] buys sensor 1; a[w] buys sensor 2 iff Y1=1; accept iff Y2=1."""
    wp = W_P if source == 'P' else W_Q
    p1 = Y1_P if source == 'P' else Y1_Q
    p2 = Y2_P if source == 'P' else Y2_Q
    first = sum(wp[w]*q[w] for w in (0,1))
    second = sum(wp[w]*q[w]*p1*a[w] for w in (0,1))
    accept = sum(wp[w]*q[w]*p1*a[w]*p2[w] for w in (0,1))
    return accept, first+second, first, second

def state(q):
    """Joint source mass and posterior W probabilities at s=(bought Y1,Y1=1)."""
    x0, x1 = q[0]/4, q[1]/4  # Q(s,W=w)
    Q = x0+x1
    P = F(3,4)*x0+F(9,4)*x1
    if Q == 0:
        return None
    m = P/Q
    l, u = F(3,4), F(9,4)
    rho = (u-m)*(m-l)/(m*(u-l))
    tv = abs(x0/Q-F(3,4)*x0/P)
    return Q, P, m, rho, tv, x0, x1

leaves = {(source,w,y1,y2):path_mass(source,w,y1,y2)
          for source,w,y1,y2 in product(('P','Q'),range(2),range(2),range(2))}
assert all(x>0 for x in leaves.values())
assert all(sum(v for (s,*_),v in leaves.items() if s == source) == 1 for source in ('P','Q'))
assert Y1_P != Y1_Q and all(Y2_P[w] != Y2_Q[w] for w in (0,1))

A = (F(1),F(1,2)); B = (F(1,2),F(1))
chosen_a = (F(1),F(0))
SA, SB = state(A), state(B)
assert tuple(SA[:5]) == (F(3,8),F(15,32),F(5,4),F(4,15),F(4,15))
assert tuple(SB[:5]) == (F(3,8),F(21,32),F(7,4),F(4,21),F(4,21))
assert SA[4]>SB[3]  # invalidity of freezing policy-B rho for policy A
assert SA[0]*SA[4] - SA[0]*SB[3] == F(1,35)

out = {}
for name,q in (('A',A),('B',B)):
    p = run('P',q,chosen_a)
    z = run('Q',q,chosen_a)
    s = state(q)
    out[name] = {'q':[fmt(v) for v in q],
                 'O':[fmt(p[0]),fmt(z[0]),fmt(p[1]),fmt(z[1])],
                 'Q_state_mass':fmt(s[0]),'P_state_mass':fmt(s[1]),
                 'm':fmt(s[2]),'rho':fmt(s[3]),'actual_TV':fmt(s[4]),
                 'Q_times_TV':fmt(s[0]*s[4])}
assert out['A']['O'] == ['9/64','1/16','13/16','1/1']
assert out['B']['O'] == ['9/128','1/32','31/32','7/8']

G = [F(k,6) for k in range(7)]
policy_checks = 0
positive_mixture_cases = 0
for q0,q1,a0,a1 in product(G,repeat=4):
    q=(q0,q1); a=(a0,a1)
    if q0+q1==0:
        continue
    s=state(q)
    conditional_Q = (q0*a0+q1*a1)/(q0+q1)
    conditional_P = (q0*a0+3*q1*a1)/(q0+3*q1)
    action_gap = abs(conditional_Q-conditional_P)
    assert action_gap<=s[3]
    if q0*q1>0:
        positive_mixture_cases+=1
        assert s[3] == s[4]
    assert s[0]*s[4] == q0*q1/(2*(q0+3*q1))
    p=run('P',q,a); z=run('Q',q,a)
    expected_P_accept = sum(W_P[w]*q[w]*Y1_P*a[w]*Y2_P[w] for w in (0,1))
    expected_Q_accept = sum(W_Q[w]*q[w]*Y1_Q*a[w]*Y2_Q[w] for w in (0,1))
    assert p[0]==expected_P_accept and z[0]==expected_Q_accept
    assert p[1]==p[2]+p[3] and z[1]==z[2]+z[3]
    policy_checks+=1
assert policy_checks == 2352
assert positive_mixture_cases == 1764

report={'schema':'EC49J_EXACT_FRACTION_REPORT_V1','status':'PASS',
        'checks':{'strict_positive_PQ_terminal_leaves':16,'rational_policy_grid':policy_checks,
                  'strict_mixture_grid_cases':positive_mixture_cases,'grid_denominator':6},
        'policies':out,
        'frozen_m_policy_B_underestimation_for_A':{'policy_B_rho':'4/21',
            'policy_A_true_TV':'4/15','conditional_violation':'8/105',
            'Q_occupation_weighted_violation':'1/35'},
        'scope':'finite auxiliary positive-rational two-source observation tree, not native signed BRC/X6'}
print(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2))
