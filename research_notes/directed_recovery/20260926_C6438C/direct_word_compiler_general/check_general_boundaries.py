"""Bounded input, strict-scale and cursor checks for the general constructor."""
from copy import deepcopy
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import construct_general_word as direct
from stage45.brc_loop_recheck import CALLS

ROOT = Path(__file__).resolve().parent
saved = direct.read(ROOT/'M3_EIGHTH_PAIR_PARTIAL.json.gz')
checks = []


def rejected(name, *, m=3, tolerance='1/8', pair_budget=0,
             square_label_limit=256, previous=None):
    start = len(CALLS)
    try:
        direct.build(m, tolerance, pair_budget, square_label_limit, previous)
    except ValueError as exc:
        checks.append({'case': name, 'rejected': True, 'reason': str(exc),
                       'actual_core_calls': len(CALLS)-start})
    else:
        raise AssertionError(name+' was accepted')


for label, value in [('zero_tolerance', '0'), ('negative_tolerance', '-1/8'),
                     ('float_tolerance', 0.125)]:
    rejected(label, tolerance=value)
rejected('phase_below_three', m=2)
rejected('boolean_phase', m=True)
rejected('negative_pair_budget', pair_budget=-1)
rejected('negative_square_budget', square_label_limit=-1)
rejected('changed_phase_cursor', m=4, previous=saved)
rejected('changed_tolerance_cursor', tolerance='1/4', previous=saved)
rejected('reduced_square_budget', square_label_limit=32, previous=saved)
bad = deepcopy(saved)
bad['request']['denominator_exponent'] += 1
rejected('changed_derived_denominator', previous=bad)
bad = deepcopy(saved)
bad['four_square_search']['records'][0]['observed_pair_sum'] = 1
rejected('changed_observed_pair', previous=bad)

obs = direct.compiler.PositivePathObserver()
scale_cases = []
for tolerance, expected in [(F(8), 2), (F(4), 4)]:
    bits, scale, probes = direct.choose_scale(obs, tolerance)
    assert bits == expected
    scale_cases.append({'tolerance': str(tolerance), 'B': bits, 'scale': scale,
                        'actual_probes': probes, 'passed': True})
# For delta = 4, B = 3 gives equality and must not be accepted.
assert scale_cases[1]['actual_probes'][1]['signed_observation'] == '0'

result = {'status': 'AUTHOR_ACTUAL_BOUNDED_CHECKS_NOT_ADMITTED',
          'source': direct.source_binding(), 'negative_controls': checks,
          'strict_scale_boundary_cases': scale_cases,
          'actual_boundary_observer_operations': obs.operations,
          'actual_core_call_count': len(CALLS), 'native_core_calls': CALLS,
          'scope': 'parameter and cursor boundaries; no new phase, ideal reference or Shor execution'}
raw = direct.compiler.packed(result)
(ROOT/'GENERAL_BOUNDARY_CHECKS.json.gz').write_bytes(gzip.compress(raw, mtime=0))
summary = {k:v for k,v in result.items() if k not in (
    'native_core_calls', 'actual_boundary_observer_operations')}
summary['payload_sha256'] = hashlib.sha256(raw).hexdigest()
(ROOT/'GENERAL_BOUNDARY_CHECKS.summary.json').write_text(
    json.dumps(summary, indent=2)+'\n', encoding='utf-8')
print(json.dumps(summary))
