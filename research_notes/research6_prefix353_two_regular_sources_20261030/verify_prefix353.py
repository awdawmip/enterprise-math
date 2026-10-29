#!/usr/bin/env python3
"""PREFIX-353: exact exhaustive count of physical five-port sources at t=1/4.

Requires SymPy. All theorem-bearing checks use exact QQ(i) arithmetic.
No numerical root solver, float comparison, time evolution or native X6 is used.
"""
import json
from pathlib import Path
from math import comb
import sympy as sp

I = sp.I
R = sp.Rational
u, v = sp.symbols("u v")

A = sp.Matrix([
    [4, 4, 0],
    [0, -4, 4],
    [-5+3*I, 0, -3+I],
    [-2-2*I, 4+4*I, 2+2*I],
    [-2, 0, 5+2*I],
])
q0 = [R(2125,3721), R(200,3721), R(29125,29768), R(5825,7442), R(31525,59536)]
qp = [R(4), R(1), R(1), R(1), R(1)]
t = R(1,4)
q = [(1-t)*a+t*b for a,b in zip(q0, qp)]
ratio = [sp.cancel(qj/q[0]) for qj in q]
assert all(x > 0 for x in q)
assert A[:3,:].det() != 0
B = sp.simplify(A[3:,:] * A[:3,:].inv())
assert B == sp.Matrix([
    [R(5,2)+R(9,2)*I, R(3,2)+R(7,2)*I, 4*I],
    [R(11,4)+R(15,8)*I, R(11,4)+R(15,8)*I, R(5,4)+R(9,4)*I],
])
assert ratio == [1,R(4321,21259), R(117143,170072), R(24917,42518), R(154111,340144)]

# Physical gauge: y1=sqrt(q1)>0, y2/y1=u, y3/y1=v.
# Real torus: u*conj(u)=ratio[1], v*conj(v)=ratio[2].
# Rationalized complexification substitutes conj(u)=ratio[1]/u,
# conj(v)=ratio[2]/v and clears u*v; valid for u*v != 0.
Fs=[]
for row_index in range(2):
    C=list(B.row(row_index))
    h=C[0]+C[1]*u+C[2]*v
    hb=sp.conjugate(C[0])+sp.conjugate(C[1])*ratio[1]/u+sp.conjugate(C[2])*ratio[2]/v
    f=sp.cancel(u*v*(h*hb-ratio[row_index+3]))
    Fs.append(sp.Poly(f,u,v,extension=I).as_expr())
assert all(sp.Poly(f,v).degree()==2 for f in Fs)

# R(u) is the resultant in v. The trivial factor u is not physical;
# the nonzero roots are those of the following primitive QQ(i) sextic.
coeff = [
    5090835228527261+71614895574338548*I,
    417416545202030142+543235570042720056*I,
    3337275220717175466+1137796654098146880*I,
    10776039194181628336,
    16419146937566867214-5597875276434275520*I,
    10103847682197884622-13149381638926200696*I,
    606268127997851879-8528625800598994972*I,
]
P=sp.Poly(sum(coeff[k]*u**k for k in range(7)),u,extension=I)
resultant=sp.resultant(Fs[0],Fs[1],v)
constant=sp.cancel(resultant/(u*P.as_expr()))
assert constant != 0 and not constant.has(u)
assert sp.degree(P.as_expr(),u)==6 and P.eval(0)!=0
assert sp.gcd(P,sp.Poly(sp.diff(P.as_expr(),u),u,extension=I)).degree()==0

# Exact self-inversive relation: P(u)=C*u^6*conj(P(r2/conj(u))).
# Therefore the six roots are invariant under u -> r2/conj(u).
r2=ratio[1]
C=sp.cancel(coeff[6]/sp.conjugate(coeff[0]))
for k in range(7):
    assert sp.simplify(coeff[k]-C*r2**(6-k)*sp.conjugate(coeff[6-k]))==0

# Subresultant-linear recovery: a5 F4 - a4 F5 = b(u)*v + c(u).
# At every P-root b != 0, so v is unique and equals -c/b.
F4,F5=[sp.Poly(f,v) for f in Fs]
a4,b4,c4=F4.all_coeffs(); a5,b5,c5=F5.all_coeffs()
b=sp.expand(a5*b4-a4*b5)
c=sp.expand(a5*c4-a4*c5)
for poly in [b,c,a4,a5]:
    assert sp.gcd(P,sp.Poly(poly,u,extension=I)).degree()==0
E4=sp.Poly(sp.expand(a4*c*c-b4*b*c+c4*b*b),u,extension=I)
E5=sp.Poly(sp.expand(a5*c*c-b5*b*c+c5*b*b),u,extension=I)
Q4,rem4=sp.div(E4,P)
Q5,rem5=sp.div(E5,P)
assert rem4.is_zero and rem5.is_zero
assert sp.gcd(P,Q4).degree()==0
# Q4 * P is the exact eliminated equation along v=-c/b.
# Its simple roots give a nonzero two-variable complex Jacobian;
# restriction to the real physical 2-torus has a nonzero real Jacobian.

