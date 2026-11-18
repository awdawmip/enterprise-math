"""Exact rational-plane reference and original seeded FFT RK4 replay. Python, NumPy, SciPy."""
import argparse
import ast
import hashlib
import importlib.util
import itertools
import json
import math
import os
import sys
import time
from collections import Counter
from fractions import Fraction as F
from functools import cache
from pathlib import Path
from types import SimpleNamespace

import numpy as np
from scipy import fft


CHECK="research_checks/CFD_SPECTRAL_HYBRID_292BCE_20260917.py"
SUMMARY="research_artifacts/CFD_SPECTRAL_HYBRID_292BCE_20260917/summary.json"
PROBE="research_notes/CFD-B1F673/prior_3d/probe.py"
ADAPTER="research_artifacts/CFD_SPECTRAL_HYBRID_292BCE_20260917/static_carrier_native_adapter.py"
PINS={ADAPTER:"c3a8975aaf60e858900146350909983546a86fd6bfe51388fc1c6217a587442b",CHECK:"eaa378080453b967a47b820e2a66594b1eaec2398a9381e366c2cdbe65378856",
      SUMMARY:"5eaca57874aa5327b1aaed5a7aeb796133d3dea8fc5b0c62a3f3a203105f11c7",
      PROBE:"1d10429616026f13643f0ba1641acd8c23f3aecd1dc7c03b429f5e0c4381eb09"}
Z=(F(0),F(0))
ONE=(F(1),F(0))
K=7
B=list(itertools.product(range(-K,K+1),repeat=2))
AXES=((1,0),(-1,0),(0,1),(0,-1))


def scalar(z):
    return F(float(z.real)),F(float(z.imag))


def plus(a,b):
    return a[0]+b[0],a[1]+b[1]


def scale(a,r):
    return r*a[0],r*a[1]


def times(a,b):
    return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]


def cpower(a,n):
    v=ONE
    for _ in range(n):
        v=times(v,a)
    return v


def accum(dest,k,a):
    dest[k]=plus(dest.get(k,Z),a)


def norm2(a):
    return a[0]**2+a[1]**2


