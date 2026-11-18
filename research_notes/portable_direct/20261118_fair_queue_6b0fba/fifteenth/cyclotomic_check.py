"""Exact spectral checks and a pinned positive-BRC port replay. Python 3 + SymPy.

Run from a checkout: python cyclotomic_check.py --repo /path/to/enterprise-math
Output is deterministic JSON on stdout (no files are downloaded).
"""
import argparse
import hashlib
import json
import sys
from collections import Counter
from dataclasses import asdict
from functools import cache
from math import gcd, lcm
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

x = sp.Symbol("x")
def pol(expr):
    return sp.Poly(expr, x, domain=sp.ZZ)

X = pol(x)
ONE = pol(1)
TWO = pol(2)
R2 = 4 * X - X**2

@cache
def dirichlet(n):
    if n == 0:
        return ONE
    if n == 1:
        return X - 2
    return (X - 2) * dirichlet(n - 1) - dirichlet(n - 2)

@cache
def oriented(d):
    product = ONE
    for k in sp.divisors(d):
        if 1 < k < d:
            product *= oriented(int(k))
    return dirichlet(d - 1).exquo(product)

@cache
def omega(d):
    # Invert the native complement substitution by leading-term subtraction.
    p = oriented(d)
    h = p.degree() // 2
    rem = (-1)**h * p
    coeffs = []
    for j in range(h, -1, -1):
        c = rem.nth(2*j) * (-1)**j
        rem -= c * R2**j
        coeffs.append(c)
    assert rem.is_zero
    return sp.Poly.from_list(coeffs, x, domain=sp.ZZ)

@cache
def dickson(n):
    if n == 0:
        return TWO
    if n == 1:
        return X
    return X*dickson(n-1) - dickson(n-2)

def from_cyclotomic(d):
    p = pol(sp.cyclotomic_poly(d, x))
    h = p.degree()//2
    assert all(p.nth(k) == p.nth(2*h-k) for k in range(h))
    q = p.nth(h)*ONE
    for j in range(1,h+1):
        q += p.nth(h+j)*dickson(j)
    return (-1)**h*q.compose(2-X)

def is_prime_power(n):
    fs = sp.factorint(n)
    return int(next(iter(fs))) if len(fs) == 1 else 1

def trace_vector(p):
    h = p.degree()
    trace = [h]
    for j in range(1,h):
        trace.append(-j*p.nth(h-j) - sum(p.nth(h-k)*trace[j-k] for k in range(1,j)))
    return trace

