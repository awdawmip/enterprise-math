#!/usr/bin/env python3
"""Exact source-label-preserving S23 two-replacement-probe certificate.

Scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
No floating point, external dependencies, or randomized hidden state.
"""
from fractions import Fraction as Q
from itertools import combinations_with_replacement, product
import json

A = (0, 0, 0, 1, 1, 1)
B = (2, 2, 3, 2, 2, 4)
C = (5, 6, 7, 8, 9, 10)
M = ((10, 10, 0, 0, 0, 0), (9, 11, 0, 0, 0, 0),
     (0, 0, 20, 0, 0, 0), (0, 0, 0, 10, 10, 0),
     (0, 0, 0, 2, 18, 0), (0, 0, 0, 0, 0, 20))
BETA = Q(1, 2)
MASKS = tuple(frozenset(k for k in range(5) if (mask >> k) & 1)
              for mask in range(32))
REQS = (
    ("M2", 2, lambda f: any(2 not in s and (0 in s or 1 in s) for s in f)),
    ("M3", 3, lambda f: any(0 in s and 3 not in s for s in f)),
    ("M4", 4, lambda f: any(1 in s and 4 not in s for s in f)),
    ("C5_6", 5, lambda f: any({0, 2} <= s for s in f)),
    ("C7", 7, lambda f: any({0, 3} <= s for s in f)),
    ("C8_9", 8, lambda f: any({1, 2} <= s for s in f)),
    ("C10", 10, lambda f: any({1, 4} <= s for s in f)),
)


def branch(a, b, c):
    return (a, (1-a)*b, (1-a)*(1-b)*c, (1-a)*(1-b)*(1-c))


def raw(z, mask=frozenset()):
    return tuple(branch(BETA if A[j] in mask else z[A[j]],
                        BETA if B[j] in mask else z[B[j]], z[C[j]])
                 for j in range(6))


def mix(r):
    return tuple(tuple(sum((Q(M[i][j], 20) * r[j][k] for j in range(6)), Q(0))
                       for k in range(4)) for i in range(6))


def obs(z, mask=frozenset()):
    return mix(raw(z, mask))


def unmix(p):
    return ((tuple(11*p[0][k] - 10*p[1][k] for k in range(4))),
            (tuple(10*p[1][k] - 9*p[0][k] for k in range(4))),
            p[2],
            tuple((9*p[3][k] - 5*p[4][k])/4 for k in range(4)),
            tuple((5*p[4][k] - p[3][k])/4 for k in range(4)),
            p[5])


def first_missing(family):
    for name, coordinate, condition in REQS:
        if not condition(family):
            return (name, coordinate)
    return None


def inverse(all_p, family):
    r0 = unmix(all_p[0])
    r = {mask: unmix(p) for mask, p in zip(family, all_p[1:])}
    z = [None]*11
    z[0], z[1] = r0[0][0], r0[3][0]
    for k in (2, 3, 4):
        for mask in family:
            for j in range(6):
                if B[j] == k and A[j] in mask and k not in mask:
                    z[k] = r[mask][j][1]/(1-BETA)
                    break
            if z[k] is not None:
                break
        assert z[k] is not None
    for j in range(6):
        for mask in family:
            if A[j] in mask and B[j] in mask:
                z[C[j]] = r[mask][j][2]/((1-BETA)**2)
                break
        assert z[C[j]] is not None
    assert all(0 <= v <= 1 for v in z)
    return tuple(z)


def tv(p, q):
    return sum((abs(a-b) for a, b in zip(p, q)), Q(0))/2


def distance(z, w, family):
    return max(tv(row, other)
               for mask in (frozenset(), *family)
               for row, other in zip(obs(z, mask), obs(w, mask)))


def exact_states(n):
    # Deterministic, low-denominator rational points in the complete cube.
    state = 20261103
    for _ in range(n):
        point = []
        for i in range(11):
            state = (1103515245*state + 12345) % (2**31)
            den = 3 + (i % 7)
            point.append(Q(state % (den + 1), den))
        yield tuple(point)


def main():
    one_fail = 0
    for mask in MASKS:
        family = (mask,)
        missing = first_missing(family)
        assert missing is not None
        one_fail += 1
    families = list(combinations_with_replacement(range(32), 2))
    good = []
    fail_witnesses = 0
    for i, j in families:
        family = (MASKS[i], MASKS[j])
        missing = first_missing(family)
        if missing is None:
            good.append((i, j))
        else:
            name, coord = missing
            x = [Q(1)]*5 + [Q(0)]*6
            y = x.copy()
            y[coord] = Q(0) if coord in (2, 3, 4) else Q(1)
            for mask in (frozenset(), *family):
                assert obs(x, mask) == obs(y, mask), (i, j, name, coord)
            fail_witnesses += 1
    assert good == [(3,31), (7,27), (11,23), (15,19)], good
    assert fail_witnesses == 524

    for i,j in good:
        family = (MASKS[i], MASKS[j])
        for bits in product((Q(0), Q(1)), repeat=11):
            measured = (obs(bits), obs(bits, family[0]), obs(bits, family[1]))
            assert inverse(measured, family) == bits, (i,j,bits)
    rational_points = list(exact_states(160))
    for i,j in good:
        family = (MASKS[i], MASKS[j])
        for z in rational_points:
            assert inverse((obs(z), *(obs(z,mask) for mask in family)), family) == z
    # Stable observer inequalities, from explicit inverse and coupling.
    stability_pairs=0
    for i,j in good:
        family=(MASKS[i],MASKS[j])
        for z,w in zip(rational_points[:80], rational_points[80:]):
            eps=max(abs(a-b) for a,b in zip(z,w))
            d=distance(z,w,family)
            assert eps <= 84*d and d <= 3*eps, (i,j,z,w,d)
            stability_pairs+=1
    out = {
      "status":"PASS_BRC_S23_MIN_TWO_CONSTANT_REPLACEMENT_PROBES_20261103",
      "scientific_pin":"43ec6098b1330ae86d0a7863be336c5d97f6ef34",
      "beta":"1/2",
      "single_masks_exhausted":one_fail,
      "unordered_two_mask_families_exhausted":len(families),
      "two_mask_families_not_injective_with_exact_witness":fail_witnesses,
      "two_mask_families_injective":len(good),
      "injective_mask_pairs":[[a,b] for a,b in good],
      "exact_binary_corner_inverses":2048*len(good),
      "exact_rational_interior_inverses":len(rational_points)*len(good),
      "exact_tv_stability_pairs":stability_pairs,
      "proof_scope":"All real [0,1]^11 by symbolic inverse and combinatorial witness necessity; finite checks audit the implementation.",
      "native_claim_or_independent_review":False
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
