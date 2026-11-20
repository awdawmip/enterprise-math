"""Exact rational-function certificate for R5 even-m primitive-fourth-root pole."""
import sympy as sp
z, I = sp.symbols('z'), sp.I
S0 = (214, 215, 216, 217, 218)
S1 = (214, 216, 217, 218, 219, 220, 221)
S2 = (215, 216, 217, 218, 219, 220, 221)
def H(S):
    value = z / (1-z)
    for p in S:
        value /= 1-z*I**p
    return value
def M(a, b):
    return (1-a*b*z*z)/((1-a*z)*(1-b*z)*(1-a*b*z))
def pair_overlap(a, b, c):
    tri = (1-a*b*c*z**3)/((1-a*b*c*z*z)*(1-a*z)*(1-b*z)*(1-c*z))
    return M(b,c)/(1-a*z)+M(a,c)/(1-b*z)+M(a,b)/(1-c*z)-tri
h = z / ((1-z)*(1-z*z)*(1-I*z)) * (
    sp.Rational(1,2)*pair_overlap(-1,-I,1)
    + (1-I)/4*pair_overlap(-1,-I,I)
    + (1+I)/4*pair_overlap(-1,-I,-I))
h0,h1,h2 = (H(S) for S in (S0,S1,S2))
d = -h0 * sum(p*z*I**p/(1-z*I**p) for p in S0)
d += 220*(1-I)*h1 + 220*h2-440*h
even = sp.cancel((d+d.subs(z,-z))/2)
expected = ((656-2*I)*z*z+(872+440*I)*z**4+(216+2*I)*z**6)/(1-z**4)**3
assert sp.cancel(even-expected) == 0
print('PASS: symbolic rational identity for every positive even m')
print('D_even numerator = (656-2i)z^2+(872+440i)z^4+(216+2i)z^6')
