"""V-divides-R two-bit scalar observer, using frozen single progressions."""
from copy import deepcopy
from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parent
DIRECT = ROOT.parent/'sep27-qft-gap-direct/direct_gap'
DIRECT_PIN = '3ab2515c1b9df35d01c9605f21d8f8fe56bd044effe489063192c0a5c56a8521'
PROOF = ROOT.parent/'sep27-qft-two-bit/TWO_BIT_PERIOD_NESTING.md'
PROOF_PIN = '9189f01243aa308f516534337b40e6e2c03a7fcf3f79a7dde179a5689bca1d26'
SCHEMA = 'BRC_ALIGNED_TWO_BIT_STRETCH_V1'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


if sha(DIRECT/'direct_signed_gap.py') != DIRECT_PIN:
    raise ValueError('frozen direct observer source changed')
sys.path.insert(0, str(DIRECT))
from direct_signed_gap import (DirectSignedGapObserver, TypedFloorMoments,
    typed_two_power, semantic_certificate, require, FLOOR_PIN, BASELINE_PIN,
    DIRECT_PROOF_PIN)


def validate_inputs(g, ell, k, R, r, stride):
    require(all(type(x) is int for x in (g, ell, k, R, r, stride)), 'strict integer inputs required')
    require(g >= 2 and 0 <= ell < k < g, 'g>=2 and 0<=ell<k<g required')
    require(R >= 1 and 0 <= r < R, 'positive modulus and canonical residue required')
    require(stride == 1, 'only physical stride one is supported')


