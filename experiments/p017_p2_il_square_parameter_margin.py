"""Numerical certificate for the corrected Iwaniec-Laborde square-window P2 margin.

Research status: diagnostic/certificate only, not an explicit P2 theorem.

The 1981 final printed G(b,c) uses the maximal section-6 Selberg level
D1=(y^3/x)^(1/2+o(1)).  At theta=1/2 and the levels of interest here,
section 6 is instead capped by D1<=z^2 with z=D^(1/6).  This script enforces
that cap before optimizing the square-window main coefficient.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import log


@dataclass(frozen=True)
class ILConstants:
    B1: float
    B2: float


def alpha_from_theta_at_il_max(theta: float) -> float:
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


def selberg_level_exponent(theta: float, d: float) -> float:
    """Power exponent for the largest legal D1, suppressing tiny epsilon loss."""
    analytic_ceiling = (3.0 * theta - 1.0) / 2.0
    z_squared_ceiling = d / 3.0  # a=6, z=D^(1/6)
    return min(analytic_ceiling, z_squared_ceiling)


def square_G(theta: float, d: float, c: float, constants: ILConstants) -> tuple[float, float]:
    """Evaluate the section-6-level-corrected Laborde coefficient."""
    alpha = d / theta - 1.0
    if alpha <= 0.0:
        raise ValueError("need d>theta")
    b = 6.0 / d - 1.0 - c
    delta1 = selberg_level_exponent(theta, d)
    if delta1 <= 0.0:
        raise ValueError("non-positive Selberg level exponent")
    B1, B2 = constants.B1, constants.B2
    high_tail_penalty = 2.0 * ((c * d / 6.0 - theta) / delta1) ** 2
    G = (
        B1 * (c - b)
        + B2
        - (c / 6.0) * log(6.0 / (1.0 + alpha))
        - ((6.0 - c) / 6.0) * log(6.0 * alpha / (1.0 + alpha))
        - high_tail_penalty
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
        G, b = square_G(theta, d, c, constants)
        if G > best[0]:
            best = (G, c, b)
    return best


def main() -> None:
    constants = reconstruct_constants()
    theta = 0.5
    d = 5.0 / 9.0
    best = grid_optimum(theta, d, constants)
    G, c, b = best

    delta1 = selberg_level_exponent(theta, d)
    advanced_dmax = 2.0 * theta - 5.0 / 14.0
    advanced_gap = advanced_dmax - d
    base_dmax = 5.0 / 8.0
    base_gap = base_dmax - d
    x0 = 1e31

    print("reconstructed B1,B2:", constants)
    print("legal Selberg D1 exponent:", delta1, "(d/3)")
    print("theta=1/2, d=5/9 corrected optimum G,c,b:", best)
    print("advanced pair ceiling/gap:", advanced_dmax, advanced_gap)
    print("base (1/2,1/2) ceiling/gap:", base_dmax, base_gap)
    print("x^(base gap) at x=1e31:", x0 ** base_gap)

    assert abs(delta1 - d / 3.0) < 1e-12
    assert feasible(theta, d, c)
    assert G > 0.122
    assert abs(base_gap - 5.0 / 72.0) < 1e-12


if __name__ == "__main__":
    main()
