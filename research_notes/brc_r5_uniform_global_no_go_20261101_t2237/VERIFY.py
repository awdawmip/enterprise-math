"""R5: exact global two-parameter signed-support certificate; stdlib only.

The nature-parameter box corners are algebraic closure points, not claimed
strict-positive physical instances. Multi-affine interpolation proves the
statements for every interior parameter and real behavioral strategy.
"""
from fractions import Fraction as F
from itertools import product

Z, O = F(0), F(1)
W_BITS = (0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0)
PREVIOUS_W_BITS = (0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1)
M = (-211, 10, -113, 0)
M_SHORT = (-5, 1, -3, 0)


def obs(bits, eta, z):
    """Retain two-law, source-specific positive terminal masses until readout."""
    p1, p2, q1, q2, qb, r, k1, k2, l1, l2, lb = bits
    eta, z = F(eta), F(z)
    assert Z <= eta <= F(5, 6) and Z <= z <= O
    y, mass = [Z] * 4, [Z, Z]

    def terminal(ap, aq, answer, time):
        assert ap >= Z and aq >= Z
        mass[0] += ap
        mass[1] += aq
        if answer == "P":
            y[0] += ap
        else:
            y[1] += aq
        y[2] += ap * time
        y[3] += aq * time

    for p, q, k, l in ((p1, q1, k1, l1), (p2, q2, k2, l2)):
        ap = aq = F(1, 8)
        terminal(ap * p, aq * p, "P", 1)
        ap *= 1 - p; aq *= 1 - p
        terminal(ap / 2, 3 * aq / 4, "Q", 2)
        ap /= 2; aq /= 4
        terminal(ap * q, aq * q, "P", 2)
        ap *= 1 - q; aq *= 1 - q
        terminal(3 * ap / 5, aq / 2, "Q", 3)
        ap *= F(2, 5); aq /= 2
        terminal(ap / 2, aq / 2, "P", 3)
        ap /= 2; aq /= 2
        terminal(ap * k, aq * k, "P", 3)
        ap *= 1 - k; aq *= 1 - k
        terminal(ap / 4, aq / 2, "Q", 4)
        ap *= F(3, 4); aq /= 2
        terminal(ap * l, aq * l, "P", 4)
        terminal(ap * (1 - l), aq * (1 - l), "Q", 5)

    # B enters the genuine shared J key; its high branch reaches L.
    ap, aq = F(1, 4), F(1, 8)
    terminal(ap * qb, aq * qb, "P", 2)
    ap *= 1 - qb; aq *= 1 - qb
    terminal(ap * (1 - F(6, 5) * eta) * (1 - z),
             aq * (1 - eta) * (1 - z), "P", 4)
    terminal(ap * (1 - F(6, 5) * eta) * z,
             aq * (1 - eta) * z, "Q", 4)
    ap *= F(6, 5) * eta; aq *= eta
    terminal(ap * lb, aq * lb, "P", 4)
    terminal(ap * (1 - lb), aq * (1 - lb), "Q", 5)

    terminal(F(1, 2) * r, F(5, 8) * r, "Q", 1)
    terminal(F(1, 2) * (1 - r), F(5, 8) * (1 - r), "P", 3)
    assert mass == [O, O], mass
    return tuple(y)


def lr(bits, eta, z):
    p, q, r, k, l = bits
    return obs((p, p, q, q, q, r, k, k, l, l, l), eta, z)


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), Z)


def main():
    full_bits = tuple(product((0, 1), repeat=11))
    lr_bits = tuple(product((0, 1), repeat=5))
    corners = ((Z, Z), (Z, O), (F(5, 6), Z), (F(5, 6), O))
    witness = (F(11, 40), F(55, 64), F(267, 160), F(187, 128))
    assert len(full_bits) == 2048 and len(lr_bits) == 32
    count = 0
    for eta, z in corners:
        full = [obs(bits, eta, z) for bits in full_bits]
        limited = [lr(bits, eta, z) for bits in lr_bits]
        count += len(full) + len(limited)
        assert obs(W_BITS, eta, z) == witness
        max_f = max(dot(M, v) for v in full)
        max_l = max(dot(M, v) for v in limited)
        assert max_f == -238 and max_l == -F(481, 2)
        assert max_f - max_l == F(5, 2)
        assert dot(M, witness) == -238
        assert dot(M, lr((0, 1, 1, 0, 0), eta, z)) == -F(481, 2)
        max_short_f = max(dot(M_SHORT, v) for v in full)
        max_short_l = max(dot(M_SHORT, v) for v in limited)
        assert max_short_f == -F(1767, 320)
        assert max_short_l == -F(89, 16)
        assert max_short_f - max_short_l == F(13, 320)
        print(f"corner eta={eta} z={z} full={max_f} lr={max_l} gap={max_f-max_l} short_gap={max_short_f-max_short_l}")
    assert count == 8320
    eta, z = F(1, 2), F(3, 4)
    assert obs(PREVIOUS_W_BITS, eta, z) == (F(4, 5), F(15, 64), F(3), F(23, 8))
    assert obs(W_BITS, eta, z) == witness
    assert sum(abs(x) for x in M) == 334
    assert F(5, 2) / 334 == F(5, 668)
    print("exact flow calculations=8320 (2048 FULL + 32 LR, four nature-box corners)")
    print("all real eta in (0,5/6), z in (0,1): max_FULL M=-238, max_LR M=-481/2")
    print("uniform gap=5/2; explicit FULL witness Linf distance to conv(LR)>=5/668")
    print("independent simple direction=(-5,1,-3,0), exact gap=13/320")
    print("scope=finite two-law stopping model; author-side proof, not native X6 admission")
    print("PASS_EXACT_R5_GLOBAL_TWO_PARAMETER_UNIFORM_SIGNED_SUPPORT_NO_GO")


if __name__ == "__main__":
    main()
