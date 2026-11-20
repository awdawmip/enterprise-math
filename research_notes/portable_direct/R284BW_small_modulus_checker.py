#!/usr/bin/env python3
"""R284BW: exhaustive exact 35-bit star-Port certificate; stdlib only.

Enumeration order: row-major 16-tuple, each entry in (1,2), lexicographic.
SHA-256 hashes the 65,536 residues in that order, unsigned 8-byte big-endian.
"""
import bisect
import hashlib
import itertools
import json
import math
from pathlib import Path

P = 34359738337
T, S = 6, 13
D0, D3, Z1, Z2, Z3 = (2905293013, 27976265365, 618143958,
                          12373935123, 32899103541)


def signature(c):
    a, b1, b2, b3, u1, a11, x, y, u2, w, a22, z, u3, g, h, r = c
    t, s = T - a11, S - a22
    u = t * s - x * w
    v = -r * u - z * (t * h + x * g) - y * (w * h + s * g)
    p1, p2 = s * u1 + x * u2, t * u2 + w * u1
    q1 = -r * p1 - u1 * z * h + x * z * u3 + y * (u2 * h + s * u3)
    q2 = -r * p2 + t * z * u3 + u1 * z * g + y * (w * u3 - u2 * g)
    q3 = u * u3 + p1 * g + p2 * h
    j = -a * u - b1 * p1 - b2 * p2
    k = -a * v - b1 * q1 - b2 * q2 - b3 * q3
    return (u, v, p1, p2, q1, q2, q3, j), k


def observable(c):
    (u, v, p1, p2, q1, q2, q3, j), k = signature(c)
    return (D0 * (u * D3 + v) - Z1 * (p1 * D3 + q1)
            - Z2 * (p2 * D3 + q2) - Z3 * q3 + j * D3 + k) % P


def independent_determinant(c):
    mat = [[-c[i * 4 + j] for j in range(4)] for i in range(4)]
    for i, d in enumerate((D0, T, S, D3)):
        mat[i][i] += d
    for j, z in enumerate((Z1, Z2, Z3), 1):
        mat[0][j] -= z
    out = 0
    for perm in itertools.permutations(range(4)):
        inv = sum(perm[i] > perm[j] for i in range(4)
                  for j in range(i + 1, 4))
        out += (-1 if inv % 2 else 1) * math.prod(
            mat[i][perm[i]] for i in range(4))
    return out % P


def prime_by_trial_division(n):
    return n > 2 and n % 2 == 1 and all(
        n % d for d in range(3, math.isqrt(n) + 1, 2))


def verify():
    assert P.bit_length() == 35 and prime_by_trial_division(P)
    signatures = {}
    observations = []
    digest = hashlib.sha256()
    crosschecks = 0
    for index, c in enumerate(itertools.product((1, 2), repeat=16)):
        c = tuple(c)
        key, _ = signature(c)
        prior = signatures.get(key)
        if prior is None:
            signatures[key] = c
        else:
            assert prior[:3] + prior[4:] == c[:3] + c[4:]
            assert prior[3] != c[3]
        r = observable(c)
        observations.append((r, c))
        digest.update(r.to_bytes(8, 'big', signed=False))
        if index % 257 == 0:
            assert independent_determinant(c) == r
            crosschecks += 1
    assert len(observations) == 65536 and len(signatures) == 32768
    assert min(k[6] for k in signatures) == 59
    assert max(k[6] for k in signatures) == 196
    ordered = sorted(observations)
    values = [r for r, _ in ordered]
    distances = [(values[(i + 1) % len(values)] - values[i]) % P
                 for i in range(len(values))]
    assert min(distances) == 59
    assert all(d >= 59 for d in distances)
    mi = distances.index(59)

    def decode(z):
        z %= P
        i = bisect.bisect_left(values, z)
        candidates = (i % 65536, (i - 1) % 65536)
        j = min(candidates, key=lambda k: min(
            (values[k] - z) % P, (z - values[k]) % P))
        return ordered[j][1]

    decoded = 0
    for r, c in observations:
        for error in (-29, 0, 29):
            assert decode(r + error) == c
            decoded += 1
    a, b = ordered[mi], ordered[(mi + 1) % len(ordered)]
    assert a[1][:3] + a[1][4:] == b[1][:3] + b[1][4:]
    return {
        'schema': 'EM_R284BW_EXACT_35BIT_PORT_CERT_V1',
        'frozen_source': 'R284BV@630117e9b8e3fc7be964b4e5cb16e99c6917f43e',
        'matrix_alphabet': [1, 2], 'size': 4,
        'frozen_d1_d2': [T, S], 'modulus_prime': P,
        'modulus_bits': P.bit_length(),
        'controls_d0_d3_z1_z2_z3': [D0, D3, Z1, Z2, Z3],
        'candidate_count': len(observations),
        'nonconstant_signature_classes': len(signatures),
        'each_fibre': 'exactly two matrices differing only at C03',
        'q3_min': 59, 'q3_max': 196,
        'minimum_circular_gap': min(distances),
        'minimum_gap_pair_count': distances.count(59),
        'maximal_correctable_integer_error': 29,
        'sharp_real_error_condition': '0 <= rho < 59/2',
        'independent_leibniz_checks': crosschecks,
        'nearest_neighbor_decoding_checks': decoded,
        'residue_lexicographic_be64_sha256': digest.hexdigest(),
        'first_min_gap_pair': {'first_residue': a[0],
                               'first_matrix_row_major': a[1],
                               'second_residue': b[0],
                               'second_matrix_row_major': b[1]},
        'decoder': 'sorted-residue nearest-neighbor lookup; 65536 entries',
        'proof_scope': 'full finite H=2, n=4; NOT_REVIEWED',
        'native_x6_brc_application': 'not established'
    }


if __name__ == '__main__':
    result = verify()
    target = Path(__file__).with_name('R284BW_small_modulus_verification.json')
    target.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2, sort_keys=True))
