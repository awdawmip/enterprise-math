"""Structural two-bit shortcuts on the unchanged V-divides-R domain.

Composition with the frozen direct private progression; no whole-query route,
ordinary numerical propagator, or answer-dependent selection.
"""
from copy import deepcopy
from pathlib import Path
import hashlib
import sys
ROOT = Path(__file__).resolve().parent
DIRECT = ROOT.parent/'sep27-qft-gap-direct/direct_gap'
DIRECT_PIN = '3ab2515c1b9df35d01c9605f21d8f8fe56bd044effe489063192c0a5c56a8521'
ALIGNED = ROOT.parent/'sep27-qft-two-bit-aligned'
ALIGNED_PIN = 'a6fd6cf5bfe10829c1918c50a952de22e5e2bc6cd538011f37a3bffdff5acdb2'
PROOF = ROOT.parent/'sep27-qft-two-bit/TWO_BIT_PERIOD_NESTING.md'
PROOF_PIN = '9189f01243aa308f516534337b40e6e2c03a7fcf3f79a7dde179a5689bca1d26'
SHORTCUT_PROOF = ROOT/'STRUCTURAL_SHORTCUTS.md'
SHORTCUT_PIN = '845df9a8a9e67862f197412d2bd8a20fdc10aedf14db73efc59f70ca97cfda7f'
SHORTCUT_REVIEW = ROOT/'guard_review/STRUCTURAL_SHORTCUTS_REVIEW.md'
REVIEW_PIN = '133d81d27860bc108075a8b995ec42644d37834c3824caaacfc6c22b30f946ab'
SCHEMA = 'BRC_TWO_BIT_STRUCTURAL_SHORTCUTS_V1'


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


