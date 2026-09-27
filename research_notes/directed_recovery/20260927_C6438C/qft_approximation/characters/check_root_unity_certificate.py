"""Bounded actual arithmetic and native-program bindings of public roots."""
from __future__ import annotations
from pathlib import Path
from copy import deepcopy
import gzip
import hashlib
import json
import sys
from root_unity_certificate import (PREVIOUS,certify_root_structure,verify_root_structure,
    certify_program_root_suffix,verify_program_root_suffix)
from stage45.brc_loop_recheck import CALLS,verify_vendor

ROOT=Path(__file__).resolve().parent
for path in (PREVIOUS/'optimization/collision_analysis',PREVIOUS/'optimization/streaming'):
    sys.path.insert(0,str(path))
from check_gram_sampler import load_bank
from lazy_streaming import LazyStreamingProgram
from check_power_sum_certificate import clean,reject,pack_state
from stage80.fixed_phase import norm


def main():
    first=len(CALLS)
    kernel=verify_vendor()
    files=(Path(__file__),ROOT/'root_unity_certificate.py')
    hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    fixtures=[(21,2,1,20),(65,3,2,8),(4097,3,3,8),
              (257,5,8,3),(65537,5,16,3),(257,3,8,3),(65,2,2,8)]
    cases,negatives=[],[]
    for args in fixtures:
        certificate=certify_root_structure(*args)
        expected='UNAVAILABLE' if args[:2]==(65,2) else 'CERTIFIED_TWO_PART_LOWER_BOUND'
        assert certificate['status']==expected
        if args[1]==args[3]:
            assert certificate['a_equals_public_root']
            assert certificate['shor_base_order_certified_if_same_root']==1 << args[2]
        cases.append({'certificate':certificate,'replay':verify_root_structure(certificate)})
    for name,args in [('even modulus',(66,3,2,8)),('zero ell',(65,3,0,8)),
        ('boolean ell',(65,3,True,8)),('boolean root',(65,3,2,True)),
        ('noncanonical root',(65,3,2,65)),('zero root',(65,3,2,0)),
        ('noncanonical base',(65,65,2,8)),('false root',(65,3,2,7)),
        ('nonunit root',(65,3,2,5)),('overclaimed root order',(65,3,3,8)),
        ('impossible enormous degree',(65,3,1000000,8))]:
        reject(name,lambda args=args:certify_root_structure(*args),negatives)
    changed=deepcopy(cases[1]['certificate'])
    changed['certified_suffix_bits']+=1
    reject('changed proved suffix',lambda:verify_root_structure(changed),negatives)
    changed_square=deepcopy(cases[1]['certificate'])
    changed_square['modular_square_steps'][0]['output']+=1
    reject('changed actual square',lambda:verify_root_structure(changed_square),negatives)
    changed_source=deepcopy(cases[1]['certificate'])
    changed_source['source']['root_unity_source_sha256']='0'*64
    reject('changed source',lambda:verify_root_structure(changed_source),negatives)

    bank,bank_source=load_bank()
    native=[]
    for N,a,ell,b in fixtures[1:3]:
        program=LazyStreamingProgram(N,a,4,bank,61)
        certificate=certify_program_root_suffix(program,ell,b)
        assert certificate['status']=='CERTIFIED_UNIFORM_TERMINAL_SUFFIX'
        replay=verify_program_root_suffix(certificate,program)
        state,den=program.initial()
        frontier={(): (state,den)}
        prefixes,fair_edges,total=[],0,0
        for depth in range(program.t):
            following={}
            for history,(state,den) in frontier.items():
                parent=norm(state,den)
                children=program.branches(state,den,history)
                masses=tuple(norm(s,d) for s,d in children)
                assert sum(masses)==parent
                if depth>=program.t-ell:
                    assert masses==(parent/2,parent/2)
                    fair_edges+=2
                prefixes.append({'history':history,'parent_mass':parent,'child_masses':masses,
                    'parent':pack_state(state,den),'children':[pack_state(s,d) for s,d in children]})
                for bit,child in enumerate(children):
                    if masses[bit]:
                        if depth+1==program.t:total+=masses[bit]
                        else:following[history+(bit,)]=child
            frontier=following
        assert total==1
        native.append({'N':N,'a':a,'ell':ell,'b':b,'t':4,'certificate':certificate,
            'replay':replay,'complete_native_prefix_checks':prefixes,
            'certified_fair_child_edges':fair_edges,'total_terminal_mass':total,
            'all_61_coordinates_retained':True,'metrics':program.report_metrics()})
    program=LazyStreamingProgram(65,3,4,bank,61)
    reject('suffix exceeds program',lambda:certify_program_root_suffix(program,5,8),negatives)
    wrong=deepcopy(native[0]['certificate'])
    wrong['suffix_start_depth']+=1
    reject('changed suffix boundary',lambda:verify_program_root_suffix(wrong,program),negatives)
    program.initial=lambda: ({(0,3,0):(1,)+(0,)*60},1)
    reject('injected initial work',lambda:certify_program_root_suffix(program,2,8),negatives)
    del program.initial
    assert hashes=={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    result={'status':'AUTHOR_ACTUAL_BOUNDED_SHARED_CONTEXT_NOT_ADMITTED',
        'source_hashes':hashes,'kernel_verification':kernel,'structure_cases':cases,
        'actual_full_program_cases':native,'phase_bank_source':bank_source,
        'negative_controls':negatives,'native_core_calls':CALLS[first:],
        'factor_or_shor_base_order_input':False,'root_witness_search_performed':False,
        'ideal_reference_simulation':False,'bare_label_color_oracle_implemented':False,
        'runtime_root_walker_implemented':False,
        'resource_scope':'ell8/16 are arithmetic certificates only; full native instrument only two t4 fixtures'}
    raw=json.dumps(clean(result),sort_keys=True,separators=(',',':')).encode()
    (ROOT/'ROOT_UNITY_CERTIFICATE_RESULTS.json.gz').write_bytes(gzip.compress(raw,mtime=0))
    digits=sum(c['certificate']['arithmetic_cost']['adder_digit_replays']
               +c['certificate']['jacobi']['cost']['adder_digit_replays'] for c in cases)
    summary={'status':result['status'],'structure_cases':len(cases),'complete_structure_replays':len(cases),
        'certified_lengths':[c['certificate']['certified_suffix_bits'] for c in cases],
        'full_actual_program_cases':len(native),
        'full_actual_positive_prefixes':sum(len(x['complete_native_prefix_checks']) for x in native),
        'certified_fair_child_edges':sum(x['certified_fair_child_edges'] for x in native),
        'negative_controls_rejected':len(negatives),'initial_structure_adder_digit_replays':digits,
        'all_fixture_native_core_calls':len(CALLS)-first,'source_hashes':hashes,
        'payload_sha256':hashlib.sha256(raw).hexdigest()}
    (ROOT/'ROOT_UNITY_CERTIFICATE_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary))


if __name__=='__main__': main()
