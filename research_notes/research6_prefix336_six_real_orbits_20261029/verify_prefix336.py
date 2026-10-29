#!/usr/bin/env python3
"""PREFIX-336: exact rational certification of six real BRC source orbits.

All certificate decisions use rational arithmetic.  The six decimal centers
are merely input candidates; Newton-contraction proves true solutions exist.
The five labelled ports retain all nine ordered provenance pairs each.
"""
import json
from itertools import combinations
from sympy import I, Matrix, Rational, conjugate, simplify

A = Matrix([
    [4,4,0],
    [0,-4,4],
    [-5+3*I,0,-3+I],
    [-2-2*I,4+4*I,2+2*I],
    [-2,0,5+2*I],
])
U = A / 8
source = Matrix([4,5-2*I,7-4*I])
b = [1360,128,2330,1864,1261]
lam=Rational(10,61)
L=Rational(1062562,458329)

# Verified original BRC carrier: all nine ordered labelled pairs at every port.
ports=[]
for j in range(5):
    v=[A[j,k]*source[k] for k in range(3)]
    ordered=[simplify(v[k]*conjugate(v[l])) for k in range(3) for l in range(3)]
    assert len(ordered)==9
    mass=simplify(sum(ordered))
    assert mass==b[j]
    ports.append({'row':j+1,'intensity_b':int(mass)})

# Full spark is the checkable hypothesis for the degree-six bound.
minors={','.join(str(z+1) for z in ix):str(simplify(A[list(ix),:].det())) for ix in combinations(range(5),3)}
assert len(minors)==10 and all(d!='0' for d in minors.values())

# a3>0 removes the continuous global phase.  F(v)=|A a(v)|^2-b.
R=Matrix([[A[j,0].as_real_imag()[0],-A[j,0].as_real_imag()[1],
            A[j,1].as_real_imag()[0],-A[j,1].as_real_imag()[1],
            A[j,2].as_real_imag()[0]] for j in range(5)])
S=Matrix([[A[j,0].as_real_imag()[1],A[j,0].as_real_imag()[0],
            A[j,1].as_real_imag()[1],A[j,1].as_real_imag()[0],
            A[j,2].as_real_imag()[1]] for j in range(5)])
H=[2*(R.row(j).T*R.row(j)+S.row(j).T*S.row(j)) for j in range(5)]
centers=[
    ['-9.872155986','-0.497496459','0.991123454','-1.977834057','3.013046410'],
    ['-9.851679166','0.672017894','0.997408380','1.897396211','3.094999288'],
    ['-6.837934178','6.406340759','1.820539644','1.328370101','4.317624519'],
    ['3.972277190','-3.655156020','5.069231734','1.852070781','7.206948698'],
    ['3.826943394','0.866306597','5.391314313','-1.020335300','8.029290029'],
    ['3.472972568','1.984555753','5.333493587','0.744208408','8.062257748'],
]
rr=Rational(1,100000000)
eta_bound=Rational(1,1000000000)
K_bound=Rational(30)
assert eta_bound+K_bound*rr**2/2<rr and K_bound*rr<1
boxes=[]
low=[]
high=[]
for i,words in enumerate(centers):
    c=Matrix([Rational(z) for z in words])
    Fc=Matrix([(R.row(j).dot(c))**2+(S.row(j).dot(c))**2-b[j] for j in range(5)])
    J=Matrix.vstack(*[2*(R.row(j).dot(c)*R.row(j)+S.row(j).dot(c)*S.row(j)) for j in range(5)])
    assert J.det()!=0
    Jinv=J.inv()
    eta=max(abs(q) for q in Jinv*Fc)
    # Uniform exact rational upper bound for sup_{||v-c||_inf <= rr} ||D T(v)||_inf / rr
    K=max(sum(abs(Jinv[ii,jj])*sum(abs(H[jj][kk,ll]) for ll in range(5))
              for jj in range(5) for kk in range(5)) for ii in range(5))
    assert eta<eta_bound and K<K_bound
    assert c[4]-rr>0
    sq=sum(z*z for z in c)
    abs_sum=sum(abs(z) for z in c)
    normlo=sq-2*rr*abs_sum
    normhi=sq+2*rr*abs_sum+5*rr*rr
    assert normlo>0
    low.append(normlo)
    high.append(normhi)
    boxes.append({'orbit':i+1,'center_5d':words,'radius_inf':str(rr),
                 'eta_less_than':'1/1000000000', 'K_less_than':'30',
                 'norm2_center_decimal':str(sq.evalf(15)),
                 'certified':True})
