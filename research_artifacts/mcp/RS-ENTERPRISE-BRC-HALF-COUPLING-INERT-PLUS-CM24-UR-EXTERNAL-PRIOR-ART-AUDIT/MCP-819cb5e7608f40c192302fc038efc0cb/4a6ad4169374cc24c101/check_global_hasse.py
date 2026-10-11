"""Directed/nonblind local Hesse Hasse check; no queries or native authority.

The trinomial extraction is constructed directly, not imported from author code.
Only primes 19 and 37 are evaluated. Symbolic checks certify the ODE chain rule.
"""
from pathlib import Path
from math import factorial, comb
import hashlib
import json
import sympy as s

H, h, X, x, z, J = s.symbols('H h X x z J')
ROOT = Path(__file__).resolve().parent
SNAPSHOT = ROOT.parent / 'input-snapshot-19b59309'

def poly(expr, var, p):
    return s.Poly(s.expand(expr), var, modulus=p)

def zero(expr, var, p):
    return poly(expr, var, p).is_zero

def pin(path):
    b = path.read_bytes()
    return {'path': str(path), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

source_pins = [pin(SNAPSHOT / name) for name in [
    'CM24_MARKED_HESSE_FRICKE_LOCAL_QUOTIENT_20261011.md', 'check_local_quotient.py']]
assert source_pins[0]['sha256'] == '19b59309b7acc37fb2fa2681ae63273886edf81a960932a697e1eec6267e0772'
assert source_pins[1]['sha256'] == '300dbfcc57746e989c86ef8a804335b79708f8224bc71ad33df7349e53a1e209'

# L_x[G(z(x))] equals 4 L_z[G], checked coefficient by coefficient.
q = 4*x*(1-x)
chain_checks = {
    'G_second': s.expand(x*(1-x)*s.diff(q,x)**2 - 4*q*(1-q)),
    'G_first': s.expand(x*(1-x)*s.diff(q,x,2) + (1-2*x)*s.diff(q,x) - 4*(1-s.Rational(3,2)*q)),
    'G_zero': -s.Rational(2,9) + 4*s.Rational(1,18),
}
assert all(v == 0 for v in chain_checks.values())
R = J**2-J*X*(X**2-126*X+2944)+X*(X+192)**3
assert s.expand(R.subs(J,1728) - (X**2-576*X-1728)**2) == 0
assert s.expand(h**3*(h**3+8)**3-64*(h**3-1)**3-(h**6-20*h**3-8)**2) == 0

def evaluate_pair(polynomial, a, p):
    def add(b,c): return ((b[0]+c[0])%p, (b[1]+c[1])%p)
    def mul(b,c): return ((b[0]*c[0]+2*b[1]*c[1])%p, (b[0]*c[1]+b[1]*c[0])%p)
    out=(0,0)
    for c in polynomial.all_coeffs(): out=add(mul(out,a), (int(c)%p,0))
    return out

def case(p):
    m=(p-1)//6
    assert p == 6*m+1 and s.isprime(p)
    # Direct multinomial coefficient of (xyz)^(p-1) in
    # (x^3+y^3+z^3-3hxyz)^(p-1), choosing a terms from each cube.
    direct = 0
    for a in range(2*m+1):
        n=p-1-3*a
        integer_multinomial=factorial(p-1)//(factorial(a)**3*factorial(n))
        direct += (integer_multinomial*pow(-3,n,p)%p)*h**n
    hasse=poly(direct,h,p)
    simplified=poly(sum((factorial(3*a)*pow(factorial(a)**3*pow(27,a,p),-1,p)%p)*h**(6*m-3*a)
                        for a in range(2*m+1)),h,p)
    assert hasse == simplified
    coefficients=[comb(m,k)*comb(2*m,k)%p for k in range(m+1)]
    G=poly(sum(coefficients[k]*z**k for k in range(m+1)),z,p)
    g_ode=z*(1-z)*s.diff(G.as_expr(),z,2)+(1-pow(2,-1,p)*3*z)*s.diff(G.as_expr(),z)-pow(18,-1,p)*G.as_expr()
    assert zero(g_ode,z,p)
    F=poly(G.as_expr().subs(z,q),x,p)
    f_ode=x*(1-x)*s.diff(F.as_expr(),x,2)+(1-2*x)*s.diff(F.as_expr(),x)-2*pow(9,-1,p)*F.as_expr()
    assert zero(f_ode,x,p)
    assert F.degree() == 2*m and F.eval(0)%p == 1
    for n in range(2*m):
        assert ((n+1)**2*int(F.nth(n+1))-(n+pow(3,-1,p))*(n+2*pow(3,-1,p))*int(F.nth(n)))%p == 0
    pull_h=poly(sum(coefficients[k]*pow(4,k,p)*h**(6*m-6*k)*(h**3-1)**k for k in range(m+1)),h,p)
    assert pull_h == hasse
    S=poly(sum(coefficients[k]*pow(108,k,p)*X**(m-k) for k in range(m+1)),X,p)
    A=(H+3)**6; B=(H+3)**3-27
    pull_H=poly(sum(int(S.nth(m-k))*A**(m-k)*B**k for k in range(m+1)),H,p)
    direct_H=poly(hasse.as_expr().subs(h,pow(3,-1,p)*(H+3)),H,p)
    wrong_H=poly(sum(int(S.nth(m-k))*pow(27,-k,p)*A**(m-k)*B**k for k in range(m+1)),H,p)
    assert direct_H == pull_H and pull_H.degree() == p-1 and pull_H.LC()%p == 1
    assert wrong_H != pull_H
    assert s.gcd(S,S.diff()).degree() == 0
    assert s.gcd(pull_H,pull_H.diff()).degree() == 0
    assert S.eval(0)%p == pow(108,m,p)*comb(2*m,m)%p != 0
    assert S.eval(108)%p == pow(108,m,p)*comb(3*m,m)%p != 0
    assert hasse.eval(1)%p != 0 and hasse.eval(0)%p != 0
    elliptic=poly(h**6-20*h**3-8,h,p)
    elliptic_gcd=s.gcd(hasse,elliptic)
    assert elliptic_gcd.degree() == (6 if p%4 == 3 else 0)
    assert s.gcd(elliptic,elliptic.diff()).degree() == 0
    if p == 19:
        assert zero(S.as_expr()-(X-7)*(X**2-6*X+1),X,p)
        assert elliptic_gcd == elliptic.monic()
    # One concrete bad-normalization root in F_p[sqrt(2)] per requested prime.
    assert pow(2,(p-1)//2,p) == p-1
    D=poly(A-216*B,H,p)
    bad_examples=[]
    for aa in range(p):
        for bb in range(p):
            v=(aa,bb)
            if evaluate_pair(D,v,p) != (0,0): continue
            correct=evaluate_pair(pull_H,v,p); old=evaluate_pair(wrong_H,v,p)
            assert correct == (0,0)
            if old != (0,0):bad_examples.append({'H':v,'correct_Hasse':correct,'old_extra_27_minus_k':old})
    assert len(bad_examples) == 6
    return {'p':p,'m':m,'S_coefficients_ascending':[int(S.nth(k))%p for k in range(m+1)],
            'Hasse_degree':hasse.degree(),'H_degree':pull_H.degree(),'H_monic':True,
            'direct_ternary_equals_correct_pullback':True,'G_ODE':True,'F_ODE':True,'coefficient_recurrence':True,
            'endpoint_values':{'S0':int(S.eval(0)%p),'S108':int(S.eval(108)%p),'Hasse_h0':int(hasse.eval(0)%p),'Hasse_h1':int(hasse.eval(1)%p)},
            'Hasse_squarefree':True,'j1728_Hesse_factor':str(elliptic.as_expr()),
            'j1728_gcd_degree':elliptic_gcd.degree(),'j1728_gcd':str(elliptic_gcd.as_expr()),
            'Hasse_factorization_h':str(s.factor(hasse.as_expr(),modulus=p)),
            'old_wrong_polynomial_gcd_degree':s.gcd(wrong_H,pull_H).degree(),
            'old_normalization_first_counterexample':bad_examples[0],
            'six_marked_216_lifts_old_normalization_fail_count':len(bad_examples)}

results={'schema':'DIRECTED_CM24_GLOBAL_HASSE_CHECK_V1','context':'DIRECTED_SHARED_NONBLIND_NONOFFICIAL_DRIVER_REVIEW',
         'professional_queries':0,'source_pins':source_pins,'symbolic_chain_checks':{k:str(v) for k,v in chain_checks.items()},
         'elliptic_correspondence_square_identity':True,'cases':[case(p) for p in (19,37)],
         'all_prime_argument':'See REPORT.md: finite-field ODE uniqueness, not characteristic-zero series reduction.',
         'scope':'Hesse plane-cubic Hasse polynomial and inherited hypergeometric Fricke pullback; no period/G_p/UR acceptance.'}
(ROOT/'RESULTS.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({'primes':[c['p'] for c in results['cases']],'direct_Hasse_pullback_equal':True,
                 'j1728_gcd_degrees':[c['j1728_gcd_degree'] for c in results['cases']],
                 'old_extra_factor_failures':[c['six_marked_216_lifts_old_normalization_fail_count'] for c in results['cases']],
                 'status':'PASS'},sort_keys=True))
