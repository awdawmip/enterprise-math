"""Exact least-prime witnesses and CRT cost of a proposed modular patch.

Run from the shared workspace:
  python research_notes/portable_direct/riesel_structure_20261119/verify_prime_dictionary.py --source-dir vendor_src

The BRC core generates the two integer sequence values and algebraic factors.
A standard-library C++ segmented sieve exhausts primes in increasing order.
Its exact base-2^32 limb remainder is cross-checked with Python integer % on
every prime <=10^8. No probable-prime assumption is used.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import gcd, isqrt, lcm, prod
from pathlib import Path
import subprocess
import sys

A = 690786768637635218740714348513373826260012289
EXPECTED = {66: 48324739, 282: 1896714101}
ORDER_DATA = {
    48324739: (16108246, [(2, 1), (7, 1), (11, 2), (37, 1), (257, 1)]),
    1896714101: (1896714100, [(2, 2), (5, 2), (103, 1), (107, 1), (1721, 1)]),
}


def segmented_primes(bound, segment_size=1000000):
    root = isqrt(bound)
    small = bytearray(b'\x01') * (root + 1)
    small[:2] = b'\x00\x00'
    for p in range(2, isqrt(root) + 1):
        if small[p]:
            small[p*p:root+1:p] = b'\x00' * ((root-p*p)//p + 1)
    base = [p for p in range(2, root+1) if small[p]]
    for lo in range(2, bound+1, segment_size):
        hi = min(bound+1, lo+segment_size)
        mark = bytearray(b'\x01') * (hi-lo)
        for p in base:
            if p*p >= hi:
                break
            start = max(p*p, ((lo+p-1)//p)*p)
            if start < hi:
                mark[start-lo:hi-lo:p] = b'\x00' * ((hi-1-start)//p + 1)
        for offset, live in enumerate(mark):
            if live:
                yield lo+offset


def full_trial_prime(p):
    bound = isqrt(p)
    assert p >= 2 and all(p % d for d in range(2, bound+1))
    return {"p": p, "full_trial_division_bound": bound}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-dir', type=Path, default=Path(__file__).resolve().parents[3] / 'src')
    parser.add_argument('--input', type=Path, default=Path(__file__).resolve().parent.with_name('riesel_mixed_20261119') / 'certificate.json')
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('prime_dictionary_results.json'))
    args = parser.parse_args()
    directory = Path(__file__).resolve().parent
    data = json.loads(args.input.read_text())
    assert int(data['optimized']['a']) == A
    sys.path.insert(0, str(args.source_dir))
    from enterprise_math.brc_transport import Affine, EffectHistogram
    step = EffectHistogram.from_terms(1, [(1, Affine(((2,),), (1,)), 1)])
    double = EffectHistogram.from_terms(1, [(1, Affine(((2,),), (0,)), 1)])

    def advance(packet, x):
        (point, weights), = packet.evaluate((x,)).items()
        assert weights.entries == ((Fraction(1), 1),)
        assert point[0].denominator == 1
        return int(point[0])

    examples = {}
    values = {}
    for n in EXPECTED:
        x = A*A-1
        for _ in range(n):
            x = advance(step, x)
        y = A
        for _ in range(n//2):
            y = advance(double, y)
        assert x == (y-1)*(y+1) == A*A*2**n-1
        assert 1 < y-1 < y+1 < x
        values[n] = x
        examples[n] = {'n': n, 'N': str(x), 'minus_factor': str(y-1),
                       'plus_factor': str(y+1), 'algebraic_identity_checked': True}

    # Compile the delivered exact kernel, then retain each actual stdout result.
    executable = directory / 'segmented_prime_divisor'
    subprocess.run(['g++', '-std=c++17', '-O3', str(directory/'segmented_prime_divisor.cpp'), '-o', str(executable)], check=True)
    for n, value in values.items():
        bound = 50000000 if n == 66 else 4294967295
        raw = subprocess.run([str(executable), str(bound)], input=str(value)+'\n', text=True, capture_output=True, check=True)
        observed = json.loads(raw.stdout)
        assert observed['least_prime_divisor'] == EXPECTED[n]
        examples[n]['ordered_cpp_scan'] = observed
        examples[n]['least_prime_divisor'] = EXPECTED[n]

    # This separately evaluates ordinary Python integers, rather than the limb
    # implementation. It exhausts all primes <=100,000,000 for both values.
    cross_bound = 100000000
    first = {n: None for n in EXPECTED}
    first_index = {n: None for n in EXPECTED}
    count = 0
    for p in segmented_primes(cross_bound):
        count += 1
        for n, value in values.items():
            if first[n] is None and value % p == 0:
                first[n], first_index[n] = p, count
    assert count == 5761455
    assert first == {66: 48324739, 282: None}
    assert first_index[66] == examples[66]['ordered_cpp_scan']['primes_checked']

    for n, p in EXPECTED.items():
        assert values[n] % p == 0
        proof = full_trial_prime(p)
        d, factors = ORDER_DATA[p]
        assert prod(q**e for q, e in factors) == d
        factor_proofs = [full_trial_prime(q) for q, _ in factors]
        assert pow(2, d, p) == 1
        order_residues = {str(q): pow(2, d//q, p) for q, _ in factors}
        assert all(r != 1 for r in order_residues.values())
        assert (A*A % p)*pow(2, n, p) % p == 1
        root_residue = (A % p)*pow(2, n//2, p) % p
        assert root_residue in (1, p-1)
        examples[n]['prime_proof'] = proof
        examples[n]['order_certificate'] = {
            'order': d, 'factorization': factors, 'factor_prime_proofs': factor_proofs,
            'pow_2_order_mod_p': 1, 'proper_order_test_residues': order_residues,
            'zero_phase': n % d}
        examples[n]['factor_side'] = 'minus_factor' if root_residue == 1 else 'plus_factor'
        examples[n]['python_crosscheck'] = {
            'bound': cross_bound, 'all_primes_count': count,
            'first_divisor_in_range': first[n], 'index_if_found': first_index[n]}

    rows = data['optimized']['rows']
    old_period = lcm(*(r['order'] for r in rows))
    holes = [n for n in range(old_period)
             if not any(n % r['order'] == r['exponent_phase'] for r in rows)]
    assert old_period == 6720 and len(holes) == 1152
    p = EXPECTED[282]
    d = ORDER_DATA[p][0]
    joint = lcm(old_period, d)
    common = gcd(old_period, d)
    compatible = [n for n in holes if n % common == 282 % common]
    assert common == 20 and len(compatible) == 176
    lifted_holes = len(holes)*(joint//old_period)
    residue_after_old_period = (pow(2, old_period, p)-1) % p
    assert residue_after_old_period != 0
    patch = {
        'new_prime': p, 'new_order': d, 'new_zero_phase': 282,
        'old_period': old_period, 'old_hole_count': len(holes),
        'gcd_periods': common, 'joint_period': joint,
        'old_period_refinement_factor': joint//old_period,
        'new_channel_hits': joint//d, 'newly_filled_old_holes': len(compatible),
        'new_hits_already_covered': joint//d-len(compatible),
        'old_holes_lifted_to_joint_period': lifted_holes,
        'remaining_holes': lifted_holes-len(compatible),
        'compatible_old_hole_classes': compatible,
        'count_proof': 'For each old class h, the two congruences have one intersection mod lcm iff h=282 mod gcd. Other old classes have no intersection.',
        'observer_witness': {'first_n': 282, 'second_n': 282+old_period,
                            'all_old_labelled_residues_equal': True,
                            'new_prime_residue_first': 0,
                            'new_prime_residue_second': residue_after_old_period},
        'labelled_future_phase_states': {'before': old_period, 'after': joint,
            'fixed_bits_before': (old_period-1).bit_length(),
            'fixed_bits_after': (joint-1).bit_length(),
            'scope': 'Exact whole labelled divisor traces under every future shift; each active one-zero-phase channel forces congruence modulo its true order.'},
    }
    result = {
        'schema': 'RIESEL_FINITE_PRIME_DICTIONARY_OBSTRUCTION_V1',
        'researcher_id': 'EM-DIRECT-970E1C',
        'research_activity_id': 'RA-D2EC212845B63844081F9A14',
        'status': 'AUTHOR_PROOF_AND_EXACT_FINITE_COMPUTATION',
        'a': str(A), 'k': str(A*A),
        'project_arithmetic_source_commit': data['project_source_commit'],
        'native_scope': 'Internal exact integer registers at a fixed X6 anchor; n counts arithmetic updates.',
        'brc_entrypoints': ['EffectHistogram.from_terms', 'EffectHistogram.evaluate'],
        'examples': {str(n): value for n, value in examples.items()},
        'necessary_maximum_prime_in_any_full_cover': EXPECTED[282],
        'finite_bound_scope': 'A full finite prime cover, if one exists, must contain a prime at least 1896714101. This is a proved finite lower bound, not unboundedness of least prime divisors.',
        'patch': patch,
    }
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'output': str(args.output), 'least_primes': EXPECTED,
                      'python_crosscheck_primes': count,
                      'joint_period_after_patch': joint,
                      'remaining_holes_after_patch': patch['remaining_holes']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
