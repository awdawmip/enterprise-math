"""Exact rational certificate for R5's 14-leaf terminal-LR transport and time shadows.

Runs with Python 3 standard library only; no external network or floating point.
This checker is an author-side finite computation, not a native Enterprise Math review.
"""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product

ZERO, ONE = F(0), F(1)
R1 = {"a": F(2), "b": F(1, 2)}
Q1 = {"a": F(1, 3), "b": F(2, 3)}
Q2 = {"u": F(1, 8), "v": F(1, 8), "w": F(3, 4)}
R2 = {(h, k): (F(1) if k != "w" else (F(7, 3) if h == "a" else F(1, 3)))
      for h in Q1 for k in Q2}
S = {("a", "u"): F(1, 10), ("a", "v"): F(2, 5),
     ("b", "u"): F(1, 5), ("b", "v"): F(3, 10)}
Y = (F(1, 2), F(1), F(3, 2))
BETA, GAMMA = F(3, 4), F(11, 200)

leaves = []
for h in Q1:
    for k in Q2:
        if k == "w":
            kernel = [(R2[(h, k)], ONE)]
        else:
            s = S[(h, k)]
            kernel = [(Y[0], s), (Y[1], ONE - 2*s), (Y[2], s)]
        assert sum((prob for _, prob in kernel), ZERO) == ONE
        assert sum((y * prob for y, prob in kernel), ZERO) == R2[(h, k)]
        for y, prob in kernel:
            q = Q1[h] * Q2[k] * prob
            leaves.append((h, k, y, q))

assert len(leaves) == 14
assert all(q > 0 for _, _, _, q in leaves)
assert sum((q for _, _, _, q in leaves), ZERO) == ONE
assert sum((y*q for _, _, y, q in leaves), ZERO) == ONE
assert sum((Q1[h]*Q2[k]*R2[(h,k)] for h in Q1 for k in Q2), ZERO) == ONE


def obs(c1, c2, decision):
    """c1[h], c2[(h,k)] are continuation probabilities; decision is Q-label rate."""
    e_p = e_q = t_p = t_q = ZERO
    for h, k, y, q in leaves:
        z1, z2 = c1[h], c2[(h, k)]
        assert ZERO <= z1 <= ONE and ZERO <= z2 <= ONE
        a1, a2, a3 = decision(h, k, y)
        assert all(ZERO <= x <= ONE for x in (a1,a2,a3))
        w1, w2, w3 = ONE-z1, z1*(ONE-z2), z1*z2
        dq = w1*a1 + w2*a2 + w3*a3
        time = w1 + 2*w2 + 3*w3
        e_p += y*q*dq
        e_q += q*(ONE-dq)
        t_p += y*q*time
        t_q += q*time
    return (e_p,e_q,t_p,t_q)


def bayes(h,k,y):
    return (F(int(R1[h]<BETA)),F(int(R2[(h,k)]<BETA)),F(int(y<BETA)))

full_c1 = {"a": ZERO, "b": ONE}
full_c2 = {(h,k): F(int((h,k)==("b","v"))) for h in Q1 for k in Q2}
full_o = obs(full_c1,full_c2,bayes)
assert full_o == (F(43,240),F(19,40),F(17,12),F(7,4)), full_o

q_y=defaultdict(lambda:ZERO)
q_decide_q_y=defaultdict(lambda:ZERO)
for h,k,y,q in leaves:
    z1,z2 = full_c1[h],full_c2[(h,k)]
    a1,a2,a3 = bayes(h,k,y)
    dq = (ONE-z1)*a1 + z1*(ONE-z2)*a2 + z1*z2*a3
    q_y[y] += q
    q_decide_q_y[y] += q*dq
assert dict(sorted(q_y.items())) == {
    F(1,3):F(1,2),F(1,2):F(1,16),F(1):F(1,8),
    F(3,2):F(1,16),F(7,3):F(1,4)}
