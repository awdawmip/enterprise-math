"""Execute only the declared provenance-retaining BRC extension/certificates."""
from __future__ import annotations
from itertools import product
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import brc_x6_extension as e

root = Path(__file__).parent
checks = {}

def check(group, predicate):
    if not predicate:
        raise AssertionError(group)
    checks[group] = checks.get(group, 0) + 1

# Exhaustive finite input cover: every raw X6 point with coordinates -1,0,1.
for number, x in enumerate(product((-1, 0, 1), repeat=6)):
    b = e.branch(f'cube-{number}', x)
    c, h = e.c12(b), e.c4(b)
    check('integral_reconstruction', e.decode(c, h) == x)
    check('length_decomposition', 3*e.native_length_square(b) ==
          2*e.norm12_pair(c)[0] + h[0]**2 + h[1]**2)
    tb, ub = e.transform(b, 'T'), e.transform(b, 'U')
    check('T_intertwiner', (e.c12(tb), e.c4(tb)) == e.observed_T(c, h))
    check('U_intertwiner', (e.c12(ub), e.c4(ub)) == e.observed_U(c, h))
    check('two_observation_reconstruction', e.decode_two_observations(c, e.c12(ub)) == x)
    check('U_involution', e.transform(ub, 'U').x == x)
    check('positive_CWM_retained', b.cwm == tb.cwm == ub.cwm)
    check('coordinate_length_retained', e.native_length_square(b) ==
          e.native_length_square(tb) == e.native_length_square(ub))
    current = b
    for n in range(1, 13):
        current = e.transform(current, 'T')
        check('CWM_each_T_step', current.cwm == b.cwm)
        if n == 6:
            check('six_step_reversal', current.x == tuple(-z for z in x))
        if n == 12:
            check('twelve_step_return', current.x == x)
    # Every declared word through depth three, checked in both representations.
    for n in range(4):
        for word in product(('T', 'U'), repeat=n):
            direct, cc, hh = b, c, h
            for op in word:
                direct = e.transform(direct, op)
                cc, hh = (e.observed_T if op == 'T' else e.observed_U)(cc, hh)
            check('word_intertwiner', (e.c12(direct), e.c4(direct)) == (cc, hh))
            check('word_provenance', direct.source_id == b.source_id and
                  direct.operation_history == word)

# Primitive adjacency is checked by action on the 12 signed generators.
origin = e.branch('origin', (0,)*6)
for axis in range(6):
    for sign in (-1, 1):
        x = tuple(sign if j == axis else 0 for j in range(6))
        b = e.branch(f'neighbor-{axis}-{sign}', x)
        for op in ('T', 'U'):
            y = e.transform(b, op)
            check('primitive_adjacency', sum(abs(v) for v in y.x) == 1)

# The exact two-dimensional integer kernel is exercised beyond the cube.
for s, t in product(range(-3, 4), repeat=2):
    b = e.branch(f'kernel-{s}-{t}', (s, t, -s, -t, s, t))
    check('kernel_C12_zero', e.c12(b) == (0,)*4)
    check('kernel_C4', e.c4(b) == (3*s, 3*t))
    check('kernel_U_reveals_nonzero', (e.c12(e.transform(b, 'U')) == (0,)*4) == (s == t == 0))

# Integral image mod 3: exactly 3^4 of 3^6 pairs are compatible.
compatible = 0
for values in product(range(3), repeat=6):
    c, h = values[:4], values[4:]
    expected = ((h[0]-c[0]+c[2]) % 3 == 0 and (h[1]-c[1]+c[3]) % 3 == 0)
    try:
        x = e.decode(c, h)
    except ValueError:
        check('gluing_rejection', not expected)
    else:
        compatible += 1
        b = e.branch('gluing', x)
        check('gluing_acceptance', expected and (e.c12(b), e.c4(b)) == (c, h))
check('gluing_index_nine', compatible == 81)

