"""Paid small-odd-part order discovery through frozen actual typed columns.

No supplied order, factors, ordinary modular pow/remainder/gcd, or phase
propagation. Exponent bits and loop indices are declared routing only.
"""
from pathlib import Path
from copy import deepcopy
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
OLD = ROOT.parents[1] / 'sep26-shor-general'
sys.path.insert(0, str(OLD / 'optimization/lazy_modular'))
from lazy_modular import Arithmetic, LazyModularFactory, verify_lazy_permutation, source_binding
from stage45.brc_loop_recheck import CALLS

SCHEMA = 'BRC_SMALL_ODD_PART_ORDER_V1'


def require(test, message):
    if not test:
        raise ValueError(message)


def source_hashes():
    import lazy_modular
    return {'typed_odd_part.py': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'lazy_modular.py': hashlib.sha256(Path(lazy_modular.__file__).read_bytes()).hexdigest()}


class OddPartDiscoveryError(ValueError):
    def __init__(self, message, evidence, metrics):
        super().__init__(message)
        self.evidence, self.metrics = evidence, metrics


class OddPartCertificateError(ValueError):
    def __init__(self, message, evidence):
        super().__init__(message)
        self.evidence = evidence


def discover_odd_part(N, b, odd_budget):
    """CERTIFIED exact q,s,R or PARTIAL after a finite odd-return budget.

    The first n squarings are always paid, even for odd_budget zero. A
    successful first return at q<=odd_budget is followed by paid binary
    exponentiation b^q and at most n recovery squarings. Every newly created
    modular table receives a full typed permutation replay once per call.
    """
    started = len(CALLS)
    arithmetic, factory = Arithmetic(), LazyModularFactory()
    verifications, verified = [], set()
    record = {'schema': SCHEMA, 'status': 'RUNNING',
        'inputs': {'N': N, 'b': b, 'odd_budget': odd_budget},
        'n': None, 'q': None, 's': None, 'R': None,
        'evidence': {'source_sha256': source_hashes(), 'unit_check': None,
            'c_squaring_chain': [], 'c': None, 'odd_first_return_chain': [],
            'odd_power_chain': [], 'b_to_q': None, 'two_part_chain': [],
            'host_wiring': 'integer widths, exponent bits, loop/index routing, equality, dictionaries and metadata only',
            'scope': 'exact modular order discovery; no phase/amplitude propagation or hidden order input'}}
    evidence = record['evidence']
    stats = {'c_squarings': 0, 'odd_return_steps': 0,
             'odd_power_multiplications': 0, 'odd_power_squarings': 0,
             'two_part_squarings': 0}

    def finish():
        tables = factory.export_certificate()
        evidence['table_instances'] = tables
        evidence['permutation_verifications'] = deepcopy(verifications)
        evidence['arithmetic_operations'] = deepcopy(arithmetic.operations)
        evidence['arithmetic_stats'] = dict(arithmetic.stats)
        evidence['native_source'] = source_binding() if tables else None
        metrics = dict(stats)
        metrics.update(table_instance_count=len(tables),
            setup_adder_digit_replays=sum(x['stats']['setup_adder_digit_replays'] for x in tables),
            column_adder_digit_replays=sum(x['stats']['column_adder_digit_replays'] for x in tables),
            verification_adder_digit_replays=sum(x['replayed_adder_digits'] for x in verifications),
            auxiliary_adder_digit_replays=arithmetic.stats['adder_digit_replays'],
            column_requests=sum(x['stats']['column_requests'] for x in tables),
            computed_columns=sum(x['stats']['computed_columns'] for x in tables),
            cache_hits=sum(x['stats']['cache_hits'] for x in tables),
            actual_native_core_calls_delta=len(CALLS)-started)
        metrics['total_adder_digit_replays'] = sum(metrics[k] for k in (
            'setup_adder_digit_replays', 'column_adder_digit_replays',
            'verification_adder_digit_replays', 'auxiliary_adder_digit_replays'))
        record['metrics'] = metrics
        return deepcopy(record)

    def table(multiplier):
        result = factory(N, multiplier)
        if multiplier not in verified:
            verifications.append(verify_lazy_permutation(result))
            verified.add(multiplier)
        return result

    def column(multiplier, source):
        action = table(multiplier)
        target = action[source]
        return target, {'multiplier': multiplier, 'source': source, 'target': target,
                        'permutation_certificate_sha256': action.certificate_sha256}

    try:
        require(type(N) is int and N >= 2, 'integer modulus N>=2 required')
        require(type(b) is int and 1 <= b < N, 'canonical integer unit candidate 1<=b<N required')
        require(type(odd_budget) is int and odd_budget >= 0, 'nonnegative integer odd budget required')
        n = (N-1).bit_length()
        record['n'] = n
        # Retain a typed failed gcd before a constructor could discard its
        # internal failed inverse trace for a nonunit request.
        left, right, divisions = N, b, []
        while right:
            quotient, remainder, operation = arithmetic.divide(left, right)
            divisions.append({'left': left, 'right': right, 'quotient': quotient,
                              'remainder': remainder, 'division_operation': operation})
            left, right = right, remainder
        evidence['unit_check'] = {'gcd': left, 'divisions': divisions}
        require(left == 1, 'b is not a unit modulo N')
        value = b
        for step in range(n):
            value, edge = column(value, value)
            evidence['c_squaring_chain'].append({'step': step+1, **edge})
            stats['c_squarings'] += 1
        c = value
        evidence['c'] = c
        value, q = 1, None
        for exponent in range(1, odd_budget+1):
            value, edge = column(c, value)
            evidence['odd_first_return_chain'].append({'exponent': exponent, **edge})
            stats['odd_return_steps'] += 1
            if value == 1:
                q = exponent
                break
        if q is None:
            record['status'] = 'PARTIAL'
            evidence['partial_reason'] = 'no first return within the declared odd budget; no complete order certified'
            return finish()
        require(q & 1 == 1, 'odd-part first return must be odd')
        record['q'] = q
        # Binary exponentiation uses only actual typed columns. Reusing a
        # prior table is explicit cache reuse, not an uncharged new instance.
        rest, power, value, bit = q, b, 1, 0
        while rest:
            selected = rest & 1
            multiply_edge = None
            if selected:
                value, multiply_edge = column(power, value)
                stats['odd_power_multiplications'] += 1
            rest >>= 1
            square_edge = None
            if rest:
                power, square_edge = column(power, power)
                stats['odd_power_squarings'] += 1
            evidence['odd_power_chain'].append({'bit': bit, 'selected': selected,
                'value': value, 'multiply_edge': multiply_edge, 'square_edge': square_edge})
            bit += 1
        evidence['b_to_q'] = value
        s = 0
        while value != 1 and s < n:
            value, edge = column(value, value)
            s += 1
            stats['two_part_squarings'] += 1
            evidence['two_part_chain'].append({'s': s, **edge})
        require(value == 1, 'two-part recovery did not return within the proven width bound')
        R, product_operation = arithmetic.multiply(q, 1 << s)
        relation, _, comparison_operation = arithmetic.compare(R, N)
        require(relation < 0, 'unit order must be less than the modulus')
        record.update(status='CERTIFIED', s=s, R=R)
        evidence['order_assembly'] = {'q': q, 'two_power': 1 << s, 'R': R,
            'multiplication_operation': product_operation,
            'order_below_modulus_comparison': comparison_operation}
        evidence['proof_scope'] = 'n removes all 2-power order; odd first return is exact q; first square return of b^q is exact 2^s'
        return finish()
    except ValueError as error:
        record['status'] = 'REJECTED'
        evidence['error'] = str(error)
        failed = finish()
        raise OddPartDiscoveryError(str(error), failed, failed['metrics']) from error


