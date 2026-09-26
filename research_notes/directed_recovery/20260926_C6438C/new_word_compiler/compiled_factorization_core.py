from __future__ import annotations
# Derived from the existing verified recursive factorization driver.
# The only algorithmic loop change preserves unfinished compilation as a leaf.
from pathlib import Path as _Path
import sys as _sys
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / 'integration'))

class CompilationPending(Exception):
    def __init__(self, report):
        super().__init__('Complete phase bank is not yet certified')
        self.report = report

"""Certificate-bearing recursive factorization around the sparse BRC Shor core.

Exact prechecks finish prime/prime-power/even leaves. Other composite leaves
are split only by the actual sampled Shor driver or its native gcd precheck.
An exhausted budget leaves a visible unresolved cofactor; it never proves prime.
"""
from fractions import Fraction as F
from pathlib import Path
import sys, json
from general_streaming import GeneralStreamingProgram, ROOT
from general_driver import factor_attempts
sys.path.insert(0, str(ROOT.parent / 'completion'))
from typed_integer_prechecks import perfect_power, wilson_primality, verify_precheck, multiply, divide, power, add
from sparse_modular import sparse_modular_columns, integer, digest


def factor_integer(N, rng, phase_provider, *, failure_bits=16, max_attempts=None, base_provider=None):
    """Finite-attempt complete/partial result, without a hidden factor oracle.

    phase_provider(t) returns (bank, dim, error_certificate), whose
    terminal_TV_bound is a uniform whole-instrument bound to ideal Shor.
    For the probability theorem, rng supplies conditionally uniform draws and
    base_provider is absent. An explicit base_provider is a replay policy.
    A budget override remains visible and may weaken the probability guarantee.
    """
    if not integer(N) or N < 2: raise ValueError('integer N >= 2 required')
    if not integer(failure_bits) or failure_bits < 1: raise ValueError('positive failure_bits required')
    if max_attempts is not None and (not integer(max_attempts) or max_attempts < 1):
        raise ValueError('positive optional max_attempts required')
    n_initial = (N - 1).bit_length()
    node_bits = failure_bits + (n_initial - 1).bit_length()
    pending = [(N, 1)]; primes = {}; unresolved = []; events = []; certificates = {}
    guaranteed_budget = base_provider is None

    def retain(cert):
        checked = verify_precheck(cert); key = checked['certificate_sha256']
        certificates[key] = cert
        return key

    while pending:
        value, multiplicity = pending.pop()
        if value == 1: continue
        q, rem, divtrace = divide(value, 2)
        if rem == 0 and value != 2:
            events.append({'input': value, 'multiplicity': multiplicity,
                'action': 'EXACT_EVEN_SPLIT', 'division': divtrace})
            pending.extend([(2, multiplicity), (q, multiplicity)])
            continue
        pp = perfect_power(value); pp_id = retain(pp)
        if pp['status'] == 'PERFECT_POWER':
            base, exponent = pp['power']['base'], pp['power']['exponent']
            new_multiplicity, mult_trace = multiply(multiplicity, exponent)
            events.append({'input': value, 'multiplicity': multiplicity,
                'action': 'EXACT_PERFECT_POWER', 'certificate_id': pp_id,
                'multiplicity_product': mult_trace})
            pending.append((base, new_multiplicity)); continue
        primality = wilson_primality(value); prime_id = retain(primality)
        if primality['status'] == 'PRIME':
            if value in primes:
                primes[value]['exponent'], add_trace = add(primes[value]['exponent'], multiplicity)
            else:
                primes[value] = {'prime': value, 'exponent': multiplicity, 'certificate_id': prime_id}
                add_trace = None
            events.append({'input': value, 'multiplicity': multiplicity,
                'action': 'CERTIFIED_PRIME', 'certificate_id': prime_id,
                'exponent_addition': add_trace})
            continue
        n = (value - 1).bit_length(); t = 2 * n
        try:
            bank, dim, error = phase_provider(t)
        except CompilationPending as exc:
            guaranteed_budget = False
            events.append({'input': value, 'multiplicity': multiplicity,
                'action': 'COMPILATION_PARTIAL',
                'non_perfect_power_certificate_id': pp_id,
                'composite_certificate_id': prime_id, 't': t,
                'compilation': exc.report})
            unresolved.append({'cofactor': value, 'multiplicity': multiplicity,
                'status': 'COMPILATION_PARTIAL', 'event_index': len(events)-1})
            continue
        epsilon = F(error['terminal_TV_bound'])
        if not 0 <= epsilon <= 1: raise ValueError('terminal TV certificate must lie in [0,1]')
        gamma = F(1, 8 * n) - epsilon
        certified_R = ((gamma.denominator + gamma.numerator - 1) // gamma.numerator) * node_bits if gamma > 0 else None
        # Lack of a useful conservative bound does not prevent an actual run.
        # Its stopping budget and missing guarantee are made explicit.
        R = max_attempts if max_attempts is not None else certified_R or 16 * n * node_bits
        guaranteed_budget &= certified_R is not None and R >= certified_R
        factory = lambda number, a, width: GeneralStreamingProgram(number, a, width, bank, dim,
            column_factory=sparse_modular_columns)
        bases = None if base_provider is None else base_provider(value)
        attempt = factor_attempts(value, t, R, rng, factory, bases=bases)
        events.append({'input': value, 'multiplicity': multiplicity,
            'action': 'SAMPLED_SHOR_SPLIT', 'non_perfect_power_certificate_id': pp_id,
            'composite_certificate_id': prime_id, 't': t,
            'error_certificate': json.loads(json.dumps(error, default=str)),
            'per_attempt_success_lower_bound': str(max(F(0), gamma)),
            'node_failure_bits': node_bits, 'certified_attempt_budget': certified_R,
            'actual_attempt_budget': R, 'attempt_result': attempt})
        if attempt['factors']:
            divisor = attempt['factors'][0]
            quotient, remainder, trace = divide(value, divisor)
            if remainder or not 1 < divisor < value or quotient < 2:
                raise AssertionError('Shor returned no proper exact split')
            events[-1]['verified_split'] = trace
            pending.extend([(divisor, multiplicity), (quotient, multiplicity)])
        else:
            unresolved.append({'cofactor': value, 'multiplicity': multiplicity,
                'status': attempt['status'], 'event_index': len(events) - 1})

    product = 1; product_steps = []
    for value, exponent, kind in ([(p, r['exponent'], 'CERTIFIED_PRIME') for p, r in sorted(primes.items())]
            + [(r['cofactor'], r['multiplicity'], 'UNRESOLVED') for r in unresolved]):
        term, ptrace = power(value, exponent)
        product, mtrace = multiply(product, term)
        product_steps.append({'value': value, 'exponent': exponent, 'kind': kind,
            'power': ptrace, 'multiply': mtrace})
    if product != N: raise AssertionError('complete/partial multiplicative ledger does not reconstruct input')
    return {'schema': 'BRC_RECURSIVE_FACTORIZATION_V1', 'N': N,
        'status': 'COMPLETE' if not unresolved else 'PARTIAL',
        'prime_factors': [r for p, r in sorted(primes.items())], 'unresolved': unresolved,
        'events': events, 'certificates': certificates,
        'multiplicative_ledger': {'value': product, 'steps': product_steps, 'exact': True},
        'requested_failure_bits': failure_bits,
        'probability_contract': {
            'uniform_random_source_required': True,
            'explicit_base_policy': base_provider is not None,
            'budgets_meet_uniform_random_bound': bool(guaranteed_budget),
            'bound_if_contract_holds': f'P(any unresolved retry-limit leaf) <= 2^-{failure_bits}' if guaranteed_budget else None,
            'scope': 'Does not cover external randomness exhaustion/interruption; does not turn a PRNG replay into ideal randomness.',
            'transcript_TV_is_a_separate_budget': True},
        'prime_proof': 'Exact Wilson certificates; Shor failure never used as primality',
        'cost_boundary': 'Wilson and work-register size are exponential in input bit length; no polynomial classical factoring claim'}


def verify_factorization(result):
    """Verify every asserted prime and the complete/partial product ledger."""
    if result.get('schema') != 'BRC_RECURSIVE_FACTORIZATION_V1': raise ValueError('wrong result type')
    N = result['N']
    if not integer(N) or N < 2: raise ValueError('invalid input')
    certificates = result['certificates']
    for key, cert in certificates.items():
        checked = verify_precheck(cert)
        if checked['certificate_sha256'] != key: raise ValueError('certificate ID mismatch')
    seen = set(); entries = []
    for row in result['prime_factors']:
        prime, exponent = row['prime'], row['exponent']
        if not integer(prime) or prime < 2 or prime in seen: raise ValueError('invalid or duplicate prime entry')
        if not integer(exponent) or exponent < 1: raise ValueError('invalid exponent')
        cert = certificates[row['certificate_id']]
        if cert['N'] != prime or cert['schema'] != 'BRC_WILSON_PRIMALITY_V1' or cert['status'] != 'PRIME':
            raise ValueError('unproved prime leaf')
        seen.add(prime); entries.append((prime, exponent, 'CERTIFIED_PRIME'))
    if [p for p, e, k in entries] != sorted(seen): raise ValueError('prime ledger order differs')
    for row in result['unresolved']:
        value, exponent = row['cofactor'], row['multiplicity']
        if not integer(value) or value < 2 or not integer(exponent) or exponent < 1:
            raise ValueError('invalid unresolved cofactor')
        entries.append((value, exponent, 'UNRESOLVED'))
    expected_status = 'PARTIAL' if result['unresolved'] else 'COMPLETE'
    if result['status'] != expected_status: raise ValueError('completion status hides unresolved factors')
    product = 1; steps = []
    for value, exponent, kind in entries:
        term, ptrace = power(value, exponent)
        product, mtrace = multiply(product, term)
        steps.append({'value': value, 'exponent': exponent, 'kind': kind, 'power': ptrace, 'multiply': mtrace})
    rebuilt = {'value': product, 'steps': steps, 'exact': True}
    if product != N or digest(rebuilt) != digest(result['multiplicative_ledger']):
        raise ValueError('multiplicative ledger fails actual typed replay')
    return {'verified': True, 'N': N, 'status': expected_status, 'prime_leaves': len(seen),
        'unresolved_cofactors': len(result['unresolved']),
        'certificate_count': len(certificates), 'result_sha256': digest(result),
        'stochastic_budget_verified': False,
        'scope': 'factor claims, prime certificates and multiplicative conservation; stochastic guarantee remains conditional on the declared RNG and uniform compiler bound'}


def certified_phase_provider(t):
    sys.path.insert(0, str(ROOT.parent / 'phases'))
    from closed_phase_bank import load_certified_bank
    bank, intervals, dim, report = load_certified_bank(t, cutoff=33,
        expected_payload_sha256='feecbc02808991f6d7b1e2c3179c8da2018b76901ef34c26ef0d28b65729dd5c')
    certificate = {**report['error_certificate'], 'bank_payload_sha256': report['bank_payload_sha256']}
    return bank, dim, certificate
