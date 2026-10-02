#!/usr/bin/env python3
"""Replay prior weighted sums and return events with all native X6 axes.

Native position uses unit +/- E_i steps only. Weighted six-component responses
are path observables, not fractional native coordinates. Old probability laws
are preserved under declared readouts; old path provenance is not preserved.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'src'))
from enterprise_math.brc_transport import Affine, EffectHistogram, MomentState, eye
from enterprise_math.brc_weighted import CWM_ZERO,cwm_edge,cwm_propagate,cwm_recoalesce


def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


OLD_PATH=ROOT/'experiments/brc_expanded_types_20261002_fca717/related_branches.py'
NATIVE_PATH=ROOT/'experiments/brc_native_x6_residual_20261002_fca717/run_x6.py'
SPATIAL_PATH=ROOT/'experiments/brc_residual_spatial_decay_20261002_fca717/run_spatial_decay.py'
old=load_module('old_weighted_replay_reference',OLD_PATH)
native=load_module('native_x6_replay_reference',NATIVE_PATH)
spatial=load_module('old_spatial_replay_reference',SPATIAL_PATH)
D=6
HORIZON=128
SAMPLES={1,2,3,4,8,16,32,64,128}
ZERO=(0,)*D
STEPS=native.STEPS


def norm2(x):return sum(v*v for v in x)
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def old_scalar(x):return sum(x)
def old_plane(x):return (x[0]+x[2]+x[4],x[1]+x[3]+x[5])


def weighted():
    prior=old.weighted_independent()  # Read-only recomputation; old files untouched.
    weights={'equal':lambda n:F(1),'linear_j':lambda n:F(n),
             'geometric_decay':lambda n:F(3,4)**(n-1),
             'geometric_growth':lambda n:F(4,3)**(n-1)}
    output={};checks=dict(response_moment_steps=0,old_row_matches=0,
                          joint_short_time_checks=0,scalar_CWM_pushforward_checks=0,
                          checked_native_edges=0)
    for name,amplitude in weights.items():
        state=MomentState.from_point(ZERO)
        joint={(ZERO,ZERO):cwm_edge(1)}
        scalar={F():cwm_edge(1)}
        sum1=sum2=sum4=radial_fourth=F();rows=[]
        for n in range(1,HORIZON+1):
            a=amplitude(n)
            packet=EffectHistogram.from_terms(D,[(F(1,12),Affine(eye(D),tuple(a*v for v in step)),1) for step in STEPS])
            state=state.then(packet)
            previous=sum2
            sum1+=a;sum2+=a*a;sum4+=a**4
            radial_fourth+=F(8,3)*a*a*previous+a**4
            expected=tuple(tuple(sum2/6 if i==j else F() for j in range(D)) for i in range(D))
            mass,mean,cov=native.matrix_stats(state.to_matrix())
            assert mass==1 and mean==ZERO and cov==expected
            k6=radial_fourth-F(4,3)*sum2**2
            assert k6==-sum4/3
            gamma6=k6/sum2**2
            reference=prior['families'][name]['rows'][n-1]
            assert reference['variance']==sum2
            assert reference['kappa4']==-2*sum4
            assert gamma6==reference['gamma4']/6
            checks['response_moment_steps']+=1;checks['old_row_matches']+=1
            if n<=3:
                nxt={}
                for (x,w),mass0 in joint.items():
                    for dx in STEPS:
                        y=add(x,dx);z=add(w,tuple(a*v for v in dx));key=(y,z)
                        assert all(type(v)==int for v in y) and sum(abs(v) for v in dx)==1
                        assert old_scalar(z)-old_scalar(w)==a*old_scalar(dx)
                        nxt[key]=cwm_recoalesce(nxt.get(key,CWM_ZERO),cwm_propagate(mass0,cwm_edge(F(1,12))))
                        checks['checked_native_edges']+=1
                joint=nxt
                nxt={}
                for y,w in scalar.items():
                    for sign in (-1,1):
                        z=y+sign*a
                        nxt[z]=cwm_recoalesce(nxt.get(z,CWM_ZERO),cwm_propagate(w,cwm_edge(F(1,2))))
                scalar=nxt
                pushed={}
                for (x,w),mass0 in joint.items():
                    key=old_scalar(w)
                    pushed[key]=cwm_recoalesce(pushed.get(key,CWM_ZERO),mass0)
                assert set(pushed)==set(scalar)
                for y in pushed:
                    assert pushed[y].total==scalar[y].total
                    assert pushed[y].count==6**n*scalar[y].count
                    assert pushed[y].dominant==scalar[y].dominant/6**n
                    checks['scalar_CWM_pushforward_checks']+=1
                direct_cov=tuple(tuple(sum((p.total*w[i]*w[j] for (x,w),p in joint.items()),F())
                                       for j in range(D)) for i in range(D))
                assert direct_cov==cov
                cross=tuple(tuple(sum((p.total*x[i]*w[j] for (x,w),p in joint.items()),F())
                                  for j in range(D)) for i in range(D))
                assert cross==tuple(tuple(sum1/6 if i==j else F() for j in range(D)) for i in range(D))
                assert sum((p.total*norm2(x) for (x,w),p in joint.items()),F())==n
                assert sum((p.total*norm2(w)**2 for (x,w),p in joint.items()),F())==radial_fourth
                checks['joint_short_time_checks']+=1
            if n in SAMPLES:
                rows.append(dict(n=n,native_position_covariance=tuple(tuple(F(n,6) if i==j else F() for j in range(D)) for i in range(D)),
                    full_response_covariance=cov,native_response_cross_covariance=tuple(tuple(sum1/6 if i==j else F() for j in range(D)) for i in range(D)),
                    native_position_squared_spread=n,response_squared_spread=sum2,
                    effective_independent_count=sum2**2/sum4,old_scalar_gamma4=reference['gamma4'],
                    full_six_response_contraction=k6,full_six_response_normalized=gamma6))
        output[name]=dict(rows=rows,old_family=name,old_horizon=HORIZON,
            readout='sum of all six response components',
            probability_law_match='exact per-step sign readout, hence all finite-time joint scalar laws',
            path_refinement='native count = 6^n * old count; native dominant = old dominant / 6^n')
    return dict(families=output,checks=checks,
        exact_bridge='C6 = old scalar gamma4 / 6 = -1/(3*N_eff)',
        native_vs_response='X takes original integer unit steps. W=sum a_j*deltaX_j is a six-component history response; W is not a native Cell address.')


def scalar_or_plane_step(law,steps):
    nxt={}
    for x,p in law.items():
        for dx,q in steps.items():
            y=tuple(a+b for a,b in zip(x,dx))
            nxt[y]=nxt.get(y,F())+p*q
    return nxt


def returns():
    scalar_noise=spatial.axis_law(1,F(1))
    plane_noise=spatial.axis_law(2,F(1))
    assert {v:sum(F(1,12) for step in STEPS if (old_scalar(step),)==v) for v in scalar_noise}==scalar_noise
    assert {v:sum(F(1,12) for step in STEPS if old_plane(step)==v) for v in plane_noise}==plane_noise
    law={ZERO:cwm_edge(1)};scalar={(0,):F(1)};plane={(0,0):F(1)}
    counts=dict(full_joint_timepoints=0,matched_scalar_and_plane_laws=0,
                native_endpoint_observations=0,exact_return_coefficient_queries=0)
    for n in range(1,7):
        law,_=native.cwm_step(law,[(dx,F(1,12)) for dx in STEPS])
        scalar=scalar_or_plane_step(scalar,scalar_noise)
        plane=scalar_or_plane_step(plane,plane_noise)
        pushed1={};pushed2={}
        for x,w in law.items():
            u,v=(old_scalar(x),),old_plane(x)
            pushed1[u]=pushed1.get(u,F())+w.total
            pushed2[v]=pushed2.get(v,F())+w.total
        assert pushed1==scalar and pushed2==plane
        count=native.endpoint_count(n,ZERO)
        assert law.get(ZERO,CWM_ZERO).count==count
        assert law.get(ZERO,CWM_ZERO).total==F(count,12**n)
        if n%2==0:
            m=n//2
            assert scalar[(0,)]==F(comb(2*m,m),4**m)
            assert plane[(0,0)]==F(comb(2*m,m)**2,16**m)
        counts['full_joint_timepoints']+=1
        counts['matched_scalar_and_plane_laws']+=2
        counts['native_endpoint_observations']+=len(law)
        counts['exact_return_coefficient_queries']+=1
    rows=[]
    for m in range(1,65):
        n=2*m
        scalar=F(comb(n,m),4**m)
        plane=F(comb(n,m)**2,16**m)
        full=F(native.endpoint_count(n,ZERO),12**n)
        assert 0<full<plane<scalar
        counts['exact_return_coefficient_queries']+=1
        rows.append(dict(step=n,half_time=m,old_scalar_return=scalar,old_plane_return=plane,
            full_X6_return=full,full_return_given_old_plane_return=full/plane,
            plane_zero_but_full_nonzero=plane-full,
            scaled_full_return_m3=full*m**3))
    return dict(readouts=dict(scalar='sum six coordinates',plane='(x1+x3+x5,x2+x4+x6)'),
        projection_status='declared classical benchmark readouts; neither is asserted to define a complete crystal-packet layer or the STAR carrier',
        parameter_match='one native unit step per old step; same old scalar +/-1 or planar four-axis innovation laws',
        rows=rows,checks=counts,
        analytic_asymptotics={'scalar_even_return':'(pi*m)^(-1/2)',
            'plane_even_return':'1/(pi*m)','full_X6_even_return':'27/(4*pi^3*m^3)',
            'full_return_given_plane_return':'27/(4*pi^2*m^2)'},
        recurrence_boundary='Old scalar and plane readouts are recurrent; full iid X6 walk is transient. This follows from the generating integral and renewal criterion, not from a finite fitted slope.')


def encode(value):
    if isinstance(value,F):return str(value)
    if isinstance(value,dict):return {k:encode(v) for k,v in value.items()}
    if isinstance(value,(tuple,list)):return [encode(v) for v in value]
    return value


def main():
    result=dict(evidence='MATCHED_OLD_READOUTS_WITH_DECLARED_FULL_X6_REFINEMENT_NOT_UNIQUE_NATIVE_DYNAMICS',
        terminology='立体=完整六维原生空间；三维=其中一层晶包；任意读出不自动定义晶包层。',
        old_reference_sources={'weighted':str(OLD_PATH.relative_to(ROOT)),
                               'return_axis_laws_d1_d2_unit_step':str(SPATIAL_PATH.relative_to(ROOT))},
        weighted=weighted(),returns=returns())
    result['source_sha256']={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in
        (Path(__file__),OLD_PATH,NATIVE_PATH,SPATIAL_PATH,ROOT/'src/enterprise_math/brc_transport.py',ROOT/'src/enterprise_math/brc_weighted.py')}
    (HERE/'weighted_return_results.json').write_text(json.dumps(encode(result),indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(dict(status='PASS',weighted=result['weighted']['checks'],returns=result['returns']['checks'])))
    return result


if __name__=='__main__':main()
