#!/usr/bin/env python3
"""PREFIX-368: exact real-form count for three rational finite five-Port fibers.

Requires sympy >=1.14. No floating point enters any decision.
"""
import json
from functools import reduce
from math import gcd, lcm
from pathlib import Path
import sympy as s

I, R = s.I, s.Rational
u, v, z, T = s.symbols('u v z t')
A = s.Matrix([
    [4, 4, 0], [0, -4, 4], [-5 + 3*I, 0, -3 + I],
    [-2 - 2*I, 4 + 4*I, 2 + 2*I], [-2, 0, 5 + 2*I],
])
B = s.simplify(A[3:, :] * A[:3, :].inv())
Q = [34000 + 204144*T, 3200 + 56336*T, 58250 + 1286*T,
     46600 + 12936*T, 31525 + 28011*T]
EXPECTED = {R(5,16): 6, R(1,3): 4, R(2,5): 2}

def poly_F(q):
    out=[]
    for j in range(2):
        a,b,c=list(B.row(j))
        out.append(s.expand((a+b*u+c*v)*(
            s.conjugate(a)*q[0]*u*v + s.conjugate(b)*q[1]*v
            + s.conjugate(c)*q[2]*u) -q[j+3]*u*v))
    return out

def variations(signs):
    nonzero=[x for x in signs if x]
    return sum(a != b for a,b in zip(nonzero,nonzero[1:]))

def signs_at_infinity(sturm,minus):
    return [int(s.sign(p.LC()) * (-1 if minus and p.degree()%2 else 1))
            for p in sturm]

def compute(r):
    t=s.factor((200-2125*r*r)/(12759*r*r-3521))
    assert 0 <= t <= R(1,4)
    q=[s.factor(x.subs(T,t)) for x in Q]
    assert s.cancel(q[1]/q[0] - r**2) == 0
    assert all(qj > 0 for qj in q)
    f=poly_F(q)
    res=s.Poly(s.resultant(f[0],f[1],v),u)
    assert res.degree()==7 and res.TC()==0
    p=s.Poly(s.cancel(res.as_expr()/u),u)
    assert p.degree()==6 and p.TC()!=0 and p.LC()!=0
    assert s.gcd(p,p.diff()).degree()==0
    assert p.eval(-r)!=0

    # Two finite, genuine quadratic equations in v at every u-root of P.
    for f_j in f:
        a2=s.Poly(s.Poly(f_j,v).coeff_monomial(v**2),u)
        assert s.gcd(a2,p).degree()==0
    sres=s.subresultants(f[0],f[1],v)
    linear=[s.Poly(x,v) for x in sres if s.Poly(x,v).degree()==1]
    assert len(linear)==1
    vcoeff=s.Poly(linear[0].coeff_monomial(v),u)
    assert s.gcd(vcoeff,p).degree()==0

    # Cayley transform; its real roots correspond exactly to |u|=r.
    h=s.Poly(s.cancel((1-I*z)**6*p.as_expr().subs(
        u,r*(1+I*z)/(1-I*z))),z)
    assert h.degree()==6
    ratios=[s.cancel(x/h.LC()) for x in h.all_coeffs()]
    assert all(s.simplify(s.im(x))==0 for x in ratios)
    den=lcm(*[int(s.denom(x)) for x in ratios])
    integer_coeff=[int(s.expand(x*den)) for x in ratios]
    common=reduce(gcd,integer_coeff)
    integer_coeff=[x//common for x in integer_coeff]
    if integer_coeff[0] < 0: integer_coeff=[-x for x in integer_coeff]
    H=s.Poly.from_list(integer_coeff,z,domain=s.ZZ)
    assert H.degree()==6 and s.gcd(H,H.diff()).degree()==0
    st=[s.Poly(a,z,domain=s.QQ) for a in s.sturm(H.as_expr(),z)]
    m=signs_at_infinity(st,True)
    pl=signs_at_infinity(st,False)
    n=variations(m)-variations(pl)
    assert n == EXPECTED[r]
    return {
        'radius':str(r),'t':str(t),'alpha':str(s.cancel(q[1]/q[0])),
        'H_coefficients_descending':integer_coeff,
        'P_degree':p.degree(),'resultant_degree':res.degree(),
        'gcd_P_derivative_degree':s.gcd(p,p.diff()).degree(),
        'gcd_P_v_subresultant_coefficient_degree':s.gcd(vcoeff,p).degree(),
        'gcd_H_derivative_degree':s.gcd(H,H.diff()).degree(),
        'P_minus_r_nonzero':True,
        'signs_minus_infinity':m,'signs_plus_infinity':pl,
        'variations_minus':variations(m),'variations_plus':variations(pl),
        'real_Cayley_roots':n,'physical_U1_orbits':n,
        'complex_nonphysical_pairs':(6-n)//2,
    }

def main():
    rows=[compute(r) for r in EXPECTED]
    results={
        'research':'PREFIX-368',
        'model':'2026-10-30 frozen static auxiliary complex three-dimensional five-Port intensity inverse problem',
        'mathematical_scope':'three exact rational fibers; not global interval classification',
        'method':'anti-holomorphic inversion plus rational Cayley transform and Sturm variation',
        'p000_native_x6_promoted':False,
        'native_heartbeat_computation':False,
        'independent_driver_review':False,
        'verification':'sympy exact rational and Gaussian rational arithmetic; symbolic Euclidean/resultant/Sturm',
        'points':rows,
        'outcome':'PASS_PREFIX368_EXACT_THREE_FIBER_REAL_FORM_STURM_6_4_2',
    }
    dst=Path(__file__).with_name('RESULTS_PREFIX368.json')
    dst.write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(results['outcome'])
    for item in rows:
        print('r=',item['radius'],'t=',item['t'],'V(-inf)=',item['variations_minus'],
            'V(+inf)=',item['variations_plus'],'real roots=',item['real_Cayley_roots'])
    print('sympy',s.__version__)
if __name__=='__main__': main()
