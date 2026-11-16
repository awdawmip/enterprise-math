#!/usr/bin/env python3
"""R749SSR exact six-phase continuous-calibration and noise certificate.
Requires Python 3 and SymPy; no floating point is used in proof checks.
"""
import json
from pathlib import Path
import sympy as s

W=(1,1,2,3,6); N=90
q,e,d=s.symbols('q e d')
S=lambda u:18*u**4+54*u**3-345*u**2+2070*u-16315
n=[0]*(N+1);n[0]=1
for w in W:
    for t in range(w,N+1):n[t]+=n[t-w]
C=[0]*(N+1);T=[0]*(N+1)
for t in range(1,N+1):
    C[t]=C[t-1]+n[t-1]
    T[t]=T[t-1]+C[t-1]
for t in range(1,25):
    cc=tt=0
    for k5 in range((t-1)//6+1):
        for k4 in range((t-1-6*k5)//3+1):
            for k3 in range((t-1-6*k5-3*k4)//2+1):
                u=t-1-6*k5-3*k4-2*k3
                cc+=(u+1)*(u+2)//2
                tt+=u*(u+1)*(u+2)//6
    assert (cc,tt)==(C[t],T[t]),t
A=[s.Rational(3335,3),s.Rational(13780,9),s.Rational(12845,9),
   s.Rational(3740,3),s.Rational(11485,9),s.Rational(12980,9)]
B=[151823,252353,241283,192485,182531,217793]
LL=[s.Rational(455,36),s.Rational(-295,36),s.Rational(-25,36),
    s.Rational(185,36),s.Rational(-25,36),s.Rational(-295,36)]
phases=[]; polynomials={}
for r in range(6):
    sample=[r+6*k for k in range(1,8)]
    cp=s.Poly(s.interpolate([(z,C[z]) for z in sample[:6]],q),q)
    tp=s.Poly(s.interpolate([(z,T[z]) for z in sample],q),q)
    assert cp.degree()==5 and tp.degree()==6
    assert all(cp.eval(z)==C[z] and tp.eval(z)==T[z] for z in sample)
    polynomials[r]=(cp,tp)
    D=s.Poly(cp.as_expr()+d,q)
    P=s.Poly(s.expand(q**3*(tp.as_expr()+e)-s.Rational(1,108)*S(q)*D.as_expr()),q)
    assert D.degree()==P.degree()==5
    L=s.factor(P.nth(5)/D.nth(5))
    a=s.factor((P.nth(4)-L*D.nth(4))/D.nth(5))
    b=s.factor((P.nth(3)-L*D.nth(3)-a*D.nth(4))/D.nth(5))
    assert L==LL[r] and s.simplify(a-(A[r]-720*d))==0
    assert s.simplify(b-s.Rational(5,81)*(314928*d+69984*e-B[r]))==0
    ds=s.factor(A[r]/720)
    allowed=bool(-2<=ds<=2)
    item={"residue":r,"phase_limit":str(L),"a_constant":str(A[r]),
          "b_offset":B[r],"critical_d":str(ds),"critical_d_allowed":allowed}
    if allowed:
        lo=s.factor(b.subs({d:ds,e:-2}))
        hi=s.factor(b.subs({d:ds,e:2}))
        es=s.solve(b.subs(d,ds),e)[0]
        assert lo>0 and hi>0 and es < -2
        item.update({"b_min":str(lo),"b_max":str(hi),
                     "forbidden_e_second_cancellation":str(es),
                     "optimal_common_fixed_error_order":"q^-3"})
    else:
        assert ds>2
        item["optimal_common_fixed_error_order"]="q^-2"
    phases.append(item)

z=s.symbols('z')
v=1+z+z**2+z**3+z**4+z**5
nc=s.Poly(z*v**3*(1+z**2+z**4)*(1+z**3),z)
nt=s.Poly(z**2*v**4*(1+z**2+z**4)*(1+z**3),z)
assert nc.degree()==23 and nt.degree()==29
for j in range(4):
    for t in range(j):assert s.binomial(t-j+5,5)==0
for j in range(5):
    for t in range(j):assert s.binomial(t-j+6,6)==0
cp,tp=polynomials[0];q0=5070;d0=s.Rational(667,432)
def Y(k,ee,dd):
    return s.factor(s.Integer(k)**3*(tp.eval(k)+ee)/(cp.eval(k)+dd)-s.Rational(S(k),108))
delta=s.factor(Y(q0+6,0,d0)-Y(q0,0,d0))
assert delta == -s.Rational(43072397158749918762229855318,
                            22845986049467232904102240398950261)
assert delta<0 and 720*d0==A[0]
out={"research_unit":"R749SSR","status":"PASS",
     "evidence_class":"AUTHOR_EXACT_NOT_REVIEWED",
     "frozen_scientific_pin":"awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389",
     "weights":W,"domain":"q>=6 integer, e,d real in [-2,2]; fixed across reads",
     "C_numerator_degree":nc.degree(),"T_numerator_degree":nt.degree(),
     "phases":phases,"exact_q5070_delta":str(delta),
     "scope":"For any fixed m, global cutoff-pair infimum sup-norm separation is zero; no universal positive absolute-noise radius. Optimal fixed same-calibration orders only."}
path=Path(__file__).with_name("R749SSR_CONTINUOUS_SIX_SHIFT_RESULTS.json")
path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print("PASS: six exact phases, four real critical cancellations, finite-horizon uniform-noise obstruction")
print("exact q=5070 delta:",delta)
