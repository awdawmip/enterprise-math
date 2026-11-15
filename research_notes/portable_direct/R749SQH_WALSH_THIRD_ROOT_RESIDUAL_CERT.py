#!/usr/bin/env python3
"""R749SQH: exact cubic-root leading correction to inherited R749SQG count.
Requires sibling R749SQG_WALSH_QUASIPOLYNOMIAL_CERT.py, Python stdlib only.
"""
from contextlib import redirect_stdout
from fractions import Fraction
from io import StringIO
from math import comb, factorial
from pathlib import Path
import json
import runpy

upstream = Path(__file__).with_name('R749SQG_WALSH_QUASIPOLYNOMIAL_CERT.py')
with redirect_stdout(StringIO()):
    prior = runpy.run_path(str(upstream))
C, P, Q9 = (prior[k] for k in ('C', 'P', 'Q2'))
step, order = 420, 7
assert len(C) == 9 * step

class_counts = {"r_mod_3_0": 0, "r_mod_3_1": 0, "r_mod_3_2": 0}
examples = {}
for first in range(1, step + 1):
    values = [C[first + j * step - 1] - P(first + j * step) - (-1) ** (first + j * step - 1) * Q9(first + j * step)
              for j in range(order + 1)]
    seventh = sum((-1) ** (order - j) * comb(order, j) * values[j] for j in range(order + 1))
    proposed = Fraction((1 - 3 * (first % 3 == 0)) * step ** order, 4 * 3 ** 16)
    assert seventh == proposed, (first, seventh, proposed)
    class_counts[f'r_mod_3_{first % 3}'] += 1
    if first in (1, 2, 3, 4, 5, 6):
        examples[str(first)] = {'actual_420_step_seventh_difference': str(seventh),
                                'predicted': str(proposed)}
assert list(class_counts.values()) == [140, 140, 140]

result = {
    'schema': 'R749SQH_WALSH_THIRD_ROOT_LEADING_PERIODIC_RESIDUAL_V1',
    'status': 'PASS',
    'scientific_pin': 'a72226e2430ffa4786321ac86e7f0c599d5f0389',
    'upstream': 'R749SQG_WALSH_QUASIPOLYNOMIAL_CERT.py at PR #2495',
    'model': 'auxiliary 16-atom Walsh 23-positive-slack-count model',
    'roots': 'primitive cube roots rho and rho^2',
    'pole_orders': {'primitive_3': 8, 'primitive_4': 4, 'primitive_5': 3, 'primitive_6': 2, 'primitive_7': 1},
    'leading_factor': '(1-3*indicator(3|r))/(4*3^16*7!)',
    'r_mod_3_leading_coefficients': {'0': str(Fraction(-2, 4 * 3 ** 16 * factorial(7))),
                                   '1': str(Fraction(1, 4 * 3 ** 16 * factorial(7))),
                                   '2': str(Fraction(1, 4 * 3 ** 16 * factorial(7)))},
    'validation': {'exact_integer_r_range': '1..3780',
                   'all_420_residue_classes_checked': True,
                   'seventh_420_step_difference': '(1-3*indicator(3|r))*420^7/(4*3^16)',
                   'arithmetic': 'integer and fractions.Fraction only, no floats',
                   'counts': class_counts, 'examples': examples},
    'status_scope': 'AUTHOR_EXACT_NOT_REVIEWED; symbolic cube-root pole derivation proves all r>=1, numerical check is independent finite consistency'
}
print(json.dumps(result, ensure_ascii=False, indent=2))
