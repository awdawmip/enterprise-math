"""Bounded complete alias checks against consecutive actual typed columns.

The comparison is a same-arithmetic finite enumeration, not ordinary pow/mod
and not an ideal state or phase reference. All evidence is retained.
"""
from pathlib import Path
from copy import copy, deepcopy
import gzip
import hashlib
import json
import sys
from time import perf_counter
from fractions import Fraction

ROOT = Path(__file__).resolve().parent
OLD = ROOT.parents[1] / 'sep26-shor-general'
sys.path.insert(0, str(OLD / 'optimization/collision_analysis'))
from check_gram_sampler import load_bank
from lazy_streaming import LazyStreamingProgram
from lazy_modular import LazyModularFactory, verify_lazy_permutation
from typed_aliases import discover_aliases, verify_alias_result, AliasDiscoveryError, source_hashes
from stage45.brc_loop_recheck import CALLS, verify_vendor


def packed(value):
    def exact_default(item):
        if isinstance(item, Fraction):
            return str(item)
        raise TypeError('unsupported evidence value: '+type(item).__name__)
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False,
                      default=exact_default).encode()


def consecutive_reference(program, depth, targets):
    """All +/- magnitudes observed from forward/inverse typed permutations."""
    if depth == 0:
        return {'aliases': {z: ((0,) if z == 1 else ()) for z in targets},
                'powers': [{'magnitude': 0, 'positive': 1, 'negative': 1}], 'tables': []}
    factory = LazyModularFactory()
    b = program.modular_powers[depth-1]
    forward = factory(program.N, b)
    inverse = factory(program.N, forward.inverse_multiplier)
    proof = [verify_lazy_permutation(x) for x in factory.tables.values()]
    positive, negative = 1, 1
    aliases = {z: [] for z in targets}
    powers = []
    for d in range(1 << depth):
        powers.append({'magnitude': d, 'positive': positive, 'negative': negative})
        for z in targets:
            if positive == z:
                aliases[z].append(d)
            if d and negative == z:
                aliases[z].append(-d)
        if d+1 < 1 << depth:
            positive, negative = forward[positive], inverse[negative]
    return {'aliases': {z: tuple(sorted(ds)) for z, ds in aliases.items()},
            'powers': powers, 'tables': factory.export_certificate(), 'verifications': proof}


