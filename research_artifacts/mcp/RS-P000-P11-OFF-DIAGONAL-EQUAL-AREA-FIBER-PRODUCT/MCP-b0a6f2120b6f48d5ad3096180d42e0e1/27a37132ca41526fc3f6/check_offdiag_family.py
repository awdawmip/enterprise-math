#!/usr/bin/env python3
"""Exact regression for the P11 off-diagonal cut family. See CHECK_PLAN.md.

Finite checks are not a rank/infinitude/completeness proof. No floating point,
CAS rank, root census, or imported driver's derivation is used.
"""
from fractions import Fraction as F
from math import gcd, isqrt, lcm
import hashlib
import json
from pathlib import Path
import parent_checker as inherited

A, C = 1945, 265
P = (F(9), F(2112))


def on_curve(p):
    return p is None or p[1]**2 == p[0]*(p[0]-A)*(p[0]-C)


def add(p, q):
    assert on_curve(p) and on_curve(q)
    if p is None:
        return q
    if q is None:
        return p
    x, y = p
    z, v = q
    if x == z and y == -v:
        return None
    slope = ((3*x*x-2*(A+C)*x+A*C)/(2*y)
             if p == q else (v-y)/(z-x))
    X = slope*slope+(A+C)-x-z
    Y = -y+slope*(x-X)
    out = (X, Y)
    assert on_curve(out)
    return out


def mul(n, p):
    assert n >= 0
    r = None
    while n:
        if n & 1:
            r = add(r, p)
        p = add(p, p)
        n >>= 1
    return r


def qsqrt(q):
    q = F(q)
    assert q >= 0
    u, v = isqrt(q.numerator), isqrt(q.denominator)
    assert u*u == q.numerator and v*v == q.denominator, q
    return F(u, v)


def reconstruct(d, mu, nu):
    assert d > 0 and d*d+mu*mu == A and d*d+nu*nu == C
    h = F(132)/d
    t = ((h-d)**2-841)/4
    H = (h-d, h, h+d)
    T = (t-210, t, t+210)
    discriminants = ((41,29,1),(mu,None,nu),(47,37,23))
    roots = {}
    for i in range(3):
        for j in range(3):
            if (i,j) == (1,1):
                continue
            v = F(discriminants[i][j])
            assert v*v == H[i]*H[i]-4*T[j]
            pair = ((H[i]-v)/2,(H[i]+v)/2)
            assert pair[0]+pair[1] == H[i] and pair[0]*pair[1] == T[j]
            roots[(i,j)] = pair
    D = lcm(*(v.denominator for p in roots.values() for v in p))
    integer_roots = {ij: tuple(int(D*v) for v in p) for ij,p in roots.items()}
    datum_rational = tuple(D*q for q in H)+tuple(D*D*q for q in T)
    assert all(q.denominator == 1 for q in datum_rational)
    datum = tuple(int(q) for q in datum_rational)
    assert inherited.outer_root_table(datum) == integer_roots
    assert inherited.common_root_gcd(datum) == 1
    form = inherited.equal_area_normal_form(datum)
    assert form['top_triangle'] == [21*D,20*D,29*D]
    assert form['bottom_triangle'] == [35*D,12*D,37*D]
    assert form['K'] == 528*D*D and form['h'] != 0
    assert form['d'] == D*d and form['h'] == D*h
    assert form['e'] == 210*D*D
    swapped = tuple(-z for z in datum[:3][::-1])+datum[3:]
    swapform = inherited.equal_area_normal_form(swapped)
    assert swapform['top_triangle'] == form['bottom_triangle']
    assert swapform['bottom_triangle'] == form['top_triangle']
    assert swapform['K'] == -form['K']
    assert swapform['h'] == -form['h']
    return {'d':str(d),'mu':str(mu),'nu':str(nu),'h':str(h),'t':str(t),
            'D':D,'datum':datum,'roots':{str(k):v for k,v in integer_roots.items()},
            'primitive_gcd':1,'top_triangle':form['top_triangle'],
            'bottom_triangle':form['bottom_triangle'],
            'column_signs':[0 if z==0 else (1 if z>0 else -1) for z in datum[3:]],
            'd_over_b':str(d/29),'swap_verified':True}


