"""An exact time/row-storage tradeoff for the actual native prefix instrument.

The checkpoint is an earlier unnormalized state. Queries above it recurse
without memoizing an entire present state. Arithmetic/certificate caches are
accounted separately and are NOT covered by the row-storage bound.
"""
from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / 'gram_research'))
from single_walker import PointRowOracle, RawRow, QueryBudgetExhausted, normalize_row


class CheckpointRowOracle(PointRowOracle):
    def __init__(self, program, history=(), *, query_budget=100000,
                 checkpoint_depth_cap=None):
        super().__init__(program, history, query_budget=query_budget)
        if checkpoint_depth_cap is not None and (
                type(checkpoint_depth_cap) is not int or checkpoint_depth_cap < 0):
            raise ValueError('nonnegative checkpoint depth cap required')
        self.checkpoint_depth_cap = checkpoint_depth_cap
        self.checkpoint_depth = 0
        self.checkpoint = {1: RawRow(tuple(int(j == 0) for j in range(self.dim)), 1)}
        self.stats.update({'point_node_visits': 0, 'checkpoint_row_inputs': 0,
            'checkpoint_base_lookups': 0, 'checkpoint_advances': 0,
            'peak_checkpoint_rows': 1, 'peak_checkpoint_build_live_rows': 1,
            'peak_recursion_frames': 0, 'old_depth_queries_from_initial_state': 0,
            'operation_units_used': 0, 'root_query_calls': 0})

    def _charge(self, kind):
        if self.stats['operation_units_used'] >= self.query_budget:
            raise QueryBudgetExhausted('checkpoint oracle operation budget reached')
        self.stats['operation_units_used'] += 1
        self.stats[kind] += 1

    def _track_row(self, row):
        self.stats['max_numerator_bits'] = max(self.stats['max_numerator_bits'],
            max((abs(x).bit_length() for x in row.values), default=0))
        self.stats['max_denominator_bits'] = max(self.stats['max_denominator_bits'],
                                                row.den.bit_length())
        return row

    def _advance_checkpoint(self, target):
        while self.checkpoint_depth < target:
            i = self.checkpoint_depth
            future = {}
            # The old checkpoint remains intact until a complete advance. An
            # interrupted attempt may redo work, which is charged again.
            for label, row in self.checkpoint.items():
                self._charge('checkpoint_row_inputs')
                moved = self.apply_feedback(i, row)
                for destination, contribution, sign in (
                    (label, row, 1),
                    (self.program.tables[i][label], moved, 1 if self.history[i] == 0 else -1)):
                    contribution = normalize_row(tuple(sign*x for x in contribution.values),
                                                 contribution.den << 1)
                    if destination in future:
                        contribution = self.combine(future[destination], contribution, halve=False)
                    self._track_row(contribution)
                    if any(contribution.values):
                        future[destination] = contribution
                    else:
                        future.pop(destination, None)
                self.stats['peak_checkpoint_build_live_rows'] = max(
                    self.stats['peak_checkpoint_build_live_rows'], len(self.checkpoint)+len(future))
            self.checkpoint = future
            self.checkpoint_depth += 1
            self.stats['checkpoint_advances'] += 1
            self.stats['peak_checkpoint_rows'] = max(self.stats['peak_checkpoint_rows'], len(future))

    def query(self, depth, label):
        if (type(depth) is not int or not 0 <= depth <= len(self.history)
                or type(label) is not int or not 0 <= label < (1 << (self.program.N-1).bit_length())):
            raise ValueError('query requires retained prefix and carrier label')
        self.stats['query_requests'] += 1
        self.stats['root_query_calls'] += 1
        target = depth // 2
        if self.checkpoint_depth_cap is not None:
            target = min(target, self.checkpoint_depth_cap)
        self._advance_checkpoint(target)
        base_depth = self.checkpoint_depth
        base = self.checkpoint
        if depth < base_depth:
            self.stats['old_depth_queries_from_initial_state'] += 1
            base_depth = 0
            base = {1: RawRow(tuple(int(j == 0) for j in range(self.dim)), 1)}
        zero = RawRow((0,) * self.dim, 1)

        def visit(j, z, frames):
            self._charge('point_node_visits')
            self.stats['peak_recursion_frames'] = max(self.stats['peak_recursion_frames'], frames)
            if j == base_depth:
                self.stats['checkpoint_base_lookups'] += 1
                return base.get(z, zero)
            i = j-1
            predecessor = self.inverse_table(i)[z]
            left = visit(i, z, frames+1)
            right = self.apply_feedback(i, visit(i, predecessor, frames+1))
            self.stats['recurrence_queries'] += 1
            return self._track_row(self.combine(left, right, 1 if self.history[i] == 0 else -1))

        return visit(depth, label, 1)

    def report(self):
        result = super().report()
        result.update({'oracle_type': 'EARLIER_PREFIX_CHECKPOINT_WITH_BACKWARD_POINT_RECURSION',
            'checkpoint_depth': self.checkpoint_depth,
            'checkpoint_depth_cap': self.checkpoint_depth_cap,
            'checkpoint_rows': len(self.checkpoint),
            'checkpoint_row_scalar_slots': len(self.checkpoint)*self.dim,
            'query_budget_unit': 'recursive node visit or checkpoint input row',
            'whole_current_state_enumerated_as_algorithm_step': False,
            'earlier_prefix_state_materialized': True,
            'total_memory_bound_claimed': False,
            'point_query_memoization': False,
            'certificates_and_modular_column_caches_are_additional_memory': True})
        return result

    def evidence(self):
        result = super().evidence()
        result.update({'checkpoint_rows': [
            {'label': label, 'values': row.values, 'den': row.den}
            for label, row in sorted(self.checkpoint.items())],
            'checkpoint_oracle_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
        return result
