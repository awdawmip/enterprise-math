"""Numerical certificate for the Iwaniec-Laborde square-window P2 parameter margin.

Research status: diagnostic/certificate only.  It evaluates the published final
main-term function from Iwaniec-Laborde (1981), section 7, after reconstructing
the Laborde constants B1,B2 from the paper's printed theta=0.45 optimum.

The purpose is not to claim an explicit all-x theorem.  It checks that at the
square-window exponent theta=1/2 there is a large main-term margin while a
sieve level D=x^(5/9) remains well below the analytic maximum
D_max=x^(9/14+o(1)) furnished by the same bilinear framework.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import log


@dataclass(frozen=True)
class ILConstants:
    B1: float
    B2: float


def alpha_from_theta_at_il_max(theta: float) -> float:
    """IL maximal-level relation: (1+alpha)theta = 2 theta - 5/14."""
    return (2.0 * theta - 5.0 / 14.0) / theta - 1.0


def reconstruct_constants(
    theta: float = 0.45,
    c: float = 5.1828,
    b: float = 4.8698,
    G: float = 0.00177,
) -> ILConstants:
    """Invert the printed IL optimum to recover B1 and B2 numerically."""
    alpha = alpha_from_theta_at_il_max(theta)
    factor = (3.0 * (3.0 * theta - 1.0) / (2.0 * (1.0 + alpha) * theta)) ** 2
    B1 = ((c - 6.0 / (1.0 + alpha)) / factor - log(alpha) / 6.0) / 2.0

    nonconstant = (
        -(c / 6.0) * log(6.0 / (1.0 + alpha))
        - ((6.0 - c) / 6.0) * log(6.0 * alpha / (1.0 + alpha))
        - 2.0
        * ((c * theta * (1.0 + alpha) - 6.0 * theta) / (3.0 * (3.0 * theta - 1.0)))
        ** 2
    )
    B2 = G - B1 * (c - b) - nonconstant
    return ILConstants(B1=B1, B2=B2)


def il_G(theta: float, d: float, c: float, constants: ILConstants) -> tuple[float, float]:
    """Evaluate IL equation-(section 7) G(b,c) with D=x^d and a=6."""
    alpha = d / theta - 1.0
    if alpha <= 0.0:
        raise ValueError("need d>theta")
    b = 6.0 / d - 1.0 - c
    B1, B2 = constants.B1, constants.B2
    G = (
        B1 * (c - b)
        + B2
        - (c / 6.0) * log(6.0 / (1.0 + alpha))
        - ((6.0 - c) / 6.0) * log(6.0 * alpha / (1.0 + alpha))
        - 2.0
        * ((c * theta * (1.0 + alpha) - 6.0 * theta) / (3.0 * (3.0 * theta - 1.0)))
        ** 2
    )
    return G, b


def feasible(theta: float, d: float, c: float) -> bool:
    b = 6.0 / d - 1.0 - c
    root_coordinate = 6.0 * theta / d
    return 3.0 <= b < root_coordinate < c <= 6.0


def grid_optimum(theta: float, d: float, constants: ILConstants, steps: int = 200_000):
    best = (-1e100, None, None)
    for j in range(steps + 1):
        c = 3.0 + 3.0 * j / steps
        if not feasible(theta, d, c):
            continue
        G, b = il_G(theta, d, c, constants)
        if G > best[0]:
            best = (G, c, b)
    return best


def main() -> None:
    constants = reconstruct_constants()
    theta = 0.5
    d = 5.0 / 9.0
    best = grid_optimum(theta, d, constants)
    G, c, b = best

    dmax = 2.0 * theta - 5.0 / 14.0
    exponent_slack = dmax - d
    x0 = 1e31
    power_slack_at_x0 = x0 ** exponent_slack

    # Robustness check: deliberately much wider than the last printed digit in
    # the paper's c,b,G values.  Each endpoint is sampled; the square-window
    # test is made at the simple nearby choice c=5.62.
    B1_values = []
    B2_values = []
    for c0 in (5.182, 5.184):
        for b0 in (4.869, 4.871):
            for G0 in (0.0017, 0.0019):
                cc = reconstruct_constants(theta=0.45, c=c0, b=b0, G=G0)
                B1_values.append(cc.B1)
                B2_values.append(cc.B2)

    test_c = 5.62
    robust_G = []
    for B1 in (min(B1_values), max(B1_values)):
        for B2 in (min(B2_values), max(B2_values)):
            g, test_b = il_G(theta, d, test_c, ILConstants(B1, B2))
            robust_G.append(g)

    print("reconstructed B1,B2:", constants)
    print("theta=1/2, d=5/9 optimum (grid): G,c,b =", best)
    print("IL analytic level ceiling exponent:", dmax)
    print("level exponent slack:", exponent_slack, "= 11/126")
    print("x^(11/126) at x=1e31:", power_slack_at_x0)
    print("robust c=5.62 lower G under broad printed-value perturbation:", min(robust_G))
    print("corresponding b:", test_b)

    assert feasible(theta, d, c)
    assert G > 0.127
    assert abs(exponent_slack - 11.0 / 126.0) < 1e-12
    assert min(robust_G) > 0.127


if __name__ == "__main__":
    main()
