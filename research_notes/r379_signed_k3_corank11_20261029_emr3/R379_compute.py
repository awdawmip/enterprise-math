#!/usr/bin/env python3
"""R379: exact eleventh-corank PF2 phase of a signed BRC K3 deformation.

Run from Enterprise Math PR #1592 checkout:
    python research_notes/r379_signed_k3_corank11_20261029_emr3/R379_compute.py
Requires SymPy.  Derived solely from the original R346 signed twelve-term
K/J -> B -> D -> raw minors recurrence, without the R348/R363 all-index claim.
Exact interval signs use rational Bernstein coefficients, never sampling.
"""
from __future__ import annotations
import json
import sys
from fractions import Fraction
from math import comb
from pathlib import Path
from sympy import Poly, Rational, Symbol, binomial, diff, expand

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'r346_unbounded_interior_tp2_corank301_20261028_emr3'))
from R346_verify import K, J

theta = Symbol('theta')

def clean(values):
    z = list(values)
    while z and z[-1] == 0:
        z.pop()
    return tuple(z)

def add(a, b):
    return clean((a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b))))

def scale(a, q):
    return clean(v*q for v in a)

def multiply(a, b):
    if not a or not b:
        return ()
    out = [0]*(len(a) + len(b)-1)
    for i, va in enumerate(a):
        for j, vb in enumerate(b):
            out[i+j] += va*vb
    return clean(out)

def row_coefficients():
    """Twenty-three raw-D minor observations, differences j=0..22.

    r=11: highest B index 59; highest t degree 35.
    Coefficient arrays retain the full signed K/J polynomial algebra.
    """
    S, P = 59, 35
    signed_K = [None] + [
        [((int(value),) if value else ()) for value in K(i)[:P+1]]
        for i in range(1,13)
    ]
    assert signed_K[3][2] == (-8,)
    signed_K[3][2] = (-8, -8)
    B = [[() for _ in range(P+1)] for _ in range(S+1)]
    B[0][0] = B[0][1] = (1,)
    for s in range(1, S+1):
        for j, value in enumerate(J(s)[:P+1]):
            if value:
                B[s][j] = (int(value),)
        for i in range(1,min(s,12)+1):
            for j, value in enumerate(signed_K[i]):
                if not value:
                    continue
                for p in range(j,P+1):
                    if B[s-i][p-j]:
                        B[s][p] = add(B[s][p],multiply(value,B[s-i][p-j]))
    def D(q,k):
        result = ()
        for w in range(k+1):
            result = add(result,scale(B[q+w][q],
                        (-1)**(k-w)*comb(k,w)*2**(q-w)))
        return result
    observations = []
    for v in range(23):
        k = v+1
        q = 11+k
        minor = add(multiply(D(q,k),D(q+1,k+1)),
                    scale(multiply(D(q,k+1),D(q+1,k)),-1))
        observations.append(scale(minor,Fraction(5)**(21-2*k)))
    out = []
    while observations:
        out.append(expand(sum(Rational(z)*theta**i
                              for i,z in enumerate(observations[0]))))
        observations = [add(observations[i+1],scale(observations[i],-1))
                        for i in range(len(observations)-1)]
    return out



def bernstein_coefficients(polynomial, left, right):
    """Exact rational Bernstein coefficients on a closed rational interval."""
    left, right = Rational(left), Rational(right)
    assert left < right
    shifted = Poly(polynomial, theta, domain='QQ').shift(left)
    n = shifted.degree()
    powers = [v * (right-left)**i for i, v in
              enumerate(reversed(shifted.all_coeffs()))]
    return [sum(powers[i] * Rational(binomial(k, i), binomial(n, i))
                for i in range(k+1)) for k in range(n+1)]


from sympy import oo

def verify():
    import hashlib, json
    C=[Poly(z,theta,domain='ZZ') for z in row_coefficients()]
    T=[Poly(C[j].as_expr()**2-C[j-1].as_expr()*C[j+1].as_expr(),theta,domain='ZZ') for j in range(1,22)]
    assert len(C)==23 and len(T)==21
    cp=[[str(x) for x in p.all_coeffs()] for p in C]
    tp=[[str(x) for x in p.all_coeffs()] for p in T]
    serial=json.dumps({'c':cp,'T':tp},separators=(',',':'))
    digest=hashlib.sha256(serial.encode()).hexdigest()
    for v in (Rational(-1), Rational(0), Rational(1,2), Rational(9,10), Rational(1), Rational(3,2), Rational(2)):
        cvals=[p.eval(v) for p in C];tvals=[p.eval(v) for p in T]
        negc=[i for i,z in enumerate(cvals) if z<0]
        negt=[i+1 for i,z in enumerate(tvals) if z<0]
        zeros=[i for i,z in enumerate(cvals) if z==0]
        print('POINT',v,'cnegative',negc[:15], 'Tnegative',negt[:15], 'zeros',zeros, flush=True)
    assert expand(C[22].as_expr()-58786*(30-16*theta)**22)==0
    out={'schema':'EM_R379_CORANK11_RAW_SIGNED_K3_V1','r':11,'model':'original signed twelve-term BRC K/J, K3[t2]=-8(1+theta)',
         'c_desc':cp,'T_desc':tp,'joint_digest':digest,'scope':'finite 23 original D minor Newton observations, not Q infinite all-index'}
    HERE.joinpath('R379_COEFFICIENTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print('R379_SYMBOLIC_PASS','sha',digest,'c',len(C),'T',len(T), flush=True)
    return out
if __name__=='__main__':verify()
