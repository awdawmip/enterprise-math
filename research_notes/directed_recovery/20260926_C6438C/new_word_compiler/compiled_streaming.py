"""Complete-carrier native-word adapter for the existing streaming instrument.

The integer matrix cache is derived only from actual apply_word columns.
Certified compiler-result validation and program construction are kept separate
from native execution, so a partial bank cannot silently become an instrument.
"""
from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent
for directory in ('integration', 'sparse'):
    sys.path.insert(0, str(ROOT.parent / directory))
from general_streaming import GeneralStreamingProgram
from sparse_modular import sparse_modular_columns
from stage80.fixed_phase import apply_word
from stage79.phase_compiler import encode


def normalized_word(word, dim):
    result = tuple(tuple(gate) for gate in word)
    for gate in result:
        if not gate or gate[0] not in ('h4', 'neg', 'swap'):
            raise ValueError('only actual native h4/neg/swap words are accepted')
        needed = {'h4': 4, 'neg': 1, 'swap': 2}[gate[0]]
        if len(gate) != needed+1 or len(set(gate[1:])) != needed:
            raise ValueError('native gate needs distinct legal coordinate labels')
        if any(not isinstance(i, int) or isinstance(i, bool) or not 0 <= i < dim
               for i in gate[1:]):
            raise ValueError('native word coordinates must lie in the complete carrier')
    return result


