#!/usr/bin/env python3
"""Author-side exact finite-ring certificate for joint (t,j) CM-branch collisions.

This is NOT an Enterprise Math native experiment or all-prime proof checker.
All computations use (Z/p^N Z)[s]/(s*s-2), p=13,19.
"""
import json
from fractions import Fraction
from pathlib import Path


def ring(p, n):
    modulus = p ** n

    def r(a=0, b=0):
        return (int(a) % modulus, int(b) % modulus)

    def add(x, y):
        return r(x[0] + y[0], x[1] + y[1])

    def neg(x):
        return r(-x[0], -x[1])

    def sub(x, y):
        return add(x, neg(y))

    def mul(x, y):
        return r(x[0]*y[0] + 2*x[1]*y[1], x[0]*y[1] + x[1]*y[0])

    def inv(x):
        nrm = (x[0]*x[0] - 2*x[1]*x[1]) % modulus
        assert nrm % p != 0, ('nonunit', p, x, nrm)
        q = pow(nrm, -1, modulus)
        return r(x[0]*q, -x[1]*q)

    def div(x,y):
        return mul(x,inv(y))

    def powr(x,e):
        out = r(1)
        while e:
            if e % 2:
                out = mul(out,x)
            x = mul(x,x)
            e //= 2
        return out

    return r, add, sub, mul, div, inv, powr, modulus


def rational_factor_identity():
    """Exact original involution identity checked at a range of rational points.

    Symbolic derivation in the accompanying Markdown is independent of this
    finite set of regression checks.
    """
    cases = [Fraction(2), Fraction(3), Fraction(5,7), Fraction(-3,2), Fraction(19,11)]
    for x in cases:
        if x in (0,-1):
            continue
        j = lambda z: 27*(1+z)*(1+9*z)**3/z
        t = x/(27*(1+x)**2)
        lhs = j(x)-j(1/x)
        rhs = 27*(x-1/x)*(1/t-64)*(1/t-8)
        assert lhs == rhs
    return len(cases)


