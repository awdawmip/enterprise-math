"""Exact CRT block lists for the permutation/translation Riesel family.

The .bin files are reproducible intermediate inputs, not certificates.
Run from the workspace root: python v4_phase_work/prepare_family.py
"""
from __future__ import annotations

from hashlib import sha256
from itertools import permutations
import json
from math import factorial, lcm, prod
from pathlib import Path
import struct

DIRECTORY = Path(__file__).resolve().parent
ROOT = next(p for p in DIRECTORY.parents
            if (p / 'research_notes/portable_direct/riesel_mixed_20261119/certificate.json').exists())
PRIOR = ROOT / 'research_notes/portable_direct/riesel_mixed_20261119'
STRUCTURE = ROOT / 'research_notes/portable_direct/riesel_structure_20261119'
ROWS = json.loads((PRIOR / 'certificate.json').read_text())['original']['rows']
LOCAL = json.loads((STRUCTURE / 'local_shapes_results.json').read_text())
PRIMES = [r['p'] for r in ROWS]
PERIODS = LOCAL['effective_periods']
PHASES = LOCAL['original_u_phases']
INDEX = {p: i for i, p in enumerate(PRIMES)}
M = prod(PRIMES)
L = lcm(*PERIODS)
GROUP7 = [71, 113, 127, 281, 337, 14449, 29191]
GROUP5 = [31, 41, 151, 1321]
PAIR24 = [97, 673]
PAIR32 = [641, 6700417]
FIXED = [7, 17, 241, 257, 65537]
BLOCKS = [GROUP7, GROUP5, PAIR24, PAIR32, FIXED]


def phase_coordinate(p, q, r):
    i = INDEX[p]
    e = PERIODS[i]
    h = e // q
    return next(c for c in range(e) if c % q == r and c % h == PHASES[i] % h)


def root_for_phase(p, c):
    i = INDEX[p]
    return ROWS[i]['a_residue'] * pow(2, PHASES[i] - c, p) % p


