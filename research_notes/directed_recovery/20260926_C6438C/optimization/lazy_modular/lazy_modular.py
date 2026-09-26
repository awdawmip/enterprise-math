"""Demand-driven modular permutations from actual BRC full-adder columns.

No all-N table, ordinary modular multiplication, pow or modulo propagator.
The complete permutation follows from a typed inverse certificate. Each
requested column retains shift-add, long-division and carry provenance.
"""
from __future__ import annotations
from pathlib import Path
from functools import lru_cache
from copy import deepcopy
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
PROJECT = ROOT.parents[1]
for directory in ('sparse', 'completion'):
    sys.path.insert(0, str(PROJECT / directory))
import sparse_modular as sparse
import typed_integer_prechecks as typed
from stage45.brc_loop_recheck import CALLS

SCHEMA = 'BRC_LAZY_MODULAR_PERMUTATION_V1'


def require(test, message):
    if not test:
        raise ValueError(message)


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


@lru_cache(None)
def source_binding():
    _, primitive = sparse.native_adder()
    return {'native_adder': primitive, 'files_sha256': {
        'lazy_modular': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'sparse_modular': hashlib.sha256(Path(sparse.__file__).read_bytes()).hexdigest(),
        'typed_integer_prechecks': hashlib.sha256(Path(typed.__file__).read_bytes()).hexdigest()},
        'primitive_source': '0852cad130c1d877174d235687cf60c19f318c58',
        'arithmetic_route': 'actual full-adder columns; digit transducer composition',
        'runtime_state_propagator': 'complete positive unit permutation on work labels'}


def trace_cost(trace):
    """Counts from the shipped arithmetic source, without evaluating values.

    Host wiring counts <<, >>, &, | and ~ only; metadata, loop/index control,
    hashing, allocation and Python implementation internals are excluded.
    """
    result = {'adder_digit_replays': 0, 'host_bit_wiring_operations': 0,
              'host_bit_length_calls_in_arithmetic': 0}
    def visit(item):
        if isinstance(item, dict):
            if 'cells' in item and 'low' in item and 'carry' in item:
                n = len(item['cells'])
                result['adder_digit_replays'] += n
                result['host_bit_wiring_operations'] += 10*n
                return
            operation = item.get('operation')
            if operation == 'BRC_UNSIGNED_COMPARE':
                result['host_bit_wiring_operations'] += 3
                result['host_bit_length_calls_in_arithmetic'] += 2
            elif operation == 'BRC_UNSIGNED_SHIFT_ADD':
                result['host_bit_wiring_operations'] += 3*len(item['steps'])
                result['host_bit_length_calls_in_arithmetic'] += 3
            elif operation == 'BRC_UNSIGNED_LONG_DIVISION':
                result['host_bit_wiring_operations'] += 6*len(item['steps'])
                result['host_bit_length_calls_in_arithmetic'] += 1
            for child in item.values():
                visit(child)
        elif isinstance(item, (tuple, list)):
            for child in item:
                visit(child)
    visit(trace)
    return result


