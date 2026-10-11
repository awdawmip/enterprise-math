"""Frozen task-local candidate; run only after own current execution-open.

Finite p^3 regression, not an all-prime proof or UR/LIFT acceptance.
All formulas are frozen before comparison. No provider/network/Task mutation.
Outputs are confined to this new author's directory.
"""
from __future__ import annotations

import ast
from hashlib import sha256
import json
from math import comb, factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PRIMES = [7, 13, 19, 31, 37, 43]
TASK_ID = 'RS-ENTERPRISE-CM24-HESSE-INHOMOGENEOUS-P3-TRANSPORT'


def inv(n, modulus):
    return pow(n, -1, modulus)


def coefficient_array(a_num, a_den, b_num, b_den, p, modulus):
    a = a_num * inv(a_den, modulus) % modulus
    b = b_num * inv(b_den, modulus) % modulus
    out = [1]
    for n in range(p - 1):
        out.append(out[-1] * (a+n) * (b+n) * inv((n+1)**2, modulus) % modulus)
    return out


def beta_seed(p):
    m = (p-1)//6
    seed = 0
    for n in range(3*m+1, p):
        an = (-1)**(3*m) * factorial(m) * factorial(2*m)
        an *= factorial(n-1-m) * factorial(n-1-2*m)
        an = an * inv(18*factorial(n)**2, p) % p
        seed += an * pow(4, n, p) * (-1)**(p-n) * comb(n, p-n)
    return seed % p


