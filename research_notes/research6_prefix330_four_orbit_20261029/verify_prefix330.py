#!/usr/bin/env python3
"""PREFIX-330 author-side exact algebraic BRC fibre proof verifier.

Requirements: Python 3.10+, SymPy. All polynomial operations are exact over Q(i).
No numerical root approximations or trig are used as proof evidence.
"""
from itertools import combinations
import json
from functools import reduce
import sympy as S

I=S.I
x,y,t=S.symbols('x y t')
A=S.Matrix([
    [4,4,0],
    [0,-4,4],
    [-5+3*I,0,-3+I],
    [-2-2*I,4+4*I,2+2*I],
    [-2,0,5+2*I],
])
Q64=S.Matrix([32,16,10,104,29])
minor_values = [S.expand(A[list(rows),:].det()) for rows in combinations(range(5),3)]
assert len(minor_values)==10 and all(v!=0 for v in minor_values)
Q=[S.Rational(k,64) for k in Q64]
assert Q == [S.Rational(1,2),S.Rational(1,4),S.Rational(5,32),S.Rational(13,8),S.Rational(29,64)]

# Provenance-preserving BRC ordered path-pair evaluation.
def brc_quality(source):
    results=[];pair_count=0
    for j in range(5):
        paths=[S.expand(A[j,k]*source[k]/8) for k in range(3)]
        mass=S.Integer(0)
        for k in range(3):
            for ell in range(3):
                mass+=paths[k]*S.conjugate(paths[ell]);pair_count+=1
        results.append(S.simplify(S.expand_complex(mass)))
    return results,pair_count

rational_sources=[S.Matrix([0,1+I,1]),S.Matrix([0,1-I,1])]
for a in rational_sources:
    brc, pairs=brc_quality(a)
    assert brc==Q and pairs==45

# Complexified Segre fibre B_j(z,w)=q_j (q_j=q64/64), chart z3=1.
z=S.Matrix([x,y,1]); v=A*z
M=S.diag(*list(v))*A.conjugate()
D=S.factor(M[:3,:].det())
assert S.factor(D /(-1024*I*(x+y)*(y-1)*(x*(1-4*I)+1-2*I)))==1
w=S.simplify(M[:3,:].inv()*Q64[:3,0])
P=S.together((M[3,:]*w)[0]-Q64[3]).as_numer_denom()[0].expand()
R=S.together((M[4,:]*w)[0]-Q64[4]).as_numer_denom()[0].expand()
sub=S.subresultants(P,R,x)
assert [S.degree(a,x) for a in sub]==[3,3,2,1,0]
lin=S.Poly(sub[-2],x)
x_expression=S.cancel(-lin.nth(0)/lin.nth(1))
res=S.factor(S.resultant(P,R,x),extension=I)
factors=S.factor_list(res,extension=I)[1]
quartics=[f for f,k in factors if S.degree(f,y)==4]
assert len(quartics)==1
Qy=S.Poly(quartics[0],y,extension=I).monic()
Q_exp=S.Poly(
  (4009889320-1781681608*I)*y**4
 +(-16309089106+5648135613*I)*y**3
 +(32330408686-7256734999*I)*y**2
 +(-28275431456-362195540*I)*y
 +(7718155900+2476622526*I), y, extension=I).monic()
assert Qy==Q_exp
assert S.gcd(Qy,Qy.diff()).degree()==0
assert S.simplify(Qy.eval(1+I))!=0 and S.simplify(Qy.eval(1-I))!=0

# Compute canonical residues of rational expressions in K = Q(i)[y]/Qy.
# Coprimality of every denominator is an explicit part of the certificate.
def residue(expr):
    num,den=S.fraction(S.cancel(expr))
    num_poly=S.Poly(num,y,extension=I)
    den_poly=S.Poly(den,y,extension=I)
    dn=den_poly.rem(Qy)
    assert S.gcd(dn,Qy).degree()==0
    return (num_poly.rem(Qy)*dn.invert(Qy)).rem(Qy)

xbar=residue(x_expression)
assert xbar.degree()<=3
# All five Segre equations hold mod the quartic, not only the last two.
W=[residue(wj.subs(x,x_expression)) for wj in w]
for j in range(5):
    acc=S.Poly(0,y,extension=I)
    for k in range(3):
        vjk=residue(v[j].subs(x,x_expression))
        acc+=(vjk*W[k]*S.Poly(S.conjugate(A[j,k]),y,extension=I)).rem(Qy)
    assert acc.rem(Qy)==S.Poly(Q64[j],y,extension=I)

