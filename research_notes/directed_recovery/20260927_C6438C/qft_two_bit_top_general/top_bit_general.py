"""Code-only highest-selected-bit scalar observer for arbitrary supplied R.

All numerical work uses the frozen actual typed runner. No scientific run is
performed on import. A separate reviewed checker and startup guard are needed.
"""
from copy import deepcopy
from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parent
DIRECT = ROOT.parent/'sep27-qft-gap-direct/direct_gap'
DIRECT_PIN = '3ab2515c1b9df35d01c9605f21d8f8fe56bd044effe489063192c0a5c56a8521'
PROOF_PIN = '880fb9d90f9258e0b96f6f47281bd711b11bd2ec515bddb6a6212cf45266ee89'
REVIEW_PIN = 'e5f31e9619a3233c65af23b642d262e98996d6ca9ee538910e38c21ba412aaab'
SCHEMA = 'BRC_TOP_BIT_GENERAL_MODULUS_V1'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


if sha(DIRECT/'direct_signed_gap.py') != DIRECT_PIN:
    raise ValueError('frozen direct source changed')
sys.path.insert(0, str(DIRECT))
from direct_signed_gap import (DirectSignedGapObserver, typed_two_power,
    semantic_certificate, require, FLOOR_PIN, BASELINE_PIN, DIRECT_PROOF_PIN)


def validate_inputs(g, ell, k, R, r, stride):
    require(all(type(x) is int for x in (g, ell, k, R, r, stride)), 'strict integer inputs required')
    require(g >= 2 and 0 <= ell < k < g and k == g-1, 'highest selected bit must be g-1')
    require(R >= 1 and 0 <= r < R, 'positive supplied modulus and canonical residue required')
    require(stride == 1, 'only stride one is supported')


