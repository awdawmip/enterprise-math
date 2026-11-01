"""GH-91 universal algebra check over Q(z): the final identity is denominator-free."""
import sympy as s
z,x,x1,x2,u,u1,u2,u3=s.symbols('z x x1 x2 u u1 u2 u3')

def B(y,y1,y2):
    return ((1-z)*(y*x2-y1*x1+y2*x)
            +(z-3)*y*x1/4+(3-5*z)*y1*x/4+(2-7*z)*y*x/16)

U3=((9*z-3)*u2/4+(27*z-2)*u1/16+27*z*u/64)/(1-z)
H=8*u1+5*u; J=8*u2+5*u1; T=8*x1+x
K=8*(1-z)*x2+2*(z-3)*x1+(15*z+5)*x/8
left=64*B(u1,u2,u3)+40*B(u,u1,u2)
right=(z-1)*J*T+(2*(z+3)*J+(z+15)*u/8)*x+H*K
assert s.factor((left-right).subs(u3,U3)) == 0
# GH-87 root fiber identity (assuming H=0) at a=9.
a=9; j=s.symbols('j')
U1=-5*u/8; U2=(j-5*U1)/8
E=((1-a)*(2*u*u2-u1**2)+(1-3*a)*u*u1/2-9*a*u**2/16)
assert s.factor(E.subs({u1:U1,u2:U2}, simultaneous=True)) == -u*(32*j+u)/16
print('PASS_GH91_SYMBOLIC_GLOBAL_SYZYGY_AND_TARGET_ROOT_FIBER')
