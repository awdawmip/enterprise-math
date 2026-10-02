#!/usr/bin/env python3
"""Exact finite synthetic dynamics: affine, nonlinear, conditional, and tails.

Nonlinear endpoint transport uses CWM with explicit state, not an undocumented
nonlinear extension of Affine/MomentState. Infinite-tail statements are analytic
boundaries; the executable BRC examples are finite truncations only.
"""
from __future__ import annotations
import hashlib
import json
from fractions import Fraction as F
from math import comb
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'src'))
from enterprise_math.brc_transport import Affine, EffectHistogram, MomentState, eye, sm
from enterprise_math.brc_weighted import CWM_ZERO, cwm_edge, cwm_propagate, cwm_recoalesce

SAMPLES={1,2,3,4,8,16,32,64,128}


def raw_stats(law, order=4):
    return [sum((w*x**k for x,w in law.items()),F()) for k in range(order+1)]


def centered(raw):
    assert raw[0]==1
    mean=raw[1]
    var=raw[2]-mean*mean
    fourth=raw[4]-4*mean*raw[3]+6*mean*mean*raw[2]-3*mean**4
    k4=fourth-3*var*var
    return mean,var,k4,None if var==0 else k4/(var*var)


def moment_observations(state):
    m=state.to_matrix(); d=state.dimension
    assert m[d][d]==1
    mean=tuple(m[i][d] for i in range(d))
    cov=tuple(tuple(m[i][j]-mean[i]*mean[j] for j in range(d)) for i in range(d))
    return mean,cov


def multiplicative():
    multipliers={F(3,4):F(1,2),F(5,4):F(1,2)}
    h=EffectHistogram.from_terms(1,[(p,Affine(((a,),),(0,)),1) for a,p in multipliers.items()])
    single=raw_stats(multipliers)
    state=MomentState.from_point((1,))
    rows=[]; direct={F(1):F(1)}
    for n in range(1,129):
        state=state.then(h)
        raw=[x**n for x in single]
        mean,var,k4,gamma=centered(raw)
        got_mean,got_cov=moment_observations(state)
        assert got_mean==(mean,) and got_cov==((var,),)
        assert mean==1 and var==F(17,16)**n-1
        if n<=8:
            out={}
            for x,p in direct.items():
                for a,q in multipliers.items():
                    out[a*x]=out.get(a*x,F())+p*q
            direct=out
            assert raw_stats(direct)==raw
        if n in SAMPLES:
            rows.append(dict(n=n,mean=mean,variance=var,k4=k4,gamma4=gamma))
    # Leading normalized fourth term has this exponential base > 1.
    ratio=single[4]/single[2]**2
    assert ratio==F(353,289)>1
    assert rows[-1]['gamma4']>0
    return dict(type='random_affine_multiplier',production_checks=128,explicit_checks=8,
                multiplier_raw_moments=single,asymptotic_gamma_growth_base=ratio,
                formula='gamma4(n) ~ (353/289)^n',rows=rows)


def rotating_modes():
    r=((F(3,5),-F(4,5)),(F(4,5),F(3,5)))
    noise=[(F(1),F()),(F(-1),F()),(F(),F(1)),(F(),F(-1))]
    cases=[]
    for c in (F(3,4),F(1),F(4,3)):
        a=tuple(tuple(c*x for x in row) for row in r)
        h=EffectHistogram.from_terms(2,[(F(1,4),Affine(a,b),1) for b in noise])
        state=MomentState.from_point((0,0))
        s2=s4=fourth=F(); rows=[]; direct={(F(),F()):F(1)}
        for n in range(1,129):
            state=state.then(h)
            _,cov=moment_observations(state)
            previous=s2
            s2=c*c*s2+1; s4=c**4*s4+1
            fourth=c**4*fourth+4*c*c*previous+1
            k4=fourth-2*s2*s2
            assert cov==((s2/2,F()),(F(),s2/2))
            assert k4==-s4
            if n<=4:
                out={}
                for x,p in direct.items():
                    y0=(a[0][0]*x[0]+a[0][1]*x[1],a[1][0]*x[0]+a[1][1]*x[1])
                    for b in noise:
                        y=(y0[0]+b[0],y0[1]+b[1])
                        out[y]=out.get(y,F())+p/4
                direct=out
                radial=sum((p*(x[0]*x[0]+x[1]*x[1])**2 for x,p in direct.items()),F())
                assert radial==fourth
            if n in SAMPLES: rows.append(dict(n=n,ell_squared=s2,radial_k4=k4,normalized_radial_k4=k4/s2**2))
        limit=F() if c==1 else -abs(1-c*c)/(1+c*c)
        cases.append(dict(c=c,production_checks=128,explicit_checks=4,limit_normalized_radial_k4=limit,
                          limiting_regime='diffusive' if c==1 else 'bounded_variance' if c<1 else 'exponential_variance',rows=rows))
    return dict(type='damped_neutral_amplified_linear_mode',cases=cases)


