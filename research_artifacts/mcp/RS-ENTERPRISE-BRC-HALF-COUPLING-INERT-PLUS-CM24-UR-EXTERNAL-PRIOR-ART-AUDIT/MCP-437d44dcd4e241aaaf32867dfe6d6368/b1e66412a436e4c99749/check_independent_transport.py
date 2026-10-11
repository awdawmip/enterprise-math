"""Bounded independent read-only reproduction of frozen p^2 transport.

Uses direct product/factorial coefficients and polynomial convolution instead
of author recurrence/binomial composition; imports no author checker.
Outputs are confined to this review directory. Not formal DR or UR/LIFT proof.
"""
from fractions import Fraction as R
from math import factorial, comb
from pathlib import Path
from hashlib import sha256
import ast
import json
import sympy as sy

ROOT = Path(__file__).resolve().parent
SELECTED = [7, 13, 19, 37, 73]


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def product_coefficient(n, aa, bb):
    numerator = R(1)
    for j in range(n):
        numerator *= (aa+j)*(bb+j)
    return numerator / factorial(n)**2


def arrays(p):
    return ([product_coefficient(n, R(1, 6), R(1, 3)) for n in range(p)],
            [product_coefficient(n, R(1, 3), R(2, 3)) for n in range(p)])


def convolution(a, b):
    c = [R(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def substitute(a, linear_or_quadratic):
    result = [R(0)]*((len(a)-1)*(len(linear_or_quadratic)-1)+1)
    power = [R(1)]
    for c in a:
        for k, t in enumerate(power):
            result[k] += c*t
        power = convolution(power, linear_or_quadratic)
    return result


def residue(c, modulus):
    c = R(c)
    require(c.denominator % modulus != 0, 'denominator zero')
    return c.numerator*pow(c.denominator, -1, modulus) % modulus


def valuation(c, p):
    require(c != 0, 'finite valuation of zero requested')
    a, b = abs(c.numerator), c.denominator
    n = 0
    while a % p == 0:
        n += 1
        a //= p
    while b % p == 0:
        n -= 1
        b //= p
    return n


def pair_mul(a, b, modulus):
    return ((a[0]*b[0]+2*a[1]*b[1]) % modulus,
            (a[0]*b[1]+a[1]*b[0]) % modulus)


def evaluate_pair(a, x, modulus):
    # Weighted successive powers, not the author's Horner evaluation.
    result = [0, 0]
    power = (1, 0)
    for c in a:
        r = residue(c, modulus)
        for j in range(2):
            result[j] = (result[j]+r*power[j]) % modulus
        power = pair_mul(power, x, modulus)
    return tuple(result)


def pair_sub(a, b, modulus):
    return tuple((x-y) % modulus for x, y in zip(a, b))


def quotient_digit(value, p):
    require(all(x % p == 0 for x in value), 'division outside p ideal')
    return tuple(x//p % p for x in value)


def deriv(a):
    return [i*a[i] for i in range(1, len(a))]


def legendre_square_coefficients(m):
    # Rodrigues closed form for P_{2m}(T)=Q_m(T^2), not H_m reflected.
    result = [R(0)]*(m+1)
    for j in range(m+1):
        result[m-j] = R((-1)**j*factorial(4*m-2*j),
                        2**(2*m)*factorial(j)*factorial(2*m-j)*factorial(2*m-2*j))
    return result


def precision_functions():
    src = ROOT/'frozen-inputs'/'REUSED_PRECISION_SOURCE.py'
    b = src.read_bytes()
    require(sha256(b).hexdigest() == 'd8a19c7e4a319b5e9b17b66a1b5ef4ac563bd984815c7355bd73784e0bc521d8', 'precision pin')
    names = {'_require_natural', '_require_positive', 'precision_ratio',
             'project_precision', 'precision_detail', 'recompose_precision'}
    defs = [x for x in ast.parse(b.decode()).body if isinstance(x, ast.FunctionDef) and x.name in names]
    require({x.name for x in defs} == names, 'precision dependencies')
    env = {}
    exec(compile(ast.Module(body=defs, type_ignores=[]), str(src), 'exec'), env)
    return env


def symbolic_ode():
    x = sy.symbols('x')
    q = 4*x*(1-x)
    residuals = [sy.expand(x*(1-x)*sy.diff(q,x)**2-4*q*(1-q)),
                 sy.expand(x*(1-x)*sy.diff(q,x,2)+(1-2*x)*sy.diff(q,x)-4*(1-sy.Rational(3,2)*q)),
                 -sy.Rational(2,9)+4*sy.Rational(1,18)]
    require(residuals == [0, 0, 0], 'ODE chain coefficients')
    n = sy.symbols('n')
    # x(1-x)Y''+(1-2x)Y'-(2/9)Y: coefficient x^n.
    outgoing = (n+1)*n+(n+1)
    incoming = n*(n-1)+2*n+sy.Rational(2,9)
    require(sy.expand(outgoing-(n+1)**2) == 0, 'ODE outgoing')
    require(sy.expand(incoming-(n+sy.Rational(1,3))*(n+sy.Rational(2,3))) == 0, 'ODE incoming')
    return {'three_chain_rule_residuals': list(map(str,residuals)), 'recurrence_residuals': ['0','0'],
            'analytic_proof_scope': 'Q[[x]], no reduction of n>=p infinite tails'}


def check(p, precision):
    require(p % 6 == 1, 'prime class')
    m = (p-1)//6
    a, b = arrays(p)
    va = [valuation(c,p) for c in a]
    vb = [valuation(c,p) for c in b]
    require(va == [int(n>m)+int(n>2*m) for n in range(p)], 'Gauss valuation entries')
    require(vb == [int(n>2*m)+int(n>4*m) for n in range(p)], 'Hesse valuation entries')
    composed = substitute(a,[R(0),R(4),R(-4)])
    require(composed[:p] == b, 'characteristic zero low coefficients')
    delta = [composed[k]-(b[k] if k<p else 0) for k in range(2*p-1)]
    require(all(residue(c,p*p)==0 for c in delta), 'Q2 entire coefficients')
    require(valuation(delta[-1],p)==2, 'p3 sharp global top coefficient')
    require(all(residue(c,p*p)==0 for c in deriv(delta)), 'coefficient derivative')
    reflected = substitute(b,[R(1),R(-1)])
    require(all(residue(c-d,p*p)==0 for c,d in zip(reflected,b)), 'reflection')

    qpoly = legendre_square_coefficients(m)
    hpoly = [R(comb(m,k)*comb(2*m,k)) for k in range(m+1)]
    qref = substitute(qpoly,[R(1),R(-1)])
    require(all(residue(c-d,p)==0 for c,d in zip(qref,hpoly)), 'inherited Q variable against Rodrigues')
    require(all(residue(a[n]-(hpoly[n] if n<=m else 0),p)==0 for n in range(p)), 'finite Gauss to inherited H')
    fp = sum(c*R(1,2)**n for n,c in enumerate(deriv(a)))
    qp = sum(c*R(1,2)**n for n,c in enumerate(deriv(qpoly)))
    require(residue(fp+qp,p)==0, 'inherited fprime=-Qprime')
    g = sum(c*R(1,2)**n for n,c in enumerate(a))
    # Independent B recurrence check against exact Task recurrence.
    B = [c*R(1,2)**n for n,c in enumerate(a)]
    require(B[0]==1 and all(B[n+1]/B[n] == R((6*n+1)*(3*n+1),36*(n+1)**2) for n in range(p-1)), 'Task rational half')

    mod = p*p
    xplus = (residue(R(1,2),mod),residue(R(1,4),mod))
    xminus = (xplus[0],-xplus[1] % mod)
    require(pair_sub((1,0),xplus,mod)==xminus, 'exact reflected lift')
    require(pair_mul((4,0),pair_mul(xplus,xminus,mod),mod)==(residue(R(1,2),mod),0), 'exact Task fiber lift')
    values = [evaluate_pair(b,x,mod) for x in (xplus,xminus)]
    slopes = [evaluate_pair(deriv(b),x,mod) for x in (xplus,xminus)]
    jacobians = [(0,-2 % mod),(0,2)]
    require(values==[(residue(g,mod),0)]*2,'exact lift value')
    require(slopes==[pair_mul(q,(residue(fp,mod),0),mod) for q in jacobians], 'oriented derivative')
    require(slopes[1]==(slopes[0][0],-slopes[0][1] % mod), 'sigma derivative')
    require(tuple((slopes[0][i]+slopes[1][i]) % mod for i in range(2))==(0,0), 'opposite derivative')
    out = {'p':p,'coefficient_count':2*p-1,'low_coefficients_exact':True,'Q2_all_coefficients':True,
           'valuation_entries':{'a':va,'b':vb},'top_coefficient_mod_p3':residue(delta[-1],p**3),
           'Q_variable_and_derivative_sign_verified':True,'fprime_half_mod_p':residue(fp,p),
           'Qprime_half_mod_p':residue(qp,p),'g_mod_p2':residue(g,mod),'branch_values_mod_p2':values,
           'branch_derivatives_mod_p2':slopes,'branch_map_derivatives_mod_p2':jacobians}
    if p % 24 in (13,19):
        require(residue(g,p)==0,'inherited CM0 finite corroboration')
        require(residue(fp,p)!=0,'inherited SIMPLE finite corroboration')
        digit=residue(g/p,p)
        require(quotient_digit(values[0],p)==quotient_digit(values[1],p)==(digit,0),'divided digit')
        shifted=sum(c*(R(1,2)+p)**n for n,c in enumerate(a))
        shifted_digit=residue(shifted/p,p)
        require(shifted_digit==(digit+residue(fp,p)) % p,'Task shift')
        # A non-rational branch shift tests both coordinates, epsilon=1+s.
        shifted_x=((xplus[0]+p) % mod,(xplus[1]+p) % mod)
        shifted_h=quotient_digit(evaluate_pair(b,shifted_x,mod),p)
        tangent=pair_mul((1,1),tuple(t % p for t in slopes[0]),p)
        require(shifted_h==((digit+tangent[0]) % p,tangent[1]), 'Hesse nonrational lift shift')
        represent=residue(g,mod)
        require(precision['project_precision'](represent,p,mod)==digit,'Source projection application')
        require(precision['precision_detail'](represent,p,mod)==0,'Source detail application')
        require(precision['recompose_precision'](digit,0,p,mod)==represent,'Source recomposition application')
        out.update({'first_divided_digit_mod_p':digit,'rational_shift_digit':shifted_digit,
                    'nonrational_Hesse_shift_epsilon':[1,1],'nonrational_Hesse_shift_digit':shifted_h})
    return out


def negatives():
    a,b=arrays(5);composed=substitute(a,[R(0),R(4),R(-4)])
    p5=[(k,residue(c-(b[k] if k<5 else 0),25)) for k,c in enumerate(composed)
        if residue(c-(b[k] if k<5 else 0),25)]
    require(p5==[(5,3),(6,9),(7,20),(8,20)], 'excluded p5 negative')
    a,b=arrays(13);mod=169;x=(residue(R(1,2),mod),residue(R(1,4),mod))
    literal=(1,0)
    for _ in range(13):
        literal=pair_mul(literal,x,mod)
    conjugate=(x[0],-x[1] % mod)
    difference=pair_sub(literal,conjugate,mod)
    require(difference==(13,78), 'literal x^p versus sigma')
    literal_digit=quotient_digit(evaluate_pair(b,literal,mod),13)
    require(literal_digit==(9,2),'literal powering wrong divided digit')
    mod3=13**3;x3=(residue(R(1,2),mod3),residue(R(1,4),mod3))
    g=sum(c*R(1,2)**n for n,c in enumerate(a))
    difference3=pair_sub(evaluate_pair(b,x3,mod3),(residue(g,mod3),0),mod3)
    require(difference3==(507,1690),'p13 pointwise p3 counterexample')
    return {'excluded_p5_coefficients_mod25':p5,'p13_literal_p_power_minus_sigma_mod169':difference,
            'p13_literal_p_power_Hesse_divided_digit':literal_digit,
            'p13_L_Hesse_minus_g_half_mod2197':difference3,'p13_divided_second_digit_difference_mod169':[39,130]}


def main():
    symbolic=symbolic_ode();precision=precision_functions()
    cases=[check(p,precision) for p in SELECTED]
    evidence=json.loads((ROOT/'frozen-inputs'/'QUADRATIC_EXACT_REGRESSION_RESULTS.json').read_text())
    by_p={r['p']:r for r in evidence['cases']}
    compare=['g_mod_p2','branch_values_mod_p2','branch_derivatives_mod_p2','branch_map_derivatives_mod_p2']
    for c in cases:
        for key in compare:
            require(json.loads(json.dumps(c[key]))==by_p[c['p']][key],f'author selected evidence match: {key}')
        require(c['top_coefficient_mod_p3']==by_p[c['p']]['highest_coefficient_mod_p3_nonzero'],'author top evidence')
        if 'first_divided_digit_mod_p' in c:
            require(c['first_divided_digit_mod_p']==by_p[c['p']]['first_divided_digit_mod_p'],'author digit evidence')
            require(c['rational_shift_digit']==by_p[c['p']]['rational_shift']['digit_at_rational_half_plus_p'],'author shift evidence')
    result={'status':'BOUNDED_INDEPENDENT_REPRODUCTION_PASS','selected_primes':SELECTED,
            'not_prior_77_prime_regression':True,'author_checker_imported_or_executed':False,
            'symbolic_ode':symbolic,'cases':cases,'negative_precision_evidence':negatives(),
            'five_selected_author_evidence_rows_match':True,'formal_DR':False,
            'UR_proved':False,'LIFT_proved':False,'period_normal_identified':False}
    (ROOT/'INDEPENDENT_REPRODUCTION_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'cases'},indent=2))


if __name__=='__main__':
    main()
