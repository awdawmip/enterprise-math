"""Symbolic p^3 CM/reference identities only; no numerical primes."""
import json
from pathlib import Path
import sympy as S

z,t,q,delta = S.symbols('z t q delta')
p = S.symbols('p', integer=True, positive=True)
J = t*(t-3)*(3*t-1)/(t*t-1)**2
A = (3*z-1)/(z-1)**3
B = (3*z-1)**2/(z+1)**3
L = (z+1)/(2*(1-z))
K = -z*(z-3)*(3*z-1)/(3*(z+1)**2)
checks=[]

def exact(name,expr):
    residual=S.factor(S.cancel(S.simplify(expr)))
    assert residual==0,(name,residual)
    checks.append({'name':name,'residual':str(residual)})

def cm(name,expr):
    n,d=S.fraction(S.cancel(expr))
    pol=z*z-6*z+1
    r=S.rem(S.rem(n,pol,z)*S.invert(S.rem(d,pol,z),pol,z),pol,z)
    exact(name,r)

exact('J_double_critical_identity',J-S.Rational(1,4)+(t*t-6*t+1)**2/(4*(t*t-1)**2))
exact('J_prime_at_three',S.diff(J,t).subs(t,3)-S.Rational(3,8))
exact('J_prime_at_one_third',S.diff(J,t).subs(t,S.Rational(1,3))+S.Rational(27,8))
exact('reference_derivative_retained',S.diff((p/3)*J.subs(t,z**p),z)/p**2-z**(p-1)*S.diff(J,t).subs(t,z**p)/3)
cm('CM_K_L_prime',K*S.diff(L,z)+S.Rational(1,12))
cm('CM_K_A_prime',K*S.diff(A,z)-S.Rational(1,8))
cm('CM_A_prime_equals_B_prime',S.diff(A,z)-S.diff(B,z))
cm('CM_delta_squared',(2*L)**2-2)
cm('CM_J_value',J.subs(t,z)-S.Rational(1,4))
cm('CM_J_prime',S.diff(J,t).subs(t,z))

y,v,c0,c1 = S.symbols('y v c0 c1')
M0=p*y
fa=M0+p**2*delta*c0/4
fb=M0-p**2*delta*c0/4
da=-2*delta*v-p**2*(c1-c0)
db=2*delta*v-p**2*(c1-c0)
Rcm=-fa*fb/12+(delta/16)*(fb*da-fa*db)
res=S.rem(S.Poly(S.expand(Rcm+M0**2/12+M0*v/2),delta),S.Poly(delta**2-2,delta)).as_expr()
for k in range(3):
    exact(f'CM_R_plus_pU_over_12_coefficient_p{k}',S.expand(res).coeff(p,k))

bquot=1+p*(S.Rational(9,2)-3*q)
lam=S.expand((p**2-p+S.Rational(2,9))*bquot)
exact('Lambda_div_p2_constant',lam.coeff(p,0)-S.Rational(2,9))
exact('Lambda_div_p2_next_digit',lam.coeff(p,1)+S.Rational(2,3)*q)
prod=S.expand(9*(1+2*p*q)*lam/2)
exact('infinity_normalization_constant',prod.coeff(p,0)-1)
exact('infinity_normalization_next_digit',prod.coeff(p,1)+q)

d0,d3,d13=S.symbols('d0 d3 d13')
nodes=[S.Rational(0),S.Rational(3),S.Rational(1,3)]
vals=[d0,d3,d13]
eta=sum(val*(a*a-1)**2*S.prod((t-b)/(a-b) for b in nodes if b!=a)
        for a,val in zip(nodes,vals))
for a,val in zip(nodes,vals):
    exact(f'interpolation_at_{a}',eta.subs(t,a)-val*(a*a-1)**2)
exact('kernel_J_infinity_coefficient',S.limit(t*J,t,S.oo)-3)
exact('eta_has_no_first_infinity_coefficient',S.limit(t*eta/(t*t-1)**2,t,S.oo))

report={'status':'PASS_EXACT_SYMBOLIC_SECOND_DIGIT_IDENTITIES',
        'scope':'Symbolic CM, reference, scalar and interpolation identities; no prime scan',
        'check_count':len(checks),'checks':checks,
        'LIFT_claimed_proved':False}
Path(__file__).with_name('EXACT_CM_SECOND_DIGIT_CHECK.json').write_text(json.dumps(report,indent=2)+'\n')
print(f'PASS: {len(checks)} exact symbolic identities; LIFT remains OPEN.')
