#!/usr/bin/env python3
"""Exact-rational regression checker for the c=103/20 T1-T3 source map.

Checks all exponent identities and the discrete Abel/Buchstab-shell identity
behind the exact T3 collapse.  This is regression evidence for the algebraic
lemma, not a finite P2 theorem.
"""

from fractions import Fraction as Q


def source_parameters() -> None:
    a = Q(6)
    b = Q(93, 20)
    c = Q(103, 20)
    d = Q(5, 9)

    delta = 2 * c - b - 1
    U = (b + 1) / (2 * a)

    assert delta == Q(93, 20)
    assert U == Q(113, 240)
    assert c - b == Q(1, 2)

    # T1 source range.
    assert b / a == Q(31, 40)
    assert d / a == Q(5, 54)
    # D=W^(10/9): convert D-exponents to W-exponents.
    assert Q(10, 9) * Q(1, 6) == Q(5, 27)
    assert Q(10, 9) * Q(31, 40) == Q(31, 36)

    # T2 is nonempty only for s<U/2.  The largest p occurs at s=1/a.
    assert U / 2 == Q(113, 480)
    t2_p_hi = U - Q(1, 6)
    assert t2_p_hi == Q(73, 240)
    assert Q(10, 9) * t2_p_hi == Q(73, 216)

    # T3 terminal endpoint.
    assert Q(10, 9) * U == Q(113, 216)

    # At z=D^(1/a), psi(z)=b-1 and Delta-(b-1)=1.
    psi_z = b + 1 - 2 * a * Q(1, 6)
    assert psi_z == b - 1 == Q(73, 20)
    assert delta - psi_z == 1
    assert 1 / delta == Q(20, 93)

    # Effective coarse base-carry coefficient.
    base_error = Q(29, 20000)
    assert base_error / delta == Q(29, 93000)
    assert base_error / delta < Q(312, 1_000_000)


def abel_identity() -> None:
    # Synthetic exact rational least-prime shells.  We use decreasing affine
    # psi-values and arbitrary nonnegative shell masses.  R_i is the tail sum.
    shells = [7, 11, 5, 13, 3]
    # psi_1 > ... > psi_m > 0, all <= psi(z)=73/20.
    psi = [Q(7, 2), Q(3), Q(5, 2), Q(3, 2), Q(1, 2)]
    delta = Q(93, 20)

    m = len(shells)
    R = []
    for i in range(m):
        R.append(sum(shells[i:]))
    R.append(17)  # states whose least prime is beyond the T3 endpoint

    # To make shell_i=R_i-R_(i+1), fold the endpoint tail into every R_i.
    R = [x + R[-1] for x in R[:-1]] + [R[-1]]
    assert all(R[i] - R[i + 1] == shells[i] for i in range(m))

    t3 = sum(psi[i] * shells[i] for i in range(m))
    lhs = R[0] - t3 / delta

    rhs = (1 - psi[0] / delta) * R[0]
    for i in range(1, m):
        rhs += (psi[i - 1] - psi[i]) / delta * R[i]
    rhs += psi[-1] / delta * R[-1]

    assert lhs == rhs
    assert all(psi[i - 1] >= psi[i] for i in range(1, m))
    assert 1 - psi[0] / delta > 0

    # Coarse theorem: psi_1<=73/20 implies first coefficient >=20/93.
    assert psi[0] <= Q(73, 20)
    assert 1 - psi[0] / delta >= Q(20, 93)
    assert lhs >= Q(20, 93) * R[0]


def main() -> None:
    source_parameters()
    abel_identity()
    print("P017 c515 T1-T3 source map / T3 Buchstab collapse checker: PASS")
    print("T3 is removed as an independent upper-sieve/bilinear remainder.")
    print("T1 and T2 remain live; source-main budget must not be naively recredited.")


if __name__ == "__main__":
    main()
