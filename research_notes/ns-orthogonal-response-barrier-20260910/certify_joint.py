#!/usr/bin/env python3
"""Causal support orthogonality and dictionary-independent certificate obstruction.
Exact parent Fourier algebra is reused unchanged. No PDE sampling, no discarded outputs.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
import hashlib,json,sys,time
import sympy as s
ROOT=Path(__file__).resolve().parent
PAR=next((p for p in [ROOT/'parent',ROOT.parent/'ns-goal-primal-dual-certificate-20260910'] if (p/'certify_goal.py').is_file()),None)
if PAR is None: raise FileNotFoundError('pinned certify_goal.py dependency required')
expected='954caee644e7a251e7a4631bf94cdca32dd19cd14d7d9577506235b2f59c9a81'
assert hashlib.sha256((PAR/'certify_goal.py').read_bytes()).hexdigest()==expected
sys.path.insert(0,str(PAR))
import certify_goal as C
P=C.P;E=P.E
if not __debug__:raise RuntimeError('Assertions are required; do not use -O')
OUT=ROOT/'output';OUT.mkdir(exist_ok=True)

def inst_product(A,B):
    """Exact real same-output pairing, BEFORE Sobolev weighting or time integration."""
    by=defaultdict(list)
    for (k,r,m),v in B.items():by[k].append((r,m,v))
    out={}
    for (k,ra,ma),aa in A.items():
        for rb,mb,bb in by[k]:
            a,b=P.real_inner(aa,bb);key=(E.sq(k),ra+rb,ma+mb)
            old=out.get(key,(F(0),F(0)));out[key]=(old[0]+a,old[1]+b)
    return {k:v for k,v in out.items()if v!=(0,0)}

def weighted(raw,power):
    out=defaultdict(lambda:s.S.Zero)
    for (n,r,m),(a,b) in raw.items():
        out[r,m]+=s.Integer(n)**s.Rational(power,2)*(C.qsym(a)+C.qsym(b)*s.sqrt(2))
    return {k:s.expand(v)for k,v in out.items()if v!=0}

def integrate(poly):
    out=defaultdict(lambda:s.S.Zero);const=s.S.Zero
    for (r,m),v in poly.items():
        fac=s.factorial(m);const+=v*fac/s.Integer(r)**(m+1)
        for j in range(m+1):out[r,j]-=v*fac/(s.factorial(j)*s.Integer(r)**(m-j+1))
    return s.expand(const),{k:s.expand(v)for k,v in out.items()if v!=0}

def derivative(poly):
    out=defaultdict(lambda:s.S.Zero)
    for (r,m),v in poly.items():
        out[r,m]-=r*v
        if m:out[r,m-1]+=m*v
    return {k:s.expand(v)for k,v in out.items()if s.expand(v)!=0}

def addpoly(*pairs):
    out=defaultdict(lambda:s.S.Zero)
    for factor,poly in pairs:
        for key,v in poly.items():out[key]+=factor*v
    return {k:s.expand(v)for k,v in out.items()if s.expand(v)!=0}

def at(const,poly,t):
    ans=P.ri(const)
    for (r,m),v in poly.items():ans+=P.ri(v)*P.expiv(-r*t)*t**m
    return ans

def running(d,t,c=F(3,4)):
    raw=inst_product(d,d);H=weighted(raw,1);D=weighted(raw,3)
    cn,Ip=integrate(D)
    assert derivative(Ip)==D
    assert s.expand(cn+sum((v for (r,m),v in Ip.items()if m==0),s.S.Zero))==0
    assert s.expand(cn-E.gram_expr(d,d,power=3))==0
    energy=addpoly((s.S.One,H),(C.qsym(c),Ip))
    assert derivative(energy)==addpoly((s.S.One,derivative(H)),(C.qsym(c),D))
    result=at(C.qsym(c)*cn,energy,t)
    assert result.a>0
    return result,len(energy)

def ceiling(x,den=10**10):return F((F(x)*den).__ceil__(),den)
def floor(x,den=10**10):return F((F(x)*den).__floor__(),den)
def view(iv):return {'lower':str(iv.a),'upper':str(iv.b),'lower_readout':float(iv.a),'upper_readout':float(iv.b)}

def main():
    start=time.monotonic();data=P.build_parent_directions()
    v=E.scale(data['v'],F(10));g=E.scale(data['g'],F(100))
    h2=E.scale(data['psi'][0],F(100));h3=E.scale(data['psi'][1],F(1000))
    C.packet_check(v);C.packet_check(h2,True);C.packet_check(h3,True)
    low={key:val for key,val in v.items()if E.sq(key[0])==2}
    high={key:val for key,val in v.items()if E.sq(key[0])==8}
    assert not E.ntime(low,low) and not E.ntime(high,high)
    ks=[(1,1,0),(1,0,1),(0,1,1),(2,-2,0)]
    kernel=s.Matrix(ks).T.nullspace();assert kernel==[s.Matrix([0,-2,2,1])]
    neg=lambda k:tuple(-x for x in k)
    L=ks[:3]+[neg(k)for k in ks[:3]];J=[ks[3],neg(ks[3])]
    ad=lambda *aa:tuple(map(sum,zip(*aa)))
    support2={ad(x,y)for x,y in product(L,J)}
    support3={ad(x,y,z)for x,y,z in product(L,L,J)}|{ad(x,y,z)for x,y,z in product(L,J,J)}
    assert support2.isdisjoint(support3)
    assert {k for k,_,_ in h2}<=support2 and {k for k,_,_ in h3}<=support3
    assert inst_product(h2,h3)=={}
    n3=E.heat_derivative(h3);K3=P.plus(E.ntime(v,h3),E.ntime(h3,v))
    c3=E.gram_expr(n3,n3);c4=E.gram_expr(K3,K3)
    c3n=P.rootiv(P.ri(c3));assert c3n.b<F(16,125)
    temporal,w=P.temporal_certificate(g);assert w==F(3271,10000)
    rows=[]
    for amp in [F(157,1000),F(4,25)]:
        vv=E.scale(v,amp);d=P.plus(E.scale(h2,amp**2),E.scale(h3,amp**3))
        e=P.plus(P.linear(vv,d),E.scale(g,-amp**2))
        assert e==E.scale(K3,-amp**4)
        C.packet_check(d,True);C.packet_check(e)
        en=P.rootiv(P.ri(E.gram_expr(e,e)))
        assert s.expand(E.gram_expr(e,e)-C.qsym(amp)**8*c4)==0
        inv,Lraw,Cb=P.inverse_certificate(amp)
        Lbound=ceiling(Lraw,10**8);alpha=ceiling(Lbound*Cb,10**8)
        # The very same fixed constants as the previous dual obstruction at .16.
        if amp==F(4,25):
            Lbound=F(200630557,50000000);alpha=F(1556725999,50000000)
        assert Lraw<Lbound and Lbound*Cb<alpha
        U=P.rootiv(P.I((amp**2*w)**2+(amp**3*F(16,125))**2))
        Usplit=amp**2*w+amp**3*F(16,125)
        assert U.b<Usplit
        eta=U.b+Lbound*en.b
        t0=F(17,100);eng,terms=running(d,t0);dlo=P.rootiv(eng).a
        hlo=dlo-Lbound*en.b
        row={'amplitude':str(amp),'inverse_upper':str(Lbound),'alpha_upper':str(alpha),
             'support2_modes':len(support2),'support3_modes':len(support3),
             'correction_packets':len(d),'complete_linear_defect_packets':len(e),
             'complete_linear_defect_modes':len({k for k,_,_ in e}),
             'defect_norm':view(en),'split_norm_upper':str(Usplit),
             'orthogonal_norm_upper':str(U.b),'eta_upper':str(eta),
             'eta_upper_readout':float(eta),'test_time':str(t0),'running_energy_at_test':view(eng),
             'exact_response_norm_lower':str(hlo),'exact_response_lower_readout':float(hlo),
             'scalar_running_terms':terms,'inverse_certificate':inv}
        if amp==F(157,1000):
            etar=ceiling(eta);r=F(3,200)
            assert etar+alpha*r*r<r and 2*alpha*r<1
            row.update({'status':'GLOBAL_FULL_NS_CERTIFICATE','eta_rational':str(etar),'radius':str(r),
                        'ball_margin':str(r-etar-alpha*r*r),'contraction':str(2*alpha*r),
                        '4alpha_eta':str(4*alpha*etar)})
        else:
            lower=floor(hlo);assert lower>0 and 4*alpha*lower>1
            row.update({'status':'DICTIONARY_INDEPENDENT_FIXED_MAJORANT_OBSTRUCTION',
                'response_lower_rational':str(lower),'4alpha_lower':str(4*alpha*lower),
                'necessary_alpha_upper':str(1/(4*lower)),
                'alpha_reduction_fraction_required':str(1-1/(4*lower*alpha)),
                'scope':'Every trial dictionary using this fixed reference and this fixed scalar alpha; not NS blow-up.'})
        rows.append(row)
        print(amp,row['status'],'upper_eta',float(eta),'lower_h0',float(hlo),flush=True)
    result={'status':'PASS','record_id':'FINDING-EM-PDE-ORTHOGONAL-RESPONSE-BARRIER-20260910',
            'parent_goal_sha256':expected,'backend_sha256':hashlib.sha256(Path(E.__file__).read_bytes()).hexdigest(),
            'kernel_generator':[0,-2,2,1],'generic_two_layer_support_disjoint':True,
            'c3_exact':str(c3),'c4_exact':str(c4),'c3_readout':float(c3),'c4_readout':float(c4),
            'unit_response_temporal_certificate':temporal,'cases':rows,
            'exact_derivative_and_integral_checks':True,'full_outputs_retained':True,
            'PDE_simulation':False,'all_time_upper_via_orthogonality_and_analytic_heat_bounds':True,
            'single_time_used_only_as_lower_bound':True,
            'limits':['Analytic parents including C*=9.503 and the all-mode inverse remain dependencies.',
                      'Not independent peer review or a proof-assistant formalization.',
                      'No arbitrary-data regularity or historical novelty claim.',
                      'No temporal sampling is promoted to a uniform upper bound.',
                      'The obstruction is for a fixed scalar feedback majorant, not the exact nonlinear solution.'],
            'elapsed_seconds':time.monotonic()-start}
    (OUT/'verification.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print('PASS',time.monotonic()-start,flush=True)
if __name__=='__main__':main()
