"""Whole-period signed correlation using actual native matrix actions.

The current certification deliberately discovers a complete cycle in O(R).
The symbolic small-odd-part discovery/log algorithm is NOT implemented here.
"""
from copy import deepcopy
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))
from carry_executor import CarryExecutor
from lazy_modular import Arithmetic, LazyModularColumns, verify_lazy_permutation
from stage45.brc_loop_recheck import CALLS


def require(test, message):
    if not test:
        raise ValueError(message)


def source_hashes():
    import carry_executor, lazy_modular
    return {name: hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest()
            for name, module in (('period_aggregator.py', sys.modules[__name__]),
                                 ('carry_executor.py', carry_executor),
                                 ('lazy_modular.py', lazy_modular))}


def semantic(value):
    if isinstance(value, dict):
        return {str(k): semantic(v) for k, v in value.items()
                if k not in ('native_kernel_calls_delta', 'actual_native_core_calls_delta')}
    if isinstance(value, (tuple, list)):
        return [semantic(v) for v in value]
    return value


class PeriodCertificateError(ValueError):
    def __init__(self, message, evidence):
        super().__init__(message)
        self.evidence = evidence


def certify_period(program, depth, limit):
    """Actually walk a fresh typed table to its first return, retaining all columns."""
    require(type(depth) is int and 1 <= depth <= program.t, 'positive program depth required')
    require(type(limit) is int and limit >= 1, 'positive finite cycle budget required')
    require(len(program.tables) == program.t and len(program.modular_powers) == program.t,
            'complete admitted modular schedule required')
    inherited = program.tables[depth-1]
    b = program.modular_powers[depth-1]
    require(inherited.N == program.N and inherited.b == b, 'program table/schedule mismatch')
    start = len(CALLS)
    inherited_replay = verify_lazy_permutation(inherited)
    table = LazyModularColumns(program.N, b)
    fresh_replay = verify_lazy_permutation(table)
    states, period = [1], None
    for exponent in range(1, limit+1):
        value = table[states[-1]]
        states.append(value)
        if value == 1:
            period = exponent
            break
    return {
        'schema': 'ACTUAL_TYPED_FIRST_RETURN_PERIOD_V1',
        'status': 'CERTIFIED' if period is not None else 'PARTIAL',
        'source_sha256': source_hashes(),
        'inputs': {'N': program.N, 'a': program.a, 't': program.t,
                   'depth': depth, 'b': b, 'limit': limit},
        'R': period, 'states': tuple(states),
        'inherited_permutation_replay': inherited_replay,
        'fresh_permutation_replay': fresh_replay,
        'actual_cycle_table': table.export_certificate(),
        'actual_native_core_calls_delta': len(CALLS)-start,
        'complexity': 'O(R) consecutive typed columns on success; no small-odd-part discovery implemented',
    }


def verify_period_certificate(program, certificate):
    """Full actual replay, not trust in status/hash/declared first return."""
    require(isinstance(certificate, dict) and certificate.get('status') == 'CERTIFIED',
            'a completed actual first-return certificate is required')
    inputs = certificate['inputs']
    require((inputs['N'], inputs['a'], inputs['t']) == (program.N, program.a, program.t),
            'period certificate belongs to another input')
    replay = certify_period(program, inputs['depth'], inputs['limit'])
    if semantic(certificate) != semantic(replay):
        raise PeriodCertificateError('complete period evidence does not replay',
                                     {'certificate': deepcopy(certificate), 'replay': replay})
    return {'verified': True, 'replay': replay}


