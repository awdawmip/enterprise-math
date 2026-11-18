#!/usr/bin/env python3
"""Integer-exact, dependency-free certificate for R749SUJ."""
import json
from math import gcd


def canonical(a, u, v, d):
    return a == d and sorted((u, v)) == [a - 1, a + 1]


def exhaustive(M):
    """Independent (a,d,u) enumeration, with v forced by determinant 1."""
    candidates = []
    for a in range(1, M + 1):
        for d in range(1, M + 1):
            p = a * d - 1
            for u in range(1, M + 1):
                if p <= 0 or p % u:
                    continue
                v = p // u
                if 1 <= v <= M and not canonical(a, u, v, d):
                    candidates.append((max(u, v) * a * d, (a, u, v, d)))
    peak = max(s for s, _ in candidates)
    winners = sorted(t for s, t in candidates if s == peak)
    runner = max((s for s, _ in candidates if s < peak), default=None)
    return peak, winners, len(candidates), runner


def modular(M):
    """Independent oriented inverse search; restores all labeled symmetries."""
    peak = 2
    winners = {(1, 1, 1, 2), (2, 1, 1, 1)}
    for a in range(1, M + 1):
        for u in range(2, M + 1):
            if gcd(a, u) != 1:
                continue
            D = min(M, (u * u + 1) // a)
            r = pow(a, -1, u)
            if D < r:
                continue
            d = r + u * ((D - r) // u)
            if a * d < u + 1:
                continue
            v = (a * d - 1) // u
            if not 1 <= v <= u or canonical(a, u, v, d):
                continue
            s = u * a * d
            pair = {(a, u, v, d), (a, v, u, d), (d, u, v, a), (d, v, u, a)}
            if s > peak:
                peak, winners = s, pair
            elif s == peak:
                winners.update(pair)
    return peak, sorted(winners)


def main():
    fast = {}
    for M in range(2, 601):
        fast[M] = modular(M)
    for M in range(2, 121):
        b, wins, _, _ = exhaustive(M)
        assert (b, wins) == fast[M], (M, b, wins, fast[M])
    first_nonunit = [M for M in range(2, 601)
                     if any(abs(u+v-a-d) != 1 for a,u,v,d in fast[M][1])]
    assert first_nonunit == [58, 93], first_nonunit
    cases = {}
    for M in (57, 58, 59, 93, 94):
        b, w, n, runner = exhaustive(M)
        assert (b, w) == fast[M]
        cases[str(M)] = {"T_star": b, "labeled_winners": [list(t) for t in w],
                         "winner_q": sorted({u+v-a-d for a,u,v,d in w}),
                         "noncanonical_candidate_count": n, "runner_up": runner}
    assert cases['58']['T_star'] == 127890
    assert cases['93']['T_star'] == 579576
    assert cases['58']['winner_q'] == [2] == cases['93']['winner_q']
    results = {
      'record':'R749SUJ', 'status':'PASS', 'arithmetic':'exact_integer',
      'independent_bruteforce_crosscheck_M':'2..120',
      'modular_inverse_scan_M':'2..600',
      'first_nonunit_q_M_up_to_600': first_nonunit,
      'specific_cases':cases,
      'conjecture':'all noncanonical threshold maximizers satisfy abs(u+v-a-d)=1',
      'disposition':'FALSIFIED_BY_M58_AND_M93',
      'scope':'finite exact U_M Port-observer auxiliary classification; no native-event admission'
    }
    print(json.dumps(results, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
