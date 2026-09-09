#!/usr/bin/env python3
"""Full-output, 3D rational Fourier experiment. No physical/continuum theorem.
Extends the parent's exact Gaussian-rational and radical arithmetic unchanged.
Run python ns_f0_full3d_d5c00d.py --output results.json
"""
from __future__ import annotations
from fractions import Fraction as F
from math import gcd
from functools import reduce
from collections import defaultdict
from pathlib import Path
import argparse, json, hashlib
from ns_f0_discrete_transfer_d5c00d import (GQ, ZERO, I, radical_bounds,
    rad_add, rad_scale, rad_clean, rad_serial, truncq)
K = tuple[int,int,int]
V = tuple[GQ,GQ,GQ]
Field = dict[K,V]
ZK=(0,0,0)
ZV=(ZERO,ZERO,ZERO)

def addk(p:K,q:K)->K: return tuple(a+b for a,b in zip(p,q))
def negk(k:K)->K: return tuple(-a for a in k)
def d(k:K)->int: return sum(a*a for a in k)
def plus(a:V,b:V)->V: return tuple(x+y for x,y in zip(a,b))
def times(c,a:V)->V: return tuple(c*x for x in a)
def dot(a,b)->GQ: return sum((GQ.of(x)*y for x,y in zip(a,b)),ZERO)
def ip(a:V,b:V)->F: return sum((x.conj()*y for x,y in zip(a,b)),ZERO).re
def norm2(a:V)->F: return sum((x.norm2() for x in a),F(0))
def conj(a:V)->V: return tuple(x.conj() for x in a)
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def clean(u:Field)->Field: return {k:v for k,v in u.items() if v!=ZV}
def add(u:Field,v:Field,c=1)->Field:
    return clean({k:plus(u.get(k,ZV),times(c,v.get(k,ZV))) for k in u.keys()|v.keys()})
def scale(c,u:Field)->Field: return clean({k:times(c,v) for k,v in u.items()})
def project(k:K,v:V)->V:
    if k==ZK: return ZV
    return plus(v,times(-dot(k,v)/d(k),tuple(GQ(x) for x in k)))
def representatives(u:Field): return sorted(k for k in u if k>negk(k))
def validate(u:Field):
    assert ZK not in u
    for k,v in u.items():
        assert dot(k,v)==ZERO
        assert u.get(negk(k))==conj(v)
def energy(u:Field)->F: return sum((norm2(v) for v in u.values()),F(0))/2

def weighted(u:Field,power:int=0):
    # 1/2 sum |k|^(2*power+1) |u_k|^2, a finite radical expression.
    out=defaultdict(F)
    for k,v in u.items(): out[d(k)]+=F(d(k))**power*norm2(v)/2
    return rad_clean(dict(out))
def modal_inner(u:Field,v:Field,power:int=0)->F:
    return sum((F(d(k))**power*ip(a,v.get(k,ZV)) for k,a in u.items()),F(0))
def wip(u:Field,v:Field,power:int=0):
    out=defaultdict(F)
    for k,a in u.items(): out[d(k)]+=F(d(k))**power*ip(a,v.get(k,ZV))
    return rad_clean(dict(out))

def bilinear(a:Field,b:Field,packets:bool=False):
    out={}; provenance=defaultdict(list)
    for p,ap in sorted(a.items()):
        for q,bq in sorted(b.items()):
            k=addk(p,q)
            if k==ZK: continue
            c=times(-I*dot(ap,q),project(k,bq))
            if c!=ZV:
                out[k]=plus(out.get(k,ZV),c)
                if packets: provenance[k].append((p,q,c))
    out=clean(out)
    return (out,dict(provenance)) if packets else out

def generator(u:Field,nu:F):
    n=bilinear(u,u)
    f=add(n,{k:times(-nu*d(k),a) for k,a in u.items()})
    return f,n