@lru_cache(maxsize=64)
def replay_complete_word(dim, word):
    """Actual forward/inverse columns, with one common dyadic denominator."""
    forward, backward = [], []
    den = 1
    for j in range(dim):
        basis = [int(i == j) for i in range(dim)]
        v, d = apply_word(basis, 1, word)
        inverse_v, inverse_d = apply_word(basis, 1, word, inverse=True)
        recovered, recovered_d = apply_word(v, d, word, inverse=True)
        if recovered != basis or recovered_d != 1:
            raise ValueError('actual native inverse did not restore the complete basis')
        if d <= 0 or d & (d-1) or inverse_d <= 0 or inverse_d & (inverse_d-1):
            raise ValueError('native exact words must have dyadic column denominators')
        forward.append((tuple(v), d)); backward.append((tuple(inverse_v), inverse_d))
        den = max(den, d, inverse_d)
    columns = tuple(tuple(x*(den//d) for x in col) for col, d in forward)
    inverse_columns = tuple(tuple(x*(den//d) for x in col) for col, d in backward)
    # Inverse is the transpose and all complete columns are orthonormal.
    for i in range(dim):
        for j in range(dim):
            if inverse_columns[j][i] != columns[i][j]:
                raise ValueError('actual inverse columns differ from the transpose')
            dot = sum(a*b for a, b in zip(columns[i], columns[j]) if a and b)
            if dot != (den*den if i == j else 0):
                raise ValueError('native complete-column orthogonality failed')
    payload = {'dim': dim, 'word': word, 'denominator': den,
               'forward_columns': columns, 'inverse_columns': inverse_columns}
    digest = hashlib.sha256(json.dumps(payload, sort_keys=True,
        separators=(',', ':')).encode()).hexdigest()
    return den, columns, inverse_columns, digest


class CompleteNativeWord:
    """Integer quotient of one actually replayed complete native word."""
    def __init__(self, word, dim=61):
        if not isinstance(dim, int) or isinstance(dim, bool) or dim < 4:
            raise ValueError('integer complete carrier dimension >=4 required')
        self.dim = dim
        self.inverse_phase_word = normalized_word(word, dim)
        self.den, self.columns, self.inverse_columns, self.columns_sha256 = replay_complete_word(
            dim, self.inverse_phase_word)
        self.h4_count = sum(g[0] == 'h4' for g in self.inverse_phase_word)
        self.sign_count = sum(g[0] == 'neg' for g in self.inverse_phase_word)
        self.swap_count = sum(g[0] == 'swap' for g in self.inverse_phase_word)
        self._forward_nonzero = tuple(tuple((i, x) for i, x in enumerate(col) if x)
                                      for col in self.columns)
        self._inverse_nonzero = tuple(tuple((i, x) for i, x in enumerate(col) if x)
                                      for col in self.inverse_columns)

    def apply_numer(self, values, inverse=False):
        if len(values) != self.dim:
            raise ValueError('all residual input coordinates must be retained')
        if any(not isinstance(x, int) or isinstance(x, bool) for x in values):
            raise ValueError('integer numerator vector required')
        result = [0]*self.dim
        columns = self._inverse_nonzero if inverse else self._forward_nonzero
        for source, value in enumerate(values):
            if value:
                for target, coefficient in columns[source]:
                    result[target] += coefficient*value
        return result

    def binding_record(self):
        return {'dim': self.dim, 'denominator': self.den,
                'word': self.inverse_phase_word,
                'actual_complete_columns_sha256': self.columns_sha256,
                'complete_forward_columns': self.dim,
                'complete_inverse_columns': self.dim,
                'all_columns_orthonormal': True,
                'all_inverse_columns_equal_transpose': True,
                'H4_count': self.h4_count, 'sign_count': self.sign_count,
                'swap_count': self.swap_count,
                'scope': 'actual full-word quotient, including arbitrary retained residual input'}


def rational(value):
    if isinstance(value, bool) or not isinstance(value, (int, str, F)):
        raise ValueError('exact integer/Fraction/rational-string value required')
    return F(value)


def bank_from_compilation(compilation, *, t=None, epsilon=None):
    """Turn a complete certified result into a replayed word bank or PARTIAL.

    A partial result is a normal resumable outcome. It never constructs a word
    bank, a modular permutation, or a program from its completed subset.
    """
    status = compilation.get('status')
    if status == 'PARTIAL':
        return {'status': 'PARTIAL', 'reason': 'PHASE_COMPILATION_PARTIAL',
                'bank': None, 'dim': None, 'error_certificate': None,
                'cursor': compilation.get('cursor'), 'compilation': compilation}
    if status != 'CERTIFIED':
        raise ValueError('compiler must explicitly return CERTIFIED or PARTIAL')
    if t is None:
        t = compilation.get('t')
    if not isinstance(t, int) or isinstance(t, bool) or t < 2 or t % 2:
        raise ValueError('positive even control width required')
    if compilation.get('t', t) != t:
        raise ValueError('compiled phase bank is bound to a different width')
    if epsilon is None:
        epsilon = compilation.get('epsilon', compilation.get('requested_epsilon'))
    epsilon = rational(epsilon)
    if not 0 < epsilon <= 1:
        raise ValueError('requested single-instrument epsilon must lie in (0,1]')
    for name in ('epsilon', 'requested_epsilon'):
        if name in compilation and rational(compilation[name]) != epsilon:
            raise ValueError('compiler result belongs to a different requested epsilon')
    phases = compilation.get('phases', {})
    from certified_word_compiler import verify_phase_record
    bank, rows, bindings = {}, [], {}
    total = F(0)
    for m in range(2, t+1):
        record = phases.get(str(m), phases.get(m))
        if not isinstance(record, dict) or record.get('status') != 'CERTIFIED':
            raise ValueError('CERTIFIED bank is missing a complete certified phase')
        if record.get('phase_index') != m or record.get('dim') != 61:
            raise ValueError('phase target or full 61-mode carrier does not match')
        if not isinstance(record.get('certificate'), dict) or not record['certificate']:
            raise ValueError('a successful phase must retain its complete certificate')
        # This verifier binds record word/m/dim/bound/hash to its certificate,
        # then forces actual complete-column, root-probe and strict-margin
        # replay. A nonempty dictionary or a claimed numerical bound is not
        # treated as a scientific certificate.
        verification = verify_phase_record(record)
        if verification.get('status') != 'VERIFIED':
            raise ValueError('phase certificate did not pass complete scientific replay')
        bound = rational(record['operator_error_bound'])
        if bound < 0 or (m == 2 and bound != 0):
            raise ValueError('invalid exact-quarter or phase error bound')
        word = CompleteNativeWord(record['word'], 61)
        if m == 2:
            exact_quarter = CompleteNativeWord((('swap', 0, 1), ('neg', 1)), 61)
            if word.columns != exact_quarter.columns or word.den != exact_quarter.den:
                raise ValueError('zero-error quarter turn must be the complete exact native phase')
        bank[m] = word
        occurrences = t-m+1
        contribution = occurrences*bound
        total += contribution
        rows.append({'m': m, 'occurrences': occurrences,
                     'phase_operator_error_bound': bound,
                     'weighted_error_bound': contribution})
        binding = word.binding_record()
        binding['compiler_certificate_replay'] = verification
        binding['compiler_record_sha256'] = hashlib.sha256(json.dumps(
            encode(record), sort_keys=True, separators=(',', ':')).encode()).hexdigest()
        bindings[str(m)] = binding
    declared = rational(compilation['occurrence_weighted_error_bound'])
    if declared != total or total > epsilon:
        raise ValueError('whole phase schedule does not meet its stated error budget')
    error_certificate = {
        't': t, 'dim': 61, 'requested_epsilon': epsilon,
        'phase_occurrence_rows': rows, 'telescoping_sum': total,
        'operator_norm_bound': total, 'terminal_TV_bound': min(F(1), total),
        'all_residual_modes_retained': True,
        'scope': 'one complete terminal instrument and its fixed postprocessing; full-retry transcript requires a separate sum budget'}
    return {'status': 'CERTIFIED', 'bank': bank, 'dim': 61,
            'error_certificate': error_certificate,
            'word_bindings': bindings, 'compilation': compilation,
            'cursor': compilation.get('cursor')}


def compile_bank(t, epsilon, **compiler_options):
    """Bounded certified compiler plus complete native-word streaming adapter."""
    from certified_word_compiler import compile_phase_bank
    compilation = compile_phase_bank(t, epsilon, **compiler_options)
    return bank_from_compilation(compilation, t=t, epsilon=epsilon)


def program_from_compilation(N, a, t, compilation, *, epsilon=None):
    result = bank_from_compilation(compilation, t=t, epsilon=epsilon)
    if result['status'] != 'CERTIFIED':
        return {**result, 'program': None}
    program = GeneralStreamingProgram(N, a, t, result['bank'], result['dim'],
                                      column_factory=sparse_modular_columns)
    program.compilation_error_certificate = result['error_certificate']
    return {**result, 'program': program}
