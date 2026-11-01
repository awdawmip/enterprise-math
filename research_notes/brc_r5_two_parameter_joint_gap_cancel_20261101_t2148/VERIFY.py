"""Exact rational certificate for R5 two-parameter bypass cancellation and surviving facet.

Python 3 standard library only. See RESEARCH.md for the multiaffine interpolation proof.
"""
from fractions import Fraction as F
from itertools import product, permutations
from math import prod

Z, O = F(0), F(1)
N = (25, -160, -95, 242)
H = (5, 0, 5, -8)
J = (-3, 0, -1, 0)
FULL_WITNESS = (Z, Z, O, O, Z, Z, O, O, O, O, O)
ETA_CORNERS = (F(1, 2), F(3, 5))
Z_CORNERS = (F(3, 4), F(9, 10))


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), Z)


def obs(bits, eta, z):
    """Positive P/Q source-labelled terminal flow; all 11 FULL decision parameters."""
    p1, p2, q1, q2, qb, r, k1, k2, l1, l2, lb = bits
    assert Z < eta < F(5, 6) and Z < z < O
    y, mass = [Z] * 4, [Z, Z]

    def terminal(ap, aq, answer, time):
        assert ap >= 0 and aq >= 0
        mass[0] += ap
        mass[1] += aq
        if answer == 'P':
            y[0] += ap
        else:
            y[1] += aq
        y[2] += ap * time
        y[3] += aq * time

    for p, q, k, l in ((p1, q1, k1, l1), (p2, q2, k2, l2)):
        ap = aq = F(1, 8)
        terminal(ap * p, aq * p, 'P', 1)
        ap *= 1 - p; aq *= 1 - p
        terminal(ap / 2, 3 * aq / 4, 'Q', 2)
        ap /= 2; aq /= 4
        terminal(ap * q, aq * q, 'P', 2)
        ap *= 1 - q; aq *= 1 - q
        terminal(3 * ap / 5, aq / 2, 'Q', 3)
        ap *= F(2, 5); aq /= 2
        terminal(ap / 2, aq / 2, 'P', 3)
        ap /= 2; aq /= 2
        terminal(ap * k, aq * k, 'P', 3)
        ap *= 1 - k; aq *= 1 - k
        terminal(ap / 4, aq / 2, 'Q', 4)
        ap *= F(3, 4); aq /= 2
        terminal(ap * l, aq * l, 'P', 4)
        terminal(ap * (1 - l), aq * (1 - l), 'Q', 5)

    # B arrives at J with likelihood ratio 2, then bypasses toward L.
    ap, aq = F(1, 4), F(1, 8)
    terminal(ap * qb, aq * qb, 'P', 2)
    ap *= 1 - qb; aq *= 1 - qb
    lowp = ap * (1 - F(6, 5) * eta)
    lowq = aq * (1 - eta)
    # Additional strictly positive natural answer split z, independent of law.
    terminal(lowp * (1 - z), lowq * (1 - z), 'P', 4)
    terminal(lowp * z, lowq * z, 'Q', 4)
    ap *= F(6, 5) * eta; aq *= eta
    terminal(ap * lb, aq * lb, 'P', 4)
    terminal(ap * (1 - lb), aq * (1 - lb), 'Q', 5)

    terminal(F(1, 2) * r, F(5, 8) * r, 'Q', 1)
    terminal(F(1, 2) * (1 - r), F(5, 8) * (1 - r), 'P', 3)
    assert mass == [O, O]
    return tuple(y)


def lr(bits, eta, z):
    p, q, r, k, l = bits
    return obs((p, p, q, q, q, r, k, k, l, l, l), eta, z)


def h_and_c_expansion(bits, eta, z):
    p1, p2, q1, q2, qb, r, k1, k2, l1, l2, lb = bits
    m = F(5, 4) - F(3, 2) * eta
    n = F(3, 4) - F(9, 10) * eta
    h = -F(33, 8) + F(5, 2) * r - qb / 4 + (1 - qb) * (F(1, 4) - eta + eta * lb - m * z)
    c = r / 2 + 3 * (1 - r) + F(5, 4) * qb + (1 - qb) * (F(7, 4) - F(3, 5) * eta * (1 - lb) - n * z)
    for p, q, k, l in ((p1, q1, k1, l1), (p2, q2, k2, l2)):
        h += 13 * p / 16 - p * q / 8 + q / 8 + (-F(3, 8) + l / 4) * (1 - p) * (1 - q) * (1 - k) / 8
        c += p / 2 + (1 - p) * (F(1, 8) + 5 * q / 16 + (1 - q) * (F(3, 16) + 3 * k / 40 + (1 - k) * (F(19, 320) + 3 * l / 160)))
    return h, c


