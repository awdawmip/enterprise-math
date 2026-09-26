"""Conditional order reduction: a generic exact prefix-row oracle is powerful.

This pays for the supplied oracle. It is not a fast order-finding algorithm.
All post-query arithmetic uses the inherited typed unsigned transducers.
"""
from pathlib import Path
import hashlib
from checkpoint_row_oracle import CheckpointRowOracle
from single_walker import PointRowOracle
from lazy_modular import Arithmetic


def typed_power(arithmetic, base, exponent, modulus):
    result, current, remaining = 1, base, exponent
    steps = []
    while remaining:
        item = {'remaining': remaining, 'current': current, 'result_before': result}
        if remaining & 1:
            result, item['multiply'] = arithmetic.modmul(result, current, modulus)
        remaining >>= 1
        if remaining:
            current, item['square'] = arithmetic.modmul(current, current, modulus)
        item['result_after'] = result
        steps.append(item)
    return result, steps


def order_from_row_oracle(oracle):
    if not isinstance(oracle, PointRowOracle):
        raise ValueError('admitted actual program row oracle required')
    program = oracle.program
    n = (program.N-1).bit_length()
    depth = 2*n-1
    if program.t != 2*n or oracle.history != (0,)*depth:
        raise ValueError('default-width all-zero pre-final prefix required')
    row = oracle.query(depth, 1)
    if row.values[0] <= 0 or any(row.values[1:]):
        raise ValueError('zero-prefix complete row has wrong form')
    arithmetic = Arithmetic()
    quotient, remainder, division = arithmetic.divide(row.den, row.values[0])
    s = quotient
    addition = None
    if remainder:
        s, addition = arithmetic.add(quotient, 1)
    if not 1 <= s < program.N:
        raise ValueError('oracle implies impossible squared-base order')
    power, steps = typed_power(arithmetic, program.a, s, program.N)
    r = s if power == 1 else s << 1
    verified_power, final_steps = typed_power(arithmetic, program.a, r, program.N)
    if verified_power != 1:
        raise ValueError('oracle-derived order fails typed power verification')
    return {'N': program.N, 'a': program.a, 't': program.t,
        'depth': depth, 'history': oracle.history, 'row': row,
        'squared_base_order': s, 'base_order': r,
        'top_level_complete_row_queries': 1,
        'ceil_inverse': {'quotient': quotient, 'remainder': remainder,
                         'division_operation': division, 'increment_operation': addition},
        'base_to_s': power, 'base_to_s_steps': steps,
        'base_to_r': verified_power, 'base_to_r_steps': final_steps,
        'arithmetic_operations': arithmetic.operations, 'arithmetic_cost': arithmetic.stats,
        'oracle_cost_must_be_added': True, 'conditional_on_correct_generic_row_oracle': True,
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
