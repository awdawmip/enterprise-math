#!/usr/bin/env python3
"""EC49G: exact two-action, two-source BRC acquisition witness.
Only Python stdlib Fraction; exhaustive finite deterministic policies.
"""
from fractions import Fraction as F
from itertools import product
import json

# Conditional on W; joint masses are half of these (W is source-neutral).
ROWS = {
    0: {"11": (F(1, 2), F(1, 12)), "10": (F(1, 4), F(1, 6)),
        "01": (F(1, 6), F(1, 4)), "00": (F(1, 12), F(1, 2))},
    1: {"11": (F(7, 12), F(1, 6)), "10": (F(1, 6), F(1, 12)),
        "01": (F(1, 12), F(1, 6)), "00": (F(1, 6), F(7, 12))},
}
COST = {"A": F(2), "B": F(3, 2)}
LAMBDA = F(2)
C = F(1, 24)


def mix(rows0, rows1):
    return {k: tuple((x + y) / 2 for x, y in zip(rows0[k], rows1[k]))
            for k in rows0}


MIXED = mix(ROWS[0], ROWS[1])
BRANCHES = (("stop", 0), ("stop", 1)) + tuple(
    ("continue", a0, a1) for a0, a1 in product((0, 1), repeat=2))
POLICIES = (("stop", 0), ("stop", 1)) + tuple(
    ("buy", first, x, y) for first in ("A", "B")
    for x, y in product(BRANCHES, repeat=2))
assert len(POLICIES) == 74


def evaluate(rows, policy):
    """Return (Paccept,Qaccept,E_P T,E_Q T)."""
    result = [F(0), F(0), F(0), F(0)]
    for ab, (p, q) in rows.items():
        if policy[0] == "stop":
            accept, time = policy[1], F(0)
        else:
            first = policy[1]
            bit1 = int(ab[0] if first == "A" else ab[1])
            branch = policy[2 + bit1]
            time = COST[first]
            if branch[0] == "stop":
                accept = branch[1]
            else:
                second = "B" if first == "A" else "A"
                bit2 = int(ab[0] if second == "A" else ab[1])
                accept = branch[1 + bit2]
                time += COST[second]
        result[0] += p * accept
        result[1] += q * accept
        result[2] += p * time
        result[3] += q * time
    return tuple(result)


def support(obs):
    a, b, tp, tq = obs
    return a - LAMBDA * b - C * (tp + tq)


def fraction_str(f):
    return str(f.numerator) if f.denominator == 1 else f"{f.numerator}/{f.denominator}"


def vector_str(v):
    return [fraction_str(x) for x in v]


def root_options(scores):
    return {
        "reject": fraction_str(scores[0]),
        "accept": fraction_str(scores[1]),
        "buy_A": fraction_str(max(scores[2:38])),
        "buy_B": fraction_str(max(scores[38:74])),
    }


# Full-model checks: P and Q are normalized, all eight (W,A,B) leaves strictly positive.
for w, rows in ROWS.items():
    assert all(p > 0 and q > 0 for p, q in rows.values())
    assert sum(p for p, _ in rows.values()) == 1
    assert sum(q for _, q in rows.values()) == 1
    assert sum(p / 2 for p, _ in rows.values()) == F(1, 2)
    assert sum(q / 2 for _, q in rows.values()) == F(1, 2)
    # W invariant individual action marginals and their LR histogram.
    assert sum(p for ab, (p, q) in rows.items() if ab[0] == '1') == F(3, 4)
    assert sum(q for ab, (p, q) in rows.items() if ab[0] == '1') == F(1, 4)
    assert sum(p for ab, (p, q) in rows.items() if ab[1] == '1') == F(2, 3)
    assert sum(q for ab, (p, q) in rows.items() if ab[1] == '1') == F(1, 3)
assert sum(p / 2 for rows in ROWS.values() for p, _ in rows.values()) == 1
assert sum(q / 2 for rows in ROWS.values() for _, q in rows.values()) == 1

