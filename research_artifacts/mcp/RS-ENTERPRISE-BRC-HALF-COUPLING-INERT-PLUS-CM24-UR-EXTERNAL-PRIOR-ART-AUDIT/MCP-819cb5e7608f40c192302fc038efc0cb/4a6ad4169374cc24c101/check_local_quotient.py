"""Task-specific exact algebra and new quotient checks, not a UR proof.

No search, provider, repository, identity or control writes. Classical modular
curve arithmetic remains an external typed observer; no native X6 claim.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as s

H, h, t, X, J = s.symbols('H h t X J')
u = h**3
jh = 27*u*(u+8)**3/(u-1)**3
jH = (H+3)**3*(H+9)**3*(H**2+27)**3/(H**3*(H**2+9*H+27)**3)
jt = (t+27)*(t+243)**3/t**3
xH = (H+3)**6/((H+3)**3-27)
xt = t+54+729/t
R = J**2-J*X*(X**2-126*X+2944)+X*(X+192)**3
checks = {}
def zero(name, expression):
    value = s.cancel(expression)
    assert value == 0, (name, value)
    checks[name] = 'EXACT_ZERO'

zero('hesse_to_j_H', jh.subs(h, (H+3)/3)-jH)
zero('Maier_gamma_27_over_H_marking', jH-jH.subs(H, 27/H))
zero('Maier_to_selected_h_Mobius', (1+9/H)-((H+3)/3+2)/((H+3)/3-1))
zero('t3_small_cover', (27/H)**3/((27/H)**2+9*(27/H)+27)-729/(H*(H**2+9*H+27)))
zero('j_t_H_composition', jt.subs(t,H*(H**2+9*H+27))-jH)
zero('Fricke_H_composition', xt.subs(t,H*(H**2+9*H+27))-xH)
zero('Fricke_j_correspondence', R.subs({J:jt,X:xt}))
zero('Fricke_involution', xt-xt.subs(t,729/t))
zero('local_H_derivative', s.diff(xH,H)-3*(H+3)**5*(H**3+9*H**2+27*H-27)/(H**2*(H**2+9*H+27)**2))
D = s.together(xH-216).as_numer_denom()[0]
assert s.factor(s.discriminant((H+3)**6-X*((H+3)**3-27),H)) == 3**12*X**5*(X-108)**3
assert s.degree(D,H) == 6
assert s.discriminant(D,H) == 2**21*3**36
assert s.gcd(D, s.together(s.diff(xH,H)).as_numer_denom()[0]) == 1
assert s.expand(R.subs(X,216)) == J**2-4834944*J+14670139392
assert 4834944**2-4*14670139392 == 2**19*3**6*13**2*19**2
checks['degree_six_fiber_discriminant'] = {'degree':6,'discriminant':'2^21*3^36','all_target_p_at_least_5_unramified':True}
checks['j_collision_exception_only'] = {'target_j_collision_primes':[13,19],'fricke_cover_still_unramified':True}

def field_case(p):
    # Field F_p[sqrt(2)]. Targets have (2/p)=-1.
    assert p % 24 in (13,19)
    assert pow(2,(p-1)//2,p) == p-1
    one, z = (1,0),(0,0)
    def f(a): return (a % p,0)
    def add(a,b): return ((a[0]+b[0])%p,(a[1]+b[1])%p)
    def neg(a): return ((-a[0])%p,(-a[1])%p)
    def sub(a,b): return add(a,neg(b))
    def mul(a,b): return ((a[0]*b[0]+2*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
    def power(a,n):
        out = one
        while n:
            if n&1: out = mul(out,a)
            a = mul(a,a);n >>= 1
        return out
    def inv(a):
        n=(a[0]*a[0]-2*a[1]*a[1])%p
        assert n
        return (a[0]*pow(n,-1,p)%p,-a[1]*pow(n,-1,p)%p)
    def div(a,b):return mul(a,inv(b))
    def norm(a):return (a[0]*a[0]-2*a[1]*a[1])%p
    m = (p-1)//6
    # Inherited Sakai polynomial is only used to check this new pullback.
    c=[1]
    for k in range(m):c.append(c[-1]*(-m+k)*(-2*m+k)*pow((k+1)**2,-1,p)%p)
    sp=s.Poly(sum(c[k]*pow(108,k,p)*X**(m-k) for k in range(m+1)),X,modulus=p)
    assert sp.eval(0)%p == s.binomial(2*m,m)*pow(108,m,p)%p != 0
    assert sp.eval(108)%p == s.binomial(3*m,m)*pow(108,m,p)%p != 0
    if p == 19:
        assert s.Poly(sp.as_expr()-(X-7)*(X**2-6*X+1),X,modulus=p).is_zero
    d=s.Poly(sp.diff(),X,modulus=p).eval(216)%p
    assert sp.eval(216)%p == 0 and d != 0
    # Equivalent 27^-m(h^3-1)^m S(X); leading coefficient 1.
    # h=(H+3)/3 contributes the same global 27^-2m to each
    # coefficient; 27^(2m)=3^(p-1)=1 in F_p.
    expected=s.Poly(sum(int(sp.nth(m-k))*(H+3)**(6*(m-k))*((H+3)**3-27)**k for k in range(m+1)),H,modulus=p)
    pp=expected
    assert pp.degree() == p-1 and pp.LC()%p == 1
    def ev(poly,a):
        v=z
        for c in poly.all_coeffs():v=add(mul(v,a),f(int(c)))
        return v
    hs=[]
    for aa in range(p):
        for bb in range(p):
            hh=(aa,bb);uu=power(hh,3)
            if uu not in [(4%p,2%p),(4%p,-2%p)]:continue
            hi=sub(mul(f(3),hh),f(3))
            tt=mul(f(27),sub(uu,one))
            xx=add(add(tt,f(54)),div(f(729),tt))
            assert xx == f(216)
            assert power(uu,p) == sub(f(8),uu)
            assert power(tt,p) == div(f(729),tt)
            nh=norm(hh);assert pow(nh,3,p) == 8%p
            xprime=div(mul(mul(f(27),power(hh,5)),sub(uu,f(2))),power(sub(uu,one),2))
            assert xprime != z
            U=mul(mul(f(pow(27,-m,p)),power(sub(uu,one),m)),xprime)
            assert ev(pp,hi) == z
            phprime=ev(pp.diff(),hi)
            assert phprime == mul(U,f(d))
            r=nh*pow(2,-1,p)%p
            assert pow(r,3,p) == 1
            nu=(-2**7*3**6*pow(r,2,p))%p
            assert norm(U) == nu
            assert norm(phprime) == nu*d*d%p
            hs.append({'h':hh,'H':hi,'t':tt,'norm_h':nh,'cube_root_branch':r,'jacobian':xprime,'norm_U':nu,'norm_P_H_prime':norm(phprime)})
    assert len(hs) == 6
    return {'p':p,'m':m,'six_distinct_branches':hs,'S_prime_216':int(d),'local_pullback_derivative_checks':6,'directed_derivative_sign_not_recovered_by_norm':True}

finite=[field_case(p) for p in (13,19,37,43)]
out={'schema':'CM24_EXACT_LOCAL_QUOTIENT_CHECK_V1','symbolic_checks':checks,'global_fiber_discriminant':'3^12*X^5*(X-108)^3','p19_j1728_factor_included':'S19=(X-7)*(X^2-6X+1)','field_cases':finite,'verification_history':[{'first_run':'FAILED_ASSERTION_AT_P_H_ROOT','reason':'Incorrect extra 27^-k was introduced during H-to-h coefficient conversion','correction':'Use common 27^-2m=3^-(p-1)=1 for all coefficients; never per-k 27^-k','corrected_fresh_run':'PASS'}],'claim_scope':'Exact conditional/source-normalized local-map and derivative-norm transport; four primes are falsification checks, not UR proof or repetition of 77-prime regression','UR_proved':False,'G_p_identified':False,'period_divided_coordinate_identified':False}
Path(__file__).with_name('LOCAL_QUOTIENT_CHECK_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'symbolic_checks':len(checks),'field_primes':[13,19,37,43],'distinct_local_branches':sum(len(x['six_distinct_branches']) for x in finite),'status':'PASS'},sort_keys=True))
