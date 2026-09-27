"""Typed endpoint identities with an unchanged one-window interior fallback.

This is a stride-one integer counting observer, not a Gram propagator.
"""
from copy import deepcopy
from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parent
FROZEN = ROOT.parents[1] / 'sep27-qft-signedgap/signed_gap'
ONE_WINDOW_PIN = 'c15e80d580fc8aa52821cb8b0526ada4cd31933cd089bdb1fa1199d1de1ff8b7'
BASELINE_PIN = '86ea28956fa7ac9c41fb38a8c63f4ba00b0377f3264b5a525c46c5335faff90a'
ENDPOINT_PROOF_PIN = 'e43e061fa0e04022daeb14aa30d9956ebe5ba9365b2aaa9c569d762a29e912c0'
SCHEMA = 'BRC_ENDPOINT_SIGNED_GAP_V1'
IDENTITIES = {
    'highest_bit': 'K = 4*T(L/2,R,r) - T(L,R,r)',
    'lowest_even_modulus': 'K = (1-2*(r mod 2))*T(L,R,r)',
    'lowest_odd_modulus': 'K = 4*T(L/2,R,r_half) - T(L,R,r)',
    'interior_one_window': 'frozen K = 4*J_zero - T(L,R,r)'}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


if sha(FROZEN/'one_window_signed_gap.py') != ONE_WINDOW_PIN:
    raise ValueError('frozen one-window source changed')
if sha(FROZEN/'signed_gap.py') != BASELINE_PIN:
    raise ValueError('frozen baseline source changed')
sys.path.insert(0, str(FROZEN))
from one_window_signed_gap import OneWindowSignedGapObserver
from signed_gap import (require, validate_inputs, typed_two_power,
                        semantic_certificate, FLOOR_DIR, FLOOR_PIN, PROOF_PIN)


class EndpointSignedGapObserver:
    def __init__(self):
        self.fallback = OneWindowSignedGapObserver()
        self.runner = self.fallback.runner
        self.requests = []
        self._source = sha(__file__)

    def _check(self):
        require(sha(__file__) == self._source, 'endpoint source changed')
        require(sha(FROZEN/'one_window_signed_gap.py') == ONE_WINDOW_PIN,
                'frozen one-window source changed')
        require(sha(ROOT.parent/'ENDPOINT_IDENTITIES.md') == ENDPOINT_PROOF_PIN,
                'endpoint identity proof changed')
        self.fallback._check()

    def _interval(self, length, R, r):
        start = len(self.runner.signed_operations)
        value = self.runner.interval_count(length, R, r)
        require(value >= 0, 'unsigned interval count became negative')
        return {'inputs': {'length': length, 'R': R, 'r': r}, 'value': value,
                'signed_operations_start': start,
                'signed_operations_stop': len(self.runner.signed_operations)}

    def one_negative(self, g, k, R, r, *, stride=1):
        validate_inputs(g, k, R, r, stride)
        self._check()
        runner = self.runner
        start = len(runner.signed_operations)
        window_start = len(runner.weight_queries)
        record = {'inputs': {'g': g, 'k': k, 'R': R, 'r': r, 'stride': stride},
                  'raw_denominator_exponent': 2*g,
                  'signed_operations_start': start, 'negative_values_are_valid': True}
        if k == g-1:
            branch = 'highest_bit'
            half = typed_two_power(runner, g-1)
            length = runner.add(half, half)
            scale_stop = len(runner.signed_operations)
            Jzero = self._interval(half, R, r)
            total = self._interval(length, R, r)
            outer_start = len(runner.signed_operations)
            four_Jzero = runner.mul(4, Jzero['value'])
            value = runner.sub(four_Jzero, total['value'])
            record.update(H=half, L=length, scale_operations_stop=scale_stop,
                interval_receipts=[Jzero, total], four_J_zero=four_Jzero,
                outer_operations_start=outer_start)
        elif k == 0:
            # All parity/half-residue magnitudes originate in typed divisions.
            modulus_half, modulus_parity = runner.floor_div(R, 2)
            residue_half, residue_parity = runner.floor_div(r, 2)
            half = typed_two_power(runner, g-1)
            length = runner.add(half, half)
            scale_stop = len(runner.signed_operations)
            record.update(H=half, L=length, scale_operations_stop=scale_stop,
                modulus_half=modulus_half, modulus_parity=modulus_parity,
                residue_half=residue_half, residue_parity=residue_parity)
            if modulus_parity == 0:
                branch = 'lowest_even_modulus'
                total = self._interval(length, R, r)
                outer_start = len(runner.signed_operations)
                parity_twice = runner.mul(2, residue_parity)
                sign = runner.sub(1, parity_twice)
                value = runner.mul(sign, total['value'])
                record.update(interval_receipts=[total], parity_twice=parity_twice,
                              sign=sign, outer_operations_start=outer_start)
            else:
                branch = 'lowest_odd_modulus'
                half_start = len(runner.signed_operations)
                if residue_parity:
                    half_numerator = runner.add(r, R)
                    r_half = runner.exact_div(half_numerator, 2)
                else:
                    half_numerator = r
                    r_half = residue_half
                half_stop = len(runner.signed_operations)
                require(0 <= r_half < R, 'half residue not canonical')
                Jzero = self._interval(half, R, r_half)
                total = self._interval(length, R, r)
                outer_start = len(runner.signed_operations)
                four_Jzero = runner.mul(4, Jzero['value'])
                value = runner.sub(four_Jzero, total['value'])
                record.update(half_residue={'numerator': half_numerator, 'value': r_half,
                    'signed_operations_start': half_start, 'signed_operations_stop': half_stop,
                    'even_residue_reuses_recorded_division': residue_parity == 0},
                    interval_receipts=[Jzero, total], four_J_zero=four_Jzero,
                    outer_operations_start=outer_start)
        else:
            branch = 'interior_one_window'
            fallback_index = len(self.fallback.requests)
            inherited = self.fallback.one_negative(g, k, R, r, stride=stride)
            value = inherited['value']
            record.update(frozen_one_window_request=inherited,
                          fallback_request_index=fallback_index)
        record.update(branch=branch, identity=IDENTITIES[branch], value=value,
            signed_operations_stop=len(runner.signed_operations),
            window_query_indices=list(range(window_start, len(runner.weight_queries))))
        self.requests.append(record)
        return deepcopy(record)

    def export_certificate(self):
        self._check()
        return deepcopy({'schema': SCHEMA, 'source_sha256': self._source,
            'one_window_source_sha256': ONE_WINDOW_PIN, 'baseline_helper_source_sha256': BASELINE_PIN,
            'floor_moment_source_sha256': FLOOR_PIN, 'signed_gap_proof_sha256': PROOF_PIN,
            'endpoint_proof_sha256': ENDPOINT_PROOF_PIN, 'identities': IDENTITIES,
            'requests': self.requests, 'actual_integer_evidence': self.runner.evidence(),
            'scope': 'endpoint signed integer counts with frozen interior fallback; stride one; no full Gram integration',
            'host_wiring': 'validated public index/branch selection; signs encoded by existing typed runner; hashes and resource metadata',
            'admission': 'AUTHOR_EXECUTED_SHARED_CONTEXT_NOT_ADMITTED'})

    def incomplete_snapshot(self):
        inherited = self.fallback.incomplete_snapshot()
        return deepcopy({'schema': 'INCOMPLETE_'+SCHEMA, 'source_sha256': self._source,
                         'requests': self.requests,
                         'actual_integer_evidence': inherited['actual_integer_evidence'],
                         'complete_certificate': False})


