"""Exact arithmetic for the smaller C46 graph correspondence. Requires SymPy."""
from sympy import Rational, expand, invert, rem, symbols

t = symbols("t")
f = t**8 + 5*t**6 + 245*t**2 + 2401
a = -49 - 70*t + 35*t**2 - 12*t**3 + 4*t**4
b = 196 - 35*t + 35*t**2 - 11*t**3 + t**4
reduce_mod = lambda p: rem(expand(p), f, t)
tau = lambda p: p.subs(t, -t)

def multiply(left, right):
    x, y = left
    z, w = right
    return reduce_mod(x*z - y*tau(w)), reduce_mod(x*w + y*tau(z))

assert expand(a*tau(a) + b*tau(b) - 17*f) == 0
trace = expand(a+tau(a))
assert trace == 2*(4*t**4+35*t**2-49)
trace_inverse = invert(trace, f, t)
q = reduce_mod(b*invert(tau(a), f, t))
assert reduce_mod(q*tau(q)) == -1
half = Rational(1,2)
T = (a,b)
Tstar = (tau(a),-b)
assert multiply(T,Tstar) == multiply(Tstar,T) == (0,0)
assert multiply(T,T) == (reduce_mod(trace*a),reduce_mod(trace*b))
assert multiply((t,0*t),T) != multiply(Tstar,(t,0*t))
for sign in (1,-1):
    projection = (half,sign*q/2)
    assert multiply(projection,projection) == projection
    assert multiply((1+0*t,sign*q),(a,0*t)) == (a,sign*b)
    assert multiply((t,0*t),projection) == multiply((half,-sign*q/2),(t,0*t))

rho = reduce_mod(7*invert(t, f, t))
rosati_residue = reduce_mod(q + q.subs(t, -rho))
assert rosati_residue.coeff(t,0) == -Rational(389,23207)
trace_sigma = reduce_mod(b*trace_inverse)
assert reduce_mod(trace_sigma + trace_sigma.subs(t,-rho)).coeff(t,0) == Rational(1075,7234)
weights = [abs(a.coeff(t,j))+abs(b.coeff(t,j)) for j in range(5)]
bidegree = sum(weights), sum(n*7**j for j,n in enumerate(weights))
assert weights == [245,105,70,23,5] and bidegree == (448,24304)
print("norm = 17*f; trace =", trace)
print("weights and bidegree of both effective parts:", weights, bidegree)
print("constant term of q(t) + q(-7/t):", rosati_residue.coeff(t,0))
