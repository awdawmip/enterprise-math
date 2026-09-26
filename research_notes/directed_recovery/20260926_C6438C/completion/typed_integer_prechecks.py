"""BRC full-adder integer transducers for exact factoring prechecks.

Only bit wiring/control and columns of sparse.native_adder construct values.
Multiplication is shift-add; division is binary long division. Every digit
column, bypass, carry, quotient bit and root-search decision is retained.
Wilson decides primality and does not return a factor of a composite integer.
This intentionally simple completeness baseline is not an efficiency claim.
"""
from __future__ import annotations
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'sparse'))
from sparse_modular import add_unsigned, native_adder, integer, digest


def uint(value):
    if not integer(value) or value < 0:
        raise ValueError('nonnegative non-boolean integer required')


def add(left, right):
    uint(left); uint(right)
    width = max(left.bit_length(), right.bit_length(), 1) + 1
    value, carry, trace = add_unsigned(left, right, width)
    if carry:
        raise AssertionError('declared full sum width overflowed')
    return value, trace


def compare(left, right):
    """Two's-complement subtraction from two executed adder transducers."""
    uint(left); uint(right)
    width = max(left.bit_length(), right.bit_length(), 1) + 1
    complement = (~right) & ((1 << width) - 1)  # fixed bitwise NOT wiring
    low, carry0, first = add_unsigned(left, complement, width)
    difference, carry1, second = add_unsigned(low, 1, width)
    nonnegative = bool(carry0 or carry1)
    relation = 0 if difference == 0 and nonnegative else 1 if nonnegative else -1
    return relation, {
        'operation':'BRC_UNSIGNED_COMPARE', 'left':left, 'right':right,
        'width':width, 'bitwise_complement':complement,
        'first_add':first, 'second_add':second,
        'nonnegative':nonnegative, 'low_difference':difference,
        'relation':relation,
    }


def multiply(left, right):
    uint(left); uint(right)
    width = max(1, left.bit_length() + right.bit_length())
    value = 0
    steps = []
    for bit in range(right.bit_length()):
        selected = (right >> bit) & 1
        term = left << bit
        if selected:
            following, carry, trace = add_unsigned(value, term, width)
            if carry:
                raise AssertionError('full product width overflowed')
        else:
            following, trace = value, None
        steps.append({'bit':bit, 'selected':selected, 'input':value,
                      'wired_term':term, 'output':following,
                      'adder':trace, 'bypass':not bool(selected)})
        value = following
    return value, {'operation':'BRC_UNSIGNED_SHIFT_ADD', 'left':left,
                   'right':right, 'width':width, 'steps':steps, 'value':value}


def divide(value, modulus):
    uint(value); uint(modulus)
    if modulus == 0:
        raise ValueError('positive divisor required')
    quotient = remainder = 0
    steps = []
    for bit in reversed(range(value.bit_length())):
        incoming = (value >> bit) & 1
        shifted = (remainder << 1) | incoming
        relation, subtraction = compare(shifted, modulus)
        qbit = int(relation >= 0)
        following = subtraction['low_difference'] if qbit else shifted
        quotient = (quotient << 1) | qbit
        steps.append({'bit':bit, 'input_remainder':remainder,
                      'input_bit':incoming, 'wired_shift':shifted,
                      'subtract_modulus':subtraction,
                      'quotient_bit':qbit, 'output_remainder':following})
        remainder = following
    return quotient, remainder, {'operation':'BRC_UNSIGNED_LONG_DIVISION',
        'value':value, 'modulus':modulus, 'steps':steps,
        'quotient':quotient, 'remainder':remainder}


def power(base, exponent):
    uint(base); uint(exponent)
    value = 1
    b = base
    rest = exponent
    steps = []
    bit = 0
    while rest:
        selected = rest & 1
        if selected:
            following, multiply_trace = multiply(value, b)
        else:
            following, multiply_trace = value, None
        rest >>= 1
        if rest:
            next_b, square_trace = multiply(b, b)
        else:
            next_b, square_trace = b, None
        steps.append({'bit':bit, 'selected':selected, 'input':value,
                      'base_power':b, 'multiply':multiply_trace,
                      'output':following, 'square':square_trace,
                      'next_base_power':next_b})
        value, b = following, next_b
        bit += 1
    return value, {'operation':'BRC_UNSIGNED_POWER', 'base':base,
                   'exponent':exponent, 'steps':steps, 'value':value}


