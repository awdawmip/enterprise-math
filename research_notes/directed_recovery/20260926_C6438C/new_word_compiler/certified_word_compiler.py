"""Resumable full-carrier compiler over unchanged actual H4/sign/swap letters.

The target is only observed. No target matrix propagates a dynamic state.
Every accepting inequality is replayed as signed observations of positive BRC
paths. Completeness is an author theorem, not a practical search-time claim.
"""
from __future__ import annotations

import gzip
import hashlib
import importlib.util
import json
import os
import sys
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

# Exact certificate integers may exceed Python's default decimal I/O cap.
# This removes only that serialization/parser limit, never an arithmetic or
# native-coefficient limit. Callers still control explicit search budgets.
if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parent
SOURCE = Path(os.environ.get('BRC_STAGE87_SOURCE',
    'D:/em/TEMP/sep26-local-takeover/intake_brc/stage87-source')).resolve()
ZERO_SOURCE = Path(os.environ.get('BRC_ZERO_ENDPOINT_SOURCE',
    'D:/em/TEMP/sep26-shor-alternative/adversarial/zero_endpoint_extension.py')).resolve()
sys.path.insert(0, str(SOURCE))
import stage80.fixed_phase as fixed
from stage79.phase_compiler import polynomial_probe, encode
from stage45.brc_loop_recheck import CALLS, core_power, verify_vendor

_spec = importlib.util.spec_from_file_location('compiler_zero_endpoint', ZERO_SOURCE)
_zero = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_zero)

DIM = 61
VERSION = 'FIXED_WORD_COMPILER_V1'
ACTIVITY = 'RA-CAAAC604CB513AEA8BBC1DFC'
PRIMITIVE_SOURCE = '0852cad130c1d877174d235687cf60c19f318c58'
ALPHABET = (('h4', 0, 1, 2, 3), ('neg', 0)) + tuple(
    ('swap', j, j+1) for j in range(DIM-1))
QUARTER_WORD = (('swap', 0, 1), ('neg', 1))


def packed(value):
    return json.dumps(encode(value), sort_keys=True, ensure_ascii=False,
                      separators=(',', ':')).encode('utf-8')


def digest(value):
    return hashlib.sha256(packed(value)).hexdigest()


def json_value(value):
    return json.loads(packed(value))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, minimum=0):
    require(isinstance(value, int) and not isinstance(value, bool) and value >= minimum,
            'invalid integer parameter')
    return value


def rational(value, positive=False):
    require(isinstance(value, (int, str, F)) and not isinstance(value, bool),
            'only explicit integer/rational inputs are supported')
    result = F(value)
    require(not positive or result > 0, 'positive rational required')
    return result


def normalize_word(word):
    result = []
    for raw in word:
        gate = tuple(raw)
        require(bool(gate) and gate[0] in ('h4', 'neg', 'swap'), 'unknown native letter')
        require(len(gate) == {'h4': 5, 'neg': 2, 'swap': 3}[gate[0]], 'letter arity')
        ids = gate[1:]
        require(all(isinstance(i, int) and not isinstance(i, bool) and 0 <= i < DIM
                    for i in ids) and len(set(ids)) == len(ids), 'coordinate indices')
        result.append(gate)
    return tuple(result)


def positive_determinant(word):
    return sum(g[0] != 'h4' for g in word) % 2 == 0


@lru_cache(None)
def source_binding():
    files = {
        'compiler': Path(__file__),
        'native_profile': ROOT / 'NATIVE_WORD_PROFILE.json',
        'fixed_phase': SOURCE / 'stage80/fixed_phase.py',
        'phase_compiler': SOURCE / 'stage79/phase_compiler.py',
        'zero_endpoint_extension': ZERO_SOURCE,
        'brc_adapter': SOURCE / 'stage45/brc_loop_recheck.py',
    }
    return {'primitive_source': PRIMITIVE_SOURCE, 'kernel': verify_vendor(),
            'files_sha256': {name: hashlib.sha256(path.read_bytes()).hexdigest()
                             for name, path in files.items()},
            'alphabet_sha256': digest(ALPHABET), 'dimension': DIM}