def verify_endpoint_certificate(certificate, *, replay_capture=None):
    require(replay_capture is None or type(replay_capture) is list, 'replay capture must be a list or None')
    semantic_certificate(certificate)
    require(type(certificate) is dict and certificate.get('schema') == SCHEMA, 'wrong endpoint schema')
    require(certificate.get('source_sha256') == sha(__file__), 'endpoint source pin mismatch')
    require(certificate.get('one_window_source_sha256') == ONE_WINDOW_PIN, 'one-window source pin mismatch')
    require(certificate.get('baseline_helper_source_sha256') == BASELINE_PIN, 'baseline source pin mismatch')
    require(certificate.get('floor_moment_source_sha256') == FLOOR_PIN, 'floor source pin mismatch')
    require(certificate.get('endpoint_proof_sha256') == ENDPOINT_PROOF_PIN, 'endpoint proof pin mismatch')
    requests = certificate.get('requests')
    require(type(requests) is list, 'request list required')
    observer = EndpointSignedGapObserver()
    try:
        for record in requests:
            require(type(record) is dict and type(record.get('inputs')) is dict, 'malformed request')
            inputs = record['inputs']
            require(set(inputs) == {'g', 'k', 'R', 'r', 'stride'}, 'unexpected input fields')
            observer.one_negative(inputs['g'], inputs['k'], inputs['R'], inputs['r'], stride=inputs['stride'])
        replay = observer.export_certificate()
    except BaseException:
        if replay_capture is not None and observer.runner.arithmetic.operations:
            replay_capture.append(observer.incomplete_snapshot())
        raise
    if replay_capture is not None:
        replay_capture.append(deepcopy(replay))
    require(semantic_certificate(certificate) == semantic_certificate(replay), 'endpoint certificate does not replay')
    return {'verified': True, 'requests_replayed': len(requests),
            'replay_arithmetic_stats': deepcopy(observer.runner.arithmetic.stats),
            'replay_certificate': replay,
            'excluded_runtime_field': 'actual_integer_evidence.arithmetic_stats.native_kernel_calls_delta'}
