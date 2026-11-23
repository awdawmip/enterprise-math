#!/usr/bin/env python3
"""Author exact rational checks for threshold contact energy, not formal review."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import random


def energy(values, left, right):
    return sum((values[n + 1] - values[n]) ** 2 for n in range(left, right))


def positive_square(values, left, right):
    return sum(max(values[n], F(0)) ** 2 / n ** 2
               for n in range(left, right + 1))


def gamma(left, right):
    h = right - left
    return sum(F((n - left) * (right - n), h * n * n)
               for n in range(left + 1, right))


def components(values, left, right):
    assert values[left] == values[right] == 0
    result = []
    n = left + 1
    while n < right:
        if values[n] <= 0:
            n += 1
            continue
        start = n - 1
        while n < right and values[n] > 0:
            n += 1
        result.append((start, n))
    return result


def threshold_bound(road, reference, left, right, tau, check_closed_form=False):
    assert tau >= 0
    residual = {n: road[n] - reference[n] for n in range(left, right + 1)}
    assert residual[left] == residual[right] == 0
    u = {n: max(residual[n] - tau * n, F(0))
         for n in range(left, right + 1)}
    pools = components(u, left, right)
    budget = F(0)
    for a, b in pools:
        h = b - a
        chord = {n: residual[a] + F(n - a, h) * (residual[b] - residual[a])
                 for n in range(a, b + 1)}
        z = {n: residual[n] - chord[n] for n in range(a, b + 1)}
        v = {n: z[n] - u[n] for n in range(a, b + 1)}
        cross = sum((u[n + 1] - u[n]) * (v[n + 1] - v[n])
                    for n in range(a, b))
        by_parts = sum(u[n] * (2 * v[n] - v[n - 1] - v[n + 1])
                       for n in range(a + 1, b))
        assert cross == by_parts and cross >= 0
        ez, eu = energy(z, a, b), energy(u, a, b)
        assert eu <= ez
        weight = gamma(a, b)
        assert weight <= F(h * h - 1, 6 * a * a)
        if check_closed_form:
            h1 = sum(F(1, n) for n in range(a + 1, b))
            h2 = sum(F(1, n * n) for n in range(a + 1, b))
            assert weight == ((a + b) * h1 - (h - 1) - a * b * h2) / h
        assert positive_square(u, a, b) <= weight * ez
        # Ground-state identity for the locally centered cumulative edge field.
        e = {n: n * residual[n + 1] - (n + 1) * residual[n]
             for n in range(a, b)}
        mean = F(a * residual[b] - b * residual[a], h)
        variance = sum(F(1, n * (n + 1)) * (e[n] - mean) ** 2
                       for n in range(a, b))
        assert variance == ez
        budget += weight * ez
    floor = {n: max(reference[n] + tau * n, F(0))
             for n in range(left, right + 1)}
    for n in range(left, right + 1):
        assert max(road[n], F(0)) <= floor[n] + u[n]
    su = positive_square(u, left, right)
    sfloor = positive_square(floor, left, right)
    actual = positive_square(road, left, right)
    assert su <= budget
    gap = actual - sfloor - budget
    assert gap <= 0 or gap ** 2 <= 4 * sfloor * budget
    return {'budget': budget, 'floor_square': sfloor, 'actual_square': actual,
            'excess_square': su, 'pools': pools, 'u': u}


def interval(x, digits=35):
    x = F(x)
    scale = 10 ** digits
    lo, hi = (x * scale).__floor__(), (x * scale).__ceil__()
    def fmt(n):
        sign = '-' if n < 0 else ''
        n = abs(n)
        return f'{sign}{n // scale}.{n % scale:0{digits}d}'
    return {'lower': fmt(lo), 'upper': fmt(hi)}


def general_checks():
    rng = random.Random(2026112302)
    count = 0
    component_count = 0
    for _ in range(48):
        left = rng.randint(2, 20)
        right = rng.randint(left + 2, 2 * left)
        a, b = F(rng.randint(-10, 10), 3), F(rng.randint(-20, 20), 2)
        reference = {n: a * n + b for n in range(left, right + 1)}
        residual = {n: F(rng.randint(-4, 30), rng.randint(1, 9))
                    for n in range(left, right + 1)}
        residual[left] = residual[right] = F(0)
        road = {n: reference[n] + residual[n] for n in residual}
        for tau in (F(0), F(1, 100), F(1, 5), F(2)):
            result = threshold_bound(road, reference, left, right, tau, True)
            count += 1
            component_count += len(result['pools'])
    return {'exact_cases': count, 'positive_components_checked': component_count,
            'signed_reference_and_residual_cases': True,
            'all_closed_window_integer_checks': True}


def padded_family(s):
    x, h = s ** 4, s ** 3
    right = 2 * x
    eps = F(1, x ** 3)
    q = {}
    for n in range(x, right + 1):
        r = (n - x) % h
        q[n] = F(r * r * (h - r) ** 2, x * h * h)
    base = {n: eps * n if x < n < right else F(0)
            for n in range(x, right + 1)}
    road = {n: q[n] + base[n] for n in q}
    zero = {n: F(0) for n in q}
    for n in range(x - 1, right + 2):
        second = road.get(n - 1, F(0)) - 2 * road.get(n, F(0)) + road.get(n + 1, F(0))
        assert abs(second) <= F(5, n)
    assert all(road[n] > 0 for n in range(x + 1, right))
    actual = positive_square(road, x, right)
    assert F(81, 524288) <= actual < F(1, 128)
    original = threshold_bound(q, zero, x, right, F(0))
    bare = threshold_bound(road, zero, x, right, F(0))
    stable = threshold_bound(road, zero, x, right, eps)
    assert original['budget'] <= F(1, 315)
    assert bare['pools'] == [(x, right)]
    assert bare['budget'] >= F(27 * s * s, 1048576)
    assert stable['u'] == q
    assert stable['pools'] == [(x + i * h, x + (i + 1) * h) for i in range(s)]
    assert stable['budget'] <= F(2, 315) + F(5, 3) * eps ** 2 * h ** 2
    assert stable['floor_square'] == (x + 1) * eps ** 2
    eq, eb = energy(q, x, right), energy(base, x, right)
    cross = sum((q[n + 1] - q[n]) * (base[n + 1] - base[n])
                for n in range(x, right))
    assert cross == 3 * eps * x * q[x + 1]
    assert eb == eps ** 2 * x * (5 * x - 1)
    assert eq >= F(9 * s * s, 8192)
    levels = []
    delta = 2
    while delta <= x:
        total = F(0)
        for left in range(x, right, delta):
            peak, end = left + delta // 2, left + delta
            t = F(2, delta) * (2 * road[peak] - road[left] - road[end])
            total += delta ** 3 * max(t, F(0)) ** 2 / x ** 2
        if delta <= h:
            assert total <= F(25 * delta ** 4, 4 * x ** 3) <= F(25, 4)
        else:
            assert total <= 36 * eps ** 2 * x
        levels.append({'width': delta, 'normalized_positive_width_budget': interval(total)})
        delta *= 2
    return {'s': s, 'X': x, 'h': h, 'epsilon': str(eps),
            'grid': 'all integers, fixed before road values; zero fine remainder',
            'source_integer_checks': x + 3,
            'actual_positive_energy': interval(actual),
            'original_contact_budget': interval(original['budget']),
            'padded_bare_contact_budget': interval(bare['budget']),
            'threshold_contact_budget': interval(stable['budget']),
            'threshold_floor_square': interval(stable['floor_square']),
            'bare_to_threshold_budget_ratio': interval(bare['budget'] / stable['budget']),
            'original_pool_count': len(original['pools']), 'padded_bare_pool_count': 1,
            'threshold_pool_count': len(stable['pools']), 'fixed_tree_levels': levels,
            'status': 'PASS'}


def main():
    root = Path(__file__).resolve().parent
    result = {'schema': 'RH_THRESHOLD_CONTACT_CERTIFICATE_V1', 'status': 'PASS',
              'scope': 'Author exact finite checks; general source families, not actual arithmetic q',
              'arithmetic': 'Fraction exactly; decimal displays rounded outward',
              'general': general_checks(), 'families': [padded_family(s) for s in (2, 4, 8)],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'proof_sha256_at_run': hashlib.sha256((root / 'THRESHOLD_CONTACT_ENERGY.md').read_bytes()).hexdigest()}
    (root / 'threshold_contact_certificate.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'general': result['general'],
                      'families': [{k: row[k] for k in ('s', 'X', 'actual_positive_energy',
                                   'padded_bare_contact_budget', 'threshold_contact_budget',
                                   'bare_to_threshold_budget_ratio')} for row in result['families']]}, ensure_ascii=False))


if __name__ == '__main__':
    main()
