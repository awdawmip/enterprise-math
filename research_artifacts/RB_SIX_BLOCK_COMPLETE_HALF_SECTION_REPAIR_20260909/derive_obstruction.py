"""Symbolic discovery of an integer certificate for a necessary ODE obstruction."""
import json
import sympy as s

R,t,k,a,b,c,d,e,f,u,v=s.symbols('R t k a b c d e f u v')
P=R**3-3*R
F=(R+2)*t
G=a*R**3+b*R**2+c*R+d+(e*R+f)*t

def red(expr):
    return s.rem(s.Poly(s.expand(expr),t),s.Poly(t*t-P,t)).as_expr().expand()

def D(expr):
    return red(2*t*s.diff(expr,R)+3*(R*R-1)*s.diff(expr,t))

N=red(F*D(G)-G*D(F))
atQ=s.rem(s.Poly(N.subs(t,-k),R),s.Poly(P-k*k,R)).as_expr().expand()
C2=s.Poly(atQ,R).coeff_monomial(R**2)
H=s.rem(s.Poly(((R+2)*3*(R*R-1))**2,R),s.Poly(P,R)).as_expr().expand()
Lb=k*k*b-72*a
Lc=k*k*c+(3*k*k-144)*a
Ld=k*k*d-36*a
psi=k**4-12*k*k-324
certificate=s.expand(k*k*C2+(k*k+12)*Lb+6*Lc+6*Ld-6*a*psi)

def biquad(expr):
    q=s.rem(s.Poly(s.expand(expr),u),s.Poly(u*u-2,u)).as_expr()
    return s.rem(s.Poly(s.expand(q),v),s.Poly(v*v-3,v)).as_expr().expand()

q=12*u-10*v
frozen=biquad(q*q-12*q-324)
norm=biquad(s.prod(frozen.subs({u:su*u,v:sv*v},simultaneous=True) for su in [-1,1] for sv in [-1,1]))
norm_cofactor=s.div(s.Poly(s.rem(s.Poly(s.expand(s.prod(frozen.subs({u:su*u,v:sv*v},simultaneous=True) for su in [-1,1] for sv in [-1,1])),v),s.Poly(v*v-3,v)).as_expr()-norm,u),s.Poly(u*u-2,u))
out={'sympy_version':s.__version__,'ODE':'N^2 = 4*K_ODE*(t+k)^2*G*(G-F)*(G-lambda*F)','leading_pole_condition':'a != 0 and 4*K_ODE*a=1','torsion_remainder_H':str(H),'torsion_coefficient_constraints':[str(x) for x in [Lb,Lc,Ld]],'critical_R2_coefficient':str(C2),'integer_elimination_identity_residual':str(certificate),'forced_frozen_condition':str(psi),'frozen_k_squared':str(q),'frozen_obstruction':str(frozen),'obstruction_norm_over_Q':str(norm),'norm_cofactor_after_v_relation':str(norm_cofactor[0].as_expr()),'norm_cofactor_remainder':str(norm_cofactor[1].as_expr()),'critical_cubic_discriminant_factor':str(biquad(4-q*q))}
assert certificate==0 and norm!=0 and norm_cofactor[1].as_expr()==0
print(json.dumps(out,indent=2))
