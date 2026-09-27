"""Exact two-carry contraction of complete native displacement correlations.

The admitted program and its methods stay trusted and fixed within one executor.
This is not a hostile-Python sandbox. No modular collision list is inferred here.
"""
from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parent
OLD = ROOT.parent / 'sep26-shor-general/optimization/collision_analysis'
sys.path.insert(0, str(OLD))
from gram_sampler import GramSampler, Correlation, normalized, transpose

GRAM_SHA = '468de944518fbc6afa81a17555676436376da63921a784c810ffe8fab3ca17e9'


def phase_snapshot(program):
    return (id(program), program.N, program.a, program.t, program.dim,
            program.full_dim, program.codec, program.modular_powers,
            tuple((k, id(g), g.dim, g.den, g.inverse_phase_word,
                   g.columns, g.inverse_columns,
                   getattr(g, '_forward_nonzero', None),
                   getattr(g, '_inverse_nonzero', None)) for k, g in sorted(program.bank.items())))


class CarryExecutor(GramSampler):
    """No coefficient cache: each query has two carry-indexed boundary matrices.

    Full observer receipts and optional caller-held returned matrices are additional
    memory. Complete alias discovery and source admission are separate costs.
    """
    def __init__(self, program, history):
        if hashlib.sha256((OLD/'gram_sampler.py').read_bytes()).hexdigest() != GRAM_SHA:
            raise ValueError('frozen inherited Gram source changed')
        super().__init__(program)
        history = tuple(history)
        if len(history) > program.t or any(type(x) is not int or x not in (0, 1) for x in history):
            raise ValueError('complete explicit classical prefix required')
        self.history = self._bound_history = history
        self._bound_phase = phase_snapshot(program)
        self._source_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        self.carry_stats = {'coefficient_queries': 0, 'positive_contractions': 0,
            'negative_transposes': 0, 'out_of_range_zero_queries': 0,
            'carry_digits': 0, 'allowed_local_tuples': 0,
            'peak_boundary_matrix_slots': 0,
            'observed_boundary_and_sum_max_numerator_bits': 0,
            'observed_boundary_and_sum_max_denominator_bits': 0,
            'program_binding_checks': 0}

    def _check(self):
        if self.history != self._bound_history or phase_snapshot(self.program) != self._bound_phase:
            raise ValueError('history or admitted program fields changed')
        self.carry_stats['program_binding_checks'] += 1

    def gamma(self, *args, **kwargs):
        raise ValueError('use certified aliases plus sum_coefficients; legacy recursion is disabled')

    mass = probabilities = advance = gamma

    def _zero(self):
        return Correlation(tuple((0,)*self.dim for _ in range(self.dim)), 1)

    def _seed(self):
        full = (1,)+(0,)*(self.program.full_dim-1)
        row = full if self.program.codec is None else self.program.codec.encode(full)
        return Correlation(tuple(tuple(int(x == 1 and y == 1) for y in row) for x in row), 1)

    def _observe_size(self, matrices):
        for matrix in matrices:
            self.carry_stats['observed_boundary_and_sum_max_numerator_bits'] = max(
                self.carry_stats['observed_boundary_and_sum_max_numerator_bits'],
                max((abs(v).bit_length() for row in matrix.rows for v in row), default=0))
            self.carry_stats['observed_boundary_and_sum_max_denominator_bits'] = max(
                self.carry_stats['observed_boundary_and_sum_max_denominator_bits'], matrix.den.bit_length())

    def coefficient(self, depth, displacement):
        self._check()
        if type(depth) is not int or not 0 <= depth <= len(self.history):
            raise ValueError('coefficient must refer to retained history prefix')
        if type(displacement) is not int:
            raise ValueError('integer displacement required; booleans excluded')
        self.carry_stats['coefficient_queries'] += 1
        length = 1 << depth
        if not -length < displacement < length:
            self.carry_stats['out_of_range_zero_queries'] += 1
            return self._zero()
        if displacement < 0:
            self.carry_stats['negative_transposes'] += 1
            return transpose(self.coefficient(depth, -displacement))
        self.carry_stats['positive_contractions'] += 1
        boundary = (self._seed(), self._zero())
        self._observe_size(boundary)
        self.carry_stats['peak_boundary_matrix_slots'] = max(
            self.carry_stats['peak_boundary_matrix_slots'], 2*self.dim*self.dim)
        for j in range(depth):
            digit = (displacement >> (depth-1-j)) & 1
            gates = self._gates(j)
            contributions = [[], []]
            for carry_out in (0, 1):
                for carry_in in (0, 1):
                    for x in (0, 1):
                        # Only finite address/carry wiring, not native amplitude arithmetic.
                        y = x + digit + carry_in - 2*carry_out
                        if y not in (0, 1):
                            continue
                        self.carry_stats['allowed_local_tuples'] += 1
                        matrix = boundary[carry_out]
                        if y:
                            matrix = self._right_transpose(matrix, gates)
                        if x:
                            matrix = self._left(matrix, gates)
                        sign = -1 if self.history[j] and x != y else 1
                        contributions[carry_in].append((sign, matrix))
            # The inherited actual signed observer aligns dyadic denominators,
            # sums complete entries, and divides by four exactly once per digit.
            boundary = tuple(self._combine(terms) if terms else self._zero()
                             for terms in contributions)
            self.carry_stats['carry_digits'] += 1
            self._observe_size(boundary)
        return boundary[0]

    def sum_coefficients(self, depth, displacements):
        """Sum a caller-supplied list; this method does NOT certify completeness."""
        self._check()
        if type(depth) is not int or not 0 <= depth <= len(self.history):
            raise ValueError('valid retained depth required')
        ds = tuple(displacements)
        if any(type(d) is not int or not -(1 << depth) < d < (1 << depth) for d in ds):
            raise ValueError('bounded integer displacement list required')
        if len(set(ds)) != len(ds):
            raise ValueError('duplicate displacement would duplicate coherent terms')
        answer = self._zero()
        for d in ds:
            # _combine includes 1/4 for one native recurrence. Here undo that
            # structural dyadic factor because these are coefficients to add.
            combined = self._combine(((1, answer), (1, self.coefficient(depth, d))))
            answer = normalized(tuple(tuple(v << 2 for v in row) for row in combined.rows), combined.den)
        self._observe_size((answer,))
        return answer

    def evidence(self):
        self._check()
        return {'carry_stats':dict(self.carry_stats), 'inherited_action_stats':dict(self.stats),
                'observer_operations':self.observer.operations,
                'history':self.history, 'dimension':self.dim,
                'phase_bindings':self.program.phase_bindings,
                'codec_binding':self.program.codec_binding,
                'source_sha256':self._source_sha, 'inherited_gram_sha256':GRAM_SHA,
                'coefficient_cache_entries':0,
                'inherited_legacy_cache_entries':len(self.cache),
                'coefficient_queries_counts_recursive_method_invocations':True,
                'observed_bit_widths_exclude_transients':True,
                'boundary_slots_exclude_terms_native_temporaries_and_receipts':True,
                'actual_coefficients_do_not_require_modular_queries':True,
                'arbitrary_python_monkeypatch_detection_claimed':False}
