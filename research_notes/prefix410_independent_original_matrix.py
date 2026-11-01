"""Independent PREFIX-410 witness check from the original 5x3 complex A matrix.

No use of the reduced I4/I5 coefficients nor the main checker's
Fraction-pair implementation. Symbolic Rational/Matrix arithmetic only.
"""
import sympy as S
R=S.Rational; I=S.I
A=S.Matrix([
 [4,4,0],
 [0,-4,4],
 [-5+3*I,0,-3+I],
 [-2-2*I,4+4*I,2+2*I],
 [-2,0,5+2*I],
]); assert A[:3,:3].det()!=0
u=R(9,10000000)+I*R(19999991,20000000)
v=R(2499,50000000)-I*R(7,50000)
W=S.Matrix([1,u,v])
Y=A[:3,:].inv()*W
ports=A*Y
assert all(S.simplify(ports[j]-W[j])==0 for j in range(3))

def n2(z):return S.expand(S.conjugate(z)*z).simplify()
I1=n2(ports[0]);I2=n2(ports[1]);I3=n2(ports[2]);I4=n2(ports[3]);I5=n2(ports[4]);Cu=n2(ports[0]+ports[1]);Cv=n2(ports[0]+ports[2]);
eps=R(1,1000000);eta=R(1,10000);beta=eps
assert I1==1
assert 1-eps<=I2<=1+eps
assert 2-eps<=Cu<=2+eps
assert 0<=I3<=beta
assert 1-eta<=Cv<=1+eta
assert R(709,32)-eta<=I5<=R(709,32)+eta
assert I4==R(740026064956965833,20000000000000000)
kappa=41-I4
assert kappa==R(79973935043034167,20000000000000000)
assert kappa<4-R(792,61)*eta
print('PASS original five-Port A, recovered Y, all six interval inequalities')
print('PORTS',*[str(S.simplify(z)) for z in ports])
print('RECONSTRUCTED_Y',*[str(S.simplify(z)) for z in Y])
print('I2',I2,'Cu',Cu,'I3',I3,'Cv',Cv,'I4',I4,'I5',I5)
print('KAPPA_UPPER',kappa)
print('PASS_PREFIX410_INDEPENDENT_ORIGINAL_MATRIX_SOURCE_WITNESS')
