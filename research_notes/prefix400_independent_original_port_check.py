#!/usr/bin/env python3
"""Independent original-complex-Port symbolic expansion for PREFIX-400."""
import sympy as s
I=s.I
A=s.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],
            [-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
A3=A[:3,:]
assert s.expand(A3.det()) == -32+32*I
B=s.simplify(A*A3.inv())
c,d=s.symbols('c d', real=True)
r=s.Rational(59,63)
W=s.Matrix([1,r,c+I*d])
def sq(w):
    e=s.expand_complex(w)
    return s.expand(s.re(e)**2+s.im(e)**2)
ps=[sq(w) for w in B*W]
k=c*c+d*d; T=245*c-123*d; sigma=123*c+245*d
N=s.Integer(75154)
K4=s.Rational(300616,3969); K5=s.Rational(2638189,63504)
assert ps[:3] == [1,s.Rational(3481,3969),k]
assert s.expand(ps[3] - (K4+16*k+s.Rational(16,63)*T))==0
assert s.expand(ps[4] - (K5+s.Rational(53,8)*k+s.Rational(61,504)*T))==0
assert s.expand(T*T+sigma*sigma-N*k)==0
assert s.expand(1+k+2*c - (1+k+s.Rational(2,75154)*(245*T+123*sigma)))==0
for v in [(1,1),(-s.Rational(7687,37577),-s.Rational(52583,37577))]:
    vals=[z.subs({c:v[0],d:v[1]}) for z in ps]
    assert vals == [1,s.Rational(3481,3969),2,s.Rational(550600,3969),s.Rational(4417309,63504)]
print('PASS_PREFIX400_INDEPENDENT_ORIGINAL_A_MATRIX_CIRCLE_AND_CV_IDENTITIES')
print('B4',B[3,:], 'B5',B[4,:])
