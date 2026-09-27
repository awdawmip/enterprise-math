"""A coherent, fixed-path-list native suffix estimator with point-row access.

The stored raw prefix is complete. Its suffix is never materialized here.
Random paths are fixed before queries and are never chosen using a target label.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
from types import MappingProxyType
import hashlib
import sys

ROOT = Path(__file__).resolve().parent
RESEARCH = ROOT.parents[1] / 'sep27-qft-research'
sys.path.insert(0, str(RESEARCH / 'gram_research'))
from single_walker import PointRowOracle, RawRow, normalize_row
from lazy_modular import digest


@dataclass(frozen=True)
class MeanRow:
    values: tuple
    den: int


def checked_histories(prefix_history, target_history):
    prefix_history, target_history = tuple(prefix_history), tuple(target_history)
    if (any(type(bit) is not int or bit not in (0, 1) for bit in target_history)
            or any(type(bit) is not int or bit not in (0, 1) for bit in prefix_history)
            or target_history[:len(prefix_history)] != prefix_history):
        raise ValueError('fixed complete target history must extend its prefix')
    return prefix_history, target_history


def draw_path_list(prefix_history, target_history, sample_count, rng):
    """Draw the entire auxiliary sample list before any row-query label exists.

    This is an exact software random-source interface, not physical randomness.
    An incomplete list is never silently promoted into an unbiased estimator.
    """
    prefix_history, target_history = checked_histories(prefix_history, target_history)
    if type(sample_count) is not int or sample_count < 1:
        raise ValueError('positive sample count required')
    ell = len(target_history)-len(prefix_history)
    paths, pending, draws = [], [], []
    try:
        for _ in range(sample_count):
            pending = []
            for _ in range(ell):
                bit = rng.randrange(2)
                if type(bit) is not int or bit not in (0, 1):
                    raise ValueError('random source returned a non-bit')
                pending.append(bit)
                draws.append(bit)
            paths.append(tuple(pending))
            pending = []
    except (StopIteration, EOFError):
        return {'status': 'INCOMPLETE_PATH_RANDOM_SOURCE', 'paths': tuple(paths),
            'pending_path': tuple(pending), 'drawn_bits': tuple(draws),
            'requested_sample_count': sample_count, 'suffix_length': ell,
            'prefix_history': prefix_history, 'target_history': target_history,
            'estimator_ready': False}
    return {'status': 'COMPLETE_PATH_LIST', 'paths': tuple(paths), 'drawn_bits': tuple(draws),
        'requested_sample_count': sample_count, 'suffix_length': ell,
        'prefix_history': prefix_history, 'target_history': target_history,
        'estimator_ready': True,
        'random_contract': 'independent conditional-uniform bits before all label queries',
        'query_label_or_latent_seed_argument': False}


class SuffixPathEstimator:
    """E_e Z_e = actual v_h, with fixed complete paths defining one function.

    Explicit paths are accepted for exact finite fixtures. An iid estimator
    interpretation additionally needs the declared independent-uniform source;
    passing a hand-picked path list never certifies that statistical premise.
    """
    def __init__(self, program, prefix_state, prefix_den, prefix_history,
                 target_history, paths, *, construction_receipt=None):
        prefix_history, target_history = checked_histories(prefix_history, target_history)
        if len(target_history) > program.t:
            raise ValueError('target exceeds admitted native program')
        if type(prefix_den) is not int or prefix_den <= 0 or prefix_den & (prefix_den-1):
            raise ValueError('raw positive dyadic prefix denominator required')
        ell = len(target_history)-len(prefix_history)
        paths = tuple(tuple(path) for path in paths)
        if not paths or any(len(path) != ell or any(type(b) is not int or b not in (0, 1)
                                                   for b in path) for path in paths):
            raise ValueError('nonempty complete fixed suffix path list required')
        rows = {}
        for key, row in prefix_state.items():
            if (type(key) is not tuple or len(key) != 3 or key[0] != 0 or key[2] != 0
                    or type(key[1]) is not int or not 0 <= key[1] < (1 << (program.N-1).bit_length())
                    or len(row) != program.dim or any(type(v) is not int for v in row)):
                raise ValueError('complete raw native prefix at a round boundary required')
            if any(row):
                rows[key[1]] = tuple(row)
        if not rows:
            raise ValueError('nonzero raw prefix required')
        if construction_receipt is not None:
            if (construction_receipt.get('status') != 'COMPLETE_PATH_LIST'
                    or tuple(map(tuple, construction_receipt['paths'])) != paths
                    or tuple(construction_receipt['prefix_history']) != prefix_history
                    or tuple(construction_receipt['target_history']) != target_history):
                raise ValueError('path-construction receipt is incomplete or belongs to another function')
        self.program = program
        self.prefix_history, self.target_history = prefix_history, target_history
        self.k, self.i, self.ell = len(prefix_history), len(target_history), ell
        self.prefix_rows = MappingProxyType(rows)
        self.prefix_den = prefix_den
        self.paths = paths
        self.construction_receipt = construction_receipt
        self.helper = PointRowOracle(program, target_history)
        self.descriptor = {'N': program.N, 'a': program.a, 't': program.t, 'dim': program.dim,
            'prefix_history': prefix_history, 'target_history': target_history,
            'prefix_denominator': prefix_den, 'prefix_rows': sorted(rows.items()), 'paths': paths,
            'construction': construction_receipt if construction_receipt is not None
                            else {'status': 'EXPLICIT_FINITE_FIXTURE_NOT_IID_CLAIM'}}
        self.function_sha256 = digest(self.descriptor)
        self.stats = {'point_path_requests': 0, 'point_mean_requests': 0,
            'typed_inverse_column_requests': 0, 'selected_suffix_factors_applied': 0,
            'prefix_lookup_zero_rows': 0, 'mean_signed_coordinate_observations': 0,
            'max_path_numerator_bits': 0, 'max_path_denominator_bits': 0,
            'max_mean_numerator_bits': 0, 'max_mean_denominator_bits': 0}
        self.query_receipts = []

    def _check_fixed(self):
        if (self.paths != tuple(map(tuple, self.descriptor['paths']))
                or self.target_history != tuple(self.descriptor['target_history'])
                or self.prefix_history != tuple(self.descriptor['prefix_history'])
                or self.helper.history != self.target_history):
            raise ValueError('path list/history changed after the estimator was fixed')

    def point_path(self, path_index, target_label):
        self._check_fixed()
        if (type(path_index) is not int or not 0 <= path_index < len(self.paths)
                or type(target_label) is not int
                or not 0 <= target_label < (1 << (self.program.N-1).bit_length())):
            raise ValueError('fixed path index and carrier query label required')
        self.stats['point_path_requests'] += 1
        path = self.paths[path_index]
        source = target_label
        inverse_steps = []
        for offset in reversed(range(self.ell)):
            if path[offset]:
                depth = self.k+offset
                before = source
                source = self.helper.inverse_table(depth)[source]
                inverse_steps.append({'round': depth, 'input': before, 'output': source})
                self.stats['typed_inverse_column_requests'] += 1
        values = self.prefix_rows.get(source)
        if values is None:
            row = RawRow((0,)*self.program.dim, 1)
            self.stats['prefix_lookup_zero_rows'] += 1
        else:
            row = normalize_row(values, self.prefix_den)
        for offset, selected in enumerate(path):
            if selected:
                depth = self.k+offset
                row = self.helper.apply_feedback(depth, row)
                if self.target_history[depth]:
                    # Exact signed-permutation wiring; no modulus/absolute
                    # value discards interference in a complete coordinate.
                    row = RawRow(tuple(-value for value in row.values), row.den)
                self.stats['selected_suffix_factors_applied'] += 1
        self.stats['max_path_numerator_bits'] = max(self.stats['max_path_numerator_bits'],
            max((abs(value).bit_length() for value in row.values), default=0))
        self.stats['max_path_denominator_bits'] = max(self.stats['max_path_denominator_bits'], row.den.bit_length())
        self.query_receipts.append({'path_index': path_index, 'target_label': target_label,
            'source_label': source, 'typed_inverse_steps': inverse_steps,
            'row_values': row.values, 'row_denominator': row.den,
            'function_sha256': self.function_sha256})
        return row

    def point_mean(self, target_label):
        self._check_fixed()
        self.stats['point_mean_requests'] += 1
        rows = tuple(self.point_path(j, target_label) for j in range(len(self.paths)))
        common = max(row.den for row in rows)
        values = []
        for coordinate in range(self.program.dim):
            terms = tuple(((row.values[coordinate] << (common.bit_length()-row.den.bit_length())),)
                          for row in rows)
            value = self.helper.observe('fixed_path_mean_signed_coordinate', terms)
            if value.denominator != 1:
                raise AssertionError('aligned path mean numerator is not integral')
            values.append(value.numerator)
        self.stats['mean_signed_coordinate_observations'] += self.program.dim
        # General m need not be a power of two. This is a rational observer
        # of a coherent function, not a new dyadic native propagator.
        den = common*len(self.paths)
        if not any(values):
            den = 1
        self.stats['max_mean_numerator_bits'] = max(self.stats['max_mean_numerator_bits'],
            max((abs(value).bit_length() for value in values), default=0))
        self.stats['max_mean_denominator_bits'] = max(self.stats['max_mean_denominator_bits'], den.bit_length())
        return MeanRow(tuple(values), den)

    def report(self):
        helper = self.helper.report()
        return {**self.stats, 'dimension': self.program.dim, 'prefix_depth': self.k,
            'target_depth': self.i, 'suffix_length': self.ell, 'sample_count': len(self.paths),
            'stored_prefix_rows': len(self.prefix_rows),
            'stored_prefix_scalar_slots': len(self.prefix_rows)*self.program.dim,
            'fixed_path_bit_slots': len(self.paths)*self.ell,
            'construction_random_bit_draws': (len(self.construction_receipt['drawn_bits'])
                if self.construction_receipt is not None else 0),
            'path_list_has_declared_uniform_source_contract': self.construction_receipt is not None,
            'function_sha256': self.function_sha256,
            'helper': helper, 'suffix_amplitude_table_constructed': False,
            'random_paths_resampled_per_query': False,
            'full_prefix_construction_and_certificate_cost_excluded': True,
            'typed_table_costs_are_cumulative_program_costs': True,
            'effective_approximate_sampling_claimed': False}

    def evidence(self, *, include_shared_bindings=True):
        result = {'descriptor': self.descriptor, 'function_sha256': self.function_sha256,
            'report': self.report(), 'query_receipts': list(self.query_receipts),
            'actual_observer_operations': list(self.helper.observer.operations),
            'shared_phase_binding_sha256': digest(self.program.phase_bindings),
            'shared_modular_certificate_sha256': [table.certificate_sha256 for table in self.helper.tables],
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
        if include_shared_bindings:
            result['actual_helper_evidence'] = self.helper.evidence()
        else:
            result['shared_binding_scope'] = 'caller must retain full actual native and typed-column certificates separately'
        return result