class AlignedTwoBitObserver:
    def __init__(self):
        self.direct = DirectSignedGapObserver()
        self.runner = self.direct.runner
        self.requests = []
        self.inflight = None
        self._source = sha(__file__)

    def _check(self):
        require(sha(__file__) == self._source, 'two-bit adapter source changed')
        require(sha(DIRECT/'direct_signed_gap.py') == DIRECT_PIN, 'frozen direct source changed')
        require(sha(PROOF) == PROOF_PIN, 'two-bit theorem changed')
        self.direct._check()

    def _computed(self, function):
        return self.direct._computed(function)

    def _division(self, x, m):
        start = len(self.runner.signed_operations)
        quotient, remainder = self.runner.floor_div(x, m)
        return {'numerator': x, 'denominator': m, 'quotient': quotient, 'remainder': remainder,
                'signed_operations_start': start,
                'signed_operations_stop': len(self.runner.signed_operations)}

    def _length(self, head, step, limit):
        last_minus_head = self._computed(lambda: self.runner.sub(self.runner.sub(limit, 1), head))
        if last_minus_head['value'] < 0:
            zero = self._computed(lambda: self.runner.add(0, 0))
            return {'head': head, 'step': step, 'limit': limit, 'empty': True,
                    'last_minus_head': last_minus_head, 'n': 0, 'zero': zero}
        division = self._division(last_minus_head['value'], step)
        length = self._computed(lambda: self.runner.add(division['quotient'], 1))
        return {'head': head, 'step': step, 'limit': limit, 'empty': False,
                'last_minus_head': last_minus_head, 'division': division,
                'length_addition': length, 'n': length['value']}

    def _branch(self, label, head, step, expected_n, M, U, P, V, remainder, coefficients):
        r = self.runner
        branch = {'label': label, 'head': head, 'step': step, 'expected_n': expected_n,
                  'signed_operations_start': len(r.signed_operations)}
        parity = self._division(head['value'], 2)
        require(parity['remainder'] in (0, 1), 'invalid observed parity')
        sign = -1 if parity['remainder'] else 1
        branch.update(parity=parity, sign=sign)
        original = self.direct._progression(head, label+':original', M, U, P, step, coefficients)
        count_difference = self._computed(lambda: r.sub(original['n'], expected_n['value']))
        require(count_difference['value'] == 0, 'parity branch canonical length differs')
        shifted_head = self._computed(lambda: r.add(head['value'], 1))
        shifted = self.direct._progression(shifted_head, label+':shifted', M, U, P, step, coefficients)
        removed = self._computed(lambda: r.sub(original['n'], shifted['n']))
        require(removed['value'] in (0, 1), 'shifted canonical range has invalid count')
        tail = {'removed_zero_terms': removed['value'], 'count_difference': removed,
                'extension': 'A_one(M)=0 is the empty sum; no nonempty table outside [0,M)'}
        if removed['value']:
            require(original['n'] > 0, 'cannot remove a term from an empty progression')
            last_index = self._computed(lambda: r.sub(original['n'], 1))
            last_z = self._computed(lambda: r.add(head['value'], r.mul(step, last_index['value'])))
            shifted_last = self._computed(lambda: r.add(last_z['value'], 1))
            boundary_difference = self._computed(lambda: r.sub(shifted_last['value'], M))
            require(boundary_difference['value'] == 0, 'removed shifted term is not exactly A_one(M)')
            tail.update(last_index=last_index, last_original_z=last_z,
                        shifted_last=shifted_last, boundary_difference=boundary_difference)
        original_weight = self._computed(lambda: r.sub(V, remainder))
        original_product = self._computed(lambda: r.mul(original_weight['value'], original['value']))
        shifted_product = self._computed(lambda: r.mul(remainder, shifted['value']))
        unsigned_difference = self._computed(lambda: r.sub(original_product['value'], shifted_product['value']))
        signed_result = self._computed(lambda: r.mul(sign, unsigned_difference['value']))
        branch.update(original=original, canonical_count_difference=count_difference,
            shifted=shifted, shifted_zero_tail=tail, original_weight=original_weight,
            shifted_weight=remainder, original_product=original_product, shifted_product=shifted_product,
            unsigned_difference=unsigned_difference, signed_result=signed_result, value=signed_result['value'],
            sign_is_original_z_not_shifted_z=True, signed_operations_stop=len(r.signed_operations))
        return branch

    def _orientation(self, label, head, L, M, U, P, V, R, h, h_parity, coefficients):
        r = self.runner
        record = {'orientation': label, 'multiplicity': 1, 'head': head,
                  'signed_operations_start': len(r.signed_operations), 'branches': []}
        length = self._length(head['value'], R, L)
        record['original_length'] = length
        if length['empty']:
            zero = self._computed(lambda: r.add(0, 0))
            record.update(empty=True, zero=zero, value=zero['value'],
                          signed_operations_stop=len(r.signed_operations))
            return record
        compressed_head = self._division(head['value'], V)
        z0, remainder = compressed_head['quotient'], compressed_head['remainder']
        record.update(empty=False, compressed_head=compressed_head, constant_low_remainder=remainder)
        head0 = self._computed(lambda: r.add(z0, 0))
        if h_parity == 0:
            expected = self._computed(lambda: r.add(length['n'], 0))
            branch_specs = [('even_step', head0, h, expected)]
        else:
            twice_h = self._computed(lambda: r.add(h, h))
            n_plus_one = self._computed(lambda: r.add(length['n'], 1))
            even_count = self._division(n_plus_one['value'], 2)
            odd_count = self._division(length['n'], 2)
            even_expected = self._computed(lambda: r.add(even_count['quotient'], 0))
            odd_expected = self._computed(lambda: r.add(odd_count['quotient'], 0))
            odd_head = self._computed(lambda: r.add(z0, h))
            record['parity_split'] = {'twice_h': twice_h, 'n_plus_one': n_plus_one,
                                      'even_count': even_count, 'odd_count': odd_count}
            branch_specs = [('even_j', head0, twice_h['value'], even_expected),
                            ('odd_j', odd_head, twice_h['value'], odd_expected)]
        for branch_label, branch_head, step, expected in branch_specs:
            record['branches'].append(self._branch(label+':'+branch_label, branch_head,
                step, expected, M, U, P, V, remainder, coefficients))
        total = self._computed(lambda: r.total(branch['value'] for branch in record['branches']))
        record.update(total=total, value=total['value'], signed_operations_stop=len(r.signed_operations))
        return record

    def two_negative(self, g, ell, k, R, r, *, stride=1):
        require(self.inflight is None,
                'incomplete request: use a fresh observer; retained work cannot resume')
        validate_inputs(g, ell, k, R, r, stride)
        self._check()
        runner = self.runner
        start = len(runner.signed_operations)
        self.inflight = {'inputs': {'g': g, 'ell': ell, 'k': k, 'R': R, 'r': r, 'stride': stride},
                         'signed_operations_start': start}
        V = typed_two_power(runner, ell)
        alignment = self._division(R, V)
        self.inflight.update(V=V, alignment=alignment)
        require(alignment['remainder'] == 0, 'unaligned input: V must divide R; paid division retained')
        h = alignment['quotient']
        h_parity = self._division(h, 2)
        M = typed_two_power(runner, g-ell)
        U = typed_two_power(runner, k-ell)
        P = runner.add(U, U)
        H = typed_two_power(runner, g-k-1)
        L = runner.mul(V, M)
        self.inflight.update(h=h, h_parity=h_parity, M=M, U=U, P=P, H=H, L=L,
                             scales_operations_stop=len(runner.signed_operations))
        coefficients, helpers = self.direct._coefficients(H, P)
        self.inflight.update(coefficients=coefficients, coefficient_helpers=helpers, orientations=[])
        for label, head in (
            ('nonnegative_difference', self._computed(lambda: runner.add(r, 0))),
            ('negative_difference_magnitude', self._computed(lambda: runner.sub(R, r)))):
            orientation = self._orientation(label, head, L, M, U, P, V, R, h,
                                             h_parity['remainder'], coefficients)
            self.inflight['orientations'].append(orientation)
        final = self._computed(lambda: runner.add(self.inflight['orientations'][0]['value'],
                                                  self.inflight['orientations'][1]['value']))
        count = sum(2*len(o['branches']) for o in self.inflight['orientations'])
        tables = sum(len(b[which]['table_calls']) for o in self.inflight['orientations']
                     for b in o['branches'] for which in ('original', 'shifted'))
        require(count <= 8 and tables <= 16, 'progression/table structural bound exceeded')
        self.inflight.update(final_addition=final, value=final['value'],
            raw_denominator_exponent=2*g, compressed_length_is_not_normalization=True,
            single_progression_calls=count, top_level_table_calls=tables,
            signed_operations_stop=len(runner.signed_operations), negative_values_are_valid=True)
        record = self.inflight
        self.requests.append(record)
        self.inflight = None
        return deepcopy(record)

    def export_certificate(self):
        self._check()
        require(self.inflight is None, 'an incomplete request cannot be certified')
        return deepcopy({'schema': SCHEMA, 'source_sha256': self._source,
            'direct_source_sha256': DIRECT_PIN, 'direct_proof_sha256': DIRECT_PROOF_PIN,
            'two_bit_proof_sha256': PROOF_PIN, 'floor_moment_source_sha256': FLOOR_PIN,
            'baseline_helper_source_sha256': BASELINE_PIN, 'requests': self.requests,
            'actual_integer_evidence': self.runner.evidence(),
            'scope': 'V-divides-R stride-one two-negative-bit scalar observer; no order discovery or full Gram integration',
            'host_wiring': 'strict input validation, public loop/exponent indices, sign/branch routing of typed outputs, metadata',
            'admission': 'AUTHOR_EXECUTED_SHARED_CONTEXT_NOT_ADMITTED'})

    def incomplete_snapshot(self):
        r = self.runner
        return deepcopy({'schema': 'INCOMPLETE_'+SCHEMA, 'source_sha256': self._source,
            'requests': self.requests, 'inflight_request': self.inflight,
            'actual_integer_evidence': {'arithmetic_operations': r.arithmetic.operations,
                'arithmetic_stats': r.arithmetic.stats, 'signed_operations': r.signed_operations,
                'moment_nodes': r.nodes, 'window_weight_queries': r.weight_queries, 'stats': r.stats},
            'complete_certificate': False})


