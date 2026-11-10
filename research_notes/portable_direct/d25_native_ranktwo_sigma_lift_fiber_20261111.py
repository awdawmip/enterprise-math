"""D25 author-side exact F*sigma(F)=p I lift-fiber checker.

This computes a conditional native-acceptance constraint in a fixed rank-2
basis over (Z/p²)[T]/(T²-2). No H0/B0 or [X]U evaluation is performed.
"""


def plus(x, y, m):
    return ((x[0] + y[0]) % m, (x[1] + y[1]) % m)


def times(x, y, m):
    return ((x[0] * y[0] + 2 * x[1] * y[1]) % m,
            (x[0] * y[1] + x[1] * y[0]) % m)


def sigma(x, m):
    return (x[0] % m, -x[1] % m)


def matmul(a, b, m):
    return [[plus(times(a[i][0], b[0][j], m),
                  times(a[i][1], b[1][j], m), m)
             for j in range(2)] for i in range(2)]


def sigmamat(a, m):
    return [[sigma(c, m) for c in row] for row in a]


def lifted_F(p, b, d):
    m = p * p
    return [[times((-p, 0), sigma(d, m), m),
             plus((1, 0), times((p, 0), b, m), m)],
            [(p, 0), times((p, 0), d, m)]]


def is_q_frobenius(F, p, qsign=1):
    m = p * p
    want = [[((qsign * p) % m, 0), (0, 0)],
            [(0, 0), ((qsign * p) % m, 0)]]
    return matmul(F, sigmamat(F, m), m) == want


def test():
    # Complete fixed-basis model fiber at p=5.
    p = 5
    vals = [(a, b) for a in range(p) for b in range(p)]
    matrices = set()
    for b in vals:
        for d in vals:
            F = lifted_F(p, b, d)
            assert is_q_frobenius(F, p)
            assert [[tuple(x % p for x in cell) for cell in row] for row in F] == \
                [[(0, 0), (1, 0)], [(0, 0), (0, 0)]]
            matrices.add(tuple(cell for row in F for cell in row))
    assert len(matrices) == p ** 4

    # Priority p=373: distinct model matrices share exactly the same square.
    p = 373
    F0 = lifted_F(p, (0, 0), (0, 0))
    F1 = lifted_F(p, (0, 1), (1, 1))
    assert F0 != F1 and is_q_frobenius(F0, p) and is_q_frobenius(F1, p)
    assert not is_q_frobenius([[(0, 0), (1, 0)],
                               [(-p, 0), (0, 0)]], p)
    print({"p5_distinct_fixed_basis_lifts": len(matrices),
           "p373_modulus": p * p,
           "p373_model0": F0,
           "p373_model1": F1,
           "same_q_frobenius": True,
           "native_h0b0_run": False})


if __name__ == "__main__":
    test()
