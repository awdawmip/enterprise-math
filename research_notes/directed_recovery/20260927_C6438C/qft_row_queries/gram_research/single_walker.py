"""Actual native-instrument single-label sampler with a memoized row oracle.

Only point queries are constructed; this cache can still grow exponentially.
The exact latent coupling is a domain specialization of amplitude-query sampling.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parent
PREVIOUS = ROOT.parents[1] / 'sep26-shor-general'
for p in (PREVIOUS / 'new_word_compiler', PREVIOUS / 'optimization/streaming'):
    sys.path.insert(0, str(p))
from certified_word_compiler import PositivePathObserver
from lazy_streaming import LazyStreamingProgram
from stage58.coupled_reader import choose


@dataclass(frozen=True)
class RawRow:
    values: tuple
    den: int


class QueryBudgetExhausted(RuntimeError):
    pass


def normalize_row(values, den):
    values = tuple(values)
    if (type(den) is not int or den <= 0 or den & (den-1)
            or any(type(x) is not int for x in values)):
        raise ValueError('integer row and positive dyadic denominator required')
    if not any(values):
        return RawRow(values, 1)
    while den > 1 and not any(x & 1 for x in values):
        values = tuple(x >> 1 for x in values)
        den >>= 1
    return RawRow(values, den)


class PointRowOracle:
    def __init__(self, program, history=(), *, query_budget=1000):
        if not isinstance(program, LazyStreamingProgram):
            raise ValueError('actual admitted native lazy program required')
        history = tuple(history)
        if len(history) > program.t or any(type(b) is not int or b not in (0, 1) for b in history):
            raise ValueError('complete classical history required')
        if type(query_budget) is not int or query_budget < 0:
            raise ValueError('nonnegative point-query budget required')
        self.program, self.dim, self.history = program, program.dim, history
        self.query_budget, self.cache = query_budget, {}
        self.observer = PositivePathObserver()
        self.observation_count = 0
        self.tables = list(program.lazy_factory.tables.values())
        self.stats = {'query_requests': 0, 'query_cache_hits': 0, 'base_queries': 0,
            'recurrence_queries': 0, 'native_phase_vector_applications': 0,
            'zero_native_actions_skipped': 0, 'single_term_wiring': 0,
            'zero_term_wiring': 0, 'max_numerator_bits': 0, 'max_denominator_bits': 0}

    def observe(self, name, terms):
        terms = tuple(tuple(F(x) for x in term) for term in terms
                      if all(x != 0 for x in term))
        if not terms:
            self.stats['zero_term_wiring'] += 1
            return F(0)
        if len(terms) == 1 and len(terms[0]) == 1:
            self.stats['single_term_wiring'] += 1
            return terms[0][0]
        self.observation_count += 1
        return self.observer.evaluate(f'{self.observation_count}:{name}', terms)

    def norm_observation(self, row, name='row_norm'):
        if len(row.values) != self.dim:
            raise ValueError('row must retain all admitted coordinates')
        return self.observe(name, ((F(v, row.den), F(v, row.den)) for v in row.values))

    def apply_feedback(self, depth, row):
        if type(depth) is not int or not 0 <= depth <= len(self.history):
            raise ValueError('feedback prefix unavailable')
        if len(row.values) != self.dim:
            raise ValueError('feedback row dimension mismatch')
        if not any(row.values):
            self.stats['zero_native_actions_skipped'] += 1
            return row
        values, den = row.values, row.den
        for ctrl in range(depth):
            if self.history[ctrl]:
                gate = self.program.bank[depth-ctrl+1]
                values = tuple(gate.apply_numer(values))
                den *= gate.den
                self.stats['native_phase_vector_applications'] += 1
        return normalize_row(values, den)

    def combine(self, left, right, sign=1, halve=True):
        if type(sign) is not int or sign not in (-1, 1) or type(halve) is not bool:
            raise ValueError('exact sign and halve convention required')
        if len(left.values) != self.dim or len(right.values) != self.dim:
            raise ValueError('complete signed rows required')
        den = max(left.den, right.den)
        sl, sr = den.bit_length()-left.den.bit_length(), den.bit_length()-right.den.bit_length()
        values = []
        for x, y in zip(left.values, right.values):
            value = self.observe('signed_row_sum', (((x << sl),), (sign*(y << sr),)))
            if value.denominator != 1:
                raise AssertionError('aligned row sum is not an integer')
            values.append(value.numerator)
        return normalize_row(values, den << int(halve))

    def inverse_table(self, depth):
        inverse = self.program.tables[depth].inverse()
        if not any(inverse is table for table in self.tables):
            self.tables.append(inverse)
        return inverse

    def _retain(self, key, row):
        if len(self.cache) >= self.query_budget:
            raise QueryBudgetExhausted('row-query budget reached; live cache retained')
        self.cache[key] = row
        self.stats['max_numerator_bits'] = max(self.stats['max_numerator_bits'],
            max((abs(v).bit_length() for v in row.values), default=0))
        self.stats['max_denominator_bits'] = max(self.stats['max_denominator_bits'], row.den.bit_length())
        return row

    def query(self, depth, label):
        if (type(depth) is not int or not 0 <= depth <= len(self.history)
                or type(label) is not int or not 0 <= label < (1 << (self.program.N-1).bit_length())):
            raise ValueError('query requires retained prefix and carrier label')
        self.stats['query_requests'] += 1
        key = (depth, label)
        if key in self.cache:
            self.stats['query_cache_hits'] += 1
            return self.cache[key]
        if len(self.cache) >= self.query_budget:
            raise QueryBudgetExhausted('row-query budget reached; live cache retained')
        if depth == 0:
            self.stats['base_queries'] += 1
            full = tuple(int(label == 1 and j == 0) for j in range(self.program.full_dim))
            values = full if self.program.codec is None else self.program.codec.encode(full)
            return self._retain(key, RawRow(tuple(values), 1))
        i = depth-1
        predecessor = self.inverse_table(i)[label]
        left = self.query(i, label)
        right = self.apply_feedback(i, self.query(i, predecessor))
        row = self.combine(left, right, 1 if self.history[i] == 0 else -1)
        self.stats['recurrence_queries'] += 1
        return self._retain(key, row)

    def append(self, bit):
        if type(bit) is not int or bit not in (0, 1) or len(self.history) >= self.program.t:
            raise ValueError('one next classical bit required')
        self.history += (bit,)

    def report(self):
        metrics = [table.report_metrics() for table in self.tables]
        return {**self.stats, 'history': self.history, 'dimension': self.dim,
            'distinct_queries': len(self.cache), 'cached_row_scalar_slots': len(self.cache)*self.dim,
            'query_keys': sorted(self.cache), 'query_budget': self.query_budget,
            'actual_positive_path_observations': len(self.observer.operations),
            'typed_modular_tables': metrics,
            'adder_digit_replays': sum(x['setup_adder_digit_replays']+x['column_adder_digit_replays'] for x in metrics),
            'computed_modular_columns': sum(x['computed_columns'] for x in metrics),
            'complete_current_work_state_enumerated_as_algorithm_step': False,
            'cache_may_eventually_cover_full_support': True,
            'durable_cross_process_cursor_claimed': False}

    def evidence(self):
        return {'report': self.report(), 'observer_operations': self.observer.operations,
            'point_rows': [{'depth': key[0], 'label': key[1], 'values': row.values, 'den': row.den}
                           for key, row in sorted(self.cache.items())],
            'typed_modular_certificates': [table.export_certificate() for table in self.tables],
            'phase_bindings': self.program.phase_bindings, 'codec_binding': self.program.codec_binding,
            'native_two_H4_binding': self.program.h4_binding,
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def transition_plan(oracle, latent, auxiliary_bit):
    """Exact local score conditioned on latent proposal, not marginal bit p0."""
    i = len(oracle.history)
    if (i >= oracle.program.t or type(auxiliary_bit) is not int or auxiliary_bit not in (0, 1)
            or type(latent) is not int):
        raise ValueError('live round, exact latent label and auxiliary bit required')
    candidate = latent if auxiliary_bit == 0 else oracle.program.tables[i][latent]
    predecessor = oracle.inverse_table(i)[candidate]
    x = oracle.query(i, candidate)
    source = oracle.query(i, predecessor)
    if not any((x if auxiliary_bit == 0 else source).values):
        raise ValueError('latent label has zero parent row')
    y = oracle.apply_feedback(i, source)
    plus = oracle.combine(x, y, halve=False)
    minus = oracle.combine(x, y, sign=-1, halve=False)
    nx, ny = oracle.norm_observation(x), oracle.norm_observation(y)
    total = oracle.observe('proposal_squared_rows', ((nx,), (ny,)))
    numerator = oracle.norm_observation(plus, 'plus_quadratic')
    other = oracle.norm_observation(minus, 'minus_quadratic')
    if total <= 0 or numerator+other != 2*total:
        raise AssertionError('actual complete rows failed parallelogram identity')
    p0 = numerator/(2*total)
    if not 0 <= p0 <= 1:
        raise AssertionError('local conditional probability out of range')
    return {'history': oracle.history, 'latent_before': latent,
            'auxiliary_bit': auxiliary_bit, 'candidate': candidate, 'predecessor': predecessor,
            'row_x': x, 'row_y': y, 'proposal_norm_sum': total,
            'plus_norm': numerator, 'minus_norm': other,
            'bit_probability_given_proposed_label': p0}


class SingleWalker:
    def __init__(self, program, *, query_budget=1000, oracle=None):
        self.program = program
        self.oracle = PointRowOracle(program, query_budget=query_budget) if oracle is None else oracle
        if self.oracle.program is not program or self.oracle.history:
            raise ValueError('sampler must start from the admitted empty prefix')
        self.latent = 1
        self.events = []
        self.pending_auxiliary_bit = None
        self.pending_plan = None
        self.random_calls = 0

    @property
    def history(self):
        return self.oracle.history

    def _draw(self, probability, rng):
        if probability == 0:
            return 1
        if probability == 1:
            return 0
        self.random_calls += 1
        return choose(probability, rng)

    def step(self, rng):
        if len(self.history) >= self.program.t:
            raise ValueError('terminal walker')
        if self.pending_auxiliary_bit is None:
            self.pending_auxiliary_bit = self._draw(F(1, 2), rng)
        if self.pending_plan is None:
            self.pending_plan = transition_plan(self.oracle, self.latent, self.pending_auxiliary_bit)
        plan = self.pending_plan
        if tuple(plan['history']) != self.history or plan['latent_before'] != self.latent:
            raise AssertionError('unfinished transition lost its original parent')
        bit = self._draw(plan['bit_probability_given_proposed_label'], rng)
        local_prob = plan['bit_probability_given_proposed_label'] if bit == 0 else 1-plan['bit_probability_given_proposed_label']
        if local_prob <= 0:
            raise AssertionError('random interface selected impossible local branch')
        self.oracle.append(bit)
        self.latent = plan['candidate']
        self.events.append({**plan, 'selected_bit': bit,
                            'selected_local_probability': local_prob})
        self.pending_auxiliary_bit = self.pending_plan = None
        return self.events[-1]

    def run(self, rng, *, postprocess=None):
        status = 'COMPLETE_READOUT'
        try:
            while len(self.history) < self.program.t:
                self.step(rng)
        except (StopIteration, EOFError):
            status = 'INCOMPLETE_RANDOM_SOURCE'
        except QueryBudgetExhausted:
            status = 'INCOMPLETE_POINT_QUERY_BUDGET'
        result = {'status': status, 'N': self.program.N, 'a': self.program.a, 't': self.program.t,
            'history': self.history, 'latent_work_label': self.latent, 'events': list(self.events),
            'random_calls_attempted': self.random_calls,
            'pending_auxiliary_bit': self.pending_auxiliary_bit, 'pending_plan': self.pending_plan,
            'local_scores_are_not_marginal_readout_probabilities': True,
            'live_object_resume_only': True, 'oracle_report': self.oracle.report(),
            'random_source_contract': 'fresh conditionally uniform randrange; software fixture is not physical randomness'}
        if status == 'COMPLETE_READOUT':
            k = sum(bit << i for i, bit in enumerate(self.history))
            result['k'] = k
            result['postprocessing'] = (postprocess(self.program.N, self.program.a, self.program.t, k)
                                        if postprocess is not None else {'status': 'INSTRUMENT_ONLY'})
        return result
