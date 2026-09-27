"""Declared actual typed and full-signed-matrix checks; no ideal reference."""
from copy import deepcopy
from pathlib import Path
from fractions import Fraction
from time import perf_counter
import gzip
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parents[1]
for directory in (ROOT, BASE / 'sep27-qft-carry-execution/modular_alias',
                  BASE / 'sep26-shor-general/optimization/collision_analysis'):
    sys.path.insert(0, str(directory))
from leading_zero_aggregator import LeadingZeroAggregator
from paid_aggregator import CarryExecutor, source_hashes
from check_gram_sampler import load_bank, ExactCarrierCodec, LazyStreamingProgram
from typed_aliases import discover_aliases
from stage45.brc_loop_recheck import CALLS, verify_vendor


def packed(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'),
        default=lambda x: str(x) if isinstance(x, Fraction) else (_ for _ in ()).throw(TypeError(type(x).__name__))).encode()


def sources():
    hashes = source_hashes()
    for name in ('leading_zero_aggregator.py', 'check_paid_aggregation.py'):
        hashes[name] = hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
    return hashes


def main():
    first, started = len(CALLS), perf_counter()
    guard = json.loads((ROOT.parent/'STARTUP_GUARD.json').read_bytes())
    assert guard['activity_allowed'] and guard['persistence_allowed'] and not guard['sync_debt_events']
    before = sources()
    assert before['carry_executor.py'] == 'f017b1fb1516e8faa97afd39d663e4eda6d21cad95f65bb2ccf5a79d7ff3b810'
    assert before['typed_odd_part.py'] == '188defd9307e461e8617243f76a8b6109309d6ac6b1834a71511172b58a6618c'
    vendor = verify_vendor()
    bank, bank_source = load_bank()
    programs, addresses, alias_records, cases, evidence, negatives = [], [], [], [], [], []
    fixtures = ((21, 2, 3, (0, 0, 0)), (21, 2, 4, (0, 1, 0, 1)),
        (65, 3, 4, (0, 0, 1, 1)), (17, 3, 4, (0, 0, 0, 1)),
        (17, 4, 3, (0, 0, 1)), (97, 5, 2, (0, 1)))
    saved = None
    for N, a, depth, history in fixtures:
        program = LazyStreamingProgram(N, a, 4, bank, 61,
            codec=ExactCarrierCodec(61, tuple(range(6))))
        programs.append(program)
        agg = LeadingZeroAggregator(program, history)
        base = CarryExecutor(program, history)
        targets = (1, program.modular_powers[depth-1])
        aliases = discover_aliases(program, depth, targets, 3)
        alias_records.append(aliases)
        for target in targets:
            cert = agg.discover_address(depth, target, 3)
            addresses.append(cert)
            actions0, calls0 = agg.stats['native_phase_vector_applications'], len(CALLS)
            actual = agg.gamma_with_address(depth, target, cert)
            ordinary_cost = {'phase_vector_actions': agg.stats['native_phase_vector_applications']-actions0,
                'actual_core_calls': len(CALLS)-calls0}
            query = deepcopy(agg.aggregation_queries[-1])
            actions0, calls0 = agg.stats['native_phase_vector_applications'], len(CALLS)
            counted = agg.gamma_leading_zero(depth, target, cert)
            leading_query = agg.aggregation_queries[-1]
            suffix = leading_query.get('suffix_evidence', {})
            leading_cost = {'phase_vector_actions': suffix.get('inherited_action_stats', {}).get('native_phase_vector_applications', 0),
                'actual_core_calls': len(CALLS)-calls0,
                'suffix_coefficient_method_invocations': suffix.get('carry_stats', {}).get('coefficient_queries', 0),
                'weighted_matrix_terms': leading_query.get('weighted_matrix_terms', 0),
                'typed_count_digit_replays': leading_query.get('index_arithmetic_stats', {}).get('adder_digit_replays', 0)}
            base_actions0, calls0 = base.stats['native_phase_vector_applications'], len(CALLS)
            expected = base.sum_coefficients(depth, aliases['aliases'][target])
            baseline_cost = {'phase_vector_actions': base.stats['native_phase_vector_applications']-base_actions0,
                'actual_core_calls': len(CALLS)-calls0, 'alias_count': len(aliases['aliases'][target])}
            assert actual == counted == expected
            case = {'N': N, 'a': a, 'depth': depth, 'history': history,
                'target': target, 'r': cert['r'], 'R': cert['R'], 's': cert['s'], 'q': cert['q'],
                'K': leading_query['K'], 'ell': leading_query['ell'], 'g': leading_query['g'], 'M': leading_query['M'],
                'all_matrix_entries_equal': True, 'matrix': {'rows': actual.rows, 'den': actual.den},
                'any_residual_row_or_column_entry': any(v for j,row in enumerate(actual.rows)
                    for k,v in enumerate(row) if j >= 2 or k >= 2),
                'address_cost': cert['metrics'], 'ordinary_cost': ordinary_cost,
                'leading_cost': leading_cost, 'baseline_cost': baseline_cost,
                'aliases': aliases['aliases'][target]}
            cases.append(case)
            print(json.dumps({k:v for k,v in case.items() if k not in ('matrix', 'address_cost')}), flush=True)
            if saved is None:
                saved = (agg, depth, target, cert)
        evidence.append({'paid': agg.evidence(), 'baseline': base.evidence()})
    # Independent typed alias search establishes no displacement for this unit.
    program = LazyStreamingProgram(65, 9, 4, bank, 61,
        codec=ExactCarrierCodec(61, tuple(range(6))))
    programs.append(program)
    agg = LeadingZeroAggregator(program, (1,0,1,0))
    for target in (2, 5):
        cert = agg.discover_address(4, target, 3)
        addresses.append(cert)
        assert cert['status'] == 'NONMEMBER'
        ordinary = agg.gamma_with_address(4, target, cert)
        counted = agg.gamma_leading_zero(4, target, cert)
        assert ordinary == counted == agg._zero()
        if target == 2:
            aliases = discover_aliases(program, 4, (target,), 3)
            alias_records.append(aliases)
            assert not aliases['aliases'][target]
        cases.append({'N':65, 'a':9, 'depth':4, 'target':target, 'status':'NONMEMBER',
            'all_matrix_entries_equal':True, 'nonunit_target':target == 5})
    evidence.append({'paid':agg.evidence()})
    agg, depth, target, cert = saved
    bad_r, bad_status, bad_source = deepcopy(cert), deepcopy(cert), deepcopy(cert)
    bad_r['r'] = cert['R']
    bad_status['status'] = 'NONMEMBER'
    bad_source['order_certificate']['evidence']['source_sha256']['typed_odd_part.py'] = '0'*64
    controls = [('wrong_address', target, bad_r), ('forged_membership', target, bad_status),
        ('wrong_source', target, bad_source), ('boolean_target', True, cert),
        ('different_target', 2, cert)]
    for name, z, record in controls:
        try:
            agg.gamma_with_address(depth, z, record)
        except ValueError as error:
            negatives.append({'name':name, 'rejected':True, 'message':str(error),
                'failed_replay_evidence':getattr(error,'evidence',None)})
        else:
            raise AssertionError('negative accepted: '+name)
    try:
        agg.discover_address(depth, target, 0)
    except ValueError as error:
        partial = getattr(error, 'evidence', None)
        assert partial and partial['status'] == 'PARTIAL'
        negatives.append({'name':'paid_partial_order', 'rejected':True, 'failed_replay_evidence':partial})
    else:
        raise AssertionError('PARTIAL accepted')
    old_history = agg.history
    agg.history = (1,)+old_history[1:]
    try:
        agg.gamma_with_address(depth, target, cert)
    except ValueError as error:
        negatives.append({'name':'changed_history', 'rejected':True, 'message':str(error)})
    else:
        raise AssertionError('changed history accepted')
    finally:
        agg.history = old_history
    assert sources() == before
    payload = {'schema':'PAID_PERIOD_AND_COUNTED_SUFFIX_BOUNDED_CHECK_V1',
        'status':'AUTHOR_ACTUAL_NATIVE_BOUNDED_SHARED_CONTEXT_NOT_ADMITTED',
        'source_sha256':before, 'source_unchanged_during_run':True,
        'startup_guard':guard, 'vendor':vendor, 'bank_source':bank_source,
        'cases':cases, 'address_certificates':addresses, 'alias_evidence':alias_records,
        'aggregation_evidence':evidence, 'negative_controls':negatives,
        'programs':[{'N':p.N,'a':p.a,'t':p.t,'dim':p.dim,'full_dim':p.full_dim,
            'phase_bindings':p.phase_bindings,'codec_binding':p.codec_binding,'h4_binding':p.h4_binding,
            'modular_powers':p.modular_powers,'program_table_instances':p.lazy_factory.export_certificate(),
            'program_permutation_verifications':p.lazy_permutation_verifications} for p in programs],
        'actual_native_core_calls':len(CALLS)-first, 'native_core_call_receipts':CALLS[first:],
        'elapsed_seconds':perf_counter()-started,
        'scope':'Paid discovered orders and recovered addresses; conditional leading-zero suffix count; full signed actual matrices; all bit/setup/replay costs retained; no general dequantization or factoring improvement claimed'}
    raw = packed(payload)
    path = ROOT/'PAID_AGGREGATION_RESULTS.json.gz'
    path.write_bytes(gzip.compress(raw, compresslevel=9, mtime=0))
    assert gzip.decompress(path.read_bytes()) == raw
    summary = {k:v for k,v in payload.items() if k in ('schema','status','source_sha256','source_unchanged_during_run',
        'actual_native_core_calls','elapsed_seconds','scope')}
    summary.update(payload_sha256=hashlib.sha256(raw).hexdigest(), payload_bytes=len(raw),
        gzip_sha256=hashlib.sha256(path.read_bytes()).hexdigest(), gzip_bytes=path.stat().st_size,
        case_count=len(cases), negative_controls_rejected=len(negatives),
        cases=[{k:v for k,v in c.items() if k not in ('matrix','address_cost')} for c in cases])
    (ROOT/'PAID_AGGREGATION_SUMMARY.json').write_bytes(packed(summary))
    print(json.dumps(summary), flush=True)


if __name__ == '__main__':
    main()