def main():
    start_time = perf_counter()
    first = len(CALLS)
    startup = json.loads((ROOT.parent / 'STARTUP_GUARD.json').read_bytes())
    assert startup['activity_allowed'] and startup['persistence_allowed'] and not startup['sync_debt_events']
    policy = json.loads((ROOT / 'POLICY_READBACK.json').read_bytes())
    assert 'ACTUAL_TYPED_BRC_ONLY' in policy['machine']['content']
    before = {**source_hashes(), 'check_typed_aliases.py': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    kernel = verify_vendor()
    bank, bank_source = load_bank()
    cases, programs = [], []
    # Declared finite fixtures; targets include units outside the preparation
    # subgroup, duplicates and both unit target orientations.
    for N, a, targets in ((21, 2, (1, 2, 5, 1)), (65, 3, (1, 3, 2, 1))):
        program = LazyStreamingProgram(N, a, 4, bank, 61)
        programs.append(program)
        for depth in range(5):
            width = min(3, 1 << depth)
            actual = discover_aliases(program, depth, targets, width)
            reference = consecutive_reference(program, depth, tuple(sorted(set(targets))))
            assert actual['aliases'] == reference['aliases']
            for ds in actual['aliases'].values():
                assert len(ds) == len(set(ds))
            cases.append({'N': N, 'a': a, 'depth': depth, 'width': width,
                          'actual': actual, 'reference': reference, 'complete_aliases_equal': True})
        # Width eight is larger than the actual small order in these declared
        # schedules. It forces repeated baby labels, not an assumed period.
        actual = discover_aliases(program, 3, targets, 8)
        reference = consecutive_reference(program, 3, tuple(sorted(set(targets))))
        assert actual['aliases'] == reference['aliases']
        assert actual['short_period'] is not None
        assert any(len(x['exponents']) > 1 for x in actual['evidence']['baby_buckets'])
        cases.append({'N': N, 'a': a, 'depth': 3, 'width': 8,
                      'actual': actual, 'reference': reference, 'complete_aliases_equal': True,
                      'repeated_baby_labels_present': True})
        print(json.dumps({'N': N, 'cases': 6, 'full_aliases_equal': True}), flush=True)
    replay = verify_alias_result(programs[0], cases[2]['actual'])
    assert replay['verified']
    failures = []
    program = programs[0]
    mismatched = copy(program)
    mismatched.modular_powers = (1, *program.modular_powers[1:])
    forged = copy(program)
    forged.tables = list(program.tables)
    forged.tables[0] = copy(program.tables[0])
    forged.tables[0].permutation_certificate = deepcopy(program.tables[0].permutation_certificate)
    forged.tables[0].permutation_certificate['inverse_certificate']['inverse_multiplier'] = 0
    for name, p, depth, targets, width in (
        ('negative_depth', program, -1, (1,), 1),
        ('future_depth', program, 5, (1,), 1),
        ('boolean_depth', program, True, (1,), 1),
        ('zero_width', program, 2, (1,), 0),
        ('oversized_width', program, 2, (1,), 5),
        ('out_of_domain_target', program, 2, (21,), 2),
        ('boolean_target', program, 2, (True,), 2),
        ('nonunit_target_full_failed_gcd_trace', program, 2, (3,), 2),
        ('schedule_table_mismatch', mismatched, 1, (1,), 1),
        ('forged_program_inverse_proof', forged, 1, (1,), 1),
    ):
        try:
            discover_aliases(p, depth, targets, width)
        except AliasDiscoveryError as e:
            failures.append({'name': name, 'rejected': True, 'message': str(e),
                             'evidence': e.evidence, 'metrics': e.metrics})
        else:
            raise AssertionError('negative control accepted: '+name)
    tampered = deepcopy(cases[2]['actual'])
    tampered['aliases'][1] = ()
    try:
        verify_alias_result(program, tampered)
    except ValueError as error:
        failures.append({'name': 'omitted_alias_output', 'rejected': True,
                         'message': str(error), 'tampered_record': tampered,
                         'verification_replay_reference': replay})
    else:
        raise AssertionError('omitted alias accepted')
    after = {**source_hashes(), 'check_typed_aliases.py': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    assert before == after
    payload = {'schema': 'BRC_BOUNDED_COMPLETE_ALIASES_CHECKS_V1',
        'status': 'AUTHOR_ACTUAL_TYPED_BOUNDED_SHARED_CONTEXT_NOT_ADMITTED',
        'source_sha256': before, 'source_unchanged_during_execution': True,
        'startup_guard': startup, 'kernel': kernel, 'bank_source': bank_source,
        'programs': [{'N': p.N, 'a': p.a, 't': p.t, 'dimension': p.dim,
            'phase_bindings': p.phase_bindings, 'h4_binding': p.h4_binding,
            'modular_powers': p.modular_powers,
            'modular_tables': p.lazy_factory.export_certificate(),
            'permutation_verifications': p.lazy_permutation_verifications} for p in programs],
        'cases': cases, 'complete_result_replay': replay,
        'negative_controls': failures,
        'native_core_call_receipts': CALLS[first:], 'actual_native_core_calls': len(CALLS)-first,
        'elapsed_seconds': perf_counter()-start_time,
        'no_ordinary_modular_pow_or_mod_reference': True,
        'scope': 'All signed bounded aliases for fixed inputs; no new phase propagation and no polynomial bit-complexity claim.'}
    raw = packed(payload)
    target = ROOT / 'TYPED_ALIASES_RESULTS.json.gz'
    target.write_bytes(gzip.compress(raw, mtime=0))
    assert gzip.decompress(target.read_bytes()) == raw
    summary = {'status': payload['status'], 'cases': len(cases),
        'complete_aliases_equal': all(x['complete_aliases_equal'] for x in cases),
        'negative_controls_rejected': len(failures),
        'actual_native_core_calls': payload['actual_native_core_calls'],
        'payload_bytes': len(raw), 'payload_sha256': hashlib.sha256(raw).hexdigest(),
        'gzip_bytes': target.stat().st_size, 'gzip_sha256': hashlib.sha256(target.read_bytes()).hexdigest(),
        'source_sha256': before, 'elapsed_seconds': payload['elapsed_seconds'],
        'case_metrics': [{'N': x['N'], 'depth': x['depth'], 'width': x['width'],
                         'short_period': x['actual']['short_period'],
                         'aliases': x['actual']['aliases'], 'metrics': x['actual']['metrics']} for x in cases]}
    (ROOT / 'TYPED_ALIASES_SUMMARY.json').write_bytes(packed(summary)+b'\n')
    print(json.dumps({k:v for k,v in summary.items() if k != 'case_metrics'}), flush=True)


if __name__ == '__main__':
    main()
