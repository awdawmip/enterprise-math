"""Independent exact reconstruction of general pure-imaginary five-port coefficients."""
import sympy as s
I=s.I
A=s.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],[-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
w,x,y=s.symbols('w x y',real=True)
u=I*w;v=x+I*y
src=A[:3,:].inv()*s.Matrix([1,u,v])
y4=s.expand((A[3,:]*src)[0]);y5=s.expand((A[4,:]*src)[0])
assert s.simplify(y4-((5+9*I)/2+(3+7*I)/2*u+4*I*v))==0
assert s.simplify(y5-((22+15*I)/8)*(1+u)-(5+9*I)/4*v)==0
j=(53-8*w+29*w*w)/2
p=(245+123*w)/16
q=(-123+245*w)/16
c=s.Rational(709,64)*(w*w-1)
t=x*x+y*y
I4=s.expand(s.expand_complex(y4*s.conjugate(y4)))
k=s.expand(s.expand_complex(y5*s.conjugate(y5)))-s.Rational(709,32)
assert s.simplify(I4-(j+(36+12*w)*x+(-20+28*w)*y+16*t))==0
assert s.simplify(k-(c+p*x+q*y+s.Rational(53,8)*t))==0
assert s.simplify((p*p+q*q)-s.Rational(37577,128)*(1+w*w))==0
assert s.simplify((36+12*w)*q-(-20+28*w)*p+(63*w*w-368*w-59)/2)==0
print('PASS_PREFIX417_INDEPENDENT_RAW_MATRIX_GENERAL_W_COEFFICIENTS')