def traces(p,d):
    h = p.degree()
    trace = trace_vector(p)
    alpha_x = 2-X
    prev, cur = TWO, alpha_x
    for n in range(2*d+1):
        r = prev.rem(p)
        actual = sum(r.nth(j)*trace[j] for j in range(h))
        arithmetic = sum(k*sp.mobius(d//k) for k in sp.divisors(gcd(d,n)))
        assert actual == arithmetic
        prev, cur = cur, (alpha_x*cur - prev).rem(p)
    return 2*d+1

def odd_sheet_smith(d,p):
    h = p.degree()
    a,b=ONE,ONE
    cols=[]
    for _ in range(2*h):
        cols.append([a.nth(j) for j in range(h)]+[b.nth(j) for j in range(h)])
        a = (a*X).rem(p)
        b = (b*(4-X)).rem(p)
    M = sp.Matrix(cols).T
    S = smith_normal_form(M, domain=sp.ZZ)
    diag = [abs(int(S[j,j])) for j in range(2*h)]
    assert diag == [1]*h + [2]*h
    return diag

def arithmetical_checks():
    stats=Counter()
    examples = {}
    for d in range(3,49):
        p=omega(d)
        h=p.degree()
        assert p == from_cyclotomic(d)
        assert abs(p.eval(0)) == is_prime_power(d)
        midpoint = is_prime_power(d//2) if d%2==0 else 1
        assert p.eval(4) == midpoint
        D=int(p.discriminant())
        D_or=int(oriented(d).discriminant())
        assert D_or == 4**h*midpoint*D**2
        if d%2:
            other=from_cyclotomic(2*d)
            assert other == (-1)**h * p.compose(4-X)
            assert p*other == oriented(d)
            assert abs(p.resultant(other))==2**h
            if d<=31:
                odd_sheet_smith(d,p)
                stats['odd_orders_smith_normal_forms']+=1
        else:
            assert from_cyclotomic(2*d)==oriented(d)
            assert D_or // D**2 == 4**h*midpoint
        # In z (not y=z^2), factor by an independent Q-polynomial routine.
        theta=sum(p.nth(j)*4**j*x**(2*j)*(1+x**2)**(h-j) for j in range(h+1))
        factors = pol(theta).factor_list()[1]
        degs=sorted(int(f.degree()) for f,m in factors for _ in range(m))
        expected_degree = int(sp.totient(lcm(d,4)))//2
        assert degs == [expected_degree]*(2*h//expected_degree)
        stats['chart_irreducible_factors'] += len(degs)
        stats['ramanujan_trace_comparisons'] += traces(p,d)
        for j in range(d):
            ok=all((r+j)%d in {(-r+j)%d,(r-j)%d} for r in range(d))
            assert ok == (2*j%d==0)
            stats['all_input_shift_descent_tests'] += 1
        if d in (3,4,5,6,8,10,12,15,18,20,30):
            examples[str(d)]={'omega_descending':list(map(int,p.all_coeffs())),
                'midpoint':midpoint,'disc_field':D,'norm_relative_disc_or_gluing':4**h*midpoint,
                'oriented_chart_irreducible_degrees':degs}
        stats['dirichlet_vs_cyclotomic']+=1
    return dict(stats),examples

def positive_brc(repo):
    kernel=repo/'src'/'enterprise_math'/'brc_weighted.py'
    sha=hashlib.sha256(kernel.read_bytes()).hexdigest()
    assert sha=='4f3e356227a1c964d33a3ddae94922463ba28097a43b8d1b8f6cd9ca5615fc9f'
    sys.path.insert(0,str(repo/'src'))
    from enterprise_math import brc_weighted as brc
    from enterprise_math import exact_arithmetic as ar
    sha_ar=hashlib.sha256(Path(ar.__file__).read_bytes()).hexdigest()
    assert sha_ar=="f4f8feead82dc53a35e5fec495b31e46e64820f7b115c9efd6034063e68f8ad6"
    assert Path(brc.__file__).resolve() == kernel.resolve()
    unit=brc.cwm_edge(1)
    # All four named ports are retained. Each branch leaves its port in place
    # or goes round the labeled cycle in the stated direction.
    def run(steps):
        states={0:unit}
        for sign in steps:
            new={}
            for j,value in states.items():
                for dest in (j,({1:(1,2,3,0), -1:(3,0,1,2)}[sign])[j]):
                    path=brc.cwm_propagate(value,unit)
                    new[dest]=brc.cwm_recoalesce(new.get(dest,brc.CWM_ZERO),path)
            states=new
        result=[]
        for j in range(4):
            s=states.get(j,brc.CWM_ZERO)
            assert s.total==s.count and s.dominant==int(s.live)
            result.append(s.count)
        return result
    rows={}
    for label,steps in [('plus',[1]),('minus',[-1]),('plus_then_plus',[1,1]),
                        ('minus_then_plus',[-1,1])]:
        counts=run(steps)
        a,b=counts[0]-counts[2],counts[1]-counts[3]
        num,den=4*b*b,a*a+b*b
        assert den>0 and num in (0,2*den,4*den)
        trace=ar.brc_evaluate_division(ar.division(num,den))
        assert trace.remainder==0
        rows[label]={'named_ports_0_to_3':counts,'signed_pair':[a,b],
                     'division_trace':asdict(trace),'projective_readout':trace.quotient}
    assert [r['projective_readout'] for r in rows.values()]==[2,2,4,0]
    return {'revision':'c0f816e2ab6be0145a3edd1a77488bddfd42a2f6',
            'kernel_sha256':sha,'division_facade_sha256':sha_ar,
            'entrypoints':['cwm_edge','cwm_propagate','cwm_recoalesce','brc_evaluate_division'],
            'observer':'CWM positive mass at named ports, then signed differences',
            'outputs':rows}

if __name__=='__main__':
    cli=argparse.ArgumentParser()
    cli.add_argument('--repo',type=Path,default=Path.cwd())
    args=cli.parse_args()
    stats,examples=arithmetical_checks()
    print(json.dumps({'range':[3,48],'spectral_checks':stats,'examples':examples,
        'labeled_port_brc':positive_brc(args.repo.resolve())},indent=2,sort_keys=True))
