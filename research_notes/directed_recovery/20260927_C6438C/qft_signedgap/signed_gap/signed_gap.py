"""One-negative-bit signed gap counts, from three actual typed floor sums.

Only physical stride one is supported. This is an integer observer, not a
modular-order certificate, state propagator, or full Gram implementation.
"""
from copy import deepcopy
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
FLOOR_DIR = ROOT.parents[1] / 'sep27-qft-adaptive/nonzero_structure'
FLOOR_PIN = '633502c9b484e60e5dc5fcf6edd0420f12d52c33c43e88851b9e1e6465ea94a2'
PROOF_PIN = '1a84d09ed1fecdf7a42de9c1b1e48da881c820e544214011703c79a688938776'
SCHEMA = 'BRC_ONE_NEGATIVE_SIGNED_GAP_V1'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


require(sha(FLOOR_DIR / 'typed_floor_moments.py') == FLOOR_PIN,
        'frozen typed floor-moment source does not match')
sys.path.insert(0, str(FLOOR_DIR))
from typed_floor_moments import TypedFloorMoments


def strict_json(value):
    """Preserve integer/bool distinctions; reject non-JSON or mixed-key input."""
    def check(item):
        if type(item) in (str, int, bool) or item is None:
            return
        if type(item) in (list, tuple):
            for child in item:
                check(child)
            return
        if type(item) is dict:
            require(all(type(key) is str for key in item), 'JSON object keys must be strings')
            for child in item.values():
                check(child)
            return
        raise ValueError('certificate contains an unsupported JSON value')
    check(value)
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True)


def validate_inputs(g, k, R, r, stride):
    require(all(type(x) is int for x in (g, k, R, r, stride)), 'strict integer inputs required')
    require(g >= 1 and 0 <= k < g, 'g >= 1 and 0 <= negative bit k < g required')
    require(R >= 1 and 0 <= r < R, 'positive counting modulus and canonical residue required')
    require(stride == 1, 'only physical stride one is supported; no stride certificate')


def typed_two_power(runner, exponent):
    """Exponent is a public finite loop bound; each magnitude doubling is typed."""
    value = 1
    for _ in range(exponent):
        value = runner.add(value, value)
    return value


class SignedGapObserver:
    def __init__(self):
        self.runner = TypedFloorMoments()
        self.requests = []
        self._source = sha(__file__)

    def _check(self):
        require(sha(__file__) == self._source, 'signed-gap source changed')
        require(sha(FLOOR_DIR / 'typed_floor_moments.py') == FLOOR_PIN,
                'frozen floor-moment source changed')
        self.runner._check()

    def one_negative(self, g, k, R, r, *, stride=1):
        validate_inputs(g, k, R, r, stride)
        self._check()
        runner = self.runner
        start = len(runner.signed_operations)
        U = typed_two_power(runner, k)
        H = typed_two_power(runner, g-k-1)
        scale_stop = len(runner.signed_operations)
        query_start = len(runner.weight_queries)
        J0 = runner.window_weight(H, U, 2, R, r, 0)
        Jplus = runner.window_weight(H, U, 2, R, r, 1)
        Jminus = runner.window_weight(H, U, 2, R, r, -1)
        outer_start = len(runner.signed_operations)
        doubled = runner.mul(2, J0)
        minus_plus = runner.sub(doubled, Jplus)
        value = runner.sub(minus_plus, Jminus)
        receipt = {
            'inputs': {'g': g, 'k': k, 'R': R, 'r': r, 'stride': stride},
            'H': H, 'U': U, 'P': 2,
            'weights': {'J_zero': J0, 'J_plus': Jplus, 'J_minus': Jminus},
            'outer_values': {'twice_J_zero': doubled, 'minus_J_plus': minus_plus},
            'value': value, 'raw_denominator_exponent': 2*g,
            'signed_operations_start': start, 'scale_operations_stop': scale_stop,
            'outer_operations_start': outer_start,
            'signed_operations_stop': len(runner.signed_operations),
            'weight_query_indices': list(range(query_start, len(runner.weight_queries))),
            'negative_values_are_valid': True}
        self.requests.append(receipt)
        return deepcopy(receipt)

    def export_certificate(self):
        self._check()
        return deepcopy({
            'schema': SCHEMA, 'source_sha256': self._source,
            'floor_moment_source_sha256': FLOOR_PIN, 'symbolic_proof_sha256': PROOF_PIN,
            'scope': 'integer signed pair counts; stride one; no certified modular order or full Gram integration',
            'requests': self.requests, 'actual_integer_evidence': self.runner.evidence(),
            'host_wiring': 'input validation, public finite indices, sign encoding, record routing and resource metadata',
            'admission': 'AUTHOR_EXECUTED_SHARED_CONTEXT_NOT_ADMITTED'})

    def incomplete_snapshot(self):
        """Preserve available work on interruption without invoking more arithmetic."""
        runner = self.runner
        return deepcopy({'schema': 'INCOMPLETE_'+SCHEMA, 'source_sha256': self._source,
            'requests': self.requests, 'actual_integer_evidence': {
                'arithmetic_operations': runner.arithmetic.operations,
                'arithmetic_stats': runner.arithmetic.stats,
                'signed_operations': runner.signed_operations,
                'moment_nodes': runner.nodes, 'window_weight_queries': runner.weight_queries,
                'stats': runner.stats}, 'complete_certificate': False})


