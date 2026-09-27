"""Source-pinned structural routing of actual typed signed-gap observers.

Endpoint first; interior typed divisibility zero; otherwise frozen direct.
This is a scalar integer observer, not a quantum or full Gram propagator.
"""
from copy import deepcopy
from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parent
STAGES = ROOT.parents[1]
ENDPOINT_DIR = STAGES/'sep27-qft-gap-shortcuts/endpoint_gap'
DIRECT_DIR = STAGES/'sep27-qft-gap-direct/direct_gap'
ENDPOINT_PIN = 'c75e7e82cc0ef2413048153716f5100f3a9d1d4f50c375b7cb1690c3cfe6e036'
DIRECT_PIN = '3ab2515c1b9df35d01c9605f21d8f8fe56bd044effe489063192c0a5c56a8521'
DESIGN_PIN = '0e83c68d171313896d5c1c872d64fe5c2079bace52c6b529469198ee8ae0e2e9'
SCHEMA = 'BRC_STRUCTURAL_HYBRID_SIGNED_GAP_V1'
ZERO_IDENTITY = 'R divides U: every signed residue histogram is zero'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


if sha(ENDPOINT_DIR/'endpoint_signed_gap.py') != ENDPOINT_PIN:
    raise ValueError('frozen endpoint source changed')
if sha(DIRECT_DIR/'direct_signed_gap.py') != DIRECT_PIN:
    raise ValueError('frozen direct source changed')
sys.path.insert(0, str(ENDPOINT_DIR))
sys.path.insert(0, str(DIRECT_DIR))
from endpoint_signed_gap import EndpointSignedGapObserver
from direct_signed_gap import DirectSignedGapObserver
from signed_gap import (TypedFloorMoments, FLOOR_PIN, require, validate_inputs,
                        typed_two_power, strict_json)

DEPENDENCY_PINS = {
    'endpoint_signed_gap.py': ENDPOINT_PIN,
    'direct_signed_gap.py': DIRECT_PIN,
    'signed_gap.py': '86ea28956fa7ac9c41fb38a8c63f4ba00b0377f3264b5a525c46c5335faff90a',
    'typed_floor_moments.py': FLOOR_PIN,
    'DESIGN.md': DESIGN_PIN}


def _raw_runner_snapshot(runner):
    """Existing arrays only: unlike evidence(), this does not call source_binding."""
    return deepcopy({'arithmetic_operations': runner.arithmetic.operations,
        'arithmetic_stats': runner.arithmetic.stats,
        'signed_operations': runner.signed_operations,
        'moment_nodes': runner.nodes, 'window_weight_queries': runner.weight_queries,
        'stats': runner.stats})


def runner_evidence(certificate):
    """Three disjoint executed runners; nested request copies are not extra work."""
    return {'routing': certificate['routing_integer_evidence'],
            'endpoint': certificate['endpoint_certificate']['actual_integer_evidence'],
            'direct': certificate['direct_certificate']['actual_integer_evidence']}


def semantic_hybrid_certificate(certificate):
    strict_json(certificate)
    require(type(certificate) is dict, 'hybrid certificate object required')
    normalized = deepcopy(certificate)
    try:
        evidence = runner_evidence(normalized)
        for item in evidence.values():
            stats = item['arithmetic_stats']
            count = stats['native_kernel_calls_delta']
            require(type(count) is int and count >= 0, 'invalid primitive cache call metric')
            stats['native_kernel_calls_delta'] = 0
    except (KeyError, TypeError) as error:
        raise ValueError('three complete runner evidence blocks required') from error
    return strict_json(normalized)


