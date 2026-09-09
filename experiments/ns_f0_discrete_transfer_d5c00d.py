#!/usr/bin/env python3
"""Exact rational, finite-resolution autonomous NS-carrier certificate.

No floating-point decisions, continuous-time integration, external force,
assumed singular profile, or unproved infinite-cutoff limit is used.
This is a finite-model certificate, not a Navier--Stokes blow-up proof.
Run: python checker.py --output results.json
Python standard library only.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt
from random import Random
import argparse
import json
from pathlib import Path
from typing import Dict, Tuple, Union

Scalar = Union[int, F]

@dataclass(frozen=True)
class GQ:
    re: F = F(0)
    im: F = F(0)
    def __post_init__(self):
        object.__setattr__(self, 're', F(self.re))
        object.__setattr__(self, 'im', F(self.im))
    @staticmethod
    def of(x: Union['GQ', Scalar]) -> 'GQ':
        return x if isinstance(x, GQ) else GQ(F(x))
    def __add__(self, x):
        x = GQ.of(x); return GQ(self.re+x.re, self.im+x.im)
    __radd__ = __add__
    def __neg__(self): return GQ(-self.re, -self.im)
    def __sub__(self, x): return self + (-GQ.of(x))
    def __rsub__(self, x): return GQ.of(x) + (-self)
    def __mul__(self, x):
        x=GQ.of(x)
        return GQ(self.re*x.re-self.im*x.im, self.re*x.im+self.im*x.re)
    __rmul__ = __mul__
    def __truediv__(self, x):
        x=GQ.of(x); d=x.norm2()
        if not d: raise ZeroDivisionError('Gaussian rational zero divisor')
        n=self*x.conj(); return GQ(n.re/d, n.im/d)
    def conj(self): return GQ(self.re, -self.im)
    def norm2(self) -> F: return self.re*self.re+self.im*self.im
    def serial(self): return [str(self.re),str(self.im)]

ZERO=GQ(); I=GQ(0,1)

@dataclass(frozen=True)
class State:
    m: int
    b: F
    a: Tuple[GQ,...]
    def __post_init__(self):
        if self.m < 1 or len(self.a) != 2*self.m+1:
            raise ValueError('m>=1 and len(a)=2*m+1 required')
        object.__setattr__(self, 'b', F(self.b))
    def at(self,j:int) -> GQ:
        return self.a[j+self.m] if -self.m <= j <= self.m else ZERO
    def serial(self):
        return {'m':self.m,'b':str(self.b),'a':{str(j):self.at(j).serial()
                for j in range(-self.m,self.m+1) if self.at(j)!=ZERO}}

def state(m:int,b:Scalar, a:Dict[int,GQ]) -> State:
    return State(m,F(b),tuple(a.get(j,ZERO) for j in range(-m,m+1)))

def combine(x:State,y:State,s:Scalar=1) -> State:
    if x.m!=y.m: raise ValueError('Different carriers')
    return State(x.m,x.b+F(s)*y.b,tuple(a+F(s)*b for a,b in zip(x.a,y.a)))

def scale(s:Scalar,x:State)->State:
    return State(x.m,F(s)*x.b,tuple(F(s)*a for a in x.a))

def vector_field(x:State,nu:Scalar=1)->State:
    nu=F(nu)
    return State(x.m,-nu*x.b,tuple(-nu*(1+j*j)*x.at(j)
          -I*x.b/2*(x.at(j-1)+x.at(j+1)) for j in range(-x.m,x.m+1)))

def exact_step(x:State,h:Scalar,nu:Scalar=1)->Tuple[State,State]:
    """Unique implicit-midpoint update, solved by exact tridiagonal algebra."""
    h,nu=F(h),F(nu)
    if h<=0 or nu<=0: raise ValueError('h and nu must be positive')
    beta=x.b/(1+h*nu/2)
    off=I*h*beta/4
    diag=[F(1)+h*nu*(1+j*j)/2 for j in range(-x.m,x.m+1)]
    piv=[]; rhs=[]
    for k,d in enumerate(diag):
        if k==0: p=GQ(d); r=x.a[k]
        else:
            p=GQ(d)-off*off/piv[k-1]
            r=x.a[k]-off*rhs[k-1]/piv[k-1]
        assert p.im==0 and p.re>0, 'positive pivot proof violated'
        piv.append(p); rhs.append(r)
    mid=[ZERO]*len(diag)
    for k in range(len(diag)-1,-1,-1):
        mid[k]=(rhs[k]-(off*mid[k+1] if k+1<len(mid) else ZERO))/piv[k]
    z=State(x.m,beta,tuple(mid))
    y=combine(scale(2,z),x,-1)
    return y,z

def energy(x:State)->F:
    return (x.b*x.b+sum((a.norm2() for a in x.a),F(0)))/4

def dissipation(x:State)->F:
    return (x.b*x.b+sum((F(1+j*j)*x.at(j).norm2()
                    for j in range(-x.m,x.m+1)),F(0)))/2

Radical=Dict[int,F]
def rad_clean(r:Radical)->Radical:
    return {d:c for d,c in r.items() if c}
def rad_add(x:Radical,y:Radical,s:Scalar=1)->Radical:
    r=dict(x)
    for d,c in y.items(): r[d]=r.get(d,F(0))+F(s)*c
    return rad_clean(r)
def rad_scale(s:Scalar,x:Radical)->Radical:
    return rad_clean({d:F(s)*c for d,c in x.items()})
def critical(x:State)->Radical:
    r={1:x.b*x.b/2}
    for j in range(-x.m,x.m+1):
        d=1+j*j; r[d]=r.get(d,F(0))+x.at(j).norm2()/2
    return rad_clean(r)
def critical_dissipation(x:State)->Radical:
    r={1:x.b*x.b}
    for j in range(-x.m,x.m+1):
        d=1+j*j; r[d]=r.get(d,F(0))+d*x.at(j).norm2()
    return rad_clean(r)
def transfer(x:State)->Radical:
    r={}
    for j in range(-x.m,x.m):
        c=x.b*(x.at(j).conj()*x.at(j+1)).im/2
        d,e=1+j*j,1+(j+1)*(j+1)
        r[d]=r.get(d,F(0))+c; r[e]=r.get(e,F(0))-c
    return rad_clean(r)
def radical_bounds(r:Radical,bits:int=80)->Tuple[F,F]:
    den=1<<bits; lo=hi=F(0)
    for d,c in r.items():
        k=isqrt(d*den*den); l=F(k,den)
        u=l if k*k==d*den*den else F(k+1,den)
        lo+=c*(l if c>=0 else u); hi+=c*(u if c>=0 else l)
    return lo,hi

def rad_serial(r:Radical): return {str(d):str(c) for d,c in sorted(r.items())}
def truncq(x:F,delta:F)->F:
    return delta*int(x/delta) # Fraction -> int truncates toward zero.
def quantize(x:State,delta:Scalar)->State:
    delta=F(delta)
    if delta<=0: raise ValueError('delta must be positive')
    return State(x.m,truncq(x.b,delta),tuple(GQ(truncq(a.re,delta),truncq(a.im,delta)) for a in x.a))

def verify_step(x:State,y:State,z:State,h:F,nu:F)->None:
    assert combine(y,x,-1)==scale(h,vector_field(z,nu))
    assert combine(y,x)==scale(2,z)
    assert energy(y)-energy(x)==-h*nu*dissipation(z)
    rhs=rad_scale(h,rad_add(transfer(z),critical_dissipation(z),-nu))
    assert rad_add(critical(y),critical(x),-1)==rhs

def heat_multiplier(j:int,h:F,nu:F)->F:
    t=h*nu*(1+j*j)/2
    return (1-t)/(1+t)

def heat_reference(x:State,h:F,nu:F)->State:
    return State(x.m,heat_multiplier(0,h,nu)*x.b,
                 tuple(heat_multiplier(j,h,nu)*x.at(j) for j in range(-x.m,x.m+1)))

def residual_gram(x:State,h:F,nu:F)->Radical:
    """Finite Cauchy Gram; full output j=-m-1,...,m+1 is retained.

    Weight 1/sqrt(1+j*j) is recorded as sqrt(d)/d.
    Kernel positivity is proved in note.md by its exact 2-by-2 determinant.
    No infinite sum is evaluated or used as a numerical certificate.
    """
    out={}; rb=heat_multiplier(0,h,nu)
    for j in range(-x.m-1,x.m+2):
        terms=[(x.at(k),rb*heat_multiplier(k,h,nu)) for k in [j-1,j+1]
               if -x.m<=k<=x.m]
        c=F(0)
        for a,r in terms:
            for b,s in terms:
                assert abs(r)<1 and abs(s)<1
                c+=(a.conj()*b).re/(1-r*s)
        d=1+j*j
        out[d]=out.get(d,F(0))+x.b*x.b*c/(8*d)
    return rad_clean(out)

def full_source_action(x:State)->Radical:
    out={}
    for j in range(-x.m-1,x.m+2):
        source=-I*x.b/2*(x.at(j-1)+x.at(j+1))
        d=1+j*j
        out[d]=out.get(d,F(0))+source.norm2()/(2*d)
    return rad_clean(out)

def edge_defect_squared(x:State)->F:
    return x.b*x.b*(x.at(-x.m).norm2()+x.at(x.m).norm2())/8

def witnesses()->dict:
    h,nu,delta=F(1,64),F(1),F(1,4)
    mid=state(2,32,{0:GQ(32),-1:GQ(0,-16),1:GQ(0,-16)})
    x=combine(mid,vector_field(mid,nu),-h/2)
    y=combine(mid,vector_field(mid,nu),h/2)
    actual,z=exact_step(x,h,nu); assert actual==y and z==mid
    verify_step(x,y,z,h,nu)
    dk=rad_add(critical(y),critical(x),-1)
    assert dk=={1:F(-288),2:F(240)}
    assert radical_bounds(dk)[0]>0
    assert quantize(x,delta)==x and quantize(y,delta)==y
    assert energy(y)-energy(x)==-24
    cutoff_checks=[]
    for m in [2,3,5,8]:
        zz=state(m,mid.b,{j:mid.at(j) for j in range(-2,3)})
        xx=combine(zz,vector_field(zz),-h/2)
        yy=combine(zz,vector_field(zz),h/2)
        oo,mm=exact_step(xx,h)
        assert oo==yy and mm==zz
        assert rad_add(critical(yy),critical(xx),-1)==dk
        cutoff_checks.append(m)
    # BRC counterexample uses SAME initial modal energies, not just equal midpoints.
    p=mid
    n=state(2,32,{0:GQ(32),-1:GQ(0,16),1:GQ(0,16)})
    assert p.b==n.b and [a.norm2() for a in p.a]==[a.norm2() for a in n.a]
    yp,_=exact_step(p,h); yn,_=exact_step(n,h)
    yp=quantize(yp,delta); yn=quantize(yn,delta)
    dp=rad_add(critical(yp),critical(p),-1)
    dn=rad_add(critical(yn),critical(n),-1)
    assert radical_bounds(dp)[0]>0 and radical_bounds(dn)[1]<0
    assert energy(yp)<energy(p) and energy(yn)<energy(n)
    # A rounding-only counterexample: phase cancellation is not coordinatewise monotone.
    prec=state(2,1,{-1:GQ(F(11,10)),1:GQ(F(-1,5))})
    precq=quantize(prec,delta)
    precdiff=rad_add(residual_gram(precq,h,nu),residual_gram(prec,h,nu),-1)
    assert energy(precq)<energy(prec) and radical_bounds(precdiff)[0]>0
    # Execute the fixed quantized law through absorption, not an external forcing.
    t=x; count=0; integer_bound=int(4*energy(x)/(delta*delta))
    edge_max=F(0); edge_nonzero=0; quantization_energy_loss=F(0)
    while energy(t)>0 and count<integer_bound:
        nxt,zz=exact_step(t,h,nu)
        verify_step(t,nxt,zz,h,nu)
        edge=edge_defect_squared(zz); edge_max=max(edge_max,edge); edge_nonzero+=int(edge>0)
        qn=quantize(nxt,delta)
        quantization_energy_loss+=energy(nxt)-energy(qn)
        assert energy(qn)<energy(t)
        t=qn; count+=1
    assert energy(t)==0
    # Quantization source remains explicit; a rational map alone is not a fixed grid.
    rng=Random(20260909); tested=0; gram_checked=0; rounding_injection_example=None
    for m in [1,2,3,4]:
        for k in range(6):
            hs=[F(1,64),F(1,8),F(3)][k%3]
            nus=[F(1,3),F(1),F(2)][k%3]
            q=state(m,F(rng.randint(-5,5),4),{j:GQ(F(rng.randint(-5,5),4),F(rng.randint(-5,5),4)) for j in range(-m,m+1)})
            r,s=exact_step(q,hs,nus); verify_step(q,r,s,hs,nus)
            qr=quantize(r,delta)
            assert energy(qr)<=energy(r)
            Hq=heat_reference(q,hs,nus)
            assert rad_add(residual_gram(q,hs,nus),residual_gram(Hq,hs,nus),-1)==full_source_action(q)
            assert radical_bounds(residual_gram(q,hs,nus))[0]>=0
            net=rad_add(residual_gram(qr,hs,nus),residual_gram(q,hs,nus),-1)
            net=rad_add(net,full_source_action(q))
            inj=rad_add(residual_gram(r,hs,nus),residual_gram(Hq,hs,nus),-1)
            rounding=rad_add(residual_gram(qr,hs,nus),residual_gram(r,hs,nus),-1)
            assert net==rad_add(inj,rounding)
            if rounding_injection_example is None and radical_bounds(rounding)[0]>0:
                rounding_injection_example={'input':q.serial(),'h':str(hs),'nu':str(nus),'Gram_rounding_change':rad_serial(rounding)}
            gram_checked+=1
            assert radical_bounds(rad_add(critical(qr),critical(r),-1))[1]<=0
            tested+=1
    return {'status':'EXACT_FINITE_MODEL_CERTIFICATE_NOT_NS_BLOWUP_PROOF',
            'parameters':{'nu':str(nu),'h':str(h),'delta':str(delta),'m':2},
            'witness':{'before':x.serial(),'midpoint':mid.serial(),'after':y.serial(),
                       'energy_before':str(energy(x)),'energy_after':str(energy(y)),
                       'energy_change':'-24','critical_change':rad_serial(dk),
                       'critical_change_positive_rational_lower_bound':'48',
                       'quantization_changes_witness':False,'one_step_missing_mode_source':False},
            'phase_observer_counterexample':{'input_modal_energies_identical':True,
                       'positive_input':p.serial(),'negative_input':n.serial(),
                       'positive_critical_change':rad_serial(dp),'negative_critical_change':rad_serial(dn),
                       'positive_bounds':[str(v) for v in radical_bounds(dp)],
                       'negative_bounds':[str(v) for v in radical_bounds(dn)]},
            'all_cutoff_checks':cutoff_checks,
            'quantized_trajectory':{'steps_to_exact_zero':count,'a_priori_integer_step_bound':integer_bound,
                       'steps_with_nonzero_cutoff_defect':edge_nonzero,'max_edge_defect_L2_squared':str(edge_max),
                       'quantization_energy_loss':str(quantization_energy_loss)},
            'discrete_Gram':{'identities_checked':gram_checked,'full_nonlinear_outputs_retained':True,
                       'witness_Gram_change':rad_serial(rad_add(residual_gram(y,h,nu),residual_gram(x,h,nu),-1)),
                       'rounding_can_inject_Gram_example':rounding_injection_example,
                       'rounding_only_counterexample':{'before':prec.serial(),'after':precq.serial(),
                         'Gram_change':rad_serial(precdiff),'energy_decreases':True,
                         'scope':'Rounding operator alone, not claimed as a grid-started orbit'}},
            'additional_exact_cases':tested,'seed':20260909,
            'nonclaims':['Not native X6 dynamics','No real-fluid instability theorem',
                         'No Lyapunov instability or finite-time NS singularity',
                         'No infinite-cutoff or vanishing-step bridge','No Lean build or independent review']}

def main()->None:
    if not __debug__:
        raise RuntimeError('Run without -O: exact certificate assertions must be active')
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=Path('results.json'))
    args=p.parse_args(); result=witnesses()
    args.output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'energy_change':'-24','critical_change':'240*sqrt(2)-288 > 48',
          'steps_to_exact_zero':result['quantized_trajectory']['steps_to_exact_zero'],
          'exact_cases':result['additional_exact_cases'],'output':str(args.output)},ensure_ascii=False))
if __name__=='__main__': main()