class Arithmetic:
    def __init__(self):
        self.operations = []
        self.stats = {'typed_operations': 0, 'adder_digit_replays': 0,
                      'host_bit_wiring_operations': 0,
                      'host_bit_length_calls_in_arithmetic': 0,
                      'native_kernel_calls_delta': 0}

    def _retain(self, operation, trace, calls_before):
        self.operations.append({'operation': operation, 'trace': trace})
        self.stats['typed_operations'] += 1
        cost = trace_cost(trace)
        if operation == 'add':
            cost['host_bit_length_calls_in_arithmetic'] += 2
        for key, value in cost.items():
            self.stats[key] += value
        self.stats['native_kernel_calls_delta'] += len(CALLS)-calls_before
        return len(self.operations)-1

    def add(self, left, right):
        start = len(CALLS)
        value, trace = typed.add(left, right)
        return value, self._retain('add', trace, start)

    def compare(self, left, right):
        start = len(CALLS)
        relation, trace = typed.compare(left, right)
        index = self._retain('compare', trace, start)
        return relation, trace['low_difference'], index

    def multiply(self, left, right):
        start = len(CALLS)
        value, trace = typed.multiply(left, right)
        return value, self._retain('multiply', trace, start)

    def divide(self, value, modulus):
        start = len(CALLS)
        quotient, remainder, trace = typed.divide(value, modulus)
        return quotient, remainder, self._retain('divide', trace, start)

    def modmul(self, left, right, modulus):
        product, mul_id = self.multiply(left, right)
        _, residue, div_id = self.divide(product, modulus)
        return residue, {'multiply_operation': mul_id, 'division_operation': div_id}

    def modsubtract(self, left, right, modulus):
        relation, difference, compare_id = self.compare(left, right)
        if relation >= 0:
            return difference, {'comparison': compare_id, 'add_modulus': None}
        extended, add_id = self.add(left, modulus)
        relation2, difference, subtract_id = self.compare(extended, right)
        require(relation2 >= 0, 'modular subtraction invariant')
        return difference, {'comparison': compare_id, 'add_modulus': add_id,
                            'subtract_after_extension': subtract_id}


def inverse_certificate(N, b):
    """Residue-coefficient extended Euclid, entirely from typed arithmetic.

    Invariant r_i == coefficient_i*b (mod N); coefficients stay in [0,N).
    """
    arithmetic = Arithmetic()
    r0, r1, c0, c1 = N, b, 0, 1
    steps = []
    while r1:
        quotient, next_r, divide_id = arithmetic.divide(r0, r1)
        product_mod, product_ids = arithmetic.modmul(quotient, c1, N)
        next_c, subtraction_ids = arithmetic.modsubtract(c0, product_mod, N)
        require(0 <= next_r < r1 and 0 <= next_c < N, 'Euclidean residue invariant')
        steps.append({'r0': r0, 'r1': r1, 'c0': c0, 'c1': c1,
                      'quotient': quotient, 'division_operation': divide_id,
                      'product_mod_operations': product_ids, 'product_mod': product_mod,
                      'coefficient_subtraction': subtraction_ids,
                      'next_remainder': next_r, 'next_coefficient': next_c})
        r0, r1, c0, c1 = r1, next_r, c1, next_c
    require(r0 == 1, 'multiplier is not a unit modulo N')
    check, check_ids = arithmetic.modmul(b, c0, N)
    require(check == 1, 'typed inverse product is not one')
    return {'N': N, 'b': b, 'inverse_multiplier': c0, 'gcd': r0,
            'euclidean_steps': steps, 'inverse_product': check,
            'inverse_product_operations': check_ids,
            'arithmetic_operations': arithmetic.operations,
            'cost': {k:v for k,v in arithmetic.stats.items() if k != 'native_kernel_calls_delta'}}


def permutation_certificate(N, b):
    require(sparse.integer(N) and N >= 2 and sparse.integer(b) and 0 <= b < N,
            'integer N >= 2 and 0 <= b < N required')
    inverse = inverse_certificate(N, b)
    n = (N-1).bit_length()
    return {'schema': SCHEMA, 'N': N, 'b': b, 'width': n, 'carrier_size': 1 << n,
            'source': source_binding(), 'inverse_certificate': inverse,
            'identity_tail': {'first': N, 'last_exclusive': 1 << n},
            'column_rule': 'y<N: typed_shift_add_and_long_division(b,y,N); y>=N: y',
            'inverse_rule': 'same rule with certified inverse_multiplier',
            'completeness': 'symbolic arithmetic invariants plus typed inverse witness; no all-N enumeration',
            'fibres': 'all signed, residual and spectator coordinates transported intact',
            'admission': 'AUTHOR_EXECUTED_SHARED_CONTEXT_NOT_ADMITTED'}


