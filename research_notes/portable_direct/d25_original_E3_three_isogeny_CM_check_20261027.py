#!/usr/bin/env python3
"""Author-only exact certificate: original E3 3-isogeny and CM de Rham eigenlines.
Not a native H0/B0 divided-power Frobenius experiment.
"""
import sympy as S
x, y, c = S.symbols('x y c')
q = S.Rational
f = x**3 + x**2/4 + c*x/2 + c**2/4
U = x + c/x + c**2/x**2
D = S.diff(U, x)
q3 = U**3 + U**2/4 - q(9,2)*c*U - c*(27*c+4)/4
assert S.cancel(f*D**2-q3) == 0  # full rational Velu curve map
assert S.cancel((x*S.diff(f,x)-2*f)/x**2-(x-c/(2*x)-c**2/(2*x**2))) == 0
s = S.sqrt(2)
t = (2-s)/4
c0, cb = t/27, (1-t)/27

def f_of(X, cc):
    return X**3 + X**2/4 + cc*X/2 + cc**2/4

def f3_of(X, cc):
    return X**3 + X**2/4 - q(9,2)*cc*X - cc*(27*cc+4)/4
assert S.simplify(S.expand(f3_of(-3*y-q(1,3),c0)+27*f_of(y,cb))) == 0

# Already-documented original E3 2-isogeny M2 is consumed, not re-proved.
u = S.sqrt(-3)
M2 = S.Matrix([[s,-q(1,18)],[0,s]])
M2sig = S.Matrix([[-s,-q(1,18)],[0,-s]])
# New original E3 3-isogeny, columns are pulled-back target de Rham classes.
M3 = S.Matrix([[u,-u/9],[0,-u]])
Mtheta = S.simplify(M3*M2sig)
beta = (4-s)/72
for M, val in [(M2*M2sig+2*S.eye(2),0),
               (M3*M3+3*S.eye(2),0),
               (Mtheta*Mtheta+6*S.eye(2),0)]:
    assert all(S.simplify(v)==val for v in M)
assert S.simplify(M3.det()-3) == 0
assert S.simplify(Mtheta.det()-6) == 0
assert all(S.simplify(v)==0 for v in Mtheta*S.Matrix([beta,1])-
           s*u*S.Matrix([beta,1]))

# Original p=373 witness in F_p[T]/(T^2-2), with u^2=-3 in the base field.
p=373
root_u=177
assert (root_u*root_u+3)%p == 0 and pow(2,(p-1)//2,p)==p-1
P=lambda a,b:(a%p,b%p)
zero=P(0,0)
add=lambda a,b:P(a[0]+b[0],a[1]+b[1])
mul=lambda a,b:P(a[0]*b[0]+2*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
neg=lambda a:P(-a[0],-a[1])
scale=lambda a,k:P(a[0]*k,a[1]*k)
def matmul(A,B):
    return [[add(mul(A[i][0],B[0][j]),mul(A[i][1],B[1][j]))
             for j in range(2)] for i in range(2)]
inv9,inv18,inv72=(pow(q,-1,p) for q in (9,18,72))
T=P(0,1)
M3p=[[P(root_u,0),P(-root_u*inv9,0)],[zero,P(-root_u,0)]]
M2sigp=[[neg(T),P(-inv18,0)],[zero,neg(T)]]
Cp=matmul(M3p,M2sigp)
assert Cp==[[P(0,196),P(301,144)],[zero,P(0,177)]]
assert matmul(Cp,Cp)==[[P(-6,0),zero],[zero,P(-6,0)]]
Bp=P(4*inv72,-inv72)
assert Bp==P(228,316)
v=[Bp,P(1,0)]
lhs=[add(mul(Cp[i][0],v[0]),mul(Cp[i][1],v[1])) for i in range(2)]
rhs=[mul(P(0,root_u),v[0]),mul(P(0,root_u),v[1])]
assert lhs==rhs
print('EXACT_ORIGINAL_E3_CM_ISOGENY_CERTIFICATE_PASS')
print('p=373, u=177, M3=',M3p,' theta=',Cp,' beta=',Bp)
print('H0/B0_NATIVE_BENCHMARK_NOT_EXECUTED')