def integrated_noise():
    # v'=v+eta, x'=x+v. The Jordan shear is a two-state linear integrator.
    a=((F(1),F(1)),(F(),F(1)))
    h=EffectHistogram.from_terms(2,[(F(1,2),Affine(a,(0,s)),1) for s in (-1,1)])
    state=MomentState.from_point((0,0)); rows=[]
    for n in range(1,129):
        state=state.then(h)
        _,cov=moment_observations(state)
        varx=F((n-1)*n*(2*n-1),6)
        cross=F(n*(n-1),2)
        k4=-F((n-1)*n*(2*n-1)*(3*n*n-3*n-1),15)
        assert cov==((varx,cross),(cross,F(n)))
        # Independent response-kernel sums; no asymptotic approximation.
        assert varx==sum((F(j*j) for j in range(n)),F())
        assert k4==-2*sum((F(j**4) for j in range(n)),F())
        if n in SAMPLES:
            rows.append(dict(n=n,position_variance=varx,velocity_variance=n,k4=k4,
                             gamma4=None if varx==0 else k4/varx**2))
    return dict(type='integrated_noise_jordan_shear',production_checks=128,
                asymptotic='Var(x) ~ n^3/3; gamma4(x) ~ -18/(5n) ~ const*ell_x^(-2/3)',rows=rows)


def nonlinear_logistic():
    laws={'two_points':{F(1,4):F(1,2),F(3,4):F(1,2)},
          'three_points':{F():F(1,8),F(1,2):F(3,4),F(1):F(1,8)}}
    assert raw_stats(laws['two_points'])[:3]==raw_stats(laws['three_points'])[:3]
    cases=[]; checks=0
    for rate in (F(2),F(3),F(4)):
        tracks={}; predicted_variance=None
        for name,initial in laws.items():
            state={x:cwm_edge(w) for x,w in initial.items()}
            rows=[]
            for n in range(9):
                law={x:w.total for x,w in state.items()}
                raw=raw_stats(law); mean,var,k4,gamma=centered(raw)
                rows.append(dict(n=n,mean=mean,variance=var,k4=k4,gamma4=gamma))
                if n==8: break
                nxt={}
                for x,w in state.items():
                    y=rate*x*(1-x)
                    nxt[y]=cwm_recoalesce(nxt.get(y,CWM_ZERO),cwm_propagate(w,cwm_edge(1)))
                next_raw=raw_stats({x:w.total for x,w in nxt.items()})
                assert next_raw[1]==rate*(raw[1]-raw[2])
                assert next_raw[1]-rate*mean*(1-mean)==-rate*var
                assert next_raw[2]==rate**2*(raw[2]-2*raw[3]+raw[4])
                checks+=1
                state=nxt
            tracks[name]=rows
        a,b=tracks['two_points'],tracks['three_points']
        assert a[1]['mean']==b[1]['mean']==3*rate/16
        assert a[1]['variance']==0 and b[1]['variance']==3*rate**2/256
        assert a[2]['mean']-b[2]['mean']==3*rate**3/256
        # Gaussian closure from the identical initial first two moments
        # produces a third, incorrect next variance for BOTH exact laws.
        m,v=F(1,2),F(1,16)
        gaussian_m2=m*m+v
        gaussian_m3=m**3+3*m*v
        gaussian_m4=m**4+6*m*m*v+3*v*v
        next_mean=rate*(m-gaussian_m2)
        predicted_variance=rate**2*(gaussian_m2-2*gaussian_m3+gaussian_m4)-next_mean**2
        assert predicted_variance not in (a[1]['variance'],b[1]['variance'])
        cases.append(dict(rate=rate,gaussian_two_moment_next_variance=predicted_variance,
                          mean_gap_at_step_two=3*rate**3/256,trajectories=tracks))
    assert all(x['mean']==F(3,4) for x in cases[-1]['trajectories']['two_points'][1:])
    assert all(x['mean']==0 for x in cases[-1]['trajectories']['three_points'][2:])
    return dict(type='nonlinear_logistic_endpoint_transport',transition_checks=checks,
        affine_second_moment_closure_valid=False,
        exact_law='mean_next - f(mean) = -rate*variance; second moment requires third and fourth moments',cases=cases)


