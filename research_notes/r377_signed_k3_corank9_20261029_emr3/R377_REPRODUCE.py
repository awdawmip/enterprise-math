#!/usr/bin/env python3
"""R377: exact ninth-corank PF2 phase of a signed BRC K3 deformation.

Run from Enterprise Math PR #1592 checkout:
    python research_notes/r377_signed_k3_corank9_20261029_emr3/R377_REPRODUCE.py
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
    """Nineteen raw-D minor observations, differences j=0..18.

    r=9: highest B index 49; highest t degree 29.
    Coefficient arrays retain the full signed K/J polynomial algebra.
    """
    S, P = 49, 29
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
    for v in range(19):
        k = v+1
        q = 9+k
        minor = add(multiply(D(q,k),D(q+1,k+1)),
                    scale(multiply(D(q,k+1),D(q+1,k)),-1))
        observations.append(scale(minor,Fraction(5)**(17-2*k)))
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
    """Complete rational Bernstein phase proof and independent checks, r=9."""
    import hashlib
    c = row_coefficients()
    assert len(c)==19
    C=[Poly(z,theta,domain='ZZ') for z in c]
    T=[Poly(C[j].as_expr()**2-C[j-1].as_expr()*C[j+1].as_expr(),theta,domain='ZZ') for j in range(1,18)]
    assert len(T)==17
    cp=[[str(x) for x in p.all_coeffs()] for p in C]
    tp=[[str(x) for x in p.all_coeffs()] for p in T]
    serial=json.dumps({'c':cp,'T':tp},separators=(',',':'))
    digest=hashlib.sha256(serial.encode()).hexdigest()
    assert digest=='aeddee2458ba0352f5f3c23cd4bb0a80ca631d7bb72dbdad5122f421279806f7'
    left=Rational(-1); m=Rational(183,100)
    a=Rational(1831256,1000000); b=Rational(1831257,1000000)
    u=Rational(37,20); v=Rational(203,100); w=Rational(5,2)
    checks=[]; count=0
    def cert(p,l,r,label):
        nonlocal count
        coeffs=bernstein_coefficients(p,l,r)
        assert all(q>0 for q in coeffs), (label,l,r)
        count+=len(coeffs)
        checks.append([label,str(l),str(r),len(coeffs)])
    for j,p in enumerate(C):cert(p,left,m,'c'+str(j))
    for j,p in enumerate(T,1):cert(p,left,m,'T'+str(j))
    for j,p in enumerate(C):cert(p,m,b,'c'+str(j))
    for j,p in enumerate(T,1):
        cert(p,m,a if j==9 else b,'T'+str(j))
    assert T[8].eval(a)>0>T[8].eval(b)
    deriv=Poly(-diff(T[8].as_expr(),theta),theta,domain='ZZ')
    cert(deriv,a,b,'-T9_prime')
    cert(-T[8],b,u,'-T9')
    cert(-C[9],u,v,'-c9')
    cert(-C[5],v,w,'-c5')
    shifted=Poly((-C[0].as_expr()).subs(theta,theta+w),theta,domain='QQ')
    assert len(shifted.all_coeffs())==7 and all(z>0 for z in shifted.all_coeffs())
    count+=len(shifted.all_coeffs())
    assert expand(C[18].as_expr()-4862*(30-16*theta)**18)==0
    sys.path.insert(0,str(HERE.parent/'r369_signed_k3_branch_top_catalan_20261029_emr3'))
    from R369_check import compute_rows
    for t in (Rational(-1,2),Rational(0),Rational(1)):
        rows,_=compute_rows(t,9)
        assert len(rows[9])==19
        assert all(rows[9][j]==C[j].eval(t) for j in range(19))
    assert len(checks)==76 and count==1846
    result={'schema':'R377_SIGNED_K3_CORANK9_EXACT_V1','status':'R377_EXACT_PASS',
        'theorem':'PF2 iff -1<theta<=unique T9 root eta9 in (1831256/1000000,1831257/1000000)',
        'model':'R346 original signed twelve K/J branches; K3[t2]=-8(1+theta)',
        'r':9,'coefficient_count':19,'turan_count':17,
        'eta9_bracket':[str(a),str(b)],
        'root_signs':[str(T[8].eval(a)),str(T[8].eval(b))],
        'interval_checks':checks,'strict_bernstein_and_tail_coefficients':count,
        'tail_shift_positive_coeffs_desc':[str(z) for z in shifted.all_coeffs()],
        'independent_r369_three_point_equalities':57,'C_T_sha256':digest,
        'C_polynomials_descending':cp,'T_polynomials_descending':tp,
        'scope':'finite 19 raw-D Newton observations; author-side; not native X6; no R363 assumption'}
    (HERE/'R377_EVIDENCE.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print('R377_EXACT_PASS','eta9≈1.83125667371567','sign_checks',count,'independent',57,'digest',digest)
    return result

if __name__=='__main__':verify()
