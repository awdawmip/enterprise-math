"""Pure direct difference formula using actual typed degree-three moments.

No endpoint dispatch: both difference orientations are always retained.
"""
from copy import deepcopy
from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parent
FROZEN = ROOT.parents[1]/'sep27-qft-signedgap/signed_gap'
BASELINE_PIN = '86ea28956fa7ac9c41fb38a8c63f4ba00b0377f3264b5a525c46c5335faff90a'
DIRECT_PROOF_PIN = 'c0c3765fce7d07f383f1ebfcb514dd8483485944bfeb202d024dd21e69205cbf'
SCHEMA = 'BRC_DIRECT_DIFFERENCE_SIGNED_GAP_V1'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


if sha(FROZEN/'signed_gap.py') != BASELINE_PIN:
    raise ValueError('frozen signed-gap helper changed')
sys.path.insert(0, str(FROZEN))
from signed_gap import (TypedFloorMoments, FLOOR_DIR, FLOOR_PIN, PROOF_PIN, require,
                        validate_inputs, typed_two_power, semantic_certificate)


class DirectSignedGapObserver:
    def __init__(self):
        self.runner = TypedFloorMoments()
        self.requests = []
        self._source = sha(__file__)

    def _check(self):
        require(sha(__file__) == self._source, 'direct source changed')
        require(sha(FROZEN/'signed_gap.py') == BASELINE_PIN, 'frozen helper changed')
        require(sha(FLOOR_DIR/'typed_floor_moments.py') == FLOOR_PIN, 'frozen floor source changed')
        require(sha(ROOT.parent/'DIFFERENCE_AUTOCORRELATION.md') == DIRECT_PROOF_PIN,
                'direct identity proof changed')
        self.runner._check()

    def _computed(self, operation):
        start = len(self.runner.signed_operations)
        value = operation()
        return {'value': value, 'signed_operations_start': start,
                'signed_operations_stop': len(self.runner.signed_operations)}

    def _exact_division(self, numerator, denominator):
        start = len(self.runner.signed_operations)
        value = self.runner.exact_div(numerator, denominator)
        stop = len(self.runner.signed_operations)
        require(stop == start+1, 'unexpected exact division record shape')
        operation = self.runner.signed_operations[start]
        require(operation['operation'] == 'signed_euclidean_division'
                and operation['result'] == (value, 0), 'division is not recorded exact')
        return {'numerator': numerator, 'denominator': denominator, 'value': value,
                'remainder': 0, 'signed_operation_index': start,
                'signed_operations_start': start, 'signed_operations_stop': stop}

    def _table(self, n, P, R, offset):
        runner = self.runner
        signed_start, node_start = len(runner.signed_operations), len(runner.nodes)
        stats_before = deepcopy(runner.stats)
        table = runner.moments(n, P, R, offset)
        record = {'inputs': {'n': n, 'm': P, 'a': R, 'b': offset},
            'outputs': {f'{p},{e}': value for (p, e), value in table.items()},
            'signed_operations_start': signed_start,
            'signed_operations_stop': len(runner.signed_operations),
            'new_moment_node_indices': list(range(node_start, len(runner.nodes))),
            'stats_before': stats_before, 'stats_after': deepcopy(runner.stats)}
        return table, record

    def _coefficients(self, H, P):
        runner = self.runner
        four_H = self._computed(lambda: runner.mul(4, H))
        eight_H = self._computed(lambda: runner.mul(8, H))
        records = {
            'n': self._computed(lambda: runner.mul(H, P)),
            'q': self._computed(lambda: runner.mul(runner.sub(four_H['value'], 2), P)),
            'dq': self._computed(lambda: runner.add(4, 0)),
            'q2': self._computed(lambda: runner.mul(-4, P)),
            'd': self._computed(lambda: runner.sub(1, four_H['value'])),
            'ddelta': self._computed(lambda: runner.sub(eight_H['value'], 4)),
            'dqdelta': self._computed(lambda: runner.add(-8, 0)),
            'q2delta': self._computed(lambda: runner.mul(8, P)),
            'qdelta': self._computed(lambda: runner.mul(runner.sub(8, eight_H['value']), P)),
            'delta': self._computed(lambda: runner.mul(runner.sub(2, four_H['value']), P))}
        return records, {'four_H': four_H, 'eight_H': eight_H}

    def _progression(self, head, orientation, L, U, P, R, coefficients):
        runner = self.runner
        start = len(runner.signed_operations)
        b = head['value']
        z = self._computed(lambda: runner.sub(runner.sub(L, 1), b))
        record = {'orientation': orientation, 'multiplicity': 1, 'head': head,
            'step': R, 'last_minus_head': z, 'signed_operations_start': start}
        if z['value'] < 0:
            zero = self._computed(lambda: runner.add(0, 0))
            record.update(empty=True, n=0, table_calls=[], zero=zero, value=zero['value'],
                          signed_operations_stop=len(runner.signed_operations))
            return record
        length_start = len(runner.signed_operations)
        quotient, remainder = runner.floor_div(z['value'], R)
        n = runner.add(quotient, 1)
        record.update(empty=False, n=n, length_receipt={'quotient': quotient,
            'remainder': remainder, 'value': n, 'signed_operations_start': length_start,
            'signed_operations_stop': len(runner.signed_operations)})
        M, M_record = self._table(n, P, R, b)
        offset_plus = self._computed(lambda: runner.add(b, U))
        Mp, Mp_record = self._table(n, P, R, offset_plus['value'])
        deltas = {f'{p},{e}': self._computed(lambda p=p, e=e: runner.sub(Mp[p, e], M[p, e]))
                  for p, e in ((0, 1), (1, 1), (0, 2), (1, 2), (0, 3))}
        D01, D11, D02, D12, D03 = (deltas[key]['value']
                                   for key in ('0,1', '1,1', '0,2', '1,2', '0,3'))
        qdelta_numerator = self._computed(lambda: runner.sub(D02, D01))
        qdelta = self._exact_division(qdelta_numerator['value'], 2)
        jqdelta_numerator = self._computed(lambda: runner.sub(D12, D11))
        jqdelta = self._exact_division(jqdelta_numerator['value'], 2)
        q2delta_numerator = self._computed(lambda: runner.total(
            (runner.mul(2, D03), runner.mul(-3, D02), D01)))
        q2delta = self._exact_division(q2delta_numerator['value'], 6)
        weighted = {
            'd': self._computed(lambda: runner.add(runner.mul(b, n), runner.mul(R, M[1, 0]))),
            'dq': self._computed(lambda: runner.add(runner.mul(b, M[0, 1]), runner.mul(R, M[1, 1]))),
            'ddelta': self._computed(lambda: runner.add(runner.mul(b, D01), runner.mul(R, D11))),
            'dqdelta': self._computed(lambda: runner.add(runner.mul(b, qdelta['value']),
                                                       runner.mul(R, jqdelta['value'])))}
        factors = {'n': n, 'q': M[0, 1], 'dq': weighted['dq']['value'], 'q2': M[0, 2],
            'd': weighted['d']['value'], 'ddelta': weighted['ddelta']['value'],
            'dqdelta': weighted['dqdelta']['value'], 'q2delta': q2delta['value'],
            'qdelta': qdelta['value'], 'delta': D01}
        terms = {name: self._computed(lambda name=name: runner.mul(coefficients[name]['value'], factors[name]))
                 for name in ('n', 'q', 'dq', 'q2', 'd', 'ddelta', 'dqdelta', 'q2delta', 'qdelta', 'delta')}
        result = self._computed(lambda: runner.total(term['value'] for term in terms.values()))
        record.update(table_calls=[M_record, Mp_record], shifted_offset=offset_plus,
            deltas=deltas,
            division_numerators={'qdelta': qdelta_numerator, 'jqdelta': jqdelta_numerator,
                                 'q2delta': q2delta_numerator},
            exact_divisions={'qdelta': qdelta, 'jqdelta': jqdelta, 'q2delta': q2delta},
            weighted_sums=weighted, term_factors=factors, terms=terms, sumA=result,
            value=result['value'], signed_operations_stop=len(runner.signed_operations))
        return record

    def one_negative(self, g, k, R, r, *, stride=1):
        validate_inputs(g, k, R, r, stride)
        self._check()
        runner = self.runner
        start = len(runner.signed_operations)
        U = typed_two_power(runner, k)
        H = typed_two_power(runner, g-k-1)
        P = runner.add(U, U)
        L = runner.mul(H, P)
        scales_stop = len(runner.signed_operations)
        coefficients, coefficient_helpers = self._coefficients(H, P)
        positive_head = self._computed(lambda: runner.add(r, 0))
        positive = self._progression(positive_head, 'nonnegative_difference', L, U, P, R, coefficients)
        negative_head = self._computed(lambda: runner.sub(R, r))
        negative = self._progression(negative_head, 'negative_difference_magnitude', L, U, P, R, coefficients)
        # Equal heads at a half-modulus residue still have two orientations.
        final = self._computed(lambda: runner.add(positive['value'], negative['value']))
        record = {'inputs': {'g': g, 'k': k, 'R': R, 'r': r, 'stride': stride},
            'L': L, 'U': U, 'P': P, 'H': H, 'scales_operations_start': start,
            'scales_operations_stop': scales_stop, 'coefficients': coefficients,
            'coefficient_helpers': coefficient_helpers, 'progressions': [positive, negative],
            'final_addition': final, 'value': final['value'], 'raw_denominator_exponent': 2*g,
            'signed_operations_start': start, 'signed_operations_stop': len(runner.signed_operations),
            'negative_values_are_valid': True, 'endpoint_shortcuts_used': False}
        self.requests.append(record)
        return deepcopy(record)

    def export_certificate(self):
        self._check()
        return deepcopy({'schema': SCHEMA, 'source_sha256': self._source,
            'baseline_helper_source_sha256': BASELINE_PIN, 'floor_moment_source_sha256': FLOOR_PIN,
            'signed_gap_proof_sha256': PROOF_PIN, 'direct_proof_sha256': DIRECT_PROOF_PIN,
            'identity': 'sum direct A(d) on both oriented alias progressions',
            'requests': self.requests, 'actual_integer_evidence': self.runner.evidence(),
            'scope': 'pure direct stride-one one-negative-bit integer observer; no endpoint dispatch or full Gram integration',
            'host_wiring': 'public indices, branch/sign routing of actual outputs, source hashes and resource metadata',
            'admission': 'AUTHOR_EXECUTED_SHARED_CONTEXT_NOT_ADMITTED'})

    def incomplete_snapshot(self):
        runner = self.runner
        return deepcopy({'schema': 'INCOMPLETE_'+SCHEMA, 'source_sha256': self._source,
            'requests': self.requests, 'actual_integer_evidence': {
                'arithmetic_operations': runner.arithmetic.operations,
                'arithmetic_stats': runner.arithmetic.stats, 'signed_operations': runner.signed_operations,
                'moment_nodes': runner.nodes, 'window_weight_queries': runner.weight_queries,
                'stats': runner.stats}, 'complete_certificate': False})