class PeriodAggregator(CarryExecutor):
    """A fixed admitted program/history; every query requires a replayed exact cycle."""
    def __init__(self, program, history):
        super().__init__(program, history)
        self.aggregation_stats = {'queries': 0, 'high_layers': 0, 'low_layers': 0,
            'high_transition_terms': 0, 'low_transition_terms': 0,
            'peak_residue_matrix_slots': 0, 'peak_carry_matrix_slots': 0,
            'large_two_part_single_coefficient_queries': 0}
        self.aggregation_queries = []
        self._aggregation_source = source_hashes()

    def gamma_known_period(self, depth, r, R, *, target, period_certificate):
        self._check()
        require(source_hashes() == self._aggregation_source, 'aggregation source changed')
        require(type(depth) is int and 1 <= depth <= len(self.history), 'valid retained positive depth required')
        require(type(R) is int and R >= 1, 'positive integer exact period required')
        require(type(r) is int and 0 <= r < R, 'canonical integer period address required')
        require(type(target) is int and 1 <= target < self.program.N, 'canonical target residue required')
        require(period_certificate['inputs']['depth'] == depth, 'certificate depth mismatch')
        require(period_certificate.get('R') == R, 'declared period differs from certificate')
        require(period_certificate['states'][r] == target,
                'declared address does not name the requested target')
        verification = verify_period_certificate(self.program, period_certificate)
        require(verification['replay']['states'][r] == target,
                'address r does not name the requested actual target')
        self.aggregation_stats['queries'] += 1
        arithmetic = Arithmetic()
        # Valuation and bit splitting are finite index wiring, not a modular
        # state propagator. Every residue-index transition is typed below.
        s, q = 0, R
        while not q & 1:
            q >>= 1
            s += 1
        record = {'depth': depth, 'r': r, 'R': R, 'target': target, 's': s, 'q': q,
                  'period_verification': verification, 'routes': [], 'low_seeds': []}
        if s > depth:
            L = 1 << depth
            _, distance, comparison = arithmetic.compare(R, r)
            record['large_two_part_distance_operation'] = comparison
            if r < L:
                answer = self.coefficient(depth, r)
            elif distance < L:
                answer = self.coefficient(depth, -distance)
            else:
                answer = self._zero()
            self.aggregation_stats['large_two_part_single_coefficient_queries'] += 1
        else:
            H = depth-s
            high = tuple(self._seed() if e == 0 else self._zero() for e in range(q))
            self.aggregation_stats['peak_residue_matrix_slots'] = max(
                self.aggregation_stats['peak_residue_matrix_slots'], q*self.dim*self.dim)
            self._observe_size(high)
            routes = {}
            if H:
                for e in range(q):
                    twice, double_op = arithmetic.add(e, e)
                    for x in (0, 1):
                        for y in (0, 1):
                            extended, add_op = arithmetic.add(twice, y)
                            _, reduced, div_op = arithmetic.divide(extended, q)
                            dest, subtract_ops = arithmetic.modsubtract(reduced, x, q)
                            routes[e, x, y] = dest
                            record['routes'].append({'e': e, 'x': x, 'y': y, 'destination': dest,
                                'double': double_op, 'add': add_op, 'divide': div_op,
                                'subtract': subtract_ops})
            for j in range(H):
                contributions = [[] for _ in range(q)]
                gates = self._gates(j)
                for e, matrix in enumerate(high):
                    for x in (0, 1):
                        for y in (0, 1):
                            term = self._right_transpose(matrix, gates) if y else matrix
                            term = self._left(term, gates) if x else term
                            sign = -1 if self.history[j] and x != y else 1
                            contributions[routes[e, x, y]].append((sign, term))
                            self.aggregation_stats['high_transition_terms'] += 1
                high = tuple(self._combine(terms) if terms else self._zero()
                             for terms in contributions)
                self.aggregation_stats['high_layers'] += 1
                self._observe_size(high)
            rH, r0, split_op = arithmetic.divide(r, 1 << s)
            record.update(H=H, rH=rH, r0=r0, address_split_operation=split_op)
            indices = []
            for c in (0, 1):
                value, add_op = arithmetic.add(rH, c)
                _, index, div_op = arithmetic.divide(value, q)
                indices.append(index)
                record['low_seeds'].append({'carry': c, 'index': index, 'add': add_op, 'divide': div_op})
            # Correlation is immutable and all following accumulators are fresh.
            boundary = tuple(high[e] for e in indices)
            self.aggregation_stats['peak_carry_matrix_slots'] = max(
                self.aggregation_stats['peak_carry_matrix_slots'], 2*self.dim*self.dim)
            for j in range(H, depth):
                digit = (r0 >> (depth-1-j)) & 1
                gates = self._gates(j)
                contributions = [[], []]
                for carry_out in (0, 1):
                    for carry_in in (0, 1):
                        for x in (0, 1):
                            y = x+digit+carry_in-2*carry_out
                            if y not in (0, 1):
                                continue
                            term = boundary[carry_out]
                            term = self._right_transpose(term, gates) if y else term
                            term = self._left(term, gates) if x else term
                            sign = -1 if self.history[j] and x != y else 1
                            contributions[carry_in].append((sign, term))
                            self.aggregation_stats['low_transition_terms'] += 1
                boundary = tuple(self._combine(terms) if terms else self._zero()
                                 for terms in contributions)
                self.aggregation_stats['low_layers'] += 1
                self._observe_size(boundary)
            # _combine already divided by four in each of all depth layers.
            answer = boundary[0]
        record['index_arithmetic_operations'] = deepcopy(arithmetic.operations)
        record['index_arithmetic_stats'] = dict(arithmetic.stats)
        self.aggregation_queries.append(record)
        self._observe_size((answer,))
        return answer

    def evidence(self):
        evidence = super().evidence()
        evidence.update(aggregation_stats=dict(self.aggregation_stats),
                        aggregation_queries=deepcopy(self.aggregation_queries),
                        aggregation_source_sha256=dict(self._aggregation_source),
                        period_discovery_cost_is_O_R_not_small_odd_part=True,
                        address_certified_from_actual_cycle_columns=True,
                        slot_counters_exclude_fresh_terms_native_temporaries_and_receipts=True)
        return evidence
