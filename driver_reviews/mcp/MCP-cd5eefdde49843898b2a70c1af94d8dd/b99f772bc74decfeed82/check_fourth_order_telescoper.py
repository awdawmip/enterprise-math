#!/usr/bin/env python3
"""Exact rational/symbolic OLD-R certificate check; no prime computations."""
import sympy as s

n = s.symbols("n")
A = (n - s.Rational(1, 6)) * (n - s.Rational(1, 3))
Ap = A.subs(n, n + 1)
C = (n + s.Rational(1, 6)) * (n + s.Rational(1, 3))
X = (n - s.Rational(5, 6)) * (n - s.Rational(2, 3))
Y = (n - s.Rational(11, 6)) * (n - s.Rational(5, 3))
P = 126 * n**2 - 117 * n + 41
Pn = P.subs(n, n + 1)

assert s.expand(2 * (n - 1)**2 + 5 * A - P / 18) == 0
e_ratio = s.factor(
    ((2 * n**2 / A.subs(n, n + 1)) + 5)
    * (2 * (n - 1)**2 / A)
    / ((2 * (n - 1)**2 / A) + 5)
)
assert s.factor(e_ratio - 2 * (n - 1)**2 * Pn / (Ap * P)) == 0

a = (6*n + 5) * (3*n + 2)
c = (6*n + 1) * (3*n + 1)
x = (6*n - 5) * (3*n - 2)
y = (6*n - 11) * (3*n - 5)
alpha = 1296 * n**2 * (n+1)**2 * a * P
beta = -72 * n**2 * c * (a*P + 18*(n-1)**2 * Pn)
gamma = c*x * (a*P + 72*(n-1)**2 * Pn)
delta = -c*x*y*Pn

un1, un, unm1, unm2 = s.symbols("un1 un unm1 unm2")
en = un - X/n**2 * unm1 + X*Y/(4*n**2*(n-1)**2) * unm2
en1 = un1 - C/(n+1)**2 * un + C*X/(4*(n+1)**2*n**2) * unm1
rec3 = (n+1)**2 * Ap*P * en1 - (n-1)**2 * C*Pn * en
rec4 = alpha*un1 + beta*un + gamma*unm1 + delta*unm2
assert s.factor(4*n**2 * 18**3 * rec3 - rec4) == 0

terminal = s.Rational(-1, 6)
assert alpha.subs(n, terminal) == 9600
assert all(q.subs(n, terminal) == 0 for q in (beta, gamma, delta))
assert P.subs(n, terminal) == 64

def B(i):
    return (s.Rational(1, 2)**i * s.rf(s.Rational(1, 6), i)
            * s.rf(s.Rational(1, 3), i) / s.factorial(i)**2)

def D(r):
    return (s.Integer(2)**(r-1) * s.factorial(r-1)**2
            / (18*s.rf(s.Rational(5, 6), r)*s.rf(s.Rational(2, 3), r)))

def H(j):
    return s.factor(sum((1 + 6*(j-r))*D(r) for r in range(1, j+1)))

def R(j):
    if j == -1:
        return s.Integer(0)
    return s.factor(sum(2*B(i)*H(i) for i in range(1, j+1)))

assert [H(j) for j in range(3)] == [0, s.Rational(1, 10), s.Rational(421, 550)]
assert [R(j) for j in range(4)] == [
    0, s.Rational(1, 180), s.Rational(4927, 356400),
    s.Rational(7604467, 392610240)]

for j in range(2, 10):
    ej = H(j) - 2*H(j-1) + H(j-2)
    assert s.factor(ej - D(j) - 5*D(j-1)) == 0
    ej1 = H(j+1) - 2*H(j) + H(j-1)
    assert s.factor((Ap*P).subs(n, j)*ej1
                    - (2*(n-1)**2 * Pn).subs(n, j)*ej) == 0
    us = [R(k)-R(k-1) for k in (j+1, j, j-1, j-2)]
    assert s.factor(sum(q.subs(n, j)*u for q, u in zip(
        (alpha, beta, gamma, delta), us))) == 0

print("PASS: symbolic coefficient/terminal identities and exact rational finite boundaries.")
print("No prime calculations, modular comparisons, or LIFT closure performed.")