class LazyModularColumns:
    def __init__(self, N, b):
        start = len(CALLS)
        self.permutation_certificate = permutation_certificate(N, b)
        self.N, self.b = N, b
        self.width = self.permutation_certificate['width']
        self.carrier_size = self.permutation_certificate['carrier_size']
        self.inverse_multiplier = self.permutation_certificate['inverse_certificate']['inverse_multiplier']
        self.certificate_sha256 = digest(self.permutation_certificate)
        self._columns = {}
        self._inverse = None
        self.stats = {'column_requests': 0, 'computed_columns': 0, 'cache_hits': 0,
                      'identity_tail_columns': 0, 'native_kernel_calls_delta': len(CALLS)-start,
                      'column_adder_digit_replays': 0, 'column_host_bit_wiring_operations': 0,
                      'column_host_bit_length_calls_in_arithmetic': 0,
                      'setup_adder_digit_replays': self.permutation_certificate['inverse_certificate']['cost']['adder_digit_replays'],
                      'setup_host_bit_wiring_operations': self.permutation_certificate['inverse_certificate']['cost']['host_bit_wiring_operations'],
                      'setup_host_bit_length_calls_in_arithmetic': self.permutation_certificate['inverse_certificate']['cost']['host_bit_length_calls_in_arithmetic']}

    def __len__(self):
        # Python requires Py_ssize_t here; integrations use carrier_size.
        return self.carrier_size

    def __iter__(self):
        raise TypeError('lazy modular permutations prohibit implicit full-domain iteration; request explicit columns')

    def __getitem__(self, y):
        require(sparse.integer(y) and 0 <= y < self.carrier_size, 'basis label outside carrier')
        self.stats['column_requests'] += 1
        if y in self._columns:
            self.stats['cache_hits'] += 1
            return self._columns[y]['target']
        arithmetic = Arithmetic()
        if y >= self.N:
            target, product = y, None
            self.stats['identity_tail_columns'] += 1
        else:
            target, product = arithmetic.modmul(self.b, y, self.N)
        require(0 <= target < self.carrier_size, 'column outside carrier')
        record = {'schema': SCHEMA+'_COLUMN', 'source': y, 'target': target,
                  'N': self.N, 'b': self.b, 'permutation_certificate_sha256': self.certificate_sha256,
                  'identity_tail': y >= self.N, 'product_operations': product,
                  'arithmetic_operations': arithmetic.operations,
                  'arithmetic_cost': {k:v for k,v in arithmetic.stats.items() if k != 'native_kernel_calls_delta'},
                  'edge_id': f'lazy-modmul:{self.N}:{self.b}:{y}'}
        self._columns[y] = record
        self.stats['computed_columns'] += 1
        self.stats['native_kernel_calls_delta'] += arithmetic.stats['native_kernel_calls_delta']
        for key in ('adder_digit_replays', 'host_bit_wiring_operations', 'host_bit_length_calls_in_arithmetic'):
            self.stats['column_'+key] += arithmetic.stats[key]
        return target

    def column_certificate(self, y):
        self[y]
        return deepcopy(self._columns[y])

    def report_metrics(self):
        return {**self.stats, 'cached_column_count': len(self._columns),
                'carrier_size': self.carrier_size,
                'resource_unit': 'native calls, adder-column digit replays and host bit wiring are distinct'}

    def inverse(self):
        if self._inverse is None:
            other = LazyModularColumns(self.N, self.inverse_multiplier)
            other._inverse = self
            self._inverse = other
        return self._inverse

    def transport_sparse(self, rows):
        """Positive branch transport, retaining each entire uninterpreted row."""
        out = {}
        for y, row in rows.items():
            target = self[y]
            require(target not in out, 'distinct sources collided despite inverse certificate')
            out[target] = row
        return out

    def export_certificate(self):
        return deepcopy({'permutation': self.permutation_certificate,
                'permutation_sha256': self.certificate_sha256,
                'queried_columns': [self._columns[y] for y in sorted(self._columns)],
                'stats': dict(self.stats),
                'resource_scope': 'cached columns grow only with distinct explicit requests; inverse is a separate lazy cache'})


