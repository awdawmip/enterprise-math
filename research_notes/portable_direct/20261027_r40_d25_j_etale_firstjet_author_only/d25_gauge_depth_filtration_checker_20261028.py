#!/usr/bin/env python3
"""Exact integer witness for D25 auxiliary marked Frobenius gauge-depth filtration.
No original H0/B0 arithmetic is performed. Standard library only.
"""
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


def mul(a, b, m):
    return ((a[0] * b[0] + 2 * a[1] * b[1]) % m,
            (a[0] * b[1] + a[1] * b[0]) % m)


def sigma(a, m):
    return a[0] % m, (-a[1]) % m


def norm(a, m):
    return (a[0] * a[0] - 2 * a[1] * a[1]) % m


def inverse(a, m):
    return tuple((v * pow(norm(a, m), -1, m)) % m for v in sigma(a, m))


def principal_sqrt(t, p, n):
    m = p ** n
    t %= m
    assert t % p == 1
    x = 1
    for k in range(1, n):
        pk = p ** k
        digit = ((t - x * x) % (pk * p)) // pk
        digit = digit * pow(2 * x, -1, p) % p
        x += digit * pk
    assert x * x % m == t
    assert x % p == 1
    return x


def element(z, y, p, n):
    m = p ** n
    x = principal_sqrt(z + 2 * y * y, p, n)
    assert norm((x, y), m) == z % m
    return (x, y % m)


def conjugator(eta, xi, p, n):
    m = p ** n
    alpha = mul(xi, inverse(eta, m), m)
    assert norm(alpha, m) == 1
    inv2 = pow(2, -1, m)
    u = ((1 + alpha[0]) * inv2 % m, alpha[1] * inv2 % m)
    ratio = mul(u, inverse(sigma(u, m), m), m)
    assert ratio == alpha
    assert mul(eta, ratio, m) == xi
    return u


def exhaustive(p, n):
    m = p ** n
    norms = [1 + p * k for k in range(p ** (n - 1))]
    groups = defaultdict(list)
    for z in norms:
        for j in range(p ** (n - 1)):
            y = p * j
            eta = element(z, y, p, n)
            groups[z].append(eta)
    assert len(groups) == p ** (n - 1)
    assert all(len(g) == p ** (n - 1) for g in groups.values())
    witnesses = 0
    for depth in range(1, n + 1):
        q = p ** depth
        for z, elements in groups.items():
            by_y = defaultdict(list)
            for eta in elements:
                by_y[eta[1] % q].append(eta)
            assert len(by_y) == p ** (depth - 1), (p, n, depth, z)
            assert all(len(g) == p ** (n - depth) for g in by_y.values())
            for vals in by_y.values():
                base = vals[0]
                for eta in vals:
                    u = conjugator(base, eta, p, n)
                    assert u[0] % q == 1 % q and u[1] % q == 0
                    witnesses += 1
    return {'p': p, 'n': n, 'modulus': m,
            'normalized_elements': (p ** (n - 1)) ** 2,
            'norm_values': p ** (n - 1),
            'tested_depths': list(range(1, n + 1)),
            'conjugator_checks': witnesses}


def target_cases():
    targets = []
    for p in [13, 19, 37, 43, 109, 211, 373]:
        for n in [2, 3, 4]:
            modulus = p ** n
            z = (1 + p * (n + 4)) % modulus
            for depth in range(1, n):
                y0 = p * (n + 3)
                y1 = (y0 + p ** depth) % modulus
                eta = element(z, y0, p, n)
                xi = element(z, y1, p, n)
                u = conjugator(eta, xi, p, n)
                q = p ** depth
                assert u[0] % q == 1 % q and u[1] % q == 0
                assert y1 % (q * p) != y0 % (q * p)
                targets.append({'p': p, 'n': n, 'depth': depth, 'norm': z,
                                'y_before': y0, 'y_after': y1,
                                'conjugator': list(u), 'odd_digit_next_depth_changes': True})
    return targets


def main():
    rows = [exhaustive(p, n) for p, n in
            [(3, 2), (3, 3), (3, 4), (5, 2), (5, 3), (5, 4), (7, 2), (7, 3), (13, 2), (13, 3)]]
    targets = target_cases()
    result = {
        'schema': 'D25_AUXILIARY_GAUGE_DEPTH_EXACT_CHECK_V1',
        'scope': 'external quadratic ring B[T]/(T^2-2); not native H0/B0',
        'universal_proof': 'separate mathematical note; these finite checks are not the proof',
        'run_utc': datetime.now(timezone.utc).isoformat(),
        'status': 'PASS',
        'full_enumeration_rows': rows,
        'full_enumeration_normalized_elements': sum(r['normalized_elements'] for r in rows),
        'full_enumeration_conjugator_checks': sum(r['conjugator_checks'] for r in rows),
        'target_odd_digit_witness_count': len(targets),
        'p373_n4_witnesses': [r for r in targets if r['p'] == 373 and r['n'] == 4],
        'formula': 'for fixed norm z, gauge subgroup 1+p^m A has exactly p^(m-1) orbits of p^(n-m) elements each, labelled by y mod p^m',
        'gauge_convention': 'multiplication conjugacy u*(eta*sigma)*u^{-1}=(eta*u/sigma(u))*sigma',
    }
    path = Path(__file__).with_name('d25_gauge_depth_filtration_author_check_20261028.json')
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'rows': len(rows),
                      'normalized_elements': result['full_enumeration_normalized_elements'],
                      'conjugator_checks': result['full_enumeration_conjugator_checks'],
                      'target_witnesses': len(targets),
                      'p373_n4': result['p373_n4_witnesses'],
                      'output_path': str(path)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
