#!/usr/bin/env python3
"""Author-side finite-ring regression for the weighted j-sheet 1-jet theorem.

Reuses (rather than recopies) the exact O_p ring implementation from the
2026-10-27 joint-(t,j) two-sheet certificate. This is auxiliary algebra,
not a native H0/B0 or q-Frobenius experiment.
"""
import json
from pathlib import Path
from fractions import Fraction
from d25_joint_t_j_collision_checker_20261027 import ring


def one_case(p, den, n=5):
    r, add, sub, mul, div, inv, powr, M = ring(p, n)
    one = r(1)
    s = r(0,1)
    plus = add(r(3),mul(r(2),s))
    minus = sub(r(3),mul(r(2),s))
    T = r(pow(den,-1,M))
    Z = r(0)

    def form(x):
        return sub(add(powr(x,2),one),mul(sub(div(one,mul(r(27),T)),r(2)),x))

    def fprime(x):
        return sub(mul(r(2),x),sub(div(one,mul(r(27),T)),r(2)))

    def lift(x):
        for _ in range(n+2):
            x=sub(x,div(form(x),fprime(x)))
        assert form(x)==Z
        return x

    def J(x):
        return div(mul(mul(r(27),add(one,x)),powr(add(one,mul(r(9),x)),3)),x)

    def j_weighted(x):
        # Exact (1+6*t*d/dt)J(x), with t=x/(27*(1+x)^2).
        a=mul(mul(r(-27),add(one,x)),powr(add(one,mul(r(9),x)),2))
        poly=add(sub(mul(r(153),powr(x,2)),r(5)),mul(r(116),x))
        return div(mul(a,poly),mul(x,sub(x,one)))

    def t_of(x):
        return div(x,mul(r(27),powr(add(one,x),2)))

    xp,xm=lift(plus),lift(minus)
    assert sub(xp,xm)[1]%p==4%p
    assert mul(xp,xm)==one
    assert t_of(xp)==T==t_of(xm)
    D=sub(J(xp),J(xm))
    H=sub(j_weighted(xp),j_weighted(xm))
    # D=0 for the exact 2-source collision fibre.
    assert D==Z
    dJdt=div(sub(H,D),mul(r(6),T))
    assert (dJdt[0]%p,dJdt[1]%p)==(0,10), (p,dJdt)
    expected_weighted=1 if p==13 else 14
    assert (H[0]%p,H[1]%p)==(0,expected_weighted), (p,H)

    # Exactly reproduce derivative of D=27*rho*(t^-1-64)*(t^-1-8)
    # at this zero by differentiating only its vanishing factor.
    if p==13:
        exact_der=mul(mul(mul(r(27),sub(xp,xm)),sub(r(8),r(64))),r(-64))
    else:
        exact_der=mul(mul(mul(r(27),sub(xp,xm)),sub(r(64),r(8))),r(-4096))
    assert dJdt==exact_der

    # At every nearby t in this p-adic ball, the ordinary j difference
    # may become more divisible but the differential difference stays a unit.
    profiles=[]
    for k in range(1,n):
        Tk=add(T,r(p**k))
        def Fk(x):
            q=sub(div(one,mul(r(27),Tk)),r(2))
            return add(sub(powr(x,2),mul(q,x)),one)
        def Fkp(x):
            return sub(mul(r(2),x),sub(div(one,mul(r(27),Tk)),r(2)))
        def liftk(x):
            for _ in range(n+2):
                x=sub(x,div(Fk(x),Fkp(x)))
            assert Fk(x)==Z
            return x
        a,b=liftk(plus),liftk(minus)
        Dk=sub(J(a),J(b)); Hk=sub(j_weighted(a),j_weighted(b))
        Djk=div(sub(Hk,Dk),mul(r(6),Tk))
        assert (Djk[0]%p,Djk[1]%p)==(0,10)
        # D's valuation equals k since t=t_*+p^k and the remaining factors are units.
        assert all(v % (p**k)==0 for v in Dk)
        assert any(v % (p**(k+1))!=0 for v in Dk)
        profiles.append({'k':k,'j_difference_divisible_by_p_power':k,'derivative_mod_p':[0,10]})
    return {'p':p,'modulus':M,'colliding_t':str(Fraction(1,den)),
            'dJdt_mod_p':[dJdt[0]%p,dJdt[1]%p],
            'weighted_H_diff_mod_p':[H[0]%p,H[1]%p],
            'D_equals_zero_mod_p5':True,
            'nearby_profiles':profiles}


def main():
    cases=[one_case(13,8),one_case(19,64)]
    # For p != 13,19 the scalar j already separates the two source
    # balls mod p: D0=27*4s*(216-64)*(216-8).
    import math
    others=[p for p in range(13,5000)
            if p%24 in (13,19) and all(p%d for d in range(2,math.isqrt(p)+1))
            and p not in (13,19)]
    for p in others:
        assert (27*4*152*208)%p != 0
    obj={'schema':'AUTHOR_D25_WEIGHTED_J_SHEET_FIRST_JET_CERTIFICATE_V1',
         'status':'AUTHOR_CHECKED_LOCAL_UNPUBLISHED_UNREVIEWED_NOT_NATIVE',
         'theorem_scope':'p=13,19 mod24, p-adic CM t-neighbourhood, j-sheet observation',
         'reused_source':'d25_joint_t_j_collision_checker_20261027.py:ring',
         'first_jet_exceptions':cases,
         'generic_primes_checked':len(others),
         'structural_result':'(t,J,(1+6*theta_t)J) separates source sheets: for p=13,19 weighted difference is unit mod p even when (t,J) coincide',
         'exact_claim_boundary':'No native E3/H0/B0 q-Frobenius, W_p mod p^3 or final LIFT inference.'}
    output=Path(__file__).with_name('d25_weighted_j_first_jet_sheet_repair_author_check_20261027.json')
    output.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','exceptions':[x['p'] for x in cases],
                      'generic_primes_checked':len(others),'output':str(output)}))

if __name__=='__main__':
    main()