class HybridSignedGapObserver:
    def __init__(self):
        self.routing = TypedFloorMoments()
        self.endpoint = EndpointSignedGapObserver()
        self.direct = DirectSignedGapObserver()
        self.requests = []
        self._source = sha(__file__)

    def _check(self):
        require(sha(__file__) == self._source, 'hybrid source changed')
        require(sha(ROOT.parent/'DESIGN.md') == DESIGN_PIN, 'hybrid design changed')
        require(sha(ENDPOINT_DIR/'endpoint_signed_gap.py') == ENDPOINT_PIN,
                'frozen endpoint source changed')
        require(sha(DIRECT_DIR/'direct_signed_gap.py') == DIRECT_PIN,
                'frozen direct source changed')
        self.routing._check()
        self.endpoint._check()
        self.direct._check()

    def one_negative(self, g, k, R, r, *, stride=1):
        validate_inputs(g, k, R, r, stride)
        self._check()
        runner = self.routing
        start = len(runner.signed_operations)
        record = {'inputs': {'g': g, 'k': k, 'R': R, 'r': r, 'stride': stride},
            'routing_operations_start': start, 'raw_denominator_exponent': 2*g,
            'negative_values_are_valid': True}
        # This ordering intentionally avoids routing arithmetic at the endpoints.
        if k == g-1 or k == 0:
            nested_index = len(self.endpoint.requests)
            nested = self.endpoint.one_negative(g, k, R, r, stride=stride)
            value = nested['value']
            require(nested['branch'] != 'interior_one_window', 'endpoint dispatch invariant')
            record.update(branch='endpoint', nested_kind='endpoint',
                nested_request_index=nested_index, nested_request=nested,
                endpoint_branch=nested['branch'], divisibility=None, zero_proof=None)
        else:
            U = typed_two_power(runner, k)
            scale_stop = len(runner.signed_operations)
            division_index = len(runner.signed_operations)
            quotient, remainder = runner.floor_div(U, R)
            divisibility = {'U': U, 'R': R, 'quotient': quotient, 'remainder': remainder,
                'scale_operations_start': start, 'scale_operations_stop': scale_stop,
                'division_signed_operation_index': division_index}
            if remainder == 0:
                zero_index = len(runner.signed_operations)
                value = runner.sub(U, U)
                require(value == 0, 'typed identical subtraction did not give zero')
                record.update(branch='interior_divisible_zero', nested_kind=None,
                    nested_request_index=None, nested_request=None,
                    endpoint_branch=None, divisibility=divisibility,
                    zero_proof={'identity': ZERO_IDENTITY,
                        'division_signed_operation_index': division_index,
                        'zero_signed_operation_index': zero_index, 'value': value})
            else:
                nested_index = len(self.direct.requests)
                nested = self.direct.one_negative(g, k, R, r, stride=stride)
                value = nested['value']
                record.update(branch='interior_direct', nested_kind='direct',
                    nested_request_index=nested_index, nested_request=nested,
                    endpoint_branch=None, divisibility=divisibility, zero_proof=None)
        record.update(value=value, routing_operations_stop=len(runner.signed_operations))
        self.requests.append(record)
        return deepcopy(record)

    def export_certificate(self):
        self._check()
        return deepcopy({'schema': SCHEMA, 'source_sha256': self._source,
            'dependency_sha256': DEPENDENCY_PINS, 'requests': self.requests,
            'routing_integer_evidence': self.routing.evidence(),
            'endpoint_certificate': self.endpoint.export_certificate(),
            'direct_certificate': self.direct.export_certificate(),
            'scope': 'structural stride-one single-negative-bit scalar observer; no order or full Gram propagation',
            'routing_rule': 'endpoint first; interior typed R-divides-U zero; otherwise frozen direct',
            'cost_rule': 'sum three disjoint runner streams once; global primitive CALLS separately',
            'host_wiring': 'strict inputs, public bit-index tests, observed remainder zero test, record routing, metadata',
            'admission': 'AUTHOR_SHARED_CONTEXT_NOT_ADMITTED'})

    def incomplete_snapshot(self):
        # No source checks or evidence() calls, hence no new arithmetic observation.
        return deepcopy({'schema': 'INCOMPLETE_'+SCHEMA, 'source_sha256': self._source,
            'requests': self.requests, 'routing_integer_evidence': _raw_runner_snapshot(self.routing),
            'endpoint_certificate': self.endpoint.incomplete_snapshot(),
            'direct_certificate': self.direct.incomplete_snapshot(),
            'complete_certificate': False})


def verify_hybrid_certificate(certificate, *, replay_capture=None):
    require(replay_capture is None or type(replay_capture) is list,
            'replay capture must be a list or None')
    expected_semantic = semantic_hybrid_certificate(certificate)
    require(certificate.get('schema') == SCHEMA, 'wrong hybrid schema')
    require(certificate.get('source_sha256') == sha(__file__), 'hybrid source pin mismatch')
    require(strict_json(certificate.get('dependency_sha256')) == strict_json(DEPENDENCY_PINS),
            'hybrid dependency pin mismatch')
    requests = certificate.get('requests')
    require(type(requests) is list, 'hybrid request list required')
    # Early input validation performs no arithmetic, even if a later input is bad.
    for request in requests:
        require(type(request) is dict and type(request.get('inputs')) is dict, 'malformed request')
        inputs = request['inputs']
        require(set(inputs) == {'g', 'k', 'R', 'r', 'stride'}, 'unexpected input fields')
        validate_inputs(inputs['g'], inputs['k'], inputs['R'], inputs['r'], inputs['stride'])
    observer = HybridSignedGapObserver()
    try:
        for request in requests:
            inputs = request['inputs']
            observer.one_negative(inputs['g'], inputs['k'], inputs['R'], inputs['r'], stride=inputs['stride'])
        replay = observer.export_certificate()
    except BaseException:
        if replay_capture is not None:
            replay_capture.append(observer.incomplete_snapshot())
        raise
    if replay_capture is not None:
        replay_capture.append(deepcopy(replay))
    require(expected_semantic == semantic_hybrid_certificate(replay),
            'hybrid certificate does not strictly replay')
    return {'verified': True, 'requests_replayed': len(requests),
        'replay_arithmetic_stats': {name: deepcopy(item['arithmetic_stats'])
                                   for name, item in runner_evidence(replay).items()},
        'replay_certificate': replay,
        'excluded_runtime_fields': [
            'routing_integer_evidence.arithmetic_stats.native_kernel_calls_delta',
            'endpoint_certificate.actual_integer_evidence.arithmetic_stats.native_kernel_calls_delta',
            'direct_certificate.actual_integer_evidence.arithmetic_stats.native_kernel_calls_delta']}
