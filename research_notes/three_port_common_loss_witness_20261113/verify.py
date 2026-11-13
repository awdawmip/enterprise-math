"""Exact checks on the vacuum/single-excitation three-qubit model. Run with python -B."""
from fractions import Fraction as F


def zeros(n):
    return [[F(0) for _ in range(n)] for _ in range(n)]


def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return list(map(list, zip(*a)))


def multiply(a, b):
    cols = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in cols] for row in a]


def retained(t):
    a = identity(8)
    for i in (4, 2, 1):
        for j in (4, 2, 1):
            a[i][j] += (t - 1) / 3
    return a


def apply(rho, t):
    a = retained(t)
    out = multiply(multiply(a, rho), transpose(a))
    # A1=v<chi|*sqrt(1-t^2); contract its exact Gram factor.
    out[0][0] += (1 - t*t) / 3 * sum(rho[i][j] for i in (4, 2, 1) for j in (4, 2, 1))
    return out


def inspect(rho, z):
    assert sum(rho[i][i] for i in range(8)) == 1
    sigma = [[sum(rho[2*i+k][2*j+k] for k in (0, 1)) for j in range(4)] for i in range(4)]
    pt = [[sigma[2*(i//2)+j%2][2*(j//2)+i%2] for j in range(4)] for i in range(4)]
    vector = [1, 0, 0, 2]
    value = sum(vector[i]*pt[i][j]*vector[j] for i in range(4) for j in range(4)) / 5
    assert value == -2*(1-z)*(2+z) / 45
    assert (value < 0) == (z < 1)
    return value


def main():
    # Symbolic witness identity: 45 times the expectation is a polynomial
    # of degree at most two. Check it at three points by exact channel computation.
    initial = zeros(8)
    initial[4][4] = F(1)
    for t in (F(0), F(1, 2), F(1)):
        inspect(apply(initial, t), t)
    assert inspect(apply(initial, F(1, 2)), F(1, 2)) == -F(1, 18)
    assert inspect(apply(initial, F(0)), F(0)) == -F(4, 45)
    assert apply(initial, F(1)) == initial

    parameters = [F(a, b) for b in range(1, 9) for a in range(b+1)]
    parameters = sorted(set(parameters))
    for t in parameters:
        a = retained(t)
        gram = multiply(transpose(a), a)
        for i in (4, 2, 1):
            for j in (4, 2, 1):
                gram[i][j] += (1-t*t)/3
        assert gram == identity(8)
        rho = initial
        for n in range(1, 6):
            rho = apply(rho, t)
            assert rho == apply(initial, t**n)
            inspect(rho, t**n)
    print(f"PASS: exact degree-two witness identity; {len(parameters)} Kraus completeness checks; "
          f"{5*len(parameters)} repeated-channel, partial-trace and witness checks.")


if __name__ == "__main__":
    main()
