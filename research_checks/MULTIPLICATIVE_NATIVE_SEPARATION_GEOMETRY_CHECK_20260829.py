from math import gcd


def factor(n: int):
    assert n >= 1
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def support(n: int):
    return frozenset(factor(n))


def minimal_carrier_path(m: int, n: int):
    """Strict native path on bare integers: change exponents only, never birth/kill support.
    Returns an explicit path iff supports are equal.
    """
    fm, fn = factor(m), factor(n)
    if set(fm) != set(fn):
        return None
    cur = m
    path = [cur]
    for p in sorted(fm):
        while factor(cur)[p] > fn[p]:
            assert factor(cur)[p] >= 2
            cur //= p
            path.append(cur)
        while factor(cur)[p] < fn[p]:
            cur *= p
            path.append(cur)
    assert cur == n
    assert all(support(x) == support(m) for x in path)
    return path


def ambient_carrier_path(m: int, n: int, carrier):
    """Path in X_C = N_0^C, where zero exponents are allowed and C is fixed."""
    carrier = tuple(sorted(carrier))
    a = {p: factor(m).get(p, 0) for p in carrier}
    b = {p: factor(n).get(p, 0) for p in carrier}
    assert support(m) <= set(carrier)
    assert support(n) <= set(carrier)
    states = [tuple(a[p] for p in carrier)]
    for p in carrier:
        while a[p] > b[p]:
            a[p] -= 1
            states.append(tuple(a[q] for q in carrier))
        while a[p] < b[p]:
            a[p] += 1
            states.append(tuple(a[q] for q in carrier))
    assert states[-1] == tuple(b[p] for p in carrier)
    return states


def carrier_bridge_signature(m: int, n: int):
    cm, cn = support(m), support(n)
    return (len(cn - cm), len(cm - cn))  # births, deaths


def erosive_reachable(m: int, n: int):
    """Directed alphabet: multiply only existing primes; divide any current prime, allowing death.
    Reachability is equivalent to supp(n) subset supp(m).
    """
    return support(n) <= support(m)


def zero_pattern(x: int, primes):
    return frozenset(p for p in primes if x % p == 0)


def is_unit_mod(x: int, n: int):
    return gcd(x, n) == 1


def squarefree_zero_pattern_regression(primes):
    n = 1
    for p in primes:
        n *= p
    for x in range(n):
        for y in range(n):
            lhs = zero_pattern((x * y) % n, primes)
            rhs = zero_pattern(x, primes) | zero_pattern(y, primes)
            assert lhs == rhs, (n, x, y, lhs, rhs)

    units = [x for x in range(n) if is_unit_mod(x, n)]
    for x in units:
        for y in units:
            assert is_unit_mod((x * y) % n, n)
    closure = set(units) | {0}
    for x in closure:
        for y in closure:
            z = (x * y) % n
            assert z == 0 or is_unit_mod(z, n)


def diagonal_valuation_barrier(limit=8):
    diagonal = {(k, k) for k in range(-limit, limit + 1)}
    forbidden = {(t, 0) for t in range(-limit, limit + 1) if t != 0}
    forbidden |= {(0, t) for t in range(-limit, limit + 1) if t != 0}
    assert diagonal.isdisjoint(forbidden)


def run():
    assert minimal_carrier_path(8, 32) == [8, 16, 32]
    p = minimal_carrier_path(12, 18)
    assert p is not None and p[0] == 12 and p[-1] == 18
    assert minimal_carrier_path(6, 10) is None
    assert minimal_carrier_path(6, 35) is None
    assert minimal_carrier_path(12, 20) is None
    assert carrier_bridge_signature(8, 32) == (0, 0)
    assert carrier_bridge_signature(6, 10) == (1, 1)
    assert carrier_bridge_signature(6, 35) == (2, 2)
    assert sum(carrier_bridge_signature(6, 35)) == len(support(6) ^ support(35))

    assert erosive_reachable(12, 6)
    assert erosive_reachable(12, 3)
    assert not erosive_reachable(6, 35)
    assert not erosive_reachable(35, 6)

    C = support(6) | support(35)
    states = ambient_carrier_path(6, 35, C)
    assert states[0] == (1, 1, 0, 0)
    assert states[-1] == (0, 0, 1, 1)
    assert len(states) - 1 == 4

    assert support(6) <= {2, 3}
    assert support(6) <= {2, 3, 5}
    assert support(6) <= {2, 3, 5, 7}

    for ps in [(3, 5), (3, 7), (5, 7), (2, 3, 5), (3, 5, 7)]:
        squarefree_zero_pattern_regression(ps)
    diagonal_valuation_barrier()

    n = 15
    z = pow(2, 2, n) - 1
    assert 1 < gcd(z, n) < n
    assert gcd(z, n) == 3
    assert zero_pattern(z, (3, 5)) == frozenset({3})

    assert support(49) == frozenset({7})
    assert support(18) == frozenset({2, 3})
    assert support(50) == frozenset({2, 5})
    assert gcd(6, 10) == 2 and support(6) != support(10)
    assert gcd(6, 35) == 1 and support(6).isdisjoint(support(35))

    print('PASS: multiplicative native separation geometry exact regressions')
    print('strict path 12 -> 18:', p)
    print('ambient carrier path 6 -> 35 states:', states)
    print('selective collapse N=15, 2^2-1:', z, 'gcd=', gcd(z, n))


if __name__ == '__main__':
    run()
