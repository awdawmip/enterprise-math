"""Exact BRC ordered-prefix -> count-occupancy Markovization audit.

Scope: finite IID ternary observations, law-independent adapted randomized
stop/decision policies and four observers (two errors, two mean sample counts).
Python standard-library Fractions; no floating point.
"""
from fractions import Fraction as F
from collections import defaultdict
import json

P = (F(1,8), F(1,24), F(5,6))
Q = (F(1,12), F(1,12), F(5,6))
assert sum(P) == sum(Q) == 1


def state(h):
    return tuple(h.count(i) for i in range(3))


def product(k, law):
    p = F(1)
    for i, v in enumerate(k):
        p *= law[i] ** v
    return p


def policy(h, N, seed):
    t = len(h)
    z = (seed + 7*t + sum((j + 1)*(sym + 2) for j, sym in enumerate(h)))
    if t == N:
        a = F(z % 7 + 1, 9)
        return a, 1 - a, F(0)
    a = F(z % 3 + 1, 12)
    b = F((z // 3) % 3 + 1, 12)
    c = 1 - a - b
    assert a >= 0 and b >= 0 and c > 0
    return a, b, c


def generic_audit(N, seed):
    paths = {(): F(1)}
    all_flow = []
    ordered = dict(error_P=F(0), error_Q=F(0), t_P=F(0), t_Q=F(0))
    for t in range(N + 1):
        flow = defaultdict(lambda: [F(0), F(0), F(0), F(0)])
        new_paths = defaultdict(F)
        for h, reach in paths.items():
            k = state(h)
            a, b, c = policy(h, N, seed)
            for j, x in enumerate((reach, reach*a, reach*b, reach*c)):
                flow[k][j] += x
            ordered['error_P'] += product(k,P)*reach*b
            ordered['error_Q'] += product(k,Q)*reach*a
            ordered['t_P'] += t*product(k,P)*reach*(a+b)
            ordered['t_Q'] += t*product(k,Q)*reach*(a+b)
            if t < N:
                for i in range(3):
                    new_paths[h + (i,)] += reach*c
        all_flow.append(dict(flow))
        paths = new_paths
    lumped = { (0,0,0): F(1) }
    folded = dict(error_P=F(0), error_Q=F(0), t_P=F(0), t_Q=F(0))
    states_checked = 0
    for t in range(N+1):
        new_lumped = defaultdict(F)
        expected_flow = all_flow[t]
        assert set(lumped)==set(expected_flow), (t,set(lumped)^set(expected_flow))
        for k, reach in lumped.items():
            f, A, B, C = expected_flow[k]
            assert reach == f and A+B+C == f
            a,b,c=A/f,B/f,C/f
            assert a >= 0 and b >= 0 and c >= 0 and a+b+c == 1
            folded['error_P'] += product(k,P)*reach*b
            folded['error_Q'] += product(k,Q)*reach*a
            folded['t_P'] += t*product(k,P)*reach*(a+b)
            folded['t_Q'] += t*product(k,Q)*reach*(a+b)
            states_checked += 1
            if t < N:
                for i in range(3):
                    new_k=tuple(v+(i==j) for j,v in enumerate(k))
                    new_lumped[new_k] += reach*c
        lumped = dict(new_lumped)
    assert ordered == folded
    assert all(x >= 0 for x in ordered.values())
    return {'N':N, 'seed':seed, 'states_checked':states_checked,
            'all_four_observers_equal':True,
            'ordered_observers':{k:str(v) for k,v in ordered.items()}}


def asymmetric_prefix_counterexample():
    # N=2: initial 0 -> continue; initial 1 -> continue with chance 1/2;
    # initial 2 -> decide P. Terminal 01 -> Q, terminal 10 -> P.
    k=(1,1,0)
    Fcount = F(3,2)
    weighted_Q = F(1,1) / Fcount
    naive_Q = F(1,2)
    expected_P = product(k,P)*Fcount*weighted_Q
    naive_P = product(k,P)*Fcount*naive_Q
    expected_Q = product(k,Q)*Fcount*weighted_Q
    naive_Q_mass = product(k,Q)*Fcount*naive_Q
    assert (expected_P,naive_P,expected_Q,naive_Q_mass)==(F(1,192),F(1,256),F(1,144),F(1,192))
    return dict(k=k, prefixes={'01':'1','10':'1/2'},
                count_policy_stop_Q=str(weighted_Q),naive_stop_Q=str(naive_Q),
                P_Q_decision_exact=str(expected_P),P_Q_decision_naive=str(naive_P),
                Q_Q_decision_exact=str(expected_Q),Q_Q_decision_naive=str(naive_Q_mass))


def main():
    outcome={
        'schema':'EM_R1_AUX_IID_MARKOVIZATION_EXACT_CHECK_V1',
        'classification':'AUTHOR_FINITE_COMPUTATION_PLUS_GENERAL_HAND_PROOF',
        'laws': {'P':[str(x) for x in P], 'Q':[str(x) for x in Q]},
        'checked_cases':[generic_audit(n,s) for n,s in [(3,1),(4,5),(5,9)]],
        'naive_uniform_averaging_counterexample':asymmetric_prefix_counterexample(),
        'general_theorem_proof_location':'PROOF.md',
        'native_P000_transfer':'NOT_CLAIMED',
        'formal_Lean_check':'NOT_RUN',
        'independent_review':'PENDING',
    }
    print(json.dumps(outcome,indent=2,ensure_ascii=False))


if __name__ == '__main__': main()