def d_e(eta, z):
    return (F(1, 2) - eta - (F(5, 4) - F(3, 2) * eta) * z,
            F(1, 2) - F(3, 5) * eta - (F(3, 4) - F(9, 10) * eta) * z)


def det4(rows):
    out = Z
    for perm in permutations(range(4)):
        sign = -1 if sum(perm[i] > perm[j] for i in range(4) for j in range(i+1, 4)) % 2 else 1
        out += sign * prod(rows[i][perm[i]] for i in range(4))
    return out


def rank_minor(eta, z):
    base = lr((Z, Z, Z, O, O), eta, z)
    p = tuple(a - b for a, b in zip(lr((O, Z, Z, O, O), eta, z), base))
    q = tuple(a - b for a, b in zip(lr((Z, O, Z, O, O), eta, z), base))
    v = lr((O, O, Z, O, O), eta, z)
    pq = tuple(v[i] - base[i] - p[i] - q[i] for i in range(4))
    r = tuple(a - b for a, b in zip(lr((Z, Z, O, O, O), eta, z), base))
    return det4((p, q, pq, r))


def main():
    full_bits = list(product((Z, O), repeat=11))
    lr_bits = list(product((Z, O), repeat=5))
    assert len(full_bits) == 2048 and len(lr_bits) == 32
    expected_gaps = ((F(1, 2), F(3, 4), F(29, 8)),
                     (F(1, 2), F(9, 10), F(7, 4)),
                     (F(3, 5), F(3, 4), F(29, 8)),
                     (F(3, 5), F(9, 10), F(29, 8)))
    min_gaps, ds, es = [], [], []
    expansion_count = 0
    for eta, z, target_gap in expected_gaps:
        fvals = []
        for bits in full_bits:
            v = obs(bits, eta, z)
            h, c = h_and_c_expansion(bits, eta, z)
            assert dot(H, v) == h and -dot(J, v) == c
            fvals.append(v)
            expansion_count += 1
        lvals = []
        for bits in lr_bits:
            v = lr(bits, eta, z)
            h, c = h_and_c_expansion((bits[0], bits[0], bits[1], bits[1], bits[1], bits[2], bits[3], bits[3], bits[4], bits[4], bits[4]), eta, z)
            assert dot(H, v) == h and -dot(J, v) == c
            lvals.append(v)
            expansion_count += 1
        d, e = d_e(eta, z)
        ds.append(d); es.append(e)
        assert min(dot(H, v) for v in fvals) == -F(143, 32) + min(Z, d)
        assert min(dot(H, v) for v in lvals) == -F(33, 8) + min(Z, d - F(11, 32))
        assert min(-dot(J, v) for v in fvals) == F(399, 160) + min(Z, e)
        assert min(-dot(J, v) for v in lvals) == F(21, 8) + min(Z, e - F(21, 160))
        assert d < 0 and e < 0
        # The exact 4x4 LR affine-coordinate determinant is positive.
        assert rank_minor(eta, z) == (59 + (59 * eta - 46) * z) / 10240
        w = obs(FULL_WITNESS, eta, z)
        gap = dot(N, w) - max(dot(N, v) for v in lvals)
        assert gap == target_gap
        min_gaps.append(gap)
        print(f'corner eta={eta} z={z}: D={d}, E={e}, H_gap=0, J_gap=0, N_gap={gap}, det={rank_minor(eta,z)}')
    assert expansion_count == 8320
    assert max(ds) == -F(29, 80)
    assert max(es) == -F(7, 400)
    assert min(min_gaps) == F(7, 4)
    w = obs(FULL_WITNESS, F(1, 2), F(3, 4))
    assert w == (F(4, 5), F(15, 64), F(3), F(23, 8))
    assert dot(N, w) == F(1573, 4)
    assert max(dot(N, lr(v, F(1, 2), F(3, 4))) for v in lr_bits) == F(3117, 8)
    assert sum(abs(x) for x in N) == 522
    print('bilinear/interpolation: 8320 exact terminal expansions at four parameter corners; 2048 FULL and 32 LR deterministic policies per corner')
    print('all-real parameter rectangle: eta in [1/2,3/5], z in [3/4,9/10]')
    print('H and J gaps identically zero; N positive gap >=7/4 for all real policies')
    print('uniform Linf distance lower bound >=7/2088; at eta=1/2,z=3/4 the distance lower bound >=1/144')
    print('rank determinant exactly (59+(59*eta-46)*z)/10240 > 0 throughout (0,5/6)x(0,1)')
    print('PASS_EXACT_R5_TWO_PARAMETER_DOUBLE_GAP_CANCEL_THIRD_FACET_RECTANGLE')

if __name__ == '__main__':
    main()
