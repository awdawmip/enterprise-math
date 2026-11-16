#!/usr/bin/env python3
"""R749SSP exact three-six-shift-read adjacent-cutoff separation certificate.

Python 3 + SymPy, rational symbolic arithmetic. Reconstructs source counts,
all six infinite polynomial certificates and the explicit q6/q7 noise gap.
"""
from functools import lru_cache
from fractions import Fraction
import json
from pathlib import Path
import sympy as sp

W = (1, 1, 2, 3, 6)
N = 200
n = [0] * (N + 1)
n[0] = 1
for w in W:
    for k in range(w, N + 1):
        n[k] += n[k-w]
C = [0] * (N + 1)
T = [0] * (N + 1)
for q in range(1, N+1):
    C[q] = C[q-1] + n[q-1]
    T[q] = T[q-1] + C[q-1]

t, e, d = sp.symbols('t e d')
S = lambda q: 18*q**4 + 54*q**3 - 345*q**2 + 2070*q - 16315

# Product of five labeled-source generating factors.
# The exact sum counts have series P(z)/(1-z^6)^5, deg P=17.
P = [1]
for w in W:
    layer = [0] * (7-w)
    for i in range(6//w):
        layer[i*w] = 1
    arr = [0] * (len(P)+len(layer)-1)
    for i, a in enumerate(P):
        for j, b in enumerate(layer):
            arr[i+j] += a*b
    P = arr
assert len(P)-1 == 17 and P[0] == 1

def binom4(x):
    return sp.prod(x-j for j in range(4))/24

@lru_cache(None)
def exact_sum_poly(residue):
    # For all m>=0: n(6m+r) is polynomial in m of degree <=4.
    result = 0
    for k in range(3):
        idx = 6*k+residue
        if idx < len(P):
            result += P[idx]*binom4(t-k+4)
    return sp.Poly(sp.expand(result), t).as_expr()

for r in range(6):
    np = exact_sum_poly(r)
    assert sp.Poly(np,t).degree() <= 4
    for m in range(20):
        assert np.subs(t,m) == n[6*m+r]

@lru_cache(None)
def ct(base):
    cp = sp.interpolate([(i,C[base+6*i]) for i in range(7)],t)
    tp = sp.interpolate([(i,T[base+6*i]) for i in range(8)],t)
    cp, tp = map(sp.expand,(cp,tp))
    assert sp.Poly(cp,t).degree() <= 5
    assert sp.Poly(tp,t).degree() <= 6
    for i in range(10):
        assert cp.subs(t,i) == C[base+6*i]
        assert tp.subs(t,i) == T[base+6*i]
    # The source-count generating function gives this six-step identity.
    block = sum(exact_sum_poly((base+h)%6).subs(
        t,t+(base+h)//6) for h in range(6))
    assert sp.expand(cp.subs(t,t+1)-cp-block)==0
    return cp,tp

@lru_cache(None)
def validate_T(base):
    cp,tp = ct(base)
    block = sum(ct(base+h)[0] for h in range(6))
    assert sp.expand(tp.subs(t,t+1)-tp-block)==0

def determinant(base, symbolic):
    rows=[]
    for j in range(3):
        q,p=base+6*j,base+1+6*j
        if symbolic:
            validate_T(q)
            validate_T(p)
            cq,tq=ct(q)
            cp,tp=ct(p)
            Q,Pp=q+6*t,p+6*t
        else:
            cq,tq=C[q],T[q]
            cp,tp=C[p],T[p]
            Q,Pp=sp.Integer(q),sp.Integer(p)
        v=Pp**3*(cq+d)
        u=Q**3*(tq+e)+sp.Rational(1,108)*(S(Pp)-S(Q))*(cq+d)
        rows.append((v,-u,cp*u-tp*v))
    a,b,c=rows
    H=sp.expand(a[0]*(b[1]*c[2]-b[2]*c[1])
               -a[1]*(b[0]*c[2]-b[2]*c[0])
               +a[2]*(b[0]*c[1]-b[1]*c[0]))
    D=sp.ilcm(*[v.q for v in sp.Poly(H,t,e,d).coeffs()])
    poly=sp.Poly(sp.expand(D*H),e,d)
    return D,{exp:sp.Poly(v,t) for exp,v in poly.terms()}

def triangle_certificate(base,symbolic):
    denominator, terms=determinant(base,symbolic)
    constant=terms[(0,0)]
    sign=int(sp.sign(constant.eval(0)))
    assert sign in (-1,1)
    bound=sp.Poly(sign*constant.as_expr(),t)
    for (i,j),cp in terms.items():
        if (i,j)==(0,0):
            continue
        major=sp.Poly(sum(abs(int(v))*t**exp[0]
                          for exp,v in cp.terms()),t)
        bound-=2**(i+j)*major
    bc=[int(v) for v in bound.all_coeffs()][::-1]
    assert bc and all(v>0 for v in bc)
    return {
        'base_cutoff':base,
        'adjacent_cutoff':base+1,
        'scale':str(denominator),
        'H00_sign':sign,
        'positive_bound_degree':len(bc)-1,
        'positive_coefficients':len(bc),
        'minimum_integer_coefficient':str(min(bc)),
        'constant_coefficient':str(bc[0]),
        'leading_coefficient':str(bc[-1]),
        'coefficients_in_ascending_t_order':[str(x) for x in bc],
    }

results=[triangle_certificate(6,False)]
assert results[0]['constant_coefficient']=='7492513905113222984'
assert results[0]['scale']=='216'
for base in (9,10,11,12,13,14):
    results.append(triangle_certificate(base,True))
    assert results[-1]['positive_bound_degree'] == 24
    assert results[-1]['positive_coefficients'] == 25

# Exact determinant-to-observation Lipschitz bound at cutoffs 6 and 7.
v=[];u=[];k=[]
for j in range(3):
    q,p=6+6*j,7+6*j
    v.append(p**3*(C[q]+2))
    u.append(q**3*(T[q]+2)+(abs(S(p)-S(q))*(C[q]+2)+107)//108)
    k.append((C[q]+2)*(C[p]+2))
B=sum(k[j]*(v[(j+1)%3]*u[(j+2)%3]
            +u[(j+1)%3]*v[(j+2)%3]) for j in range(3))
assert B==511017965164300224
lower=Fraction(int(results[0]['constant_coefficient']),
               int(results[0]['scale'])*B)
assert lower==Fraction(936564238139152873,13797485059436106048)

output={
    'schema':'R749SSP_THREE_READ_ADJACENT_EXACT_V1',
    'author_status':'AUTHOR_EXACT_NOT_REVIEWED',
    'scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
    'weights':list(W),
    'error_domains':'Independent (e,d),(E,D) in [-2,2]^2, fixed within each read sequence',
    'read_offsets':[0,6,12],
    'proved_pairs':'(6,7) and (q,q+1) for every integer q>=9',
    'q6_7_gap_sup':str(lower),
    'q6_7_noise_radius':str(lower/2),
    'q6_7_determinant_error_bound':str(B),
    'tail_residue_bases':[9,10,11,12,13,14],
    'tail_triangle_polynomial_coefficients':results,
    'proof_logic':[
        'Generating function P(z)/(1-z^6)^5 with deg(P)=17',
        'C(6m+r) and T(6m+r) residue polynomials have degrees <=5 and <=6',
        'Three-read equality forces zero determinant',
        'Every coefficient of six degree-24 determinant majorant polynomials strictly positive',
        'For q>=9 and q=6, no three-read collision on continuous error square'
    ],
    'status':'PASS'
}
result_path=Path(__file__).with_name('R749SSP_THREE_READ_ADJACENT_RESULTS.json')
result_path.write_text(json.dumps(output,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print('PASS; q=6 gap',lower,'tail residue degree 24 all-positive')
for r in results:
    print(r['base_cutoff'],r['scale'],r['H00_sign'],r['minimum_integer_coefficient'])
