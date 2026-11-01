"""PREFIX-418: independent exact symbolic reconstruction of the auxiliary 5-port model."""
import sympy as s

I = s.I
u,v,w,x,y = s.symbols('u v w x y', real=False)
M = s.Matrix([
    [4,4,0],
    [0,-4,4],
    [-5+3*I,0,-3+I],
    [-2-2*I,4+4*I,2+2*I],
    [-2,0,5+2*I],
])
source = M[:3,:].inv()*s.Matrix([1,u,v])
assert s.simplify(M[:3,:]*source-s.Matrix([1,u,v])) == s.zeros(3,1)
z4 = s.expand((M[3,:]*source)[0])
z5 = s.expand((M[4,:]*source)[0])
assert s.simplify(z4-((5+9*I)/2+(3+7*I)*u/2+4*I*v)) == 0
assert s.simplify(z5-((22+15*I)*(1+u)/8+(5+9*I)*v/4)) == 0

# Use a fresh real-coordinate expression, not previous program's coefficients.
ww,xx,yy = s.symbols('w x y',real=True)
def abs2(z):
    z = s.expand(z.subs({u:I*ww,v:xx+I*yy}))
    return s.expand(z*s.conjugate(z))
T = xx*xx+yy*yy
J = (53-8*ww+29*ww**2)/2
A,B = 36+12*ww,-20+28*ww
P,Q = (245+123*ww)/16,(-123+245*ww)/16
c = s.Rational(709,64)*(ww*ww-1)
E = s.Rational(53,8)
assert s.simplify(abs2(z4)-(J+A*xx+B*yy+16*T)) == 0
assert s.simplify(abs2(z5)-s.Rational(709,32)-(c+P*xx+Q*yy+E*T)) == 0
assert s.expand(P**2+Q**2-s.Rational(37577,128)*(1+ww**2)) == 0
assert s.expand((A*Q-B*P)+(63*ww**2-368*ww-59)/2) == 0
print('PASS_PREFIX418_INDEPENDENT_EXACT_RAW_MATRIX_PORT_AND_PHASE_COEFFICIENTS')