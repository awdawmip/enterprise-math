#!/usr/bin/env python3
"""Apply the tensor constant to the inherited all-mode NS contraction.
Full causal outputs and rational norm enclosures; no PDE trajectory sampling.
"""
from pathlib import Path
from fractions import Fraction as F
import sys,hashlib,json,time
ROOT=Path(__file__).resolve().parent
if not __debug__:raise RuntimeError('Assertions required')
paths=[ROOT/'parent'/'parent_joint',ROOT.parent/'ns-orthogonal-response-barrier-20260910']
PAR=next((p for p in paths if(p/'certify_joint.py').is_file()),None)
if PAR is None:raise FileNotFoundError('Pinned joint-response dependency required')
assert hashlib.sha256((PAR/'certify_joint.py').read_bytes()).hexdigest()=='a16b817cdc5cc46f96d447094c18fef14be8252b118e2d0435795970a9a81139'
sys.path.insert(0,str(PAR));import certify_joint as J
P=J.P;E=J.E;C=J.C;s=J.s
result_lattice=json.loads((ROOT/'tensor_lattice_verification.json').read_text())
assert result_lattice['status']=='PASS' and result_lattice['certified_constant']=='6447/1000'
Cnew=F(6447,1000);start=time.monotonic()
data=P.build_parent_directions();v=E.scale(data['v'],10);g=E.scale(data['g'],100)
p2=E.scale(data['psi'][0],100);p3=E.scale(data['psi'][1],1000)
for h in[v,g,p2,p3]:C.packet_check(h)
for h in[p2,p3]:C.packet_check(h,True)
assert not J.inst_product(p2,p3)
assert {k for k,_,_ in p2}.isdisjoint({k for k,_,_ in p3})
c3=E.gram_expr(E.heat_derivative(p3),E.heat_derivative(p3))
assert P.rootiv(P.ri(c3)).b<F(16,125)
K3=P.plus(E.ntime(v,p3),E.ntime(p3,v));c4=E.gram_expr(K3,K3)
temporal,w=P.temporal_certificate(g);assert w==F(3271,10000)
Cb=(P.I(Cnew)/P.rootiv(F(3,2))).b
rows=[]
for a in [F(4,25),F(1,6),F(7,40)]:
 inv,Lraw,_=P.inverse_certificate(a);L=J.ceiling(Lraw,10**8)
 alpha=J.ceiling(L*Cb,10**8)
 vv=E.scale(v,a);d=P.plus(E.scale(p2,a*a),E.scale(p3,a**3))
 e=P.plus(P.linear(vv,d),E.scale(g,-a*a))
 assert e==E.scale(K3,-a**4)
 C.packet_check(d,True);C.packet_check(e)
 e2=E.gram_expr(e,e);assert s.expand(e2-C.qsym(a)**8*c4)==0
 en=P.rootiv(P.ri(e2));U=P.rootiv(P.I((w*a*a)**2+(F(16,125)*a**3)**2))
 eta=J.ceiling(U.b+L*en.b,10**10)
 r={F(4,25):F(12,1000),F(1,6):F(14,1000),F(7,40):F(1,50)}[a]
 margin=r-eta-alpha*r*r;assert margin>0 and 2*alpha*r<1
 hom=(P.rootiv(F(3,4))*L).b;perturb=F(1,1000000)
 assert margin-hom*perturb>0
 rows.append({'amplitude':str(a),'inverse_upper':str(L),'feedback_upper':str(alpha),
 'linear_response_upper':str(eta),'response_norm_upper':str(U.b),'linear_defect_norm_upper':str(en.b),
 'trajectory_radius':str(r),'four_alpha_eta':str(4*alpha*eta),'inclusion_margin':str(margin),
 'contraction':str(2*alpha*r),'arbitrary_initial_perturbation_radius':str(perturb),
 'perturbation_cost_upper':str(hom*perturb),'perturbed_margin_lower':str(margin-hom*perturb),
 'correction_packets':len(d),'full_defect_packets':len(e),'full_defect_outputs':len({k for k,_,_ in e}),
 'inverse_certificate':inv})
 print('PASS',a,'L',float(L),'alpha',float(alpha),'eta',float(eta),'r',float(r),'margin',float(margin),'contraction',float(2*alpha*r),flush=True)
result={'status':'PASS','record_id':'FINDING-EM-PDE-TENSOR-CELL-GRAM-20260910',
 'constant':str(Cnew),'cases':rows,'exact_c3':str(c3),'exact_c4':str(c4),
 'temporal_certificate':temporal,'uniform_viscosity_family':{
 'viscosity':'nu>0','amplitude':'0<=a/nu<=7/40','perturbation':'||delta u0||_Hdot^1/2 <= nu/1000000',
 'trajectory_radius':'nu/50','proof':'monotone endpoint bounds and exact viscosity rescaling, not parameter sampling'},
 'full_feedback':'inherited analytic all-mode inverse and critical contraction; not frequency-truncated NS',
 'backend_sha256':hashlib.sha256(Path(E.__file__).read_bytes()).hexdigest(),
 'PDE_simulation':False,'independent_review':False,'arbitrary_data_regularity':False,
 'elapsed_seconds':time.monotonic()-start}
(ROOT/'family_verification.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print('PASS complete family',time.monotonic()-start,flush=True)
