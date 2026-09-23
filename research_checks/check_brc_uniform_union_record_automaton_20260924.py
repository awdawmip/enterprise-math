#!/usr/bin/env python3
"""Finite regression for the BRC uniform-union record automaton.

This checker is falsification/regression only. The proof is the exact
defect identity and finite-candidate argument recorded in the companion note.
"""
from math import isqrt

TARGET_RESIDUES = (13, 19)


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def target_primes(limit):
    return [p for p in range(2, limit + 1) if is_prime(p) and p % 24 in TARGET_RESIDUES]


def vp(n, p):
    n = abs(n)
    if n == 0:
        raise ValueError("vp(0) not used")
    out = 0
    while n % p == 0:
        out += 1
        n //= p
    return out


def vp_factorial(n, p):
    out = 0
    while n:
        n //= p
        out += n
    return out


def prime_factors(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out.append(n)
    return out


def order4(p):
    o = p - 1
    for r in prime_factors(o):
        while o % r == 0 and pow(4, o // r, p) == 1:
            o //= r
    return o


_ORDER = {}
_CVAL = {}


def order4_cached(p):
    if p not in _ORDER:
        _ORDER[p] = order4(p)
    return _ORDER[p]


def cancel_data(p, j):
    if p % 24 != 13:
        return False, 0
    o = order4_cached(p)
    assert o % 2 == 0
    s = o // 2
    C = (j % s == 0) and ((j // s) % 2 == 1)
    if not C:
        return False, 0
    if p not in _CVAL:
        _CVAL[p] = vp(pow(4, s) + 1, p)
    return True, _CVAL[p]


def endpoint(p, j):
    return j % ((p - 1) // 2) == 0


def beta_raw(p, j):
    eps = 0 if endpoint(p, j) else 1
    return 2 * j + eps + vp(pow(4, j) + 1, p) - vp(j, p)


def beta_automaton(p, j):
    g = 2 * j + 1
    E = int(endpoint(p, j))
    a = vp(j, p)
    C, c = cancel_data(p, j)
    if C:
        assert E == 0
        return g + c
    return g - E - a


def winf(m):
    return sum(mult * (2 * j + 1) for j, mult in m.items())


def wp_raw(p, m):
    return sum(mult * beta_raw(p, j) - vp_factorial(mult, p)
               for j, mult in m.items())


def defect_raw(p, m):
    return winf(m) - wp_raw(p, m)


def defect_automaton(p, m):
    out = 0
    for j, mult in m.items():
        E = int(endpoint(p, j))
        a = vp(j, p)
        C, c = cancel_data(p, j)
        out += mult * (E + a - (a + c if C else 0))
        out += vp_factorial(mult, p)
    return out


def candidate_primes(m):
    if not m:
        return []
    max_j = max(m)
    max_mult = max(m.values())
    limit = max(2 * max_j + 1, max_mult, 13)
    out = []
    for p in target_primes(limit):
        if p <= max_mult:
            out.append(p)
            continue
        if any(j % p == 0 or j % ((p - 1) // 2) == 0 for j in m):
            out.append(p)
    return out


def uniform_defect_record(m):
    record = 0
    updates = []
    for p in candidate_primes(m):
        d = defect_automaton(p, m)
        if d > record:
            updates.append((p, d, record, winf(m) - d + 1, winf(m) - record))
            record = d
    return record, updates


def enumerate_monomials(max_winf):
    parts = [(j, 2 * j + 1)
             for j in range(1, (max_winf - 1) // 2 + 1)]
    out = []

    def rec(idx, remaining, cur):
        if idx == len(parts):
            out.append(dict(cur))
            return
        j, w = parts[idx]
        for mult in range(remaining // w + 1):
            if mult:
                cur[j] = mult
            rec(idx + 1, remaining - mult * w, cur)
            if mult:
                del cur[j]

    rec(0, max_winf - 1, {})
    return out


def main():
    primes_5000 = target_primes(5000)
    port_failures = []
    for p in primes_5000:
        for j in range(1, 501):
            if beta_raw(p, j) != beta_automaton(p, j):
                port_failures.append((p, j, beta_raw(p, j), beta_automaton(p, j)))

    monomials = enumerate_monomials(50)
    monomial_defect_failures = []
    candidate_reduction_failures = []
    record_window_failures = []
    for m in monomials:
        if not m:
            continue
        raw_values = []
        for p in primes_5000:
            dr = defect_raw(p, m)
            da = defect_automaton(p, m)
            if dr != da:
                monomial_defect_failures.append((m, p, dr, da))
                break
            raw_values.append((p, dr))
        if monomial_defect_failures:
            break
        brute = max([0] + [d for _, d in raw_values])
        candidate = max([0] + [defect_automaton(p, m) for p in candidate_primes(m)])
        record, updates = uniform_defect_record(m)
        if brute != candidate or candidate != record:
            candidate_reduction_failures.append((m, brute, candidate, record))
            break
        old = 0
        W = winf(m)
        for p, new, prev, lo, hi in updates:
            if prev != old or not (new > prev):
                record_window_failures.append((m, "record", p, new, prev, old))
                break
            if (lo, hi) != (W - new + 1, W - prev):
                record_window_failures.append((m, "window", p, lo, hi))
                break
            old = new
        if record_window_failures:
            break

    primitive_endpoint_failures = []
    primitive_novel = []
    primitive_covered = []
    deep_cover_examples = []
    for p in primes_5000:
        j = (p - 1) // 2
        assert defect_automaton(p, {j: 1}) == 1
        prev_candidates = [q for q in target_primes(p - 1) if q < p]
        prev = max([0] + [defect_automaton(q, {j: 1}) for q in prev_candidates])
        for q in prev_candidates:
            E = endpoint(q, j)
            a = vp(j, q)
            C, _ = cancel_data(q, j)
            criterion_positive = E or (a > 0 and not C)
            actual_positive = defect_automaton(q, {j: 1}) > 0
            if criterion_positive != actual_positive:
                primitive_endpoint_failures.append((p, q, j, criterion_positive, actual_positive))
        if primitive_endpoint_failures:
            break
        if prev == 0:
            primitive_novel.append(p)
        else:
            primitive_covered.append(p)
            if prev >= 2 and len(deep_cover_examples) < 8:
                src = [(q, defect_automaton(q, {j: 1}))
                       for q in prev_candidates
                       if defect_automaton(q, {j: 1}) == prev]
                deep_cover_examples.append((p, j, prev, src))

    denominator_failures = []
    for p in primes_5000:
        j = p
        qs = target_primes(2 * p + 1)
        vals = [(q, defect_automaton(q, {j: 1})) for q in qs]
        D = max([0] + [d for _, d in vals])
        src = [q for q, d in vals if d == D and d > 0]
        if D != 1 or src != [p]:
            denominator_failures.append((p, D, src))

    ok = not (port_failures or monomial_defect_failures or candidate_reduction_failures
              or record_window_failures or primitive_endpoint_failures or denominator_failures)
    summary = {
        "status": "PASS" if ok else "FAIL",
        "target_primes_lt_5000": len(primes_5000),
        "port_j_range": [1, 500],
        "port_failures": len(port_failures),
        "monomials_Winf_lt_50": len(monomials),
        "monomial_defect_failures": len(monomial_defect_failures),
        "candidate_reduction_failures": len(candidate_reduction_failures),
        "record_window_failures": len(record_window_failures),
        "primitive_endpoint_criterion_failures": len(primitive_endpoint_failures),
        "primitive_endpoint_uniform_novel_count": len(primitive_novel),
        "primitive_endpoint_covered_count": len(primitive_covered),
        "primitive_endpoint_first_novel": primitive_novel[:12],
        "primitive_endpoint_deep_cover_examples": deep_cover_examples,
        "denominator_singleton_failures": len(denominator_failures),
    }
    print(summary)
    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