def semantic_certificate(certificate):
    """One nondeterministic runtime metric is excluded, no mathematical field."""
    strict_json(certificate)
    item = deepcopy(certificate)
    try:
        stats = item['actual_integer_evidence']['arithmetic_stats']
        count = stats['native_kernel_calls_delta']
        require(type(count) is int and count >= 0, 'invalid native call count')
        stats['native_kernel_calls_delta'] = 0
    except (KeyError, TypeError) as error:
        raise ValueError('missing typed arithmetic evidence') from error
    return strict_json(item)


def verify_certificate(certificate, *, replay_capture=None):
    """Re-execute all signed counts and complete integer traces, in request order."""
    require(replay_capture is None or type(replay_capture) is list,
            'replay capture must be a list or None')
    semantic_certificate(certificate)
    require(type(certificate) is dict and certificate.get('schema') == SCHEMA,
            'unexpected signed-gap certificate schema')
    require(certificate.get('source_sha256') == sha(__file__), 'signed-gap source pin mismatch')
    require(certificate.get('floor_moment_source_sha256') == FLOOR_PIN,
            'floor-moment source pin mismatch')
    requests = certificate.get('requests')
    require(type(requests) is list, 'certificate requests must be a list')
    observer = SignedGapObserver()
    try:
        for record in requests:
            require(type(record) is dict and type(record.get('inputs')) is dict,
                    'malformed signed-gap request')
            inputs = record['inputs']
            require(set(inputs) == {'g', 'k', 'R', 'r', 'stride'}, 'unexpected input fields')
            observer.one_negative(inputs['g'], inputs['k'], inputs['R'], inputs['r'],
                                  stride=inputs['stride'])
    except BaseException:
        if replay_capture is not None and observer.runner.arithmetic.operations:
            replay_capture.append(observer.incomplete_snapshot())
        raise
    replay = observer.export_certificate()
    if replay_capture is not None:
        replay_capture.append(deepcopy(replay))
    require(semantic_certificate(certificate) == semantic_certificate(replay),
            'complete signed-gap certificate does not replay')
    return {'verified': True, 'requests_replayed': len(requests),
            'source_sha256': observer._source,
            'replay_arithmetic_stats': deepcopy(observer.runner.arithmetic.stats),
            'replay_certificate': replay,
            'excluded_runtime_field': 'actual_integer_evidence.arithmetic_stats.native_kernel_calls_delta'}
