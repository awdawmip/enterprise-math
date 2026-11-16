#!/usr/bin/env python3
"""Adversarial unit tests of an optimization-safe Helly X6 type guard.
These are synthetic producer payloads, NOT the original-source full Helly run.
"""
from copy import deepcopy
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from types import SimpleNamespace

p=Path(__file__).with_name('X6_LP003_HELLY_FIXED_POSITIVE_CHART_TYPED_OUTPUT_REGRESSION_20261114.py')
spec=spec_from_file_location('guard',p)
m=module_from_spec(spec); spec.loader.exec_module(m)

def good():
    return {
        'fixed_sector_chart':{
            'globally_feasible':True,'common_a_values':[5,6,7],
            'common_b_values':[3,4], 'coordinate_type':'FIXED_POSITIVE_S12_LOCAL_CHART',
            'sample_fixed_positive_chart_address':[5,3,0],
            'native_cell_address_status':
                'UNSPECIFIED_REQUIRES_CELL_ANCHOR_AND_ORDERED_SIGNED_AXIS_EMBEDDING'},
        'typed_boolean_brc_support':{
            'globally_feasible':True, 'coordinatewise_common_values':([1],[1],[0]),
            'sample_support_mask':[1,1,0],
            'two_constraint_conflict_verified':True}}

def producer(data, boxes=0, chain=True, carath=True):
    calls=[]
    def invoke(name, result):
        calls.append(name)
        return result
    obj=SimpleNamespace(
        check_enterprise_demos=lambda:invoke('demos',data),
        check_interval_boxes=lambda:invoke('boxes',{'helly2_violations':boxes}),
        check_unbounded_chain=lambda:invoke('chain',{'all_minimal_obstructions_verified':chain}),
        check_carath_lower_bound=lambda:invoke('carath',{'all_lower_bounds_verified':carath}))
    return obj,calls

obj,calls=producer(good())
if m.verify_typed_helly_producer(obj) is not True or calls!=['demos','boxes','chain','carath']:
    raise AssertionError('valid fixture or evidence execution differs')

bad=[]
a=good(); a['fixed_sector_chart']['coordinate_type']='NATIVE_X6_CELL';bad.append(('wrong_coordinate_type',a,{}))
a=good(); a['fixed_sector_chart']['native_cell_address_status']='CERTIFIED_X6_NATIVE';bad.append(('fake_native_status',a,{}))
a=good(); a['fixed_sector_chart']['sample_native_address']=[5,3,0];bad.append(('native_identity_leak',a,{}))
a=good(); a['fixed_sector_chart']['common_a_values']=[5,6];bad.append(('wrong_chart_intersection',a,{}))
bad.append(('helly_violation',good(),{'boxes':1}))
bad.append(('chain_violation',good(),{'chain':False}))
bad.append(('carath_violation',good(),{'carath':False}))
for name,payload,kwargs in bad:
    obj,calls=producer(payload,**kwargs)
    try: m.verify_typed_helly_producer(obj)
    except AssertionError: pass
    else: raise AssertionError('FAILED_TO_REJECT_'+name)
print('PASS_HELLY_TYPED_GUARD_OPTIMIZATION_SAFE_SYNTHETIC 1_valid 7_invalid')
