"""Exact symbolic identities only; no prime scan or numerical evidence."""
from pathlib import Path
import json
import sympy as S

z = S.symbols('z')
A = (3*z-1)/(z-1)**3
B = (3*z-1)**2/(z+1)**3
L = (z+1)/(2*(1-z))
K = -z*(z-3)*(3*z-1)/(3*(z+1)**2)
a = lambda u: u*(1-u)
b = lambda u: 1-2*u
Ap, Bp = S.diff(A, z), S.diff(B, z)
T = Ap/(2*L)
checks = {
    'K_is_B_divergence_factor': K-a(B)/Bp,
    'leading_pullback_coefficient': K*L*Ap**2-T*a(A),
    'first_pullback_coefficient':
        2*K*S.diff(L,z)*Ap+S.diff(K*Ap,z)*L-T*b(A),
    'zero_pullback_coefficient':
        S.diff(K*S.diff(L,z),z)-S.Rational(2,9)*Bp*L+S.Rational(2,9)*T,
    'K_A_gauge_relation': K*L**2-a(A)/(2*Ap),
}
pol = z*z-6*z+1

def cmreduce(e):
    n,d = S.fraction(S.cancel(e))
    rn,rd = S.rem(n,pol,z), S.rem(d,pol,z)
    return S.rem(rn*S.invert(rd,pol,z),pol,z)

cmchecks = {
    'A_plus_B': A+B-1,
    'common_q': 4*A*(1-A)-S.Rational(1,2),
    'A_equals_B_derivative': Ap-Bp,
    'CM_derivative': Ap+S.Rational(3,8)/z,
    'Kr': K*Bp-S.Rational(1,8),
    'delta_squared': (2*L)**2-2,
    'A_from_delta': A-(2+2*L)/4,
    'Frobenius_shape_evaluation':
        z*(z-3)*(3*z-1)/((z-1)**2*(z+1)**2)-S.Rational(1,4),
}
results = {k:str(S.factor(e)) for k,e in checks.items()}
results.update({k:str(S.factor(cmreduce(e))) for k,e in cmchecks.items()})
assert all(v == '0' for v in results.values()), results
out = {
    'schema':'EM_PURE_SYMBOLIC_PULLBACK_CHECK_V1',
    'new_prime_campaign':False,
    'all_exact_rational_identities_zero':True,
    'checks':results,
    'limits':'This verifies symbolic identities only; the finite pole/Frobenius argument and p-integral precision require the paper proof.',
}
Path(__file__).with_name('EXACT_SYMBOLIC_PULLBACK_IDENTITIES.json').write_text(
    json.dumps(out,indent=2)+'\n'
)
print('PASS: all 13 exact rational pullback and CM identities vanish.')