def unrank_word(index):
    """All finite words once, length then lexicographic rank; zero is empty."""
    integer(index)
    length, block = 0, 1
    while index >= block:
        index -= block
        length += 1
        block *= len(ALPHABET)
    digits = [0]*length
    for j in range(length-1, -1, -1):
        index, digits[j] = divmod(index, len(ALPHABET))
    return tuple(ALPHABET[i] for i in digits)


def candidate(index, seeds):
    return seeds[index] if index < len(seeds) else unrank_word(index-len(seeds))


def advance(stage, offset):
    return (stage, offset+1) if offset < stage else (stage+1, 0)


class PositivePathObserver:
    """Small acyclic positive-path products/sums with separate sign endpoints.

    Inputs are source-bound actual column observations, rational target bracket
    endpoints, integers, or earlier endpoint differences. This is an observer
    expression graph; it is never a gate applied to a dynamic state.
    """
    def __init__(self):
        self.operations = []

    def evaluate(self, name, terms):
        terms = tuple(tuple(F(x) for x in term) for term in terms)
        require(bool(terms) and all(term for term in terms), 'empty observer term')
        depth = max(2, max(map(len, terms)))
        n = 3 + len(terms)*(depth-1)
        graph = [[F(0) for _ in range(n)] for _ in range(n)]
        edges = []
        for j, term in enumerate(terms):
            negative = sum(x < 0 for x in term) % 2
            factors = tuple(abs(x) for x in term) + (F(1),)*(depth-len(term))
            nodes = [0] + list(range(3+j*(depth-1), 3+(j+1)*(depth-1))) + [1+negative]
            for u, v, weight in zip(nodes, nodes[1:], factors):
                graph[u][v] = weight
                edges.append([u, v, str(weight)])
        row = core_power(tuple(map(tuple, graph)), depth)[0]
        result = row[1]-row[2]
        expected = F(0)
        for term in terms:
            product = F(1)
            for factor in term:
                product *= factor
            expected += product
        require(result == expected, 'positive-path composition identity')
        self.operations.append({'name': name, 'terms': [[str(x) for x in t] for t in terms],
            'states': n, 'depth': depth, 'positive_edges': edges,
            'positive_endpoint': str(row[1]), 'negative_endpoint': str(row[2]),
            'signed_observation': str(result), 'kernel': 'recurrent_mass_power'})
        return result

    def add(self, name, left, right):
        return self.evaluate(name, ((left,), (right,)))


def recorded_polynomial(p, x, probes):
    """Frozen probe plus its complete two-endpoint actual replay receipt."""
    frozen_value = polynomial_probe(p, x)
    graph = [[F(0) for _ in range(9)] for _ in range(9)]
    graph[0][1]=p; graph[1][2]=x; graph[2][7]=x
    graph[0][3]=2; graph[3][4]=x; graph[4][7]=1
    graph[0][5]=p; graph[5][6]=1; graph[6][8]=1
    row = core_power(tuple(map(tuple, graph)), 3)[0]
    require(row[7]-row[8] == frozen_value, 'frozen polynomial endpoint mismatch')
    probes.append({'p': str(p), 'x': str(x), 'positive_endpoint_7': str(row[7]),
                   'positive_endpoint_8': str(row[8]),
                   'signed_observation': str(frozen_value), 'states': 9, 'depth': 3})
    return frozen_value


