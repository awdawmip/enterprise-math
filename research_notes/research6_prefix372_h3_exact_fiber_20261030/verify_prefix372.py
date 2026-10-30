#!/usr/bin/env python3
"""PREFIX-372: exact H3 exceptional-fiber completion, five-Port auxiliary model.

All decision predicates are in Q(i)[x]/(A3) and exact rational arithmetic.
This program computes no native BRC heartbeat or P000 X6 dynamics.
Requires Python 3 and SymPy 1.14 (tested). Explicit standard mathematical
inputs: resultant-elimination identity and intersection count (PREFIX-367),
real-form involution (PREFIX-368), generic four-source count (PREFIX-371).
"""
import json
from sympy import (I, Matrix, Poly, Rational as R, symbols, expand,
                   conjugate, simplify, cancel, resultant, subresultants,
                   invert, gcd, factor_list)

x,u,v=symbols('x u v')
A=Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],
          [-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
B=simplify(A[3:,:]*A[:3,:].inv())
D0=12759*x-3521
N0=200-2125*x
Q=[a*D0+b*N0 for a,b in ((34000,204144),(3200,56336),
                         (58250,1286),(46600,12936),(31525,28011))]
assert expand(Q[0]+78885200)==0
assert expand(Q[1]-x*Q[0])==0
assert expand(Q[2]/Q[0]-(1101-3980*x)/424)==0
F=[]
for j in range(2):
    aa,bb,cc=B.row(j)
    F.append(Poly(expand((aa+bb*u+cc*v)*
         (conjugate(aa)*Q[0]*u*v+conjugate(bb)*Q[1]*v+
          conjugate(cc)*Q[2]*u)-Q[j+3]*u*v),v))
a,b,c=F[0].all_coeffs()
d,e,f=F[1].all_coeffs()
L=Poly(expand(d*b-a*e),u)
M=Poly(expand(d*c-a*f),u)
E=Poly(a,u)
RR=expand((a*f-c*d)**2-(a*e-b*d)*(b*f-c*e))
assert Poly(RR,u).nth(0)==0
P=Poly(cancel(RR/u),u)
assert (P.degree(),L.degree(),M.degree(),E.degree())==(6,3,3,1)
assert expand(a*RR-(a*M.as_expr()**2-b*M.as_expr()*L.as_expr()+c*L.as_expr()**2))==0

# H3 cubic: reproduce its factor in Res_u(L,M). There are three real
# cubic roots globally, but just one in the stated physical interval.
A3=Poly(6063581288774033*x**3-1986113892546671*x**2+
        211884780353647*x-7404639584785,x,domain='QQ')
assert len(factor_list(A3.as_expr(),extension=I)[1])==1
assert factor_list(A3.as_expr(),extension=I)[1][0][0].as_poly(x).degree()==3
fac=factor_list(resultant(L.as_expr(),M.as_expr(),u),extension=I)[1]
assert any(expand(Poly(g,x,extension=I).monic().as_expr()-A3.monic().as_expr())==0 and n==1
           for g,n in fac)
xl=R(1422183178,10**10)
xh=R(1422183179,10**10)
assert A3.count_roots(xl,xh)==1 and A3.eval(xl)*A3.eval(xh)<0
assert R(8,85)<xl<xh<R(4321,21259)

# Arithmetic in K=Q(i)[x]/(A3). A3 remains irreducible over Q(i).
Z=Poly(0,x,extension=I)
def k(q):return Poly(q,x,extension=I).rem(A3)
def mul(aa,bb):return (aa*bb).rem(A3)
def sub(aa,bb):return (aa-bb).rem(A3)
def inv(aa):return invert(aa,A3)
def bar(aa):
    return k(conjugate(aa.as_expr()).subs(conjugate(x),x))
def lst(expr):
    p=Poly(expr,u)
    return [k(p.nth(j)) for j in range(p.degree()+1)]
def trim(q):
    while q and q[-1].is_zero:q.pop()
    return q
def rem(A,B):
    out=A[:]
    assert B and not B[-1].is_zero
    invlead=inv(B[-1])
    while len(out)>=len(B):
        t=mul(out[-1],invlead)
        offset=len(out)-len(B)
        for i,bb in enumerate(B):out[i+offset]=sub(out[i+offset],mul(t,bb))
        trim(out)
    return out
def gcd_degree(A,B):
    aa,bb=lst(A),lst(B)
    while bb:aa,bb=bb,rem(aa,bb)
    return len(aa)-1

def ev_u(expr, uu):
    out=Z
    for coeff in Poly(expr,u).all_coeffs():
        out=(mul(out,uu)+k(coeff)).rem(A3)
    return out

# One and only one double projected root, all remaining projected roots
# simple. Any lift with a != 0 and L != 0 is unique.
checks={
    'gcd_P_Pprime':gcd_degree(P.as_expr(),P.diff().as_expr()),
    'gcd_P_L':gcd_degree(P.as_expr(),L.as_expr()),
    'gcd_P_E':gcd_degree(P.as_expr(),E.as_expr()),
    'gcd_L_M':gcd_degree(L.as_expr(),M.as_expr()),
}
assert checks=={'gcd_P_Pprime':1,'gcd_P_L':1,'gcd_P_E':0,'gcd_L_M':1}
S1=Poly(subresultants(L.as_expr(),M.as_expr(),u)[-2],u)
assert S1.degree()==1
p1=k(S1.nth(1));p0=k(S1.nth(0))
assert not p1.is_zero
u0=mul(-p0,inv(p1))
assert all(ev_u(expr,u0).is_zero for expr in
           (P.as_expr(),P.diff().as_expr(),L.as_expr(),M.as_expr()))
assert sub(mul(u0,bar(u0)),k(x)).is_zero

# Over the special common projection, F4 and F5 are proportional
# quadratics in v. Their two roots are distinct sigma-fixed points.
a0,b0,c0=(ev_u(expr,u0) for expr in (a,b,c))
kappa=k((1101-3980*x)/424)
assert not a0.is_zero and not c0.is_zero
assert sub(mul(c0,bar(c0)),mul(mul(kappa,kappa),mul(a0,bar(a0)))).is_zero
# |v1+v2|^2=|b/a|^2<4*kappa: a swapped reciprocal-conjugate
# pair would have the same phase and |v1+v2|>=2*sqrt(kappa).
margin=sub(mul(k(4)*kappa,mul(a0,bar(a0))),mul(b0,bar(b0)))
assert all(not c.has(I) for c in margin.all_coeffs())
assert margin.degree()<=2
C2,C1,C0=(R(q) for q in margin.all_coeffs())
assert C2>0 and C1<0 and C0>0
lower=C2*xl**2+C1*xh+C0
assert lower>0
assert not k(b0*b0-4*a0*c0).is_zero
# Exact source-label separation: two physical lifts at identical u have
# |v_1-v_2|^2 = 4*kappa-|b/a|^2 = margin/|a|^2 > 1/5.
A_norm=mul(a0,bar(a0))
sep5=sub(k(5)*margin,A_norm)
assert all(not coeff.has(I) for coeff in sep5.all_coeffs())

def lower_quadratic(poly):
    out=R(0)
    for (power,),coef in poly.terms():
        coef=R(coef)
        out+=coef*(xl if coef>=0 else xh)**power
    return out
sep5_lower=lower_quadratic(sep5)
assert sep5_lower>0


# Six distinct nonzero finite complex points follow: two at u0 and one
# over each of four simple projections. Existing PREFIX-367 gives total
# intersection multiplicity 6, hence every point is transverse. The
# antiholomorphic source involution acts as a locally constant permutation
# of the six distinct solutions near x_H. Its fixed-point count equals
# the verified generic count 4 on both adjacent open parameter regions.
# This is an exact mathematical deduction from the stated, versioned lemmas;
# native P000 transfer and independent Driver admission are separate.
result={
 'prefix':'372',
 'scope':'static_auxiliary_complex_three_coordinate_five_Port_inverse_problem',
 'claim':'H3_exactly_four_physical_U1_orbits_two_distinct_physical_lifts_one_projection',
 'xH_isolation':[str(xl),str(xh)],
 'A3_coefficients_desc':[str(z) for z in A3.all_coeffs()],
 'gcd_degrees_over_Qi_x_mod_A3':checks,
 'u_special_squared_modulus_equals_x_exact':True,
 'quadratic_root_product_modulus_identity':True,
 'strict_physical_double_lift_criterion_lower_bound':str(lower),
 'strict_5_times_source_squared_distance_minus_1_lower_bound':str(sep5_lower),
 'special_sources_same_u_squared_v_distance_gt':'1/5',
 'source_count_at_H3':4,
 'special_lifts_at_same_projection':2,
 'other_physical_lifts':2,
 'algebraic_intersections_distinct':6,
 'proof_dependencies':['PREFIX-367 complete intersection multiplicity six',
                       'PREFIX-368 real-form involution',
                       'PREFIX-371 generic count four and isolation'],
 'decisive_arithmetic':'exact QQ(i) quotient-field Euclidean algorithm plus rational sign enclosure',
 'independent_review':False,'formal_prover_checked':False,
 'native_P000_X6_or_typed_BRC_transfer':False,
 'passed':True}
print(json.dumps(result,ensure_ascii=False,indent=2))
print('PASS_PREFIX372_H3_EXACT_FOUR_PHYSICAL_SOURCES_AND_TWO_LIFTS')
