#!/usr/bin/env python3
"""EC48U exact rational certificate: full-LR terminal quotient, coarse-LR loss, future-operation obstruction."""
from fractions import Fraction as F
from collections import defaultdict
from random import Random
import json

rng = Random(48021)

def positive_simplex(n):
    entries = [F(rng.randrange(1, 8)) for _ in range(n)]
    total = sum(entries)
    return [x / total for x in entries]

def random_fraction():
    return F(rng.randrange(1, 8), 8)

def exact_trial():
    n, ni, nm, nj = (rng.randrange(2, 7), rng.randrange(1, 4), rng.randrange(1, 4), rng.randrange(2, 5))
    p_h, q_h = positive_simplex(n), positive_simplex(n)
    s, u = [random_fraction() for _ in range(n)], [random_fraction() for _ in range(n)]
    b_p, b_q = [positive_simplex(ni) for _ in range(n)], [positive_simplex(ni) for _ in range(n)]
    mem = [positive_simplex(nm) for _ in range(n)]
    clone = [[[positive_simplex(nj) for m in range(nm)] for i in range(ni)] for h in range(n)]
    lr = [[p_h[h]*b_p[h][i]/(q_h[h]*b_q[h][i]) for i in range(ni)] for h in range(n)]
    # A legal refined controller only sees (memory, old terminal i, full-history joint LR, clone label).
    keys = set((m,i,lr[h][i],j) for h in range(n) for m in range(nm) for i in range(ni) for j in range(nj))
    accept = {key: random_fraction() for key in keys}
    terminal_p, terminal_q = F(0), F(0)
    groups = defaultdict(lambda: [F(0), F(0)])  # total Q mass; accepted Q mass
    for h in range(n):
        for i in range(ni):
            for m in range(nm):
                q = q_h[h]*(1-s[h])*b_q[h][i]*mem[h][m]
                p = p_h[h]*(1-s[h])*b_p[h][i]*mem[h][m]
                assert p == lr[h][i]*q
                a = sum((clone[h][i][m][j]*accept[m,i,lr[h][i],j] for j in range(nj)), F(0))
                terminal_p += p*a
                terminal_q += q*a
                key = (m,i,lr[h][i])
                groups[key][0] += q
                groups[key][1] += q*a
    original_p, original_q = F(0), F(0)
    for (m,i,lratio),(q_mass, q_accepted) in groups.items():
        a_star = q_accepted/q_mass
        assert F(0) <= a_star <= F(1)
        original_q += q_mass*a_star
        original_p += lratio*q_mass*a_star
    early_p = sum((p_h[h]*s[h]*u[h] for h in range(n)), F(0))
    early_q = sum((q_h[h]*s[h]*u[h] for h in range(n)), F(0))
    tp = sum((p_h[h]*(2-s[h]) for h in range(n)), F(0))
    tq = sum((q_h[h]*(2-s[h]) for h in range(n)), F(0))
    before = (early_p+terminal_p,early_q+terminal_q,tp,tq)
    after = (early_p+original_p,early_q+original_q,tp,tq)
    assert before == after
    return any(len([1 for h in range(n) if lr[h][i]==ratio])>1 for i in range(ni) for ratio in set(lr[h][i] for h in range(n)))

N = 750
collisions = sum(exact_trial() for _ in range(N))
# Minimal coarse-LR witness: H={A,B}, one old signal i, zero persistent bits.
p = (F(3,4), F(1,4)); q = (F(1,4), F(3,4))
r1 = (F(3,4), F(1,4))
refined_p1 = sum((p[h]*r1[h] for h in range(2)),F(0))
refined_q1 = sum((q[h]*r1[h] for h in range(2)),F(0))
assert (refined_p1,refined_q1)==(F(5,8),F(3,8))
assert refined_p1-refined_q1 == F(1,4)
assert sum(p)==sum(q)==1
assert (p[0]/q[0],p[1]/q[1])==(3,F(1,3))
# Strong simulation obstruction even with exact full LR: P=Q uniform, so L=1 on both histories.
common=(F(1,2),F(1,2))
r1_strong=(F(3,4),F(1,4))
real_match = common[0]*r1_strong[0]+common[1]*(1-r1_strong[1])
assert real_match==F(3,4)
for numerator in range(9):
    u=F(numerator,8)
    simulated_match=common[0]*u+common[1]*(1-u)
    assert simulated_match==F(1,2)
report = {
    'schema':'EM_EC48U_EXACT_V1',
    'random_seed':48021,
    'source_neutral_positive_rational_trees_checked':N,
    'four_coordinate_fiber_reconstructions':'PASS',
    'controller_randomization':'source-independent rational private randomization',
    'full_joint_lr_collision_trials':collisions,
    'coarse_lr_counterexample':{'p_h':['3/4','1/4'],'q_h':['1/4','3/4'],'r_j1_given_h':['3/4','1/4'],'refined_accept_j1':[str(refined_p1),str(refined_q1)],'exact_support_gap':'1/4','old_coarse_lr':'1','old_full_history_lr':['3','1/3']},
    'future_relation_counterexample':{'p_h':['1/2','1/2'],'q_h':['1/2','1/2'],'full_lr':['1','1'],'r_j1_given_h':['3/4','1/4'],'true_P_j_equals_h':'3/4','best_observable_fiber_sampler_P_j_equals_h':'1/2','joint_correlation_gap':'1/4'},
    'scope':'Finite strictly positive two-source branch masses, terminal-only accept/reject; finite random tests not a universal proof.',
    'all_assertions':'PASS'
}
print(json.dumps(report,indent=2,sort_keys=True,ensure_ascii=False))
