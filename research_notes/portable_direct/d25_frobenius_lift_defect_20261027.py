"""Original E3 coefficient-ring Frobenius-lift guard; author-only arithmetic."""
from math import comb


def mul(x, y, modulus):
    a, b = x
    c, d = y
    return ((a * c + 2 * b * d) % modulus, (a * d + b * c) % modulus)


def ring_pow(x, exponent, modulus):
    out = (1, 0)
    while exponent:
        if exponent & 1:
            out = mul(out, x, modulus)
        x = mul(x, x, modulus)
        exponent //= 2
    return out


def numerator_binomial(p):
    modulus = p * p
    accum = [0, 0]
    for k in range(p + 1):
        coeff = comb(p, k) * pow(2, p - k, modulus) * (-1 if k % 2 else 1)
        if k % 2:
            accum[1] += coeff * pow(2, (k - 1) // 2, modulus)
        else:
            accum[0] += coeff * pow(2, k // 2, modulus)
    return (accum[0] % modulus, accum[1] % modulus)


def audit(p):
    assert p > 3 and p % 24 in (13, 19)
    mod = p * p
    q2 = ((pow(2, p - 1, mod) - 1) % mod) // p
    q108 = ((pow(108, p - 1, mod) - 1) % mod) // p
    h = pow(2, (p - 1) // 2, mod)
    rho = ((h + 1) % mod) // p
    assert rho == (-q2 * pow(2, -1, p)) % p
    assert (h + 1) % mod == p * rho
    assert (ring_pow((0, 1), p, mod)[1] + 1) % mod == p * rho

    inv108 = pow(108, -1, mod)
    c = (2 * inv108 % mod, -inv108 % mod)
    sigma_c = (c[0], (-c[1]) % mod)
    actual = ring_pow(c, p, mod)
    # Independent direct binomial numerator (2 - T)^p / 108^p.
    bin_num = numerator_binomial(p)
    independent = tuple((v * pow(108, -p, mod)) % mod for v in bin_num)
    assert actual == independent
    diff = tuple((actual[i] - sigma_c[i]) % mod for i in (0, 1))
    assert all(v % p == 0 for v in diff)
    defect = tuple(v // p for v in diff)

    # Integer-valued first divided difference of (2-T)^p - (2+T).
    d_num = tuple(((bin_num[i] - (2 if i == 0 else 1)) % mod) // p for i in (0, 1))
    predicted = ((d_num[0] - 2 * q108) * pow(108, -1, p) % p,
                 (d_num[1] - q108) * pow(108, -1, p) % p)
    assert defect == predicted
    return dict(p=p, q2=q2, q108=q108, rho=rho, d_num=d_num,
                c=c, sigma_c=sigma_c, c_p=actual, defect=defect)


if __name__ == '__main__':
    for prime in (13, 19, 37, 43, 61, 67, 211, 373):
        record = audit(prime)
        if prime == 373:
            assert record == {
                'p': 373, 'q2': 204, 'q108': 192, 'rho': 271,
                'd_num': (303, 201), 'c': (105635, 16747),
                'sigma_c': (105635, 122382), 'c_p': (70573, 110819),
                'defect': (279, 342),
            }
            print('PASS_E3_SIGMA_VS_P_POWER_P373', record)
    print('PASS_E3_SIGMA_VS_P_POWER_EIGHT_PRIMES')