@lru_cache(maxsize=128)
def isolate_target(m, bits):
    integer(m, 2); integer(bits, 3)
    # The existing closed endpoint extension executes the inherited source.
    existing = _zero.closed_dyadic_parameters(m, bits)
    probes, tower = [], [{'phase_index': 2, 'lower': '1', 'upper': '1'}]

    def bracket(p):
        if p == 0:
            require(recorded_polynomial(p, F(0), probes) == 0, 'zero root')
            require(recorded_polynomial(p, F(1, 1 << bits), probes) > 0, 'zero upper')
            return F(0), F(0)
        lo, hi, scale = 0, 1 << bits, 1 << bits
        while hi-lo > 1:
            mid = (lo+hi)//2
            value = recorded_polynomial(p, F(mid, scale), probes)
            if value == 0:
                return F(mid, scale), F(mid, scale)
            if value < 0:
                lo = mid
            else:
                hi = mid
        require(recorded_polynomial(p, F(lo, scale), probes) <= 0 <=
                recorded_polynomial(p, F(hi, scale), probes), 'root bracket signs')
        return F(lo, scale), F(hi, scale)

    lo = hi = F(1)
    for phase in range(3, m+1):
        lo, _ = bracket(lo)
        _, hi = bracket(hi)
        require((lo, hi) == (existing[phase]['lower'], existing[phase]['upper']),
                'traced isolation differs from existing closed-root executor')
        tower.append({'phase_index': phase, 'lower': str(lo), 'upper': str(hi)})
    return {'phase_index': m, 'observer_depth': bits, 'lower': str(lo), 'upper': str(hi),
        'algebraic_target': 'q2=1; qprev*q*q+2*q-qprev=0, unique positive branch',
        'closed_zero_endpoint': True, 'tower': tower, 'actual_polynomial_probes': probes,
        'legacy_target32_vector64_modified': False,
        'profile': 'new exact-target observer depth; unchanged primitive coefficients'}


@lru_cache(maxsize=32)
def actual_word_columns(word):
    word = normalize_word(word)
    fixed.primitives()
    columns, vectors = [], []
    for j in range(DIM):
        basis = [int(i == j) for i in range(DIM)]
        nums, den = fixed.apply_word(basis, 1, word)
        recovered, recovered_den = fixed.apply_word(nums, den, word, inverse=True)
        require(recovered == basis and recovered_den == 1, 'actual inverse recovery failed')
        columns.append({'source': j, 'numerators': nums, 'denominator': den,
                        'inverse_recovered_numerators': recovered,
                        'inverse_recovered_denominator': recovered_den})
        vectors.append(tuple(F(x, den) for x in nums))
    # This identity observes all actual output columns; it propagates no state.
    gram = [[sum((x*y for x, y in zip(a, b) if x and y), F(0))
             for b in vectors] for a in vectors]
    require(all(gram[i][j] == int(i == j) for i in range(DIM) for j in range(DIM)),
            'complete actual columns are not orthogonal')
    return {'complete_basis_columns': columns, 'complete_gram_matrix': json_value(gram),
        'full_inverse_recovery': True, 'orthogonal_on_all_columns': True,
        'column_orientation': 'W_ij = destination i from source j',
        'native_executor': 'stage80.fixed_phase.apply_word',
        'actual_basis_applications': 2*DIM,
        'primitive_counts': {g: sum(letter[0] == g for letter in word)
                             for g in ('h4', 'neg', 'swap')}}, tuple(vectors)


def error_observer(columns, interval, tolerance):
    obs = PositivePathObserver()
    A = obs.add('A_W00_plus_W11', columns[0][0], columns[1][1])
    B = obs.add('B_W01_minus_W10', columns[1][0], -columns[0][1])
    # Grouping equal observed diagonal inputs is structural multiplicity only.
    counts = Counter(columns[j][j] for j in range(2, DIM))
    C = F(0)
    for i, (value, count) in enumerate(sorted(counts.items())):
        term = obs.evaluate(f'C_group_{i}', ((count, value),))
        C = obs.add(f'C_sum_{i}', C, term)
    lo, hi = F(interval['lower']), F(interval['upper'])
    require(0 <= lo <= hi <= 1, 'target interval domain')
    x = hi if A >= 0 else lo
    y = lo if B >= 0 else hi
    x2 = obs.evaluate('x_squared', ((x, x),))
    y2 = obs.evaluate('y_squared', ((y, y),))
    dx = obs.add('positive_Dx', 1, x2)
    nx = obs.add('nonnegative_Nx', 1, -x2)
    dy = obs.add('positive_Dy', 1, y2)
    dd = obs.evaluate('positive_common_denominator', ((dx, dy),))
    d2 = obs.evaluate('delta_squared', ((tolerance, tolerance),))
    terms = [obs.evaluate('margin_delta', ((d2, dd),)),
             obs.evaluate('margin_dimension', ((-2*DIM, dd),)),
             obs.evaluate('margin_C', ((2, C, dd),)),
             obs.evaluate('margin_A', ((2, A, nx, dy),)),
             obs.evaluate('margin_B', ((4, B, y, dx),))]
    margin = F(0)
    for j, term in enumerate(terms):
        margin = obs.add(f'margin_sum_{j}', margin, term)
    # The rational expression is a display/identity observer. Acceptance uses
    # the cross-multiplied positive-path endpoint difference above.
    c = lambda q: (1-q*q)/(1+q*q)
    s = lambda q: 2*q/(1+q*q)
    inner_lower = C + A*c(x) + B*s(y)
    error_upper = 2*DIM - 2*inner_lower
    require(dd > 0 and margin == (d2-error_upper)*dd, 'strict margin identity')
    require(error_upper >= 0, 'negative full-carrier squared error bound')
    return json_value({'A': A, 'B': B, 'C': C, 'c_interval': [c(hi), c(lo)],
        's_interval': [s(lo), s(hi)], 'chosen_c_root': x, 'chosen_s_root': y,
        'inner_lower': inner_lower, 'frobenius_squared_upper': error_upper,
        'requested_tolerance_squared': d2, 'positive_common_denominator': dd,
        'strict_margin': margin, 'strictly_certified': margin > 0,
        'decision': 'actual signed endpoint margin > 0',
        'all_column_identity': '||W-U||F^2=2D-2*(C+A*c+B*s)',
        'actual_positive_path_operations': obs.operations})


