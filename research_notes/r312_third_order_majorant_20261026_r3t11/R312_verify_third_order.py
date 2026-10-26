"""R312 symbolic verifier for the third-order BRC majorant threshold.

Exact rational algebra in SymPy; optional real-root experiments use mpmath.
This verifies a formal expansion, not an Enterprise Math native Result.
Run: python R312_verify_third_order.py [--numeric]
"""
import json
import math
import sys
import sympy as S


def verify_symbolic():
    t, c, b, g, h = S.symbols('t c b g h', nonzero=True)
    d = 1 / t
    n = c / t**2 + b / t + g + h * t

    def trunc(expr, order=4):
        return S.series(expr, t, 0, order).removeO().expand()

    # S_j = sum_{i=0}^{d-3} i^j, j <= 3, polynomially continued in d.
    sums = [d-2, (d-3)*(d-2)/2,
            (d-3)*(d-2)*(2*d-5)/6,
            (d-3)**2*(d-2)**2/4]
    # [log(prod_i(1-(2d+4)/(n-i)))]_{t^0..t^3}.
    # Terms with k+j >= 5 contribute only O(t^4).
    logprod = S.Integer(0)
    for k in range(1, 5):
        moment = sum(S.binomial(k+j-1, j) * (2*d+4)**k * sums[j]
                     / n**(k+j) for j in range(5-k))
        logprod -= trunc(moment)/k
    logprod = S.expand(logprod)
    ell = [S.factor(logprod.coeff(t, i)) for i in range(4)]
    assert S.simplify(ell[0] + 2/c) == 0
    assert S.simplify(ell[1] - (2*b-3)/c**2) == 0

    exp_terms = [S.Integer(1), ell[1], ell[2]+ell[1]**2/2,
                 ell[3]+ell[1]*ell[2]+ell[1]**3/6]
    pref = trunc((n-3*d-2)/(d*(d-1)))
    p = [pref.coeff(t,i) for i in range(4)]
    # At critical c: exp(-2/c)=1/c; all coefficient arithmetic is rational.
    am = [S.factor(sum(p[j]*exp_terms[k-j] for j in range(k+1))/c)
          for k in range(4)]

    # The exact U/B sum grouped by r, through r=4. Remainder r>=5 is
    # O(d^-3) for U/B, hence O(t^4) after division by d.
    ur = S.Integer(0)
    for r in range(1, 5):
        for tau in range(1, r+1):
            m = r+tau-2
            choose = S.prod(d-r-i for i in range(tau))/math.factorial(tau)
            ratio = S.prod((d-2-i)/(n-d+3+i) for i in range(m))
            ur += choose * S.binomial(r-1, tau-1) * ratio
    unorm = trunc(t * ur)
    um = [S.factor(unorm.coeff(t,i)) for i in range(4)]
    assert um[0] == 1
    diff = [S.factor(am[i]-um[i]) for i in range(4)]
    assert diff[0] == 0

    beta = S.factor(S.solve(diff[1], b)[0])
    gamma = S.factor(S.solve(diff[2].subs(b,beta), g)[0])
    eta = S.factor(S.solve(diff[3].subs({b:beta,g:gamma}),h)[0])
    expected_beta = (8*c+7-4*c*c)/(2*(c+2))
    expected_gamma = (6*c**6-30*c**5-327*c**4-283*c**3-54*c**2+18*c+1)/(6*c**2*(c+2)**3)
    expected_eta = (12*c**8+546*c**7+4854*c**6+7018*c**5+5511*c**4+877*c**3-1914*c**2-495*c-8)/(12*c**3*(c+2)**5)
    assert S.simplify(beta-expected_beta) == 0
    assert S.simplify(gamma-expected_gamma) == 0
    assert S.simplify(eta-expected_eta) == 0
    assert S.factor(diff[3].subs({b:beta,g:gamma})-(c+2)/c**2*(h-eta)) == 0
    assert not um[3].has(h)  # h enters the next order only.
    return {'status':'PASS','formal_order':'t^3 with remainder O(t^4)',
            'symbolic_identities_checked': 8,
            'critical_equation':'c*exp(-2/c)=1',
            'beta':str(beta),'gamma':str(gamma),'eta':str(eta),
            'H_over_d_t3_at_critical':'(c+2)*(h-eta)/c^2',
            'sympy_version':S.__version__}


def numerical_probe():
    import mpmath as M
    M.mp.dps = 60
    c = 2/M.lambertw(2)
    beta = (8*c+7-4*c*c)/(2*(c+2))
    gamma = (6*c**6-30*c**5-327*c**4-283*c**3-54*c**2+18*c+1)/(6*c**2*(c+2)**3)
    eta = (12*c**8+546*c**7+4854*c**6+7018*c**5+5511*c**4+877*c**3-1914*c**2-495*c-8)/(12*c**3*(c+2)**5)

    def h_value(d, n, r_cap=45):
        ab = (n-3*d-2)/(d-1)
        for i in range(d-2):
            ab *= 1-(2*d+4)/(n-i)
        end=min(d-1,r_cap)
        rs=[M.mpf(1)]
        for j in range(min(d-2,2*end-2)):
            rs.append(rs[-1]*(d-2-j)/(n-d+3+j))
        ub = M.mpf(0)
        for r in range(1,end+1):
            for tau in range(1,min(r,d-r)+1):
                ub+=math.comb(d-r,tau)*math.comb(r-1,tau-1)*rs[r+tau-2]
        theta=d/(n-d+3)
        rho=theta*(1+d*theta)
        upper_tail=d*rho**end/(1-rho)
        return ab-ub, upper_tail

    entries=[]
    for d in (30,60,100,250,400,600,1000,1500):
        pred=c*d*d+beta*d+gamma+eta/d
        root=M.findroot(lambda x:h_value(d,x)[0],(pred-1,pred+1),tol=M.mpf('1e-40'))
        remainder=(root-(c*d*d+beta*d+gamma+eta/d))*d*d
        tail=h_value(d,root)[1]
        entries.append({'d':d, 'approximate_real_crossing':M.nstr(root,21),
                        'd2_scaled_residual':M.nstr(remainder,16),
                        'discarded_U_over_B_tail_upper_bound':M.nstr(tail,5)})
    return {'c':M.nstr(c,21),'beta':M.nstr(beta,21),
            'gamma':M.nstr(gamma,21),'eta':M.nstr(eta,21),
            'approximate_root_checks':entries,
            'status':'NUMERICAL_CROSSCHECK_ONLY; NOT A RIGOROUS ROOT CERTIFICATE'}


if __name__ == '__main__':
    data={'schema':'EM_R312_MAJORANT_THIRD_ORDER_V1',
          'model':'ordered positive six-edge BRC source-count auxiliary model',
          'scientific_sources':['R303','R305','R309','R310','R311'],
          'symbolic':verify_symbolic()}
    if '--numeric' in sys.argv:
        data['numerical_probe']=numerical_probe()
    print(json.dumps(data,ensure_ascii=False,indent=2))
