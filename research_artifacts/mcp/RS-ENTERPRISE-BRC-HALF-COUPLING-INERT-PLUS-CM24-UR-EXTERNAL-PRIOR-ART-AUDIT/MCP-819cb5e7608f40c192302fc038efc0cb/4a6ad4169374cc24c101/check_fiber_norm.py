"""Independent directed/shared-context CM24 local review; no network/control writes.

Run from any cwd. Only this review directory's result JSON is written.
The Sakai polynomial is an inherited candidate input, not proved here.
"""
from pathlib import Path
import json
import math
import sympy as sp

h, H, t, X, J, u, v, w = sp.symbols('h H t X J u v w')
target = 216
tH = H*(H**2 + 9*H + 27)
xH = sp.cancel(tH + 54 + 729/tH)
xh = 27*h**6/(h**3-1)
jh = 27*h**3*(h**3+8)**3/(h**3-1)**3
jt = (t+27)*(t+243)**3/t**3
R = J**2-J*X*(X**2-126*X+2944)+X*(X+192)**3
assert sp.cancel(tH.subs(H,3*h-3)-27*(h**3-1)) == 0
assert sp.cancel(xH.subs(H,3*h-3)-xh) == 0
assert sp.cancel(jt.subs(t,27*(h**3-1))-jh) == 0
assert sp.cancel(R.subs({J:jt,X:t+54+729/t})) == 0
assert sp.factor(R.subs(J,1728)) == (X**2-576*X-1728)**2

f = h**6 - 8*h**3 + 8
B = sp.expand((H+3)**6-216*((H+3)**3-27))
assert sp.expand(B.subs(H,3*h-3)) == 729*f
disc_h = sp.discriminant(f,h)
disc_H = sp.discriminant(B,H)
assert disc_h == 2**21*3**6
assert disc_H == 2**21*3**36
general_fiber = (H+3)**6-X*((H+3)**3-27)
assert sp.factor(sp.discriminant(general_fiber,H)) == 3**12*X**5*(X-108)**3
trace_discriminant = sp.discriminant(w**3-6*w-8,w)
assert trace_discriminant == -864
CM_correspondence = sp.expand(R.subs(X,216))
assert CM_correspondence == J**2-4834944*J+14670139392
assert sp.discriminant(CM_correspondence,J) == 2**19*3**6*13**2*19**2
dxH_h = 27*h**5*(h**3-2)/(h**3-1)**2
assert sp.cancel(sp.diff(xH,H).subs(H,3*h-3)-dxH_h) == 0
assert sp.gcd(f,sp.together(dxH_h).as_numer_denom()[0]) == 1
assert sp.factor(sp.resultant(u**2-8*u+8,u-1,u)) == 1
assert sp.factor(sp.resultant(u**2-8*u+8,u-2,u)) == -4
symbolic_norm = sp.expand(27**2*(2*v)**5*(-4))
assert sp.rem(symbolic_norm + 2**7*3**6*v**2,v**3-1,v) == 0

def coefficient_polynomial(p):
    m=(p-1)//6
    # Closed binomial coefficients, not the author's recurrence.
    return sp.Poly(sum(math.comb(m,k)*math.comb(2*m,k)*108**k*X**(m-k)
                       for k in range(m+1)),X,modulus=p)

