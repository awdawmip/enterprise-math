#!/usr/bin/env python3
"""Exact author-side finite-prime checker for the (m,1) block-gauge plateau.

Does not evaluate native H0/B0, source CLAIM, or enterprise geometry.
"""
import json
from collections import Counter, deque
from itertools import product
from math import prod
from pathlib import Path


def primitive_root(p):
    factors = [a for a in range(2, p) if (p - 1) % a == 0 and all(a % b for b in range(2, int(a ** .5) + 1))]
    for g in range(2, p):
        if all(pow(g, (p - 1) // f, p) != 1 for f in factors):
            return g
    return 1


def signature(s, m, p):
    x, y = s[:m], s[m:]
    return (int(any(x)), int(any(y)), sum(a * b for a, b in zip(x, y)) % p)


def generators(m, p):
    # Elementary transvections generate SL_m(F_p); one primitive diagonal generates determinant image.
    for i in range(m):
        for j in range(m):
            if i == j:
                continue
            def f(s, i=i, j=j):
                x = list(s[:m]); y = list(s[m:])
                x[i] = (x[i] + x[j]) % p
                y[j] = (y[j] - y[i]) % p
                return tuple(x + y)
            yield f
    g = primitive_root(p)
    gi = pow(g, -1, p)
    def diag(s):
        x = list(s[:m]); y = list(s[m:])
        x[0] = (x[0] * g) % p; y[0] = (y[0] * gi) % p
        return tuple(x + y)
    yield diag


def expected_signature_sizes(m, p):
    out = {(0, 0, 0): 1, (1, 0, 0): p ** m - 1, (0, 1, 0): p ** m - 1}
    if m >= 2:
        out[(1, 1, 0)] = (p ** m - 1) * (p ** (m - 1) - 1)
    for c in range(1, p):
        out[(1, 1, c)] = (p ** m - 1) * p ** (m - 1)
    return out


def exhaustive(m, p):
    gens = list(generators(m, p))
    remaining = set(product(range(p), repeat=2 * m))
    seen_label = {}
    action_checks = 0
    while remaining:
        first = next(iter(remaining))
        label = signature(first, m, p)
        q = deque([first]); remaining.remove(first)
        n = 0
        while q:
            s = q.popleft(); n += 1
            assert signature(s, m, p) == label, (m, p, 'non-equivariant generator')
            for g in gens:
                w = g(s); action_checks += 1
                assert signature(w, m, p) == label, (m, p, 'invariant not preserved')
                if w in remaining:
                    remaining.remove(w); q.append(w)
        assert label not in seen_label, (m, p, label, 'disconnected invariant fiber')
        seen_label[label] = n
    expected = expected_signature_sizes(m, p)
    assert seen_label == expected, (m, p, seen_label, expected)
    assert sum(seen_label.values()) == p ** (2 * m)
    return {
        'p': p, 'm': m, 'state_count': p ** (2 * m),
        'orbits': len(seen_label), 'expected_orbits': p + 3 if m >= 2 else p + 2,
        'action_checks': action_checks, 'zero_scalar_orbits':
        sum(1 for l in seen_label if l[-1] == 0),
        'orbits_sizes': [{'label': list(k), 'cardinality': v} for k, v in sorted(seen_label.items())]
    }


def block_commutator_test(p, m):
    n = m + 1
    a, b = 0, 1
    A = [a] * m + [b]
    total = 0
    for seed in range(80):
        B = [[(seed * 117 + i * 31 + j * 43 + i * j * 13 + 7) % p for j in range(n)] for i in range(n)]
        K = [[(B[i][j] * A[j] - A[i] * B[i][j]) % p for j in range(n)] for i in range(n)]
        X = [K[i][m] for i in range(m)]
        Y = [K[m][j] for j in range(m)]
        assert all(K[i][j] == 0 for i in range(m) for j in range(m))
        assert K[m][m] == 0
        assert sum(K[i][m] * K[m][i] for i in range(m)) % p == sum(x*y for x,y in zip(X,Y)) % p
        trace2 = sum(K[i][j] * K[j][i] for i in range(n) for j in range(n)) % p
        assert trace2 == 2 * sum(x*y for x,y in zip(X,Y)) % p
        total += 1
    return total


def main():
    cases = [(1,3), (1,5), (1,7), (1,11), (2,3), (2,5), (2,7), (2,11), (3,3), (3,5), (3,7), (4,3)]
    checks = [exhaustive(m, p) for m, p in cases]
    direct = {f'm{m}_p{p}': block_commutator_test(p, m)
              for m, p in [(2,3),(2,19),(3,5),(3,373),(4,3),(4,373)]}
    out = {'result': 'PASS', 'scope': 'exhaustive GL_m(F_p) action via elementary generators; local author only',
           'theorem_scope': 'all finite fields F_q for m>=2 by algebraic proof; m=1 edge',
           'finite_cases': len(checks), 'total_states': sum(c['state_count'] for c in checks),
           'total_generator_checks': sum(c['action_checks'] for c in checks),
           'cases': checks, 'direct_block_matrix_checks': direct,
           'p373_conditional_predictions': {f'm{m}': {
               'jet_population': 373 ** (2 * m),
               'source_fiber_per_jet': 373 ** (m*m+1),
               'full_gauge_orbits': 376,
               'scalar_max_effective_gauge_orbits': 1 + (373 ** (2 * m) - 1) // 372,
           } for m in [2, 3, 4]},
           'native_h0_b0_run': False, 'source_claim': False, 'independent_reviewer': False}
    path = Path(__file__).with_name('d25_block_m1_gauge_plateau_author_check_20261028.json')
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2, sort_keys=True)+'\n', encoding='utf-8')
    print(json.dumps({k:out[k] for k in ['result', 'finite_cases','total_states','total_generator_checks','direct_block_matrix_checks','p373_conditional_predictions']}, ensure_ascii=False))

if __name__ == '__main__':
    main()
