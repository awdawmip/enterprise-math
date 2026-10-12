#!/usr/bin/env python3
"""Exact symbolic algebra only. No prime or finite-field campaign."""
import json
from pathlib import Path
import sympy as S

k,n,u,a,Q2,Q3,La,Lma = S.symbols('k n u a Q2 Q3 La Lma')
checks = []
def check(name, expr):
    value = S.factor(S.cancel(expr))
    assert value == 0, (name, value)
    checks.append(name)

rk = -3*(6*k+1)*(3*k+1)*(n-k)/(2*(3*k-n+1)*(3*k-n+2)*(3*k-n+3))
rnplus = -4*(3*k-n)/(3*(n-k+1))
rnminus = -3*(n-k)/(4*(3*k-n+1))
R = 2*(3*k-n)*(2*n+1)*(3*k-n-1)/(3*(n-k+1))
A = (n+1)*(2*n+1)
B = -(10*n*n+5*n+1)
C = 4*n*(2*n-1)
check('summand rational telescoper', rk*R.subs(k,k+1)-R-A*rnplus-B-C*rnminus)

w = (1-u)*(1-4*u)**2
wp = S.diff(w,u)
wpp = S.diff(wp,u)
heun_a = 2*u*(u-1)*(4*u-1)
heun_b = 20*u*u-15*u+1
heun_c = 4*u-1
pull_a = w*(1-w)*wp
pull_b = (1-S.Rational(3,2)*w)*wp**2-w*(1-w)*wpp
pull_c = -wp**3/18
factor = S.Rational(3,2)*(4*u-3)**3*(4*u-1)**2
check('Heun pullback leading', pull_a-factor*heun_a)
check('Heun pullback middle', pull_b-factor*heun_b)
check('Heun pullback constant', pull_c-factor*heun_c)
check('coefficient recurrence next', 2*(n+1)*n+(n+1)-A)
check('coefficient recurrence middle', -10*n*(n-1)-15*n-1-B)
check('coefficient recurrence previous', 8*(n-1)*(n-2)+20*(n-1)+4-C)
check('terminal forward coefficient', A.subs(n,-S.Rational(1,2)))
check('terminal middle coefficient', B.subs(n,-S.Rational(1,2))+1)
check('terminal previous coefficient', C.subs(n,-S.Rational(1,2))-4)

weights = json.loads(Path(__file__).with_name('TRANSFORMED_OBSERVER_WEIGHTS.json').read_text())
def wt(v):
    return S.sympify(weights['Lambda_weight_'+v], locals={'a':a})
base = {
    'Aw': -2*Q2, 'At': -Q2/3+Q3/2, 'Ae': 2*Q3-S.Rational(10,3)*Q2,
    'Bw': -2*Q2, 'Bt': Q2, 'Be': 2*Q2,
    'Cw': La+Lma, 'Ct': -La/3+a*Lma/3, 'Ce': -La/3+(1+4*a/3)*Lma,
    'Dw': 2*Q2-S.Rational(3,2)*Q3, 'Dt': 0, 'De': 2*Q2-S.Rational(3,2)*Q3,
    'Fw': 2*Q2-S.Rational(3,2)*Q3, 'Ft': -Q2/3+Q3/2,
    'Fe': S.Rational(2,3)*Q2+Q3/2,
}
const = sum(wt(v)*x for v,x in base.items())+2*Q3
target = -S.Rational(8,3)*(1+2*a)*Q2+3*Q3-4*a*La+2*Lma
num = S.fraction(S.cancel(const-target))[0]
check('full observer finite logarithm constants', S.rem(num,a*a-S.Rational(1,2),a))

H,Lneg2,Lneg1,L2,Laa,Lminus2a,Lhalf = S.symbols('H Lneg2 Lneg1 L2 Laa Lminus2a Lhalf')
rho = S.symbols('rho')
parts = {
    'Aw': -2*H, 'At': rho*Lneg2/2, 'Ae': 0,
    'Bw': -2*Lneg1, 'Bt': rho*L2/2, 'Be':0,
    'Cw': -2*Laa, 'Ct': rho*Lminus2a/2, 'Ce':0,
    'Dw': -2*Lhalf, 'Dt':rho*Lneg1/2, 'De':0,
    'Fw': -2*Lneg1, 'Ft':rho*H/2, 'Fe':0,
}
kernel = H+2*rho*Lneg2-5*(4*a+3)*Lneg1/9-(4*a+3)*rho*L2/9
kernel += 2*(2*a+1)*Laa+2*(a-1)*rho*Lminus2a+8*a*Lhalf/9-20*a*rho*Lneg1/9
check('full observer coefficient kernel', sum(wt(v)*x for v,x in parts.items())-kernel)

out = {'status':'PASS_EXACT_SYMBOLIC_ONLY', 'prime_instantiations':0,
       'checks':checks, 'count':len(checks),
       'scope':'two-index Heun telescoper, pullback and fixed observer algebra; not LIFT'}
Path(__file__).with_name('TWO_INDEX_SYMBOLIC_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
