"""Bounded complete membership/address comparisons with retained typed cycles."""
from pathlib import Path
from copy import deepcopy
import gzip
import hashlib
import json
from time import perf_counter

from typed_target_address import (recover_target_address, verify_target_address,
                                  source_hashes, TargetAddressError)
from stage45.brc_loop_recheck import CALLS,verify_vendor

ROOT=Path(__file__).resolve().parent


def packed(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()


def main():
    started,first=perf_counter(),len(CALLS)
    startup=json.loads((ROOT.parent/'STARTUP_GUARD.json').read_bytes())
    assert startup['activity_allowed'] and startup['persistence_allowed'] and not startup['sync_debt_events']
    raw=gzip.decompress((ROOT.parent/'period_discovery/ODD_PART_RESULTS.json.gz').read_bytes())
    assert hashlib.sha256(raw).hexdigest()=='c885c4b10f78b1cda18ba75cd061138801d7b239c877c242b2cf64e51c0ce4a0'
    old=json.loads(raw)
    source_cases={(c['N'],c['b']):c for c in old['cases']}
    before={**source_hashes(),'check_target_address.py':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    vendor=verify_vendor()
    fixtures=((2,1,(1,)),(17,3,(16,)),(97,5,(25,)),
              (21,2,(1,2,5,3)),(21,4,(16,2)),(65,3,(1,3,2,8)))
    cases,replays=[],[]
    for N,b,targets in fixtures:
        source=source_cases[N,b]
        order=source['actual']
        # This reference was already executed and frozen by the order unit;
        # complete raw cycle provenance is retained below, not recomputed by
        # an ordinary modular arithmetic reference here.
        cycle=source['reference']['states'][:-1]
        assert len(cycle)==source['reference']['R'] and len(set(cycle))==len(cycle)
        for z in targets:
            actual=recover_target_address(order,z)
            expected=cycle.index(z) if z in cycle else None
            assert actual['status']==('MEMBER' if expected is not None else 'NONMEMBER')
            assert actual['r']==expected
            verified=verify_target_address(json.loads(packed(actual)))
            assert verified['verified']
            assert verified['replay']['status']==actual['status'] and verified['replay']['r']==actual['r']
            cases.append({'N':N,'b':b,'z':z,'actual':actual,
                          'expected_address_from_retained_typed_cycle':expected,'exact_result_equal':True})
            replays.append(verified)
            print(json.dumps({'N':N,'b':b,'z':z,'status':actual['status'],'r':actual['r']}),flush=True)
    negatives=[]
    valid=source_cases[21,2]['actual']
    partial=old['partial_cases'][0]['actual']
    forged=deepcopy(valid)
    forged['R']=1
    for name,order,z in (('zero_target',valid,0),('out_of_range_target',valid,21),
                          ('boolean_target',valid,True),('partial_order',partial,1),
                          ('forged_order',forged,1)):
        try:
            recover_target_address(order,z)
        except TargetAddressError as error:
            negatives.append({'name':name,'rejected':True,'message':str(error),'evidence':error.evidence})
        else: raise AssertionError('invalid input admitted: '+name)
    member=next(c['actual'] for c in cases if c['N']==97)
    nonmember=next(c['actual'] for c in cases if c['N']==21 and c['z']==5)
    for name in ('wrong_address','boolean_address','wrong_target','changed_lift',
                 'changed_CRT','omitted_table','underreported_cost','fake_membership'):
        changed=deepcopy(nonmember if name=='fake_membership' else member)
        if name=='wrong_address': changed['r']=0
        elif name=='boolean_address': changed['r']=True
        elif name=='wrong_target': changed['inputs']['z']=1
        elif name=='changed_lift': changed['evidence']['bit_lifts'][0]['test_value']=0
        elif name=='changed_CRT': changed['evidence']['crt']['k']=1
        elif name=='omitted_table': changed['evidence']['table_instances'].pop()
        elif name=='underreported_cost': changed['metrics']['total_adder_digit_replays']=0
        elif name=='fake_membership': changed.update(status='MEMBER',r=0)
        try:
            verify_target_address(changed)
        except ValueError as error:
            negatives.append({'name':name,'rejected':True,'message':str(error),
                              'evidence':getattr(error,'evidence',{'attempt':changed})})
        else: raise AssertionError('forged target record accepted: '+name)
    after={**source_hashes(),'check_target_address.py':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    assert before==after
    payload={'schema':'BRC_PAID_TARGET_ADDRESS_CHECKS_V1',
        'status':'AUTHOR_ACTUAL_TYPED_BOUNDED_SHARED_CONTEXT_NOT_ADMITTED',
        'source_sha256':before,'source_unchanged_during_execution':True,
        'startup_guard':startup,'vendor':vendor,
        'order_source_payload_sha256':hashlib.sha256(raw).hexdigest(),
        'retained_source_reference_cycles':[c['reference'] for c in old['cases']],
        'retained_reference_cost_is_prior_work_not_reexecuted':True,
        'cases':cases,'positive_serialized_replays':replays,'negative_controls':negatives,
        'native_core_call_receipts':CALLS[first:],'actual_native_core_calls':len(CALLS)-first,
        'elapsed_seconds':perf_counter()-started,
        'scope':'paid complete cyclic membership/address recovery on declared inputs; no phase propagation or general factoring speedup'}
    data=packed(payload)
    target=ROOT/'TARGET_ADDRESS_RESULTS.json.gz'
    target.write_bytes(gzip.compress(data,compresslevel=9,mtime=0))
    assert gzip.decompress(target.read_bytes())==data
    summary={k:payload[k] for k in ('status','source_sha256','actual_native_core_calls','elapsed_seconds')}
    summary.update(case_count=len(cases),member_cases=sum(c['actual']['status']=='MEMBER' for c in cases),
        nonmember_cases=sum(c['actual']['status']=='NONMEMBER' for c in cases),
        negative_controls_rejected=len(negatives),payload_bytes=len(data),
        payload_sha256=hashlib.sha256(data).hexdigest(),gzip_bytes=target.stat().st_size,
        gzip_sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
        case_summary=[{'N':c['N'],'b':c['b'],'z':c['z'],'status':c['actual']['status'],
            'r':c['actual']['r'],'reason':c['actual']['evidence'].get('reason'),
            'metrics':c['actual']['metrics']} for c in cases])
    (ROOT/'TARGET_ADDRESS_SUMMARY.json').write_bytes(packed(summary)+b'\n')
    print(json.dumps(summary),flush=True)


if __name__=='__main__': main()
