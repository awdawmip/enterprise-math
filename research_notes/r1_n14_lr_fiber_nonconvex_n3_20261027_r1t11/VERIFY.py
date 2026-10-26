"""Exact ordered-branch check of an LR-fiber-constant N=3 nonconvex quotient image.

The computation is *only* for a finite, external positive-rational P/Q model.
BRC-compatible interpretation: ordered branch identities, exact weights, explicit
observer and stopping action; no Heartbeat/native-X6 arithmetic is executed.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import json

ALPHABET = (0, 1, 2)
P3 = {"A": (F(1, 8), F(5, 8), F(1, 4)),
      "B": (F(1, 4), F(1, 4), F(1, 2))}
Q3 = {"A": (F(1, 4), F(5, 8), F(1, 8)),
      "B": (F(1, 2), F(1, 4), F(1, 4))}
RATIO = (F(2), F(1), F(1, 2))

def group(history):
    return "A" if history[0] == 0 else "B"

def x(history):
    n = len(history)
    if n == 0:
        return (0, "root")
    if n == 1:
        return (1, group(history))
    if n == 2:
        return (2, "merged")
    if n == 3:
        return (3, str(history[-1]))
    raise ValueError(history)

def weight(law, history):
    n = len(history)
    if n <= 2:
        return F(1, 3) ** n
    return F(1, 9) * (P3 if law == "P" else Q3)[group(history[:1])][history[-1]]

def edge_weight(law, h, a):
    return weight(law, h + (a,)) / weight(law, h)

def fstr(value):
    return f"{value.numerator}/{value.denominator}"

def policy(kind, h):
    state = x(h)
    if len(h) == 0:
        return (F(1), F(0), F(0))
    if len(h) == 1:
        cont = (state[1] == "A") if kind == "A" else (state[1] == "B")
        return (F(int(cont)), F(int(not cont)), F(0))
    if len(h) == 2:
        return (F(1), F(0), F(0)) if kind == "A" else (F(0), F(1), F(0))
    return (F(0), F(1), F(0))

def terminal_joint(kind, law):
    obs = defaultdict(F)
    def walk(h, survival):
        c, d0, d1 = policy(kind, h)
        assert c + d0 + d1 == 1 and all(v >= 0 for v in (c,d0,d1))
        for decision, p in enumerate((d0, d1)):
            obs[(len(h), x(h)[1], decision)] += survival * p
        if len(h) < 3:
            for a in ALPHABET:
                walk(h+(a,), survival*c*edge_weight(law,h,a))
        else:
            assert c == 0
    walk((), F(1))
    assert sum(obs.values()) == 1
    return obs

def one_observation(obs, time, state, d=None):
    return sum((v for (t,s,decision),v in obs.items()
                if t == time and s == state and (d is None or d == decision)), F(0))

def entry():
    for g in ("A","B"):
        assert sum(P3[g]) == sum(Q3[g]) == 1
        assert tuple(Q3[g][j]/P3[g][j] for j in ALPHABET) == RATIO
    states = defaultdict(set)
    path_count = 0
    for t in range(4):
        for h in product(ALPHABET, repeat=t):
            path_count += 1
            states[x(h)].add(weight("Q",h)/weight("P",h))
            if t < 3:
                assert sum(edge_weight("P",h,j) for j in ALPHABET) == 1
                assert sum(edge_weight("Q",h,j) for j in ALPHABET) == 1
                for j in ALPHABET:
                    assert edge_weight("P",h,j) > 0 and edge_weight("Q",h,j) > 0
    assert path_count == 40
    assert all(len(z)==1 for z in states.values()), states
    assert len(states) == 7, states # root; two first-state; merged; three terminal
    observations = {law: {kind: terminal_joint(kind, law) for kind in ("A","B")}
                    for law in ("P","Q")}
    midpoint = {law: defaultdict(F) for law in ("P","Q")}
    for law in ("P","Q"):
        for kind in ("A","B"):
            for key, v in observations[law][kind].items():
                midpoint[law][key] += v/2
    A_surv = F(1,3) - one_observation(midpoint["P"],1,"A")
    B_surv = F(2,3) - one_observation(midpoint["P"],1,"B")
    total_t3 = sum(v for (t,s,d),v in midpoint["P"].items() if t == 3)
    assert (A_surv,B_surv,total_t3) == (F(1,6), F(1,3), F(1,6))
    forced_c2 = total_t3 / (A_surv+B_surv)
    assert forced_c2 == F(1,3)
    gap = {}
    for law, local in (("P",P3),("Q",Q3)):
        actual = one_observation(midpoint[law],3,"0")
        forced = forced_c2*(A_surv*local["A"][0]+B_surv*local["B"][0])
        polynomial = (A_surv+B_surv)*actual-total_t3*(A_surv*local["A"][0]+B_surv*local["B"][0])
        assert actual != forced and polynomial == (A_surv+B_surv)*(actual-forced)
        gap[law] = {"midpoint_t3_y0": fstr(actual),
                    "forced_quotient_t3_y0": fstr(forced),
                    "forced_minus_midpoint": fstr(forced-actual),
                    "universal_polynomial_at_midpoint":fstr(polynomial)}
    assert gap["P"]["forced_minus_midpoint"] == "1/72"
    assert gap["Q"]["forced_minus_midpoint"] == "1/36"
    return {"status":"PASS", "number_of_ordered_prefixes":path_count,
            "compressed_states": len(states),
            "likelihood_ratio_by_compressed_state":{str(k):fstr(next(iter(v))) for k,v in sorted(states.items())},
            "two_laws_distinct": P3 != Q3,
            "midpoint_observer_joint":{
                law:{str(k): fstr(v) for k,v in sorted(midpoint[law].items()) if v}
                for law in ("P","Q")},
            "forced_from_t1_and_t2": {"survival_A":fstr(A_surv),"survival_B":fstr(B_surv),"T3_mass":fstr(total_t3),"t2_continue":fstr(forced_c2)},
            "polynomial_certificate":gap,
            "claim_scope":"finite rational example; universal all-real quotient infeasibility follows from algebraic invariant, not enumeration"}

if __name__ == "__main__":
    print(json.dumps(entry(),ensure_ascii=False,sort_keys=True,indent=2))