def run_one(p, target_denominator, n=5):
    r, add, sub, mul, div, inv, powr, modulus = ring(p,n)
    z, one = r(0), r(1)
    s = r(0,1)
    plus = add(r(3),mul(r(2),s))
    minus = sub(r(3),mul(r(2),s))

    def j(x):
        return div(mul(mul(r(27), add(one,x)),powr(add(one,mul(r(9),x)),3)),x)

    def t(x):
        return div(x,mul(r(27),powr(add(one,x),2)))

    t0 = r(pow(216,-1,modulus))
    tc = r(pow(target_denominator,-1,modulus))
    c = sub(div(one,mul(r(27),tc)),r(2))

    def f(x):
        return add(sub(powr(x,2),mul(c,x)),one)

    def fp(x):
        return sub(mul(r(2),x),c)

    def hensel(start):
        x = start
        for _ in range(n+2):
            x = sub(x, div(f(x),fp(x)))
        assert f(x) == z
        assert (x[0]%p,x[1]%p)==(start[0]%p,start[1]%p)
        return x

    xp = hensel(plus)
    xm = hensel(minus)
    assert xp != xm
    assert (sub(xp,xm)[0]%p,sub(xp,xm)[1]%p)!=(0,0)
    assert mul(xp,xm)==one
    assert t(xp)==tc and t(xm)==tc
    assert j(xp)==j(xm)
    assert j(xp)==r(8000 if p == 13 else -32768)
    assert t(plus)==t0 and t(minus)==t0
    assert j(plus)!=j(minus)
    assert sub(j(plus),j(minus))[0] == 0
    assert sub(j(plus),j(minus))[1]%p == 0
    assert sub(j(plus),j(minus))[1]%(p*p) != 0
    assert (sub(tc,t0)[0] % p)==0
    assert (sub(tc,t0)[0] % (p*p)) != 0
    assert j(plus)==r(2417472,1707264)
    assert j(minus)==r(2417472,-1707264)

    dp=sub(xp,plus)
    dm=sub(xm,minus)
    assert dp[0]%p==dp[1]%p==0
    assert dm[0]%p==dm[1]%p==0
    delta_plus=[(a//p)%p for a in dp]
    delta_minus=[(a//p)%p for a in dm]
    # The closed-form linearization of x+1/x as t changes.
    v_c=sub(c,r(6))
    assert v_c[0]%p == 0 and v_c[1]%p == 0
    dc=r((v_c[0]//p)%p,(v_c[1]//p)%p)
    d_pred=div(dc,sub(one, inv(powr(plus,2))))
    assert (d_pred[0]%p,d_pred[1]%p)==tuple(delta_plus)
    assert ((sub(tc,t0)[0]//p)%p)!=0

    # Quantitative source-separation valuation on the entire local t-disc.
    # The first column is t=t_*+p^k; at this precision, v_p(D(t))=k.
    valuation_profile=[]
    def vp_pair(a):
        def val(z):
            v=0
            while z and z%p==0:
                z//=p
                v+=1
            return n if z==0 else v
        return min(val(a[0]),val(a[1]))

    for k in (1,2,3,4):
        tv = add(tc,r(p**k))
        cv = sub(div(one,mul(r(27),tv)),r(2))
        def fv(x):
            return add(sub(powr(x,2),mul(cv,x)),one)
        def fpv(x):
            return sub(mul(r(2),x),cv)
        def newton(start):
            x=start
            for _ in range(n+2):
                x=sub(x,div(fv(x),fpv(x)))
            assert fv(x)==z
            return x
        a,b=newton(plus),newton(minus)
        assert mul(a,b)==one
        obs=sub(j(a),j(b))
        assert vp_pair(obs)==k, (p,k,obs)
        valuation_profile.append({'t_displacement_p_power':k,'j_sheet_difference_valuation':vp_pair(obs)})
    assert vp_pair(sub(j(plus),j(minus)))==1

    return {
        'p':p, 'precision_digits':n, 'ring_modulus':modulus,
        'collision_fibre':'1/'+str(target_denominator),
        'cm_fibre':'1/216',
        'collision_parameter_first_digit':((sub(tc,t0)[0]//p)%p),
        'plus_root':list(xp), 'minus_root':list(xm),
        'plus_root_first_digit':delta_plus,
        'minus_root_first_digit':delta_minus,
        'joint_observer':{'t':list(tc),'j':list(j(xp))},
        'frozen_j_difference':list(sub(j(plus),j(minus))),
        'quantitative_collision_valuation_profile':valuation_profile,
        'assertions':'PASS',
    }


def main():
    cases=[run_one(13,8),run_one(19,64)]
    assert Fraction(1,8)-Fraction(1,216)==Fraction(13,108)
    assert Fraction(1,64)-Fraction(1,216)==Fraction(19,1728)
    # Nonexceptional target control: neither exact collision fibre is congruent
    # to the CM t-residue, so they cannot occur inside the same t-residue ball.
    other=[37,43,61,67,109,139,157,163,181]
    for p in other:
        assert 216%p not in (8%p,64%p)
    report={
        'schema':'AUTHOR_EXACT_JOINT_CM_OBSERVER_CERTIFICATE_V1',
        'status':'LOCAL_UNPUBLISHED_UNREVIEWED_NOT_NATIVE_NOT_ADMITTED',
        'domain':'X0(3) source h, involution x->1/x, t and j observers',
        'symbolic_algebra_statement':'J(x)-J(1/x)=27*(x-1/x)*(t^-1-64)*(t^-1-8)',
        'exact_rational_regressions':rational_factor_identity(),
        'p_adic_cases':cases, 'nonexceptional_prime_residue_controls':other,
        'universal_proof':'Textual identity plus Hensel argument in companion Markdown; finite certificates are not general proof',
        'native_source_claim':False,
    }
    dst=Path(__file__).with_name('d25_joint_t_j_collision_author_check_20261027.json')
    dst.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'result':'PASS','case_primes':[q['p'] for q in cases],'rational_tests':report['exact_rational_regressions'],'output':str(dst)},ensure_ascii=False))


if __name__=='__main__':
    main()
