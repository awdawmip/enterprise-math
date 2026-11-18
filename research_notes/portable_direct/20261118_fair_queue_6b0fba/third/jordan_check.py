"""Exact certificates for the finite moments and the classical height bound."""
from fractions import Fraction
from math import factorial

import sympy as sp

ORDER = 8
X = sp.Symbol("X")


def moment_polynomials():
    elementary = [1]
    moments = [0]
    for n in range(1, ORDER + 1):
        elementary.append(sp.prod(X - j*j for j in range(1, n + 1)) / factorial(2*n + 1))
        value = (-1)**(n-1) * n * elementary[n]
        for j in range(1, n):
            value += (-1)**(j-1) * elementary[j] * moments[n-j]
        moments.append(sp.expand(value))
    return moments


def phase_coefficients():
    beta = [0, sp.Rational(1, 6)]
    for n in range(2, ORDER + 1):
        beta.append(sp.Rational(2, 2*n + 1) * sum(beta[j] * beta[n-j] for j in range(1, n)))
    inverse = [0, sp.Integer(1)]
    for n in range(1, ORDER):
        inverse.append(inverse[n] * sp.Rational(n*n, (n+1)*(4*n+2)))
    powers = [[int(j == 0) for j in range(ORDER + 1)]]
    for _ in range(ORDER):
        powers.append([sum(inverse[j]*powers[-1][k-j] for j in range(1, k+1))
                       for k in range(ORDER + 1)])
    return beta, powers


def jordan(k, d):
    return int(sum(sp.mobius(d//e) * e**k for e in sp.divisors(d)))


def heights(poly, n):
    A = [Fraction(poly.coeff(X, r)) for r in range(n+1)]
    for height in range(1, 500):
        upper = Fraction(11, 6) * sum(
            abs(A[r] / A[n]) * Fraction(40, height*height)**(n-r) for r in range(1, n))
        if upper < 1:
            return height
    raise AssertionError('height search range exhausted')


def check():
    polynomials = moment_polynomials()
    beta, powers = phase_coefficients()
    primitive_by_divisors = 0
    for n in range(1, ORDER+1):
        poly = polynomials[n]
        for r in range(1, n+1):
            assert poly.coeff(X, r) == sp.Rational(n, r) * beta[r] * powers[r][n] > 0
        assert poly.subs(X, 1) == 0
        assert poly.coeff(X,n) == (-1)**(n+1) * 2**(2*n-1)*sp.bernoulli(2*n)/factorial(2*n)
        for d in range(2, 43):
            inv = sum(sp.mobius(d//m)*poly.subs(X, m*m) for m in sp.divisors(d))
            assert inv == sum(poly.coeff(X,r)*jordan(2*r,d) for r in range(1,n+1))
            primitive_by_divisors += 1
    matrix_traces = 0
    for M in range(2, 15):
        # Dirichlet Green entries from the explicit inverse of the tridiagonal
        # matrix. Verify the inverse before using its trace powers.
        green = sp.Matrix(M-1, M-1, lambda i,j:
            sp.Rational((min(i,j)+1)*(M-max(i,j)-1),M))
        lap = sp.Matrix(M-1, M-1, lambda i,j: 2 if i==j else -1 if abs(i-j)==1 else 0)
        assert lap*green == sp.eye(M-1)
        power = sp.eye(M-1)
        for n in range(1, ORDER+1):
            power = power * green
            assert sp.trace(power) == polynomials[n].subs(X,M*M)
            matrix_traces += 1
    bounds = [heights(polynomials[n],n) for n in range(2,ORDER+1)]
    assert bounds == [14,16,18,20,22,24,25]
    for n in (4,5,6):
        print(f"Z_{n}(M) =", sp.together(polynomials[n]))
    print(f"matrix trace checks={matrix_traces}, primitive inversion checks={primitive_by_divisors}")
    print("s=2,...,8 first integer heights for the stated sufficient inequality:", bounds)


if __name__ == '__main__':
    check()
