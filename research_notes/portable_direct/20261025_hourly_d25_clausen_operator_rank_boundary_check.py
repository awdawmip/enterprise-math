"""Author exact-ring checks of the Clausen-compatible operator-jet identity."""


def product(a, b, degree, modulus):
    out = [0] * (degree + 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b[: degree + 1 - i]):
            out[i + j] = (out[i + j] + ai * bj) % modulus
    return out


def inverse_linear(a, b, degree, modulus):
    inv_a = pow(a % modulus, -1, modulus)
    return [(inv_a * pow((-b * inv_a) % modulus, j, modulus)) % modulus
            for j in range(degree + 1)]


def coefficients(p, degree, modulus):
    m = (p - 1) // 6
    half_p = p * pow(2, -1, modulus) % modulus
    rows = [[1] + [0] * degree]
    for r in range(1, p):
        a, b = r - 1 - m, r - 1 - 2 * m
        quadratic = [a * b % modulus, (-2 * a - b) % modulus, 2]
        denominator_inverse = inverse_linear(r - half_p, -3, degree, modulus)
        denominator_inverse = [v * pow(r, -1, modulus) % modulus for v in denominator_inverse]
        rows.append(product(product(rows[-1], quadratic, degree, modulus),
                            denominator_inverse, degree, modulus))
    return rows


def main():
    verified = 0
    for p in [7, 13, 19, 31, 37, 43, 73, 103]:
        mod, m, degree = p * p, (p - 1) // 6, 6
        rows = coefficients(p, degree, mod)

        def a(k, r):
            return rows[r][k] if 0 <= k <= degree and 0 <= r < p else 0

        for r in range(p):
            for k in range(degree + 1):
                lhs = (r * (r - p * pow(2, -1, mod)) * a(k, r)
                       - (r - 1 - m) * (r - 1 - 2 * m) * a(k, r - 1)
                       - 3 * r * a(k - 1, r)
                       + (3 * (r - 1) - 4 * m) * a(k - 1, r - 1)
                       - 2 * a(k - 2, r - 1)) % mod
                assert lhs == 0, (p, r, k, lhs)
                verified += 1
        for k in range(degree + 1):
            boundary = (-(p - 1 - m) * (p - 1 - 2 * m) * a(k, p - 1)
                        + (3 * (p - 1) - 4 * m) * a(k - 1, p - 1)
                        - 2 * a(k - 2, p - 1)) % mod
            if k == 2:
                assert boundary % p == p - 2
                assert a(2, p - 1) % p == 18 * pow(5, -1, p) % p
            verified += 1
        # A boundary-only correction cannot erase this interior rank-one defect.
        rank_one_residual = (a(0, 1) - 2 * m * m) % mod
        expected = p * m * m * pow((1 - p * pow(2, -1, mod)) % mod, -1, mod) % mod
        assert rank_one_residual == expected == p * m * m % mod
        verified += 1
    print(f"PASS: {verified} exact rank/Hasse and rank-one obstruction checks modulo p^2")


if __name__ == "__main__":
    main()
