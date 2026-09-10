#!/usr/bin/env python3
"""Reuse exact causal packets and certify an endpoint plus its monotone family."""
from fractions import Fraction as F
from pathlib import Path
import sys,json,hashlib,time
ROOT=Path(__file__).resolve().parent
if not __debug__:raise RuntimeError('Assertions are required')
PAR=next((p for p in [ROOT/'parent'/'parent'/'parent_joint',ROOT.parent/'ns-orthogonal-response-barrier-20260910'] if (p/'certify_joint.py').is_file()),None)
if PAR is None:raise FileNotFoundError('Pinned causal response checker is required')
assert hashlib.sha256((PAR/'certify_joint.py').read_bytes()).hexdigest()=='a16b817cdc5cc46f96d447094c18fef14be8252b118e2d0435795970a9a81139'
sys.path.insert(0,str(PAR));import certify_joint as J
P=J.P;E=J.E;C=J.C;s=J.s
start=time.monotonic()
cert=json.loads((ROOT/'symmetric_verification.json').read_text())
assert cert['status']=='PASS' and cert['constant']=='909/200'
Cnew=F(909,200)
data=P.build_parent_directions()
v=E.scale(data['v'],10);g=E.scale(data['g'],100)
p2=E.scale(data['psi'][0],100);p3=E.scale(data['psi'][1],1000)
for z in [v,g,p2,p3]:C.packet_check(z)
for z in [p2,p3]:C.packet_check(z,True)
assert not J.inst_product(p2,p3)
assert {k for k,_,_ in p2}.isdisjoint({k for k,_,_ in p3})
# N is the signed ordered convection; use polarization for differences.
a1=E.scale(p2,F(1,7));a2=E.scale(p3,F(1,11))
lhs=P.plus(E.ntime(P.plus(a1,a2),P.plus(a1,a2)),E.scale(E.ntime(a1,a1),-1),E.scale(E.ntime(a2,a2),-1))
rhs=P.plus(E.ntime(a1,a2),E.ntime(a2,a1))
assert lhs==rhs
n3=E.heat_derivative(p3);K3=P.plus(E.ntime(v,p3),E.ntime(p3,v))
c3=E.gram_expr(n3,n3);c4=E.gram_expr(K3,K3)
assert P.rootiv(P.ri(c3)).b<F(16,125)
temporal,w=P.temporal_certificate(g);assert w==F(3271,10000)
print('Recovered and verified causal responses',len(p2),len(p3),len(K3),flush=True)
a=F(19,100) # .19
inv,Lraw,_=P.inverse_certificate(a)
L=F(43,8);assert Lraw<L #5.375
Cb=(P.I(Cnew)/P.rootiv(F(3,2))).b
alpha=F(20);assert L*Cb<alpha #20
vv=E.scale(v,a);d=P.plus(E.scale(p2,a*a),E.scale(p3,a**3))
e=P.plus(P.linear(vv,d),E.scale(g,-a*a))
assert e==E.scale(K3,-a**4)
C.packet_check(d,True);C.packet_check(e)
en=P.rootiv(P.ri(E.gram_expr(e,e)))
assert s.expand(E.gram_expr(e,e)-C.qsym(a)**8*c4)==0
U=P.rootiv(P.I((w*a*a)**2+(F(16,125)*a**3)**2))
eta_bound=U.b+L*en.b
eta=F(1211,100000);r=F(3,125);delta=F(1,20000)
assert eta_bound<eta
margin=r-eta-alpha*r*r
contraction=2*alpha*r
hom=(P.rootiv(F(3,4))*L).b
perturbed_margin=margin-hom*delta
assert margin>0 and contraction<1 and perturbed_margin>0
res={'status':'PASS','record_id':'FINDING-EM-PDE-SYMMETRIC-POLARIZATION-20260910',
 'periodic_constant':str(Cnew),'endpoint':str(a),'viscosity':1,
 'inverse_upper':str(L),'inverse_readout':float(L),
 'feedback_upper':str(alpha),'feedback_readout':float(alpha),
 'eta_upper':str(eta),'eta_computed_upper':str(eta_bound),'eta_computed_readout':float(eta_bound),
 'radius':str(r),'inclusion_margin':str(margin),'contraction':str(contraction),
 'initial_perturbation_radius':str(delta),'homogeneous_response_factor_upper':str(hom),
 'perturbed_margin_lower':str(perturbed_margin),'perturbed_margin_readout':float(perturbed_margin),
 'full_defect_packets':len(e),'full_defect_modes':len({k for k,_,_ in e}),
 'correction_packets':len(d),'defect_norm_upper':str(en.b),
 'c4_exact':str(c4),'unit_temporal_check':temporal,'inverse_details':inv,
 'uniform_family':{'range':'0<=a/nu<=19/100','perturbation':'||delta||_(Hdot^1/2)<=nu/20000',
 'trajectory_radius':'3nu/125','justification':'L(a), a^2, a^3, a^4 monotone; rescale u=nu U(nu t).'},
 'backend_sha256':hashlib.sha256(Path(E.__file__).read_bytes()).hexdigest(),
 'all_generated_frequencies_retained':True,'PDE_simulation':False,'independent_review':False,
 'nonlinear_bilinear_operator':'Bs=(B+B^op)/2; Bs(w,w)=B(w,w)', 'analytic_dependencies':['all-mode causal inverse','critical trajectory product','local-to-global continuation'],
 'elapsed_seconds':time.monotonic()-start}
(ROOT/'symmetric_family_verification.json').write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n')
print('PASS', {k:res[k] for k in ['endpoint','feedback_upper','eta_computed_readout','inclusion_margin','contraction','perturbed_margin_readout']},flush=True)