def verify_lazy_permutation(table):
    require(type(table) is LazyModularColumns, 'actual lazy compiler type required')
    start = len(CALLS)
    rebuilt = permutation_certificate(table.N, table.b)
    require(digest(rebuilt) == table.certificate_sha256 == digest(table.permutation_certificate),
            'typed inverse/permutation certificate does not replay')
    require(table.carrier_size == rebuilt['carrier_size'] and table.width == rebuilt['width']
            and table.inverse_multiplier == rebuilt['inverse_certificate']['inverse_multiplier'],
            'lazy carrier or inverse attributes changed')
    return {'verified': True, 'schema': SCHEMA, 'N': table.N, 'b': table.b,
            'carrier_size': table.carrier_size, 'certificate_sha256': table.certificate_sha256,
            'inverse_multiplier': table.inverse_multiplier, 'whole_domain_enumerated': False,
            'replayed_adder_digits': rebuilt['inverse_certificate']['cost']['adder_digit_replays'],
            'native_kernel_calls_delta': len(CALLS)-start}


def verify_column_certificate(certificate, table):
    require(certificate['permutation_certificate_sha256'] == table.certificate_sha256,
            'column belongs to another permutation')
    replay = LazyModularColumns(table.N, table.b)
    rebuilt = replay.column_certificate(certificate['source'])
    require(digest(rebuilt) == digest(certificate), 'lazy column arithmetic does not replay')
    return {'verified': True, 'source': rebuilt['source'], 'target': rebuilt['target'],
            'column_sha256': digest(rebuilt), 'replay_stats': replay.stats}


def lazy_modular_columns(N, b):
    return LazyModularColumns(N, b)


class LazyModularFactory:
    def __init__(self):
        self.tables = {}

    def __call__(self, N, b):
        key = (N, b)
        if key not in self.tables:
            self.tables[key] = lazy_modular_columns(N, b)
        return self.tables[key]

    def export_certificate(self):
        return [self.tables[key].export_certificate() for key in sorted(self.tables)]


def lazy_modular_power_trace(N, a, exponent, *, factory=None):
    require(sparse.integer(exponent) and exponent >= 0, 'nonnegative integer exponent required')
    factory = factory or LazyModularFactory()
    table = factory(N, a)  # certifies the unit domain even at exponent zero
    rest, value, bit, steps = exponent, 1, 0, []
    while rest:
        selected = rest & 1
        output = table[value] if selected else value
        rest >>= 1
        next_b = table[table.b] if rest else None
        steps.append({'bit': bit, 'selected': selected, 'input': value, 'output': output,
                      'b': table.b, 'next_b': next_b,
                      'permutation_certificate_sha256': table.certificate_sha256,
                      'multiply_column': value if selected else None,
                      'square_column': table.b if rest else None})
        value = output
        if rest:
            table = factory(N, next_b)
        bit += 1
    return {'N': N, 'a': a, 'exponent': exponent, 'value': value, 'steps': steps,
            'tables': factory.export_certificate(), 'whole_domain_enumerated': False,
            'scope': 'typed modular arithmetic; exponent bits route actual columns, no hidden order or factors'}


def lazy_modular_power_brc(N, a, exponent):
    return lazy_modular_power_trace(N, a, exponent)['value']


def lazy_modular_power_chain(N, a, t, *, factory=None):
    require(sparse.integer(t) and t >= 0, 'nonnegative chain length required')
    factory = factory or LazyModularFactory()
    b, powers, tables, origins = a, [], [], []
    for bit in range(t):
        table = factory(N, b)
        powers.append(b)
        tables.append(table)
        following = table[b]
        origins.append({'bit': bit, 'b': b, 'square_source': b, 'square_target': following,
                        'certificate_sha256': table.certificate_sha256})
        b = following
    return tuple(powers), tuple(tables), tuple(origins)
