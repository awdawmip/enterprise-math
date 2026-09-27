"""Actual paid order/address discovery connected to native full correlations.

The phase contraction core is reused from the frozen previous package; the
O(R) full-cycle boundary is replaced by fresh small-odd-part/address replay.
"""
from pathlib import Path
from copy import deepcopy
from fractions import Fraction
import hashlib
import sys

ROOT = Path(__file__).resolve().parent
OLD = ROOT.parents[1] / 'sep27-qft-carry-execution'
for directory in (OLD, ROOT.parent / 'period_discovery', ROOT.parent / 'target_address'):
    sys.path.insert(0, str(directory))
from carry_executor import CarryExecutor, Correlation, normalized
from lazy_modular import Arithmetic, LazyModularColumns, verify_lazy_permutation
from typed_odd_part import discover_odd_part
from typed_target_address import recover_target_address, verify_target_address


def require(test, message):
    if not test:
        raise ValueError(message)


def source_hashes():
    import carry_executor, lazy_modular, typed_odd_part, typed_target_address
    return {name: hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest()
            for name, module in (('paid_aggregator.py', sys.modules[__name__]),
                ('carry_executor.py', carry_executor), ('lazy_modular.py', lazy_modular),
                ('typed_odd_part.py', typed_odd_part), ('typed_target_address.py', typed_target_address))}


class PaidDiscoveryIncomplete(ValueError):
    def __init__(self, certificate):
        super().__init__('odd budget did not certify an order')
        self.evidence = certificate


class PaidAggregator(CarryExecutor):
    def __init__(self, program, history):
        super().__init__(program, history)
        self._aggregation_source = source_hashes()
        self.aggregation_stats = {'queries': 0, 'high_layers': 0, 'low_layers': 0,
            'high_transition_terms': 0, 'low_transition_terms': 0,
            'peak_residue_matrix_slots': 0, 'peak_carry_matrix_slots': 0,
            'large_two_part_single_coefficient_queries': 0,
            'nonmember_zero_queries': 0, 'leading_zero_queries': 0,
            'suffix_coefficient_queries': 0}
        self.aggregation_queries = []

    def discover_address(self, depth, target, odd_budget):
        self._check()
        require(type(depth) is int and 1 <= depth <= len(self.history), 'valid retained positive depth required')
        certificate = discover_odd_part(self.program.N, self.program.modular_powers[depth-1], odd_budget)
        if certificate['status'] != 'CERTIFIED':
            raise PaidDiscoveryIncomplete(certificate)
        return recover_target_address(certificate, target)

    def _verify_address(self, depth, target, address_certificate):
        self._check()
        require(source_hashes() == self._aggregation_source, 'aggregation source changed')
        require(type(depth) is int and 1 <= depth <= len(self.history), 'valid retained positive depth required')
        require(type(target) is int and 1 <= target < self.program.N, 'canonical target residue required')
        require(type(address_certificate) is dict, 'actual address certificate required')
        inputs = address_certificate['inputs']
        require(inputs == {'N': self.program.N, 'b': self.program.modular_powers[depth-1], 'z': target},
                'address belongs to another modular target or schedule')
        inherited = self.program.tables[depth-1]
        require(inherited.N == self.program.N and inherited.b == inputs['b'], 'program table/schedule mismatch')
        inherited_replay = verify_lazy_permutation(inherited)
        verification = verify_target_address(address_certificate)
        verification['inherited_permutation_replay'] = inherited_replay
        replay = verification['replay']
        require(replay['status'] in ('MEMBER', 'NONMEMBER'), 'completed membership decision required')
        self.aggregation_stats['queries'] += 1
        return verification

    def gamma_with_address(self, depth, target, address_certificate):
        verification = self._verify_address(depth, target, address_certificate)
        replay = verification['replay']
        if replay['status'] == 'NONMEMBER':
            self.aggregation_stats['nonmember_zero_queries'] += 1
            self.aggregation_queries.append({'depth': depth, 'target': target,
                'address_verification': verification, 'contraction_method': 'certified_nonmember_zero'})
            return self._zero()
        return self._contract_verified_period(depth, replay['r'], replay['R'], target, verification)

    def _contract_verified_period(self, depth, r, R, target, verification):
        arithmetic = Arithmetic()
        # Valuation and bit splitting are finite index wiring, not a modular
        # state propagator. Every residue-index transition is typed below.
        s, q = 0, R
        while not q & 1:
            q >>= 1
            s += 1
        record = {'depth': depth, 'r': r, 'R': R, 'target': target, 's': s, 'q': q,
                  'address_verification': verification, 'routes': [], 'low_seeds': []}
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
                            _, x_reduced, x_div_op = arithmetic.divide(x, q)
                            dest, subtract_ops = arithmetic.modsubtract(reduced, x_reduced, q)
                            routes[e, x, y] = dest
                            record['routes'].append({'e': e, 'x': x, 'y': y, 'destination': dest,
                                'double': double_op, 'add': add_op, 'divide': div_op,
                                'subtract': subtract_ops, 'x_reduction': x_div_op})
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
        record['contraction_method'] = 'odd_residue_and_two_carry'
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
            all_orders_and_addresses_fresh_actual_typed_replayed=True,
            same_information_classical_factoring_advantage_claimed=False,
            slot_counters_exclude_fresh_terms_native_temporaries_and_receipts=True)
        return evidence