for i,j in combinations(range(6),2):
    assert max(abs(Rational(centers[i][k])-Rational(centers[j][k])) for k in range(5))>2*rr

# q is small enough that every entire phase circle passes the ten (Re/Im) tolerance-1 reports R=0.
q=[lam*lam*Rational(z,64) for z in b]
assert max(q)<1

# A two-point, two-distinct-orbit strict positive contact witness:
# a = lam*source, z = -lam*root in box 5 (zero-based i=4).
# Its squared half-distance exceeds the earlier baseline L.
cc=Matrix([Rational(s) for s in centers[4]])
# Norm squared of source+root (root has third coordinate real), with one fixed imaginary component -4.
vec=[Rational(4)+cc[0],cc[1],Rational(5)+cc[2],Rational(-2)+cc[3],Rational(7)+cc[4],Rational(-4)]
base_sumsq=sum(v*v for v in vec)
variation=2*rr*sum(abs(vec[k]) for k in [0,1,2,3,4])+5*rr**2
assert base_sumsq-variation > 420
assert (cc[4]+rr)**2 < 65   # distinct shape from source with |a3|^2=65
strict_lower=lam*lam*Rational(420,4)
assert strict_lower>L

# For six complete phase circles, symmetry gives exact MEB^2 = max_i ||lam*a_i||^2.
# The six proven roots exhaust the six-point complex algebraic fibre (degree-six argument in proof).
meb_lo=lam*lam*max(low)
meb_hi=lam*lam*max(high)
assert meb_lo>Rational('3.0013745')
assert meb_hi<Rational('3.0013746')
assert meb_lo>strict_lower

result={
 'schema':'PREFIX336_SIX_REAL_ORBIT_CERTIFICATE_V1',
 'status':'PASS_AUTHOR_SIDE_EXACT_RATIONAL',
 'model':'Static auxiliary S7-3 five-port source-labelled complex BRC, U=A/8',
 'source': ['4','5-2i','7-4i'],'raw_b':b,'scale_lambda':'10/61',
 'q':[str(x) for x in q], 'common_report':'all ten Re/Im entries zero, error bound 1',
 'all_ten_three_by_three_minors_nonzero':True,'minors':minors,
 'six_disjoint_newton_boxes':boxes,
 'global_phase_gauge':'a3 real positive','root_radius_inf':'1/100000000',
 'banach_global_bounds':{'preconditioned_residual_eta_lt':'1/1000000000',
                         'jacobian_lipschitz_K_lt':'30',
                         'map_inclusion':'eta+K*r^2/2<r',
                         'contraction':'K*r<1'},
 'complex_algebraic_degree_bound':6,
 'real_physical_orbits':6,
 'two_distinct_orbit_support':{'selected_orbits':'exact Gaussian integer original and fifth Newton root',
     'report_phases':'source as given and minus the fifth real-gauge root',
     'support_weights':['1/2','1/2'], 'squared_separation_raw_gt':'420',
     'meb2_lower_bound_strict':str(strict_lower),'baseline_L':str(L),
     'strict_gap':str(strict_lower-L)},
 'full_fiber_meb_squared_bounds':{'lower_strict':'3.0013745','upper_strict':'3.0013746',
   'exact_identity':'(10/61)^2 times maximum norm squared of six S1 orbits'},
 'validation_scope':'Exact rational arithmetic, six disjoint Banach fixed-point cubes and full-spark degree-six algebraic geometry; no use of random-search outcomes in proof.',
 'limitations':'Author-side unreviewed auxiliary static BRC. Full-phase Euclidean recovery risk is gauge-sensitive; physical phase-quotient recovery and native X6/Detector/time bridges remain separate.'
}
print(json.dumps(result,ensure_ascii=False,indent=2))
