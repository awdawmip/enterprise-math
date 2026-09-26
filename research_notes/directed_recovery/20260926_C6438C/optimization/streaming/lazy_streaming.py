"""Exact lazy modular and selected-child quotients of the native instrument.

Every feedback row is an ordered product of certified complete native-word
columns. The two-H4 contraction is bound to the actual native quartet.
No ideal phase, amplitude normalization, or residual projection occurs here.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction as F
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
PACKAGE = ROOT.parents[1]
for path in (PACKAGE / 'integration', PACKAGE / 'sparse',
             PACKAGE / 'new_word_compiler', ROOT.parent / 'lazy_modular'):
    sys.path.insert(0, str(path))
from general_streaming import GeneralStreamingProgram
from terminal_instrument import StreamingProgram as FrozenStreamingProgram
from stage80.fixed_phase import native_quartet, reduce_state, norm
from stage58.coupled_reader import choose
from compiled_streaming import CompleteNativeWord


def native_two_h4_binding():
    columns = native_quartet()
    matrix = tuple(tuple(next(sign for sign, dst in columns[src] if dst == out)
                         for src in range(4)) for out in range(4))
    coefficients = []
    for outcome in range(2):
        for spectator in range(2):
            row = []
            for arm in range(2):
                numerator = sum(matrix[outcome+2*spectator][arm+2*mid] *
                                matrix[arm+2*mid][0] for mid in range(2))
                expected = 0 if spectator else (2 if arm == 0 or outcome == 0 else -2)
                if numerator != expected:
                    raise AssertionError('actual two-H4 contraction differs')
                row.append(numerator)
            coefficients.append({'outcome': outcome, 'spectator': spectator,
                                 'arm_numerators_over_4': row})
    return {'actual_native_quartet_columns': columns,
            'two_H4_control_spectator_coefficients': coefficients,
            'spectator_zero_is_algebraic_not_reset': True}


def admit_native_bank(bank, t, dim):
    """Bind every supplied phase object to the actual complete native word.

    Error/target certification belongs to the caller's existing compiler.
    This boundary verifies the exact action needed by the mass identity.
    """
    if dim != 61:
        raise ValueError('this optimization profile retains the complete 61 modes')
    actual, certificates = {}, {}
    for m in range(2, t+1):
        gate = bank[m]
        if gate.dim != dim:
            raise ValueError('phase carrier mismatch')
        temporal_word = getattr(gate, 'inverse_phase_word',
                                (('swap', 0, 1), ('neg', 1)) if m == 2 else None)
        if temporal_word is None:
            raise ValueError('complete native word provenance required')
        word = CompleteNativeWord(temporal_word, dim)
        for j in range(dim):
            basis = [int(i == j) for i in range(dim)]
            supplied = gate.apply_numer(basis)
            native = word.apply_numer(basis)
            if len(supplied) != dim:
                raise ValueError('supplied native action omitted carrier coordinates')
            if any(x*word.den != y*gate.den for x, y in zip(supplied, native)):
                raise ValueError('supplied phase differs from its actual complete word')
        actual[m] = word
        certificates[str(m)] = word.binding_record()
    return actual, certificates


class LazyStreamingProgram(FrozenStreamingProgram):
    """Original branch evaluator with a proved lazy permutation interface."""
    def __init__(self, N, a, t, bank, dim, *, codec=None):
        from lazy_modular import LazyModularFactory, verify_lazy_permutation
        valid_int = lambda x: isinstance(x, int) and not isinstance(x, bool)
        if not valid_int(N) or N < 3 or not valid_int(a) or not 1 <= a < N:
            raise ValueError('legal N and modular base required')
        if not valid_int(t) or t < 2 or t % 2:
            raise ValueError('positive even t required')
        self.N, self.a, self.t, self.dim = N, a, t, dim
        self.full_dim = dim
        self.bank, self.phase_bindings = admit_native_bank(bank, t, dim)
        self.codec, self.codec_binding = None, None
        if codec is not None:
            sys.path.insert(0, str(ROOT.parent / 'carrier_codec'))
            from carrier_codec import ExactCarrierCodec, restrict_bank
            if type(codec) is not ExactCarrierCodec or codec.full_dim != dim:
                raise ValueError('explicit full-carrier codec required')
            self.codec, self.bank, self.codec_binding = restrict_bank(
                self.bank, indices=codec.indices, full_dim=dim)
            if self.codec != codec:
                raise AssertionError('verified codec differs from requested encoding')
            self.dim = codec.dim
        self.h4_binding = native_two_h4_binding()
        b = a
        powers, tables, proofs = [], [], []
        factory, verified = LazyModularFactory(), {}
        for _ in range(t):
            table = factory(N, b)
            if b not in verified:
                verified[b] = verify_lazy_permutation(table)
            proof = verified[b]
            if not isinstance(proof, dict) or proof.get('verified') is not True:
                raise ValueError('lazy permutation did not obtain its global certificate')
            if table.N != N or table.b != b or table.carrier_size != 1 << (N-1).bit_length():
                raise ValueError('lazy carrier or multiplier mismatch')
            powers.append(b); tables.append(table); proofs.append(proof)
            b = table[b]
        self.modular_powers = tuple(reversed(powers))
        self.tables = tuple(reversed(tables))
        self.lazy_factory = factory
        self.lazy_permutation_verifications = tuple(reversed(proofs))
        # These fields are the inherited branch evaluator's observation API.
        self.metrics = {'branch_calls': 0, 'empty_branch_calls': 0,
            'phase_calls': 0, 'H4_calls': 0, 'modular_column_applications': 0,
            'peak_endpoints': 0, 'peak_scalar_slots': 0,
            'peak_nonzero_scalars': 0, 'peak_denominator_bits': 0,
            'boundary_spectator_nonzero_seen': False}
        self.depth_metrics = {}

    def initial(self):
        full = (1, *([0]*(self.full_dim-1)))
        row = full if self.codec is None else self.codec.encode(full)
        return {(0, 1, 0): row}, 1


@dataclass
class BranchPlan:
    owner: object
    history: tuple
    rows: dict
    den: int
    targets: dict
    active_gates: tuple
    h: int
    M: int
    G: int
    masses: tuple
    transformed_rows: dict = field(default_factory=dict)


class SelectedStreamingProgram(LazyStreamingProgram):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.selected_metrics = {
            'planned_rounds': 0, 'empty_plans': 0,
            'support_column_requests': 0, 'collision_source_rows': 0,
            'feedback_row_cache_hits': 0, 'feedback_unique_rows': 0,
            'phase_vector_applications': 0, 'active_phase_instances': 0,
            'scalar_norm_terms': 0, 'scalar_collision_products': 0,
            'materialized_children': 0, 'materialized_child_rows': 0,
            'materialized_child_scalar_slots': 0,
            'peak_materialized_child_rows': 0,
            'peak_plan_source_rows': 0, 'peak_transformed_row_cache': 0,
            'contracted_native_H4_operations': 0,
        }

    def _transformed(self, plan, row):
        metrics = self.selected_metrics
        if row in plan.transformed_rows:
            metrics['feedback_row_cache_hits'] += 1
            return plan.transformed_rows[row]
        transformed = row
        for gate in plan.active_gates:
            transformed = tuple(gate.apply_numer(transformed))
            metrics['phase_vector_applications'] += 1
        plan.transformed_rows[row] = transformed
        metrics['feedback_unique_rows'] += 1
        metrics['peak_transformed_row_cache'] = max(metrics['peak_transformed_row_cache'],
                                                   len(plan.transformed_rows))
        return transformed

    def branch_plan(self, state, den, history):
        history = tuple(history)
        i = len(history)
        if i >= self.t or any(type(bit) is not int or bit not in (0, 1) for bit in history):
            raise ValueError('invalid complete classical history')
        if type(den) is not int or den <= 0 or den & (den-1):
            raise ValueError('positive dyadic amplitude denominator required')
        rows = {}
        for (x, work, spectator), values in state.items():
            if x != 0 or spectator != 0:
                raise ValueError('native round boundary requires empty control and returned spectator')
            if len(values) != self.dim or any(type(v) is not int for v in values):
                raise ValueError('all signed integer residual coordinates required')
            row = tuple(values)
            if any(row):
                rows[work] = row
        metrics = self.selected_metrics
        metrics['planned_rounds'] += 1
        metrics['peak_plan_source_rows'] = max(metrics['peak_plan_source_rows'], len(rows))
        if not rows:
            metrics['empty_plans'] += 1
            return BranchPlan(self, history, rows, den, {}, (), 1, 0, 0, (F(0), F(0)))
        gates = tuple(self.bank[i-ctrl+1] for ctrl in range(i) if history[ctrl])
        h = 1
        for gate in gates:
            h *= gate.den
        metrics['active_phase_instances'] += len(gates)
        M = sum(v*v for row in rows.values() for v in row)
        metrics['scalar_norm_terms'] += len(rows)*self.dim
        table = self.tables[i]
        targets = {work: table[work] for work in rows}
        metrics['support_column_requests'] += len(rows)
        # This finite support sanity check supplements, and does not replace,
        # the global typed inverse/permutation certificate checked at admission.
        if len(set(targets.values())) != len(targets):
            raise AssertionError('certified modular permutation collided on occupied labels')
        plan = BranchPlan(self, history, rows, den, targets, gates, h, M, 0, ())
        G = 0
        for work, target in targets.items():
            if target in rows:
                transformed = self._transformed(plan, rows[work])
                G += sum(x*y for x, y in zip(rows[target], transformed))
                metrics['collision_source_rows'] += 1
                metrics['scalar_collision_products'] += self.dim
        plan.G = G
        plan.masses = (F(h*M+G, 2*h*den*den), F(h*M-G, 2*h*den*den))
        if min(plan.masses) < 0 or sum(plan.masses) != F(M, den*den):
            raise AssertionError('complete native collision mass identity failed')
        metrics['contracted_native_H4_operations'] += 2
        return plan

    def materialize(self, plan, bit):
        if plan.owner is not self or type(bit) is not int or bit not in (0, 1):
            raise ValueError('plan ownership and selected bit required')
        metrics = self.selected_metrics
        metrics['materialized_children'] += 1
        if not plan.rows:
            return {}, 1
        out = {work: [plan.h*x for x in row] for work, row in plan.rows.items()}
        sign = 1 if bit == 0 else -1
        for work, target in plan.targets.items():
            transformed = self._transformed(plan, plan.rows[work])
            dest = out.setdefault(target, [0]*self.dim)
            for j, value in enumerate(transformed):
                dest[j] += sign*value
        state = {(0, work, 0): tuple(row) for work, row in out.items() if any(row)}
        state, den = reduce_state(state, 2*plan.h*plan.den)
        if norm(state, den) != plan.masses[bit]:
            raise AssertionError('selected native child disagrees with precomputed mass')
        metrics['materialized_child_rows'] += len(state)
        metrics['materialized_child_scalar_slots'] += len(state)*self.dim
        metrics['peak_materialized_child_rows'] = max(metrics['peak_materialized_child_rows'], len(state))
        self._observe(state, den, len(plan.history), 'selected_child_boundary')
        return state, den

    def branches(self, state, den, history):
        """Compatibility/test enumerator. The single-path sampler never calls it."""
        plan = self.branch_plan(state, den, history)
        return [self.materialize(plan, bit) for bit in (0, 1)]

    def report_metrics(self):
        return {**super().report_metrics(), 'selected_child': dict(self.selected_metrics)}


def sample_selected(program, rng, *, postprocess=None):
    """Same raw-state/RNG-interruption contract, materializing only the choice."""
    if postprocess is None:
        from lazy_postprocess import lazy_classical_postprocess
        postprocess = lazy_classical_postprocess
    state, den = program.initial()
    if norm(state, den) != 1:
        raise ValueError('initial state must have unit mass')
    history, events = (), []
    for i in range(program.t):
        before = norm(state, den)
        if before <= 0:
            raise ValueError('cannot condition on a zero-mass prefix')
        plan = program.branch_plan(state, den, history)
        masses = plan.masses
        if sum(masses) != before:
            raise AssertionError('instrument completeness failed')
        p0 = masses[0]/before
        try:
            bit = 1 if p0 == 0 else 0 if p0 == 1 else choose(p0, rng)
        except (StopIteration, EOFError):
            return {'status': 'INCOMPLETE_RANDOM_SOURCE', 'N': program.N,
                    'a': program.a, 't': program.t, 'history': history,
                    'events': events, 'next_round': i,
                    'resume_amplitude_denominator': str(den),
                    'resume_state': [{'key': list(k), 'row': list(map(str, v))}
                                     for k, v in sorted(state.items())],
                    'note': 'Raw state is before the unfinished round; preserve prefix, do not condition away this outcome.'}
        if masses[bit] <= 0:
            raise AssertionError('random interface selected a zero-mass child')
        state, den = program.materialize(plan, bit)
        history += (bit,)
        events.append({'round': i, 'bit': bit, 'conditional_probability':
                       str(masses[bit]/before), 'history_mass': str(masses[bit]),
                       'endpoints': len(state), 'amplitude_denominator_bits': den.bit_length()})
    product = F(1)
    for event in events:
        product *= F(event['conditional_probability'])
    if product != norm(state, den):
        raise AssertionError('raw prefix probabilities did not telescope')
    k = sum(bit << i for i, bit in enumerate(history))
    return {'N': program.N, 'a': program.a, 't': program.t, 'k': k,
            'history': history, 'history_probability': str(product),
            'events': events, 'postprocessing': postprocess(program.N, program.a, program.t, k)}
