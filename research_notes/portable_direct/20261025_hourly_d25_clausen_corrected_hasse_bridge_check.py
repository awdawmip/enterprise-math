"""Exact finite-ring checks for the Clausen-compatible D25 cutoff Hasse ports.

Author-derived portable evidence only. This does not run native CM experiments,
certify an all-prime result, or grant source/claim/review authority.
"""


def mul(a, b, degree, modulus):
    result = [0] * (degree + 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b[: degree + 1 - i]):
                result[i + j] = (result[i + j] + ai * bj) % modulus
    return result


def ports(p, degree, exponent):
    modulus = p**exponent
    m = (p - 1) // 6
    numerator = [1] + [0] * degree
    for h in range(-m, p - m):
        numerator = mul(numerator, [h % modulus, -1 % modulus], degree, modulus)
    for h in range(-2 * m, p - 2 * m):
        numerator = mul(numerator, [h % modulus, -2 % modulus], degree, modulus)
    factorial = 1
    for j in range(1, p):
        factorial = factorial * j % modulus
    old = [v * pow(factorial * factorial, -1, modulus) % modulus for v in numerator]

    # D(t)=prod_{j=1}^{p-1} j/(j-p/2-3t); all factors have unit constants.
    half_p = p * pow(2, -1, modulus) % modulus
    drift = [1] + [0] * degree
    for j in range(1, p):
        inverse_constant = pow((j - half_p) % modulus, -1, modulus)
        local = [j * inverse_constant * pow(3 * inverse_constant, k, modulus) % modulus
                 for k in range(degree + 1)]
        drift = mul(drift, local, degree, modulus)
    corrected = mul(old, drift, degree, modulus)
    return [(-v) % modulus for v in old], [(-v) % modulus for v in corrected]


def harmonic(p, bound, order, modulus):
    return sum(pow(j, -order, modulus) for j in range(1, bound + 1)) % modulus


def main():
    middle_pairs = 0
    for p in [7, 13, 19, 31, 37, 43, 73, 103]:
        assert p % 6 == 1
        m, modulus = (p - 1) // 6, p * p
        old, corrected = ports(p, p, 2)
        for n in range(1, p - 1):
            hn = harmonic(p, p - 1, n, modulus)
            hn1 = harmonic(p, p - 1, n + 1, modulus)
            hm = harmonic(p, m, n + 1, modulus)
            h2m = harmonic(p, 2 * m, n + 1, modulus)
            old_formula = (2 * ((1 + pow(2, n, modulus)) * pow(n, -1, modulus) * hn
                                - (-1) ** n * p * (hm + pow(2, n, modulus) * h2m))) % modulus
            denominator_coefficient = (pow(3, n, modulus) * pow(n, -1, modulus) * hn
                                       + pow(3, n, modulus) * p * pow(2, -1, modulus) * hn1) % modulus
            corrected_formula = (old_formula - 2 * denominator_coefficient) % modulus
            assert old[n + 2] == old_formula, (p, n, "old", old[n + 2], old_formula)
            assert corrected[n + 2] == corrected_formula, (p, n, "corrected", corrected[n + 2], corrected_formula)
            middle_pairs += 1
        assert (corrected[4] - old[4]) % modulus == (-9 * harmonic(p, p - 1, 2, modulus)) % modulus

    support_cases = 0
    for p in [7, 13, 19, 31, 37, 43]:
        old, corrected = ports(p, 2 * p, 1)
        assert [(i, v) for i, v in enumerate(old) if v] == [(2, p - 2), (p + 1, 4), (2 * p, p - 2)]
        assert [(i, v) for i, v in enumerate(corrected) if v] == [(2, p - 2), (p + 1, 2)]
        support_cases += 1
    print(f"PASS: {middle_pairs} full-range (prime, Hasse-order) checks modulo p^2; "
          f"{support_cases} complete-support checks modulo p")


if __name__ == "__main__":
    main()