class TopBitGeneralObserver:
    def __init__(self):
        self.direct = DirectSignedGapObserver()
        self.runner = self.direct.runner
        self.requests = []
        self.inflight = None
        self._source = sha(__file__)

    def _check(self):
        require(sha(__file__) == self._source, 'observer source changed')
        require(sha(DIRECT/'direct_signed_gap.py') == DIRECT_PIN, 'frozen direct source changed')
        require(sha(ROOT/'TOP_BIT_GENERAL_MODULUS.md') == PROOF_PIN, 'general-modulus proof changed')
        require(sha(ROOT/'guard_review/TOP_BIT_GENERAL_MODULUS_REVIEW.md') == REVIEW_PIN, 'proof review changed')
        self.direct._check()

    def _computed(self, function):
        return self.direct._computed(function)

    def _division(self, x, m):
        start = len(self.runner.signed_operations)
        q, r = self.runner.floor_div(x, m)
        return {'numerator': x, 'denominator': m, 'quotient': q, 'remainder': r,
            'signed_operations_start': start, 'signed_operations_stop': len(self.runner.signed_operations)}

    def _length(self, head, step, limit):
        t = self._computed(lambda: self.runner.sub(self.runner.sub(limit, 1), head))
        record = {'head': head, 'step': step, 'exclusive_limit': limit, 'last_minus_head': t}
        if t['value'] < 0:
            zero = self._computed(lambda: self.runner.add(0, 0))
            record.update(empty=True, n=zero['value'], zero=zero)
        else:
            division = self._division(t['value'], step)
            n = self._computed(lambda: self.runner.add(division['quotient'], 1))
            record.update(empty=False, n=n['value'], division=division, length_addition=n)
        return record

    def _coefficients(self, piece, V, M):
        r = self.runner
        start = len(r.signed_operations)
        if piece == 'low':
            operations = (
                ('a0', lambda: r.mul(V, M)),
                ('a1', lambda: r.sub(3, r.mul(2, M))),
                ('b0', lambda: r.sub(r.mul(r.mul(2, V), M), r.mul(6, V))),
                ('b1', lambda: r.add(6, 0)),
                ('c', lambda: r.mul(-6, V)))
        else:
            require(piece == 'high', 'unknown piece')
            operations = (
                ('a0', lambda: r.mul(-1, r.mul(V, M))),
                ('a1', lambda: r.sub(r.mul(2, M), 1)),
                ('b0', lambda: r.sub(r.mul(2, V), r.mul(r.mul(2, V), M))),
                ('b1', lambda: r.add(-2, 0)),
                ('c', lambda: r.mul(2, V)))
        primitive = {name: self._computed(fn) for name, fn in operations}
        a0, a1, b0, b1, c = (primitive[name]['value'] for name in ('a0','a1','b0','b1','c'))
        operations = (
            ('n', lambda: r.mul(3, a0)),
            ('d', lambda: r.mul(3, a1)),
            ('q', lambda: r.mul(6, b0)),
            ('dq', lambda: r.mul(6, b1)),
            ('q2', lambda: r.mul(12, c)),
            ('delta1', lambda: r.sub(r.add(r.mul(-6, a0), r.mul(3, b0)), c)),
            ('ddelta1', lambda: r.add(r.mul(-6, a1), r.mul(3, b1))),
            ('delta2', lambda: r.add(r.mul(-6, b0), r.mul(6, c))),
            ('ddelta2', lambda: r.mul(-6, b1)),
            ('delta3', lambda: r.mul(-8, c)))
        coefficients = {name: self._computed(fn) for name, fn in operations}
        return {'piece': piece, 'primitive': primitive, 'coefficients': coefficients,
            'signed_operations_start': start, 'signed_operations_stop': len(r.signed_operations)}

    def _segment(self, record, P, V, R, coefficients):
        r = self.runner
        n, b = record['n'], record['head']['value']
        record['signed_operations_start'] = len(r.signed_operations)
        if n == 0:
            zero = self._computed(lambda: r.add(0, 0))
            record.update(empty=True, zero=zero, value=zero['value'], table_calls=[],
                signed_operations_stop=len(r.signed_operations))
            return
        require(n > 0, 'negative segment count')
        record.update(empty=False, table_calls=[])
        table, receipt = self.direct._table(n, P, R, b)
        record['table_calls'].append(receipt)
        offset = self._computed(lambda: r.add(b, V))
        record['shifted_offset'] = offset
        shifted, receipt = self.direct._table(n, P, R, offset['value'])
        record['table_calls'].append(receipt)
        delta = {f'{u},{v}': self._computed(lambda u=u, v=v: r.sub(shifted[u,v], table[u,v]))
            for u, v in ((0,1),(1,1),(0,2),(1,2),(0,3))}
        weighted = {
            'd': self._computed(lambda: r.add(r.mul(b, table[0,0]), r.mul(R, table[1,0]))),
            'dq': self._computed(lambda: r.add(r.mul(b, table[0,1]), r.mul(R, table[1,1]))),
            'ddelta1': self._computed(lambda: r.add(r.mul(b, delta['0,1']['value']), r.mul(R, delta['1,1']['value']))),
            'ddelta2': self._computed(lambda: r.add(r.mul(b, delta['0,2']['value']), r.mul(R, delta['1,2']['value'])))}
        factors = {'n': table[0,0], 'd': weighted['d']['value'], 'q': table[0,1],
            'dq': weighted['dq']['value'], 'q2': table[0,2], 'delta1': delta['0,1']['value'],
            'ddelta1': weighted['ddelta1']['value'], 'delta2': delta['0,2']['value'],
            'ddelta2': weighted['ddelta2']['value'], 'delta3': delta['0,3']['value']}
        record.update(deltas=delta, weighted_sums=weighted, term_factors=factors, terms={})
        for name, factor in factors.items():
            record['terms'][name] = self._computed(lambda name=name, factor=factor:
                r.mul(coefficients['coefficients'][name]['value'], factor))
        numerator = self._computed(lambda: r.total(t['value'] for t in record['terms'].values()))
        record['three_sum_numerator'] = numerator
        quotient = self.direct._exact_division(numerator['value'], 3)
        record.update(exact_third=quotient, value=quotient['value'], signed_operations_stop=len(r.signed_operations))

    def _orientation(self, record, L, H, P, V, R, coefficients):
        r = self.runner
        record['signed_operations_start'] = len(r.signed_operations)
        b = record['head']['value']
        whole = self._length(b, R, L)
        record['whole_length'] = whole
        if whole['empty']:
            zero = self._computed(lambda: r.add(0, 0))
            record.update(empty=True, zero=zero, value=zero['value'], segments=[],
                signed_operations_stop=len(r.signed_operations))
            return
        low = self._length(b, R, H)
        high_count = self._computed(lambda: r.sub(whole['n'], low['n']))
        require(high_count['value'] >= 0, 'low count exceeds whole count')
        high_head = self._computed(lambda: r.add(b, r.mul(R, low['n'])))
        record.update(empty=False, low_length=low, high_count=high_count, high_head=high_head, segments=[])
        for piece, head, n in (('low', record['head'], low['n']), ('high', high_head, high_count['value'])):
            segment = {'piece': piece, 'head': head, 'n': n, 'step': R,
                'displacement_lower_bound': 0 if piece=='low' else H,
                'displacement_exclusive_upper_bound': H if piece=='low' else L,
                'coefficient_piece': piece}
            record['segments'].append(segment)
            self._segment(segment, P, V, R, coefficients[piece])
        total = self._computed(lambda: r.total(s['value'] for s in record['segments']))
        record.update(total=total, value=total['value'], signed_operations_stop=len(r.signed_operations))

    def two_negative(self, g, ell, k, R, r, *, stride=1):
        require(self.inflight is None, 'incomplete request: retained work requires a fresh observer')
        validate_inputs(g, ell, k, R, r, stride)
        self._check()
        runner = self.runner
        self.inflight = {'inputs': {'g':g,'ell':ell,'k':k,'R':R,'r':r,'stride':stride},
            'signed_operations_start': len(runner.signed_operations), 'raw_denominator_exponent': 2*g,
            'modulus_alignment_required': False, 'route': 'TOP_BIT_TWO_PIECE_FLOOR_MOMENTS'}
        V = typed_two_power(runner, ell)
        M = typed_two_power(runner, g-ell)
        L = runner.mul(V, M)
        P = runner.add(V, V)
        half = self.direct._exact_division(L, 2)
        H = half['value']
        self.inflight.update(V=V, M=M, L=L, P=P, half_length=half,
            scales_operations_stop=len(runner.signed_operations), coefficients={})
        for piece in ('low', 'high'):
            self.inflight['coefficients'][piece] = self._coefficients(piece, V, M)
        self.inflight['orientations'] = []
        for label, head in (('nonnegative_difference', self._computed(lambda: runner.add(r, 0))),
                            ('negative_difference_magnitude', self._computed(lambda: runner.sub(R, r)))):
            orientation = {'orientation':label,'multiplicity':1,'head':head}
            self.inflight['orientations'].append(orientation)
            self._orientation(orientation, L, H, P, V, R, self.inflight['coefficients'])
        result = self._computed(lambda: runner.total(o['value'] for o in self.inflight['orientations']))
        tables = sum(len(s['table_calls']) for o in self.inflight['orientations'] for s in o['segments'])
        require(tables <= 8, 'top-level table bound exceeded')
        self.inflight.update(final_addition=result, value=result['value'], top_level_table_calls=tables,
            signed_operations_stop=len(runner.signed_operations))
        record = self.inflight
        self.requests.append(record)
        self.inflight = None
        return deepcopy(record)

    def incomplete_snapshot(self):
        r = self.runner
        return deepcopy({'schema':'INCOMPLETE_'+SCHEMA, 'source_sha256':self._source,
            'requests':self.requests, 'inflight_request':self.inflight, 'complete_certificate':False,
            'actual_integer_evidence':{'arithmetic_operations':r.arithmetic.operations,
                'arithmetic_stats':r.arithmetic.stats,'signed_operations':r.signed_operations,
                'moment_nodes':r.nodes,'window_weight_queries':r.weight_queries,'stats':r.stats}})

    def export_certificate(self):
        self._check()
        require(self.inflight is None, 'incomplete work cannot be certified')
        return deepcopy({'schema':SCHEMA, 'source_sha256':self._source,
            'proof_sha256':PROOF_PIN,'proof_review_sha256':REVIEW_PIN,
            'direct_source_sha256':DIRECT_PIN,'direct_proof_sha256':DIRECT_PROOF_PIN,
            'floor_moment_source_sha256':FLOOR_PIN,'baseline_helper_source_sha256':BASELINE_PIN,
            'requests':self.requests,'actual_integer_evidence':self.runner.evidence(),
            'scope':'Highest selected bit scalar pair count at arbitrary supplied modulus; no order or matrix oracle',
            'host_wiring':'strict inputs, public indices, branches from typed observed outputs, metadata',
            'admission':'AUTHOR_EXECUTED_SHARED_CONTEXT_NOT_ADMITTED'})