def _request(m, tolerance, seeds, observer_start_bits):
    return json_value({'version': VERSION, 'phase_index': m, 'dim': DIM,
        'tolerance': tolerance, 'seed_words': seeds,
        'observer_start_bits': observer_start_bits, 'source': source_binding(),
        'schedule': 'stage s; candidate i=0..s; bits=start+s-i'})


def compile_phase(m, tolerance, *, seeds=(), cursor=None, pair_budget=1,
                  observer_start_bits=3, activity=ACTIVITY):
    integer(m, 2); integer(observer_start_bits, 3); integer(pair_budget)
    tolerance = rational(tolerance, positive=True)
    seeds = tuple(normalize_word(w) for w in seeds)
    request = _request(m, tolerance, seeds, observer_start_bits)
    request_hash = digest(request)
    if cursor is None:
        stage, offset, processed = 0, 0, 0
    else:
        require(cursor.get('request_sha256') == request_hash and cursor.get('request') == request,
                'cursor source/target/seed/profile mismatch')
        stage = integer(cursor['stage']); offset = integer(cursor['offset'])
        processed = integer(cursor['processed_pairs'])
        require(offset <= stage and processed == stage*(stage+1)//2+offset,
                'inconsistent resume position')
    call_start = len(CALLS)
    events = []
    for _ in range(pair_budget):
        index, bits = offset, observer_start_bits+stage-offset
        word = candidate(index, seeds)
        location = {'stage': stage, 'candidate_index': index, 'observer_depth': bits,
                    'word_sha256': digest(word), 'word_length': len(word)}
        stage, offset = advance(stage, offset)
        processed += 1
        if not positive_determinant(word):
            events.append(dict(location, status='SKIPPED_NEGATIVE_DETERMINANT'))
            continue
        column_record, columns = actual_word_columns(word)
        interval = isolate_target(m, bits)
        observation = error_observer(columns, interval, tolerance)
        events.append(dict(location, status=('CERTIFIED' if observation['strictly_certified']
                                             else 'UNCERTIFIED_AT_THIS_OBSERVER_DEPTH')))
        if observation['strictly_certified']:
            certificate = json_value({'schema': VERSION+'_CERTIFICATE',
                'status': 'AUTHOR_ACTUAL_BOUNDED_EXECUTION_NOT_ADMITTED',
                'activity': activity, 'source': source_binding(), 'dim': DIM,
                'phase_index': m, 'word': word, 'determinant': 1,
                'requested_tolerance': tolerance, 'operator_error_bound': tolerance,
                'bound_is_strict': True, 'all_modes_retained': True,
                'target_used_for_propagation': False, 'target_interval': interval,
                'actual_columns': column_record, 'error_observer': observation,
                'search_location': location,
                'native_core_calls_this_search_call': len(CALLS)-call_start,
                'finite_search_is_not_a_complexity_bound': True})
            result = {'status': 'CERTIFIED', 'phase_index': m, 'dim': DIM,
                'word': json_value(word), 'operator_error_bound': str(tolerance),
                'certificate': certificate, 'certificate_sha256': digest(certificate),
                'pairs_used_this_call': len(events), 'events': events,
                'cursor': {'request_sha256': request_hash, 'request': request,
                           'stage': stage, 'offset': offset, 'processed_pairs': processed}}
            return result
    return {'status': 'PARTIAL', 'phase_index': m, 'dim': DIM,
        'pairs_used_this_call': len(events), 'events': events,
        'native_core_calls_this_call': len(CALLS)-call_start,
        'cursor': {'request_sha256': request_hash, 'request': request,
                   'stage': stage, 'offset': offset, 'processed_pairs': processed},
        'reason': 'finite pair budget exhausted; no no-solution conclusion'}


