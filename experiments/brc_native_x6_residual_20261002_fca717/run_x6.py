#!/usr/bin/env python3
"""Full native X6 residual diagnostics, with time separate from six axes.

All spatial updates in the primary programs are original +/- E_i steps.
Probabilities and heartbeat programs are declared experiments, not new axioms.
Raw signed charts are internal coordinates, never fabricated final Cell codecs.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'src'))
from enterprise_math.brc_transport import Affine, EffectHistogram, MomentState, eye, mm, mv, transpose
from enterprise_math.brc_weighted import CWM_ZERO, cwm_edge, cwm_propagate, cwm_recoalesce

D=6
HORIZON=64
ENUM_END=6
SAMPLES={1,2,3,4,8,16,32,64}
ZERO=(0,)*D
STEPS=tuple(tuple(s if j==i else 0 for j in range(D)) for i in range(D) for s in (-1,1))
P=((1,0,-1,0,0,0),(0,1,-1,0,0,0))
LIFT_METRIC=((F(2,3),F(-1,3)),(F(-1,3),F(2,3)))
H1=(1,1,1,0,0,0)
H2=(0,0,0,1,1,1)


def trace(a):return sum((a[i][i] for i in range(len(a))),F())
def outer(a,b):return tuple(tuple(x*y for y in b) for x in a)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def norm2(x):return sum(v*v for v in x)
def project_cov(c):return mm(mm(P,c),transpose(P))
def carrier_q(x):
    u,v=mv(P,x)
    return u*u+v*v-u*v


def decompose(x):
    visible=F(2,3)*carrier_q(x)
    hidden=F(sum(x[:3])**2,3)+sum(v*v for v in x[3:])
    assert norm2(x)==visible+hidden
    return visible,hidden


def matrix_stats(m):
    mass=m[-1][-1]
    mean=tuple(m[i][-1]/mass for i in range(D))
    cov=tuple(tuple(m[i][j]/mass-mean[i]*mean[j] for j in range(D)) for i in range(D))
    return mass,mean,cov


def law_stats(law):
    mass=sum(law.values(),F())
    mean=tuple(sum((p*x[i] for x,p in law.items()),F())/mass for i in range(D))
    cov=tuple(tuple(sum((p*(x[i]-mean[i])*(x[j]-mean[j]) for x,p in law.items()),F())/mass
                    for j in range(D)) for i in range(D))
    fourth=sum((p*norm2(tuple(a-b for a,b in zip(x,mean)))**2 for x,p in law.items()),F())/mass
    k4=fourth-trace(cov)**2-2*trace(mm(cov,cov))
    return mass,mean,cov,k4


def cwm_step(law,terms):
    nxt={}; edge_checks=0
    for x,w in law.items():
        for dx,p in terms:
            assert len(dx)==D and sum(abs(z) for z in dx)==1
            y=add(x,dx)
            nxt[y]=cwm_recoalesce(nxt.get(y,CWM_ZERO),cwm_propagate(w,cwm_edge(p)))
            edge_checks+=1
    return nxt,edge_checks


def endpoint_count(n,z):
    """Exact coefficient of (sum_i (s_i+s_i^-1))^n in all six variables."""
    if len(z)!=D:raise ValueError('six raw coordinates required')
    dp={0:1}
    for component in z:
        nxt={}
        for used,ways in dp.items():
            for m in range(abs(component),n-used+1,2):
                count=comb(m,(m+component)//2)
                nxt[used+m]=nxt.get(used+m,0)+comb(used+m,m)*ways*count
        dp=nxt
    return dp.get(n,0)


def primary_programs():
    sign_pattern=(1,-1,1,-1,1,-1)
    programs=[]
    totals=dict(moment_steps=0,cwm_endpoint_observations=0,primitive_edge_checks=0,
                direct_fourth_moment_checks=0,endpoint_coefficient_queries=0,explicit_word_checks=0)
    for name,decay in (('six_axis_diffusion',F(1)),('linear_mass_decay',F(1,2)),('two_phase_oscillation',F(1))):
        raw=MomentState.from_point(ZERO).to_matrix()
        cwm={ZERO:cwm_edge(1)}; direct={ZERO:F(1)}
        mean=(F(),)*D; expected_cov=tuple((F(),)*D for _ in range(D)); cumulant=F()
        rows=[]; sparse_rows=[]
        for n in range(1,HORIZON+1):
            phase=1 if n%2 else -1
            terms=[]
            for dx in STEPS:
                bias=sum(a*b for a,b in zip(dx,sign_pattern))
                p=(1+F(phase,2)*bias)/12 if name=='two_phase_oscillation' else F(1,12)
                terms.append((dx,decay*p))
            packet=EffectHistogram.from_terms(D,[(p,Affine(eye(D),dx),1) for dx,p in terms])
            raw=packet.moment_action(raw)
            mass,actual_mean,actual_cov=matrix_stats(raw)
            step_law={dx:p/decay for dx,p in terms}
            _,step_mean,step_cov,step_k4=law_stats(step_law)
            mean=add(mean,step_mean)
            expected_cov=tuple(tuple(expected_cov[i][j]+step_cov[i][j] for j in range(D)) for i in range(D))
            cumulant+=step_k4
            assert mass==decay**n and actual_mean==mean and actual_cov==expected_cov
            if name=='two_phase_oscillation':
                assert mean==tuple(F(v,12) if n%2 else F() for v in sign_pattern)
                assert expected_cov==tuple(tuple(n*(F(i==j,6)-F(sign_pattern[i]*sign_pattern[j],144))
                                                 for j in range(D)) for i in range(D))
                assert cumulant==-F(83*n,288)
            else:
                assert mean==ZERO
                assert expected_cov==tuple(tuple(F(n,6) if i==j else F() for j in range(D)) for i in range(D))
                assert cumulant==-F(n,3)
            projected=project_cov(expected_cov)
            visible=trace(mm(LIFT_METRIC,projected))
            hidden=trace(expected_cov)-visible
            assert hidden>0 and all(expected_cov[i][i]>0 for i in range(D))
            if name!='two_phase_oscillation':
                assert visible==F(n,3) and hidden==F(2*n,3)
                assert projected==((F(n,3),F(n,6)),(F(n,6),F(n,3)))
            if n<=ENUM_END:
                cwm,edges=cwm_step(cwm,terms)
                totals['primitive_edge_checks']+=edges
                nxt={}
                for x,p0 in direct.items():
                    for dx,p in terms:
                        y=add(x,dx);nxt[y]=nxt.get(y,F())+p0*p
                direct=nxt
                assert {x:w.total for x,w in cwm.items()}==direct
                stats=law_stats(direct)
                assert stats==(mass,mean,expected_cov,cumulant)
                assert sum(w.count for w in cwm.values())==12**n
                totals['direct_fourth_moment_checks']+=1
                totals['cwm_endpoint_observations']+=len(cwm)
                for x in cwm:decompose(x)
                # In the unbiased programs the entire planar fourth-order
                # radial defect vanishes, despite nonzero full-X6 contraction.
                if name!='two_phase_oscillation':
                    eq=sum((p*carrier_q(x) for x,p in direct.items()),F())/mass
                    eq2=sum((p*carrier_q(x)**2 for x,p in direct.items()),F())/mass
                    assert eq==F(n,2) and eq2==F(n*n,2) and eq2-2*eq*eq==0
                    for x in (ZERO,(n,0,0,0,0,0),(0,0,0,n,0,0)):
                        count=endpoint_count(n,x)
                        w=cwm.get(x,CWM_ZERO)
                        assert w.count==count and w.total==count*(decay/12)**n
                        if count:assert w.dominant==(decay/12)**n
                        totals['endpoint_coefficient_queries']+=1
                if n<=4 and name=='six_axis_diffusion':
                    words=Counter(tuple(sum(v[i] for v in word) for i in range(D))
                                  for word in product(STEPS,repeat=n))
                    assert words=={x:w.count for x,w in cwm.items()}
                    totals['explicit_word_checks']+=1
                sparse_rows.append(dict(step=n,endpoints=len(cwm),full_path_count=12**n))
            if n in SAMPLES:
                rows.append(dict(step=n,phase=phase if name=='two_phase_oscillation' else None,
                    surviving_mass=mass,full_reference_mean=mean,residual_covariance=expected_cov,
                    star_reference_mean=mv(P,mean),star_covariance=projected,
                    full_centered_squared_residual=trace(expected_cov),
                    star_visible_native_squared_readout=visible,star_hidden_native_squared_readout=hidden,
                    unnormalized_centered_squared_residual=mass*trace(expected_cov),
                    full_fourth_cumulant_contraction=cumulant,
                    normalized_full_fourth_contraction=cumulant/trace(expected_cov)**2,
                    carrier_radial_fourth_defect=F() if name!='two_phase_oscillation' else 'NOT_USED_AS_DIAGNOSTIC'))
            totals['moment_steps']+=1
        programs.append(dict(id=name,all_six_axes_active=True,covariance_rank=6,
            primitive_kernel='positive +/- E_i on all six axes',
            reference_status='declared full-X6 mean; not uniquely recoverable from a planar baseline',
            total_mass_multiplier=decay,rows=rows,full_distribution_checks=sparse_rows))
    long_queries=[]
    for n,z in ((64,ZERO),(64,(2,0,0,0,0,0)),(64,(0,0,0,2,0,0)),(64,(64,0,0,0,0,0)),(63,ZERO)):
        count=endpoint_count(n,z)
        if sum(abs(v) for v in z)%2!=n%2:assert count==0
        if z==(64,0,0,0,0,0):assert count==1
        long_queries.append(dict(step=n,raw_X6_endpoint=z,count=count,probability=F(count,12**n)))
        totals['endpoint_coefficient_queries']+=1
    assert long_queries[1]['count']==long_queries[2]['count']
    return dict(programs=programs,checks=totals,long_horizon_exact_joint_endpoint_queries=long_queries,
        full_joint_law='For unbiased diffusion: coefficient of (sum_i(s_i+s_i^-1)/12)^n; all six variables retained.',
        long_horizon_method='Exact 6D first/second moment action and independent cumulant additivity; no claim of enumerating all length-64 paths.')


def hidden_depth_cycles():
    increments=[tuple(a if i<3 else b for i in range(D)) for a,b in product((-1,1),repeat=2)]
    packet=EffectHistogram.from_terms(D,[(F(1,4),Affine(eye(D),v),1) for v in increments])
    state=MomentState.from_point(ZERO);law={ZERO:cwm_edge(1)}
    rows=[];edges=endpoints=0
    for n in range(1,HORIZON+1):
        state=state.then(packet)
        mass,mean,cov=matrix_stats(state.to_matrix())
        expected=tuple(tuple(F(n) if i//3==j//3 else F() for j in range(D)) for i in range(D))
        assert mass==1 and mean==ZERO and cov==expected
        assert project_cov(cov)==((0,0),(0,0)) and trace(cov)==6*n
        if n<=8:
            phase={(x,a,b):cwm_propagate(w,cwm_edge(F(1,4))) for x,w in law.items()
                   for a,b in product((-1,1),repeat=2)}
            for axis in range(D):
                nxt={}
                for (x,a,b),w in phase.items():
                    sign=a if axis<3 else b
                    dx=tuple(sign if i==axis else 0 for i in range(D))
                    y=add(x,dx);key=(y,a,b)
                    nxt[key]=cwm_recoalesce(nxt.get(key,CWM_ZERO),cwm_propagate(w,cwm_edge(1)))
                    assert sum(abs(v) for v in dx)==1
                    expected_readout=(a,0) if axis==0 else (a,a) if axis==1 else (0,0)
                    assert mv(P,y)==expected_readout
                    edges+=1
                phase=nxt
            law={}
            for (x,a,b),w in phase.items():law[x]=cwm_recoalesce(law.get(x,CWM_ZERO),w)
            assert len(law)==(n+1)**2
            for i,j in product(range(n+1),repeat=2):
                a,b=2*i-n,2*j-n;x=(a,a,a,b,b,b)
                w=law[x];count=comb(n,i)*comb(n,j)
                assert (w.count,w.total,w.dominant)==(count,F(count,4**n),F(1,4**n))
                endpoints+=1
            assert law_stats({x:w.total for x,w in law.items()})[:3]==(1,mean,cov)
        if n in SAMPLES:rows.append(dict(period=n,native_step=6*n,residual_covariance=cov,
            full_squared_residual=trace(cov),carrier_squared_residual=0,covariance_rank=2))
    return dict(status='FULL_X6_HIDDEN_MODE_CONTROL_NOT_FULL_RANK_DIFFUSION',
        program='choose two independent signs each period; retain first through E1,E2,E3 and second through E4,E5,E6',
        primitive_steps_per_period=6,mean_zero_does_not_imply_residual_zero=True,
        checks=dict(moment_periods=HORIZON,primitive_edges=edges,exact_endpoint_CWM_triples=endpoints),rows=rows)


def future_separation():
    """Positive conditional native kernel; no affine closure is presumed."""
    initial=[(0,0,0,1,0,0),(0,0,0,-1,0,0)]
    outputs=[]
    for x in initial:
        assert mv(P,x)==(0,0)
        dx=(1,0,0,0,0,0) if x[3]>0 else (-1,0,0,0,0,0) if x[3]<0 else (0,1,0,0,0,0)
        law,_=cwm_step({x:cwm_edge(1)},[(dx,F(1))])
        y=next(iter(law))
        outputs.append(dict(before=x,after=y,before_star=mv(P,x),after_star=mv(P,y)))
    assert outputs[0]['after_star']==(1,0) and outputs[1]['after_star']==(-1,0)
    # Three-coordinate readout x1,x2,x3 also loses E4 and fails this future.
    assert initial[0][:3]==initial[1][:3]
    return dict(kernel='if x4>0 step +E1; if x4<0 step -E1; if x4=0 step +E2',
        declared_conditional_program=True,full_state_required_for_this_future=True,examples=outputs)


def source_witness():
    a,b=(3,4,0,0,0,0),(4,5,1,0,0,0)
    assert mv(P,a)==mv(P,b)==(3,4)
    assert carrier_q(a)==carrier_q(b)==13
    assert norm2(a)==25 and norm2(b)==42
    assert mm(P,transpose(P))==((2,1),(1,2))
    assert mm(LIFT_METRIC,mm(P,transpose(P)))==eye(2)
    for x in (a,b,H1,H2,(1,2,3,4,5,6)):decompose(x)
    return dict(first=a,second=b,shared_star=(3,4),native_squared_lengths=[25,42],
        star_kernel_basis=[H1,(0,0,0,1,0,0),(0,0,0,0,1,0),(0,0,0,0,0,1)],
        raw_length_decomposition='L_E^2 = (2/3) Q_car + (x1+x2+x3)^2/3 + x4^2+x5^2+x6^2')


def encode(value):
    if isinstance(value,F):return str(value)
    if isinstance(value,dict):return {k:encode(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):return [encode(v) for v in value]
    return value


def main():
    result=dict(schema='NATIVE_X6_RESIDUAL_DIAGNOSTIC_V1',
        terminology={'立体':'完整六维原生空间','三维':'六维立体世界中的一层晶包','时间':'单独的事件顺序，不计为空间轴'},
        native_space_dimension=D,time_is_separate=True,final_Cell_address_codec_claimed=False,
        kernel_status='DECLARED_POSITIVE_PROGRAMS_ON_NATIVE_PRIMITIVE_ADJACENCY_NOT_A_UNIQUE_NATIVE_DYNAMICS',
        source_witness=source_witness(),primary=primary_programs(),
        hidden_depth_control=hidden_depth_cycles(),conditional_future=future_separation())
    paths=[Path(__file__),ROOT/'src/enterprise_math/brc_transport.py',ROOT/'src/enterprise_math/brc_weighted.py',
           ROOT/'definitions/P000_FCC_PRIMARY_COORDINATE_CARRIER_20260829.md',
           ROOT/'definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md',
           ROOT/'definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.md']
    result['source_sha256']={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    (HERE/'results.json').write_text(json.dumps(encode(result),ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',primary=result['primary']['checks'],hidden=result['hidden_depth_control']['checks'])))


if __name__=='__main__':main()
