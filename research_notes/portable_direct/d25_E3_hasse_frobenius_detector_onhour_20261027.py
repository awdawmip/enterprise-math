"""D25 original E3: exact Hasse p^2 Frobenius-defect detector.

Author-side exact arithmetic, not native H0/B0 divided-power execution.
All F_{p^2} operations use ordered pairs (a,b) representing a+b*T, T^2=2.
"""
from math import comb

PRIMES = (13, 19, 37, 43, 61, 67, 211, 373)


def add(a, b, mod):
    return ((a[0] + b[0]) % mod, (a[1] + b[1]) % mod)


def mul(a, b, mod):
    return ((a[0]*b[0] + 2*a[1]*b[1]) % mod,
            (a[0]*b[1] + a[1]*b[0]) % mod)


def power(a, exponent, mod):
    result = (1, 0)
    while exponent:
        if exponent & 1:
            result = mul(result, a, mod)
        a = mul(a, a, mod)
        exponent //= 2
    return result


def hasse_and_derivative(p, c, mod):
    """Coefficient [xi^(p-1)] omega/dxi and its ordinary c-derivative."""
    n = p - 1
    res = der = (0, 0)
    cp = (1, 0)
    previous = (0, 0)
    for j in range((p - 1)//3 + 1):
        factor = comb(2*j, j)*comb(n-j, 2*j)
        res = add(res, tuple(factor*z % mod for z in cp), mod)
        if j:
            der = add(der, tuple(j*factor*z % mod for z in previous), mod)
        previous, cp = cp, mul(cp, c, mod)
    return res, der


def legendre_value_derivative(p, x):
    """Independent finite-field Legendre 3-term recurrence and derivative."""
    n = (p - 1)//3
    prev, curr = (1, 0), x
    dprev, dcurr = (0, 0), (1, 0)
    for j in range(1, n):
        xc = mul(x, curr, p)
        xcprime = add(curr, mul(x, dcurr, p), p)
        inv = pow(j + 1, -1, p)
        nxt = tuple(inv*((2*j + 1)*xc[i] - j*prev[i]) % p for i in range(2))
        dnxt = tuple(inv*((2*j + 1)*xcprime[i] - j*dprev[i]) % p for i in range(2))
        prev, curr = curr, nxt
        dprev, dcurr = dcurr, dnxt
    return curr, dcurr


def check_prime(p):
    assert p > 3 and p % 24 in (13, 19)
    mod = p*p
    inv108 = pow(108, -1, mod)
    c = (2*inv108 % mod, -inv108 % mod)
    sigma_c = (c[0], -c[1] % mod)
    c_p = power(c, p, mod)
    delta_raw = tuple((c_p[i] - sigma_c[i]) % mod for i in range(2))
    assert all(v % p == 0 for v in delta_raw)
    delta_c = tuple(v // p for v in delta_raw)

    h_sigma, dh_sigma = hasse_and_derivative(p, sigma_c, mod)
    h_point, _ = hasse_and_derivative(p, c_p, mod)
    defect = tuple((h_point[i] - h_sigma[i]) % mod for i in range(2))
    delta_h = tuple(v // p for v in defect)
    assert all(v % p == 0 for v in defect)
    predicted = mul(tuple(v % p for v in dh_sigma), delta_c, p)
    assert delta_h == predicted

    # Mod-p Hasse = P_((p-1)/3)(1-54*c); conjugate x is -T/2.
    x = (0, -pow(2, -1, p) % p)
    pn, dpn = legendre_value_derivative(p, x)
    assert pn == (0, 0)
    assert tuple(v % p for v in h_sigma) == pn
    assert tuple(v % p for v in dh_sigma) == tuple(-54*v % p for v in dpn)
    assert tuple(v % p for v in dh_sigma) != (0, 0)
    assert (delta_h == (0, 0)) == (delta_c == (0, 0))

    # A norm-only check misses the p=37 anti-invariant residual.
    n_c = pow(18, -3, mod)
    nc_pow_difference = (pow(n_c, p, mod) - n_c) % mod
    qp18 = (pow(18, p-1, mod) - 1) % mod // p
    assert nc_pow_difference == p*((-3*pow(18, -3, p)*qp18) % p) % mod
    trace_c_delta = (2*mul(tuple(v % p for v in c), delta_c, p)[0]) % p
    assert trace_c_delta == (-3*pow(18, -3, p)*qp18) % p
    assert (nc_pow_difference == 0) == (qp18 == 0)
    if p == 37:
        assert qp18 == 0 and delta_c == (1, 1)
        assert delta_h == (33, 35)
    if p == 373:
        assert sigma_c == (105635, 122382)
        assert c_p == (70573, 110819)
        assert delta_c == (279, 342)
        assert tuple(v % p for v in dh_sigma) == (0, 326)
        assert h_sigma == (130177, 121225)
        assert h_point == (104067, 99591)
        assert delta_h == (303, 315)
    return (p, qp18, delta_c, tuple(v % p for v in dh_sigma), delta_h)


def main():
    for p in PRIMES:
        print('PASS', check_prime(p))
    print('PASS_E3_HASSE_FROBENIUS_SECOND_DIGIT_DETECTOR')


if __name__ == '__main__':
    main()
