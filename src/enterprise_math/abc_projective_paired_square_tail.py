"""Paired-residual strengthening of the P025 projective sparse-failure layer.

For a primitive non-unit triple a+b=c, failure of PCC_eta in any cyclic
orientation forces *two distinct* multiplicity residuals to have large product.
If eta=p/q, then for a suitable pair x,y among a,b,c,

    m(x) m(y) >= c^(1+p/q) / 2.

The proof uses the additive relation, not a stronger conjecture.  If the
c-oriented ratio fails, pair c with the larger of a,b; otherwise pair the
failing a- or b-component with c.  The complementary block radical cancels.

Since the square-divisor root q2(n) satisfies q2(n)^2 >= m(n), a failure forces

    q2(x) q2(y) >= c^((1+eta)/2) / sqrt(2).

On a dyadic interval this yields a two-square-divisor union bound whose analytic
size is O_eta(X^(3/2-eta/2) log X).  This is an elementary internal improvement
of Supplement 50; it is not claimed competitive with classical or modern abc
exceptional-set estimates.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt

from .abc_projective_capacity_condition import projective_capacity_condition_state
from .abc_projective_sparse_failure import largest_square_divisor_root
from .abc_support import multiplicity_residual


@dataclass(frozen=True)
class PairedResidualWitness:
    abc: tuple[int, int, int]
    failing_cyclic_index: int
    component_indices: tuple[int, int]
    component_values: tuple[int, int]
    residuals: tuple[int, int]
    residual_product: int
    square_root_divisors: tuple[int, int]
    square_root_product: int


def _power_ge_fraction(value: object, c: int, p: int, q: int) -> bool:
    # ``value`` is a Fraction; keep the helper local to avoid float state.
    return value.numerator**q >= value.denominator**q * c**p


def projective_failure_paired_residual_witness(
    a: int,
    b: int,
    c: int,
    numerator: int,
    denominator: int,
) -> PairedResidualWitness | None:
    """Return the exact paired-residual witness for a non-unit PCC failure.

    ``None`` means PCC holds at eta=p/q.  The theorem here is deliberately
    scoped to ``a,b>1``.  Unit triples are one-dimensional in the additive
    relation and are counted separately in the sparse layer.
    """
    if not 0 < numerator < denominator:
        raise ValueError("require 0 < numerator < denominator")
    if a <= 1 or b <= 1:
        raise ValueError("paired-residual theorem here requires a,b>1")

    state = projective_capacity_condition_state(a, b, c)
    sigma = state.sigma_projective
    if not _power_ge_fraction(sigma, c, numerator, denominator):
        return None

    # cyclic defect order is c,b,a; component indices are 2,1,0.
    component_for_ratio = (2, 1, 0)
    residuals_all = tuple(multiplicity_residual(n) for n in (a, b, c))
    values = (a, b, c)

    for cyclic_index, (ratio, component_index) in enumerate(
        zip(state.cyclic_weighted_defects, component_for_ratio, strict=True)
    ):
        if not _power_ge_fraction(ratio, c, numerator, denominator):
            continue

        if component_index == 2:
            partner_index = 0 if a >= b else 1
        else:
            partner_index = 2

        residual_pair = (
            residuals_all[component_index],
            residuals_all[partner_index],
        )
        residual_product = residual_pair[0] * residual_pair[1]

        # Uniform constant-1/2 theorem:
        #     m(x)m(y) >= c^(1+p/q)/2
        # Raise to q to keep the check exact.
        if (2 * residual_product) ** denominator < c ** (denominator + numerator):
            raise AssertionError("PCC failure lost paired-residual lower bound")

        component_values = (values[component_index], values[partner_index])
        square_roots = tuple(largest_square_divisor_root(n) for n in component_values)
        square_product = square_roots[0] * square_roots[1]
        if square_product * square_product < residual_product:
            raise AssertionError("paired square roots failed residual-product domination")

        return PairedResidualWitness(
            abc=(a, b, c),
            failing_cyclic_index=cyclic_index,
            component_indices=(component_index, partner_index),
            component_values=component_values,
            residuals=residual_pair,
            residual_product=residual_product,
            square_root_divisors=square_roots,
            square_root_product=square_product,
        )

    raise AssertionError("projective maximum failed to expose a failing cyclic term")


def dyadic_paired_square_product_threshold(
    X: int, numerator: int, denominator: int
) -> int:
    """Return the exact integer product threshold for square-divisor roots.

    On X/2<c<=X, paired residual pressure gives

        (s*t)^(2q) > X^(q+p) / 2^(2q+p).

    The returned Y is the least positive integer with

        2^(2q+p) * Y^(2q) >= X^(q+p).
    """
    if isinstance(X, bool) or not isinstance(X, int) or X < 2:
        raise ValueError("X must be an integer >=2")
    if not 0 < numerator < denominator:
        raise ValueError("require 0 < numerator < denominator")
    p, q = numerator, denominator
    target = X ** (q + p)
    factor = 2 ** (2 * q + p)
    lo, hi = 1, max(1, isqrt(X) ** 2)
    while factor * hi ** (2 * q) < target:
        hi *= 2
    while lo < hi:
        mid = (lo + hi) // 2
        if factor * mid ** (2 * q) >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo


def dyadic_paired_square_triple_union_bound(
    X: int, numerator: int, denominator: int
) -> int:
    """Explicit union bound for non-unit PCC-failure triples on X/2<c<=X.

    There are three unordered component pairs.  For fixed square-root divisors
    s,t the number of possible ordered values in the two labelled positions is
    at most floor(X/s^2)*floor(X/t^2); the additive relation can only reduce
    this number.  Summing over s*t>=Y gives the finite exact union envelope.
    """
    Y = dyadic_paired_square_product_threshold(X, numerator, denominator)
    N = isqrt(X)
    counts = [0] + [X // (t * t) for t in range(1, N + 1)]
    tail = [0] * (N + 2)
    for t in range(N, 0, -1):
        tail[t] = tail[t + 1] + counts[t]

    pair_bound = 0
    for s in range(1, N + 1):
        t0 = (Y + s - 1) // s
        if t0 <= N:
            pair_bound += counts[s] * tail[t0]
    return 3 * pair_bound
