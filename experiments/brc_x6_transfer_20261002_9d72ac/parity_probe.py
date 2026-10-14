#!/usr/bin/env python3
"""Exact six-axis joint-law preservation probe; no new spatial dimension.

The native spatial substrate is fixed X6. Initial laws occupy signed raw charts
relative to one chosen Cell anchor. Positive probabilities are not amplitudes.
F(x)=x+Q(x)e1 with Q=product(x2..x6) is a DECLARED conditional test operation,
not a derived force law. Q is an observer, never an extra spatial axis.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb, prod
from pathlib import Path
import hashlib
import json
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'src'))
from enterprise_math.brc_transport import Affine,EffectHistogram,MomentState,eye,ma,point_moment,sm

HORIZON=8
AUDITOR='EM-BRCAUDIT-9D72AC'


def laws():
    states=list(product((-1,1),repeat=6))
    return {'independent':{x:F(1,64) for x in states},
            'parity_plus':{x:F(1,32) for x in states if prod(x)==1},
            'parity_minus':{x:F(1,32) for x in states if prod(x)==-1}}


def project(law,indices):
    out=defaultdict(F)
    for x,p in law.items(): out[tuple(x[i] for i in indices)]+=p
    return dict(out)


def tv(a,b):
    return sum((abs(a.get(x,F())-b.get(x,F())) for x in set(a)|set(b)),F())/2


def push(law,transform):
    out=defaultdict(F)
    for x,p in law.items(): out[transform(x)]+=p
    return dict(out)


def q(x): return prod(x[1:])


def advance(x,n=1): return (x[0]+n*q(x),)+x[1:]


def moment_state(law,readout=lambda x:x):
    dim=len(readout(next(iter(law))))
    matrix=sm(0,eye(dim+1))
    for x,p in law.items(): matrix=ma(matrix,sm(p,point_moment(readout(x))))
    return MomentState.from_matrix(matrix)


def scalar_stats(law):
    mean=sum((p*x[0] for x,p in law.items()),F())
    variance=sum((p*(x[0]-mean)**2 for x,p in law.items()),F())
    fourth=sum((p*(x[0]-mean)**4 for x,p in law.items()),F())
    k4=fourth-3*variance*variance
    return dict(mean=mean,variance=variance,kappa4=k4,
                gamma4=k4/(variance*variance) if variance else None,
                status='OK' if variance else 'ZERO_VARIANCE_NORMALIZATION_UNDEFINED')


def encoded_law(law):
    return [{'raw_chart':list(x),'probability':str(p)} for x,p in sorted(law.items())]


def json_default(value):
    if isinstance(value,F): return str(value)
    raise TypeError(type(value).__name__)


def main():
    initial=laws()
    proper_checks=0
    proper_by_size={str(k):0 for k in range(6)}
    for mask in range(63):
        indices=[j for j in range(6) if mask&(1<<j)]
        reference=project(initial['independent'],indices)
        for name in ('parity_plus','parity_minus'):
            assert project(initial[name],indices)==reference
            proper_checks+=1
        proper_by_size[str(len(indices))]+=1
    assert sum(proper_by_size.values())==63
    monomial_count=0
    for powers in product(range(6),repeat=6):
        if sum(powers)>5: continue
        values=[sum((p*prod(x[j]**powers[j] for j in range(6)) for x,p in law.items()),F())
                for law in initial.values()]
        assert len(set(values))==1
        monomial_count+=1
    assert monomial_count==comb(11,6)
    states={name:moment_state(law) for name,law in initial.items()}
    assert len({state.upper for state in states.values()})==1
    assert all(len(state.upper)==28 for state in states.values())
    assert states['independent'].to_matrix()==eye(7)
    sixth={name:sum((p*prod(x) for x,p in law.items()),F()) for name,law in initial.items()}
    assert sixth=={'independent':0,'parity_plus':1,'parity_minus':-1}
    repaired={name:moment_state(law,lambda x:(x[0],q(x))) for name,law in initial.items()}
    shear=EffectHistogram.from_terms(2,[(F(1),Affine(((F(1),F(1)),(F(0),F(1))),(F(0),F(0))),1)])
    trajectories={name:[] for name in initial}
    comparisons=[]
    primitive_checks=repair_checks=0
    current={name:dict(law) for name,law in initial.items()}
    for n in range(HORIZON+1):
        for name,law in current.items():
            assert law==push(initial[name],lambda x:advance(x,n))
            assert sum(law.values(),F())==1
            for x in law:
                if n<HORIZON:
                    y=advance(x)
                    delta=tuple(b-a for a,b in zip(x,y))
                    assert delta[0] in (-1,1) and delta[1:]==(0,)*5
                    assert advance(y,-1)==x and q(y)==q(x)
                    primitive_checks+=1
            expected=moment_state(law,lambda x:(x[0],q(x)))
            assert repaired[name]==expected
            repair_checks+=1
            stats=scalar_stats(law)
            expected_variance={'independent':1+n*n,'parity_plus':(n+1)**2,'parity_minus':(n-1)**2}[name]
            assert stats['variance']==expected_variance
            trajectories[name].append({'n':n,**stats,'law':encoded_law(law)})
        row={'n':n}
        for name in ('parity_plus','parity_minus'):
            full=tv(current[name],current['independent'])
            axis=tv(project(current[name],[0]),project(current['independent'],[0]))
            assert full==F(1,2)
            assert axis==(F(0) if n==0 else F(1,2))
            row[name]={'full_spatial_law_TV':full,'axis1_TV':axis}
        assert tv(current['parity_plus'],current['parity_minus'])==1
        comparisons.append(row)
        if n<HORIZON:
            current={name:push(law,advance) for name,law in current.items()}
            repaired={name:state.then(shear) for name,state in repaired.items()}
    result={'status':'PASS','researcher_id':AUDITOR,
            'activity_id':'RA-BRCAUDIT-20261002-9D72AC',
            'scope':'Fixed native X6, one chosen Cell anchor; declared conditional unit-step model; not a universal propagation law',
            'state_types':{'spatial':'six signed raw chart coordinates; not final Cell addresses',
                           'Q':'joint observer product of axes2..6; not an additional spatial axis',
                           'weights':'positive rational probabilities, not amplitudes',
                           'time':'declared ordered model-step index, no physical calibration'},
            'population':'D={x in Z6: x2..x6 in {-1,1}}; initial x1 in {-1,1}',
            'operation':'F(x)=x+Q(x)e1; inverse F^-1(x)=x-Q(x)e1; active fixed chart',
            'future_scope':'F^n for nonnegative n; repaired pair exact for joint (X1,Q) observers. Full X6 identity and arbitrary future operations are not represented by the pair.',
            'initial_laws':{name:encoded_law(law) for name,law in initial.items()},
            'same_initial_BRC_degree2_packed':states['independent'].upper,
            'initial_repaired_observer_pair_moments':{name:s.to_matrix() for name,s in {name:moment_state(law,lambda x:(x[0],q(x))) for name,law in initial.items()}.items()},
            'initial_sixth_joint_product':sixth,
            'checks':{'proper_subset_projections':63,'proper_subset_comparisons':proper_checks,
                      'subsets_by_size':proper_by_size,'degree_le5_monomials':monomial_count,
                      'initial_BRC_degree2_laws':3,'primitive_unit_step_and_inverse_checks':primitive_checks,
                      'repaired_BRC_pair_timepoints':repair_checks,'full_trajectory_rows':3*(HORIZON+1)},
            'trajectories':trajectories,'TV_comparisons':comparisons,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'production_BRC_sha256':hashlib.sha256((ROOT/'src/enterprise_math/brc_transport.py').read_bytes()).hexdigest(),
            'formal_driver_acceptance':False}
    (HERE/'parity_results.json').write_text(json.dumps(result,default=json_default,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'checks':result['checks'],'initial_sixth_joint_product':sixth},default=json_default))


if __name__=='__main__': main()