class ShortcutTwoBitObserver:
    def __init__(self):
        self.direct = DirectSignedGapObserver()
        self.runner = self.direct.runner
        self.requests = []
        self.inflight = None
        self._source = sha(__file__)


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


    def incomplete_snapshot(self):
        r = self.runner
        return deepcopy({'schema': 'INCOMPLETE_'+SCHEMA, 'source_sha256': self._source,
            'requests': self.requests, 'inflight_request': self.inflight,
            'actual_integer_evidence': {'arithmetic_operations': r.arithmetic.operations,
                'arithmetic_stats': r.arithmetic.stats, 'signed_operations': r.signed_operations,
                'moment_nodes': r.nodes, 'window_weight_queries': r.weight_queries, 'stats': r.stats},
            'complete_certificate': False})

    def _check(self):
        require(sha(__file__) == self._source, 'shortcut source changed')
        for path, pin in ((DIRECT/'direct_signed_gap.py', DIRECT_PIN),
                          (ALIGNED/'aligned_two_bit.py', ALIGNED_PIN), (PROOF, PROOF_PIN),
                          (SHORTCUT_PROOF, SHORTCUT_PIN), (SHORTCUT_REVIEW, REVIEW_PIN)):
            require(sha(path) == pin, 'frozen source/proof/review changed: '+str(path))
        self.direct._check()

    def _affine_T(self, s, head, step):
        r = self.runner
        start = len(r.signed_operations)
        less = self._computed(lambda: r.sub(s, 1))
        numerator = self._computed(lambda: r.mul(s, less['value']))
        half = self.direct._exact_division(numerator['value'], 2)
        head_term = self._computed(lambda: r.mul(s, head))
        step_term = self._computed(lambda: r.mul(step, half['value']))
        total = self._computed(lambda: r.add(head_term['value'], step_term['value']))
        return {'s': s, 'head': head, 'step': step, 'less': less, 'numerator': numerator,
                'exact_half': half, 'head_term': head_term, 'step_term': step_term,
                'total': total, 'value': total['value'], 'signed_operations_start': start,
                'signed_operations_stop': len(r.signed_operations)}

    def _affine_progression(self, head, label, M, U, step):
        r = self.runner
        record = {'strategy': 'HIGHEST_BIT_AFFINE', 'orientation': label,
                  'head': head, 'step': step, 'limit': M, 'junction': U, 'multiplicity': 1,
                  'signed_operations_start': len(r.signed_operations), 'table_calls': []}
        length = self._length(head['value'], step, M)
        record.update(canonical_length=length, n=length['n'], empty=length['empty'])
        if length['empty']:
            zero = self._computed(lambda: r.add(0, 0))
            record.update(zero=zero, value=zero['value'], signed_operations_stop=len(r.signed_operations))
            return record
        n = length['n']
        junction_minus_head = self._computed(lambda: r.sub(U, head['value']))
        record['junction_minus_head'] = junction_minus_head
        if junction_minus_head['value'] < 0:
            q_receipt = self._computed(lambda: r.add(0, 0))
            record['q_selection'] = {'route': 'HEAD_ABOVE_JUNCTION', 'selected': q_receipt}
        else:
            division = self._division(junction_minus_head['value'], step)
            candidate = self._computed(lambda: r.add(division['quotient'], 1))
            difference = self._computed(lambda: r.sub(candidate['value'], n))
            selected = n if difference['value'] > 0 else candidate['value']
            q_receipt = self._computed(lambda: r.add(selected, 0))
            record['q_selection'] = {'route': 'TYPED_MIN_WITH_N', 'division': division,
                'candidate': candidate, 'candidate_minus_n': difference,
                'selected_source': 'n' if difference['value'] > 0 else 'candidate', 'selected': q_receipt}
        q = q_receipt['value']
        Tn, Tq = self._affine_T(n, head['value'], step), self._affine_T(q, head['value'], step)
        twice_q = self._computed(lambda: r.add(q, q))
        signed_count = self._computed(lambda: r.sub(twice_q['value'], n))
        mass_term = self._computed(lambda: r.mul(M, signed_count['value']))
        four_Tq = self._computed(lambda: r.mul(4, Tq['value']))
        value = self._computed(lambda: r.sub(r.add(mass_term['value'], Tn['value']), four_Tq['value']))
        record.update(q=q, Tn=Tn, Tq=Tq, twice_q=twice_q, signed_count=signed_count,
            mass_term=mass_term, four_Tq=four_Tq, sumA=value, value=value['value'],
            signed_operations_stop=len(r.signed_operations))
        return record

    def _single_progression(self, head, label, M, U, P, step, coefficients):
        if coefficients is None:
            return self._affine_progression(head, label, M, U, step)
        result = self.direct._progression(head, label, M, U, P, step, coefficients)
        result['strategy'] = 'FROZEN_DIRECT_MOMENTS'
        return result

    def _branch(self, label, head, step, expected_n, M, U, P, V, remainder, coefficients):
        r = self.runner
        branch = {'label': label, 'head': head, 'step': step, 'expected_n': expected_n,
                  'signed_operations_start': len(r.signed_operations)}
        parity = self._division(head['value'], 2)
        sign = -1 if parity['remainder'] else 1
        branch.update(parity=parity, sign=sign)
        original = self._single_progression(head, label+':original', M, U, P, step, coefficients)
        count_difference = self._computed(lambda: r.sub(original['n'], expected_n['value']))
        require(count_difference['value'] == 0, 'parity branch canonical length differs')
        branch.update(original=original, canonical_count_difference=count_difference,
                      shifted_weight=remainder)
        if remainder == 0:
            branch['shifted'] = {'execution': 'OMITTED_ZERO_COEFFICIENT', 'observed_coefficient': remainder,
                'arithmetic_executed': False, 'progression_called': False,
                'identity': 'A_two(V*z)=(-1)^z*V*A_one(z); omitted sum not evaluated'}
            product = self._computed(lambda: r.mul(V, original['value']))
            signed_result = self._computed(lambda: r.mul(sign, product['value']))
            branch.update(original_product=product, signed_result=signed_result,
                          value=signed_result['value'], progression_calls=1)
        else:
            shifted_head = self._computed(lambda: r.add(head['value'], 1))
            shifted = self._single_progression(shifted_head, label+':shifted', M, U, P, step, coefficients)
            removed = self._computed(lambda: r.sub(original['n'], shifted['n']))
            require(removed['value'] in (0, 1), 'invalid shifted canonical count')
            tail = {'removed_zero_terms': removed['value'], 'count_difference': removed,
                    'extension': 'A_one(M)=0 only as an empty overlap'}
            if removed['value']:
                require(original['n'] > 0, 'cannot remove from empty progression')
                idx = self._computed(lambda: r.sub(original['n'], 1))
                last = self._computed(lambda: r.add(head['value'], r.mul(step, idx['value'])))
                end = self._computed(lambda: r.add(last['value'], 1))
                difference = self._computed(lambda: r.sub(end['value'], M))
                require(difference['value'] == 0, 'removed shifted term is not A_one(M)')
                tail.update(last_index=idx, last_original_z=last, shifted_last=end, boundary_difference=difference)
            weight = self._computed(lambda: r.sub(V, remainder))
            first = self._computed(lambda: r.mul(weight['value'], original['value']))
            second = self._computed(lambda: r.mul(remainder, shifted['value']))
            diff = self._computed(lambda: r.sub(first['value'], second['value']))
            signed_result = self._computed(lambda: r.mul(sign, diff['value']))
            shifted['execution'] = 'EVALUATED'
            branch.update(shifted=shifted, shifted_zero_tail=tail, original_weight=weight,
                original_product=first, shifted_product=second, unsigned_difference=diff,
                signed_result=signed_result, value=signed_result['value'], progression_calls=2)
        branch.update(sign_is_original_z_not_shifted_z=True, signed_operations_stop=len(r.signed_operations))
        return branch

    def _finish(self):
        self.inflight['signed_operations_stop'] = len(self.runner.signed_operations)
        record = self.inflight
        self.requests.append(record)
        self.inflight = None
        return deepcopy(record)

    def two_negative(self, g, ell, k, R, r, *, stride=1):
        require(self.inflight is None, 'incomplete request: use a fresh observer; retained work cannot resume')
        validate_inputs(g, ell, k, R, r, stride)
        self._check()
        runner = self.runner
        self.inflight = {'inputs': {'g': g, 'ell': ell, 'k': k, 'R': R, 'r': r, 'stride': stride},
            'signed_operations_start': len(runner.signed_operations),
            'raw_denominator_exponent': 2*g, 'negative_values_are_valid': True,
            'compressed_length_is_not_normalization': True}
        V = typed_two_power(runner, ell)
        alignment = self._division(R, V)
        self.inflight.update(V=V, alignment=alignment)
        require(alignment['remainder'] == 0, 'unaligned input: V must divide R; paid division retained')
        # This is the original highest bit, not the compressed high bit.
        original_U = typed_two_power(runner, k)
        zero_test = self._division(original_U, R)
        self.inflight.update(original_highest_U=original_U, zero_test=zero_test,
                             alignment_checked_before_zero_test=True)
        if zero_test['remainder'] == 0:
            zero = self._computed(lambda: runner.add(0, 0))
            self.inflight.update(route='RESIDUE_HISTOGRAM_CANCELLATION', zero=zero, value=zero['value'],
                cancellation='R divides original 2^k; paired scalar Walsh signs cancel in each residue',
                orientations=[], orientations_evaluated=False, single_progression_calls=0,
                top_level_table_calls=0, affine_progression_calls=0, moment_progression_calls=0,
                omitted_shifted_progressions=0)
            return self._finish()
        h = alignment['quotient']
        h_parity = self._division(h, 2)
        M = typed_two_power(runner, g-ell)
        compressed_U = self._division(original_U, V)
        require(compressed_U['remainder'] == 0, 'compressed high bit is not integral')
        U = compressed_U['quotient']
        P = runner.add(U, U)
        H = typed_two_power(runner, g-k-1)
        L = runner.mul(V, M)
        affine = k == g-1
        self.inflight.update(route='HIGHEST_BIT_AFFINE' if affine else 'DIRECT_MOMENT_FALLBACK',
            h=h, h_parity=h_parity, M=M, compressed_U=compressed_U, U=U, P=P, H=H, L=L,
            scales_operations_stop=len(runner.signed_operations))
        if affine:
            coefficients, helpers = None, None
        else:
            coefficients, helpers = self.direct._coefficients(H, P)
        self.inflight.update(coefficients=coefficients, coefficient_helpers=helpers,
                             orientations=[], orientations_evaluated=True)
        for label, head in (
            ('nonnegative_difference', self._computed(lambda: runner.add(r, 0))),
            ('negative_difference_magnitude', self._computed(lambda: runner.sub(R, r)))):
            self.inflight['orientations'].append(self._orientation(label, head, L, M, U, P,
                V, R, h, h_parity['remainder'], coefficients))
        final = self._computed(lambda: runner.add(self.inflight['orientations'][0]['value'],
                                                  self.inflight['orientations'][1]['value']))
        branches = [b for o in self.inflight['orientations'] for b in o['branches']]
        progressions = [b['original'] for b in branches]
        progressions += [b['shifted'] for b in branches if b['shifted'].get('execution') == 'EVALUATED']
        table_count = sum(len(p['table_calls']) for p in progressions)
        require(len(progressions) <= 8 and table_count <= 16, 'structural bound exceeded')
        self.inflight.update(final_addition=final, value=final['value'],
            single_progression_calls=len(progressions), top_level_table_calls=table_count,
            affine_progression_calls=sum(p['strategy']=='HIGHEST_BIT_AFFINE' for p in progressions),
            moment_progression_calls=sum(p['strategy']=='FROZEN_DIRECT_MOMENTS' for p in progressions),
            omitted_shifted_progressions=sum(b['shifted']['execution']=='OMITTED_ZERO_COEFFICIENT' for b in branches))
        return self._finish()

    def export_certificate(self):
        self._check()
        require(self.inflight is None, 'an incomplete request cannot be certified')
        return deepcopy({'schema': SCHEMA, 'source_sha256': self._source,
            'aligned_source_sha256': ALIGNED_PIN, 'shortcut_proof_sha256': SHORTCUT_PIN,
            'shortcut_review_sha256': REVIEW_PIN, 'direct_source_sha256': DIRECT_PIN,
            'direct_proof_sha256': DIRECT_PROOF_PIN, 'two_bit_proof_sha256': PROOF_PIN,
            'floor_moment_source_sha256': FLOOR_PIN, 'baseline_helper_source_sha256': BASELINE_PIN,
            'requests': self.requests, 'actual_integer_evidence': self.runner.evidence(),
            'scope': 'Structural shortcuts on V-divides-R two-bit stride-one scalar observer; no general order or Gram integration',
            'host_wiring': 'strict validation, public bit indices, routing from typed signed/division outputs, metadata',
            'admission': 'AUTHOR_EXECUTED_SHARED_CONTEXT_NOT_ADMITTED'})


