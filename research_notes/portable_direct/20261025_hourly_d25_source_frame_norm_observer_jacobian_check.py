"""Exact finite-ring author checks for D25 fixed-frame norm-observer Jacobian criterion.

This checks conditional quadratic coefficient algebra; it does NOT execute the
original CM/divided-power experiment or supply independent mathematical review.
"""

def norm(pair, modulus):
    a, b = pair
    return (a*a - 2*b*b) % modulus


def cayley_beta(alpha, t, modulus):
    a, b = alpha
    inverse = pow((1 - 2*t*t) % modulus, -1, modulus)
    odd = (2*t*inverse) % modulus
    even = ((1 + 2*t*t)*inverse) % modulus
    return ((a*even + 2*b*odd) % modulus,
            (a*odd + b*even) % modulus)


def observe(kind, pair, modulus):
    a, b = pair
    if kind == 'even':
        return a % modulus
    if kind == 'odd':
        return b % modulus
    if kind == 'nonlinear':
        return (a + b*b) % modulus
    raise ValueError(kind)


def derivative(kind, alpha, p):
    a, b = [v % p for v in alpha]
    return {'even': 4*b, 'odd': 2*a,
            'nonlinear': 4*b*(1 + a)}[kind] % p


def reconstruct_x(alpha, target, kind, p, r):
    modulus = p**r
    d = derivative(kind, alpha, p)
    assert d != 0
    inverse_d = pow(d, -1, p)
    x = 0
    for k in range(1, r):
        pk = p**k
        value = observe(kind, cayley_beta(alpha, x, modulus), modulus)
        difference = (target - value) % modulus
        assert difference % pk == 0
        digit = ((difference // pk) * inverse_d) % p
        x += pk*digit
    return x % modulus


def run():
    cases = [(13, 2), (13, 3), (19, 2), (19, 3), (373, 2)]
    for p, r in cases:
        modulus = p**r
        alpha = tuple(v % modulus for v in (
            (92060, 21788) if p == 373 else (2, 1)))
        assert norm(alpha, p) != 0
        samples = p**(r-1)
        kinds = [kind for kind in ('even', 'odd', 'nonlinear')
                 if derivative(kind, alpha, p) != 0]

        # Entire fixed-first-digit frame: Jacobian criterion for (norm, F).
        for kind in kinds:
            images = set()
            for i in range(samples):
                aa = (alpha[0] % p + p*i) % modulus
                for j in range(samples):
                    bb = (alpha[1] % p + p*j) % modulus
                    pair = aa, bb
                    images.add((norm(pair, modulus),
                                observe(kind, pair, modulus)))
            assert len(images) == samples*samples, (
                p, r, kind, len(images))

        # Five representative Cayley fiber points: exact digit inversion.
        for k in sorted({0, 1, 2, samples // 2, samples-1}):
            t = p*k
            beta = cayley_beta(alpha, t, modulus)
            assert norm(beta, modulus) == norm(alpha, modulus)
            for kind in kinds:
                target = observe(kind, beta, modulus)
                assert reconstruct_x(alpha, target, kind, p, r) == t

        # Construct the tangent-blind linear observer, test top digit collision.
        a0, b0 = alpha[0] % p, alpha[1] % p

        def blind(pair):
            return (a0*pair[0] - 2*b0*pair[1]) % modulus

        other = cayley_beta(alpha, p**(r-1), modulus)
        assert other != alpha
        assert norm(other, modulus) == norm(alpha, modulus)
        assert blind(other) == blind(alpha)
        print('PASS', 'p=', p, 'r=', r,
              'local-frame points=', samples*samples,
              'transverse observers=', ','.join(kinds),
              'blind-last-digit=YES')

    p = 373
    modulus = p*p
    alpha = (92060, 21788)
    beta = cayley_beta(alpha, p, modulus)
    assert beta == (43570, 107951)
    assert norm(alpha, modulus) == norm(beta, modulus) == 122102
    assert reconstruct_x(alpha, beta[0], 'even', p, 2) == p
    assert derivative('even', alpha, p) == 243
    assert derivative('odd', alpha, p) == 231
    print('PASS p373 ordinary-Hesse fixed-frame witness:',
          'norm=122102', 'even-J=243', 'odd-J=231', 'recovered t=373')


if __name__ == '__main__':
    run()