def harmonic_seed(p):
    m, mod2 = (p-1)//6, p*p
    q2 = ((pow(2, p-1, p**3)-1)//p) % mod2
    s2 = sum(inv(6*k+2, mod2) for k in range(m)) % mod2
    divided_numerator = (-3*s2-q2) % mod2
    assert divided_numerator % p == 0
    first = divided_numerator // p
    ts = {r: sum(inv((6*k+r)**2, p) for k in range(m)) % p for r in (2,3,6)}
    result = first + q2*q2*inv(2,p) - 3*ts[6] + 12*ts[3] + 33*inv(2,p)*ts[2]
    result = 2*inv(9,p)*result % p
    return result, {'q2_mod_p2': q2, 'S2_mod_p2': s2,
                    'divided_minus_3S2_minus_q2_mod_p': first,
                    'T2_T3_T6_mod_p': ts}


def carrier(p, seed):
    j = [seed]
    for n in range(p-2):
        c = (n+inv(3,p))*(n+2*inv(3,p)) % p
        j.append((c*j[-1]-2*inv(9,p))*inv((n+1)**2,p) % p)
    assert len(j) == p-1
    return j


def compose_q(a, modulus):
    out = [0]*(2*len(a)-1)
    for n,c in enumerate(a):
        for r in range(n+1):
            out[n+r] = (out[n+r]+c*pow(4,n,modulus)*(-1)**r*comb(n,r)) % modulus
    return out


def derivative(a):
    return [n*a[n] for n in range(1,len(a))]


def mul(a,b,modulus):
    return ((a[0]*b[0]+2*a[1]*b[1]) % modulus,
            (a[0]*b[1]+a[1]*b[0]) % modulus)


def add(a,b,modulus):
    return ((a[0]+b[0]) % modulus,(a[1]+b[1]) % modulus)


def scale(c,a,modulus):
    return (c*a[0] % modulus,c*a[1] % modulus)


def minus(a,b,modulus):
    return ((a[0]-b[0]) % modulus,(a[1]-b[1]) % modulus)


def evaluate(a,x,modulus):
    out=(0,0)
    for c in reversed(a):
        out=add(mul(out,x,modulus),(c % modulus,0),modulus)
    return out


def power(x,n,modulus):
    out=(1,0)
    while n:
        if n & 1:
            out=mul(out,x,modulus)
        x=mul(x,x,modulus);n >>= 1
    return out


def load_reused_precision():
    raw=(ROOT/'frozen-inputs/REUSED_PRECISION_SOURCE.py').read_bytes()
    assert sha256(raw).hexdigest() == 'd8a19c7e4a319b5e9b17b66a1b5ef4ac563bd984815c7355bd73784e0bc521d8'
    names={'_require_natural','_require_positive','precision_ratio',
           'project_precision','precision_detail','recompose_precision'}
    nodes=[n for n in ast.parse(raw.decode()).body if isinstance(n,ast.FunctionDef) and n.name in names]
    assert {n.name for n in nodes} == names
    scope={}
    exec(compile(ast.Module(body=nodes,type_ignores=[]),'unchanged Source precision functions','exec'),scope)
    return scope


def divide_p(value,p,precision):
    assert all(c % p == 0 for c in value)
    out=tuple(precision['project_precision'](c,p*p,p**3) for c in value)
    assert all(precision['precision_detail'](c,p*p,p**3)==0 for c in value)
    assert tuple(precision['recompose_precision'](c,0,p*p,p**3) for c in out)==value
    return out


def check_prime(p,precision):
    assert p >= 7 and p % 6 == 1
    m,mod3=(p-1)//6,p**3
    # Independent candidates are computed before either Task value is read.
    seed_beta=beta_seed(p)
    seed_harmonic,harmonic_data=harmonic_seed(p)
    assert seed_beta==seed_harmonic
    j=carrier(p,seed_harmonic)
    particular=carrier(p,0)
    a=coefficient_array(1,6,1,3,p,mod3)
    b=coefficient_array(1,3,2,3,p,mod3)
    hasse=[c % p for c in b]
    assert all(c==0 for c in hasse[2*m+1:])
    padded_hasse=hasse[:p-1]
    assert all((u-v-seed_harmonic*h) % p == 0 for u,v,h in zip(j,particular,padded_hasse))
    composed=compose_q(a,mod3)
    padded_b=b+[0]*(p-1)
    delta=[(u-v) % mod3 for u,v in zip(composed,padded_b)]
    correction=[0]*p+[p*p*c for c in j]
    assert len(correction)==len(delta)
    assert all((c-d) % mod3 == 0 for c,d in zip(delta,correction))
    zero_seed_global_failures=[n for n,c in enumerate(delta)
                             if (c-(p*p*particular[n-p] if n>=p else 0)) % mod3]
    inv3=inv(3,p)
    residuals=[]
    for n in range(p-1):
        next_j=j[n+1] if n+1<len(j) else 0
        residual=((n+1)**2*next_j-(n+inv3)*(n+2*inv3)*j[n]+2*inv(9,p)) % p
        assert residual==0
        residuals.append(residual)
    assert j[-1] == inv(10,p)
    assert a[-1] % (p*p)==b[-1] % (p*p)==0
    assert (a[-1]//(p*p)) % p==inv(10,p)
    assert (b[-1]//(p*p)) % p==1
    half=(inv(2,mod3),0)
    g=evaluate(a,half,mod3)
    fp=evaluate(derivative(a),half,mod3)
    target=p % 24 in (13,19)
    branches=[]
    for sign in (1,-1):
        x=(inv(2,mod3),sign*inv(4,mod3) % mod3)
        assert scale(4,mul(x,minus((1,0),x,mod3),mod3),mod3)==half
        xmod=(x[0] % p,x[1] % p)
        xp=power(xmod,p,p)
        jvalue=evaluate(j,xmod,p)
        particular_value=evaluate(particular,xmod,p)
        hv=evaluate(hasse,xmod,p)
        lx=evaluate(b,x,mod3)
        correction_value=mul(xp,jvalue,p)
        corrected=add(lx,scale(p*p,correction_value,mod3),mod3)
        assert corrected==g
        lp=evaluate(derivative(b),x,mod3)
        qprime=scale(4,minus((1,0),scale(2,x,mod3),mod3),mod3)
        jslope=evaluate(derivative(j),xmod,p)
        corrected_slope=add(lp,scale(p*p,mul(xp,jslope,p),mod3),mod3)
        assert corrected_slope==mul(qprime,fp,mod3)
        particular_slope=evaluate(derivative(particular),xmod,p)
        naive_slope=add(lp,scale(p*p,mul(xp,particular_slope,p),mod3),mod3)
        naive_derivative_error=minus(mul(qprime,fp,mod3),naive_slope,mod3)
        divided=None
        if target:
            assert g[0] % p==0 and hv==(0,0)
            assert jvalue==particular_value
            assert xp==(x[0] % p,-x[1] % p)
            gd=divide_p(g,p,precision)
            ld=divide_p(lx,p,precision)
            predicted=add(ld,scale(p,mul(xp,particular_value,p),p*p),p*p)
            assert gd==predicted
            divided={'Gauss_divided_mod_p2':gd,'Hesse_uncorrected_divided_mod_p2':ld,
                     'particular_correction_mod_p':mul(xp,particular_value,p),
                     'Hesse_corrected_divided_mod_p2':predicted}
        branches.append({'sign':sign,'x_mod_p3':x,'uncorrected_Hesse_minus_Gauss_mod_p3':minus(lx,g,mod3),
                         'x_power_p_mod_p':xp,'Hasse_value_mod_p':hv,'full_J_value_mod_p':jvalue,
                         'zero_seed_particular_value_mod_p':particular_value,
                         'full_seed_derivative_transport':True,'zero_seed_derivative_error_mod_p3':naive_derivative_error,
                         'second_digit':divided})
    if p==13:
        assert branches[0]['uncorrected_Hesse_minus_Gauss_mod_p3']==(507,1690)
        assert branches[0]['second_digit']['Gauss_divided_mod_p2'] != branches[0]['second_digit']['Hesse_uncorrected_divided_mod_p2']
    return {'p':p,'m':m,'p_mod_24':p % 24,'target':target,
            'beta_seed_mod_p':seed_beta,'harmonic_seed_mod_p':seed_harmonic,
            'harmonic_input':harmonic_data,'full_J_coefficients_mod_p':j,
            'zero_seed_particular_coefficients_mod_p':particular,
            'full_coefficientwise_p3_correction':True,'endpoint_residual':residuals[-1],
            'factor_entry_residuals':{str(n):residuals[n] for n in (2*m,4*m)},
            'zero_seed_polynomial_failure_degrees':zero_seed_global_failures,
            'branches':branches}


def main():
    binding=json.loads((ROOT/'OWN_CURRENT_EXECUTION_BINDING.json').read_text())
    assert binding['task_id']==TASK_ID and binding['own_authorized_open'] is True
    assert binding['current_session_id'] and binding['current_claim_id'] and binding['run_id']
    precision=load_reused_precision()
    cases=[check_prime(p,precision) for p in PRIMES]
    out={'status':'PASS','scope':'SIX_SELECTED_PRIMES_NEW_P3_CARRIER_REGRESSION_NOT_UR_LIFT_PROOF',
         'task_id':TASK_ID,'binding':binding,'cases':cases,'provider_calls':0,
         'UR_proved':False,'LIFT_proved':False,'period_normal_identified':False,
         'general_tool_family_created':False,'shared_nonblind_context':True}
    (ROOT/'HESSE_P3_EXACT_REGRESSION_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'primes':PRIMES,
                      'target_cases':[r['p'] for r in cases if r['target']],
                      'harmonic_seeds':{r['p']:r['harmonic_seed_mod_p'] for r in cases}},indent=2))


if __name__=='__main__':
    main()