theta={y:q_decide_q_y[y]/q_y[y] for y in q_y}
assert theta=={F(1,3):ONE,F(1,2):F(2,5), F(1):ZERO,
               F(3,2):ZERO,F(7,3):ZERO},theta
full_continue1 = {h:ONE for h in Q1}
full_continue2 = {(h,k):ONE for h in Q1 for k in Q2}
terminal_o = obs(full_continue1,full_continue2,
                  lambda h,k,y:(ZERO,ZERO,theta[y]))
assert terminal_o == (F(43,240),F(19,40),F(3),F(3)),terminal_o

# At t=2, the only reached LR collision after a stops is bu,bv.
# Both have Q arrival mass 1/12, and a full strategy continues only bv.
# Its aggregate continuing mass is 1/12, so its seedless continuation is 1/2.
comp_c1={"a":ZERO,"b":ONE}
comp_c2={(h,k):(F(1,2) if R2[(h,k)]==ONE else ZERO)
         for h in Q1 for k in Q2}
p_target=full_o[0]
q_target=ONE-full_o[1]
comp_p_o=obs(comp_c1,comp_c2,lambda h,k,y:(p_target,p_target,p_target))
comp_q_o=obs(comp_c1,comp_c2,lambda h,k,y:(q_target,q_target,q_target))
assert comp_p_o==(F(43,240),F(197,240),F(17,12),F(7,4)),comp_p_o
assert comp_q_o==(F(21,40),F(19,40),F(17,12),F(7,4)),comp_q_o

# Exact error-only zonotope support for alpha=1, beta=3/4.
err_min=BETA+sum((q*min(ZERO,y-BETA) for y,q in q_y.items()),ZERO)
assert err_min==F(101,192),err_min

# Independent finite strategy-vertex check of the previously published
# full-vs-seedless 14-leaf *four-observer* support gap.
def J(o):return o[0]+BETA*o[1]+GAMMA*o[3]
full_vals=[]
for bits in product((ZERO,ONE),repeat=8):
    x={"a":bits[0],"b":bits[1]}
    y={(h,k):bits[2+i] for i,(h,k) in enumerate((h,k) for h in Q1 for k in Q2)}
    full_vals.append(J(obs(x,y,bayes)))
seedless_vals=[]
for bits in product((ZERO,ONE),repeat=5):
    x={"a":bits[0],"b":bits[1]}
    y={(h,k):bits[2+list(sorted(set(R2.values()))).index(R2[(h,k)])]
       for h in Q1 for k in Q2}
    seedless_vals.append(J(obs(x,y,bayes)))
assert len(full_vals)==256 and len(seedless_vals)==32
assert min(full_vals)==F(379,600),min(full_vals)
assert min(seedless_vals)==F(1517,2400),min(seedless_vals)
assert min(seedless_vals)-min(full_vals)==F(1,2400)
assert J(full_o)==min(full_vals)
print('LEAVES=14, STRICT_POSITIVE_AND_LR_CONSERVATION=PASS')
print('FULL_FOUR_VECTOR='+str(full_o))
print('TERMINAL_ONLY_FOUR_VECTOR='+str(terminal_o))
print('TERMINAL_Q_LR_MASSES='+str(sorted(q_y.items())))
print('TERMINAL_Q_DECISION_RATE='+str(sorted(theta.items())))
print('SEEDLESS_MATCH_EP_TIME='+str(comp_p_o))
print('SEEDLESS_MATCH_EQ_TIME='+str(comp_q_o))
print('ERROR_ONLY_SIGNED_SUPPORT='+str(err_min))
print('FULL_DETERMINISTIC_STOP_PATTERNS='+str(len(full_vals)))
print('SEEDLESS_DETERMINISTIC_STOP_PATTERNS='+str(len(seedless_vals)))
print('FULL_SUPPORT_MIN='+str(min(full_vals)))
print('SEEDLESS_SUPPORT_MIN='+str(min(seedless_vals)))
print('FOUR_OBSERVER_SUPPORT_GAP='+str(min(seedless_vals)-min(full_vals)))
print('ALL EXACT CHECKS PASSED')
