#!/usr/bin/env python3
"""Read-only quick verification of the C87 position artifacts.

Recomputes the two stored one-dimensional integrals and the fourteen exact
weight integrations. It does not rerun the adaptive family search, alter a
certificate, regenerate exploratory values, or compare timing metadata.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

import certify_axis_midpoint as axis
import certify_position_values as values

HERE=Path(__file__).resolve().parent


def verify():
    a_path=HERE/'axis_midpoint_certificate.json'
    f_path=HERE.parent/'integrated_kernel_certificate.json'
    v_path=HERE/'position_value_certificate.json'
    a=json.loads(a_path.read_text())
    f=json.loads(f_path.read_text())
    v=json.loads(v_path.read_text())
    terms,source_hash=axis.terms_from_json()
    assert source_hash==a['chamber_source_sha256']==f['chamber_source_sha256']
    assert v['input_sha256']['axis_midpoint_certificate.json']==hashlib.sha256(a_path.read_bytes()).hexdigest()
    assert v['input_sha256']['integrated_kernel_certificate.json']==hashlib.sha256(f_path.read_bytes()).hexdigest()
    for name,digest in f['source_sha256'].items():
        assert hashlib.sha256((HERE.parent/name).read_bytes()).hexdigest()==digest
    b_families={ri:[(b,c,w)for z,b,c,w in terms[ri,0]if not z]for ri in range(4)}
    m_families={ri:[(z+b,c,w)for z,b,c,w in terms[ri,ri]]for ri in range(4)}
    b=axis.integrate_rows(b_families,a['n'])
    m=axis.integrate_rows(m_families,a['n'])
    assert {k:x.json()for k,x in b.items()}==a['b2']
    assert {k:x.json()for k,x in m.items()}==a['A_at_one']
    a2,expression,E=axis.axis_expansion(terms,F(1,8))
    assert a2.json()==a['a2']
    assert str(E)==a['axis_remainder_constant']
    lower=a2-F(433,1000)*axis.root20(F(1,8))-E/8
    assert lower.json()==a['axis_lower_bound']
    assert F(b['integral'].lo,axis.Q)>-F(433,1000)
    assert F(lower.lo,axis.Q)>F(1,40)
    factor=2/(axis.ZETA*F(19,20)*F(21,20)*F(41,20))
    assert (-factor*a2).json()==a['endpoint_second_derivative']
    assert (-8*factor*m['integral']).json()==a['midpoint_second_derivative']
    models=values.models_from_certificate(f)
    computed=[values.value(F(row['theta']),models,a2,b['integral'],E)for row in v['values']]
    assert computed==v['values']
    assert len(computed)==14
    assert all(int(row['I_theta_minus_mid']['upper_numerator'])<0 and
               int(row['first_derivative']['lower_numerator'])>0 for row in computed[:-1])
    assert computed[-1]['theta']=='1/2'
    for key in ('I_theta_minus_mid','first_derivative'):
        assert computed[-1][key]['lower_numerator']==computed[-1][key]['upper_numerator']=='0'
    exploratory_checks=0
    exploratory=HERE/'position_exploration_64.json'
    if exploratory.exists():
        e=json.loads(exploratory.read_text())
        assert e['status']=='exploratory_not_certified'
        assert len(e['values'])==len(computed)
        for observation,certificate in zip(e['values'],computed):
            for key in ('I_theta_minus_mid','first_derivative'):
                interval=values.restore(certificate[key])
                value=F(str(observation[key]))
                assert F(interval.lo,axis.Q)<=value<=F(interval.hi,axis.Q)
            exploratory_checks+=1
    return {'status':'PASS','read_only':True,
            'exact_axis_cancellations_and_remainder':'verified',
            'recomputed_radial_integrals':2,'radial_grid':a['n'],
            'family_intervals_checked_for_complete_coverage':len(models),
            'adaptive_family_cubature_rerun':False,
            'exact_position_weight_integrations':len(computed),
            'exploratory_points_inside_certified_intervals':exploratory_checks,
            'certificate_files_modified':False}


if __name__=='__main__':print(json.dumps(verify(),indent=2))