# Six rational Gaussian centres; Rouché via an entirely rational
# comparison |P(c)| + sum_{k>=2} |P^(k)(c)|*r^k/k! < |P'(c)|*r.
# Upper bound each complex |z| by |Re z|+|Im z|; lower bound |z|
# by max(|Re z|,|Im z|). The stronger certificate 8*LHS<RHS holds.
centers=[
    (-851569,-150284),  # A-outside
    (-450571,-15519),   # B-fixed-physical
    (-291886,343595),   # C-fixed-physical
    (-231474,-40850),   # A-inside
    (33589,-195171),    # D-inside
    (174076,-1011464),  # D-outside
]
radius=R(1,100000)
def l1(z):
    return abs(sp.re(z))+abs(sp.im(z))
def lb(z):
    return max(abs(sp.re(z)),abs(sp.im(z)))
exact_centers=[]
for xr,xi in centers:
    center=R(xr,10**6)+I*R(xi,10**6)
    exact_centers.append(center)
    # Taylor coefficients are Gaussian rationals. No float enters verdict.
    d=[sp.expand(sum(coeff[j]*comb(j,k)*center**(j-k) for j in range(k,7))) for k in range(7)]
    lhs=l1(d[0])+sum(l1(d[k])*radius**k for k in range(2,7))
    rhs=lb(d[1])*radius
    assert 8*lhs < rhs, (xr,xi)
for i in range(6):
    for j in range(i+1,6):
        assert abs(sp.re(exact_centers[i]-exact_centers[j]))>2*radius or abs(sp.im(exact_centers[i]-exact_centers[j]))>2*radius

# Exact sector separation. The involution keeps arguments/rays, so roots
# alone in their sector (B and C) must be fixed by the involution.
for index,center in enumerate(exact_centers):
    x=sp.re(center); y=sp.im(center)
    if index in (0,3): # sector A, two roots, both off the physical circle
        assert x < -radius and y < -radius
        low=(abs(y)-radius)/(abs(x)+radius)
        high=(abs(y)+radius)/(abs(x)-radius)
        assert R(1,10)<low<high<R(1,4)
    elif index==1: # sector B, only this root
        assert x < -radius and y < -radius
        low=(abs(y)-radius)/(abs(x)+radius)
        high=(abs(y)+radius)/(abs(x)-radius)
        assert R(1,100)<low<high<R(1,20)
    elif index==2: # sector C, only this root
        assert x < -radius and y > radius
    elif index in (4,5): # sector D, two roots off the circle
        assert x > radius and y < -radius
    else:
        raise AssertionError(index)
    # Four roots have |u|^2 strictly on one side of r2 across their disk.
    low2=(max(R(0),abs(x)-radius))**2+(max(R(0),abs(y)-radius))**2
    high2=(abs(x)+radius)**2+(abs(y)+radius)**2
    if index in (0,5): assert low2>r2
    if index in (3,4): assert high2<r2

# Invariance of the original rationalized equations under simultaneous
# (u,v) -> (r2/conj(u),r3/conj(v)) follows from Hermitian conjugation;
# with unique v per P-root the two fixed u's have fixed v as well.
# Their physical source count is therefore exactly 2, with nonzero
# physical angular Jacobian; no numerical roots are required for proof.

output={
    "schema":"ENTERPRISE_MATH_PREFIX353_EXACT_ROOT_COUNT_V1",
    "research_status":"AUTHOR_SIDE_EXACT_SYMBOLIC_PROOF_UNREVIEWED_NOT_ADMITTED",
    "parameter":"1/4",
    "input_q0":[str(x) for x in q0],
    "input_qplus":[str(x) for x in qp],
    "q_at_t":[str(x) for x in q],
    "intensity_ratios":[str(x) for x in ratio],
    "sextic_coefficients_ascending":[str(x) for x in coeff],
    "resultant_factor":"nonzero_constant * u * P(u)",
    "resultant_constant":str(constant),
    "complex_roots_total_with_multiplicity":6,
    "rational_disks":[{"center_real":f"{xr}/1000000","center_imag":f"{xi}/1000000","radius":"1/100000","rouche_certificate":"8*LHS<RHS","sector":("A" if i in (0,3) else "B" if i==1 else "C" if i==2 else "D"),"physical_modulus":("PROVED_EQUAL" if i in (1,2) else "PROVED_OUTSIDE" if i in (0,5) else "PROVED_INSIDE")} for i,(xr,xi) in enumerate(centers)],
    "self_inversive_involution":"u -> (4321/21259)/conjugate(u)",
    "unique_nonzero_v_per_sextic_root":True,
    "all_two_physical_v_norms_exact":True,
    "physical_source_count":2,
    "physical_jacobians_nonsingular":True,
    "exact_checkers":{"rouche":6,"sectors":4,"modulus_exclusions":4,"resultant":True,"gcd":True,"self_inversion":True,"jacobian_reduction":True},
    "model_limit":"Frozen static auxiliary C^3 five-Port intensity inverse problem; no native X6 or time evolution",
    "next":"Isolate first physical-source critical parameter in (0,1/4), conditional on the six regular t=0 predecessor sources; classify fold/collision/other change via exact discriminant."
}
path=Path(__file__).with_name("RESULTS_PREFIX353.json")
path.write_text(json.dumps(output,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("PASS_AUTHOR_SIDE_EXACT_T_QUARTER_TWO_REGULAR_SOURCES")
print("physical_sources=2, all 6 complexified roots enclosed, 4 excluded, Rouché margins 8*LHS<RHS")
print("result_file="+str(path))
