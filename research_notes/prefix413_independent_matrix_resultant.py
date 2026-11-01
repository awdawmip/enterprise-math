#!/usr/bin/env python3
"""Independent algebraic check from the original 5x3 complex Port matrix.
Requires sympy. Does not call the rational interval checker.
"""
from sympy import I, Matrix, symbols, Rational as R, simplify, expand, resultant, factor, Poly, sqrt
x,y,z,t=symbols('x y z t',real=True)
M=Matrix([
[4,4,0],
[0,-4,4],
[-5+3*I,0,-3+I],
[-2-2*I,4+4*I,2+2*I],
[-2,0,5+2*I]])
u,v=symbols('u v')
a=M[:3,:].inv()*Matrix([1,u,v])
port4=simplify((M[3,:]*a)[0])
port5=simplify((M[4,:]*a)[0])
assert simplify(port4-((5+9*I)/2+(3+7*I)*u/2+4*I*v))==0
assert simplify(port5-((22+15*I)*(1+u)/8+(5+9*I)*v/4))==0

def norm2(q): return expand(q* q.conjugate())
for sigma,expected_k,expected_i4 in [
(1,23*x+R(61,8)*y+R(53,8)*(x*x+y*y),37+48*x+8*y+16*(x*x+y*y)),
(-1,R(61,8)*x-23*y+R(53,8)*(x*x+y*y),45+24*x-48*y+16*(x*x+y*y))]:
    assert simplify(norm2(port5.subs({u:sigma*I,v:x+I*y}))-R(709,32)-expected_k)==0
    assert simplify(norm2(port4.subs({u:sigma*I,v:x+I*y}))-expected_i4)==0

B=R(1,1000000); E=R(53,8); A2=R(37577,64)
C=z-E*B
corner=expand(((z+t)**2)/4+(R(45,368))**2*(t-z)**2-t)
assert simplify(corner-(35881*t*t+63662*t*z-135424*t+35881*z*z)/135424)==0
# Equate two exact maxima with sqrt and eliminate their auxiliary variables.
W=expand(A2*((141*z+43*t)/23-16*B)-1165*C)
squared=expand(W*W-182**2*(A2*B-C*C))
resultant_pol=Poly(resultant(corner,squared,t),z).clear_denoms()[1]
expected=(411370922419157000000000000000000000000*z**4
+3406648973825365305852000000000000000000*z**3
+7207920358822113492588156702000000000000*z**2
-15929217691721140762689459588000000*z
-23522344829723509499221428663222123)
quotient=simplify(resultant_pol.as_expr()/expected)
assert quotient.is_number and quotient>0
assert simplify(resultant_pol.as_expr()-quotient*expected)==0
assert expected.subs(z,R(1806822,10**9))<0
assert expected.subs(z,R(1806823,10**9))>0
print('PASS_PREFIX413_INDEPENDENT_ORIGINAL_MATRIX_AND_QUARTIC_RESULTANT')
print('resultant proportionality:',quotient)
print('port4:',port4)
print('port5:',port5)
