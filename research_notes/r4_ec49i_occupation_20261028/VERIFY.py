#!/usr/bin/env python3
"""EC49I: exact-rational occupation budget and likelihood-ratio stress tests."""
from fractions import Fraction as F
from itertools import product
import json

zero, one = F(0), F(1)
q = ((F(22,48), F(15,48), F(11,48)),
     (F(26,48), F(9,48), F(13,48)))
p = ((F(11,48), F(15,48), F(22,48)),
     (F(13,48), F(9,48), F(26,48)))
qbar = tuple((q[0][j] + q[1][j])/2 for j in range(3))
pbar = tuple((p[0][j] + p[1][j])/2 for j in range(3))

# Action 0 = immediate reject, 1 = immediate accept,
# 2..9 = buy ternary signal then accept the mask indexed by action-2.
actions = list(range(10))
def is_buy(action): return action >= 2
def mask_bit(action, y): return int(bool((action-2) & (1 << y)))

def full_outcome(src, pair):
    accept = zero
    buy = zero
    for w, action in enumerate(pair):
        if action == 1: accept += F(1,2)
        if is_buy(action):
            buy += F(1,2)
            accept += F(1,2)*sum(src[w][y]*mask_bit(action,y) for y in range(3))
    return (accept, buy)

def compiled_outcome(src_bar, pair):
    # Q-conditional terminal acceptance is the unique source-neutral compiler
    # because the likelihood ratio for each Y is independent of W.
    buy = F(sum(is_buy(a) for a in pair), 2)
    immediate_accept = F(sum(a == 1 for a in pair), 2)
    final = zero
    for y in range(3):
        numerator = sum(q[w][y] * mask_bit(a,y) for w,a in enumerate(pair) if is_buy(a))
        denominator = sum(q[w][y] for w,a in enumerate(pair) if is_buy(a))
        conditional_accept = numerator/denominator if denominator else zero
        final += buy*src_bar[y]*conditional_accept
    return (immediate_accept+final,buy)

assert all(sum(row)==1 and all(v>0 for v in row) for src in (q,p) for row in src)
assert all(p[w][y]/q[w][y]==(F(1,2),one,F(2))[y] for w in range(2) for y in range(3))
assert qbar == (F(1,2),F(1,4),F(1,4))
assert pbar == (F(1,4),F(1,4),F(1,2))
assert all(sum(abs(src[w][y]-bar[y]) for y in range(3))/2 == F(1,16)
           for src,bar in ((p,pbar),(q,qbar)) for w in range(2))

max_p = zero
max_q = zero
max_clock = zero
strict_cases = 0
for pair in product(actions, repeat=2):
    pf, pclock = full_outcome(p,pair)
    qf, qclock = full_outcome(q,pair)
    pr, prclock = compiled_outcome(pbar,pair)
    qr, qrclock = compiled_outcome(qbar,pair)
    buy = F(sum(is_buy(a) for a in pair),2)
    budget = buy/F(16)
    ep, eq = abs(pf-pr),abs(qf-qr)
    assert ep <= budget and eq <= budget
    assert pclock == prclock == qclock == qrclock
    max_p,max_q,max_clock=max(max_p,ep),max(max_q,eq),max(max_clock,abs(pclock-prclock))
    strict_cases += int(ep>0 or eq>0)

# A sharp nonconstant-LR fiber; full observer sees W and source-neutral chooses A iff W=high.
L,U,m=F(1,3),F(3),one
Q=(F(3,4),F(1,4))  # W=low,high
P=(F(1,4),F(3,4))
assert sum(Q)==sum(P)==1
assert (P[0]/Q[0],P[1]/Q[1]) == (L,U)
TV=sum(abs(x-y) for x,y in zip(P,Q))/2
sharp=(U-m)*(m-L)/(m*(U-L))
uniform=(F(1,1)-L) / (F(1,1)+L) # sqrt(U)=3sqrt(L) => 1/2
old_rho=min(one,(U-L)/(2*L))
assert TV==sharp==uniform==F(1,2) and old_rho==1
pi_Q_A=Q[1]; pi_P_A=P[1]
assert abs(pi_P_A-pi_Q_A)==TV

# A second rational fiber with non-maximal m verifies mean-dependent improvement.
L2,U2,m2=F(1,2),F(2),F(5,4)
Q_hi=(m2-L2)/(U2-L2)
Q2=(1-Q_hi,Q_hi)
P2=tuple(r*x/m2 for r,x in zip((L2,U2),Q2))
sharp2=(U2-m2)*(m2-L2)/(m2*(U2-L2))
assert sum(P2)==1 and sum(Q2)==1
# Embed the conditional fiber in a globally normalized positive three-leaf model.
Q_global=(F(2,5)*Q2[0],F(2,5)*Q2[1],F(3,5))
P_global=(F(2,5)*m2*P2[0],F(2,5)*m2*P2[1],F(1,2))
assert sum(Q_global)==sum(P_global)==1 and all(x>0 for x in Q_global+P_global)
assert tuple(P_global[j]/Q_global[j] for j in range(2))==(L2,U2)
assert sum(abs(x-y) for x,y in zip(P2,Q2))/2 == sharp2==F(3,10)

print(json.dumps({
    'scope':'finite positive rational dual-source auxiliary BRC; no signed native X6',
    'exhaustive_visible_pure_policies':100,
    'initial_hidden_histories':2,
    'max_compiled_accept_error_P':str(max_p),
    'max_compiled_accept_error_Q':str(max_q),
    'max_compiled_clock_error':str(max_clock),
    'nonzero_accept_error_policies':strict_cases,
    'one_W_buy_occupation_budget':str(F(1,32)),
    'previous_uniform_per_stage_budget':str(F(1,16)),
    'LR_example_Q_low_high':[str(x) for x in Q],
    'LR_example_P_low_high':[str(x) for x in P],
    'LR_example_sharp_TV':str(TV),
    'LR_example_old_rho':str(old_rho),
    'LR_example_source_neutral_action_gap':str(abs(pi_P_A-pi_Q_A)),
    'nonmaximal_LR_fiber_sharp_TV':str(sharp2),
    'status':'EXACT_FRACTION_ASSERTIONS_PASS'
},indent=2,ensure_ascii=False,sort_keys=True))
