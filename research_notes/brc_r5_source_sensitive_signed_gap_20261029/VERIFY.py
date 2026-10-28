#!/usr/bin/env python3
"""Exact rational regression for the R5 heterogeneous merged-tail signed gap.

The all-real upper bound is proved algebraically in the companion Markdown;
finite regression is not substituted for that proof.
"""
from fractions import Fraction as F
from itertools import product
from random import Random
import json

S = (F(1, 2), F(1), F(3, 2), F(5, 2))
A = F(1, 4)
MU = {
    'A': tuple(map(F, ('7/50', '11/75', '1/2', '16/75'))),
    'B': tuple(map(F, ('17/200', '23/150', '3/5', '97/600'))),
}
NU = {
    'A': {
        'L': tuple(map(F, ('1/2', '1/6', '1/4', '1/12'))),
        'R': tuple(map(F, ('17/100', '23/75', '1/5', '97/300'))),
    },
    'B': {
        'L': tuple(map(F, ('5/12', '1/3', '1/6', '1/12'))),
        'R': tuple(map(F, ('31/120', '5/18', '1/15', '143/360'))),
    },
}
ETA = {
    'A': tuple(map(F, ('1/8', '1/4', '3/8', '1/4'))),
    'B': tuple(map(F, ('5/32', '3/16', '13/32', '1/4'))),
}
DIRECTION = (F(7), F(7), F(-1), F(1))


def kernel_check(k, expectation):
    assert all(x > 0 for x in k)
    assert sum(k) == 1
    assert sum(s*x for s, x in zip(S, k)) == expectation


def signatures():
    for origin in ('A', 'B'):
        kernel_check(MU[origin], F(3, 2))
        kernel_check(NU[origin]['L'], F(1))
        kernel_check(NU[origin]['R'], F(3, 2))
        kernel_check(ETA[origin], F(3, 2))


def incoming(origin, side):
    j = 1 if side == 'L' else 2
    return A*MU[origin][j]*NU[origin][side][2]


def terminal_q_masses(U, L, R, gamma_a, gamma_b):
    """Full time/signature terminal Q masses; policy may distinguish merged origin."""
    W = {}
    def add(time, s, q):
        W[(time, s)] = W.get((time, s), F(0)) + q
    add(1, S[0], F(1, 2))
    add(1, S[2], (F(1, 2))*(1-U))
    for origin in ('A', 'B'):
        for j, s in enumerate(S):
            q = A*MU[origin][j]*U
            if j == 1:
                q -= A*MU[origin][j]*L
            if j == 2:
                q -= A*MU[origin][j]*R
            add(2, s, q)
        for side, flow in (('L',L), ('R',R)):
            j = 1 if side == 'L' else 2
            gamma = gamma_a if origin == 'A' else gamma_b
            for k, s in enumerate(S):
                q = A*MU[origin][j]*NU[origin][side][k]*flow
                if k == 2:
                    add(3, s, (1-gamma)*q)
                    for z, terminal_s in enumerate(S):
                        add(4, terminal_s, gamma*q*ETA[origin][z])
                else:
                    add(3, s, q)
    assert all(q >= 0 for q in W.values())
    assert sum(W.values()) == 1
    assert sum(s*q for (t,s),q in W.items()) == 1
    return W


def optimal_declaration_value(W, c=DIRECTION):
    c1,c2,c3,c4 = c
    return c1 + sum(
        q*(t*(c3*s+c4)+max(F(0), c2-c1*s))
        for (t,s),q in W.items()
    )


def claimed_lr_formula(U,L,R,gamma):
    return (F(35,4)-F(17,320)*U + F(1729,14400)*L
            +F(29,400)*R-gamma*(F(7,25600)*L+F(7,6400)*R))


def main():
    signatures()
    v = tuple(incoming(origin,'L') for origin in ('A','B'))
    w = tuple(incoming(origin,'R') for origin in ('A','B'))
    assert v == (F(11,1200), F(23,3600))
    assert w == (F(1,40), F(1,100))
    assert sum(v) == F(7,450) and sum(w) == F(7,200)
    vals = []
    for U,alpha_l,alpha_r,gamma in product((0,1),repeat=4):
        L,R = F(U*alpha_l),F(U*alpha_r)
        W = terminal_q_masses(F(U),L,R,F(gamma),F(gamma))
        objective = optimal_declaration_value(W)
        assert objective == claimed_lr_formula(U,L,R,gamma)
        vals.append(((U,alpha_l,alpha_r,gamma),objective))
    lr_args, lr_max = max(vals,key=lambda row: row[1])
    assert lr_args == (1,1,1,0)
    assert lr_max == F(16001,1800)
    rng = Random(20261029)
    checked = 0
    for _ in range(1000):
        U = F(rng.randint(0,20), 20)
        alpha_l = F(rng.randint(0,20), 20)
        alpha_r = F(rng.randint(0,20), 20)
        gamma = F(rng.randint(0,20), 20)
        L,R=U*alpha_l,U*alpha_r
        W = terminal_q_masses(U,L,R,gamma,gamma)
        assert optimal_declaration_value(W) == claimed_lr_formula(U,L,R,gamma)
        assert optimal_declaration_value(W) <= lr_max
        checked += 1
    W_full = terminal_q_masses(F(1),F(1),F(1),F(0),F(1))
    full_value = optimal_declaration_value(W_full)
    assert full_value == F(409661,46080)
    gap = full_value-lr_max
    assert gap == F(59,76800) > 0
    x_a = v[0]+w[0]
    x_b = v[1]+w[1]
    assert x_a == F(41,1200) and x_b == F(59,3600)
    stop_at_merge = F(-3,2)
    cont_a = sum(q*(4*(1-s)+7*max(F(0),1-s)) for s,q in zip(S,ETA['A']))
    cont_b = sum(q*(4*(1-s)+7*max(F(0),1-s)) for s,q in zip(S,ETA['B']))
    assert cont_a == F(-25,16) and cont_b == F(-93,64)
    assert cont_a < stop_at_merge < cont_b
    assert (cont_b-stop_at_merge)*x_b == gap
    print(json.dumps({
        'status':'PASS_EXACT_FRACTION_NONBLIND_AUTHOR_SIDE_UNREVIEWED_NOT_ADMITTED',
        'source_r5_note':'research_notes/brc_r5_diamond_observer_quotient_20261029_t0240/RESEARCH.md',
        'selected_heterogeneous_tail':'research_notes/brc_r5_diamond_observer_quotient_20261029_t0240/NEXT_TASK.md',
        'direction':list(map(str,DIRECTION)),
        'lr_support':str(lr_max), 'lr_policy':lr_args,
        'valid_full_history_witness_value':str(full_value),
        'full_policy':{'U':1,'alpha_L':1,'alpha_R':1,'gamma_A':0,'gamma_B':1,
                       'terminal_declare_P':'s == 1/2'},
        'strict_support_gap':str(gap),
        'source_arrivals':{'A':str(x_a),'B':str(x_b)},
        'merge_stop':str(stop_at_merge), 'merge_continue_A':str(cont_a),
        'merge_continue_B':str(cont_b),
        'deterministic_lr_patterns_checked':len(vals),
        'rational_lr_samples_checked':checked,
        'claim':'h_FULL(c)>h_LR(c), hence convex hulls differ for this specific model',
        'open':'general R5 equality-of-hulls/unequal-images mother target'
    },ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
