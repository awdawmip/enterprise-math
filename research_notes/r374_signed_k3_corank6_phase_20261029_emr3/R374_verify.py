#!/usr/bin/env python3
"""R374: exact global PF2 phase at corank 6 in the signed BRC K3 deformation.
Run from the Enterprise Math PR #1592 checkout:
 python research_notes/r374_signed_k3_corank6_phase_20261029_emr3/R374_verify.py
Optional independent raw-D/L route: append --independent (slower).
Only original R346 signed K/J source and sympy required; no previous ZIP/CSV.
"""
import hashlib
import json
import sys
from fractions import Fraction
from math import comb
from pathlib import Path
from sympy import Poly, Rational, Symbol, binomial, diff, expand, factor

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'r346_unbounded_interior_tp2_corank301_20261028_emr3'))
from R346_verify import K, J
x = Symbol('theta')
R = 6

def clean(seq):
    out = list(seq)
    while out and out[-1] == 0:
        out.pop()
    return tuple(out)

def add(a,b):
    return clean((a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0)
                 for i in range(max(len(a),len(b))))

def scale(a, v):
    return clean(z*v for z in a)

def mul(a,b):
    if not a or not b:
        return ()
    out = [0]*(len(a)+len(b)-1)
    for i, u in enumerate(a):
        if u:
            for j, v in enumerate(b):
                if v:
                    out[i+j] += u*v
    return clean(out)

def original_D_observations():
    smax, tmax = 3*R+16, 2*R+8  # 34 and 20: exact dependency closure
    kernels = [None]+[[((int(v),) if v else ()) for v in K(i)[:tmax+1]]
                       for i in range(1,13)]
    assert kernels[3][2] == (-8,)
    kernels[3][2] = (-8,-8)  # -8(1+theta); other signed terms unchanged
    B = [[() for _ in range(tmax+1)] for _ in range(smax+1)]
    B[0][0] = B[0][1] = (1,)
    for s in range(1,smax+1):
        for j, v in enumerate(J(s)[:tmax+1]):
            if v:
                B[s][j] = (int(v),)
        for i in range(1,min(s,12)+1):
            for j, kval in enumerate(kernels[i]):
                if kval:
                    for p in range(j,tmax+1):
                        if B[s-i][p-j]:
                            B[s][p] = add(B[s][p],mul(kval,B[s-i][p-j]))
    def D(q,k):
        acc = ()
        for w in range(k+1):
            acc = add(acc,scale(B[q+w][q],(-1)**(k-w)*comb(k,w)*2**(q-w)))
        return acc
    observations=[]
    for v in range(2*R+1):
        k, q = v+1, R+v+1
        minor = add(mul(D(q,k),D(q+1,k+1)),
                    scale(mul(D(q,k+1),D(q+1,k)),-1))
        observations.append(scale(minor,Fraction(5)**(2*R-1-2*k)))
    return observations

def coefficients():
    obs=original_D_observations()
    out=[]
    while obs:
        out.append(expand(sum(Rational(a)*x**j for j,a in enumerate(obs[0]))))
        obs=[add(obs[i+1],scale(obs[i],-1)) for i in range(len(obs)-1)]
    return out

def bernstein_coefficients(poly,a,b):
    a,b=Rational(a),Rational(b)
    assert a<b
    z=Poly(poly,x,domain='QQ').shift(a)
    n=z.degree()
    p=[v*(b-a)**i for i,v in enumerate(reversed(z.all_coeffs()))]
    return [sum(p[i]*Rational(binomial(k,i),binomial(n,i))
                for i in range(k+1)) for k in range(n+1)]

def verify():
    c=coefficients()
    assert len(c)==13
    c0_expected = (-65536000000000000*x**5+664829952000000000*x**4
        -6329544704000000000*x**3+25625926656000000000*x**2
        -40156077952000000000*x+19614743512000000000)
    assert expand(c[0]-c0_expected)==0
    assert expand(c[-1]-132*(30-16*x)**12)==0
    T=[expand(c[j]**2-c[j-1]*c[j+1]) for j in range(1,12)]
    a,b=Rational(901,1000),Rational(902,1000)
    groups=[]
    def cert(tag,seq,lo,hi):
        count=0
        for p in seq:
            beta=bernstein_coefficients(p,lo,hi)
            assert all(z>0 for z in beta),tag
            count += len(beta)
        groups.append({'group':tag,'polynomials':len(seq),'strict_positive_bernstein_coefficients':count,
                       'interval':[str(lo),str(hi)]})
    # PF2 sufficient conditions on (-1,sigma6]: all remaining c_j and T_j positive.
    cert('c1..c12',[c[j] for j in range(1,13)],-1,Rational(211,200))
    cert('T1..T11',T,-1,Rational(211,200))
    cert('c0_before', [c[0]],-1,a)
    cert('minus_c0_derivative',[-diff(c[0],x)],a,b)
    assert c[0].subs(x,a)>0>c[0].subs(x,b)
    # PF2 necessity beyond the unique c0 zero: cover every theta>b.
    cert('minus_c0_mid',[-c[0]],b,2)
    cert('minus_c7_middle',[-c[7]],2,Rational(12,5))
    cert('minus_c5_middle',[-c[5]],Rational(12,5),Rational(253,100))
    # -c0(253/100+y) has strictly positive coefficients for all y>=0.
    tail=list(reversed(Poly(-c[0],x,domain='QQ').shift(Rational(253,100)).all_coeffs()))
    assert len(tail)==6 and all(v>0 for v in tail)
    # Rational explicit separating witness: first five coranks PF2 at theta=1,
    # sixth corank not PF2 because its constant is negative.
    assert c[0].subs(x,1)==-645658536000000000
    if '--independent' in sys.argv:
        sys.path.insert(0,str(HERE.parent/'r369_signed_k3_branch_top_catalan_20261029_emr3'))
        from R369_check import compute_rows
        rows,_=compute_rows(x,R)
        assert len(rows[R])==13 and all(expand(rows[R][j]-c[j])==0 for j in range(13))
    rows=''.join(f'{j},'+','.join(str(v) for v in Poly(p,x,domain='ZZ').all_coeffs())+'\n'
                 for j,p in enumerate(c))
    result={'schema':'EM_R374_BRC_SIGNED_K3_CORANK6_GLOBAL_PF2_V1',
        'status':'R374_EXACT_PASS', 'domain':'theta>-1',
        'conclusion':'corank6 finite coefficient sequence PF2 iff -1<theta<=sigma6',
        'sigma6_definition':'unique c0 zero on (901/1000,902/1000)',
        'c0_descending':[str(z) for z in Poly(c[0],x).all_coeffs()],
        'c0_at_1':str(c[0].subs(x,1)),
        'groups':groups,
        'total_certified_positive_Bernstein_coefficients':sum(z['strict_positive_bernstein_coefficients'] for z in groups),
        'tail_positive_power_coefficients_at_253_over_100':[str(z) for z in tail],
        'all_c_integer_polynomial_rows_sha256':hashlib.sha256(rows.encode()).hexdigest(),
        'independent_13_polynomial_crosscheck':'PASS' if '--independent' in sys.argv else 'NOT_RUN',
        'all_index_R363_assumed':False, 'native_X6_transfer_claimed':False,
        'mathematical_admission_claimed':False}
    return result

if __name__=='__main__':
    result=verify()
    print(json.dumps(result,ensure_ascii=False,indent=2))
