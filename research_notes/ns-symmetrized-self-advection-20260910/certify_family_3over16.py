#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parent
cert=json.loads((ROOT/'selfsym_verification.json').read_text()); assert cert['status']=='PASS' and cert['self_constant']=='99/20'
PAR=ROOT/'parent'/'parent'/'parent'/'parent_joint'; sys.path.insert(0,str(PAR)); import certify_joint as J
P=J.P;E=J.E;C=J.C
D=P.build_parent_directions();v=E.scale(D['v'],10);g=E.scale(D['g'],100);p2=E.scale(D['psi'][0],100);p3=E.scale(D['psi'][1],1000)
assert {k for k,_,_ in p2}.isdisjoint({k for k,_,_ in p3})
K3=P.plus(E.ntime(v,p3),E.ntime(p3,v)); temporal,w=P.temporal_certificate(g)
Cself=F(99,20); Ctraj=(P.I(Cself)/P.rootiv(F(3,2))).b
a=F(3,16); inv,Lraw,_=P.inverse_certificate(a); L=F(1311,250); assert Lraw<L
alpha=F(106,5); assert L*Ctraj<alpha
d=P.plus(E.scale(p2,a*a),E.scale(p3,a**3)); e=P.plus(P.linear(E.scale(v,a),d),E.scale(g,-a*a)); assert e==E.scale(K3,-a**4)
en=P.rootiv(P.ri(E.gram_expr(e,e)))
U=P.rootiv(P.I((w*a*a)**2+(F(16,125)*a**3)**2)); eta_comp=U.b+L*en.b
eta=F(589,50000); r=F(47,2000); delta=F(1,500000)
assert eta_comp<eta
margin=r-eta-alpha*r*r; contraction=2*alpha*r; hom=(P.rootiv(F(3,4))*L).b; pert=margin-hom*delta
assert margin>0 and contraction<1 and pert>0
res={'status':'PASS','record_id':'FINDING-EM-PDE-SYMMETRIZED-SELF-ADVECTION-20260910','viscosity_for_check':1,'endpoint_amplitude':str(a),'inverse_upper':str(L),'self_trajectory_feedback_constant_upper':str(Ctraj),'alpha_upper':str(alpha),'eta_computed_upper':str(eta_comp),'eta_used':str(eta),'trajectory_radius':str(r),'ball_margin':str(margin),'contraction_upper':str(contraction),'arbitrary_initial_perturbation_radius':str(delta),'perturbed_margin_lower':str(pert),'uniform_parameter_extension':'0<=a<=3/16 by monotonicity of inherited L(a), a^2,a^3,a^4 upper terms','viscosity_scaling':'0<=a/nu<=3/16 and perturbation <=2e-6 nu','all_output_modes_retained':True,'PDE_time_sampling':False,'limits':['Restricted A3 family and a small open neighborhood only.','No arbitrary-data regularity or optimal threshold claim.']}
(ROOT/'family_3over16_verification.json').write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(res,indent=2,ensure_ascii=False))
