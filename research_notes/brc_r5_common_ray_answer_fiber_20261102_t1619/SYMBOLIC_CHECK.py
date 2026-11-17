"""Independent exact SymPy check of formal real-parameter 4D minors."""
import sympy as s
R=s.Rational
a,b,c=s.symbols('u_C u_I u_B',real=True)
def obs(x,jB,jI,kC,kI,kBJ,kIJ):
 x,jB,jI,kC,kI,kBJ,kIJ=map(s.sympify,(x,jB,jI,kC,kI,kBJ,kIJ))
 D=((1-jB)+(1-x)*(1-jI))/8
 w=(R(1,4),(1-x)/4,(1-jB)/8,(1-x)*(1-jI)/8)
 C=sum(m*(1-k) for m,k in zip(w,(kC,kI,kBJ,kIJ)))
 U=sum(m*(1-k)*u for m,k,u in zip(w,(kC,kI,kBJ,kIJ),(a,b,c,c)))
 return s.Matrix([1-R(2,5)*D-U,R(3,5)*D+U,
                  R(5,2)-R(3,4)*x+2*D+R(3,2)*C,
                  R(5,2)-R(3,4)*x+2*D+R(4,3)*C])
V=[obs(x,y,y,z,z,z,z) for x in (0,1) for y in (0,1) for z in (0,1)]
D=s.factor(s.Matrix.hstack(*[V[i]-V[0] for i in (1,2,3,4)]).det())
assert s.simplify(D+(2*c-a-b)/2560)==0
x,jB,jI,kC,kI,kBJ,kIJ=s.symbols('x jB jI kC kI kBJ kIJ')
f=obs(x,jB,jI,kC,kI,kBJ,kIJ)
J=s.factor(f.jacobian((x,jB,kC,kI)).subs({i:R(1,2) for i in (x,jB,jI,kC,kI,kBJ,kIJ)}).det())
assert s.simplify(J+(a-b)/10240)==0
print('LR_AFFINE_DET',D)
print('FULL_INTERIOR_JAC',J)
print('PASS_R5_COMMON_RAY_SYMBOLIC')