# A Q-transition kernel differs after action B=1, despite identical standalone LR histograms.
assert ROWS[0]['11'][1] / F(1, 3) == F(1, 4)
assert ROWS[1]['11'][1] / F(1, 3) == F(1, 2)

score_sets = {}
obs_sets = {}
root_table = {}
for label, rows in (("W0", ROWS[0]), ("W1", ROWS[1]), ("coarse", MIXED)):
    obs_sets[label] = [evaluate(rows, policy) for policy in POLICIES]
    score_sets[label] = [support(v) for v in obs_sets[label]]
    root_table[label] = root_options(score_sets[label])

assert root_table == {
    'W0': {'reject': '0', 'accept': '-1', 'buy_A': '5/48', 'buy_B': '1/8'},
    'W1': {'reject': '0', 'accept': '-1', 'buy_A': '1/12', 'buy_B': '1/24'},
    'coarse': {'reject': '0', 'accept': '-1', 'buy_A': '1/12', 'buy_B': '1/12'},
}
assert max(score_sets['W0']) == F(1, 8)
assert max(score_sets['W1']) == F(1, 12)
assert max(score_sets['coarse']) == F(1, 12)

# W0: acquire B; if B=1 acquire A; accept iff A=1. W1: acquire A; accept iff A=1.
POLICY0 = ('buy', 'B', ('stop', 0), ('continue', 0, 1))
POLICY1 = ('buy', 'A', ('stop', 0), ('stop', 1))
assert POLICY0 in POLICIES and POLICY1 in POLICIES
assert support(evaluate(ROWS[0], POLICY0)) == F(1, 8)
assert support(evaluate(ROWS[1], POLICY1)) == F(1, 12)
full_vec = tuple((x + y) / 2 for x, y in zip(evaluate(ROWS[0], POLICY0), evaluate(ROWS[1], POLICY1)))
assert full_vec == (F(5, 8), F(1, 6), F(29, 12), F(25, 12))
assert support(full_vec) == F(5, 48)
assert support(full_vec) - max(score_sets['coarse']) == F(1, 48)

# Exhaustive full-W pure policies: each branch separately picks one of 74 pure trees.
full_scores = [(s0 + s1) / 2 for s0, s1 in product(score_sets['W0'], score_sets['W1'])]
assert len(full_scores) == 74 * 74 == 5476
assert max(full_scores) == support(full_vec)
assert max(score_sets['coarse']) <= max(full_scores)

report = {
    "unit": "EC49G", "status": "EXACT_FINITE_ENUMERATION_PASS",
    "source": "eight strictly positive rational (W,A,B) leaves; W neutral under P,Q",
    "conditioned_leaf_masses": {str(w): {ab: vector_str(values) for ab, values in rows.items()} for w, rows in ROWS.items()},
    "acquisition_costs": {key: fraction_str(value) for key, value in COST.items()},
    "support": "alpha - 2 beta - (E_P T + E_Q T)/24",
    "action_marginal_LR": {"A": {"A1": "3", "A0": "1/3"}, "B": {"B1": "2", "B0": "1/2"}},
    "action_conditional_Q_A1_given_B1": {"W0": "1/4", "W1": "1/2"},
    "root_option_support": root_table,
    "policy_counts": {"coarse_deterministic": len(POLICIES), "W_revealed_deterministic": len(full_scores)},
    "W0_policy": repr(POLICY0), "W1_policy": repr(POLICY1),
    "W0_vector": vector_str(evaluate(ROWS[0], POLICY0)),
    "W1_vector": vector_str(evaluate(ROWS[1], POLICY1)),
    "full_vector": vector_str(full_vec),
    "coarse_support_max": "1/12", "full_support_max": "5/48", "exact_gap": "1/48",
    "scope": "finite passive eight-atom two-source acquisition; each A/B acquired at most once; zero prior cost; real behavioral randomization convexifies deterministic policies for linear support",
    "not_claimed": ["native signed BRC transfer", "X6 heartbeat physical correspondence", "minimal-state characterization", "universal novelty priority"],
}
print(json.dumps(report, ensure_ascii=False, indent=2) + '\n', end='')
