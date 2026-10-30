"""Finite symbolic checks supporting the exact rational pole proof; not a native experiment."""
import sympy as s
from sympy.concrete.gosper import gosper_sum
k=s.symbols('k')
N=(2*k+1)*(3*k+1)*(3*k+2)
D=(2*k-1)*(3*k-2)*(3*k-1)
q=N/(36*(k+1)**3)
assert s.cancel(D.subs(k,k+1)-N)==0
assert s.cancel(q*(k+1)**3/D.subs(k,k+1)-s.Rational(1,36))==0
assert s.expand(D).coeff(k,3)==18
assert D.subs(k,0)==-2 and D.subs(k,1)==2
assert s.Rational(36*6*18,18)==216
F1=36
F2=s.Rational(36*7*D.subs(k,1)+36*F1,D.subs(k,1))
assert F2==900 and F2-F1==864
# The formal asymptotic slope is -216, contradicting the exact first two values.
assert F2-F1 != -216
# Independent decision procedure: conventional hypergeometric Gosper solver.
n=s.symbols('n', integer=True, nonnegative=True)
a=(6*n+1)*s.rf(s.Rational(1,2),n)*s.rf(s.Rational(1,3),n)*s.rf(s.Rational(2,3),n)/(2**n*s.factorial(n)**3)
assert gosper_sum(a,n) is None
print('SLOPE_REQUIRED -216; F(1)=36; F(2)=900; FINITE_DIFFERENCE=864')
print('PASS_GOSPER_SINGLE_TERM_RATIONAL_OBSTRUCTION_CHECK')
