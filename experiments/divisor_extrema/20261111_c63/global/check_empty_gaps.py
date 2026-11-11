"""Exact bivariate polynomial check for the unrestricted high-inventory lemma."""
from sympy import Poly, Rational, cancel, symbols

r,c,x,t = symbols('r c x t')
k = 2*r+1
rho = (k+4*c)/(k+c)
tau = 28*(k+4*c)*(k+4*c-1)/((4*k+c)*(k+c-1))
slope = tau*(rho-1)/(tau+rho)**2
gap_ratio = 16*(3*r+3)*(3*r+2)*(3*r+1)/((k+c)*(k+c-1))
num = cancel(100*r**2*slope-Rational(21,10)*gap_ratio).as_numer_denom()[0]
shifted = Poly(num.subs(c,r+2+x).subs(r,64+t),x,t)
coeffs = shifted.coeffs()
assert len(coeffs)==52 and min(coeffs)==168000 and shifted.eval({x:0,t:0})>0
print('Validated 52 positive nonzero coefficients; smallest =',min(coeffs))
