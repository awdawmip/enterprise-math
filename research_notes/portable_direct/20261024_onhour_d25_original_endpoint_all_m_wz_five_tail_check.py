"""D25 full original endpoint: symbolic all-(m,n) WZ and exact Fraction checks.
Author-side reproducibility only: not a native benchmark or admitted Source Result.
Python3 standard library + SymPy. No network, floating arithmetic or service claims.
"""
from fractions import Fraction
from math import factorial
import sympy as s

m,n=s.symbols("m n", integer=True, nonnegative=True)
P=(27*n**4+(324*m+180)*n**3+(1836*m**2+1746*m+429)*n**2
  +(4320*m**3+5940*m**2+2706*m+412)*n
  +3456*m**4+6336*m**3+4128*m**2+1184*m+128)
D=(n+2*m+1)*(n+4*m+1)*(n+4*m+2)*(n+4*m+3)*(6*n+12*m+1)
g=4*n*P/(9*D)

C=(16*(3*m+1)*(3*m+2)*(6*m+1)*(6*m+5)
   *(4*m+2*n+1)*(4*m+2*n+3)*(12*m+6*n+13)
   /(81*(2*m+n+1)*(2*m+n+2)*(4*m+n+1)*(4*m+n+2)
      *(4*m+n+3)*(4*m+n+4)*(12*m+6*n+1)))
num=(3*n+1)*(3*n+2)*(4*m+2*n+1)*(12*m+6*n+7)
den=36*(n+1)*(2*m+n+1)*(4*m+n+1)*(12*m+6*n+1)
r=num/den
assert s.cancel(r*g.subs(n,n+1)-g-(C-1))==0
assert all(coeff>0 for coeff in s.Poly(s.expand(den-2*num),m,n).coeffs())
print("PASS: exact symbolic bivariate WZ and geometric ratio<1/2")

def terms(mm,N):
    pref=Fraction(factorial(6*mm),3**(6*mm)*factorial(2*mm)**3)
    value=Fraction(1)
    result=[]
    for j in range(N+1):
        result.append(pref*(6*j+12*mm+1)*value)
        if j<N:
            value*=Fraction((4*mm+2*j+1)*(3*j+1)*(3*j+2),
                            36*(j+1)*(2*mm+j+1)*(4*mm+j+1))
    return result

def gn(mm,j):
    return Fraction(4*j*int(P.subs({m:mm,n:j})),
                    9*int(D.subs({m:mm,n:j})))

for mm in range(15):
    T=terms(mm,4*mm+5)
    Tp=terms(mm+1,4*mm+5)
    assert gn(mm,0)==0
    for j in range(4*mm+5):
        assert Tp[j]-T[j]==T[j+1]*gn(mm,j+1)-T[j]*gn(mm,j)
    S=sum(T[:4*mm+1])
    Snext=sum(Tp[:4*mm+5])
    delta=T[4*mm+1]*gn(mm,4*mm+1)+sum(Tp[4*mm+1:4*mm+5])
    assert Snext-S==delta and delta>0
print("PASS: exact original summand and moving-terminal five-tail m=0..14")