def square_class_chord_identity():
    # f(X)-ell(X)^2 is the monic cubic having the three line intersections.
    # Evaluation at each of its rational roots e gives minus a square.
    import sympy as S
    x,e1,e2,e3,m,z=S.symbols('x e1 e2 e3 m z')
    f=(x-e1)*(x-e2)*(x-e3)
    for e in (e1,e2,e3):
        assert S.expand((f-(m*x+z)**2).subs(x,e)+(m*e+z)**2)==0
    return 'PASS_EXACT_POLYNOMIAL_IDENTITY'


def boundary_checks():
    # h-d=132/d-d and t=((h-d)^2-841)/4. Positive roots d
    # for t=210, 0, -210, respectively, are the following exact lists.
    candidates = {210:[3,44],0:[4,33],-210:[11,12]}
    checks=[]
    for t, ds in candidates.items():
        for d in ds:
            assert ((F(132,d)-d)**2-841)/4 == t
            u,v=A-d*d,C-d*d
            ok=u>=0 and v>=0 and isqrt(u)**2==u and isqrt(v)**2==v
            checks.append({'t':t,'d':d,'mu2':u,'nu2':v,'admissible':ok})
    assert [z['d'] for z in checks if z['admissible']]==[3]
    return checks


def main():
    source=Path(__file__).with_name('parent_checker.py').read_bytes()
    assert hashlib.sha256(source).hexdigest()=='dec70c04830e0291aca3e09bac595fcb22731670a00d4be9e1c86313713bf26b'
    assert 21*21+20*20==29*29 and 35*35+12*12==37*37
    assert 21*20==35*12==420
    assert A==(41*41+47*47)//2 and C==(1+23*23)//2 and A-C==1680
    assert on_curve(P)
    discriminant=A*A*C*C*(A-C)*(A-C)
    assert P[1]%11==0 and discriminant%11 != 0
    slope=(3*P[0]**2-2*(A+C)*P[0]+A*C)/(2*P[1])
    double=add(P,P)
    assert double[0].denominator>1 and double[0].denominator%121==0
    rows=[]
    for n in (1,3,5,7,9,11):
        point=mul(n,P)
        x,y=point
        d,mu,nu=qsqrt(x),qsqrt(A-x),qsqrt(C-x)
        assert abs(y)==d*mu*nu
        row=reconstruct(d,mu,nu)
        row.update(n=n,point=[str(x),str(y)])
        rows.append(row)
    assert len({r['d_over_b'] for r in rows})==len(rows)
    assert tuple(rows[0]['datum'])==(41,44,47,0,210,420)
    report={'schema':'P11_OFFDIAG_EXACT_REGRESSION_V1',
            'scope':'PREDECLARED_REGRESSION_NOT_GLOBAL_PROOF',
            'seed':[str(z) for z in P],'A':A,'C':C,
            'cubic_discriminant':discriminant,
            'nontorsion_certificate':{'prime':11,'y_mod_11':int(P[1]%11),
                'discriminant_mod_11':discriminant%11,'tangent_slope':str(slope),
                'double':[str(z) for z in double],'method':'LUTZ_NAGELL_INTEGRAL_MONIC_CUBIC'},
            'square_class_chord_identity':square_class_chord_identity(),
            'boundary_candidates':boundary_checks(),'rows':rows,
            'all_checks_passed':True,'inherited_checker_sha256':hashlib.sha256(source).hexdigest()}
    Path(__file__).with_name('offdiag_checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'all_checks_passed':True,'odd_multiples':[r['n'] for r in rows],
        'D_digits':[len(str(r['D'])) for r in rows],
        'column_signs':[r['column_signs'] for r in rows],
        'n3':rows[1], 'nontorsion':report['nontorsion_certificate']},indent=2))


if __name__=='__main__':
    main()
