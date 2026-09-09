"""Exact exploratory linear reduction of the full six-coefficient L(6O) pencil.

The integer derivation is 2 delta. No previous enumeration is executed.
SymPy 1.14.0 is a symbolic discovery aid; final certificates are checked separately.
"""
import json
import sympy as s

R,t,k=s.symbols('R t k')
a,b,c,d,e,f=s.symbols('a b c d e f')
P=R**3-3*R
F=(R+2)*t
G=a*R**3+b*R**2+c*R+d+(e*R+f)*t

def red(expr):
    return s.rem(s.Poly(s.expand(expr),t),s.Poly(t*t-P,t)).as_expr().expand()

def D(expr):
    return red(2*t*s.diff(expr,R)+3*(R*R-1)*s.diff(expr,t))

N=red(F*D(G)-G*D(F))
atQ=s.rem(s.Poly(N.subs(t,-k),R),s.Poly(R**3-3*R-k*k,R)).as_expr().expand()
coeffs=s.Poly(atQ,R).all_coeffs()
M,rhs=s.linear_eq_to_matrix(coeffs,[a,b,c,d,e,f])
sol=s.linsolve(coeffs,[b,c,d])
out={'sympy_version':s.__version__,'G':str(G),'F':str(F),'integer_derivative_numerator':str(N),'critical_remainder':str(atQ),'critical_matrix_columns':['a','b','c','d','e','f'],'critical_matrix':[[str(x) for x in row] for row in M.tolist()],'solution_for_b_c_d':str(sol),'minor_b_c_d':str(s.factor(M[:,1:4].det()))}
print(json.dumps(out,indent=2))