def conditional_urn():
    cases=[]
    for capacity in (4,8):
        # Lazy Ehrenfest urn: hold 1/2, otherwise flip one of N bits.
        state={0:cwm_edge(1)}; mean=second=F(); rows=[]
        stationary={F(k):F(comb(capacity,k),2**capacity) for k in range(capacity+1)}
        stationary_stats=centered(raw_stats(stationary))
        assert stationary_stats[1]==F(capacity,4) and stationary_stats[3]==-F(2,capacity)
        for n in range(1,129):
            out={}
            for k,w in state.items():
                edges=[(k,F(1,2)),(k+1,F(capacity-k,2*capacity)),(k-1,F(k,2*capacity))]
                assert sum(p for _,p in edges)==1
                for j,p in edges:
                    if p:
                        assert 0<=j<=capacity
                        out[j]=cwm_recoalesce(out.get(j,CWM_ZERO),cwm_propagate(w,cwm_edge(p)))
            state=out
            raw=raw_stats({F(x):w.total for x,w in state.items()})
            mean,second=(1-F(1,capacity))*mean+F(1,2),(1-F(2,capacity))*second+mean+F(1,2)
            assert raw[0]==1 and raw[1]==mean and raw[2]==second
            mu,var,k4,gamma=centered(raw)
            if n in SAMPLES: rows.append(dict(n=n,mean=mu,variance=var,k4=k4,gamma4=gamma))
        # Verify the full stationary measure with an independent matrix sum.
        for j in range(capacity+1):
            mass=stationary[F(j)]/2
            if j>0: mass+=stationary[F(j-1)]*F(capacity-j+1,2*capacity)
            if j<capacity: mass+=stationary[F(j+1)]*F(j+1,2*capacity)
            assert mass==stationary[F(j)]
        cases.append(dict(capacity=capacity,transition_checks=128,
            stationary_mean=stationary_stats[0],stationary_variance=stationary_stats[1],
            stationary_gamma4=stationary_stats[3],rows=rows))
    return dict(type='state_dependent_lazy_ehrenfest',second_moment_closure_valid=True,
        reason='conditional polynomial expectations have degree at most two',cases=cases)


def tail_boundaries():
    cases=[]
    for power in (2,4):
        rows=[]
        for cutoff in (8,16,32,64,128,256):
            z=sum((F(1,k**power) for k in range(1,cutoff+1)),F())
            law={F(sign*k):F(1,2*k**power)/z for k in range(1,cutoff+1) for sign in (-1,1)}
            raw=raw_stats(law); mean,var,k4,gamma=centered(raw)
            h=EffectHistogram.from_terms(1,[(p,Affine(((1,),),(x,)),1) for x,p in law.items()])
            got_mean,got_cov=moment_observations(MomentState.from_point((0,)).then(h))
            assert got_mean==(0,) and got_cov==((var,),)
            if power==2: assert var==cutoff/z
            if power==4: assert raw[4]==cutoff/z
            rows.append(dict(cutoff=cutoff,variance=var,raw_fourth=raw[4],gamma4=gamma))
        cases.append(dict(power=power,finite_truncation_checks=6,
            infinite_limit_boundary='second moment diverges; ordinary mean not integrable' if power==2 else 'variance finite but fourth moment diverges',
            proof='absolute moment order m uses sum k^(m-power); p-series converges iff m < power-1',rows=rows))
    return dict(type='finite_truncated_power_tail_and_analytic_boundary',
        infinite_brc_execution_claimed=False,cases=cases)


def serializable(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:serializable(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [serializable(v) for v in x]
    return x


def run():
    result=dict(evidence='EXACT_SYNTHETIC_MODELS_WITH_EXPLICIT_TYPING_NOT_NATIVE_OR_PHYSICAL_PROMOTION',
        multiplicative=multiplicative(),rotating_modes=rotating_modes(),integrated_noise=integrated_noise(),
        nonlinear_logistic=nonlinear_logistic(),conditional_urn=conditional_urn(),tail_boundaries=tail_boundaries(),
        source_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
            for p in [Path(__file__),ROOT/'src/enterprise_math/brc_transport.py',ROOT/'src/enterprise_math/brc_weighted.py']})
    affine_cases=[result['multiplicative'],result['integrated_noise'],*result['rotating_modes']['cases']]
    result['counts']=dict(
        production_affine_checks=sum(c['production_checks'] for c in affine_cases),
        nonlinear_transition_checks=result['nonlinear_logistic']['transition_checks'],
        conditional_urn_transition_checks=sum(c['transition_checks'] for c in result['conditional_urn']['cases']),
        finite_tail_checks=sum(c['finite_truncation_checks'] for c in result['tail_boundaries']['cases']),
        explicit_affine_distribution_checks=sum(c.get('explicit_checks',0) for c in affine_cases))
    (HERE/'dynamics_results.json').write_text(json.dumps(serializable(result),ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',**result['counts'])))
    return result


if __name__=='__main__':run()
