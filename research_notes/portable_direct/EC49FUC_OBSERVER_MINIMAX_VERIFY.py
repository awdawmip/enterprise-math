#!/usr/bin/env python3
"""EC49FUC: exact rational regressions for the clipping observer/minimax theorems.

Scientific claims for all real epsilon and all n follow from the accompanying
human proof; these Fraction checks verify the rational identities and examples.
No third-party packages, network requests, or task-claim side effects.
"""

from fractions import Fraction as F
from math import comb

M = F(1469, 64)
L = F(951, 1280)
U = F(3, 4)
W = U - L
E = F(1048576, 18958647)
A0, A1 = F(1, 8400), F(133679, 65536000)
B0, B1 = F(23, 181440), F(948007537, 428070666240)
Q_E = F(3310244525, 8132285009)


def q(e: F) -> F:
    """Clipped mass ratio in the immutable EC49FUB pricing chart."""
    a, b = A0 - e * A1, B0 - e * B1
    assert a > 0 and b > 0
    return b / (a + b)


def q_closed(e: F) -> F:
    return (575 * (41217719 * e - 2359296)
            / (45529434409 * e - 2630615040))


def continuous_top_bin(e: F, delta: F) -> F:
    assert F(0) <= delta <= W
    zbar = (L + U) / 2
    return (delta * (1 - e * M * (U - delta / 2))
            / (W * (1 - e * M * zbar)))


def integral_top_bin(e: F, delta: F) -> F:
    """Independent antiderivative calculation of continuous top-bin mass."""
    start = U - delta
    top = (U - start) - e * M * (U * U - start * start) / 2
    total = W - e * M * (U * U - L * L) / 2
    return top / total


def risk(e: F, n: int) -> F:
    return (1 - q(e)) ** n / 2


def check() -> None:
    assert W == F(9, 1280)
    assert q(F(0)) == F(115, 223)
    assert q(E) == Q_E
    assert 1 - Q_E == F(4822040484, 8132285009)
    assert q(F(0)) == q_closed(F(0))

    # Exact derivative numerator of the linear-over-linear q(e) formula.
    a, b = 575 * 41217719, -575 * 2359296
    c, d = 45529434409, -2630615040
    assert a * d - b * c == -581059943674675200

    for e in (F(-1000000), F(-2), F(-1, 3), F(0), F(1, 32), E):
        assert e <= E
        qe = q(e)
        assert qe == q_closed(e) and Q_E <= qe < 1
        for delta in (F(0), W / 17, W / 4, W / 2, W):
            rho = continuous_top_bin(e, delta)
            assert rho == integral_top_bin(e, delta)
            assert 0 <= rho <= 1
            top_minus = rho
            top_plus = (1 - qe) * rho + qe
            tv_of_two_bin_measures = abs(top_plus - top_minus)
            assert tv_of_two_bin_measures == qe * (1 - rho)

        # Exact product total-variation identity, via a binomial reduction.
        for n in range(1, 7):
            binom_plus = [
                F(comb(n, k)) * qe ** k * (1 - qe) ** (n - k)
                for k in range(n + 1)
            ]
            binom_minus = [F(1)] + [F(0)] * n
            tv = sum(abs(x - y) for x, y in zip(binom_plus, binom_minus)) / 2
            assert tv == 1 - (1 - qe) ** n
            assert risk(e, n) == (1 - tv) / 2

    assert continuous_top_bin(F(0), W / 4) == F(1, 4)
    assert q(F(0)) * (1 - continuous_top_bin(F(0), W / 4)) == F(345, 892)
    assert continuous_top_bin(E, W / 4) == F(1547881, 6614596)
    assert (q(E) * (1 - continuous_top_bin(E, W / 4))
            == F(16772065588485375, 53791779891391364))
    assert risk(E, 5) == F(
        1303539709278313450862689328621721630775794995712,
        35568287345581273008371650102150627634759859484049
    )
    print("EC49FUC exact Fraction regression: PASS")
    print("q(E) =", Q_E)
    print("five-draw minimax risk =", risk(E, 5))
    print("epsilon=0, delta=W/4 quantized TV =", F(345, 892))


if __name__ == "__main__":
    check()
