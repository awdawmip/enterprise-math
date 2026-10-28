#!/usr/bin/env python3
"""EC49Q positive-rational action-code cost obstruction: exact finite checks.

Portable Python standard library only. This checker verifies the declared
four-atom auxiliary model; all-real theorems are established in PROOF.md.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

W = (0, 1)
Z = (0, 1)
ACTIONS = ("SR", "SA", "A", "B")
COST = {"SR": 0, "SA": 0, "A": 1, "B": 2}
Q = {(w, z): F(1, 4) for w in W for z in Z}
P = {(w, z): (F(3, 8) if w == z else F(1, 8)) for w in W for z in Z}
DELTA = F(1, 8)


def vec(init, terminal, full=False):
    """deterministic policy with W at stage 0 and optional full terminal W."""
    accepted = [F(), F()]
    paid = [F(), F()]
    for masses_index, masses in enumerate((P, Q)):
        for w, z in product(W, Z):
            action = init[w]
            if action in ("SR", "SA"):
                accept = action == "SA"
            else:
                accept = bool(terminal[(w, action, z) if full else (action, z)])
            accepted[masses_index] += masses[w, z] * int(accept)
            paid[masses_index] += masses[w, z] * COST[action]
    return tuple(accepted + paid)


def h(o):
    return o[0] - o[1] - (o[2] + o[3]) / 16


def frac_dict(values):
    return {k: str(v) for k, v in values.items()}


def best_grid(budget, step=4):
    # For these specified rational decision probabilities, optimize the
    # terminal acceptance over both binary signals exactly by positive parts.
    pairs = [(F(i, step), F(j, step))
             for i in range(step + 1)
             for j in range(step + 1 - i)]
    best, witness = F(-1), None
    checked = 0
    for (x0, y0), (x1, y1) in product(pairs, repeat=2):
        c = (x0 + x1 + 2 * (y0 + y1)) / 2
        if c > budget:
            continue
        checked += 1
        lv = DELTA * (abs(x0 - x1) + abs(y0 - y1))
        if lv > best:
            best = lv
            witness = (x0, y0, x1, y1, c)
    return best, witness, checked


def budget_frontier(c):
    if c <= F(1, 2):
        return c / 4
    if c <= F(3, 2):
        return (c + F(1, 2)) / 8
    return F(1, 4)


def main():
    assert sum(P.values()) == sum(Q.values()) == 1
    assert all(v > 0 for v in list(P.values()) + list(Q.values()))
    assert all(sum(P[w, z] for z in Z) == F(1, 2) for w in W)
    assert all(sum(Q[w, z] for z in Z) == F(1, 2) for w in W)
    assert all(sum(P[w, z] for w in W) == F(1, 2) for z in Z)
    assert all(sum(Q[w, z] for w in W) == F(1, 2) for z in Z)

    terminal0 = tuple((a, z) for a in ("A", "B") for z in Z)
    terminal1 = tuple((w, a, z) for w in W for a in ("A", "B") for z in Z)
    maxima = {False: (F(-10), None, 0), True: (F(-10), None, 0)}
    for full, keys in ((False, terminal0), (True, terminal1)):
        count = 0
        bmax, witness = F(-10), None
        for init in product(ACTIONS, repeat=2):
            for bits in product((0, 1), repeat=len(keys)):
                final = dict(zip(keys, bits))
                o = vec(init, final, full=full)
                assert o[2] == o[3]
                value = h(o)
                count += 1
                if value > bmax:
                    bmax, witness = value, (init, o)
        maxima[full] = (bmax, witness, count)
    assert maxima[False][0] == F(1, 16), maxima[False]
    assert maxima[True][0] == F(1, 8), maxima[True]
    assert maxima[False][2] == 256 and maxima[True][2] == 4096

    # Full-information optimal witness: buy A at W=0,1; accept exactly z=w.
    full_init = ("A", "A")
    full_term = {(w, a, z): (w == z) for w in W for a in ("A", "B") for z in Z}
    full_target = vec(full_init, full_term, True)
    assert full_target == (F(3, 4), F(1, 2), F(1), F(1))
    assert h(full_target) == F(1, 8)

    # Compressed rational behavioral witness:
    # W=0 buys cheap A; W=1 buys B with probability 1/2, otherwise rejects.
    # Accept on (A,Z=0) or (B,Z=1).
    weights = {(0, "A"): F(1), (0, "B"): F(),
               (1, "A"): F(), (1, "B"): F(1, 2)}
    mixa = [F(), F()]
    mixcost = [F(), F()]
    for idx, source in enumerate((P, Q)):
        for w, z in product(W, Z):
            for a in ("A", "B"):
                prob = weights[w, a]
                mixcost[idx] += source[w, z] * prob * COST[a]
                if (a, z) in (("A", 0), ("B", 1)):
                    mixa[idx] += source[w, z] * prob
    mix = tuple(mixa + mixcost)
    assert mix == (F(9, 16), F(3, 8), F(1), F(1))
    assert h(mix) == F(1, 16)
    assert mix[0] - mix[1] == F(3, 16)

    grid_results = {}
    total_grid_valid = 0
    for c in (F(0), F(1, 4), F(1, 2), F(3, 4), F(1), F(5, 4), F(3, 2), F(2)):
        best, wit, count = best_grid(c)
        expected = budget_frontier(c)
        assert best == expected, (c, best, expected)
        total_grid_valid += count
        grid_results[str(c)] = {"max_L": str(best), "cost_budget": str(c),
                                "enumerated_feasible_grid_pairs": count,
                                "witness_x0_y0_x1_y1_cost": [str(x) for x in wit]}

    # Same-cost cloned sensors: construct code A for W=0, B for W=1.
    # For each deterministic full stage policy whose A/B observational laws
    # and costs are IDENTICAL, exactly match its accepted P/Q and cost vector.
    # The resulting acceptance probability after Z is a rational mixture of
    # the original A/B terminal choices (no shared random seed).
    clone_policies_verified = 0
    for init in product(ACTIONS, repeat=2):
        for bits in product((0, 1), repeat=len(terminal1)):
            term = dict(zip(terminal1, bits))
            full_clone = [F(), F(), F(), F()]
            compressed_clone = [F(), F(), F(), F()]
            for idx, source in enumerate((P, Q)):
                for w, z in product(W, Z):
                    act = init[w]
                    paid = int(act in ("A", "B"))  # both clones cost one
                    acc = int(act == "SA") if act in ("SR", "SA") else int(term[w, act, z])
                    full_clone[idx] += source[w, z] * acc
                    full_clone[2 + idx] += source[w, z] * paid
                    # Compile initial purchase to A if W=0 else B. Terminal
                    # remembers the actual chosen label and recovers W.
                    recovered_w = 0 if w == 0 else 1
                    coded_acc = int(act == "SA") if not paid else int(term[recovered_w, act, z])
                    compressed_clone[idx] += source[w, z] * coded_acc
                    compressed_clone[2 + idx] += source[w, z] * paid
            assert tuple(full_clone) == tuple(compressed_clone)
            clone_policies_verified += 1
    assert clone_policies_verified == 4096

    report = {
        "unit": "EC49Q",
        "carrier": "four exact positive-rational P/Q atoms; auxiliary P-Q difference",
        "W_Z": [0, 1],
        "P": {f"{w}{z}": str(P[w, z]) for w, z in product(W, Z)},
        "Q": {f"{w}{z}": str(Q[w, z]) for w, z in product(W, Z)},
        "cost_A_B": [1, 2],
        "full_witness": [str(v) for v in full_target],
        "compressed_rational_witness": [str(v) for v in mix],
        "linear_functional": "H=alpha-beta-(E_P T+E_Q T)/16",
        "support_compressed_max": str(maxima[False][0]),
        "support_full_max": str(maxima[True][0]),
        "exact_support_gap": str(maxima[True][0]-maxima[False][0]),
        "deterministic_policies": {"compressed": maxima[False][2], "full": maxima[True][2]},
        "rational_grid_initial_policy_pair_evaluations": total_grid_valid,
        "grid_budget_frontier": grid_results,
        "same_cost_clone_full_deterministic_cases_checked": clone_policies_verified,
        "verification": "PASS: exact Fraction finite checks; all-real generality by PROOF.md analytic argument",
        "scope": "one-purchase-stage auxiliary two-source positive-weight observation; not native BRC signed amplitude/X6",
    }
    output = Path(__file__).with_name("EXACT_REPORT.json")
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True)+"\n", encoding="utf-8")
    print(json.dumps({"verification": "PASS", "full_witness": report["full_witness"],
                      "compressed_witness": report["compressed_rational_witness"],
                      "supports": [report["support_compressed_max"], report["support_full_max"]],
                      "support_gap": report["exact_support_gap"],
                      "deterministic": report["deterministic_policies"],
                      "grid_feasible_pairs": total_grid_valid,
                      "same_cost_clone_cases": clone_policies_verified},
                     ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
