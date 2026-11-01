"""PREFIX-419 independent original-matrix SymPy verification."""
import sympy as s
I=s.I
M=s.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],[-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
a,b,x,y,h,k,t,r,S=s.symbols('a b x y h k t r S',real=True)
u=a+I*b;v=x+I*y
src=M[:3,:].inv()*s.Matrix([1,u,v])
assert s.simplify(M[:3,:]*src-s.Matrix([1,u,v]))==s.zeros(3,1)
z4=s.expand((M[3,:]*src)[0]);z5=s.expand((M[4,:]*src)[0])
def intensity(z):return s.expand(z*s.conjugate(z))
R=a*a+b*b; Ss=(1+a)**2+b*b
J=(53+29*R)/2+39*a-4*b; A=36+28*a+12*b; B=-20-12*a+28*b
P=(245*(1+a)+123*b)/16; Q=(-123*(1+a)+245*b)/16
c=s.Rational(709,64)*(Ss-2); E=s.Rational(53,8)
T=x*x+y*y; K=c+P*x+Q*y+E*T
assert s.simplify(intensity(z4)-(J+A*x+B*y+16*T))==0
assert s.simplify(intensity(z5)-s.Rational(709,32)-K)==0
mu=B/Q; lam=(A-mu*P)/2; d=16-lam-E*mu
xt=(h-t)/2;yt=(k-c-P*xt-E*t)/Q
assert s.simplify(J+A*xt+B*yt+16*t-(J-mu*c+lam*h+mu*k+d*t))==0
p,q,aa,bb,K0,Z=s.symbols('p q aa bb K0 Z',real=True,nonzero=True)
N=p*p+q*q; alpha=aa*p+bb*q; delta=aa*q-bb*p
lmb=(alpha-delta*K0/Z)/N
X=(K0*p+Z*q)/N;Y=(K0*q-Z*p)/N
assert s.factor(aa-lmb*p-delta*X/Z)==0
assert s.factor(bb-lmb*q-delta*Y/Z)==0
assert s.factor(X*X+Y*Y-(K0*K0+Z*Z)/N)==0
ar=(S-r-1)/2;br=s.symbols('br',real=True)
assert s.simplify(((1+ar)**2+br**2-S)-(ar*ar+br*br-r))==0
print('PASS_PREFIX419_INDEPENDENT_GENERAL_RAW_MATRIX_AFFINE_OBSERVERS_AND_DUAL_SUPPORT')
