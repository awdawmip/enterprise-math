"""Bounded typed witnesses and actual full-native suffix checks."""
from __future__ import annotations
from pathlib import Path
from copy import deepcopy
from fractions import Fraction as F
import gzip
import hashlib
import json
import sys
from power_sum_certificate import (PREVIOUS, certify_power_sum_structure,
    verify_power_sum_structure, certify_program_suffix, verify_program_suffix)
from lazy_modular import lazy_modular_power_trace
from typed_jacobi import typed_jacobi_trace
from stage45.brc_loop_recheck import CALLS, verify_vendor

ROOT = Path(__file__).resolve().parent
for path in (PREVIOUS/'optimization/collision_analysis',PREVIOUS/'optimization/streaming'):
    sys.path.insert(0,str(path))
from check_gram_sampler import load_bank
from lazy_streaming import LazyStreamingProgram
from stage80.fixed_phase import norm


def clean(value):
    if isinstance(value,F):
        return {'numerator':value.numerator,'denominator':value.denominator}
    if isinstance(value,dict):
        return {str(k):clean(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):
        return [clean(v) for v in value]
    return value


def pack_state(state,den):
    return {'denominator':den,'rows':[[list(key),list(value)] for key,value in sorted(state.items())]}


def reject(name,action,results):
    try:
        action()
    except ValueError as error:
        results.append({'name':name,'rejected':True,'message':str(error)})
    else:
        raise AssertionError('accepted negative control: '+name)


def full_suffix_case(bank,N,a,ell,u,v):
    program = LazyStreamingProgram(N,a,4,bank,61)
    certificate = certify_program_suffix(program,ell,u,v)
    assert certificate['status'] == 'CERTIFIED_UNIFORM_TERMINAL_SUFFIX'
    replay = verify_program_suffix(certificate,program)
    initial,den = program.initial()
    frontier = {(): (initial,den)}
    prefix_records, term_mass, fair_edges = [],F(0),0
    for depth in range(program.t):
        following = {}
        for history,(state,den) in frontier.items():
            mass = norm(state,den)
            assert mass > 0
            children = program.branches(state,den,history)
            child_masses = tuple(norm(s,d) for s,d in children)
            assert sum(child_masses,F(0)) == mass
            if depth >= program.t-ell:
                assert child_masses == (mass/2,mass/2)
                fair_edges += 2
            prefix_records.append({'history':history,'parent_mass':mass,'child_masses':child_masses,
                'claimed_suffix':depth >= program.t-ell,
                'parent':pack_state(state,den),
                'children':[pack_state(s,d) for s,d in children]})
            for bit,(child,child_den) in enumerate(children):
                if child_masses[bit]:
                    if depth+1 == program.t:
                        term_mass += child_masses[bit]
                    else:
                        following[history+(bit,)] = (child,child_den)
        frontier = following
    assert term_mass == 1
    return {'N':N,'a':a,'t':4,'ell':ell,'certificate':certificate,'replay':replay,
        'complete_native_prefix_checks':prefix_records,'certified_fair_child_edges':fair_edges,
        'total_terminal_mass':term_mass,'all_61_coordinates_retained':True,
        'metrics':program.report_metrics()}


def main():
    first = len(CALLS)
    kernel = verify_vendor()
    files = [Path(__file__),ROOT/'power_sum_certificate.py']
    source_hashes = {str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    fixtures = [(65,3,2,1,8),(85,2,2,2,9),(4097,3,3,8,1),
        (4294967297,3,6,2,1),(18446744073709551617,3,7,2,1),
        (65,2,2,1,8)]
    cases,negatives = [],[]
    for args in fixtures:
        certificate = certify_power_sum_structure(*args)
        expected = 'UNAVAILABLE' if args[:2] == (65,2) else 'CERTIFIED_TWO_PART_LOWER_BOUND'
        assert certificate['status'] == expected
        cases.append({'certificate':certificate,'replay':verify_power_sum_structure(certificate)})
    for name,args in [
        ('even modulus',(66,3,2,1,8)),('zero ell',(65,3,0,1,8)),
        ('boolean ell',(65,3,True,1,8)),('boolean witness',(65,3,2,True,8)),
        ('negative witness',(65,3,2,-1,8)),('same parity',(65,3,2,1,3)),
        ('false sum',(65,3,2,1,6)),('nonprimitive witness',(45,2,2,3,6)),
        ('impossible enormous degree',(65,3,1000000,1,2)),
        ('wrong degree',(65,3,3,1,8)),('noncanonical base',(65,65,2,1,8))]:
        reject(name,lambda args=args:certify_power_sum_structure(*args),negatives)
    changed = deepcopy(cases[0]['certificate'])
    changed['certified_suffix_bits'] += 1
    reject('changed proved suffix',lambda:verify_power_sum_structure(changed),negatives)
    changed_arithmetic = deepcopy(cases[0]['certificate'])
    changed_arithmetic['powers'][1]['steps'][0]['output'] += 1
    reject('changed actual square result',lambda:verify_power_sum_structure(changed_arithmetic),negatives)
    changed_source = deepcopy(cases[0]['certificate'])
    changed_source['source']['power_sum_source_sha256'] = '0'*64
    reject('changed source',lambda:verify_power_sum_structure(changed_source),negatives)

    bank,bank_source = load_bank()
    full = [full_suffix_case(bank,65,3,2,1,8),full_suffix_case(bank,4097,3,3,8,1)]
    p = LazyStreamingProgram(65,3,4,bank,61)
    reject('suffix longer than schedule',lambda:certify_program_suffix(p,5,1,8),negatives)
    wrong_program = deepcopy(full[0]['certificate'])
    wrong_program['suffix_start_depth'] += 1
    reject('changed suffix boundary',lambda:verify_program_suffix(wrong_program,p),negatives)
    p.initial = lambda: ({(0,3,0):(1,)+(0,)*60},1)
    reject('injected initial work',lambda:certify_program_suffix(p,2,1,8),negatives)
    del p.initial

    # Structural counterexample: N=21 is 1 modulo 4 and J(2,21)=-1,
    # yet actual typed 2^6=1 modulo 21 implies its order cannot be divisible by 4.
    # This is a finite arithmetic witness, not an order-search or QFT reference.
    boundary = {'N':21,'a':2,'N_low_two_bits':21 & 3,
        'jacobi':typed_jacobi_trace(2,21),
        'power_six':lazy_modular_power_trace(21,2,6)}
    assert boundary['jacobi']['value'] == -1 and boundary['power_six']['value'] == 1
    assert source_hashes == {str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    result = {'status':'AUTHOR_ACTUAL_BOUNDED_SHARED_CONTEXT_NOT_ADMITTED',
        'source_hashes':source_hashes,'kernel_verification':kernel,
        'structure_cases':cases,'negative_controls':negatives,
        'actual_full_program_cases':full,'phase_bank_source':bank_source,
        'modulus_congruence_only_counterexample':boundary,
        'native_core_calls':CALLS[first:],
        'factor_or_order_input':False,'order_value_computed':False,
        'ideal_reference_simulation':False,'bare_label_color_oracle_implemented':False,
        'resource_scope':'witness-only large cases; full actual instrument comparison only the two t4 cases'}
    raw = json.dumps(clean(result),sort_keys=True,separators=(',',':')).encode()
    (ROOT/'POWER_SUM_CERTIFICATE_RESULTS.json.gz').write_bytes(gzip.compress(raw,mtime=0))
    digits = sum(c['certificate']['arithmetic_cost']['adder_digit_replays']
        + c['certificate']['primitive_witness_gcd']['cost']['adder_digit_replays']
        + c['certificate']['jacobi']['cost']['adder_digit_replays'] for c in cases)
    summary = {'status':result['status'],'structure_cases':len(cases),'complete_structure_replays':len(cases),
        'certified_lengths':[c['certificate']['certified_suffix_bits'] for c in cases],
        'maximum_modulus_bits':max(x[0].bit_length() for x in fixtures),
        'full_actual_program_cases':len(full),
        'full_actual_positive_prefixes':sum(len(x['complete_native_prefix_checks']) for x in full),
        'certified_fair_child_edges':sum(x['certified_fair_child_edges'] for x in full),
        'negative_controls_rejected':len(negatives),
        'initial_structure_runs_adder_digit_replays':digits,
        'all_fixture_native_core_calls':len(CALLS)-first,
        'source_hashes':source_hashes,'payload_sha256':hashlib.sha256(raw).hexdigest()}
    (ROOT/'POWER_SUM_CERTIFICATE_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary))


if __name__ == '__main__':
    main()