def verify_top_bit_certificate(certificate, *, replay_capture=None):
    require(replay_capture is None or type(replay_capture) is list, 'replay capture must be list or None')
    semantic_certificate(certificate)
    require(type(certificate) is dict and certificate.get('schema') == SCHEMA, 'wrong top-bit schema')
    for key, pin in (('source_sha256',sha(__file__)),('proof_sha256',PROOF_PIN),
                    ('proof_review_sha256',REVIEW_PIN),('direct_source_sha256',DIRECT_PIN),
                    ('direct_proof_sha256',DIRECT_PROOF_PIN),('floor_moment_source_sha256',FLOOR_PIN),
                    ('baseline_helper_source_sha256',BASELINE_PIN)):
        require(certificate.get(key) == pin, 'source/proof mismatch: '+key)
    requests = certificate.get('requests')
    require(type(requests) is list, 'request list required')
    observer = TopBitGeneralObserver()
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
    require(semantic_certificate(certificate) == semantic_certificate(replay), 'complete top-bit certificate does not replay')
    return {'verified':True,'requests_replayed':len(requests),
        'replay_arithmetic_stats':deepcopy(observer.runner.arithmetic.stats),'replay_certificate':replay,
        'excluded_runtime_field':'actual_integer_evidence.arithmetic_stats.native_kernel_calls_delta'}
