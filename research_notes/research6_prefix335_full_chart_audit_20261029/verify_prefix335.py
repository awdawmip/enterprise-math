#!/usr/bin/env python3
"""Exact, author-side S7-3 five-port algebraic-fiber boundary audit.
Uses source-labelled ordered BRC pairs before any amplitude quotient.
Python 3 + SymPy; no floating-point comparisons.
"""
import json
from sympy import (I, Matrix, Poly, Rational, S, conjugate, degree, diff, expand,
                   gcd, invert, rem, resultant, simplify, subresultants, symbols)

x, y, s, t = symbols('x y s t')
A = Matrix([
    [4, 4, 0], [0, -4, 4], [-5+3*I, 0, -3+I],
    [-2-2*I, 4+4*I, 2+2*I], [-2, 0, 5+2*I],
])
b = [32, 16, 10, 104, 29]
H = ((4009889320-1781681608*I)*y**4
     +(-16309089106+5648135613*I)*y**3
     +(32330408686-7256734999*I)*y**2
     +(-28275431456-362195540*I)*y
     +7718155900+2476622526*I)
T = (29758587129448225*t**4-255711023882111440*t**3
     +1277050567880509143*t**2-1191970997377517618*t
     +300837526733367626)
C = A.conjugate()[:3, :]
assert simplify(C.det()) != 0

def eliminate_first_three(z):
    f = A*z
    d = expand(f[0]*f[1]*f[2])
    W = C.inv()*Matrix([b[j]*f[(j+1)%3]*f[(j+2)%3] for j in range(3)])
    P = expand(f[3]*A.conjugate().row(3).dot(W)-b[3]*d)
    R = expand(f[4]*A.conjugate().row(4).dot(W)-b[4]*d)
    return f, d, W, P, R

f, d, W, P, R = eliminate_first_three(Matrix([x,y,1]))
assert simplify(f[0]-4*(x+y)) == 0
assert simplify(f[1]-4*(1-y)) == 0
assert simplify(f[2]-(-1-I)*((1-4*I)*x+1-2*I)) == 0

# z3=0, y=1 chart. Three positive b_j require s != 0,-1.
_, d0, W0, P0, R0 = eliminate_first_three(Matrix([s,1,0]))
P_s = (493*s**3+(-2704-548*I)*s**2+(341-200*I)*s-440-60*I)
R_s = (12053*s**2+(-18914-7095*I)*s-6861-7095*I)
kP = Poly(P0,s).LC()/493
kR = Poly(R0,s).LC()/12053
assert simplify(P0-kP*P_s)==0
assert simplify(R0-kR*s*R_s)==0
# Z[i] -> F5: i maps to 2, and 2^2 = -1 mod 5.
p5 = Poly(expand(P_s).subs(I,2),s,modulus=5)
r5 = Poly(expand(R_s).subs(I,2),s,modulus=5)
assert p5 == Poly(-2*s**3+s,s,modulus=5)
assert r5 == Poly(-2*s**2+s-1,s,modulus=5)
assert p5.degree()==3 and r5.degree()==2
assert gcd(p5,r5)==Poly(1,s,modulus=5)

res = resultant(P,R,x)
E = (y-1)**2*(y-1-I)*(y-1+I)*(17*y-9-2*I)*H
quotient, remainder = Poly(res,y,extension=I).div(Poly(E,y,extension=I))
assert remainder.is_zero and quotient.degree()==0 and quotient.LC()!=0
assert gcd(Poly(H,y,extension=I),Poly(diff(H,y),y,extension=I)).degree()==0
assert expand(H.subs(y,1+I))!=0 and expand(H.subs(y,1-I))!=0
for yy in (1+I,1-I):
    gg=gcd(Poly(P.subs(y,yy),x,extension=I),Poly(R.subs(y,yy),x,extension=I))
    assert gg.monic()==Poly(x,x,extension=I)
y0=Rational(9,17)+Rational(2,17)*I
g0=gcd(Poly(P.subs(y,y0),x,extension=I),Poly(R.subs(y,y0),x,extension=I))
assert g0.monic()==Poly(x+y0,x,extension=I)

lin=next(z for z in subresultants(P,R,x) if degree(z,x)==1)
aa=expand(lin).coeff(x,1); bb=expand(lin).coeff(x,0)
modH=lambda obj:rem(expand(obj),H,y,extension=I)
assert gcd(Poly(aa,y,extension=I),Poly(H,y,extension=I)).degree()==0
xx=modH(-bb*invert(aa,H,y,extension=I))
assert modH(P.subs(x,xx))==0 and modH(R.subs(x,xx))==0
D=modH(d.subs(x,xx)); N=modH(W[2].subs(x,xx))
assert gcd(Poly(D,y,extension=I),Poly(H,y,extension=I)).degree()==0
te=modH(N*invert(D,H,y,extension=I))
assert modH(T.subs(t,te))==0
M=Matrix.zeros(4,4)
for j in range(4):
    c=Poly(modH(te*y**j),y,extension=I)
    for i in range(4): M[i,j]=c.nth(i)
assert simplify(M.charpoly(t).as_expr()-T/Poly(T,t).LC())==0
assert gcd(Poly(T,t),Poly(diff(T,t),t)).degree()==0
assert Poly(T,t).count_roots(-S.Infinity,S.Infinity)==2
for lo,hi in [(Rational(45534,100000),Rational(45535,100000)),
              (Rational(64597,100000),Rational(64598,100000))]:
    assert lo>0 and Poly(T,t).count_roots(lo,hi)==1
assert Poly(T,t).eval(1)!=0

observed=[]
for a in (Matrix([0,1+I,1]),Matrix([0,1-I,1])):
    masses=[]
    for j in range(5):
        v=[A[j,k]*a[k]/8 for k in range(3)]
        pairs=[v[k]*conjugate(v[l]) for k in range(3) for l in range(3)]
        masses.append(simplify(sum(pairs)))
    assert masses==[Rational(n,64) for n in b]
    observed.append([str(v) for v in masses])
result={
  'schema':'PREFIX335_EXACT_ALGEBRA_AUDIT_V1',
  'status':'PASS_AUTHOR_SIDE_SYMBOLIC',
  'model':'S7-3 static auxiliary five-port labelled BRC, A as source rows, Q=b/64',
  'exact_input_b':b,
  'chart_infinity':'NO_SOLUTIONS: mod (5,i-2), gcd(-2s^3+s,-2s^2+s-1)=1',
  'affine_D_zero':'NO_SOLUTIONS: b1,b2,b3 positive and f1*f2*f3 != 0',
  'resultant_factors_degrees':{'y=1':2,'y=1+i':1,'y=1-i':1,'17y=9+2i':1,'H(y)':4},
  'resultant_expected_factor_exact':True,
  'quartic_H_squarefree':True,
  'quartic_branch_real_positive_t_count':2,
  'T_real_root_intervals':['(45534/100000,45535/100000)','(64597/100000,64598/100000)'],
  'T_charpoly_exact':True,
  'physical_S1_phase_orbits':4,
  'complex_bilinear_fiber_points':6,
  'explicit_ordered_BRC_pairs_computed':90,
  'limitations':'Auxiliary static BRC only; source authorship is shared-context, not native independent Driver review or X6 bridge',
}
print(json.dumps(result,ensure_ascii=False,indent=2))
