#!/usr/bin/env python3
"""Stage249: exact rational Bellman/primal and unmerged ordered-history certificate.

Only the external ternary IID problem, horizon 9, a=3/10, b=19/40.
No SciPy, floating point, native X6 claims or platform credentials required.
"""
from fractions import Fraction as F
from functools import lru_cache

N = 9
P = (F(1, 8), F(1, 24), F(5, 6))
Q = (F(1, 12), F(1, 12), F(5, 6))
LAMBDA = F(43416, 607)
CAP_P, CAP_Q = F(3, 10), F(19, 40)
A, B = (1, 0, 5), (0, 0, 9)
C_A = F(24543634, 28453125)       # P/continue tie: Pr(continue)
D_B = F(3388291539, 4742187500)  # terminal P/Q tie: Pr(decide P)
ZERO = (0, 0, 0)


def next_state(s, sym):
    return tuple(x + (k == sym) for k, x in enumerate(s))


@lru_cache(None)
def bellman(s):
    """Conditional P-normalized Bellman value for t_P+lambda(e_P+e_Q)."""
    likelihood = F(2, 3)**s[0] * F(2)**s[1]
    actions = {"P": LAMBDA * likelihood, "Q": LAMBDA}
    if sum(s) < N:
        actions["C"] = 1 + sum(P[k] * bellman(next_state(s, k))[0]
                                for k in range(3))
    minimum = min(actions.values())
    minimizers = tuple(k for k, val in actions.items() if val == minimum)
    return minimum, minimizers, actions


def policy(s):
    """Exact randomized Markov policy on proven sufficient count states."""
    if s == A:
        return (("P", 1-C_A), ("C", C_A))
    if s == B:
        return (("P", D_B), ("Q", 1-D_B))
    return ((bellman(s)[1][0], F(1)),)


@lru_cache(None)
def suffix_observers(s):
    """Four separate conditional observers under P and Q (exact fractions)."""
    ep = eq = tp = tq = F(0)
    for action, chance in policy(s):
        if action == "P":
            eq += chance
        elif action == "Q":
            ep += chance
        else:
            children = [suffix_observers(next_state(s, k)) for k in range(3)]
            ep += chance * sum(P[k] * children[k][0] for k in range(3))
            eq += chance * sum(Q[k] * children[k][1] for k in range(3))
            tp += chance * (1 + sum(P[k] * children[k][2] for k in range(3)))
            tq += chance * (1 + sum(Q[k] * children[k][3] for k in range(3)))
    return ep, eq, tp, tq


def full_ordered_dfs():
    """Do not merge path prefixes: independently sum labeled P/Q terminal masses."""
    terminal_p = terminal_q = ep = eq = tp = tq = F(0)
    nodes = leaves = 0

    def walk(s, pweight, qweight, depth):
        nonlocal terminal_p, terminal_q, ep, eq, tp, tq, nodes, leaves
        nodes += 1
        for act, chance in policy(s):
            if not chance:
                continue
            pw, qw = chance * pweight, chance * qweight
            if act == "C":
                assert depth < N
                for k in range(3):
                    walk(next_state(s, k), pw*P[k], qw*Q[k], depth+1)
            else:
                leaves += 1
                terminal_p += pw
                terminal_q += qw
                tp += pw * depth
                tq += qw * depth
                if act == "Q":
                    ep += pw
                else:
                    eq += qw

    walk(ZERO, F(1), F(1), 0)
    assert (terminal_p, terminal_q) == (1, 1)
    return (ep, eq, tp, tq), nodes, leaves


def verify():
    states = [(i, j, n-i-j) for n in range(N+1)
              for i in range(n+1) for j in range(n-i+1)]
    assert len(states) == 220
    ties = []; gaps = 0
    for s in states:
        h, minimizers, acts = bellman(s)
        ties.extend((s, tuple(minimizers)) for _ in [0] if len(minimizers) > 1)
        gaps += sum(v > h for v in acts.values())
        assert all(v >= h for v in acts.values())
        assert all(act in minimizers for act, weight in policy(s) if weight)
    assert ties == [(A, ("P", "C")), (B, ("P", "Q"))], ties
    assert gaps == 383, gaps
    assert F(0) < C_A < 1 and F(0) < D_B < 1

    root_value = F(126226064573, 2039053824)
    exact_optimum = F(65983208881, 10195269120)
    witness = (CAP_P, CAP_Q, exact_optimum,
               F(61538202869, 10195269120))
    assert bellman(ZERO)[0] == root_value
    assert root_value - LAMBDA*(CAP_P + CAP_Q) == exact_optimum
    assert suffix_observers(ZERO) == witness
    actual, nodes, leaves = full_ordered_dfs()
    assert actual == witness, (actual, witness)
    assert witness[2] > witness[3]
    assert witness[2]+LAMBDA*(witness[0]+witness[1]) == root_value
    print('STAGE249_EXACT_AUTHOR_PASS')
    print(f'Bellman states={len(states)} ties={len(ties)} strict_gaps={gaps}')
    print('K=',LAMBDA,'J_root=',root_value)
    print('coins_continue_A=',C_A,'coin_decide_P_B=',D_B)
    print('eP,eQ,tP,tQ=', ','.join(map(str,witness)))
    print('V9(3/10,19/40)=',exact_optimum)
    print('independent ordered DFS nodes=',nodes,'terminal branches=',leaves)


if __name__ == '__main__':
    verify()
