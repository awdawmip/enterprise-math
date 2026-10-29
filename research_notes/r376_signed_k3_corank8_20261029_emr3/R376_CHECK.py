#!/usr/bin/env python3
"""R376: exact eighth-corank PF2 phase of a signed BRC K3 deformation.

Run from Enterprise Math PR #1592 checkout:
    python research_notes/r376_signed_k3_corank8_20261029_emr3/R376_CHECK.py
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
    """Seventeen raw-D minor observations, differences j=0..16.

    r=8: highest B index 44; highest t degree 26.
    Coefficient arrays retain the full signed K/J polynomial algebra.
    """
    S, P = 44, 26
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
    for v in range(17):
        k = v+1
        q = 8+k
        minor = add(multiply(D(q,k),D(q+1,k+1)),
                    scale(multiply(D(q,k+1),D(q+1,k)),-1))
        observations.append(scale(minor,Fraction(5)**(15-2*k)))
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
    import hashlib
    c=row_coefficients()
    assert len(c)==17
    T=[expand(c[j]**2-c[j-1]*c[j+1]) for j in range(1,16)]
    C=[Poly(z,theta,domain='ZZ') for z in c]
    U=[Poly(z,theta,domain='ZZ') for z in T]
    a,b=Rational(183,100),Rational(1831,1000)
    q,d,e=Rational(37,20),Rational(2),Rational(5,2)
    root_counts=[]
    for label,arr in [('c',C),('T',U)]:
        for idx,p in enumerate(arr):
            count=int(p.count_roots(-1,b))
            expected=int(label=='T' and idx==8)
            assert count==expected and p.eval(-1)>0 and p.eval(0)>0
            assert p.eval(b)<0 if expected else p.eval(b)>0
            root_counts.append((label,idx+1 if label=='T' else idx,count))
    assert U[8].eval(a)>0>U[8].eval(b)
    # Four rigorously overlapping exclusion intervals cover every theta>eta8.
    witnesses=[('T9',U[8],-1,q,q,1),('T3',U[2],q,d,d,0),
               ('c3',C[3],d,e,d,0),('c0',C[0],e,oo,e,0)]
    covering=[]
    for name,p,left,right,point,expected in witnesses:
        count=int(p.count_roots(left,right))
        assert count==expected and p.eval(point)<0,(name,count)
        covering.append((name,str(left),str(right),count))
    at=Rational(15,8)
    assert [j for j,p in enumerate(C) if p.eval(at)==0]==list(range(9,17))
    assert all(p.eval(at)>0 for p in C[:9]) and U[2].eval(at)<0
    assert c[-1]==expand(1430*(30-16*theta)**16)
    # Independent exact rational cross-check via the prior R369 B->L->Q path.
    sys.path.insert(0,str(HERE.parent/'r369_signed_k3_branch_top_catalan_20261029_emr3'))
    from R369_check import compute_rows
    for t in (Rational(-1,2),Rational(0),Rational(1)):
        rows,_=compute_rows(t,8)
        assert all(rows[8][j]==C[j].eval(t) for j in range(17))
    coefficients=[[str(v) for v in p.all_coeffs()] for p in C]
    turans=[[str(v) for v in p.all_coeffs()] for p in U]
    serial=json.dumps({'C':coefficients,'T':turans},separators=(',',':'))
    digest=hashlib.sha256(serial.encode()).hexdigest()
    assert digest=='1641424c4da68106c12a5b49c8d81faac5742a4d8c7f8eb8bc13a5532ed7a54a'
    left,right=U[8].refine_root(a,b,eps=Rational(1,10**28))
    result={'schema':'R376_CORANK8_EXACT_V1','status':'R376_EXACT_PASS',
        'theorem':'PF2 iff -1<theta<=unique root eta8 of T9 in (183/100,1831/1000)',
        'eta8_refined':[str(left),str(right)],'root_counts':root_counts,
        'exclusion_cover':covering,'independent_exact_equalities':51,
        'c_polynomials_descending':coefficients,'T_polynomials_descending':turans,
        'C_T_sha256':digest,'model':'signed original R346 K/J, K3[t^2]=-8(1+theta)',
        'scope':'finite 17 raw-D Newton observations; no native X6 or R363 assumption'}
    (HERE/'R376_EVIDENCE.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print('R376_EXACT_PASS','eta8≈',((left+right)/2).evalf(25),
          'Sturm_polynomials',len(root_counts),'negative_cover',len(covering),
          'independent_equalities',51,'C_T_digest',digest)
    return result

if __name__=='__main__':verify()