def root_bounds(x):
    unit=10**65
    n=math.isqrt(x.numerator*unit**2//x.denominator)
    return F(n,unit),F(n+(n*n*x.denominator!=x.numerator*unit**2),unit)


def rnd(f,up=True):
    """Outward four-significant-figure decimal for a nonnegative exact rational."""
    assert f>=0
    if not f:
        return "0"
    x=f; e=0
    while x<1:
        x*=10; e-=1
    while x>=10:
        x/=10; e+=1
    x*=1000
    a=-(-x.numerator//x.denominator) if up else x.numerator//x.denominator
    if a==10000:
        a=1000; e+=1
    return f"{a//1000}.{a%1000:03d}e{e:+d}"


def load(root):
    for k,v in PINS.items():
        assert hashlib.sha256((root/k).read_bytes()).hexdigest()==v
    tree=ast.parse((root/CHECK).read_bytes())
    names={"native_operators","DealiasedFFT","project","FFTEngine","rk4","set_mode","div_free_amp","structured",
           "extract_support","random_initial","StaticEngine","rotational_pairs_into"}
    const={"N","K","M","NU","DT","STEPS","LIMIT","STRUCT_SEEDS"}
    selected=[node for node in tree.body if
              (isinstance(node,(ast.ClassDef,ast.FunctionDef)) and node.name in names) or
              (isinstance(node,ast.Assign) and getattr(node.targets[0],"id",None) in const)]
    assert len(selected)==len(names)+len(const)
    spec=importlib.util.spec_from_file_location("trajectory29_pinned_adapter",root/ADAPTER)
    sca=importlib.util.module_from_spec(spec); sys.modules[spec.name]=sca; spec.loader.exec_module(sca)
    for node in selected:
        if getattr(node,"name","")=="rotational_pairs_into":
            assert len(node.decorator_list)==1
            node.decorator_list=[]  # Original loop body with ordinary Python/NumPy scalar evaluation.
    ns={"np":np,"fft":fft,"time":time,"math":math,"sca":sca}
    exec(compile(ast.Module(selected,[]),str(root/CHECK),"exec"),ns)
    return SimpleNamespace(**ns),json.loads((root/SUMMARY).read_text())


@cache
def eulerian(n,j):
    if n==0:
        return int(j==0)
    if not 0<=j<n:
        return 0
    return (j+1)*eulerian(n-1,j)+(n-j)*eulerian(n-1,j-1)


def occupancy(n,r):
    cs=[F(1)]
    for _ in range(n):
        cs=[sum((cs[j-i]/math.factorial(i) for i in range(5) if 0<=j-i<len(cs)),F(0))
            for j in range(min(r+1,len(cs)+4))]
    return (cs[r]*math.factorial(r)/n**r) if r<len(cs) else F(0)


def drift(v,h):
    result={}
    for (x,y),a in v.items():
        if a==Z:
            continue
        for (s,t),vel in h.items():
            dest=x+s,y+t
            factor=y if s else x
            if factor and max(map(abs,dest))<=K:
                u=times((vel[1],-vel[0]),a)
                accum(result,dest,scale(u,factor))
    return {k:a for k,a in result.items() if a!=Z}


def dist(p):
    x,y=map(abs,p)
    if not x+y:
        return math.inf
    return x+y-1 if x*y or x+y==1 else x+y+1


def leading(h,w):
    powers=[w]
    for _ in range(2*K-1):
        powers.append(drift(powers[-1],h))
    sectors={}
    seen=0
    for s,t in itertools.product((1,-1),repeat=2):
        cx=scale((h[s,0][1],-h[s,0][0]),t)
        cy=scale((h[0,t][1],-h[0,t][0]),s)
        seed=plus(times(cx,w[0,t]),times(cy,w[s,0]))
        assert seed!=Z
        sectors[f"{s},{t}"]=rnd(root_bounds(norm2(seed))[1])
        for m,n in itertools.product(range(1,K+1),repeat=2):
            r=m+n-1
            label=s*m,t*n
            assert all(label not in powers[j] for j in range(r))
            predicted=scale(times(seed,times(cpower(cx,m-1),cpower(cy,n-1))),eulerian(r,n-1))
            assert predicted==powers[r][label] and predicted!=Z
            seen+=1
    return dict(quadrant_seed_abs_upper=sectors,mixed_frequencies_exact=seen,
                K7_corner_Eulerian=eulerian(13,6),
                twelve_step_leading_ratios={r:str(occupancy(12,r)) for r in (1,4,5,7,10,13)})


def interval_reference(h,w,T,nu,n=12):
    z=nu*T
    wf=[w]
    for j in range(n):
        history={}
        for l in range(j+1):
            factor=(-z)**l/math.factorial(l)
            for k,a in wf[j-l].items():
                accum(history,k,scale(a,factor))
        v=drift(history,h)
        for (x,y),a in wf[j].items():
            accum(v,(x,y),scale(a,-nu*(x*x+y*y)))
        wf.append({k:scale(a,T/(j+1)) for k,a in v.items() if a!=Z})
    value={}
    for v in wf:
        for k,a in v.items():
            accum(value,k,a)
    hs={k:root_bounds(norm2(a))[1] for k,a in h.items()}
    C=max(sum((abs(y if s else x)*hs[s,t] for s,t in AXES if max(abs(x-s),abs(y-t))<=K),F(0)) for x,y in B)
    W=[root_bounds(sum(map(norm2,v.values()),F(0)))[1] for v in wf]
    eps=T/(n+1)*(2*nu*K*K*W[-1]+C*sum((W[j]*z**(n-j)/math.factorial(n-j) for j in range(n+1)),F(0)))
    eh=sum(((-z)**j/math.factorial(j) for j in range(n+1)),F(0))
    h_norm=root_bounds(sum(map(norm2,h.values()),F(0)))[1]
    eps_h=h_norm*z**(n+1)/math.factorial(n+1)
    eta=T*(1-z/2+z*z/6)
    tail={r:W[0]*(C*eta)**r/math.factorial(r) for r in (3,5,8,13)}
    td=T*(C+2*nu*K*K)
    assert td<1
    rk_tail={r:W[0]*(T*C)**r/((1-td)*math.factorial(r)) for r in tail}
    return value,eh,eps+eps_h,C,tail,rk_tail


def run(ref,initial,n,mode="fft"):
    original=ref.rk4.__globals__
    saved=original["DT"],original["STEPS"]
    original["DT"],original["STEPS"]=ref.DT*12/n,n
    events=[]
    engine=ref.FFTEngine() if mode=="fft" else ref.StaticEngine(initial)
    class Recorder:
        def rhs(self,x):
            y=engine.rhs(x)
            events.append((x.copy(),y.copy()))
            return y
    try:
        final=ref.rk4(initial,Recorder())
    finally:
        original["DT"],original["STEPS"]=saved
    return final,events,engine.stats


def comparison(y,w,h,eh,eps):
    err=F(0)
    for x,v in itertools.product(B,range(3)):
        p,q=x
        target=w.get(x,Z) if v==2 else (scale(h[x],eh) if x in h and v==(1 if p else 0) else Z)
        actual=scalar(y[v,p%16,q%16,0])
        err+=norm2(plus(actual,scale(target,-1)))
    assert not np.any(y[:,:,:,1:]) and not np.any(y[:,8,:,:]) and not np.any(y[:,:,8,:])
    lo,hi=root_bounds(err)
    return [rnd(max(F(0),lo-eps),False),rnd(hi+eps)]


def audit(root):
    ref,summary=load(root)
    name="heldout-xy-plane-generators"
    y0=ref.structured(name)
    h={k:scalar(y0[1 if k[0] else 0,k[0]%16,k[1]%16,0]) for k in AXES}
    w={k:scalar(y0[2,k[0]%16,k[1]%16,0]) for k in AXES}
    T,nu=12*F(ref.DT),F(ref.NU)
    info=leading(h,w)
    P,eh,eps,C,tail,rk_tail=interval_reference(h,w,T,nu)
    truth,observed,stage_stats={},None,None
    roundoff_lower=None; plane_original=None
    for n in (6,12,24):
        y,ev,_=run(ref,y0,n)
        truth[n]=comparison(y,P,h,eh,eps)
        if n==12:
            def radial(q):
                return sum((norm2(scalar(y[2,x%16,z%16,0])) for x,z in B if dist((x,z))>=q),F(0))
            plane_original=y
            observed={q:[rnd(root_bounds(radial(q))[0],False),rnd(root_bounds(radial(q))[1])] for q in tail}
            roundoff_lower=rnd(root_bounds(radial(13))[0]-rk_tail[13],False)
            allfields=[a for pair in ev for a in pair]
            layer_zero=all(not np.any(v[:,:,:,1:]) for v in allfields)
            div=max(float(np.max(np.abs(ref.native_operators(16)[1][0]*v[0]+ref.native_operators(16)[1][1]*v[1]))) for v in allfields)
            conj=max(float(np.max(np.abs(v[:,:, :,0]-v[:,(-np.arange(16))%16][:,:,(-np.arange(16))%16,0].conjugate()))) for v in allfields)
            # RK4's first RHS state of each step is the preceding accepted state.
            accepted=[ev[4*i][0] for i in range(n)]+[y]
            energies=[float(np.sum(np.abs(v)**2)) for v in accepted]
            assert layer_zero and all(a>b for a,b in zip(energies,energies[1:]))
            stage_stats=dict(stages=len(ev),offplane_is_zero=layer_zero,
                             max_divergence_input_or_rhs=div,max_conjugacy_input_or_rhs=conj,
                             energy_initial=energies[0],energy_final=energies[-1],strict_decreases=n)
    line={}
    for name,freq in [("heldout-oblique-line",2),("heldout-even-axis",4)]:
        u=ref.structured(name)
        y,_,_=run(ref,u,12)
        x=F(ref.DT)*nu*freq
        R=sum(((-x)**j/math.factorial(j) for j in range(5)),F(0))**12
        true_error=F(0)
        for k in np.ndindex(u.shape):
            true_error+=norm2(plus(scalar(y[k]),scale(scalar(u[k]),-R)))
        line[name]=dict(shell=freq,source_error_vs_exact_RK_l2_upper=rnd(root_bounds(true_error)[1]),
                        rk_multiplier_error_vs_exp_upper=rnd(12*x**5/120))
    static,_,state=run(ref,y0,12,"static")
    assert state["static_sparse_calls"]==48 and state["carrier_size"]==225
    static_error=comparison(static,P,h,eh,eps)
    static_tail13=root_bounds(sum((norm2(scalar(static[2,x%16,y%16,0])) for x,y in B if dist((x,y))>=13),F(0)))
    fallbacks={}
    for size,seed in [(48,926211),(96,926212)]:
        u=ref.random_initial(size,seed)
        dense,ds,_=run(ref,u,12)
        fast,fs,state=run(ref,u,12,"static")
        assert state["decision"]=="FALLBACK_DENSE" and state["fft_calls"]==48
        assert all(np.array_equal(a,c) and np.array_equal(b,d) for (a,b),(c,d) in zip(ds,fs))
        assert np.array_equal(dense,fast)
        fallbacks[size]=dict(seed=seed,lower_bound=state["lower_bound"],all_stage_inputs_rhs_equal=len(fs),endpoint_equal=True)
    records={row["name"]:{"decision":row["decision"],"carrier":row["carrier_size"],"lower":row["proved_lower_bound"]} for row in summary["cases"]}
    return dict(source_sha256=PINS,comparison_domain="3D finite Fourier surrogate; k3=0, 3 velocity components",
                actual_seed=926203,leading=info,vertical_drift_operator_norm_upper=rnd(C),
                degree_12_plane_reference_total_l2_error_upper=rnd(eps),
                continuous_galerkin_vertical_tail_upper={q:rnd(v) for q,v in tail.items()},
                true_RK4_vertical_tail_upper={q:rnd(v) for q,v in rk_tail.items()},
                dense_float_vertical_tail_l2_intervals=observed,absolute_distance_from_exact_RK4_tail13_lower=roundoff_lower,
                original_fft_endpoint_l2_error_intervals=truth,source_static_plane_12step_analytic_error=static_error,
                static_plane_12step_max_abs_difference_from_dense=float(np.max(np.abs(plane_original-static))),
                static_plane_tail13_l2_interval=[rnd(static_tail13[0],False),rnd(static_tail13[1])],
                dense_fallback_replays=fallbacks,
                frozen_stage_metrics=stage_stats,line_analytic_controls=line,historical_routes=records)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source-root",type=Path,default=os.environ.get("ENTERPRISE_MATH"))
    args=p.parse_args()
    if not args.source_root:
        p.error("supply --source-root or ENTERPRISE_MATH")
    print(json.dumps(audit(Path(args.source_root)),indent=2))
