"""Portable exact unit84 regression: signed X6 min-zero quotient vs positive-only transition.

Fixed scientific input: Enterprise Math P000 V5 signed Z^6, unit ± axes.
No assertion about author identity, native benchmark or historical bad caller.
"""
from collections import Counter
from itertools import product
from hashlib import sha256
import json

D = 6
STEPS_SIGNED = tuple((i, sign) for i in range(D) for sign in (-1, 1))
STEPS_POSITIVE = tuple((i, 1) for i in range(D))
ZERO = (0,) * D


def canonical(z):
    m = min(z)
    return tuple(v - m for v in z)


def step(z, axis, sign):
    a = list(z)
    a[axis] += sign
    return tuple(a)


def evolve(initial, steps, length):
    states = Counter({initial: 1})
    for _ in range(length):
        out = Counter()
        for state, multiplicity in states.items():
            for axis, sign in steps:
                out[step(state, axis, sign)] += multiplicity
        states = out
    return states


def projected(states):
    out = Counter()
    for state, mass in states.items():
        out[canonical(state)] += mass
    return out


def quotient_evolve(relative, steps, length):
    out = Counter({relative: 1})
    for _ in range(length):
        nxt = Counter()
        for state, mult in out.items():
            for axis, sign in steps:
                nxt[canonical(step(state, axis, sign))] += mult
        out = nxt
    return out


def check(test, label):
    if not test:
        raise AssertionError(label)


def run():
    # Every binary min-zero observer: 2^6-1 = 63. Depth never enters quotient updates.
    observers = [r for r in product((0, 1), repeat=D) if min(r) == 0]
    depths = (-2, 0, 3)
    nchecks = 0
    shift_tests = 0
    for r in observers:
        quotient = [quotient_evolve(r, STEPS_SIGNED, length) for length in range(4)]
        for depth in depths:
            z = tuple(x + depth for x in r)
            for length in range(4):
                observed = projected(evolve(z, STEPS_SIGNED, length))
                check(observed == quotient[length], f'failed strong lumping: {r} {depth} {length}')
                check(sum(observed.values()) == 12**length, f'mass count {r} {depth} {length}')
                nchecks += 2
                shift_tests += 1
    at_zero_signed = quotient_evolve(ZERO, STEPS_SIGNED, 1)
    at_zero_positive = quotient_evolve(ZERO, STEPS_POSITIVE, 1)
    check(len(at_zero_signed) == 12, 'signed 12 distinct one-step readouts')
    check(len(at_zero_positive) == 6, 'positive 6 distinct one-step readouts')
    check(sum(at_zero_signed.values()) == 12, 'signed one-step mass')
    check(sum(at_zero_positive.values()) == 6, 'positive one-step mass')
    check(set(at_zero_positive) < set(at_zero_signed), 'strict positive subset at zero')
    nchecks += 5
    # Native G and T are not invariant under discarded diagonal depth.
    check(canonical(ZERO) == canonical((1,) * D), 'same observer')
    check(sum(v*v for v in ZERO) == 0 and sum(v*v for v in (1,)*D) == 6, 'G nonfactor')
    check(sum(abs(v) for v in ZERO) == 0 and sum(abs(v) for v in (1,)*D) == 6, 'T nonfactor')
    nchecks += 3
    return {
        'schema': 'EM_X6_UNIT84_SIGNED_RELATIVE_STRONG_LUMPABILITY_V1',
        'date': '2026-11-17',
        'science_pin': '59538f585d037d09ef687b28715c4bc1a3f9fe03',
        'domain': 'signed Z^6 chart-relative displacement, not final cell address',
        'observer': 'rho(z)=z-min(z)*1',
        'operation': 'uniform nonnegative labeled paths on 12 signed unit directions',
        'tested_binary_minzero_observers': len(observers),
        'tested_integer_depths': list(depths),
        'tested_length_range': [0,3],
        'signed_direct_projected_vs_quotient_comparisons': shift_tests,
        'explicit_integer_checks': nchecks,
        'failed_checks': 0,
        'zero_signed_one_step_distinct_readouts': len(at_zero_signed),
        'zero_positive_one_step_distinct_readouts': len(at_zero_positive),
        'zero_signed_total_mass': sum(at_zero_signed.values()),
        'zero_positive_total_mass': sum(at_zero_positive.values()),
        'nonfactoring_native_G_pair': [0,6],
        'nonfactoring_native_T_pair': [0,6],
        'formal_review': 'NOT_REVIEWED',
        'native_source_semantic_publication': 'NOT_SUBMITTED',
    }


if __name__ == '__main__':
    result = run()
    data = (json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + '\n').encode('utf-8')
    output = __file__.replace('_CHECK_20261117.py', '_RESULTS_20261117.json')
    with open(output, 'wb') as f:
        f.write(data)
    print(data.decode('utf-8'))
    print('sha256', sha256(data).hexdigest())
