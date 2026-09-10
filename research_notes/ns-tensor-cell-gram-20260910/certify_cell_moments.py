#!/usr/bin/env python3
"""Exact independent polynomial checks of the centered-cube numerator identity.
General proof is algebraic; these rational rotations test its implementation.
"""
from pathlib import Path
import sympy as s
import json
x=s.Matrix(s.symbols('x0:3'));cases=[]
def average(expr):
    out=s.S.Zero
    for powers,c in s.Poly(s.expand(expr),*x).terms():
        m=s.S.One
        for n in powers:
            if n%2:m=0;break
            m*=s.Rational(1,(n+1)*2**n)
        out+=c*m
    return s.factor(out)
def rotation(q):
    a,b,c,d=map(s.Integer,q);n=a*a+b*b+c*c+d*d
    return s.Matrix([[a*a+b*b-c*c-d*d,2*(b*c-a*d),2*(b*d+a*c)],
                     [2*(b*c+a*d),a*a-b*b+c*c-d*d,2*(c*d-a*b)],
                     [2*(b*d-a*c),2*(c*d+a*b),a*a-b*b-c*c+d*d]])/n
for q0 in [(1,0,0,0),(1,1,0,0),(1,2,3,4),(2,-1,3,1),(3,2,-1,4),(5,-2,1,3)]:
    R=rotation(q0);assert R.T*R==s.eye(3)
    e=R[:,2];t=R[:,0];A=s.eye(3)-e*e.T;B=s.eye(3)-t*t.T
    assert A*B==B*A and A*B*e==s.zeros(3,1)
    for p0 in [(1,2,3),(-2,1,0),(0,0,0)]:
        p=s.Matrix(p0);k=7*e;q=k-p
        aa=(p.T*A*p)[0];bb=(q.T*B*q)[0]
        lhs=average(((p+x).T*A*(p+x))[0]*((q-x).T*B*(q-x))[0])
        quart=average((x.T*A*x)[0]*(x.T*B*x)[0])
        rhs=aa*bb+(s.trace(A)*bb+s.trace(B)*aa+4*(p.T*A*B*p)[0])/12+quart
        assert s.simplify(lhs-rhs)==0 and lhs>=aa*bb and quart>=0
        cases.append({'quaternion':q0,'p':p0,'positive_excess':str(lhs-aa*bb),'fourth_moment_term':str(quart)})
assert s.simplify((3*s.pi**3/8)/(2*s.pi)**3-s.Rational(3,64))==0
assert s.simplify((s.pi**3/2)/(2*s.pi)**3-s.Rational(1,16))==0
(Path(__file__).parent/'cell_moments_verification.json').write_text(json.dumps({
 'status':'PASS','rational_rotated_cases':len(cases),'cases':cases,
 'continuum_bilinear_squared_constant':'3/64','continuum_first_input_only_squared_constant':'1/16',
 'scope':'exact polynomial diagnostics supporting, not replacing, the general algebraic proof'},indent=2)+'\n')
print('PASS',len(cases),'exact rational rotated cell identities')
