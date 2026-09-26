"""Bounded implicit correlation queries of the actual native instrument.

No work-amplitude map is constructed. Gamma includes raw amplitude denominators.
Only actual native word quotients and the signed positive-path observer are used.
This prototype does not assert a polynomial bound on its query cache.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parent
PACKAGE = ROOT.parents[1]
for p in (PACKAGE / 'new_word_compiler', ROOT.parent / 'streaming'):
    sys.path.insert(0, str(p))
from certified_word_compiler import PositivePathObserver
from lazy_streaming import LazyStreamingProgram


@dataclass(frozen=True)
class Correlation:
    rows: tuple
    den: int


class QueryBudgetExhausted(RuntimeError):
    pass


def normalized(rows, den):
    rows = tuple(tuple(row) for row in rows)
    if den <= 0 or den & (den-1):
        raise ValueError('positive dyadic correlation denominator required')
    if not any(v for row in rows for v in row):
        return Correlation(rows, 1)
    while den > 1 and not any(v & 1 for row in rows for v in row):
        rows = tuple(tuple(v >> 1 for v in row) for row in rows)
        den >>= 1
    return Correlation(rows, den)


def transpose(matrix):
    return Correlation(tuple(zip(*matrix.rows)), matrix.den)


class GramSampler:
    """Append-only chosen history and memo(depth, observed residue) queries.

    The supplied program has already admitted the full native bank, optional
    exact codec, actual two-H4 identity, and typed lazy modular permutations.
    This class never calls initial(), branches(), or creates labelled amplitudes.
    A query budget interruption retains this object's completed cache; durable
    cross-process cursor export is not implemented by this bounded prototype.
    """
    def __init__(self, program, *, query_budget=1000):
        if not isinstance(program, LazyStreamingProgram):
            raise ValueError('actual admitted lazy streaming program required')
        if type(query_budget) is not int or query_budget < 0:
            raise ValueError('nonnegative query budget required')
        self.program = program
        self.dim = program.dim
        self.history = ()
        self.cache = {}
        self.query_budget = query_budget
        self.observer = PositivePathObserver()
        self.observation_count = 0
        self.tables = list(program.lazy_factory.tables.values())
        self.stats = {'query_requests': 0, 'query_cache_hits': 0,
                      'base_queries': 0, 'recurrence_queries': 0,
                      'native_phase_vector_applications': 0,
                      'zero_matrix_native_actions_skipped': 0,
                      'single_term_wiring_observations': 0,
                      'zero_wiring_observations': 0,
                      'peak_cached_matrix_scalar_slots': 0,
                      'max_correlation_numerator_bits': 0,
                      'max_correlation_denominator_bits': 0}

    def _sum(self, name, values):
        values = tuple(F(v) for v in values if v)
        if not values:
            self.stats['zero_wiring_observations'] += 1
            return F(0)
        if len(values) == 1:
            self.stats['single_term_wiring_observations'] += 1
            return values[0]
        self.observation_count += 1
        return self.observer.evaluate(f'{self.observation_count}:{name}',
                                      tuple((v,) for v in values))

    def _gates(self, depth):
        return tuple(self.program.bank[depth-c+1]
                     for c in range(depth) if self.history[c])

    def _left(self, matrix, gates):
        if not gates:
            return matrix
        if not any(v for row in matrix.rows for v in row):
            self.stats['zero_matrix_native_actions_skipped'] += 1
            return matrix
        columns = [tuple(row[j] for row in matrix.rows) for j in range(self.dim)]
        den = matrix.den
        for gate in gates:
            columns = [tuple(gate.apply_numer(column)) for column in columns]
            self.stats['native_phase_vector_applications'] += self.dim
            den *= gate.den
        return normalized(tuple(zip(*columns)), den)

    def _right_transpose(self, matrix, gates):
        # (T Gamma^T)^T = Gamma T^T; factor order inside T is unchanged.
        return transpose(self._left(transpose(matrix), gates))

    def _combine(self, terms):
        den = max(matrix.den for _, matrix in terms)
        aligned = []
        for sign, matrix in terms:
            shift = den.bit_length()-matrix.den.bit_length()
            aligned.append(tuple(tuple(sign*(v << shift) for v in row)
                                 for row in matrix.rows))
        rows = []
        for i in range(self.dim):
            row = []
            for j in range(self.dim):
                value = self._sum('gram_entry', (x[i][j] for x in aligned))
                if value.denominator != 1:
                    raise AssertionError('aligned correlation sum is not integral')
                row.append(value.numerator)
            rows.append(tuple(row))
        # 1/4 is the exact product of the inherited two child coefficients.
        return normalized(rows, den << 2)

    def _retain(self, key, matrix):
        if len(self.cache) >= self.query_budget:
            raise QueryBudgetExhausted('Gram query budget exhausted; cache retained in this object')
        self.cache[key] = matrix
        self.stats['peak_cached_matrix_scalar_slots'] = max(
            self.stats['peak_cached_matrix_scalar_slots'], len(self.cache)*self.dim*self.dim)
        self.stats['max_correlation_numerator_bits'] = max(
            self.stats['max_correlation_numerator_bits'],
            max((abs(v).bit_length() for row in matrix.rows for v in row), default=0))
        self.stats['max_correlation_denominator_bits'] = max(
            self.stats['max_correlation_denominator_bits'], matrix.den.bit_length())
        return matrix

    def gamma(self, depth, residue):
        if (type(depth) is not int or not 0 <= depth <= len(self.history)
                or type(residue) is not int or not 1 <= residue < self.program.N):
            raise ValueError('query must refer to a retained prefix and an observed unit residue')
        # The public entry accepts residues only on the caller's unit-domain
        # contract. Internal queries originate at 1/b and typed permutations.
        self.stats['query_requests'] += 1
        key = (depth, residue)
        if key in self.cache:
            self.stats['query_cache_hits'] += 1
            return self.cache[key]
        if len(self.cache) >= self.query_budget:
            raise QueryBudgetExhausted('Gram query budget exhausted; cache retained in this object')
        if depth == 0:
            self.stats['base_queries'] += 1
            initial = [0]*self.program.full_dim
            initial[0] = 1
            row = tuple(initial) if self.program.codec is None else self.program.codec.encode(initial)
            # Products of the exact basis entries are structural 0/1 wiring.
            rows = tuple(tuple(int(residue == 1 and x == 1 and y == 1)
                               for y in row) for x in row)
            return self._retain(key, Correlation(rows, 1))
        i = depth-1
        table = self.program.tables[i]
        inverse = table.inverse()
        if not any(inverse is item for item in self.tables):
            self.tables.append(inverse)
        minus, plus = inverse[residue], table[residue]
        center = self.gamma(i, residue)
        lower = self.gamma(i, minus)
        upper = self.gamma(i, plus)
        gates = self._gates(i)
        sign = 1 if self.history[i] == 0 else -1
        term_lower = self._right_transpose(lower, gates)
        term_upper = self._left(upper, gates)
        term_center = self._left(self._right_transpose(center, gates), gates)
        result = self._combine(((1, center), (sign, term_lower),
                                (sign, term_upper), (1, term_center)))
        self.stats['recurrence_queries'] += 1
        return self._retain(key, result)

    def _trace(self, matrix, label):
        return self._sum(label, (F(matrix.rows[j][j], matrix.den) for j in range(self.dim)))

    def mass(self):
        return self._trace(self.gamma(len(self.history), 1), 'parent_mass')

    def probabilities(self):
        depth = len(self.history)
        if depth >= self.program.t:
            raise ValueError('terminal history has no next bit')
        parent = self.mass()
        if parent <= 0:
            raise ValueError('zero mass prefix cannot be conditioned')
        shifted = self.gamma(depth, self.program.modular_powers[depth])
        cross = self._trace(self._left(shifted, self._gates(depth)), 'collision_trace')
        children = tuple(self._sum('child_mass', (parent, sign*cross))/2
                         for sign in (1, -1))
        if min(children) < 0 or sum(children) != parent:
            raise AssertionError('Gram completeness/positivity failed')
        return {'parent_mass': parent, 'cross': cross,
                'child_masses': children, 'probabilities': tuple(x/parent for x in children)}

    def advance(self, bit):
        if type(bit) is not int or bit not in (0, 1):
            raise ValueError('one exact classical bit required')
        plan = self.probabilities()
        if plan['child_masses'][bit] <= 0:
            raise ValueError('selected child has zero probability')
        self.history += (bit,)
        actual = self.mass()
        if actual != plan['child_masses'][bit]:
            raise AssertionError('correlation recurrence disagrees with selected mass')
        return plan

    def report(self):
        table_metrics = [table.report_metrics() for table in self.tables]
        return {**self.stats, 'history': self.history, 'dimension': self.dim,
                'distinct_queries': len(self.cache),
                'cached_matrix_scalar_slots': len(self.cache)*self.dim*self.dim,
                'query_keys': sorted(self.cache),
                'actual_positive_path_observations': len(self.observer.operations),
                'typed_modular_tables': table_metrics,
                'adder_digit_replays': sum(x['setup_adder_digit_replays']+x['column_adder_digit_replays']
                                          for x in table_metrics),
                'computed_modular_columns': sum(x['computed_columns'] for x in table_metrics),
                'work_amplitude_map_constructed': False,
                'query_budget': self.query_budget,
                'durable_cross_process_cursor_claimed': False}

    def evidence(self):
        return {'report': self.report(), 'observer_operations': self.observer.operations,
                'correlations': [{'depth': k[0], 'residue': k[1],
                                  'numerator_rows': v.rows, 'denominator': v.den}
                                 for k, v in sorted(self.cache.items())],
                'typed_modular_certificates': [table.export_certificate() for table in self.tables],
                'phase_bindings': self.program.phase_bindings,
                'codec_binding': self.program.codec_binding,
                'native_two_H4_binding': self.program.h4_binding,
                'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
