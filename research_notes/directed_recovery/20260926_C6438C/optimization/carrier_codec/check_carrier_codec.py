"""Complete small-history equality and negative controls for the exact codec."""
from __future__ import annotations
import hashlib
import gzip
import json
from fractions import Fraction as F
from pathlib import Path
import sys
from time import perf_counter

ROOT = Path(__file__).resolve().parent
PACKAGE = ROOT.parents[1]
sys.path.insert(0, str(PACKAGE / 'direct_word_integration'))
from check_direct_word_integration import load_phase, bound_sources
from carrier_codec import ExactCarrierCodec, restrict_bank, restrict_word, CompleteNativeWord
from general_streaming import GeneralStreamingProgram
from sparse_modular import sparse_modular_columns
from stage45.brc_loop_recheck import CALLS, verify_vendor
from stage79.phase_compiler import encode
from stage80.fixed_phase import norm


def expect_rejected(name, fn, log):
    try:
        fn()
    except (ValueError, TypeError) as exc:
        log.append({'name': name, 'rejected': True, 'reason': str(exc)})
    else:
        raise AssertionError('negative control accepted: ' + name)


def main():
    started = perf_counter()
    first_call = len(CALLS)
    source = bound_sources()
    kernel = verify_vendor()
    bank = {2: CompleteNativeWord((('swap', 0, 1), ('neg', 1)), 61)}
    provenance = {}
    for m in (3, 4):
        record, provenance[str(m)] = load_phase(m)
        bank[m] = CompleteNativeWord(record['word'], 61)
    codec, small, certificate = restrict_bank(bank)
    vector_checks = []
    for m in sorted(bank):
        rows = [tuple(int(i == j) for i in range(6)) for j in range(6)]
        rows += [(3, -5, 7, 11, -13, 17), (0, 0, 0, 0, 0, 0)]
        for inverse in (False, True):
            for row in rows:
                expected = tuple(bank[m].apply_numer(codec.decode(row), inverse=inverse))
                actual = codec.decode(small[m].apply_numer(row, inverse=inverse))
                assert actual == expected
        vector_checks.append({'phase': m, 'forward_inverse_rows': 2 * len(rows), 'all_match': True})
    cases = []
    for N, a in ((15, 2), (21, 2)):
        full = GeneralStreamingProgram(N, a, 4, bank, 61, column_factory=sparse_modular_columns)
        compact = GeneralStreamingProgram(N, a, 4, small, 6, column_factory=sparse_modular_columns)
        fs, fd = full.initial()
        cs, cd = compact.initial()
        assert codec.encode_state(fs) == cs and fd == cd
        pending = [((), fs, fd, cs, cd)]
        records = []
        for depth in range(4):
            nxt = []
            for history, fs, fd, cs, cd in pending:
                fchildren = full.branches(fs, fd, history)
                cchildren = compact.branches(cs, cd, history)
                for bit, ((fstate, fden), (cstate, cden)) in enumerate(zip(fchildren, cchildren)):
                    assert fden == cden
                    assert fstate == codec.decode_state(cstate)
                    assert norm(fstate, fden) == norm(cstate, cden)
                    expanded = sorted((key, tuple(map(str, row))) for key, row in fstate.items())
                    witness = json.dumps(expanded, separators=(',', ':')).encode()
                    records.append({'history': history + (bit,), 'endpoints': len(fstate),
                        'mass': str(norm(fstate, fden)),
                        'full_state_sha256': hashlib.sha256(witness).hexdigest(),
                        'nonzero_residual_seen': any(any(row[2:]) for row in cstate.values()),
                        'exact_full_decoding': True})
                    nxt.append((history + (bit,), fstate, fden, cstate, cden))
            pending = nxt
        assert sum(norm(fs, fd) for _, fs, fd, _, _ in pending) == 1
        fm, cm = full.report_metrics(), compact.report_metrics()
        assert fm['peak_endpoints'] == cm['peak_endpoints']
        assert fm['peak_scalar_slots'] * 6 == cm['peak_scalar_slots'] * 61
        cases.append({'N': N, 'a': a, 't': 4, 'prefixes_checked': len(records),
            'terminal_mass': '1', 'all_61_coordinates_equal': True,
            'full_metrics': fm, 'encoded_metrics': cm, 'records': records})
    rejected = []
    tail = [0] * 61
    tail[60] = 1
    expect_rejected('nonzero_tail', lambda: codec.encode(tail), rejected)
    expect_rejected('cross_block_native_swap', lambda: restrict_word(
        CompleteNativeWord((('swap', 0, 6),), 61), codec), rejected)
    expect_rejected('complement_not_identity', lambda: restrict_word(
        CompleteNativeWord((('neg', 60),), 61), codec), rejected)
    expect_rejected('duplicate_indices', lambda: ExactCarrierCodec(61, (0, 0)), rejected)
    expect_rejected('boolean_index', lambda: ExactCarrierCodec(61, (False, 1)), rejected)
    expect_rejected('streaming_initial_basis_reordered', lambda: restrict_bank(
        bank, indices=(1, 0, 2, 3, 4, 5)), rejected)
    expect_rejected('wrong_row_width', lambda: codec.encode((1, 0)), rejected)
    expect_rejected('noninteger_row', lambda: small[2].apply_numer((True, 0, 0, 0, 0, 0)), rejected)
    tampered = CompleteNativeWord((), 61)
    tampered.den = 2
    expect_rejected('mutated_source_denominator', lambda: restrict_word(tampered, codec), rejected)
    out = {'status': 'AUTHOR_EXECUTED_SHARED_CONTEXT_NOT_ADMITTED',
        'scope': 'lossless word-boundary encoding; same actual native words; no ideal propagation',
        'activity': 'RA-CAAAC604CB513AEA8BBC1DFC', 'kernel': kernel,
        'prior_sources': source, 'phase_provenance': provenance,
        'codec_certificate': certificate, 'vector_checks': vector_checks,
        'cases': cases, 'negative_controls': rejected,
        'actual_BRC_calls': len(CALLS) - first_call,
        'seconds': perf_counter() - started,
        'source_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in (ROOT / 'carrier_codec.py', Path(__file__))}}
    payload = (json.dumps(encode(out), ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    compressed = gzip.compress(payload, mtime=0)
    (ROOT / 'CARRIER_CODEC_RESULTS.json.gz').write_bytes(compressed)
    summary = {k: out[k] for k in ('status', 'actual_BRC_calls', 'seconds', 'source_sha256')}
    summary['cases'] = [{k: c[k] for k in ('N', 't', 'prefixes_checked', 'all_61_coordinates_equal')}
                        | {'full_peak_scalar_slots': c['full_metrics']['peak_scalar_slots'],
                           'encoded_peak_scalar_slots': c['encoded_metrics']['peak_scalar_slots'],
                           'nonzero_residual_seen': any(x['nonzero_residual_seen'] for x in c['records'])}
                        for c in cases]
    summary['negative_controls_rejected'] = len(rejected)
    summary['payload_sha256'] = hashlib.sha256(payload).hexdigest()
    summary['gzip_sha256'] = hashlib.sha256(compressed).hexdigest()
    (ROOT / 'CARRIER_CODEC_SUMMARY.json').write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(summary))


if __name__ == '__main__':
    main()
