#!/usr/bin/env python3
"""Author-side exact coefficient-ring comparison; NOT the native H0/B0 experiment."""

def mul(x, y, m):
    return ((x[0] * y[0] + 2 * x[1] * y[1]) % m,
            (x[0] * y[1] + x[1] * y[0]) % m)

def sigma(x, m):
    return (x[0] % m, (-x[1]) % m)

def square(matrix, p, scalar):
    m = p * p
    b = tuple(tuple(mul(scalar, x, m) for x in row) for row in matrix)
    sb = tuple(tuple(sigma(x, m) for x in row) for row in b)
    return tuple(tuple(
        tuple(sum(mul(b[i][k], sb[k][j], m)[v] for k in range(2)) % m
              for v in (0, 1))
        for j in range(2)) for i in range(2))

def unit_candidate(p, a, b):
    m = p * p
    upper = mul((-p, 0), sigma(a, m), m)
    return (((0, 0), upper), (b, (0, 0)))

def finite_primes(n):
    for p in range(5, n + 1):
        if all(p % d for d in range(2, int(p ** .5) + 1)):
            yield p

def main():
    ps = [p for p in finite_primes(2000) if p % 24 in (13, 19)]
    assert len(ps) == 77
    for p in ps:
        m = p * p
        epsilon = (p % 24 == 13)
        delta = ((pow(2, -((p - 1) // 4), p), 0) if epsilon
                 else (0, pow(2, -((p + 1) // 4), p)))
        rho = delta if epsilon else mul((1, 1), delta, p)
        n_delta = mul(delta, sigma(delta, p), p)
        n_rho = mul(rho, sigma(rho, p), p)
        assert n_delta == (p - 1 if epsilon else 1, 0)
        assert n_rho == (p - 1, 0)
        M = unit_candidate(p, (1, 0), (1, 0))
        assert square(M, p, (1, 0)) == (((m - p, 0), (0, 0)), ((0, 0), (m - p, 0)))
        assert square(M, p, rho) == (((p, 0), (0, 0)), ((0, 0), (p, 0)))
    original_e3_coefficients = {
        19: ((11, 16), (18, 17), (0, 3), (6, 3)),
        373: ((349, 48), (131, 262), (269, 0), (269, 0)),
    }
    for p, (a, b, delta, rho) in original_e3_coefficients.items():
        M = unit_candidate(p, a, b)
        m = p * p
        assert mul(a, b, p) == (1, 0)
        assert square(M, p, (1, 0)) == (((m - p, 0), (0, 0)), ((0, 0), (m - p, 0)))
        delta_square = square(M, p, delta)
        rho_square = square(M, p, rho)
        assert delta_square == (((p if p == 373 else m - p, 0), (0, 0)),
                                ((0, 0), (p if p == 373 else m - p, 0)))
        assert rho_square == (((p, 0), (0, 0)), ((0, 0), (p, 0)))
        print('original E3 coefficient ports', p, 'delta_square', delta_square[0][0],
              'sign_compatible_square', rho_square[0][0],
              'rho_residue', rho, 'norm_rho_mod_p', mul(rho, sigma(rho, p), p))
    print('PASS_AUTHOR_SIDE_CM_SIGN_TWIST_77_PRIMES / NOT_NATIVE_H0B0')

if __name__ == '__main__':
    main()
