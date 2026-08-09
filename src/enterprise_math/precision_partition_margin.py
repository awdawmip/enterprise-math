"""Exact finite partition-margin transport for the P018 precision calculus.

For a finite block B with signed integer coordinates x_i,y_i define

    X(B) = sum x_i
    Y(B) = sum y_i
    Z(B) = sum x_i*y_i
    D(B) = X(B)*Y(B) - Z(B).

If B is partitioned into children B_j, then

    D(B) = sum_j D(B_j) + sum_{i != j} X(B_i)*Y(B_j).

For a binary split L,R this becomes

    D(B)=D(L)+D(R)+X(L)Y(R)+X(R)Y(L).

The identity is elementary bilinearity.  P018 uses it as an exact account of
what coarse precision can hide: cross-child compensation is present at the
parent level and disappears when the observation is refined.
"""

from __future__ import annotations

from collections.abc import Sequence


def _validate_pair(x: Sequence[int], y: Sequence[int]) -> None:
    if len(x) != len(y):
        raise ValueError("x and y must have equal length")
    if any(isinstance(v, bool) or not isinstance(v, int) for v in (*x, *y)):
        raise ValueError("partition-margin coordinates must be integers")


def block_margin(x: Sequence[int], y: Sequence[int]) -> dict[str, int]:
    """Return X,Y,Z,D for one finite block."""
    _validate_pair(x, y)
    total_x = sum(x)
    total_y = sum(y)
    diagonal = sum(a * b for a, b in zip(x, y))
    margin = total_x * total_y - diagonal
    return {
        "X": total_x,
        "Y": total_y,
        "Z": diagonal,
        "D": margin,
        "size": len(x),
    }


def partition_margin_identity(
    x_children: Sequence[Sequence[int]],
    y_children: Sequence[Sequence[int]],
) -> dict[str, int]:
    """Evaluate the exact margin identity for an arbitrary finite partition."""
    if len(x_children) != len(y_children):
        raise ValueError("x_children and y_children must have equal length")
    children = [block_margin(x, y) for x, y in zip(x_children, y_children)]
    flat_x = [v for block in x_children for v in block]
    flat_y = [v for block in y_children for v in block]
    parent = block_margin(flat_x, flat_y)

    child_margin_sum = sum(child["D"] for child in children)
    cross_compensation = 0
    for i, left in enumerate(children):
        for j, right in enumerate(children):
            if i != j:
                cross_compensation += left["X"] * right["Y"]

    if parent["D"] != child_margin_sum + cross_compensation:
        raise AssertionError("partition margin identity failed")

    return {
        "parent_margin": parent["D"],
        "child_margin_sum": child_margin_sum,
        "cross_compensation": cross_compensation,
        "child_count": len(children),
    }


def binary_margin_identity(
    left_x: Sequence[int],
    left_y: Sequence[int],
    right_x: Sequence[int],
    right_y: Sequence[int],
) -> dict[str, int]:
    """Binary specialization D=P(children)+two oriented sibling cross terms."""
    left = block_margin(left_x, left_y)
    right = block_margin(right_x, right_y)
    data = partition_margin_identity((left_x, right_x), (left_y, right_y))
    oriented_cross = left["X"] * right["Y"] + right["X"] * left["Y"]
    if data["cross_compensation"] != oriented_cross:
        raise AssertionError("binary cross-compensation formula failed")
    return {
        **data,
        "left_margin": left["D"],
        "right_margin": right["D"],
        "left_to_right": left["X"] * right["Y"],
        "right_to_left": right["X"] * left["Y"],
    }


def dyadic_margin_levels(x: Sequence[int], y: Sequence[int]) -> dict[str, object]:
    """Return a telescoping margin budget over repeated contiguous binary refinement.

    The finest level is the singleton partition, whose total block margin is
    identically zero.  For each coarse-to-fine step the returned shell budget is
    exactly the sum of sibling cross-compensation terms removed by refinement.
    No power-of-two input length is required; odd blocks split as evenly as
    possible until every block is a singleton.
    """
    _validate_pair(x, y)
    n = len(x)
    if n == 0:
        return {"level_margin_sums": (0,), "shell_budgets": (), "terminal_level": 0}

    blocks = [(0, n)]
    level_sums: list[int] = []
    shell_budgets: list[int] = []

    while True:
        current_sum = sum(block_margin(x[a:b], y[a:b])["D"] for a, b in blocks)
        level_sums.append(current_sum)
        if all(b - a <= 1 for a, b in blocks):
            break

        next_blocks: list[tuple[int, int]] = []
        shell = 0
        for a, b in blocks:
            if b - a <= 1:
                next_blocks.append((a, b))
                continue
            mid = a + (b - a) // 2
            left = block_margin(x[a:mid], y[a:mid])
            right = block_margin(x[mid:b], y[mid:b])
            shell += left["X"] * right["Y"] + right["X"] * left["Y"]
            next_blocks.extend(((a, mid), (mid, b)))

        next_sum = sum(block_margin(x[a:b], y[a:b])["D"] for a, b in next_blocks)
        if current_sum != next_sum + shell:
            raise AssertionError("dyadic margin shell failed to telescope")
        shell_budgets.append(shell)
        blocks = next_blocks

    if level_sums[-1] != 0:
        raise AssertionError("singleton margin level must vanish")
    if level_sums[0] != sum(shell_budgets):
        raise AssertionError("coarse margin did not equal total precision-shell compensation")

    return {
        "level_margin_sums": tuple(level_sums),
        "shell_budgets": tuple(shell_budgets),
        "terminal_level": len(level_sums) - 1,
    }