# Two raw configurations with equal CWM, length AND complete C12 readout.
a = e.branch('same-source', (1, 0, 0, 0, 2, 0))
b = e.branch('same-source', (-1, 0, 2, 0, 0, 0))
ua, ub = e.transform(a, 'U'), e.transform(b, 'U')
check('witness_before_same', e.c12(a) == e.c12(b) and a.cwm == b.cwm and
      e.native_length_square(a) == e.native_length_square(b) == 5)
check('witness_after_distinct', e.c12(ua) != e.c12(ub))
check('witness_norms', e.norm12_pair(e.c12(a)) == e.norm12_pair(e.c12(b)) == (3, 0) and
      e.norm12_pair(e.c12(ua)) == (7, 0) and e.norm12_pair(e.c12(ub)) == (3, 0))

# Actual alternative and serial positive CWM composition, separate observer.
fam = e.alternatives((e.branch('a', a.x, Fraction(1, 2)),),
                     (e.branch('b', b.x, Fraction(2, 3)),),
                     (e.branch('c', (0,1,0,0,0,0), Fraction(5,4)),))
summ = e.positive_summary(fam)
check('three_branch_CWM', (summ.count, summ.total, summ.dominant) ==
      (3, Fraction(29,12), Fraction(5,4)))
transformed = tuple(e.transform(v, 'T', Fraction(2,3)) for v in fam)
expected_cwm = e.call('cwm_propagate', summ, e.call('cwm_edge', Fraction(2,3)))
check('serial_alternative_distributivity', e.positive_summary(transformed) == expected_cwm)
c = e.weighted_observer(fam)
expected_obs = tuple(Fraction(2,3)*v for v in (-c[3], c[0], c[1]+c[3], c[2]))
check('weighted_observer_intertwiner', e.weighted_observer(transformed) == expected_obs)

receipt = {
    'schema': 'PROVISIONAL_BRC_X6_EULER_CERTIFICATE_V1',
    'status': 'FINITE_EXACT_CHECKS_PASSED_NOT_FORMALLY_ADMITTED',
    'source_commit': e.SOURCE_COMMIT, 'source_path': e.SOURCE_PATH,
    'source_blob': e.SOURCE_BLOB,
    'loader': 'Full byte-verified source, unmodified CWM AST core only; no LN imports/stubs.',
    'extension': 'brc_x6_extension.py',
    'declared_actions': {'T': 'signed six-axis cycle', 'U': 'reverse axes 5 and 6'},
    'action_index_is_physical_time': False,
    'physical_force_law_derived': False,
    'extension_independently_reviewed': False,
    'cube_domain': {'coordinate_values': [-1,0,1], 'states': 729},
    'words': {'alphabet':['T','U'], 'max_depth':3, 'words_per_state':15},
    'kernel_domain': {'s_t_min':-3, 's_t_max':3, 'states':49},
    'gluing_domain_mod3': {'pairs':729, 'accepted':compatible, 'index':9},
    'checks_by_group': checks, 'total_checks':sum(checks.values()),
    'actual_source_CWM_calls': e.CALL_COUNTS,
    'witness': {'before_A':e.observation(a), 'before_B':e.observation(b),
                'after_U_A':e.observation(ua), 'after_U_B':e.observation(ub)},
    'weighted_population': [e.observation(v) for v in fam],
    'weighted_population_after_serial_edge': [e.observation(v) for v in transformed],
    'excluded_claims': ['physical rotation law','native triad-incidence preservation',
                        'energy or quantum mechanism','algorithmic speedup','full repository test suite'],
    'file_sha256': {p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in [root/'brc_x6_extension.py', root/'check_certificate.py', e.SOURCE_LOCAL]},
}
(root/'evidence/certificate.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({k:receipt[k] for k in ['status','total_checks','checks_by_group','actual_source_CWM_calls']}, indent=2))
print('witness C12:', e.c12(a), e.c12(b), '->', e.c12(ua), e.c12(ub))
print('witness norm:',e.norm12_pair(e.c12(a)), e.norm12_pair(e.c12(b)), '->', e.norm12_pair(e.c12(ua)), e.norm12_pair(e.c12(ub)))