def signed_block(primes, phases, modulus):
    """Return all 2^r independent signs of these chosen root residues."""
    terms = []
    for p, c in zip(primes, phases):
        basis = (modulus // p) * pow(modulus // p, -1, p)
        r = root_for_phase(p, c)
        terms.append((basis * r % modulus, basis * (-r % p) % modulus))
    return [sum(terms[i][(mask >> i) & 1] for i in range(len(primes))) % modulus
            for mask in range(1 << len(primes))]


def group_options(primes, q, coordinates, modulus):
    result = []
    for perm in permutations(coordinates):
        phases = [phase_coordinate(p, q, r) for p, r in zip(primes, perm)]
        result.extend(signed_block(primes, phases, modulus))
    return result


def pair_options(primes, modulus):
    phases = [PHASES[INDEX[p]] for p in primes]
    return signed_block(primes, phases, modulus) + signed_block(primes, phases[::-1], modulus)


def decode(a_code, b_code, translation):
    """Decode selected groups and actual residues after the global translation."""
    mask_fixed = b_code % 32
    b_code //= 32
    option32 = b_code % 8
    b_code //= 8
    option24 = b_code % 8
    b_code //= 8
    mask5 = b_code % 16
    perm5_index = b_code // 16
    mask7 = a_code % 128
    perm7_index = a_code // 128
    permutation5 = list(permutations(range(4)))[perm5_index]
    permutation7 = list(permutations(range(7)))[perm7_index]
    phases = list(PHASES)
    residues = [r['a_residue'] for r in ROWS]
    for group, q, permutation, mask in [
        (GROUP7, 7, permutation7, mask7), (GROUP5, 5, permutation5, mask5)]:
        for bit, (p, r) in enumerate(zip(group, permutation)):
            i = INDEX[p]
            phases[i] = phase_coordinate(p, q, r)
            residues[i] = root_for_phase(p, phases[i]) * (-1 if mask >> bit & 1 else 1) % p
    for group, option in [(PAIR24, option24), (PAIR32, option32)]:
        swap, mask = divmod(option, 4)
        pair_phases = [PHASES[INDEX[p]] for p in group]
        if swap:
            pair_phases.reverse()
        for bit, (p, c) in enumerate(zip(group, pair_phases)):
            i = INDEX[p]
            phases[i] = c
            residues[i] = root_for_phase(p, c) * (-1 if mask >> bit & 1 else 1) % p
    for bit, p in enumerate(FIXED):
        i = INDEX[p]
        residues[i] = residues[i] * (-1 if mask_fixed >> bit & 1 else 1) % p
    result = []
    for i, p in enumerate(PRIMES):
        c = (phases[i] + translation) % PERIODS[i]
        result.append({'p': p, 'order': ROWS[i]['order'], 'base_u_phase': phases[i],
                       'u_phase': c, 'exponent_phase': (2*c+1) % ROWS[i]['order'],
                       'a_residue': residues[i] * pow(2, -translation, p) % p})
    return {'permutation5': list(permutation5), 'permutation7': list(permutation7),
            'swap24': option24 // 4, 'swap32': option32 // 4,
            'sign_masks': {'q7': mask7, 'q5': mask5, 'pair24': option24 % 4,
                           'pair32': option32 % 4, 'fixed': mask_fixed},
            'u_translation': translation, 'rows': result}


def membership(vector):
    if any(vector[INDEX[p]] != PHASES[INDEX[p]] for p in FIXED):
        return False
    for group, q, coordinates in [(GROUP5, 5, set(range(4))), (GROUP7, 7, set(range(7)))]:
        if {vector[INDEX[p]] % q for p in group} != coordinates:
            return False
        if any(vector[INDEX[p]] % (PERIODS[INDEX[p]]//q) !=
               PHASES[INDEX[p]] % (PERIODS[INDEX[p]]//q) for p in group):
            return False
    return all(sorted(vector[INDEX[p]] for p in group) == sorted(PHASES[INDEX[p]] for p in group)
               for group in [PAIR24, PAIR32])


def limbs(value):
    return (value & ((1 << 64)-1), (value >> 64) & ((1 << 64)-1), value >> 128)


def write_binary(path, modulus, left, right):
    pack = struct.Struct('<QQQQ').pack
    with path.open('wb') as f:
        f.write(b'RIESELV4')
        f.write(struct.pack('<QQQQQ', *limbs(modulus), len(left), len(right)))
        for values in [left, right]:
            buffer = bytearray()
            for code, value in enumerate(values):
                buffer.extend(pack(*limbs(value), code))
                if len(buffer) >= 1 << 20:
                    f.write(buffer)
                    buffer.clear()
            f.write(buffer)


def main():
    assert L == 3360
    assert len(set(p for group in BLOCKS for p in group)) == 20
    intersections = [t for t in range(L) if membership([(c+t) % e for c, e in zip(PHASES, PERIODS)])]
    assert intersections == list(range(0, L, 240))
    left = group_options(GROUP7, 7, range(7), M)
    group5 = group_options(GROUP5, 5, range(4), M)
    pair24 = pair_options(PAIR24, M)
    pair32 = pair_options(PAIR32, M)
    fixed = signed_block(FIXED, [PHASES[INDEX[p]] for p in FIXED], M)
    right = [(a+b+c+d) % M for a in group5 for b in pair24 for c in pair32 for d in fixed]
    assert len(left) == 645120 and len(right) == 786432
    assert len(set(left)) == len(left) and len(set(right)) == len(right)
    assert all(v != 0 for v in left+right)
    assert all((M-v) in set_left for v in left) if (set_left := set(left)) else False
    assert all((M-v) in set_right for v in right) if (set_right := set(right)) else False
    assert sum(v % 2 for v in left) == len(left)//2
    assert sum(v % 2 for v in right) == len(right)//2
    write_binary(DIRECTORY / 'family_M.bin', M, left, right)
    inverse = pow(M, -1, 3)
    left3 = [v + M*((-v*inverse) % 3) for v in left]
    right3 = [v + M*((-v*inverse) % 3) for v in right]
    assert all(v % 3 == 0 for v in left3+right3)
    write_binary(DIRECTORY / 'family_3M.bin', 3*M, left3, right3)
    family_size = factorial(4)*factorial(7)*4
    overlap_size = len(intersections)
    translated_shapes = family_size * L // overlap_size
    distinct_root_classes = translated_shapes * 2**len(PRIMES)
    assert distinct_root_classes == len(left) * len(right) * (L//overlap_size)
    result = {
        'schema': 'RIESEL_FULL_PERMUTATION_FAMILY_INPUT_V1',
        'researcher_id': 'EM-DIRECT-970E1C',
        'research_activity_id': 'RA-D2EC212845B63844081F9A14',
        'M': str(M), 'L': L, 'blocks': BLOCKS,
        'family_size_before_translation': family_size,
        'translation_overlap_subgroup': intersections,
        'translation_shape_classes': family_size//overlap_size,
        'distinct_translated_phase_vectors': translated_shapes,
        'odd_root_classes_per_branch': distinct_root_classes,
        'translation_coset_representatives': list(range(L//overlap_size)),
        'left_count': len(left), 'right_count': len(right),
        'source_files_sha256': {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest()
                                for p in [PRIOR/'certificate.json', STRUCTURE/'local_shapes_results.json']},
        'binary_format': 'little endian; magic RIESELV4; three uint64 modulus limbs; uint64 sizes; left then right nodes, each three uint64 value limbs and uint64 provenance code',
        'scope': 'Only the explicitly specified permutation, pair-swap, translation, and sign family; not all fixed-prime covers.'
    }
    (DIRECTORY / 'family_input.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['M','translation_shape_classes','odd_root_classes_per_branch','left_count','right_count']}))


if __name__ == '__main__':
    main()
