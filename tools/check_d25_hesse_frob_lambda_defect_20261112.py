#!/usr/bin/env python3
"""Exact arithmetic in (Z/p² Z)[T]/(T²-2) for D25 Hesse source-port test.
Not a crystalline/native H0/B0 benchmark; this checks a parameter-power defect.
"""

TARGETS = (13, 19, 37, 43, 373)


def add(a, b, mod):
    return ((a[0] + b[0]) % mod, (a[1] + b[1]) % mod)


def sub(a, b, mod):
    return ((a[0] - b[0]) % mod, (a[1] - b[1]) % mod)


def mul(a, b, mod):
    return ((a[0]*b[0] + 2*a[1]*b[1]) % mod,
            (a[0]*b[1] + a[1]*b[0]) % mod)


def power(a, n, mod):
    out = (1, 0)
    while n:
        if n % 2:
            out = mul(out, a, mod)
        a = mul(a, a, mod)
        n //= 2
    return out


def conj(a, mod):
    return (a[0] % mod, -a[1] % mod)


def scalar(n, a, mod):
    return ((n*a[0]) % mod, (n*a[1]) % mod)


def inverse(a, mod):
    n = (a[0]*a[0] - 2*a[1]*a[1]) % mod
    inverse_n = pow(n, -1, mod)
    return scalar(inverse_n, conj(a, mod), mod)


def divide_by_p(a, p):
    """a is a pair of canonical representatives mod p², each p-divisible."""
    assert a[0] % p == 0 and a[1] % p == 0
    return ((a[0] // p) % p, (a[1] // p) % p)


def cube_root_t(p):
    """Find an explicit residue root, then uniquely lift this branch mod p²."""
    t = (4, 2)
    candidate = None
    for a in range(p):
        for b in range(p):
            root = (a, b)
            if power(root, 3, p) == (4 % p, 2 % p):
                candidate = root
                break
        if candidate is not None:
            break
    assert candidate is not None, f'No cube root for p={p}'
    m = p*p
    diff = sub(power(candidate, 3, m), t, m)
    derivative_inverse = inverse(scalar(3, power(candidate, 2, m), m), m)
    correction = mul(diff, derivative_inverse, m)
    lifted = sub(candidate, correction, m)
    assert power(lifted, 3, m) == t
    return lifted


def omega(a, mod):
    """Frozen Hesse Omega_H=omega_H +6 nabla_lambda omega_H, H-basis."""
    d = sub(power(a, 3, mod), (1, 0), mod)
    dinv = inverse(d, mod)
    first = sub((2, 0), scalar(9, mul(power(a, 2, mod), dinv, mod), mod), mod)
    second = scalar(-1, dinv, mod)
    return first, second


def omega_derivative(a, mod):
    d = sub(power(a, 3, mod), (1, 0), mod)
    inv_d2 = power(inverse(d, mod), 2, mod)
    first = mul(scalar(9, mul(a, add(power(a, 3, mod), (2, 0), mod), mod), mod), inv_d2, mod)
    second = mul(scalar(3, power(a, 2, mod), mod), inv_d2, mod)
    return first, second


def run():
    for p in TARGETS:
        m = p*p
        # p=373 uses the previously published frozen signed Hesse root.
        lam = (91441, 93269) if p == 373 else cube_root_t(p)
        assert power(lam, 3, m) == (4, 2)
        t = (4, 2)
        sigma_lam = conj(lam, m)
        lam_p = power(lam, p, m)
        delta = divide_by_p(sub(lam_p, sigma_lam, m), p)
        q_t = divide_by_p(sub(power(t, p, m), conj(t, m), m), p)
        assert scalar(3, mul(power(conj(lam, p), 2, p), delta, p), p) == q_t
        assert power(lam_p, 3, m) == power(t, p, m)
        assert power(sigma_lam, 3, m) == conj(t, m)
        # Direct evaluation vs the precise 1st-order deformation formula.
        direct = tuple(sub(x, y, m) for x, y in zip(omega(lam_p, m), omega(sigma_lam, m)))
        predicted = tuple(scalar(p, mul(delta, derivative, p), m) for derivative in omega_derivative(conj(lam, p), p))
        assert direct == predicted
        assert all(c[0] % p == 0 and c[1] % p == 0 for c in direct)
        print(f'p={p:3d}, lambda={lam}, lambda^p={lam_p}, sigma(lambda)={sigma_lam}, '
              f'Q_t={q_t}, D_lambda={delta}, observer_difference={direct}')


if __name__ == '__main__':
    run()