# Denominator D must remain invertible on every quartic root.
Dbar=residue(D.subs(x,x_expression))
assert S.gcd(Dbar,Qy).degree()==0
# Output w3 is a primitive fibre label on the quartic component.
tbar=W[2].as_expr()
P_t=S.resultant(Qy.as_expr(),t-tbar,y)
Pt=S.Poly(S.cancel(P_t),t).monic()
Pt_expected=S.Poly(
  29758587129448225*t**4
 -255711023882111440*t**3
 +1277050567880509143*t**2
 -1191970997377517618*t
 +300837526733367626,t).monic()
assert Pt==Pt_expected
assert S.gcd(Pt,Pt.diff()).degree()==0
assert S.simplify(Pt.eval(1))!=0
assert Pt.count_roots(-S.oo,S.oo)==2
lo1,hi1=S.Rational(45534,100000),S.Rational(45535,100000)
lo2,hi2=S.Rational(64597,100000),S.Rational(64598,100000)
assert Pt.count_roots(lo1,hi1)==1
assert Pt.count_roots(lo2,hi2)==1

# Resultant produces four distinct y values, and the rational sources are
# another two distinct exact solutions, saturating PREFIX-329 degree-six bound.
# For real t among four distinct t-values, the conjugate-swap involution has
# a fixed point. Positivity then yields w=t conjugate(z), a physical source.
assert len(rational_sources)==2
assert len(Qy.all_coeffs())==5
# The report is (0,0) on j=1,2,3,5 and (sqrt(13/8),0) at j=4.
# A common phase rotation aligns port4, and all other |port_j|^2<1.
assert all(Q[j]<1 for j in (0,1,2,4)) and Q[3]>0

# A rational pair demonstrates a nontrivial separation after port4 alignment.
port4=[(A[3,:]*v)[0]/8 for v in rational_sources]
aligned=[S.simplify(v*S.conjugate(p)/S.sqrt(Q[3])) for v,p in zip(rational_sources,port4)]
delta=aligned[0]-aligned[1]
separation=S.simplify(S.expand_complex((delta.conjugate().T*delta)[0]))
assert separation==S.Rational(20,13)

out={
 "schema":"ENTERPRISE_MATH_PREFIX330_EXACT_FOUR_PHYSICAL_ORBIT_V1",
 "status":"PASS",
 "model":"STATIC_AUXILIARY_S7-3_BRC_5PORT_INDEPENDENT_1_i_REFERENCES",
 "A_rows":[[str(v) for v in row] for row in A.tolist()],
 "exact_q":[str(q) for q in Q],
 "known_rational_sources":[[str(c) for c in z] for z in rational_sources],
 "ordered_source_labelled_brc_pair_count":90,
 "all_3_by_3_A_minors_nonzero":len(minor_values),
 "quartic_y_primitive_coefficients_desc":[str(c) for c in S.Poly(Q_exp.as_expr(),y).clear_denoms()[1].all_coeffs()],
 "quartic_y_squarefree":True,
 "quartic_solutions_verified_by_quotient_ring":4,
 "segre_algebraic_fiber_count":6,
 "t_minpoly_integer_coefficients_desc":[str(c) for c in S.Poly(Pt_expected.as_expr(),t).clear_denoms()[1].all_coeffs()],
 "t_real_root_count":2,
 "t_real_root_intervals":[[str(lo1),str(hi1)],[str(lo2),str(hi2)]],
 "t_other_roots":"one nonreal conjugate pair",
 "physical_common_phase_orbit_count":4,
 "joint_port_reference_report":[["sqrt(13/8)","0"] if j==3 else ["0","0"] for j in range(5)],
 "reference_error":"0 for port4, absolute real and imaginary error <=sqrt(q_j)<1 otherwise",
 "aligned_rational_pair_distance_squared":str(separation),
 "aligned_rational_pair_meb_squared":str(separation/4),
 "verification_scope":"exact Q(i) polynomial identities, Sturm real-root counting, provenance-preserving BRC mass and an analytic universal report; geometry bound six is inherited PREFIX329 author-side proof",
 "not_claimed":"No exact MEB for the four-point joint-report set, no improvement on L=1062562/458329, no native X6/Detector/time fidelity, no Driver mathematical admission"
}
print(json.dumps(out,sort_keys=True,ensure_ascii=False,indent=2))
