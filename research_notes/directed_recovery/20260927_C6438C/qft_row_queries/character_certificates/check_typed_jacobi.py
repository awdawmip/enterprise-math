"""Bounded actual Jacobi and schedule evidence; no ideal QFT dynamics."""
from __future__ import annotations
from copy import deepcopy
from fractions import Fraction as F
from pathlib import Path
import gzip
import hashlib
import json
import sys

from typed_jacobi import (PREVIOUS, typed_jacobi_trace, verify_typed_jacobi,
    certify_square_schedule, verify_square_schedule, certify_program_final_bit,
    verify_program_final_bit)
from lazy_modular import lazy_modular_power_chain, digest
from stage45.brc_loop_recheck import CALLS, verify_vendor

ROOT = Path(__file__).resolve().parent
for path in (PREVIOUS / 'optimization/collision_analysis',
             PREVIOUS / 'optimization/streaming'):
    sys.path.insert(0, str(path))
from check_gram_sampler import load_bank
from lazy_streaming import LazyStreamingProgram, SelectedStreamingProgram
from stage80.fixed_phase import norm


def clean(value):
    if isinstance(value, F):
        return {'numerator': value.numerator, 'denominator': value.denominator}
    if isinstance(value, dict):
        return {str(k): clean(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [clean(v) for v in value]
    return value


def must_reject(name, action, collection):
    try:
        action()
    except ValueError as error:
        collection.append({'name': name, 'rejected': True, 'message': str(error)})
    else:
        raise AssertionError('negative control accepted: '+name)


def main():
    first = len(CALLS)
    kernel = verify_vendor()
    sources = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in (
        Path(__file__), ROOT / 'typed_jacobi.py',
        PREVIOUS / 'optimization/lazy_modular/lazy_modular.py',
        PREVIOUS / 'optimization/streaming/lazy_streaming.py')}
    # HAC Table 2.6, Example 2.152, and the cited elementary supplements.
    known = [(a, 21, j, 'HAC Table 2.6') for a, j in zip(
        [1,2,4,5,8,10,11,13,16,17,19,20], [1,-1,1,1,-1,-1,-1,-1,1,1,-1,1])]
    known += [(158,235,-1,'HAC Example 2.152'), (0,1,1,'empty denominator convention'),
        (4,1,1,'empty denominator convention'), (-2,1,1,'empty denominator convention'),
        (0,3,0,'nonunit zero'), (3,9,0,'nonunit multiple'), (7,21,0,'nonunit multiple'),
        (-1,7,-1,'minus one supplement'), (-1,5,1,'minus one supplement'),
        (-2,7,-1,'multiplicativity and supplements'), (-2,5,-1,'multiplicativity and supplements'),
        (2,9,1,'two supplement'), (2,15,1,'two supplement'), (2,35,-1,'two supplement'),
        (1 << 20,21,1,'even power of unit two'),
        (2,(1 << 65)+3,-1,'two supplement on a 66-bit odd modulus')]
    cases, negatives = [], []
    for a, N, expected, origin in known:
        start = len(CALLS)
        certificate = typed_jacobi_trace(a, N)
        assert certificate['value'] == expected
        generated_calls = len(CALLS)-start
        replay = verify_typed_jacobi(certificate)
        cases.append({'a': a, 'N': N, 'expected': expected, 'known_value_source': origin,
            'certificate': certificate, 'replay': replay,
            'native_calls_generation': generated_calls,
            'native_calls_generation_and_replay': len(CALLS)-start})
    for name, a, N in [('bool numerator', True,21), ('bool denominator',2,True),
                       ('string numerator','2',21), ('even denominator',2,20),
                       ('zero denominator',2,0), ('negative denominator',2,-3)]:
        must_reject(name, lambda a=a,N=N: typed_jacobi_trace(a,N), negatives)
    changed = deepcopy(cases[0]['certificate'])
    changed['value'] *= -1
    must_reject('changed Jacobi output',lambda: verify_typed_jacobi(changed),negatives)
    changed_trace = deepcopy(cases[1]['certificate'])
    changed_trace['steps'][0]['remainder'] += 1
    must_reject('changed typed remainder',lambda: verify_typed_jacobi(changed_trace),negatives)
    changed_source = deepcopy(cases[1]['certificate'])
    changed_source['source']['jacobi_source_sha256'] = '0'*64
    must_reject('changed source binding',lambda: verify_typed_jacobi(changed_source),negatives)

    schedules = []
    for N, expected in [(21,'CERTIFIED_FINAL_BIT_FAIR'),(35,'CERTIFIED_FINAL_BIT_FAIR'),
                        (15,'UNAVAILABLE'),(9,'UNAVAILABLE')]:
        _, ascending, _ = lazy_modular_power_chain(N, 2, 4)
        tables = tuple(reversed(ascending))
        certificate = certify_square_schedule(N,2,4,tables)
        assert certificate['status'] == expected
        schedules.append({'certificate': certificate, 'replay': verify_square_schedule(certificate,tables)})
        if N == 21:
            saved_tables, saved = tables, certificate
    unavailable = certify_square_schedule(21,2,4,saved_tables,initial_work_label=2)
    assert unavailable['status'] == 'UNAVAILABLE'
    wrong_schedule = list(saved_tables)
    wrong_schedule[0], wrong_schedule[1] = wrong_schedule[1], wrong_schedule[0]
    must_reject('wrong square schedule',lambda: certify_square_schedule(21,2,4,wrong_schedule),negatives)
    must_reject('wrong final multiplier',lambda: certify_square_schedule(21,5,4,saved_tables),negatives)
    must_reject('foreign modulus tables',lambda: certify_square_schedule(35,2,4,saved_tables),negatives)
    tampered_schedule = deepcopy(saved)
    tampered_schedule['square_chain'][0]['squared_multiplier'] += 1
    must_reject('changed schedule witness',lambda: verify_square_schedule(tampered_schedule,saved_tables),negatives)
    must_reject('nonunit multiplier',lambda: lazy_modular_power_chain(21,3,4),negatives)

    bank, bank_source = load_bank()
    program = LazyStreamingProgram(21,2,4,bank,61)
    program_certificate = certify_program_final_bit(program)
    assert program_certificate['status'] == 'CERTIFIED_FINAL_BIT_FAIR'
    program_replay = verify_program_final_bit(program_certificate,program)
    program.modular_powers = tuple(reversed(program.modular_powers))
    must_reject('program descriptor changed',lambda: verify_program_final_bit(program_certificate,program),negatives)
    program.modular_powers = tuple(reversed(program.modular_powers))
    program.initial = lambda: ({(0,2,0):(1,)+(0,)*60},1)
    must_reject('program initial injection',lambda: certify_program_final_bit(program),negatives)
    del program.initial
    must_reject('arbitrary object with metadata',lambda: certify_program_final_bit(object()),negatives)

    # Actual native instrument counterexample to dropping the reachable-state
    # precondition: history (0,) has identity feedback but an injected support
    # {1,2} overlaps its translate {2,4}. This is not an ideal reference run.
    counter = SelectedStreamingProgram(21,2,2,bank,61)
    e0 = (1,)+(0,)*60
    injected = {(0,1,0):e0, (0,2,0):e0}
    children = counter.branches(injected,1,(0,))
    parent_mass = norm(injected,1)
    masses = tuple(norm(state,den) for state,den in children)
    probabilities = tuple(m/parent_mass for m in masses)
    assert parent_mass == 2 and probabilities == (F(3,4),F(1,4))
    counterexample = {'N':21,'a':2,'t':2,'history':[0], 'Jacobi':-1,
        'injected_state':[[list(k),list(v)] for k,v in injected.items()],
        'parent_mass':parent_mass, 'actual_child_masses':masses,
        'actual_probabilities':probabilities,
        'claim':'Jacobi=-1 alone does not authorize arbitrary midrun state',
        'native_children': [[[[list(k),list(v)] for k,v in state.items()],den] for state,den in children]}
    # Conversely, UNAVAILABLE is not unfair: N15,a2 has J=+1 yet this original
    # t2 schedule reaches support {1,4}; final translate {2,8} is disjoint.
    unc = SelectedStreamingProgram(15,2,2,bank,61)
    unccert = certify_program_final_bit(unc)
    assert unccert['status'] == 'UNAVAILABLE'
    init, den = unc.initial()
    first_children = unc.branches(init,den,())
    unavailable_fair = []
    for bit,(state,den) in enumerate(first_children):
        mass = norm(state,den)
        if mass:
            final = unc.branches(state,den,(bit,))
            probabilities = tuple(norm(s,d)/mass for s,d in final)
            assert probabilities == (F(1,2),F(1,2))
            unavailable_fair.append({'history':[bit],'actual_probabilities':probabilities})

    assert sources == {path:hashlib.sha256(Path(path).read_bytes()).hexdigest() for path in sources}
    result = {'status':'AUTHOR_ACTUAL_BOUNDED_SHARED_CONTEXT_NOT_ADMITTED',
        'source_hashes':sources,'kernel_verification':kernel,
        'cases':cases,'negative_controls':negatives,'schedule_cases':schedules,
        'wrong_initial_label':unavailable,'program_certificate':program_certificate,
        'program_replay':program_replay,'phase_bank_source':bank_source,
        'arbitrary_state_counterexample':counterexample,
        'unavailable_but_actually_fair':{'program_certificate':unccert,'checks':unavailable_fair},
        'native_core_calls':CALLS[first:],
        'jacobi_initial_run_digit_replays':sum(c['certificate']['cost']['adder_digit_replays'] for c in cases),
        'jacobi_initial_run_label_wiring':sum(c['certificate']['cost']['jacobi_label_bit_wiring_operations'] for c in cases),
        'isolated_known_value_comparisons':True,'ideal_QFT_reference_run':False,
        'all_residual_coordinates_retained':True,'factor_or_order_input':False}
    raw = json.dumps(clean(result),sort_keys=True,separators=(',',':')).encode()
    (ROOT/'TYPED_JACOBI_RESULTS.json.gz').write_bytes(gzip.compress(raw,mtime=0))
    summary = {'status':result['status'],'jacobi_cases':len(cases),
        'jacobi_complete_replays':len(cases),'schedule_cases':len(schedules),
        'negative_controls_rejected':len(negatives),'program_descriptor_replay':True,
        'arbitrary_state_counterexample_probabilities':['3/4','1/4'],
        'unavailable_does_not_mean_unfair':True,
        'max_input_bits':max(max(abs(a).bit_length(),N.bit_length()) for a,N,_,_ in known),
        'native_core_calls_all_fixture_work':len(CALLS)-first,
        'jacobi_initial_run_digit_replays':result['jacobi_initial_run_digit_replays'],
        'jacobi_initial_run_label_wiring':result['jacobi_initial_run_label_wiring'],
        'source_hashes':sources,'payload_sha256':hashlib.sha256(raw).hexdigest()}
    (ROOT/'TYPED_JACOBI_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary))


if __name__ == '__main__':
    main()