def verify_certificate(certificate):
    """Re-execute actual columns, algebraic probes and signed margin observer."""
    cert = json_value(certificate)
    require(cert['schema'] == VERSION+'_CERTIFICATE' and cert['source'] == source_binding(),
            'certificate source/profile mismatch')
    require(cert['dim'] == DIM and cert['determinant'] == 1 and
            cert['all_modes_retained'] and not cert['target_used_for_propagation'],
            'certificate scope mismatch')
    word = normalize_word(cert['word'])
    require(positive_determinant(word), 'wrong determinant component')
    m = integer(cert['phase_index'], 2)
    tolerance = rational(cert['requested_tolerance'], positive=True)
    require(F(cert['operator_error_bound']) == tolerance and cert['bound_is_strict'],
            'error budget mismatch')
    # Force scientific replay, rather than trusting this process's earlier cache.
    record, columns = actual_word_columns.__wrapped__(word)
    interval = isolate_target.__wrapped__(m, integer(cert['target_interval']['observer_depth'], 3))
    observation = error_observer(columns, interval, tolerance)
    require(json_value(record) == cert['actual_columns'], 'complete column certificate mismatch')
    require(json_value(interval) == cert['target_interval'], 'root/probe certificate mismatch')
    require(observation == cert['error_observer'] and observation['strictly_certified'],
            'strict full-carrier error witness mismatch')
    return {'status': 'VERIFIED', 'phase_index': m, 'dim': DIM,
            'certificate_sha256': digest(cert), 'operator_error_bound': str(tolerance)}


def verify_phase_record(record):
    require(record['status'] == 'CERTIFIED' and record['dim'] == DIM,
            'only certified full-carrier phase records may be injected')
    cert = record['certificate']
    require(record['certificate_sha256'] == digest(cert), 'certificate hash mismatch')
    require(record['phase_index'] == cert['phase_index'] and
            record['dim'] == cert['dim'] and
            normalize_word(record['word']) == normalize_word(cert['word']),
            'record and certificate refer to different phase/word/carrier')
    bound = rational(record['operator_error_bound'])
    expected = rational(cert['operator_error_bound'])
    exact_quarter = (record['phase_index'] == 2 and bound == 0 and
                    record.get('exact_quarter_turn') is True and
                    F(cert['error_observer']['frobenius_squared_upper']) == 0)
    require(bound == expected or exact_quarter, 'record bound not supported by certificate')
    return verify_certificate(cert)


