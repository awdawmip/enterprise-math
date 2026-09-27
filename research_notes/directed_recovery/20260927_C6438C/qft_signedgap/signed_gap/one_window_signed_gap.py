"""One window plus one interval count for the one-negative-bit signed gap."""
from copy import deepcopy
from pathlib import Path

from signed_gap import (TypedFloorMoments, FLOOR_DIR, FLOOR_PIN, PROOF_PIN,
                        sha, require, strict_json, validate_inputs,
                        typed_two_power, semantic_certificate)

ROOT = Path(__file__).resolve().parent
BASELINE_PIN = '86ea28956fa7ac9c41fb38a8c63f4ba00b0377f3264b5a525c46c5335faff90a'
SCHEMA = 'BRC_ONE_WINDOW_SIGNED_GAP_V1'
IDENTITY = 'K = 4*J_zero - total_unsigned_interval_pairs'


class OneWindowSignedGapObserver:
    def __init__(self):
        require(sha(ROOT/'signed_gap.py') == BASELINE_PIN, 'frozen baseline helper changed')
        self.runner = TypedFloorMoments()
        self.requests = []
        self._source = sha(__file__)

    def _check(self):
        require(sha(__file__) == self._source, 'one-window source changed')
        require(sha(ROOT/'signed_gap.py') == BASELINE_PIN, 'frozen baseline helper changed')
        require(sha(FLOOR_DIR/'typed_floor_moments.py') == FLOOR_PIN, 'frozen floor source changed')
        self.runner._check()

    def one_negative(self, g, k, R, r, *, stride=1):
        validate_inputs(g, k, R, r, stride)
        self._check()
        runner = self.runner
        start = len(runner.signed_operations)
        U = typed_two_power(runner, k)
        H = typed_two_power(runner, g-k-1)
        L = runner.mul(runner.mul(2, U), H)
        scale_stop = len(runner.signed_operations)
        query_index = len(runner.weight_queries)
        Jzero = runner.window_weight(H, U, 2, R, r, 0)
        interval_start = len(runner.signed_operations)
        total = runner.interval_count(L, R, r)
        require(total >= 0, 'unsigned interval pair count became negative')
        outer_start = len(runner.signed_operations)
        four_Jzero = runner.mul(4, Jzero)
        value = runner.sub(four_Jzero, total)
        record = {
            'inputs': {'g': g, 'k': k, 'R': R, 'r': r, 'stride': stride},
            'H': H, 'U': U, 'L': L, 'P': 2,
            'weights': {'J_zero': Jzero, 'total_unsigned': total},
            'four_J_zero': four_Jzero, 'value': value,
            'raw_denominator_exponent': 2*g, 'identity': IDENTITY,
            'signed_operations_start': start, 'scale_operations_stop': scale_stop,
            'window_query_index': query_index, 'interval_operations_start': interval_start,
            'outer_operations_start': outer_start,
            'signed_operations_stop': len(runner.signed_operations),
            'negative_values_are_valid': True}
        self.requests.append(record)
        return deepcopy(record)

    def export_certificate(self):
        self._check()
        return deepcopy({'schema': SCHEMA, 'source_sha256': self._source,
            'baseline_helper_source_sha256': BASELINE_PIN,
            'floor_moment_source_sha256': FLOOR_PIN, 'signed_gap_proof_sha256': PROOF_PIN,
            'identity': IDENTITY, 'requests': self.requests,
            'actual_integer_evidence': self.runner.evidence(),
            'scope': 'one window plus interval integer observer; stride one; no order discovery or full Gram integration',
            'host_wiring': 'public loop indices, validation, sign encoding, source hashes and resource metadata',
            'admission': 'AUTHOR_EXECUTED_SHARED_CONTEXT_NOT_ADMITTED'})

    def incomplete_snapshot(self):
        runner = self.runner
        return deepcopy({'schema': 'INCOMPLETE_'+SCHEMA, 'source_sha256': self._source,
            'requests': self.requests, 'actual_integer_evidence': {
                'arithmetic_operations': runner.arithmetic.operations,
                'arithmetic_stats': runner.arithmetic.stats,
                'signed_operations': runner.signed_operations,
                'moment_nodes': runner.nodes, 'window_weight_queries': runner.weight_queries,
                'stats': runner.stats}, 'complete_certificate': False})


def verify_one_window_certificate(certificate, *, replay_capture=None):
    require(replay_capture is None or type(replay_capture) is list, 'replay capture must be a list or None')
    semantic_certificate(certificate)
    require(type(certificate) is dict and certificate.get('schema') == SCHEMA, 'wrong one-window schema')
    require(certificate.get('source_sha256') == sha(__file__), 'one-window source pin mismatch')
    require(certificate.get('baseline_helper_source_sha256') == BASELINE_PIN, 'baseline helper pin mismatch')
    require(certificate.get('floor_moment_source_sha256') == FLOOR_PIN, 'floor source pin mismatch')
    requests = certificate.get('requests')
    require(type(requests) is list, 'request list required')
    observer = OneWindowSignedGapObserver()
    try:
        for record in requests:
            require(type(record) is dict and type(record.get('inputs')) is dict, 'malformed request')
            inputs = record['inputs']
            require(set(inputs) == {'g', 'k', 'R', 'r', 'stride'}, 'unexpected input fields')
            observer.one_negative(inputs['g'], inputs['k'], inputs['R'], inputs['r'], stride=inputs['stride'])
    except BaseException:
        if replay_capture is not None and observer.runner.arithmetic.operations:
            replay_capture.append(observer.incomplete_snapshot())
        raise
    replay = observer.export_certificate()
    if replay_capture is not None:
        replay_capture.append(deepcopy(replay))
    require(semantic_certificate(certificate) == semantic_certificate(replay), 'one-window certificate does not replay')
    return {'verified': True, 'requests_replayed': len(requests),
            'replay_arithmetic_stats': deepcopy(observer.runner.arithmetic.stats),
            'replay_certificate': replay,
            'excluded_runtime_field': 'actual_integer_evidence.arithmetic_stats.native_kernel_calls_delta'}
