"""Exact independent policy enumeration for the auxiliary horizon-two BRC observer."""
from fractions import Fraction as F
from itertools import product
import json


def solve(u, p, q, c, compressed):
    P = (u * p, u * (1-p), 1-u)
    Q = (u * q, u * (1-q), 1-u)
    assert sum(P) == sum(Q) == 1 and all(x > 0 for x in P + Q)
    best = None
    winners = 0
    count = 0
    for first in ([(a, a) for a in range(3)] if compressed
                  else list(product(range(3), repeat=2))):
        for last in product(range(2), repeat=3):
            count += 1
            alpha = beta = tp = tq = F(0)
            for i, h in enumerate((0, 0, 1)):
                action = first[h]  # 0=stop/reject; 1=stop/accept; 2=continue
                decision = last[i] if action == 2 else action
                t = 2 if action == 2 else 1
                alpha += P[i] * decision
                beta += Q[i] * decision
                tp += P[i] * t
                tq += Q[i] * t
            score = alpha - beta - c * (tp + tq)
            if (not compressed and (u, p, q, c) == (F(1,2), F(3,4), F(1,4), F(1,8))
                    and first == (2, 0) and last == (1, 0, 0)):
                assert (alpha, beta, tp, tq, score) == (F(3,8), F(1,8), F(3,2), F(3,2), F(-1,8))
            if best is None or score > best[0]:
                best = (score, (alpha, beta, tp, tq), first, last)
                winners = 1
            elif score == best[0]:
                winners += 1
    return count, best, winners


def theoretical(u, p, q, c):
    d = u*(p-q)
    vf = -2*c + max(F(0), d - 2*c*u)
    vl = -2*c + max(F(0), d - 2*c)
    return vf, vl


u, p, q, c = F(1, 2), F(3, 4), F(1, 4), F(1, 8)
nf, ff, wf = solve(u, p, q, c, False)
nl, fl, wl = solve(u, p, q, c, True)
assert (nf, nl) == (72, 24)
assert (ff[0], fl[0]) == theoretical(u, p, q, c) == (F(-1, 8), F(-1, 4))
# The direct A-continue/B-stop policy is independently asserted inside enumeration.
strict = 0
cases = 0
for U, P, Q, C in product(
    (F(1,4), F(1,3), F(1,2), F(2,3), F(3,4)),
    (F(1,2), F(2,3), F(3,4), F(4,5)),
    (F(1,5), F(1,4), F(1,3), F(1,2), F(2,3)),
    (F(1,32), F(1,16), F(1,8), F(1,4), F(1,2))):
    if Q >= P:
        continue
    cases += 1
    full = solve(U, P, Q, C, False)[1][0]
    lr = solve(U, P, Q, C, True)[1][0]
    assert (full, lr) == theoretical(U, P, Q, C)
    assert full >= lr
    strict += full > lr

show = lambda f: f"{f.numerator}/{f.denominator}"
report = {
    "model": "horizon=2; leaves A+,A-,B*; P=(up,u(1-p),1-u); Q=(uq,u(1-q),1-u)",
    "witness": {"u":show(u),"p":show(p),"q":show(q),"c":show(c),
                "P":[show(x) for x in (u*p,u*(1-p),1-u)],
                "Q":[show(x) for x in (u*q,u*(1-q),1-u)],
                "full_max":show(ff[0]),"LR_max":show(fl[0]),
                "gap":show(ff[0]-fl[0]),
                "explicit_full_readout":["3/8","1/8","3/2","3/2"],
                "full_deterministic_policies":nf,"LR_deterministic_policies":nl,
                "full_maximizers":wf,"LR_maximizers":wl},
    "grid":{"exact_models_checked":cases,"positive_gap_models":strict,
            "all_theoretical_formula_matches_enumeration":True},
    "scope":"external finite two-source positive-mass observer; not native heartbeat/BRC-Shor math",
    "status":"author-side exact check; no independent mathematical admission"}
print(json.dumps(report,ensure_ascii=False,indent=2,sort_keys=True))