def compile_phase_bank(t, epsilon, *, seed_words=None, cursor=None, pair_budget=1,
                       observer_start_bits=3, activity=ACTIVITY):
    integer(t, 2); integer(pair_budget); integer(observer_start_bits, 3)
    epsilon = rational(epsilon, positive=True)
    seed_words = seed_words or {}
    seeds = {str(m): tuple(normalize_word(w) for w in seed_words.get(m, seed_words.get(str(m), ())))
             for m in range(3, t+1)}
    count = (t-1)*(t-2)//2
    delta = epsilon/(2*count) if count else epsilon/2
    request = json_value({'version': VERSION+'_BANK', 't': t, 'epsilon': epsilon,
        'seed_words': seeds, 'observer_start_bits': observer_start_bits,
        'source': source_binding(), 'delta': delta})
    if cursor is None:
        phases, next_m, active = {}, 2, None
    else:
        require(cursor['request'] == request and cursor['request_sha256'] == digest(request),
                'bank cursor source/target/seed/profile mismatch')
        phases = json_value(cursor['phases'])
        next_m = integer(cursor['next_phase'], 2)
        active = cursor['active_phase_cursor']
        require(next_m <= t+1 and set(phases) == {str(m) for m in range(2, next_m)},
                'bank cursor phase coverage mismatch')
        for m in range(2, next_m):
            record = phases[str(m)]
            require(record['phase_index'] == m and record['status'] == 'CERTIFIED' and
                    record['certificate_sha256'] == digest(record['certificate']), 'bank phase record')
            verify_phase_record(record)
            require(F(record['operator_error_bound']) == (0 if m == 2 else delta), 'bank phase budget')
    used, events = 0, []
    while next_m <= t and used < pair_budget:
        phase_seeds = (QUARTER_WORD,) if next_m == 2 else seeds[str(next_m)]
        result = compile_phase(next_m, delta, seeds=phase_seeds, cursor=active,
            pair_budget=pair_budget-used, observer_start_bits=observer_start_bits, activity=activity)
        used += result['pairs_used_this_call']
        events.append({'phase_index': next_m, 'status': result['status'],
                       'pairs_used': result['pairs_used_this_call']})
        if result['status'] == 'PARTIAL':
            active = result['cursor']
            break
        if next_m == 2:
            require(F(result['certificate']['error_observer']['frobenius_squared_upper']) == 0,
                    'quarter turn must be exact')
            result['operator_error_bound'] = '0'
            result['exact_quarter_turn'] = True
        phases[str(next_m)] = result
        next_m += 1
        active = None
    weighted = sum((t-int(m)+1)*F(record['operator_error_bound'])
                   for m, record in phases.items())
    status = 'CERTIFIED' if next_m > t else 'PARTIAL'
    return json_value({'status': status, 't': t, 'dim': DIM, 'epsilon': epsilon,
        'phases': phases, 'occurrence_weighted_error_bound': weighted,
        'bound_is_for_complete_bank': status == 'CERTIFIED',
        'pair_budget': pair_budget, 'pairs_used_this_call': used, 'phase_events': events,
        'cursor': {'request': request, 'request_sha256': digest(request), 'phases': phases,
                   'next_phase': next_m, 'active_phase_cursor': active},
        'profile': 'new compiled word algorithm; frozen legacy target32/vector64 unchanged'})


def load_legacy_seed_words(path=None, max_m=32):
    path = Path(path or ROOT.parent / 'phases/bank_t34.json.gz')
    raw = gzip.decompress(path.read_bytes())
    require(hashlib.sha256(raw).hexdigest() ==
            'feecbc02808991f6d7b1e2c3179c8da2018b76901ef34c26ef0d28b65729dd5c',
            'legacy seed archive hash mismatch')
    payload = json.loads(raw)
    return {m: [payload['phase_gates'][str(m)]['fixed_inverse_phase_word']]
            for m in range(3, max_m+1)}


class CertifiedNativeWord:
    """Literal apply_word adapter; exact static denominator retains all modes."""
    def __init__(self, certificate):
        self.verification = verify_certificate(certificate)
        self.word = normalize_word(certificate['word'])
        self.inverse_phase_word = self.word
        self.dim = DIM
        self.h4_count = sum(g[0] == 'h4' for g in self.word)
        self.neg_count = sum(g[0] == 'neg' for g in self.word)
        self.sign_count = self.neg_count
        self.swap_count = sum(g[0] == 'swap' for g in self.word)
        self.den = 1 << self.h4_count

    def apply_numer(self, vector, inverse=False):
        require(len(vector) == DIM, 'full carrier required')
        nums, den = fixed.apply_word(vector, 1, self.word, inverse=inverse)
        require(self.den % den == 0, 'word denominator bound')
        return [x*(self.den//den) for x in nums]