def verify_direct_certificate(certificate, *, replay_capture=None):
    require(replay_capture is None or type(replay_capture) is list, 'replay capture must be a list or None')
    semantic_certificate(certificate)
    require(type(certificate) is dict and certificate.get('schema') == SCHEMA, 'wrong direct schema')
    require(certificate.get('source_sha256') == sha(__file__), 'direct source pin mismatch')
    require(certificate.get('baseline_helper_source_sha256') == BASELINE_PIN, 'baseline helper pin mismatch')
    require(certificate.get('floor_moment_source_sha256') == FLOOR_PIN, 'floor source pin mismatch')
    require(certificate.get('direct_proof_sha256') == DIRECT_PROOF_PIN, 'direct proof pin mismatch')
    requests = certificate.get('requests')
    require(type(requests) is list, 'request list required')
    observer = DirectSignedGapObserver()
    try:
        for request in requests:
            require(type(request) is dict and type(request.get('inputs')) is dict, 'malformed request')
            inputs = request['inputs']
            require(set(inputs) == {'g', 'k', 'R', 'r', 'stride'}, 'unexpected input fields')
            observer.one_negative(inputs['g'], inputs['k'], inputs['R'], inputs['r'], stride=inputs['stride'])
        replay = observer.export_certificate()
    except BaseException:
        if replay_capture is not None and observer.runner.arithmetic.operations:
            replay_capture.append(observer.incomplete_snapshot())
        raise
    if replay_capture is not None:
        replay_capture.append(deepcopy(replay))
    require(semantic_certificate(certificate) == semantic_certificate(replay), 'direct certificate does not replay')
    return {'verified': True, 'requests_replayed': len(requests),
        'replay_arithmetic_stats': deepcopy(observer.runner.arithmetic.stats), 'replay_certificate': replay,
        'excluded_runtime_field': 'actual_integer_evidence.arithmetic_stats.native_kernel_calls_delta'}
