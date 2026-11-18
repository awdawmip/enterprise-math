"""Exact checks for the C46 rank-one correspondence. Python 3 and SymPy."""
from collections import Counter
from sympy import Matrix, Poly, Rational, ZZ, expand, factor, gcd, invert, rem, symbols

s, t = symbols("s t")
h = s**4 + 5*s**3 + 245*s + 2401
f = h.subs(s, t**2)
D = 8*s**2 + 168*s + 882
U = -13*s**3 - 372*s**2 - 616*s + 3773
V = 2*s**3 + 74*s**2 + 1708*s + 16464
assert Poly(h, s, domain=ZZ).is_irreducible
assert Poly(f, t, domain=ZZ).is_irreducible
quotient, remainder = divmod(Poly(expand(U**2 + V**2 - s*D**2), s), Poly(h, s))
assert remainder.is_zero and gcd(V, h) == 1
print("norm identity quotient:", factor(quotient.as_expr()))
q = rem(((U + t*D)*invert(V, h, s)).subs(s, t**2), f, t)
red = lambda x: rem(expand(x), f, t)
tau = lambda x: x.subs(t, -t)
assert red(q*tau(q)) == -1

# End^0(P) crossed-product coordinates x + y sigma.
def product(a, b):
    x, y = a
    z, w = b
    return red(x*z - y*tau(w)), red(x*w + y*tau(z))

half = Rational(1, 2)
Q = (0*t, q)
positive = (half, q/2)
negative = (half, -q/2)
frobenius = (t, 0*t)
assert product(Q, Q) == (1, 0)
for e in (positive, negative):
    assert product(e, e) == e
assert product(positive, negative) == product(negative, positive) == (0, 0)
assert product(frobenius, positive) == product(negative, frobenius)
print("rationally normalized q(t):", q)
dual_t = red(7*invert(t, f, t))
rosati_difference = red(q + q.subs(t, -dual_t))
assert rosati_difference.coeff(t, 0) == -Rational(865765, 47654027)
print("constant term of q(t) + q(-7/t):", rosati_difference.coeff(t, 0))

# Absolute multiplicity of each graph type in the positive part of K.
v = Poly(V.subs(s, t*t), t)
w = Poly((U + t*D).subs(s, t*t), t)
weights = [abs(v.nth(j)) + abs(w.nth(j)) for j in range(7)]
source, target = sum(weights), sum(m*7**j for j,m in enumerate(weights))
assert target == 3167948
print("weights by Frobenius degree:", weights)
print("bidegree of each effective part:", source, target)

# Degree-four carriers for exactly the same two image surfaces.
A = 6174 + 5012*t - 5103*t**2 + 670*t**3 - 1843*t**4
B = -90307 + 35*t - 5117*t**2 - 93*t**3 + 126*t**4
assert expand(A*tau(A) + B*tau(B)) == expand(3412525*f)
assert red(q*tau(A)) == B
for sign in (1, -1):
    assert product(Q, (A, sign*B)) == (sign*A, B)
columns = [red(q*(-t)**j) for j in range(5)] + [-t**j for j in range(5)]
assert Matrix(8, 10, lambda k, j: columns[j].coeff(t, k)).rank() == 8
weights4 = [abs(A.coeff(t, j)) + abs(B.coeff(t, j)) for j in range(5)]
assert (sum(weights4), sum(x*7**j for j, x in enumerate(weights4))) == (114480, 5621868)
print("degree-four image carrier weights:", weights4)

# a + b*i is encoded as a+7b, i^2 = -1 in F49.
F49 = range(49)
def add(x, y):
    return (x%7 + y%7)%7 + 7*((x//7 + y//7)%7)

def neg(x):
    return (-x%7)%7 + 7*((-(x//7))%7)

def mul(x, y):
    a, b = x%7, x//7
    c, d = y%7, y//7
    return (a*c - b*d)%7 + 7*((a*d+b*c)%7)

def frob(x):
    return x%7 + 7*((-(x//7))%7)

def sigma(p):
    x,y,w = p
    return x,neg(y),mul(7,w)

def frob_p(p):
    return tuple(frob(x) for x in p)

squares = {v: [u for u in F49 if mul(u,u)==v] for v in F49}
affine = []
for x in F49:
    x2 = mul(x,x)
    for y in squares[add(add(mul(x2,x),mul(1,x2)),1)]:
        for w0 in squares[mul(y,add(x2,2))]:
            affine.append((x,y,w0))
points = set(affine)
assert all(sigma(p) in points and frob_p(p) in points for p in points)
assert all(frob_p(sigma(p)) == sigma(sigma(sigma(frob_p(p)))) for p in points)
print("affine C46 points and point counts grouped by sigma orbit length:",
      len(points), dict(Counter(1 if sigma(p)==p else 2 if sigma(sigma(p))==p else 4 for p in points)))
# At Z0=0 the projective equations imply Z1=Z2=W=0, so count one extra point.
assert 1 + len(points) == 65

# y^2 = x^5 +(5+6i)x^4 +(1+3i)x^3 + 3i*x^2 + 4*x + (2+4i)
c7 = [1,5+6*7,1+3*7,3*7,4,2+4*7]
count = 1
for x in F49:
    v0 = 0
    for c in c7:
        v0 = add(mul(v0,x),c)
    count += len(squares[v0])
assert count == 55
print("C7 over F49:", count)