def _canonical_scientific(value):
    """Strict JSON types; only process-cache native-call deltas are excluded."""
    if isinstance(value, dict):
        require(all(type(k) is str for k in value), 'certificate keys must be JSON strings')
        return {k: _canonical_scientific(v) for k, v in value.items()
                if k not in ('native_kernel_calls_delta', 'actual_native_core_calls_delta')}
    if isinstance(value, (tuple, list)):
        return [_canonical_scientific(v) for v in value]
    require(value is None or type(value) in (str, int, bool), 'noncanonical certificate leaf type')
    return value


def canonical_scientific_bytes(value):
    return json.dumps(_canonical_scientific(value), sort_keys=True,
                      separators=(',', ':'), ensure_ascii=False).encode()


def verify_odd_part_certificate(record):
    """Fresh complete typed replay, accepting serialized JSON records as well.

    PARTIAL records can replay successfully but still certify no order.
    Consume q,s,R only from a CERTIFIED replay. Stored native cache-call
    deltas are not independently authenticated by the semantic comparison.
    """
    require(type(record) is dict and record.get('schema') == SCHEMA, 'odd-part certificate schema required')
    require(record.get('status') in ('CERTIFIED', 'PARTIAL'), 'completed discovery attempt required')
    canonical_scientific_bytes(record)  # reject malformed/mixed keys before execution
    inputs = record['inputs']
    replay = discover_odd_part(inputs['N'], inputs['b'], inputs['odd_budget'])
    if canonical_scientific_bytes(record) != canonical_scientific_bytes(replay):
        raise OddPartCertificateError('complete odd-part discovery certificate does not replay',
                                      {'attempted_certificate': deepcopy(record), 'replay': replay})
    return {'verified': True, 'replay': replay,
            'scope': 'strict scientific and deterministic resource replay; dynamic native cache-call deltas excluded'}
