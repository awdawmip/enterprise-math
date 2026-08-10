"""Exact kernel classification for twin-prime delayed defect observations.

This module isolates the combinatorial geometry from the Franel arithmetic.
Let ``r`` be a nontrivial twin-prime center and ``T=2r-1``.  Consider a
nonnegative depth profile ``z_j`` on ``r,...,T`` with

    z_r > 0,
    z_j z_(j+1) = 0

for every adjacent pair.  The second condition is exactly the structural
property supplied by the Franel recurrence to q-adic zero depths below q.

The twin-blackout defect observations are

    delta_n(z) = z_n-z_(n-1)              (r+2 <= n < T),
    delta_T(z) = z_T-z_(T-1)+z_r,

but only for segments n whose odd boundary ``2n-1`` is composite.  Thus the
interior is the incidence/coboundary operator of a path after deleting the
edges whose odd-boundary labels are prime.

For such an adjacent-sparse depth profile, every existing first-reentry defect
vanishes if and only if all of the following hold:

1. ``z_(T-1)=z_r`` and ``z_T=0``;
2. ``4r-5`` is prime, so the edge/defect at ``T-1`` is absent;
3. every positive interior vertex ``s`` with ``r+2 <= s <= T-2`` is isolated
   by deleted edges, equivalently ``2s-1`` and ``2s+1`` are both prime.

The proof is the graph kernel in one line: zero gradients make z constant on
each connected component of the surviving path; adjacent-sparsity forbids a
positive constant on any component containing an edge, so positive interior
mass can live only on singleton components.  The terminal observation then
pairs the primitive source at r exactly with the endpoint mass at T-1.

For an actual primitive Franel valuation row, Jarvis--Verrill reflection adds
``q>=3r-1`` to this exact geometric classification.  Hence the global P022
problem is cleanly separated into:

    prime-edge coboundary geometry  +  admissible Franel depth profiles.
"""

from __future__ import annotations

from .p022_barlow_low_order_defect_reduction import _is_prime, composite_indices
from .p022_barlow_twin_defect_difference import twin_blackout_target, twin_zero_local_visibility

DepthProfile = tuple[tuple[int, int], ...]  # sorted (index, positive depth)


def _profile_map(rank: int, profile: DepthProfile) -> tuple[int, dict[int, int]]:
    target = twin_blackout_target(rank)
    depths: dict[int, int] = {}
    previous = rank - 1
    for index, depth in profile:
        if isinstance(index, bool) or not isinstance(index, int):
            raise ValueError("depth index must be an integer")
        if index < rank or index > target or index <= previous:
            raise ValueError("depth indices must be strictly increasing inside [r,T]")
        if isinstance(depth, bool) or not isinstance(depth, int) or depth <= 0:
            raise ValueError("stored depths must be positive integers")
        depths[index] = depth
        previous = index
    if depths.get(rank, 0) <= 0:
        raise ValueError("primitive source depth z_r must be positive")
    for index in range(rank, target):
        if depths.get(index, 0) and depths.get(index + 1, 0):
            raise ValueError("adjacent positive depths are forbidden")
    return target, depths


def twin_escape_observations(rank: int, profile: DepthProfile) -> tuple[tuple[int, int], ...]:
    """All existing first-reentry defect observations of an abstract depth profile."""
    target, depths = _profile_map(rank, profile)
    observations = []
    for segment in composite_indices(target):
        if segment < rank + 2:
            continue
        value = depths.get(segment, 0) - depths.get(segment - 1, 0)
        if segment == target:
            value += depths[rank]
        observations.append((segment, value))
    return tuple(observations)


def twin_escape_kernel_conditions(rank: int, profile: DepthProfile) -> bool:
    """The three exact geometric conditions for complete first-reentry escape."""
    target, depths = _profile_map(rank, profile)
    if depths.get(target - 1, 0) != depths[rank]:
        return False
    if depths.get(target, 0) != 0:
        return False
    if not _is_prime(4 * rank - 5):
        return False
    for index in range(rank + 2, target - 1):
        if depths.get(index, 0) and twin_zero_local_visibility(index) != (False, False):
            return False
    return True


def twin_escape_kernel_theorem(rank: int, profile: DepthProfile) -> bool:
    """Certify complete invisibility iff the exact kernel conditions hold."""
    observations = twin_escape_observations(rank, profile)
    invisible = all(value == 0 for _, value in observations)
    predicted = twin_escape_kernel_conditions(rank, profile)
    if invisible != predicted:
        raise AssertionError("twin escape kernel classification failed")
    return invisible


def twin_escape_positive_components(rank: int, profile: DepthProfile) -> tuple[tuple[int, ...], ...]:
    """Connected positive supports after deleting prime-boundary edges.

    Under the adjacent-sparse contract, every positive component of a kernel
    profile away from the terminal pair is a singleton twin center.
    """
    target, depths = _profile_map(rank, profile)
    positive = set(depths)
    components = []
    seen: set[int] = set()
    for start in sorted(positive):
        if start in seen:
            continue
        component = {start}
        stack = [start]
        while stack:
            current = stack.pop()
            for neighbor, segment in ((current - 1, current), (current + 1, current + 1)):
                if neighbor not in positive or neighbor < rank or neighbor > target:
                    continue
                if segment < rank + 2 or segment > target:
                    continue
                if _is_prime(2 * segment - 1):
                    continue
                if neighbor not in component:
                    component.add(neighbor)
                    stack.append(neighbor)
        seen.update(component)
        components.append(tuple(sorted(component)))
    return tuple(components)
