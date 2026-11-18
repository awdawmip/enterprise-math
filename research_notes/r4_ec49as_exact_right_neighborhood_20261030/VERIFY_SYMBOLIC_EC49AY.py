"""EC49AY optional symbolic identity check. Executed with SymPy 1.14.0."""
import sympy as S
eta, r, t = S.symbols('eta r t')
a = 344*(1-4*eta**2)
b = 2436*eta**2+1568*eta-1201
c = 2060*eta**2-5096*eta+1769
d = 27-10*eta
f = 8+16*eta
h = S.Rational(77,688)+(674*eta-175)/16512
Tstar = (d-4*r)/f
G = (4156*eta**2-3936*eta+1121-344*(1-2*eta)*r)/(16512*(1+2*eta))
D=S.expand(b*b-4*a*c)
assert S.expand(D-(17272336*eta**4-20409088*eta**3+3509368*eta**2+3245760*eta-991743))==0
LHS = a*t*t+b*t+c + 2064*G*(d-f*t) - a*(t-Tstar)**2
P,den=S.fraction(S.cancel(LHS))
assert S.expand(P-86*(2*eta-1)*(26*eta+r*r-19))==0
assert S.expand(den-(2*eta+1))==0
assert S.simplify((h+G).subs({eta:S.Rational(2,5),r:S.sqrt(S.Rational(43,5))})-(S.Rational(15451,123840)-S.sqrt(215)/2160))==0
print('PASS: exact polynomial identity modulo r^2=19-26*eta; root polynomial and eta=2/5 radical.')
