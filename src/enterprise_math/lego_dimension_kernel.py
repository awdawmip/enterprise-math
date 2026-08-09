"""Recover a one-block causal coupling profile from a dimension-raising count law.

Assume a lower-dimensional LEGO fiber count F(c) with F(0)=1.  A newly attached
block has an occupancy-dependent integer profile k(b), independent of the
internal identity of the old fiber.  Then the observed raised count is

    G(c) = sum_{b=0}^c k(b) F(c-b).

Because F(0)=1, k is uniquely recovered by integer recursion with no division:

    k(c) = G(c) - sum_{b=0}^{c-1} k(b) F(c-b).

For the free one-slot block, k(b)=1 for all b and G=H_(m+1).
"""

from __future__ import annotations


def apply_dimension_kernel(
    lower_counts: tuple[int, ...],
    kernel: tuple[int, ...],
) -> tuple[int, ...]:
    if not isinstance(lower_counts, tuple) or not lower_counts:
        raise ValueError("lower_counts must be a non-empty tuple")
    if not isinstance(kernel, tuple) or not kernel:
        raise ValueError("kernel must be a non-empty tuple")
    if lower_counts[0] != 1:
        raise ValueError("lower_counts must be unit-normalized with F(0)=1")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in lower_counts + kernel):
        raise ValueError("counts and kernel values must be integers")
    maximum = min(len(lower_counts), len(kernel))
    return tuple(
        sum(kernel[b] * lower_counts[c - b] for b in range(c + 1))
        for c in range(maximum)
    )


def recover_dimension_kernel(
    lower_counts: tuple[int, ...],
    raised_counts: tuple[int, ...],
) -> tuple[int, ...]:
    """Exact fraction-free recursive deconvolution when lower_counts[0]=1."""
    if not isinstance(lower_counts, tuple) or not lower_counts:
        raise ValueError("lower_counts must be a non-empty tuple")
    if not isinstance(raised_counts, tuple) or not raised_counts:
        raise ValueError("raised_counts must be a non-empty tuple")
    if len(lower_counts) < len(raised_counts):
        raise ValueError("lower_counts must cover every requested raised index")
    if lower_counts[0] != 1:
        raise ValueError("lower_counts must be unit-normalized with F(0)=1")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in lower_counts + raised_counts):
        raise ValueError("count sequences must contain integers")
    kernel: list[int] = []
    for c, raised in enumerate(raised_counts):
        known = sum(kernel[b] * lower_counts[c - b] for b in range(c))
        kernel.append(raised - known)
    return tuple(kernel)


def dimension_kernel_roundtrip(
    lower_counts: tuple[int, ...],
    kernel: tuple[int, ...],
) -> bool:
    raised = apply_dimension_kernel(lower_counts, kernel)
    recovered = recover_dimension_kernel(lower_counts, raised)
    return recovered == kernel[: len(raised)]
