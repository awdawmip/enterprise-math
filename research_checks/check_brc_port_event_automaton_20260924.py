#!/usr/bin/env python3
"""Finite falsification for the BRC exact port-event automaton.

Proof is in research_notes/brc_port_event_automaton_20260924.md.
Finite computation is regression/falsification only.
"""
from sympy import primerange


def vp(n, p):
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c


def target_primes(limit):
    return [p for p in primerange(13, limit) if p % 24 in (13, 19)]


def ord_mod(a, p):
    x = 1
    for d in range(1, p):
        x = (x * a) % p
        if x == 1:
            return d
    raise AssertionError((a, p))


def epsilon(p, j):
    return 0 if (2 * j) % (p - 1) == 0 else 1


def beta_raw(p, j):
    return 2 * j + epsilon(p, j) + vp(1 + 4**j, p) - vp(j, p)


def invariants(p):
    if p % 24 == 19:
        return {"kind": 19}
    o4 = ord_mod(4, p)
    assert o4 % 2 == 0
    s = o4 // 2
    c = vp(1 + 4**s, p)
    return {"kind": 13, "s": s, "c": c}


def beta_automaton(p, j, inv=None):
    inv = inv or invariants(p)
    endpoint = int((2 * j) % (p - 1) == 0)
    a = vp(j, p)
    generic = 2 * j + 1
    if inv["kind"] == 19:
        return generic - endpoint - a
    s, c = inv["s"], inv["c"]
    cancel = int(j % s == 0 and (j // s) % 2 == 1)
    assert not (cancel and endpoint)
    return generic - endpoint - a + cancel * (a + c)


def main():
    ps = target_primes(5000)
    raw_fail = []
    event_fail = []
    class13_pmul = []
    first_intersections = []

    for p in ps:
        inv = invariants(p)
        for j in range(1, 501):
            b0 = beta_raw(p, j)
            b1 = beta_automaton(p, j, inv)
            if b0 != b1:
                raw_fail.append((p, j, b0, b1))
                continue

            n_generic = 2 * j + 2
            n_branch = b1 + 1
            delta = b1 - (2 * j + 1)
            if delta < 0:
                d = -delta
                if n_branch != n_generic - d:
                    event_fail.append((p, j, "lower", n_branch, n_generic, d))
            elif delta > 0:
                if n_branch != n_generic + delta:
                    event_fail.append((p, j, "raise", n_branch, n_generic, delta))
            elif n_branch != n_generic:
                event_fail.append((p, j, "same", n_branch, n_generic, delta))

        h = (p - 1) // 2
        j = p * h
        b = beta_automaton(p, j, inv)
        assert b == 2 * j - 1, (p, j, b)
        first_intersections.append((p, j, b + 1))

        assert beta_automaton(p, p, inv) == 2 * p
        assert beta_automaton(p, h, inv) == p - 1

        if inv["kind"] == 13:
            s, c = inv["s"], inv["c"]
            j = s * p
            b = beta_automaton(p, j, inv)
            assert b == 2 * j + 1 + c, (p, s, c, j, b)
            class13_pmul.append((p, s, c, j, b))

    assert not raw_fail, raw_fail[:5]
    assert not event_fail, event_fail[:5]

    print({
        "status": "PASS",
        "target_primes": len(ps),
        "classes": {13: sum(p % 24 == 13 for p in ps), 19: sum(p % 24 == 19 for p in ps)},
        "j_range": [1, 500],
        "raw_vs_automaton_failures": len(raw_fail),
        "event_window_failures": len(event_fail),
        "first_intersections": first_intersections[:4],
        "class13_p_multiple_cancellation_examples": class13_pmul[:4],
    })


if __name__ == "__main__":
    main()
