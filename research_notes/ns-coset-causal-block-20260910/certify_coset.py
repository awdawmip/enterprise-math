#!/usr/bin/env python3
"""Full-output parity-resolved NS certificate. No PDE sampling.
Inherited exact Fourier and rational interval routines are reused unchanged.
The all-mode symmetric constant and causal-inverse theorem are stated dependencies.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib,json,sys,time
import sympy as s
ROOT=Path(__file__).resolve().parent
PARENT=next((p for p in [ROOT/'parent', ROOT.parent/'ns-orthogonal-response-barrier-20260910'] if (p/'certify_joint.py').is_file()), None)
if PARENT is None: raise FileNotFoundError('Pinned certify_joint.py dependency required')
assert __debug__, 'Run without -O'
assert hashlib.sha256((PARENT/'certify_joint.py').read_bytes()).hexdigest()=='a16b817cdc5cc46f96d447094c18fef14be8252b118e2d0435795970a9a81139'
sys.path.insert(0,str(PARENT))
import certify_joint as J
P=J.P;E=J.E;C=J.C
assert hashlib.sha256(Path(E.__file__).read_bytes()).hexdigest()=='0ffab938427c4827700876fbd9f9c371a59d07aa89edefd5a6447071ec48d25d'

def parity(k):return sum(k)%2
def part(A,j):return {key:v for key,v in A.items() if parity(key[0])==j}
def inv(a,j):
    rt=P.rootiv(2)
    if j==0:
        ma=6*rt*(F(1,2)+rt)
        mb=4*rt*(F(1,2)+P.rootiv(3))
        gap=F(1,2)
    else:
        ma=6*rt*(F(1,2)+P.rootiv(1+rt))
        mb=4*rt*(F(1,2)+P.rootiv(1+2*rt))
        gap=F(1,4)
    def val(t):return a*(ma*P.expiv(-2*t)+mb*P.expiv(-8*t))-gap
    if val(F(0)).b<=0:
        B=F(0);lo=hi=F(0)
    else:
        lo,hi=F(0),F(4)
        assert val(lo).a>0 and val(hi).b<0
        for _ in range(40):
            mid=(lo+hi)/2;vv=val(mid)
            if vv.a>0:lo=mid
            elif vv.b<0:hi=mid
            else:break
        assert val(lo).a>0 and val(hi).b<0
        B=(a*(ma*(1-P.expiv(-2*hi))/2+mb*(1-P.expiv(-8*hi))/8)-gap*lo).b
    L=(P.expiv(P.I(0,B))/P.rootiv(F(3,4))).b
    return L,{'parity':j,'spectral_gap_squared':2 if j==0 else 1,
              'growth_zero_bracket':[str(lo),str(hi)],'growth_integral_upper':str(B),
              'inverse_upper_exact':str(L),'inverse_upper_readout':float(L)}

def main():
    start=time.monotonic()
    D=P.build_parent_directions()
    v=E.scale(D['v'],F(10));g=E.scale(D['g'],F(100))
    p2=E.scale(D['psi'][0],F(100));p3=E.scale(D['psi'][1],F(1000))
    assert {parity(k)for k,_,_ in v}=={0}
    assert {parity(k)for A in [g,p2,p3]for k,_,_ in A}=={0}
    assert {k for k,_,_ in p2}.isdisjoint({k for k,_,_ in p3})
    assert not J.inst_product(p2,p3)
    for A in [p2,p3]:C.packet_check(A,True)
    # Exact character multiplication on integer inputs; analytic law is sum modulo 2.
    modes=[k for k in product(range(-2,3),repeat=3)if any(k)]
    for p,q in product(modes,modes):
        k=tuple(x+y for x,y in zip(p,q));assert parity(k)==(parity(p)+parity(q))%2
    assert min(E.sq(k) for k in modes if parity(k)==0)==2
    assert min(E.sq(k) for k in modes if parity(k)==1)==1
    # Nonzero odd input, with full conjugate partners, tests odd x odd -> even.
    oo={}
    for k,vec in [((1,0,0),s.Matrix([0,1,0])),((0,1,0),s.Matrix([0,0,1]))]:
        oo[k,E.sq(k),0]=vec;oo[tuple(-x for x in k),E.sq(k),0]=vec
    o=E.import_packets(oo);C.packet_check(o)
    B=lambda a,b:E.scale(E.ntime(a,b),F(-1))
    Bs=lambda a,b:E.scale(P.plus(B(a,b),B(b,a)),F(1,2))
    even=E.scale(p2,F(1,100));mix=P.plus(even,o)
    full=B(mix,mix)
    assert part(full,0)==P.plus(Bs(even,even),Bs(o,o))
    assert part(full,1)==E.scale(Bs(even,o),F(2))
    assert B(o,o) and not part(B(o,o),1)
    assert not part(P.linear(v,even),1) and not part(P.linear(v,o),0)
    # Parent all-time first-response bound and full all-output linear defect.
    temporal,w=P.temporal_certificate(g);assert w==F(3271,10000)
    n3=E.heat_derivative(p3)
    assert P.rootiv(P.ri(E.gram_expr(n3,n3))).b<F(16,125)
    K3=P.plus(E.ntime(v,p3),E.ntime(p3,v));c4=E.gram_expr(K3,K3)
    Cb=(P.I(F(909,200))/P.rootiv(F(3,2))).b
    def quantities(a,LE):
        vv=E.scale(v,a);d=P.plus(E.scale(p2,a*a),E.scale(p3,a**3))
        e=P.plus(P.linear(vv,d),E.scale(g,-a*a))
        assert e==E.scale(K3,-a**4)
        C.packet_check(d,True);C.packet_check(e)
        assert not part(e,1)
        en=P.rootiv(P.ri(E.gram_expr(e,e)))
        assert s.expand(E.gram_expr(e,e)-C.qsym(a)**8*c4)==0
        U=P.rootiv(P.I((w*a*a)**2+(F(16,125)*a**3)**2))
        return d,e,en,U.b+LE*en.b
    # Fully mixed perturbations: a=1/5, both cosets kept in the nonlinear map.
    a=F(1,5);LE=F(3919,1000);LO=F(741,125)
    AE=F(291,20);AO=F(2201,100);eta=F(13363,10**6)
    LEraw,ive=inv(a,0);LOraw,ivo=inv(a,1)
    assert LEraw<LE and LOraw<LO and LE*Cb<AE and LO*Cb<AO
    d,e,en,computed=quantities(a,LE);assert computed<eta
    rE=F(1,50);rO=F(1,200);delta=F(1,10000)
    he=(P.rootiv(F(3,4))*LE).b;ho=(P.rootiv(F(3,4))*LO).b
    marginE=rE-eta-he*delta-AE*(rE*rE+rO*rO)
    marginO=rO-ho*delta-2*AO*rE*rO
    assert marginE>0 and marginO>0
    # Weighted max norm max(||dE||,||dO||/2).
    qE=2*AE*rE+4*AE*rO
    qO=AO*rO+2*AO*rE
    assert qE<1 and qO<1
    # A lower certificate proves the previous shared-alpha scalar test fails.
    energy,_=J.running(d,F(17,100))
    lower=P.rootiv(energy).a-LE*en.b
    lower_r=J.floor(lower,10**7)
    assert lower_r>0 and 4*AO*lower_r>1
    mixed={'amplitude':'1/5','inverse_even':str(LE),'inverse_odd':str(LO),
           'alpha_even':str(AE),'alpha_odd':str(AO),'eta_even_base':str(eta),
           'eta_computed_upper':str(computed),'eta_computed_readout':float(computed),
           'r_even':str(rE),'r_odd':str(rO),'initial_perturbation_norm':'1/10000',
           'margin_even_lower':str(marginE),'margin_odd_lower':str(marginO),
           'margin_even_readout':float(marginE),'margin_odd_readout':float(marginO),
           'weighted_contraction_rows':[str(qE),str(qO)],
           'weighted_contraction_upper':str(max(qE,qO)),
           'total_trajectory_radius_squared':str(rE*rE+rO*rO),
           'linear_response_lower':str(lower_r),'shared_scalar_4alpha_lower':str(4*AO*lower_r),
           'growth_certificates':[ive,ivo]}
    print('PASS mixed cosets',float(marginE),float(marginO),'contraction',float(max(qE,qO)),flush=True)
    # Larger class with genuinely invariant even perturbations (not arbitrary perturbations).
    a2=F(213,1000);L2=F(547,125);A2=F(406,25);eta2=F(7617,500000)
    r2=F(29,1000);delta2=F(1,100000)
    lraw,iv2=inv(a2,0);assert lraw<L2 and L2*Cb<A2
    dd,ee,enn,eta_raw=quantities(a2,L2);assert eta_raw<eta2
    h2=(P.rootiv(F(3,4))*L2).b
    margin2=r2-eta2-h2*delta2-A2*r2*r2
    assert margin2>0 and 2*A2*r2<1
    invariant={'amplitude':str(a2),'inverse_even':str(L2),'alpha_even':str(A2),
               'eta_upper':str(eta2),'eta_computed_upper':str(eta_raw),
               'trajectory_radius':str(r2),'perturbation_radius':str(delta2),
               'perturbation_support':'coordinate-sum even Fourier sublattice',
               'margin_lower':str(margin2),'contraction':str(2*A2*r2),'growth_certificate':iv2}
    print('PASS invariant even',float(eta_raw),'margin',float(margin2),flush=True)
    result={'schema':'EM_EXACT_CHECK_RESULT_V1','status':'PASS',
       'record_id':'FINDING-EM-PDE-COSET-CAUSAL-BLOCK-20260910',
       'constant_dependency':'Bs bound 909/200 at canonical symmetric-polarization checkpoint 14',
       'full_Fourier_backend_sha256':hashlib.sha256(Path(E.__file__).read_bytes()).hexdigest(),
       'character':'(k1+k2+k3) mod 2','parity_addition_tests':len(modes)**2,
       'symmetry_is_exact_no_mode_decimation':True,'odd_odd_source_is_nonzero_and_retained':True,
       'complete_quadratic_identities_checked':True,
       'correction_packets':len(d),'complete_linear_defect_packets':len(e),
       'complete_linear_defect_modes':len({k for k,_,_ in e}),
       'full_defect_norm_squared_unit':str(c4),'first_response_certificate':temporal,
       'mixed_neighborhood':mixed,'invariant_neighborhood':invariant,
       'interval_extension':'Endpoint monotone envelopes dominate all 0<=a<=endpoint.',
       'viscosity_scaling':'u(t)=nu U(nu t); coefficients, errors and radii multiply by nu.',
       'PDE_time_space_sampling':False,'independent_peer_review':False,
       'limitations':['Conditional on stated inherited analytic estimates; no proof-assistant formalization.',
                     'Not arbitrary-initial-data global NS regularity.',
                     'The .213 endpoint requires even-sublattice perturbations; the .2 result does not.',
                     'The two labels are Fourier parity, not helicity and not primitive force count.'],
       'elapsed_seconds':time.monotonic()-start}
    (ROOT/'verification.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print('PASS complete',time.monotonic()-start,flush=True)
if __name__=='__main__':main()
