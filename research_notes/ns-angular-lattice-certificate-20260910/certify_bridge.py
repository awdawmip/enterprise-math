#!/usr/bin/env python3
"""New angular constant, unchanged all-mode causal NS interface; no PDE sampling."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib,time
ROOT=Path(__file__).resolve().parent
PARENT=next((p for p in [ROOT/'parent/certify_joint.py',ROOT.parent/'ns-orthogonal-response-barrier-20260910/certify_joint.py'] if p.is_file()),None)
if PARENT is None:raise FileNotFoundError('Pinned joint-response checker is required')
assert hashlib.sha256(PARENT.read_bytes()).hexdigest()=='a16b817cdc5cc46f96d447094c18fef14be8252b118e2d0435795970a9a81139'
sys.path.insert(0,str(PARENT.parent))
import certify_joint as J
P=J.P;E=J.E;C=J.C
if not __debug__:raise RuntimeError('Run without -O')
started=time.monotonic()
angular=json.loads((ROOT/'output/angular_constant.json').read_text())
CANG=F(angular['certified_constant']);assert CANG==F(1521,200)
data=P.build_parent_directions()
v=E.scale(data['v'],F(10));g=E.scale(data['g'],F(100))
p2=E.scale(data['psi'][0],F(100));p3=E.scale(data['psi'][1],F(1000))
for z in [p2,p3]:C.packet_check(z,True)
assert not J.inst_product(p2,p3)
assert E.heat_derivative(p2)==g
n3=P.plus(E.ntime(v,p2),E.ntime(p2,v))
assert E.heat_derivative(p3)==n3
c3=E.gram_expr(n3,n3);assert P.rootiv(P.ri(c3)).b<F(16,125)
k3=P.plus(E.ntime(v,p3),E.ntime(p3,v))
c4=E.gram_expr(k3,k3);q4=P.rootiv(P.ri(c4))
temporal,w=P.temporal_certificate(g);assert w==F(3271,10000)
CB=P.rootiv(P.I(F(2,3)))*CANG
rows=[]
for a,r in [(F(4,25),F(13,1000)),(F(1,6),F(18,1000))]:
 inv,Lraw,oldcb=P.inverse_certificate(a)
 L=J.ceiling(Lraw,10**8)
 if a==F(4,25):L=F(200630557,50000000)
 assert Lraw<L
 alpha=J.ceiling(L*CB.b,10**8)
 vv=E.scale(v,a);d=P.plus(E.scale(p2,a*a),E.scale(p3,a**3))
 e=P.plus(P.linear(vv,d),E.scale(g,-a*a))
 assert e==E.scale(k3,-a**4)
 en=a**4*q4.b
 assert P.rootiv(P.ri(E.gram_expr(e,e))).b<=en+F(1,10**28)
 U=P.rootiv(P.I((w*a*a)**2+(F(16,125)*a**3)**2)).b
 eta=J.ceiling(U+L*en,10**10)
 margin=r-eta-alpha*r*r
 assert margin>0 and 2*alpha*r<1
 initial_multiplier=L*P.rootiv(P.I(F(3,4))).b
 delta=J.floor(margin/(2*initial_multiplier),10**10)
 assert delta>0 and initial_multiplier*delta<margin
 row={'amplitude':str(a),'inverse_upper':str(L),'new_C_B_upper':str(CB.b),
 'alpha_upper':str(alpha),'eta_upper':str(eta),'radius':str(r),'inclusion_margin':str(margin),
 'four_alpha_eta':str(4*alpha*eta),'contraction':str(2*alpha*r),
 'off_family_perturbation_radius':str(delta),'correction_packets':len(d),
 'complete_linear_defect_packets':len(e),'complete_linear_defect_modes':len({k for k,_,_ in e}),
 'eta_readout':float(eta),'alpha_readout':float(alpha),'margin_readout':float(margin),
 'nonlinear_feedback_cutoff':None,'inverse_certificate':inv}
 if a==F(4,25):
  oldalpha=F(1556725999,50000000);oldlower=F(41340889,5000000000)
  assert 4*oldalpha*oldlower>1
  row['old_fixed_alpha']=str(oldalpha)
  row['old_four_alpha_response_lower']=str(4*oldalpha*oldlower)
  row['only_bilinear_constant_changed']=True
 rows.append(row)
 print('CERTIFIED',a,'alpha',float(alpha),'eta',float(eta),'radius',float(r),'q',float(2*alpha*r),flush=True)
result={'status':'PASS','new_constant':str(CANG),'source_constant_blob':angular['parent_blob'],
 'causal_inverse_parent_sha256':hashlib.sha256(PARENT.read_bytes()).hexdigest(),
 'exact_backend_sha256':hashlib.sha256(Path(E.__file__).read_bytes()).hexdigest(),
 'support_orthogonality_checked':True,'unit_p3_source_squared':str(c3),
 'unit_next_linear_source_squared':str(c4),'temporal_certificate':temporal,'cases':rows,
 'uniform_amplitude_interval':['0','1/6'],
 'interval_reason':'For a>=0, b_a=(a M(v_unit)-1/4)_+, L(a), and sqrt(w^2 a^4+q^2 a^6)+L(a) a^4 sqrt(c4) are nondecreasing; use the certified endpoint constants and radius.',
 'limits':['Inherited all-mode causal-inverse and contraction proofs are dependencies.',
 'This tests the stated shape and small off-family neighborhoods, not arbitrary initial data.',
 'No full PDE simulation or independent review.'],
 'elapsed_seconds':time.monotonic()-started}
(ROOT/'output/bridge.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS',time.monotonic()-started,flush=True)