def primitive(v):
    g=reduce(gcd,(abs(x) for x in v),0)
    return tuple(x//g for x in v)
def basis(k:K):
    e=next(tuple(1 if i==j else 0 for i in range(3)) for j in range(3)
           if cross(k,tuple(1 if i==j else 0 for i in range(3)))!=(0,0,0))
    e=primitive(cross(k,e)); f=primitive(cross(k,e))
    assert dot(k,e)==dot(k,f)==dot(e,f)==ZERO
    return e,f

def quantize(u:Field,delta:F)->Field:
    if delta<=0: raise ValueError('delta must be positive')
    out={}
    for k in representatives(u):
        e,f=basis(k); v=u[k]
        a=dot(e,v)/sum(x*x for x in e); b=dot(f,v)/sum(x*x for x in f)
        a=GQ(truncq(a.re,delta),truncq(a.im,delta))
        b=GQ(truncq(b.re,delta),truncq(b.im,delta))
        w=plus(times(a,tuple(GQ(x) for x in e)),times(b,tuple(GQ(x) for x in f)))
        if w!=ZV: out[k]=w; out[negk(k)]=conj(w)
    validate(out)
    assert all(norm2(out.get(k,ZV))<=norm2(v) for k,v in u.items())
    return out

def adaptive_step(u:Field,nu:F,cap:F,delta:F):
    if nu<=0 or cap<=0 or delta<=0: raise ValueError("nu,cap,delta must be positive")
    validate(u)
    if not u: return {},{},F(0),{},{}
    f,n=generator(u,nu); validate(f)
    de=modal_inner(u,u,1); f2=2*energy(f)
    assert modal_inner(u,n)==0
    assert f2>0
    h=cap
    while h*f2>nu*de or h*nu*max(map(d,u))>1: h/=2
    raw=add(u,f,h); nxt=quantize(raw,delta)
    assert energy(raw)-energy(u)==-h*nu*de+h*h*f2/2
    assert energy(nxt)<=energy(raw)<energy(u)
    assert rad_add(weighted(raw),weighted(u),-1)==rad_add(
        rad_scale(h,rad_add(wip(u,n),wip(u,u,1),-nu)),rad_scale(h*h,weighted(f)))
    return nxt,raw,h,f,n

def seed(amplitude:int=32,sign:int=-1)->Field:
    A=GQ(amplitude); C=GQ(0,sign*amplitude)
    pos={(1,0,0):(ZERO,A,ZERO),(0,1,0):(ZERO,ZERO,A),(0,0,1):(A,ZERO,ZERO),
         (1,1,0):(ZERO,ZERO,C),(0,1,1):(C,ZERO,ZERO),(1,0,1):(ZERO,C,ZERO)}
    return clean({**pos,**{negk(k):conj(v) for k,v in pos.items()}})

def serial_field(u:Field):
    return {','.join(map(str,k)):[a.serial() for a in v] for k,v in sorted(u.items())}
def serial_bounds(r,bits=40):
    a,b=radical_bounds(r,bits); return [str(a),str(b)]

def initial_report():
    res=[]
    for sg in [-1,1]:
        u=seed(32,sg); nu=F(1); delta=F(1,64); cap=F(1,4096)
        assert quantize(u,delta)==u
        y,raw,h,f,n=adaptive_step(u,nu,cap,delta)
        t=wip(u,n); lin=rad_add(t,wip(u,u,1),-nu)
        dk=rad_add(weighted(y),weighted(u),-1)
        omega={k:times(I,cross(tuple(GQ(x) for x in k),v)) for k,v in u.items()}
        stretch=scale(-1,bilinear(omega,u)) # projection does not alter pairing with omega
        enst=modal_inner(omega,stretch)
        assert enst==modal_inner(u,n,1)
        res.append({'sign':sg,'h':str(h),'energy':str(energy(u)),
          'energy_change':str(energy(y)-energy(u)),
          'raw_energy_change':str(energy(raw)-energy(u)),
          'transfer':rad_serial(t),'linear_K_change':rad_serial(rad_scale(h,lin)),
          'time_discrete_K_defect':rad_serial(rad_scale(h*h,weighted(f))),
          'precision_K_defect':rad_serial(rad_add(weighted(y),weighted(raw),-1)),
          'K_change':rad_serial(dk),'K_bounds':serial_bounds(dk),
          'enstrophy_stretching_production':str(enst),
          'initial_modes':len(u),'generator_modes':len(f),'raw_modes':len(raw),
          'quantized_modes':len(y),'new_raw_modes':len(raw.keys()-u.keys()),
          'initial':serial_field(u),'next':serial_field(y)})
    return res


def linear_reference(u:Field,eta:F,nu:F)->Field:
    """Fixed backward-Euler reference, not a new force or the actual time step."""
    if eta<=0 or nu<=0: raise ValueError('eta,nu>0 required')
    return {k:times(1/(1+eta*nu*d(k)),v) for k,v in u.items()}

def gram(u:Field,eta:F,nu:F,diagnostics:bool=False):
    n,pkts=bilinear(u,u,True)
    ans=defaultdict(F); group_count=0; packet_count=0; outputs_cancelled=0
    for k,ps in pkts.items():
        # Keep (k,p,q) in ps. Equal-rate grouping is ONLY for this reference observer.
        groups={}
        for p,q,c in ps:
            rho=1/((1+eta*nu*d(p))*(1+eta*nu*d(q)))
            assert 0<rho<1
            groups[rho]=plus(groups.get(rho,ZV),c)
        packet_count+=len(ps); group_count+=len(groups)
        if k not in n: outputs_cancelled+=1
        c=F(0)
        for r,a in groups.items():
            for t,b in groups.items(): c+=ip(a,b)/(1-r*t)
        assert c>=0 # direct exact certificate in every executed example
        ans[d(k)]+=c/d(k)
    out=rad_clean(dict(ans))
    return (out,{'ordered_packets':packet_count,'output_ports':len(pkts),
                 'rate_groups':group_count,'cancelled_outputs':outputs_cancelled}) if diagnostics else out

def residual_readout(u:Field):
    return rad_scale(2,weighted(bilinear(u,u),-1))

def gram_ledger(u:Field,raw:Field,y:Field,h:F,eta:F,nu:F):
    ju,diag=gram(u,eta,nu,True); hu=linear_reference(u,eta,nu)
    jh=gram(hu,eta,nu); r=residual_readout(u)
    assert rad_add(ju,jh,-1)==r
    lin={k:times(1-h*nu*d(k),v) for k,v in u.items()}
    jl=gram(clean(lin),eta,nu); ja=gram(raw,eta,nu); jy=gram(y,eta,nu)
    temporal=rad_add(jl,jh,-1); feed=rad_add(ja,jl,-1); precision=rad_add(jy,ja,-1)
    lhs=rad_add(rad_add(jy,ju,-1),r)
    assert lhs==rad_add(rad_add(feed,temporal),precision)
    return {'J_before':rad_serial(ju),'R':rad_serial(r),
      'feedback':rad_serial(feed),'time_discretization':rad_serial(temporal),
      'precision':rad_serial(precision),'budget_identity_exact':True,
      'feedback_bounds':serial_bounds(feed),'precision_bounds':serial_bounds(precision),
      'packet_diagnostics':diag}

def affine_defect(u:Field,h:F,f:Field,nu:F):
    r1=add({k:times(nu*d(k),v) for k,v in f.items()},bilinear(u,f),-1)
    r1=add(r1,bilinear(f,u),-1); r2=scale(-1,bilinear(f,f))
    for s in [F(0),h/2,h]:
        v=add(u,f,s)
        actual=add(add(f,{k:times(nu*d(k),a) for k,a in v.items()}),bilinear(v,v),-1)
        assert actual==add(scale(s,r1),r2,s*s)
    ub=4*h*h*energy(r1)+4*h**4*energy(r2)
    return {'R1_squared_norm':str(2*energy(r1)),'R2_squared_norm':str(2*energy(r2)),
            'sup_slab_squared_bound':str(ub),'exact_checks_at_zero_half_end':True,
            'has_nonzero_time_defect':bool(r1 or r2)}

def determinant(a):
    a=[row[:] for row in a]; n=len(a); sign=1; ans=F(1)
    for j in range(n):
        p=next((i for i in range(j,n) if a[i][j]),None)
        if p is None: return F(0)
        if p!=j: a[p],a[j]=a[j],a[p]; sign=-sign
        q=a[j][j]; ans*=q
        for i in range(j+1,n):
            c=a[i][j]/q
            for k in range(j+1,n): a[i][k]-=c*a[j][k]
    return sign*ans

def cauchy_determinant(rs):
    num=F(1);den=F(1)
    for i,r in enumerate(rs):
        den*=1-r*r
        for s in rs[:i]: num*=(r-s)**2; den*=(1-r*s)**2
    return num/den

def random_field(rng,amp=3,count=4):
    out={}
    while len(out)<2*count:
        k=tuple(rng.randint(-2,2) for _ in range(3))
        if k==ZK: continue
        if k<negk(k): k=negk(k)
        e,f=basis(k)
        a=GQ(rng.randint(-amp,amp),rng.randint(-amp,amp))
        b=GQ(rng.randint(-amp,amp),rng.randint(-amp,amp))
        v=plus(times(a,tuple(GQ(x) for x in e)),times(b,tuple(GQ(x) for x in f)))
        if v!=ZV: out[k]=v;out[negk(k)]=conj(v)
    return out

def tests():
    from random import Random
    rng=Random(2026090907); count=12
    for j in range(count):
        u=random_field(rng,count=3+(j%3)); a=random_field(rng,count=3); b=random_field(rng,count=3)
        validate(u)
        assert modal_inner(u,bilinear(a,b))==-modal_inner(b,bilinear(a,u))
        y,raw,h,f,n=adaptive_step(u,F(1),F(1,4096),F(1,16))
        assert (energy(y)/F(1,16)**2).denominator==1
        assert energy(y)<energy(u)
        g=gram(u,F(1,4096),F(1)); gh=gram(linear_reference(u,F(1,4096),F(1)),F(1,4096),F(1))
        assert rad_add(g,gh,-1)==residual_readout(u)
    node_cases=[[F(1,5)],[F(-1,2),F(2,3)],[F(0),F(1,3),F(2,3)],
       [F(-3,4),F(-1,2),F(1,4),F(3,4)],[F(1,7),F(2,7),F(3,7),F(4,7),F(5,7)],
       [F(1,3),F(1,3),F(2,3)]]
    for rs in node_cases:
        assert determinant([[1/(1-r*s) for s in rs] for r in rs])==cauchy_determinant(rs)
    k=(1,2,0); v=(GQ(F(2,5)),GQ(F(-1,5)),ZERO); assert dot(k,v)==ZERO
    naive=tuple(GQ(truncq(x.re,F(1,4)),truncq(x.im,F(1,4))) for x in v)
    assert dot(k,naive)==GQ(F(1,4))
    return {'random_cases':count,'skew_identity_exact':True,'gram_identity_exact':True,
            'cauchy_determinant_cases':len(node_cases),'naive_rounding_divergence':'1/4'}

def trajectory(steps=12,amplitude=32,delta=F(1,64)):
    u=seed(amplitude); nu=F(1); cap=F(1,4096); t=F(0);rows=[]
    initial=u
    for j in range(steps):
        if not u:break
        y,raw,h,f,n=adaptive_step(u,nu,cap,delta); t+=h
        e=add(y,raw,-1); dk=rad_add(weighted(y),weighted(u),-1)
        pred=rad_scale(h,rad_add(wip(u,n),wip(u,u,1),-nu))
        td=rad_scale(h*h,weighted(f)); qd=rad_add(weighted(y),weighted(raw),-1)
        assert dk==rad_add(rad_add(pred,td),qd)
        assert radical_bounds(qd)[1]<=0
        rows.append({'step':j+1,'h':str(h),'time':str(t),'input_modes':len(u),
          'all_generator_modes':len(f),'raw_modes':len(raw),'grid_modes':len(y),
          'ports_erased_by_quantization':len(raw.keys()-y.keys()),
          'max_wavenumber_squared':max(map(d,y),default=0),
          'energy':str(energy(y)),'energy_change':str(energy(y)-energy(u)),
          'rounding_energy_loss':str(energy(raw)-energy(y)),
          'rounding_squared_error':str(2*energy(e)),
          'K_change':rad_serial(dk),'signed_generator_change':rad_serial(pred),
          'time_discrete_K_defect':rad_serial(td),'precision_K_defect':rad_serial(qd),
          'cutoff_defect':'0 (no spectral cutoff is applied)',
          'solenoidal_and_reality_exact':True})
        u=y
    return {'rows':rows,'final':serial_field(u),'final_energy':str(energy(u)),
        'cumulative_K_change':rad_serial(rad_add(weighted(u),weighted(initial),-1)),
        'cumulative_K_bounds':serial_bounds(rad_add(weighted(u),weighted(initial),-1)),
        'quantization_extinction_step_bound':str(energy(initial)/delta**2),
        'extinction_observed':not bool(u)}

def sqrt_fraction_bounds(x:F,bits=72):
    from math import isqrt
    if x<0: raise ValueError('negative square root')
    den=1<<bits; z=isqrt((x.numerator*den*den)//x.denominator)
    lo=F(z,den)
    hi=lo if z*z*x.denominator==x.numerator*den*den else F(z+1,den)
    return lo,hi

def chi_bounds(u:Field,power:int):
    lo=hi=F(0)
    for k,v in u.items():
        a,b=sqrt_fraction_bounds(norm2(v)*F(d(k))**power)
        lo+=a;hi+=b
    return lo,hi

def small_data_certificate():
    # This test exercises a general finite-sum theorem proved in the note.
    nu=F(1); a=F(1,5); epsilon=nu-a; delta=F(1,8192)
    u=seed(F(1,64)); initial_bounds=chi_bounds(u,-1)
    assert initial_bounds[1]<a
    diss_hi=F(0); nl_hi=F(0); rows=[]
    for j in range(16):
        if not u: break
        y,raw,h,f,n=adaptive_step(u,nu,F(1,64),delta)
        xm=chi_bounds(u,-1); xp=chi_bounds(u,1); xn=chi_bounds(n,-1)
        # Quantization is modewise norm contracting; exact finite proof supplies
        # chi_-1(next) <= chi_-1(u)-h*(nu-chi_-1(u))*chi_1(u).
        ychi=chi_bounds(y,-1)
        diss_hi+=h*xp[1]; nl_hi+=h*xn[1]
        assert ychi[1]+epsilon*diss_hi <= initial_bounds[0]
        assert ychi[1]<a
        assert nl_hi<=a*a/epsilon
        rows.append({'step':j+1,'h':str(h),'chi_minus_upper':str(ychi[1]),
          'cumulative_h_chi_plus_upper':str(diss_hi),'cumulative_nonlinearity_upper':str(nl_hi),
          'uniform_budget_certified':True,'grid_modes':len(y)})
        u=y
    return {'a':'1/5','nu':'1','epsilon':'4/5','delta':str(delta),
      'initial_chi_minus_bounds':[str(x) for x in initial_bounds],
      'all_step_dissipation_bound':'1/4','all_step_nonlinearity_bound':'1/20',
      'steps':len(rows),'rows':rows,'cutoff_applied':False,
      'claim':'finite recurrence theorem; no continuous-time limit claimed'}

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--output',default='results.json'); args=parser.parse_args()
    parent=Path(__file__).with_name('ns_f0_discrete_transfer_d5c00d.py')
    assert hashlib.sha256(parent.read_bytes()).hexdigest()=='b3feb31d191fe17148a7c14505ddbb98aa5eb274a31c9053158a680a26460bdb'
    u=seed(); y,raw,h,f,n=adaptive_step(u,F(1),F(1,4096),F(1,64))
    pairs=initial_report()
    assert pairs[0]['h']==pairs[1]['h']=='1/4096'
    assert pairs[0]['energy_change']==pairs[1]['energy_change']=='-1259/256'
    assert radical_bounds(rad_add(weighted(y),weighted(u),-1))[0]>14
    v=seed(sign=1); z,_,_,_,_=adaptive_step(v,F(1),F(1,4096),F(1,64))
    assert radical_bounds(rad_add(weighted(z),weighted(v),-1))[1]<-25
    report={'schema':'EM_NS_FULL3D_FINITE_EXACT_V1','event':'NS-F0-FULL3D-20260909-D5C00D-07',
     'arithmetic':'Gaussian rationals plus rational enclosures for finite radicals',
     'parameters':{'nu':'1','cap':'1/4096','delta':'1/64','reference_eta':'1/4096'},
     'first_steps':pairs,'gram_ledger':gram_ledger(u,raw,y,h,F(1,4096),F(1)),
     'affine_time_defect':affine_defect(u,h,f,F(1)),
     'regressions':tests(),'small_data':small_data_certificate(),'trajectory':trajectory(),
     'not_claimed':['continuum NS solution','finite-time blowup','native six-dimensional law',
      'independent review','Lean validation','uniform resolution-to-zero theorem']}
    Path(args.output).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'first_step_energy_change':pairs[0]['energy_change'],
       'positive_K_bounds':pairs[0]['K_bounds'],'negative_K_bounds':pairs[1]['K_bounds'],
       'gram_identity':report['gram_ledger']['budget_identity_exact'],
       'regressions':report['regressions'],'small_data_steps':report['small_data']['steps'],'trajectory_steps':len(report['trajectory']['rows']),
       'final_modes':len(report['trajectory']['final']),'final_energy':report['trajectory']['final_energy'],
       'cumulative_K_bounds':report['trajectory']['cumulative_K_bounds']},indent=2))

if __name__=='__main__':main()
