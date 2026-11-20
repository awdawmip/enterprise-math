#!/usr/bin/env python3
"""Exact author-side checks of split/nonsplit/Jordan residual gauge orbits.

Finite-field auxiliary model only; not a native Enterprise Math H0/B0 computation.
"""
from __future__ import annotations
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

I = (1, 0, 0, 1)
ZERO = (0, 0, 0, 0)


def add(a, b, p):
    return tuple((x+y) % p for x, y in zip(a, b))


def scale(a, c, p):
    return tuple((c*x) % p for x in a)


def sub(a, b, p):
    return add(a, scale(b, -1, p), p)


def mul(a, b, p):
    return ((a[0]*b[0]+a[1]*b[2]) % p,
            (a[0]*b[1]+a[1]*b[3]) % p,
            (a[2]*b[0]+a[3]*b[2]) % p,
            (a[2]*b[1]+a[3]*b[3]) % p)


def det(a, p):
    return (a[0]*a[3]-a[1]*a[2]) % p


def inv(a, p):
    d = pow(det(a, p), -1, p)
    return tuple((x*d) % p for x in (a[3], -a[1], -a[2], a[0]))


def comm(b, a, p):
    return sub(mul(b, a, p), mul(a, b, p), p)


def nonsquare(p):
    squares = {j*j % p for j in range(p)}
    return next(d for d in range(2, p) if d not in squares)


def setup(p, case):
    if case == 'split':
        a = (0, 0, 0, 1)
        def kval(u, v): return (0, u % p, v % p, 0)
        def bval(u, v): return (0, u % p, (-v) % p, 0)
        def uv(k):
            assert k[0] == k[3] == 0
            return (k[1], k[2])
        group = [(s, 0, 0, t) for s in range(1, p) for t in range(1, p)]
        def label(u, v):
            if not u and not v: return ('zero', 0)
            if not v: return ('upper_only', 0)
            if not u: return ('lower_only', 0)
            return ('both_nonzero_product', (u*v)%p)
        expected = p+2
    elif case == 'nonsplit':
        d = nonsquare(p)
        a = (0, d, 1, 0)
        def kval(u, v): return (v % p, (d*u) % p, (-u) % p, (-v) % p)
        def bval(u, v): return (u % p, v % p, 0, 0)
        def uv(k):
            u = (-k[2]) % p
            v = k[0]
            assert k == kval(u, v)
            return u, v
        group = [(s, (d*t)%p, t, s) for s in range(p) for t in range(p)
                 if (s*s-d*t*t)%p != 0]
        def label(u, v): return ('determinant', (d*u*u-v*v) % p)
        expected = p
    elif case == 'jordan':
        a = (0, 1, 0, 0)
        def kval(u, v): return ((-v) % p, u % p, 0, v % p)
        def bval(u, v): return (u % p, 0, v % p, 0)
        def uv(k):
            assert k[2] == 0 and k[0] == (-k[3])%p
            return k[1], k[3]
        group = [(s, t, 0, s) for s in range(1, p) for t in range(p)]
        def label(u, v): return ('v_nonzero', v) if v else ('v_zero_u', u)
        expected = 2*p-1
    else:
        raise ValueError(case)
    return a, kval, bval, uv, group, label, expected


def check(p, case):
    a, kval, bval, uv, group, label, expected = setup(p, case)
    classes = {}
    for u in range(p):
        for v in range(p):
            k = kval(u, v)
            assert comm(bval(u, v), a, p) == k, (p, case, u, v)
            assert uv(k) == (u, v)
            classes.setdefault(label(u, v), set()).add(k)
    assert len(classes) == expected, (p, case, len(classes), expected)
    sizes = Counter()
    actions = 0
    for key, fiber in classes.items():
        k0 = next(iter(fiber))
        orbit = set()
        for g in group:
            result = mul(mul(g, k0, p), inv(g, p), p)
            orbit.add(result)
            u1, v1 = uv(result)
            assert label(u1, v1) == key
            actions += 1
        assert orbit == fiber, (p, case, key, len(orbit), len(fiber))
        sizes[len(fiber)] += 1
    return dict(prime=p, type=case, non_scalar_A=list(a),
                centralizer_units=len(group), number_of_K=p*p,
                orbit_classes=len(classes), expected_classes=expected,
                orbit_size_histogram={str(k):v for k,v in sorted(sizes.items())},
                actions_checked=actions, verdict='PASS')


def check_second_jet(p, case, u, v):
    a, kval, bval, *_ = setup(p, case)
    b = bval(u, v)
    M = p**3
    even = add(I, scale(a,p,M),M)
    odd = scale(b,p,M)
    # Semilinear square: (even+T*odd)(even-T*odd), T^2=2
    odd_sq = sub(mul(odd, even, M), mul(even,odd,M),M)
    expected = scale(kval(u,v), p*p,M)
    assert odd_sq == expected
    return dict(prime=p,type=case,u=u,v=v,odd_square_mod_p3=list(odd_sq),predicted_mod_p3=list(expected),verdict='PASS')


def main():
    primes=[3,5,7,11,13,19]
    checks=[check(p,c) for p in primes for c in ('split','nonsplit','jordan')]
    samples=[check_second_jet(373,c,u,v) for c in ('split','nonsplit','jordan')
             for (u,v) in ((0,0),(1,0),(0,1),(1,1),(2,3),(372,5))]
    report={
        'schema':'D25_RANK2_RESIDUAL_GAUGE_ORBITS_AUTHOR_CHECK_V1',
        'date_utc':datetime.now(timezone.utc).isoformat(),
        'classification':'AUTHOR_EXACT_CHECKED / AUXILIARY_MODEL / UNREVIEWED / NOT_NATIVE / NOT_ADMITTED',
        'scope':'all rank-two non-scalar A, odd prime p, scalar Fp residual centralizer conjugacy',
        'analytical_counts':{'split':'p+2', 'nonsplit':'p', 'jordan':'2*p-1'},
        'p373_symbolic_prediction':{'split':375,'nonsplit':373,'jordan':745},
        'prime_cases':checks,
        'semilinear_odd_jet_samples':samples,
        'total_verified_finite_field_K':sum(row['number_of_K'] for row in checks),
        'total_group_actions':sum(row['actions_checked'] for row in checks),
        'second_jet_samples':len(samples),
        'all':'PASS',
        'limitations':'Finite checking supplements algebraic proof, does not establish native H0/B0 rank or permitted residual gauge group.'
    }
    out=Path(__file__).with_name('d25_rank2_residual_gauge_orbits_author_check_20261028.json')
    out.write_text(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ('all','total_verified_finite_field_K','total_group_actions','second_jet_samples','p373_symbolic_prediction')},ensure_ascii=False))

if __name__=='__main__':
    main()
