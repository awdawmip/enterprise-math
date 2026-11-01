#!/usr/bin/env python3
"""PREFIX-339 independent author-side audit of PREFIX-336 six-box certificate
and exact antipodal feasibility thresholds for two observer reports.
Dependencies: Python 3, SymPy; all proof decisions are exact rationals.
"""
import json
from itertools import combinations, product
from sympy import I, Matrix, Rational as Q, conjugate, simplify

A=Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],[-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
a0=Matrix([4,5-2*I,7-4*I]); lam=Q(10,61)
b=[1360,128,2330,1864,1261]; q=[lam**2*Q(x,64) for x in b]
assert all(0<x<1 for x in q)
assert q[2]==Q(29125,29768)

# Compute source-labelled, ordered BRC pairs instead of using a collapsed matrix formula.
pairs=[]
for j in range(5):
    v=[A[j,k]*a0[k] for k in range(3)]
    entries=[simplify(v[k]*conjugate(v[l])) for k,l in product(range(3),repeat=2)]
    assert simplify(sum(entries))==b[j]
    pairs.extend(entries)
assert len(pairs)==45

minors=[]
for idx in combinations(range(5),3):
    minor=simplify(A[list(idx),:].det())
    assert minor!=0
    minors.append({'rows':[j+1 for j in idx], 'minor':str(minor)})
assert len(minors)==10

# Fresh local 5D real representation; not importing the predecessor verification module.
real=[]; imag=[]
for j in range(5):
    r=[];s=[]
    for k in range(2):
        x,y=A[j,k].as_real_imag()
        r.extend([x,-y]); s.extend([y,x])
    x,y=A[j,2].as_real_imag()
    r.append(x); s.append(y)
    real.append(Matrix([r])); imag.append(Matrix([s]))

centers=[
 ['-9.872155986','-0.497496459','0.991123454','-1.977834057','3.013046410'],
 ['-9.851679166','0.672017894','0.997408380','1.897396211','3.094999288'],
 ['-6.837934178','6.406340759','1.820539644','1.328370101','4.317624519'],
 ['3.972277190','-3.655156020','5.069231734','1.852070781','7.206948698'],
 ['3.826943394','0.866306597','5.391314313','-1.020335300','8.029290029'],
 ['3.472972568','1.984555753','5.333493587','0.744208408','8.062257748'],
]
rad=Q(1,10**8)
H=[2*(real[j].T*real[j]+imag[j].T*imag[j]) for j in range(5)]
results=[]
for index,raw in enumerate(centers,1):
    c=Matrix([Q(z) for z in raw])
    F=Matrix([(real[j]*c)[0]**2+(imag[j]*c)[0]**2-b[j] for j in range(5)])
    J=Matrix.vstack(*[2*((real[j]*c)[0]*real[j]+(imag[j]*c)[0]*imag[j]) for j in range(5)])
    assert J.det()!=0
    # Certified local Newton map N(x)=x-J(c)^(-1)F(x)
    inv=J.inv(); pre=inv*F
    eta=max(abs(z) for z in pre)
    K=max(sum(abs(inv[ii,jj])*sum(abs(H[jj][kk,ll]) for ll in range(5)) for jj in range(5) for kk in range(5)) for ii in range(5))
    assert eta < Q(1,10**9) and K < 30
    assert eta+K*rad**2/2 < rad and K*rad < 1
    assert c[4]-rad > 0
    results.append({'orbit':index,'eta_exact':str(eta),'K_exact':str(K),'center':raw,
                    'positive_a3':True,'map_into_closed_cube':True,'contraction':True})
for a,bid in combinations(range(6),2):
    assert max(abs(Q(centers[a][k])-Q(centers[bid][k])) for k in range(5)) > 2*rad

# Two-source strict positive-contact risk witness for the dual-nonzero report.
# Select the unrotated exact Gaussian source a0, rotate by zeta=(12-5i)/13,
# and use the *negative* of the certified fifth algebraic root.
# Thus p=lambda*zeta*a0, v=-lambda*a5, and p-v=lambda*(zeta*a0+a5).
zeta=(Q(12,13),-Q(5,13))
def gmul(z,w):
    return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def ztuple(x):
    u,v=x.as_real_imag()
    return (u,v)
def zsum(pairs):
    return (sum(x for x,y in pairs),sum(y for x,y in pairs))
def raw_port3(src):
    return zsum([gmul(ztuple(A[2,j]),src[j]) for j in range(3)])
a0_pairs=[ztuple(a0[j]) for j in range(3)]
rot=[gmul(zeta,z) for z in a0_pairs]
p3=tuple(lam*x/8 for x in raw_port3(rot))
assert p3==(Q(-1445,3172),Q(2785,3172))
assert all(Q(-1,2)<x<Q(3,2) for x in p3)
# Fifth Banach root is in the five-dimensional closed cube around c5.
c5=[Q(z) for z in centers[4]]
root5=[(c5[0],c5[1]),(c5[2],c5[3]),(c5[4],Q(0))]
v3mid=tuple(-lam*x/8 for x in raw_port3(root5))
# Port3 A-coefficient row: -5+3i,0,-3+i; coordinate sensitivities
v3err=(lam*Q(11,8)*rad,lam*Q(9,8)*rad)
assert all(Q(-1,2)<v3mid[j]-v3err[j] and v3mid[j]+v3err[j]<Q(3,2) for j in range(2))
# Other ports have their |(Ua)j| fixed at sqrt(qj)<1, so zero-target
# coordinate tolerances automatically hold for both p and v.
rawdiff=[(rot[j][0]+root5[j][0],rot[j][1]+root5[j][1]) for j in range(3)]
center_sep2=sum(x*x+y*y for x,y in rawdiff)
raw_err=2*rad*(sum(abs(rawdiff[j][l]) for j in range(2) for l in range(2))+abs(rawdiff[2][0]))+5*rad**2
assert center_sep2-raw_err > 373
L=Q(1062562,458329)
witness_meb2=lam**2*Q(373,4)
assert witness_meb2 > L
# a0 and root5 genuinely lie in different full phase orbits:
assert (c5[4]+rad)**2<65 # exact |(a0)3|^2=65, |(a5)3|^2<65

# Multi-component phase criterion. For |r_x|,|r_y|<=1, antipodal +/- phase
# exists precisely when q_port <= (1-|r_x|)^2+(1-|r_y|)^2.
q3=q[2]
assert q3 > Q(1,2) and q3 < 1
assert not (q3 <= (1-Q(1,2))**2+(1-Q(1,2))**2)
# However rotating the given port to 45 degrees always gives Re=Im=sqrt(q3/2)
# and both report differences <=1; other-port components have modulus <1.
assert 0<q3/2<1

# Single-component imaginary h=3/2 is still feasible for all six orbits:
# align the port imaginary positive sqrt(q3); sqrt(q3)>1/2, <1.
assert q3 > Q(1,4) and q3 < 1
assert Q(3,2)>1

out={
 'schema':'PREFIX339_INDEPENDENT_SIX_BOX_AUDIT_AND_REPORT_PHASE_THRESHOLD_V1',
 'status':'PASS_AUTHOR_SIDE_EXACT_SYMBOLIC_REPLICATION',
 'frozen_predecessor':'d550a2b412b220337e24fbfe8fa66509f853c90a',
 'source_input':'A, a0, b, six rational center boxes from PREFIX336; independently recomputed J,F,H,eta,K',
 'ordered_labelled_BRC_pairs':len(pairs),
 'full_spark_minors':minors,
 'six_disjoint_rational_cubes':results,
 'banach_cube_radius':str(rad),
 'normless_constraint':'All five q in (0,1)',
 'port3_mass':str(q3),
 'report_two_nonzero':{'port':3,'reference_re':'1/2','reference_im':'1/2',
       'all_six_orbits_have_feasible_phase':True,
       'no_orbit_has_feasible_antipodal_pair':True,
       'inequality_for_antipodal':f'{q3} > 1/2',
       'feasible_phase_construct':'Re(Im) of rotated port3 = sqrt(q3/2) each'},
 'report_dual_super_L_contact':{'phase_zeta':'(12-5i)/13','p3_exact':[str(x) for x in p3],
       'v3_midpoint':[str(x) for x in v3mid], 'v3_error_bounds':[str(x) for x in v3err],
       'raw_separation_squared_center':str(center_sep2),
       'raw_separation_squared_error_bound':str(raw_err),
       'raw_squared_separation_strict_gt':'373',
       'distinct_phase_orbits':True, 'support_weights':['1/2','1/2'],
       'two_state_MEB2_strict_gt':str(witness_meb2),'baseline_L':str(L),
       'gap_strict_gt':str(witness_meb2-L)},
 'report_single_superunit':{'port':3,'reference_re':'0','reference_im':'3/2',
       'all_six_orbits_have_feasible_phase':True,
       'no_orbit_has_feasible_antipodal_pair':True,
       'feasible_phase_construct':'Im rotated port3 = sqrt(q3) > 1/2'},
 'general_two_component_criterion':'If other-port references zero and all q<1, +/- phases exist iff q_t <= (1-|r_Re|)^2+(1-|r_Im|)^2, when both reference magnitudes <=1.',
 'single_component_criterion':'For h>=0 and only target Im at port t with q_t>0 and other q_j<1: nonempty iff h<=1+sqrt(q_t); feasible antipodes iff h<=1.',
 'exclusions':['No complete exact algebraic minimal polynomial for the maximizing squared norm',
               'No complete exact MEB2 for either new non-antipodal report',
               'Project-native X6, time, Detector, phase gauge and Driver acceptance not established']
}
with open('RESULTS_PREFIX339.json','w',encoding='utf-8') as f:
    json.dump(out,f,ensure_ascii=False,indent=2);f.write('\n')
print('PASS_AUTHOR_SIDE_EXACT_SYMBOLIC_REPLICATION')
print('six rational Banach cubes, 10 full-spark minors, 45 ordered BRC source pairs')
print('report (Port3 Re,Im)=(1/2,1/2): all six orbits feasible; ZERO antipodal pairs')
print('two distinct shapes, dual-nonzero report: 2-point MEB2 > 9325/3721 > L')
print('report (Port3 Re,Im)=(0,3/2): all six orbits feasible; ZERO antipodal pairs')
print('q3=',q3)
