#!/usr/bin/env python3
"""PREFIX-355: exact Gaussian-rational degree/discriminant certificate.

Declared scope: static auxiliary complex C^3 five-Port model, not native X6.
Uses exact SymPy rationals; no numerical roots and no float comparisons.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

import sympy as S

I = S.I
u, v, t = S.symbols("u v t")
A = S.Matrix([
    [4, 4, 0],
    [0, -4, 4],
    [-5 + 3*I, 0, -3 + I],
    [-2 - 2*I, 4 + 4*I, 2 + 2*I],
    [-2, 0, 5 + 2*I],
])
q_zero = [S.Rational(2125, 3721), S.Rational(200, 3721),
          S.Rational(29125, 29768), S.Rational(5825, 7442),
          S.Rational(31525, 59536)]
q_plus = [4, 1, 1, 1, 1]
q = [S.expand((1-t)*q_zero[j]+t*q_plus[j]) for j in range(5)]

# Distinct ordered source-path tags (port, source leg a, source leg b).
path_tags = [(j,a,b) for j in range(5) for a in range(3) for b in range(3)]
assert len(path_tags) == len(set(path_tags)) == 45
z = S.symbols("z1 z2 z3")
zb = S.symbols("zb1 zb2 zb3")
for j in range(5):
    by_tag = sum(A[j,a]*S.conjugate(A[j,b])*z[a]*zb[b]
                 for a in range(3) for b in range(3))
    left = sum(A[j,a]*z[a] for a in range(3))
    right = sum(S.conjugate(A[j,b])*zb[b] for b in range(3))
    assert S.expand(by_tag-left*right) == 0

B = A[3:5, :]*A[0:3, :].inv()
B_expected = S.Matrix([
    [S.Rational(5,2)+S.Rational(9,2)*I,
     S.Rational(3,2)+S.Rational(7,2)*I, 4*I],
    [S.Rational(11,4)+S.Rational(15,8)*I,
     S.Rational(11,4)+S.Rational(15,8)*I,
     S.Rational(5,4)+S.Rational(9,4)*I],
])
assert (B-B_expected).applyfunc(S.simplify) == S.zeros(2,3)
B=B_expected
assert A[:3,:].det() != 0

# G_j = u*v * (q1*h_j*h_j# - q_j), where h# has reciprocal
# substitutions conj(u)=q2/(q1*u), conj(v)=q3/(q1*v).
def quadratic_coefficients(row: int):
    a,b,c = B[row,0], B[row,1], B[row,2]
    qc = q[row + 3]
    ac,bc,cc = map(S.conjugate, (a,b,c))
    alpha = S.expand(c*(ac*q[0]*u + bc*q[1]))
    beta = S.expand((a+b*u)*(ac*q[0]*u+bc*q[1])
                    +c*cc*q[2]*u - qc*u)
    gamma = S.expand(cc*q[2]*u*(a+b*u))
    return alpha,beta,gamma

A4,B4,C4 = quadratic_coefficients(0)
A5,B5,C5 = quadratic_coefficients(1)
G4 = S.expand(A4*v*v+B4*v+C4)
G5 = S.expand(A5*v*v+B5*v+C5)

# Quadratic Sylvester resultant, with D/E the linear eliminant.
D = S.expand(A5*B4-A4*B5)
E = S.expand(A5*C4-A4*C5)
K = S.expand(B4*C5-B5*C4)
R = S.Poly(S.expand(E*E+D*K),u,t)
assert R.eval({u:0}).is_zero
P, rem = R.div(S.Poly(u,u,t))
assert rem.is_zero
P = S.Poly(S.expand(P.as_expr()),u,t)

# Substantive total-degree controls for the discriminant:
# alpha: (deg_u<=1, deg_t<=1), beta/gamma: (2,1).
for expr, du in [(A4,1),(B4,2),(C4,2),(A5,1),(B5,2),(C5,2)]:
    pol = S.Poly(expr,u,t)
    assert pol.degree(u) <= du and pol.degree(t) <= 1
assert P.degree(u) == 6
assert P.degree(t) == 4
for k in range(7):
    assert S.Poly(P.as_expr().coeff(u,k),t).degree() <= 4

# Independent symbolic Sylvester determinant check (no root solver).
sylvester = S.Matrix([
    [A4,B4,C4,0],
    [0,A4,B4,C4],
    [A5,B5,C5,0],
    [0,A5,B5,C5],
])
assert S.Poly(S.expand(sylvester.det(method="berkowitz")-u*P.as_expr()),u,t).is_zero
# Exact derivative and elimination identity proving simple root -> regular intersection.
assert S.Poly(S.expand(A4*R.as_expr()-(A4*E*E-B4*E*D+C4*D*D)),u,t).is_zero

# In the entire path 0<=t<=1: 4*q2 <= q1; positivity follows
# from each positive endpoint. Thus R2=q2/q1 <= 1/4.
assert S.expand(q[0]-4*q[1]) == S.Rational(1325,3721)*(1-t)
assert all(x > 0 for x in q_zero) and all(x > 0 for x in q_plus)
abs_a4 = S.expand(B[0,0]*S.conjugate(B[0,0]))
abs_b4 = S.expand(B[0,1]*S.conjugate(B[0,1]))
abs_a5 = S.expand(B[1,0]*S.conjugate(B[1,0]))
abs_b5 = S.expand(B[1,1]*S.conjugate(B[1,1]))
assert abs_a4/abs_b4 == S.Rational(53,29) > S.Rational(1,4)
assert abs_a5/abs_b5 == 1 > S.Rational(1,4)
# Therefore the quadratic v-leading coefficients cannot vanish on
# physical |u|^2=q2/q1 for any t in [0,1].

# Nonzero discriminant at t=0 using a *finite, independent* mod-13
# certificate in F13 with i -> 5 (5^2=-1 mod 13).
def to_f13(z):
    re,im = S.expand_complex(S.expand(z)).as_real_imag()
    re,im = S.Rational(re),S.Rational(im)
    def reduce(q):
        return (int(q.p)%13)*pow(int(q.q)%13,-1,13)%13
    return (reduce(re)+5*reduce(im))%13

P0 = S.Poly(P.as_expr().subs(t,0),u)
coeff13 = [to_f13(P0.nth(k)) for k in range(7)]
assert coeff13 == [4,4,1,4,10,3,11]
# Bézout identity: U*f + V*f' == 1 (mod 13), not a numerical gcd.
U13 = [3,3,12,5,10]
V13 = [7,10,7,9,5,7]
def mul(x,y):
    out=[0]*(len(x)+len(y)-1)
    for j,a in enumerate(x):
        for k,b in enumerate(y):
            out[j+k]=(out[j+k]+a*b)%13
    return out
fprime13 = [((k+1)*coeff13[k+1])%13 for k in range(6)]
Pbez=mul(U13,coeff13)
Qbez=mul(V13,fprime13)
assert [(a+b)%13 for a,b in zip(Pbez,Qbez)] == [1]+[0]*10
assert coeff13[6] != 0

# The full discriminant is computed exactly, not inferred from sampled roots.
# Factorization may include extraneous eliminant-projection collisions.
delta = S.Poly(S.discriminant(P.as_expr(),u),t,extension=I)
assert delta.degree()==40
real_imag_coeff = [S.expand(c).as_real_imag() for c in delta.all_coeffs()]
assert all(im==0 for re,im in real_imag_coeff)
real_delta = S.Poly.from_list([re for re,im in real_imag_coeff],gens=t,domain=S.QQ)
unit,factor_list=S.factor_list(real_delta)
assert sorted((f.degree(),power) for f,power in factor_list)==[(1,6),(1,6),(1,10),(3,2),(12,1)]
assert S.Poly(S.expand(unit*S.prod(f.as_expr()**m for f,m in factor_list) - real_delta.as_expr()),t).is_zero

def primitive_positive(poly):
    p=poly.clear_denoms()[1].primitive()[1]
    return -p if p.LC()<0 else p

factors=[(primitive_positive(f),m) for f,m in factor_list]
assert sorted(f.degree()*m for f,m in factors)==[6,6,6,10,12]
cubic=next(f for f,m in factors if f.degree()==3)
degree12=next(f for f,m in factors if f.degree()==12)
assert cubic.as_expr()==(
    20146977828425934386944*t**3
    -1153636440395600981600*t**2
    -3151971160768643750*t
    -1890887364703125)
assert S.factor_list(cubic)[1][0][0].degree()==3
assert len(S.factor_list(cubic,extension=I)[1])==1

# The degree-6 leading coefficient has no root on the physical parameter
# interval: p6 is a nonzero constant multiple of q1^3*q3.
Pu=S.Poly(P.as_expr(),u)
for k, expected in [(0,q[1]**3*q[2]), (6,q[0]**3*q[2])]:
    quotient,remainder=S.div(Pu.nth(k),expected,t,extension=I)
    assert S.expand(remainder)==0
    assert S.Poly(quotient,t).degree()==0 and quotient!=0

# Isolate the entire [0,1] zero set by exact rational Sturm counting,
# then certify four rational 1e-14 brackets.
assert [S.count_roots(f,0,1) for f,m in factors if f.degree()==1]==[0,0,0]
assert S.count_roots(cubic,0,1)==1
assert S.count_roots(degree12,0,1)==3
scale=10**14
brackets={
    "alpha":(degree12,1402465963206,1402465963207),
    "beta":(degree12,6693410218037,6693410218038),
    "gamma":(degree12,38253367319640,38253367319641),
    "projection_cubic":(cubic,5989905069771,5989905069772),
}
intervals={}
for label,(f,left,right) in brackets.items():
    a,b=S.Rational(left,scale),S.Rational(right,scale)
    assert S.sign(f.eval(a))*S.sign(f.eval(b))==-1
    assert S.count_roots(f,a,b)==1
    intervals[label]={"left":str(a),"right":str(b),"width":"1/100000000000000"}
assert S.Rational(1753,125000)<S.Rational(1402465963206,scale)
assert S.Rational(1402465963207,scale)<S.Rational(561,40000)
assert S.Rational(33467,500000)<S.Rational(6693410218037,scale)
assert S.Rational(6693410218038,scale)<S.Rational(13387,200000)
assert S.Rational(1,4)<S.Rational(38253367319640,scale)
assert S.Rational(38253367319641,scale)<S.Rational(497,1250)

# Show no double-source projection ambiguity at degree-12 roots:
# Res_u(P,D) is coprime to the degree-12 factor over Q(i).
res_P_D=S.Poly(S.resultant(P.as_expr(),D,u),t,extension=I)
assert S.gcd(res_P_D,S.Poly(degree12,t,extension=I)).degree()==0

# The cubic discriminant factor is *not* a critical parameter for
# the actual pair (G4,G5).  At cubic roots P and P' have exactly one
# common u, which is D=E=0.  Every such point has an invertible
# complex Jacobian in (u,v), as the two nonvanishing resultants show.
res_D_E=S.Poly(S.resultant(D,E,u),t,extension=I)
for expr in (D,E):
    lead=S.Poly(expr,u).LC()
    assert S.gcd(S.Poly(lead,t,extension=I),S.Poly(cubic,t,extension=I)).degree()==0
assert S.rem(res_D_E,S.Poly(cubic,t,extension=I)).is_zero
for expr in [A4,A5]:
    r=S.Poly(S.resultant(D,expr,u),t,extension=I)
    assert S.gcd(r,S.Poly(cubic,t,extension=I)).degree()==0
Q=S.expand(B4*B4-4*A4*C4)
Lcoef=S.diff(D,u)
Lconst=S.diff(E,u)
W=S.expand(A4*Lconst*Lconst-B4*Lconst*Lcoef+C4*Lcoef*Lcoef)
for expr in [Q,W]:
    r=S.Poly(S.resultant(D,expr,u),t,extension=I)
    assert S.gcd(r,S.Poly(cubic,t,extension=I)).degree()==0

# Modular subresultant witness ruling out >1 double root at the cubic:
# an irreducible C over Q(i) defines a degree-3 field.  A rank/minor
# specialization t -> 14 in F37, i -> 6 has gcd_u(P,P') degree one.
assert (int(cubic.eval(14))%37)==0
assert (int(cubic.diff().eval(14))%37)!=0

def to_fp(z,p,ir):
    re,im=S.expand_complex(S.expand(z)).as_real_imag()
    re,im=S.Rational(re),S.Rational(im)
    def reduce(q):
        assert int(q.q)%p != 0
        return (int(q.p)%p)*pow(int(q.q)%p,-1,p)%p
    return (reduce(re)+ir*reduce(im))%p

p37_coeff = [to_fp(Pu.nth(k).subs(t,14),37,6) for k in range(7)]
assert p37_coeff==[4,4,16,12,17,20,25]
ff=S.Poly(sum(c*u**k for k,c in enumerate(p37_coeff)),u,modulus=37)
assert S.gcd(ff,ff.diff()).degree()==1
assert S.gcd(ff,ff.diff()).as_expr()==u-12
# The field specialization is good: lead coefficient=25 and C'(14)=32.
# If the characteristic-zero gcd had degree >=2, its first
# subresultant would vanish modulo irreducible C, hence at this
# good characteristic-37 specialization, contradicting gcd degree 1.

# The cubic's sole discriminant collision is regular.  Any D=E=0
# root makes P=P_u=0 (A4 != 0).  For G4=0, the exact resultants
# Q and W ensure G4_v !=0 and (D_u*v+E_u) !=0.  Thus the complex
# Jacobian is nonsingular, hence the real two-phase Jacobian also.
# Any other simple P root is already regular.  So cubic adds *zero*
# physical singular values, even if the eliminant has a double u.

# The other three positive discriminant roots are simple factors;
# at each, degree-six leading coefficient and D are nonzero.
# Each is an ordinary double-u collision with nonzero parameter
# unfolding.  The earlier independently stored exact source-count
# certificates (PREFIX352/353/354) give 6->4, 4->2, 2->0,
# proving actual physical folds at all three by compactness+IFT.
# This run does NOT independently rerun those antecedent certificates.

output = {
    "schema":"EM_PREFIX355_THREE_EXACT_FOLD_THRESHOLDS_V1",
    "scope":"auxiliary static complex C3 five-Port full exact-intensity fibres modulo U(1), t in [0,1]",
    "status":"AUTHOR_EXACT_SYMBOLIC_DERIVED_ON_PREFIX352_353_354_UNREVIEWED_NOT_ADMITTED",
    "input_q0":[str(x) for x in q_zero],
    "input_q_plus":[str(x) for x in q_plus],
    "path_pairs_with_labels":len(path_tags),
    "A_upper3_determinant":str(A[:3,:].det()),
    "P_degree_u":P.degree(u),
    "P_degree_t":P.degree(t),
    "discriminant_t_degree":delta.degree(),
    "discriminant_factors":[{"degree":f.degree(),"multiplicity":m,
        "primitive_ascending_coefficients":[str(x) for x in reversed(f.all_coeffs())]}
        for f,m in factors],
    "positive_candidate_intervals":intervals,
    "finite_field_at_t0":{"prime":13,"i_image":5,"P0_coefficients_ascending":coeff13,
        "bezout_U_ascending":U13,"bezout_V_ascending":V13,"bezout_equals_one":True},
    "finite_field_at_cubic":{"prime":37,"i_image":6,"t_image":14,
        "C_t_image":0,"C_derivative_image":int(cubic.diff().eval(14))%37,
        "P_coefficients_ascending":p37_coeff,"gcd_P_Pprime":"u-12"},
    "cubic_projection_critical":False,
    "cubic_regular_certificate":"gcd(C,Res_u(D,A4*A5))=gcd(C,Res_u(D,Q))=gcd(C,Res_u(D,W))=1, gcd_u(P,P') over Q(i)[t]/C has degree one",
    "three_actual_physical_singular_parameters":"alpha,beta,gamma; actual existence uses prior exact source-count certificates",
    "source_count_regimes":{"[0,alpha)":6,"alpha":5,"(alpha,beta)":4,"beta":3,"(beta,gamma)":2,"gamma":1,"(gamma,1]":0},
    "dependency_sources":["PREFIX352 t>=497/1250 no sources", "PREFIX353 t=1/4 two regular sources", "PREFIX354 t=1753/125000 six, t=561/40000 four, t=33467/500000 four, t=13387/200000 two"],
    "prior_endpoint_certificates_reexecuted":False,
    "native_X6":"NOT_EXECUTED_OR_IMPLIED",
    "next_question":"independent adversarial review of elimination/field-specialization/fold argument; construct native X6 path-provenance + third-slice-component observer-preserving lift",
    "checks":["matrix_exact", "B_exact", "45_tagged_paths", "quadratic_resultant_symbolic", "recovery_identity_exact", "physical_leading_coeff_obstruction_exact", "Fp13_bezout_exact", "full_discriminant_factorization_exact", "rational_sturm_all_real_roots", "cubic_noncritical_resultants_exact", "Fp37_subresultant_rank_witness", "degree12_nonprojection_gcd_exact"]
}

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--out', type=Path)
    args=parser.parse_args()
    content=json.dumps(output,ensure_ascii=False,indent=2,sort_keys=True)+'\n'
    if args.out:
        args.out.write_text(content,encoding='utf-8')
    print('PASS_PREFIX355_EXACT_THREE_PHYSICAL_FOLD_BRACKETS_CONDITIONAL_ON_PREFIX352_353_354')
    print('degree_u(P)=',P.degree(u),'degree_t(P)=',P.degree(t))
    print('P(0,u) mod 13 with i->5:',coeff13)
    print('F13 Bézout identity: U*P(0,u)+V*dP/du(0,u) == 1')
    print('Delta factor multiplicities:', [(f.degree(),m) for f,m in factors])
    print('positive intervals 1e-14:', intervals)
    print('cubic projection singularity regular: Res(D,Q), Res(D,W) coprime to cubic and F37 gcd degree 1')
    print('three physical folds rely on preceding full-source endpoint certificates')
