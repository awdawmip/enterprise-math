"""Exact discrete growth degree of a fixed-depth material boundary shell.

For dimension ``n>=1`` and fixed represented material depth ``K>=1``, the
coarse-contact box at spatial collapse factor ``d>=K`` contains ``d^n-1``
positive clearance states.  The states lying within the represented outer
material shell of depth ``K`` are exactly

    R_{n,K}(d) = d^n - (d-K)^n.

This is not just an asymptotic statement.  Forward differences give the exact
discrete degree:

    Delta^n R_{n,K}(d) = 0,
    Delta^(n-1) R_{n,K}(d) = n! K.

By contrast ``d^n-1`` has constant nth forward difference ``n!``.  Thus a fixed
finite material depth grows as an ``(n-1)``-degree boundary shell while the full
coarse-contact state space grows with degree ``n``.  The increasingly deep
interior is therefore material-underresolved unless the material state depth is
allowed to grow with spatial coarsening.

All statements are finite integer identities; no continuum volume or limiting
argument is used.
"""

from __future__ import annotations

from math import factorial


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def represented_boundary_shell_states(
    dimension: int,
    material_depth: int,
    collapse_factor: int,
) -> int:
    """Return ``d^n-(d-K)^n`` for ``d>=K``."""
    _require_positive("dimension", dimension)
    _require_positive("material_depth", material_depth)
    _require_positive("collapse_factor", collapse_factor)
    if collapse_factor < material_depth:
        raise ValueError("collapse_factor must be at least material_depth")
    return collapse_factor**dimension - (collapse_factor - material_depth) ** dimension


def coarse_only_contact_states(dimension: int, collapse_factor: int) -> int:
    """Return the positive coarse-contact box size ``d^n-1``."""
    _require_positive("dimension", dimension)
    _require_positive("collapse_factor", collapse_factor)
    return collapse_factor**dimension - 1


def forward_difference(values: tuple[int, ...] | list[int], order: int = 1) -> tuple[int, ...]:
    """Apply the forward-difference operator exactly ``order`` times."""
    if isinstance(order, bool) or not isinstance(order, int) or order < 0:
        raise ValueError("order must be a non-negative integer")
    current = tuple(values)
    if not current:
        raise ValueError("values must be nonempty")
    if order >= len(current):
        raise ValueError("difference order must be smaller than value count")
    for _ in range(order):
        current = tuple(right - left for left, right in zip(current, current[1:], strict=True))
    return current


def boundary_shell_degree_certificate(
    dimension: int,
    material_depth: int,
    start_factor: int | None = None,
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Return exact ``(n-1)``th and nth differences on a sufficient finite window."""
    _require_positive("dimension", dimension)
    _require_positive("material_depth", material_depth)
    start = material_depth if start_factor is None else start_factor
    _require_positive("start_factor", start)
    if start < material_depth:
        raise ValueError("start_factor must be at least material_depth")
    # n+2 samples leave at least two values after n forward differences and
    # therefore certify constancy/vanishing without symbolic algebra.
    values = tuple(
        represented_boundary_shell_states(dimension, material_depth, d)
        for d in range(start, start + dimension + 2)
    )
    lower = forward_difference(values, dimension - 1) if dimension > 1 else values
    upper = forward_difference(values, dimension)
    expected = factorial(dimension) * material_depth
    if any(value != expected for value in lower):
        raise AssertionError("boundary shell failed exact (n-1)th-difference certificate")
    if any(value != 0 for value in upper):
        raise AssertionError("boundary shell failed exact nth-difference extinction")
    return lower, upper