def verify_aligned_certificate(certificate, *, replay_capture=None):
    require(replay_capture is None or type(replay_capture) is list, 'replay capture must be a list or None')
    semantic_certificate(certificate)
    require(type(certificate) is dict and certificate.get('schema') == SCHEMA, 'wrong aligned-two-bit schema')
    for key, value in (('source_sha256', sha(__file__)), ('direct_source_sha256', DIRECT_PIN),
                       ('two_bit_proof_sha256', PROOF_PIN), ('floor_moment_source_sha256', FLOOR_PIN),
                       ('direct_proof_sha256', DIRECT_PROOF_PIN), ('baseline_helper_source_sha256', BASELINE_PIN)):
        require(certificate.get(key) == value, 'source/proof binding mismatch: '+key)
    requests = certificate.get('requests')
    require(type(requests) is list, 'request list required')
    observer = AlignedTwoBitObserver()
    try:
        for request in requests:
            require(type(request) is dict and type(request.get('inputs')) is dict, 'malformed request')
            inputs = request['inputs']
            require(set(inputs) == {'g', 'ell', 'k', 'R', 'r', 'stride'}, 'unexpected input fields')
            observer.two_negative(inputs['g'], inputs['ell'], inputs['k'], inputs['R'], inputs['r'],
                                  stride=inputs['stride'])
        replay = observer.export_certificate()
    except BaseException:
        if replay_capture is not None and observer.runner.arithmetic.operations:
            replay_capture.append(observer.incomplete_snapshot())
        raise
    if replay_capture is not None:
        replay_capture.append(deepcopy(replay))
    require(semantic_certificate(certificate) == semantic_certificate(replay), 'complete aligned-two-bit certificate does not replay')
    return {'verified': True, 'requests_replayed': len(requests),
            'replay_arithmetic_stats': deepcopy(observer.runner.arithmetic.stats), 'replay_certificate': replay,
            'excluded_runtime_field': 'actual_integer_evidence.arithmetic_stats.native_kernel_calls_delta'}