def verify_shortcut_certificate(certificate, *, replay_capture=None):
    require(replay_capture is None or type(replay_capture) is list, 'replay capture must be list or None')
    semantic_certificate(certificate)
    require(type(certificate) is dict and certificate.get('schema') == SCHEMA, 'wrong shortcut schema')
    for key, pin in (('source_sha256',sha(__file__)),('aligned_source_sha256',ALIGNED_PIN),
                    ('shortcut_proof_sha256',SHORTCUT_PIN),('shortcut_review_sha256',REVIEW_PIN),
                    ('direct_source_sha256',DIRECT_PIN),('direct_proof_sha256',DIRECT_PROOF_PIN),
                    ('two_bit_proof_sha256',PROOF_PIN),('floor_moment_source_sha256',FLOOR_PIN),
                    ('baseline_helper_source_sha256',BASELINE_PIN)):
        require(certificate.get(key) == pin, 'source/proof binding mismatch: '+key)
    requests = certificate.get('requests')
    require(type(requests) is list, 'request list required')
    observer = ShortcutTwoBitObserver()
    try:
        for request in requests:
            require(type(request) is dict and type(request.get('inputs')) is dict, 'malformed request')
            inp = request['inputs']
            require(set(inp) == {'g','ell','k','R','r','stride'}, 'unexpected input fields')
            observer.two_negative(inp['g'],inp['ell'],inp['k'],inp['R'],inp['r'],stride=inp['stride'])
        replay = observer.export_certificate()
    except BaseException:
        if replay_capture is not None and observer.runner.arithmetic.operations:
            replay_capture.append(observer.incomplete_snapshot())
        raise
    if replay_capture is not None:
        replay_capture.append(deepcopy(replay))
    require(semantic_certificate(certificate) == semantic_certificate(replay), 'complete shortcut certificate does not replay')
    return {'verified':True,'requests_replayed':len(requests),
            'replay_arithmetic_stats':deepcopy(observer.runner.arithmetic.stats),'replay_certificate':replay,
            'excluded_runtime_field':'actual_integer_evidence.arithmetic_stats.native_kernel_calls_delta'}