def perfect_power(N):
    if not integer(N) or N < 2:
        raise ValueError('N must be an integer >= 2')
    _, primitive = native_adder()
    searches = []
    result = None
    # An integer base >=2 implies exponent <= floor(log2 N).
    for exponent in range(N.bit_length() - 1, 1, -1):
        lo, hi = 2, 1 << ((N.bit_length() + exponent - 1)//exponent)
        initial_hi = hi
        probes = []
        while lo <= hi:
            total, middle_add = add(lo, hi)
            middle = total >> 1
            value, exponentiation = power(middle, exponent)
            relation, comparison = compare(value, N)
            row = {'lo':lo, 'hi':hi, 'midpoint_add':middle_add,
                   'middle':middle, 'power':exponentiation,
                   'comparison':comparison, 'relation':relation}
            if relation == 0:
                row['decision'] = 'EQUAL_POWER'
                result = {'base':middle, 'exponent':exponent}
                probes.append(row)
                break
            if relation < 0:
                lo, change = add(middle, 1)
                row.update(decision='RAISE_LO', next_lo=lo, bound_arithmetic=change)
            else:
                _, change = compare(middle, 1)
                hi = change['low_difference']
                row.update(decision='LOWER_HI', next_hi=hi, bound_arithmetic=change)
            probes.append(row)
        searches.append({'exponent':exponent, 'initial_lo':2,
                         'initial_hi':initial_hi, 'probes':probes,
                         'final_lo':lo, 'final_hi':hi})
        if result is not None:
            break
    return {'schema':'BRC_PERFECT_POWER_V1', 'N':N,
            'status':'PERFECT_POWER' if result else 'NOT_A_PERFECT_POWER',
            'power':result, 'native_adder':primitive, 'searches':searches,
            'scope':'integer root binary searches over exponents; no trial divisors or Shor order input',
            'admission':'AUTHOR_EXECUTED_UNREVIEWED_NOT_ADMITTED'}


def wilson_primality(N):
    if not integer(N) or N < 2:
        raise ValueError('N must be an integer >= 2')
    _, primitive = native_adder()
    value = 1
    steps = []
    for factor in range(2, N):
        product, multiplication = multiply(value, factor)
        _, remainder, reduction = divide(product, N)
        steps.append({'factor':factor, 'input_residue':value,
                      'multiply':multiplication, 'reduce':reduction,
                      'output_residue':remainder})
        value = remainder
    _, subtract_one = compare(N, 1)
    minus_one = subtract_one['low_difference']
    relation, equality = compare(value, minus_one)
    return {'schema':'BRC_WILSON_PRIMALITY_V1', 'N':N,
            'status':'PRIME' if relation == 0 else 'COMPOSITE',
            'native_adder':primitive, 'steps':steps,
            'factorial_residue':value, 'subtract_one':subtract_one,
            'comparison_to_minus_one':equality,
            'modular_products':max(0,N-2),
            'scope':'exact Wilson criterion; decides primality only; no composite factor returned',
            'cost':'O(N) typed modular products, exponential in integer bit length',
            'admission':'AUTHOR_EXECUTED_UNREVIEWED_NOT_ADMITTED'}


def verify_precheck(certificate):
    schema = certificate.get('schema')
    if schema == 'BRC_PERFECT_POWER_V1':
        rebuilt = perfect_power(certificate['N'])
    elif schema == 'BRC_WILSON_PRIMALITY_V1':
        rebuilt = wilson_primality(certificate['N'])
    else:
        raise ValueError('unsupported BRC precheck certificate')
    if digest(certificate) != digest(rebuilt):
        raise ValueError('BRC precheck certificate does not replay from actual primitive')
    return {'verified':True, 'schema':schema, 'N':certificate['N'],
            'status':certificate['status'], 'certificate_sha256':digest(certificate)}