def case(p):
    assert p%24 in (13,19)
    m=(p-1)//6
    assert pow(2,(p-1)//2,p) == p-1
    zeta=next(a for a in range(2,p) if pow(a,3,p)==1)
    traces=[a for a in range(p) if (a**3-6*a-8)%p==0]
    assert len(traces)==1
    trace=traces[0]
    S=coefficient_polynomial(p)
    d=int(S.diff().eval(216))%p
    assert int(S.eval(216))%p==0 and d!=0
    A=(H+3)**6
    D=(H+3)**3-27
    correct=sp.Poly(sum(int(S.nth(m-k))*A**(m-k)*D**k for k in range(m+1)),H,modulus=p)
    wrong=sp.Poly(sum(int(S.nth(m-k))*pow(27,-k,p)*A**(m-k)*D**k
                      for k in range(m+1)),H,modulus=p)
    assert pow(27,-2*m,p)==1
    assert correct.degree()==p-1 and int(correct.LC())%p==1
    branches=[]
    qs=[]
    for i in range(3):
        tr=trace*pow(zeta,i,p)%p
        nh=2*pow(zeta,2*i,p)%p
        q=sp.Poly(h**2-tr*h+nh,h,modulus=p)
        assert pow((tr*tr-4*nh)%p,(p-1)//2,p)==p-1
        qs.append(q.as_expr())
        def red(a): return sp.Poly(a,h,modulus=p).rem(q)
        def mul(a,b): return red(a.as_expr()*b.as_expr())
        def power(a,n):
            r=red(1)
            while n:
                if n&1:r=mul(r,a)
                a=mul(a,a);n//=2
            return r
        def inverse(a): return sp.invert(a,q)
        def norm(a):
            c0=int(a.nth(0))%p;c1=int(a.nth(1))%p
            return (c0*c0+c0*c1*tr+c1*c1*nh)%p
        hv=red(h);uv=power(hv,3);den=red(uv.as_expr()-1)
        assert power(hv,p)==red(tr-h)
        tv=red(27*den.as_expr())
        assert power(tv,p)==red(729*inverse(tv).as_expr())
        xv=red(tv.as_expr()+54+729*inverse(tv).as_expr())
        assert xv==red(216)
        dx=red(27*power(hv,5).as_expr()*(uv.as_expr()-2)*inverse(power(den,2)).as_expr())
        assert dx!=red(0)
        U=red(pow(27,-m,p)*power(den,m).as_expr()*dx.as_expr())
        root=red(correct.as_expr().subs(H,3*h-3))
        derivative=red(correct.diff().as_expr().subs(H,3*h-3))
        badroot=red(wrong.as_expr().subs(H,3*h-3))
        assert root==red(0)
        assert derivative==red(U.as_expr()*d)
        r=nh*pow(2,-1,p)%p
        expected_nu=(-2**7*3**6*r*r)%p
        assert norm(U)==expected_nu
        assert norm(derivative)==expected_nu*d*d%p
        branches.append({'quadratic_h_coefficients':[int(a)%p for a in q.all_coeffs()],
                         'trace_h':tr,'norm_h':nh,'r':r,'norm_U':norm(U),
                         'norm_derivative':norm(derivative),
                         'recovered_S_prime_square':norm(derivative)*pow(expected_nu,-1,p)%p,
                         'wrong_extra_27_inverse_k_remainder':[int(badroot.nth(j))%p for j in (0,1)]})
    assert sp.Poly(sp.prod(qs),h,modulus=p)==sp.Poly(f,h,modulus=p)
    Q1728=sp.Poly(X**2-576*X-1728,X,modulus=p)
    return {'p':p,'m':m,'S_coefficients':[int(a)%p for a in S.all_coeffs()],
            'S_prime_216':d,'S_prime_216_square':d*d%p,'six_roots_three_Frobenius_pairs':True,
            'correct_pullback_degree':correct.degree(),'correct_pullback_monic':True,
            'wrong_formula_equals_correct':wrong==correct,
            'Q1728_divides_S':S.rem(Q1728).is_zero,'branches':branches}

cases=[case(p) for p in (13,19,37,43)]
assert all(not a['wrong_formula_equals_correct'] for a in cases if a['p'] in (19,37))
assert all(any(any(v for v in b['wrong_extra_27_inverse_k_remainder'])
               for b in a['branches']) for a in cases if a['p'] in (19,37))
assert next(a for a in cases if a['p']==19)['Q1728_divides_S']
# Conditional width note: standard z->z map and representative c'=1/p.
# sigma*T^n*sigma^-1 = [[1-np,n],[-np^2,1+np]], so both groups
# have minimal n=3 when p !=3. Identification with every paper marking
# remains a separate check; this note does not declare its theorem false.
def width(p):
    for n in range(1,3*p+1):
        a,b,c,d=1-n*p,n,-n*p*p,1+n*p
        if (a-1)%3==b%3==c%3==(d-1)%3==0 and c%p==0:return n
    raise AssertionError('width not found')
out={'schema':'CM24_DIRECTED_LOCAL_MATH_REVIEW_V1','shared_context':True,'blind':False,
     'official_Source_DR':False,'symbolic':{'h_fiber':str(f),'H_fiber':str(B),
       'h_discriminant':str(disc_h),'H_discriminant':str(disc_H),
       'general_H_fiber_discriminant':'3^12*X^5*(X-108)^3',
       'trace_cubic_discriminant':int(trace_discriminant),
       'CM_j_correspondence':str(CM_correspondence),
       'symbolic_exact_assertions':17,
       'norm_u_minus_1':1,'norm_u_minus_2':-4,
       'norm_U':'-2^7*3^6*r^2, r=(Norm(h)/2), r^3=1',
       'scope':'Pullback derivative norm determines S_prime(216)^2 only'},
     'finite_cases':cases,'conditional_width_note':{'representative':'1/p',
       'standard_forgetful_map':'z -> z','computed_widths':{str(p):width(p) for p in (13,19,37,43)},
       'paper_higher_doublepole_not_consumed_by_base_map':True,
       'specific_cusp_marking_reconciliation_pending':True},
     'global_supersingular_identification_not_proved_by_this_local_script':True,
     'UR_proved':False,'G_p_identified':False}
path=Path(__file__).with_name('FIBER_NORM_RESULTS.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','symbolic_fiber_unramified_p_ge_5':True,
                  'primes':[a['p'] for a in cases],'quadratic_branch_checks':12,
                  'global_Hasse_identity_scope':'delegated separate review'},sort_keys=True))
