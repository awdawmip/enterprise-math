#!/usr/bin/env python3
"""Exact symbolic two-class native X6-BRC characteristic polynomial certificate.
Requires sympy; no floats, approximation or random parameter interpolation.
Frozen source: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d
"""
import sympy as S

STAR=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):
    return tuple(-k if c>0 else k for k in STAR[a] if k!=abs(c))
PH=tuple((a,p,sgn*k) for a in range(4) for k in STAR[a]
         for sgn in (-1,1) for p in near(a,sgn*k))
IX={p:i for i,p in enumerate(PH)}
def next_phase(i):
    a,p,c=PH[i]
    b=next(b for b in range(4) if b!=a and abs(c) in STAR[b])
    return tuple(IX[x] for x in
         ([(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)]))
N=tuple(next_phase(i) for i in range(48))
G=IX[(0,1,-3)]
AX=tuple(abs(v[2])-1 for v in PH)
w,z,t=S.symbols('w z t')
x=[S.Integer(1)]*4+[w,w]
assert len(PH)==48 and G==4 and all(len(n)==3 for n in N)
assert all(PH[i][2]*PH[j][2]<0 for i in range(48) for j in N[i])
def Q(zval):
    A=S.zeros(48)
    for i in range(48):
        for j in N[i]:
            A[i,j]=x[AX[i]]*(1 if i==G else (3+zval if j==G else 2))
    return A
s=t*t
L=s*s+4*(w+1)*s-48*w
F=(s-4)*(s-4*w)**6*(s+12*w)**2*L**3
Cp=(t**3-2*t*t-12*t*w-72*w)*(t**3+2*t*t-12*t*w+72*w)
Cm=(t**3-2*t*t+4*t*w+24*w)*(t**3+2*t*t+4*t*w-24*w)
P=(s-4)*L*Cp*Cm
B=4*((4*w+1)*s**7
 +4*(16*w**2-11*w-2)*s**6
 +16*(24*w**3+34*w**2-2*w+1)*s**5
 +64*w*(48*w**3-270*w**2-92*w+9)*s**4
 +768*w**2*(12*w**3-81*w**2+140*w-18)*s**3
 -27648*w**3*(21*w**2+38*w+10)*s**2
 +995328*w**4*(10*w+7)*s
 -35831808*w**5)
A1,A2,Az=Q(S.Integer(1)),Q(S.Integer(2)),Q(z)
u=S.Matrix([x[AX[i]]*int(G in N[i]) for i in range(48)])
e=S.zeros(48,1)
e[G]=1
assert A2-A1==u*e.T
assert Az-A1==(z-1)*u*e.T
c1=A1.charpoly(t).as_expr()
c2=A2.charpoly(t).as_expr()
cz=Az.charpoly(t).as_expr()
assert S.Poly(c1-F*P,t,w).is_zero
assert S.Poly(c2-F*(P-B),t,w).is_zero
assert S.Poly(cz-F*(P-(z-1)*B),t,w,z).is_zero
assert S.Poly(cz.subs(t,0)-2**46*3**12*(z+3)*w**16,w,z).is_zero
assert S.Poly(cz-t**48,t).degree(t)<=46
assert all(S.Poly(cz,t).coeff_monomial(t**(2*k+1))==0 for k in range(24))
# The w=0 family: exact symbolic minimal annihilators and sharp lower bounds.
Q0=Az.subs(w,0)
assert S.Poly(cz.subs(w,0)-t**32*(t**4-16)**3*(t**4-4*(z+3)),t,z).is_zero
def poly_at_matrix(p,A):
    X=S.zeros(48)
    I=S.eye(48)
    for a in S.Poly(p,t).all_coeffs():X=X*A+a*I
    return X
p=t*t*(t**4-16)*(t**4-4*(z+3))
assert all(S.Poly(v,z).is_zero for v in poly_at_matrix(p,Q0))
assert S.Poly(poly_at_matrix(p/t,Q0)[1,10]+256*(z+3),z).is_zero
Q01=Q0.subs(z,1)
assert all(v==0 for v in poly_at_matrix(t*t*(t**4-16),Q01))
assert poly_at_matrix(t*(t**4-16),Q01)[1,10]==64
assert Q01.rank()==32
# Exact independent finite specializations of the global polynomial identity.
for w0 in (0,1,2,3,5):
    for z0 in (0,1,2):
        A=Az.subs({w:w0,z:z0})
        assert S.Poly(A.charpoly(t).as_expr()-cz.subs({w:w0,z:z0}),t).is_zero
print("ALL_ASSERTIONS_PASS: Z[w,z,t] identity, rank-one gate, parity, determinant, w=0 sharp minpoly, 15 integer specializations")
