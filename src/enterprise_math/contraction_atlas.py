"""Integer chart tools for the P019 Contraction Atlas.

A chart is a rooted ordered binary tree on labeled unit slots. Two coordinate
systems are useful on the same tree:

- split-flow coordinates f_v = total of the left child at each internal node;
  for fixed root total these form a unimodular Z^(N-1) chart;
- imbalance coordinates z_v = n*a-m*b = |v|*f_v-m*c_v;
  these trade lattice density for proportional-deviation/locality structure.

For fixed root total, legal z-tuples form an affine sublattice of Z^(N-1).
"""

from __future__ import annotations

from typing import TypeAlias

from .contraction_trace import square_split_imbalance


Tree: TypeAlias = int | tuple["Tree", "Tree"]


def _validate_tree(tree: Tree) -> tuple[int, ...]:
    if isinstance(tree, bool):
        raise ValueError("leaf labels must be non-negative integers")
    if isinstance(tree, int):
        if tree < 0:
            raise ValueError("leaf labels must be non-negative integers")
        return (tree,)
    if not isinstance(tree, tuple) or len(tree) != 2:
        raise ValueError("internal nodes must be binary tuples")
    left = _validate_tree(tree[0])
    right = _validate_tree(tree[1])
    leaves = left + right
    if len(set(leaves)) != len(leaves):
        raise ValueError("leaf labels must be unique")
    return leaves


def tree_leaves(tree: Tree) -> tuple[int, ...]:
    """Return leaf labels in chart order."""
    return _validate_tree(tree)


def tree_size(tree: Tree) -> int:
    """Number of unit-slot leaves in a contraction tree."""
    return len(_validate_tree(tree))


def internal_block_sizes(tree: Tree) -> tuple[int, ...]:
    """Return internal subtree leaf counts in postorder."""
    _validate_tree(tree)

    def visit(node: Tree) -> tuple[int, tuple[int, ...]]:
        if isinstance(node, int):
            return 1, ()
        left_size, left_sizes = visit(node[0])
        right_size, right_sizes = visit(node[1])
        size = left_size + right_size
        return size, left_sizes + right_sizes + (size,)

    return visit(tree)[1]


def chart_index_product(tree: Tree) -> int:
    """Product of all internal block sizes."""
    product = 1
    for size in internal_block_sizes(tree):
        product *= size
    return product


def imbalance_tags(tree: Tree, leaf_totals: dict[int, int]) -> tuple[int, ...]:
    """Return postorder imbalance coordinates for one fine integer state."""
    leaves = _validate_tree(tree)
    if set(leaf_totals) != set(leaves):
        raise ValueError("leaf_totals must be defined on exactly the tree leaves")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in leaf_totals.values()):
        raise ValueError("leaf totals must be integers")

    def visit(node: Tree) -> tuple[int, int, tuple[int, ...]]:
        if isinstance(node, int):
            return 1, leaf_totals[node], ()
        left_size, left_total, left_tags = visit(node[0])
        right_size, right_total, right_tags = visit(node[1])
        tag = square_split_imbalance(left_size, right_size, left_total, right_total)
        return (
            left_size + right_size,
            left_total + right_total,
            left_tags + right_tags + (tag,),
        )

    return visit(tree)[2]


def split_flow_coordinates(tree: Tree, leaf_totals: dict[int, int]) -> tuple[int, ...]:
    """Return preorder left-child totals at every internal node.

    With a fixed root total, these N-1 integers are unconstrained: every integer
    tuple reconstructs exactly one fine leaf state.
    """
    leaves = _validate_tree(tree)
    if set(leaf_totals) != set(leaves):
        raise ValueError("leaf_totals must be defined on exactly the tree leaves")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in leaf_totals.values()):
        raise ValueError("leaf totals must be integers")

    def total(node: Tree) -> int:
        if isinstance(node, int):
            return leaf_totals[node]
        return total(node[0]) + total(node[1])

    coordinates: list[int] = []

    def visit(node: Tree) -> None:
        if isinstance(node, int):
            return
        coordinates.append(total(node[0]))
        visit(node[0])
        visit(node[1])

    visit(tree)
    return tuple(coordinates)


def recover_leaf_totals_from_split_flows(
    tree: Tree, root_total: int, split_flows: tuple[int, ...]
) -> dict[int, int]:
    """Recover leaves from arbitrary preorder split-flow integers and root total."""
    leaves = _validate_tree(tree)
    if isinstance(root_total, bool) or not isinstance(root_total, int):
        raise ValueError("root_total must be an integer")
    if not isinstance(split_flows, tuple) or any(
        isinstance(value, bool) or not isinstance(value, int) for value in split_flows
    ):
        raise ValueError("split_flows must be an integer tuple")
    if len(split_flows) != len(leaves) - 1:
        raise ValueError("a binary N-leaf tree needs exactly N-1 split flows")

    flow_index = 0
    result: dict[int, int] = {}

    def visit(node: Tree, node_total: int) -> None:
        nonlocal flow_index
        if isinstance(node, int):
            result[node] = node_total
            return
        left_total = split_flows[flow_index]
        flow_index += 1
        right_total = node_total - left_total
        visit(node[0], left_total)
        visit(node[1], right_total)

    visit(tree, root_total)
    if flow_index != len(split_flows):
        raise AssertionError("all split flows must be consumed exactly once")
    return result


def split_flows_to_preorder_imbalances(
    tree: Tree, root_total: int, split_flows: tuple[int, ...]
) -> tuple[int, ...]:
    """Convert an unconstrained split-flow chart to preorder imbalance tags."""
    leaves = _validate_tree(tree)
    if isinstance(root_total, bool) or not isinstance(root_total, int):
        raise ValueError("root_total must be an integer")
    if not isinstance(split_flows, tuple) or any(
        isinstance(value, bool) or not isinstance(value, int) for value in split_flows
    ):
        raise ValueError("split_flows must be an integer tuple")
    if len(split_flows) != len(leaves) - 1:
        raise ValueError("a binary N-leaf tree needs exactly N-1 split flows")

    flow_index = 0
    tags: list[int] = []

    def visit(node: Tree, node_total: int) -> int:
        nonlocal flow_index
        if isinstance(node, int):
            return 1
        left_size = tree_size(node[0])
        right_size = tree_size(node[1])
        left_total = split_flows[flow_index]
        flow_index += 1
        right_total = node_total - left_total
        tags.append(
            square_split_imbalance(
                left_size, right_size, left_total, right_total
            )
        )
        visit(node[0], left_total)
        visit(node[1], right_total)
        return left_size + right_size

    visit(tree, root_total)
    return tuple(tags)


def split_flow_transform_matrix(tree: Tree) -> tuple[tuple[int, ...], ...]:
    """Linear matrix from zero-root-total split flows to preorder imbalance tags."""
    size = tree_size(tree)
    if size == 1:
        return ()
    coordinate_count = size - 1
    columns = []
    for column in range(coordinate_count):
        flows = tuple(1 if index == column else 0 for index in range(coordinate_count))
        columns.append(split_flows_to_preorder_imbalances(tree, 0, flows))
    return tuple(
        tuple(columns[column][row] for column in range(coordinate_count))
        for row in range(coordinate_count)
    )


def chart_matrix(tree: Tree) -> tuple[tuple[int, ...], ...]:
    """Linear matrix from a zero-sum leaf basis to postorder imbalance coordinates.

    The last leaf in chart order is dependent. Basis column j assigns +1 to
    leaf j and -1 to the dependent last leaf, keeping root total zero.
    """
    leaves = _validate_tree(tree)
    if len(leaves) == 1:
        return ()
    dependent = leaves[-1]
    columns = []
    for leaf in leaves[:-1]:
        state = {label: 0 for label in leaves}
        state[leaf] = 1
        state[dependent] = -1
        columns.append(imbalance_tags(tree, state))
    row_count = len(leaves) - 1
    return tuple(
        tuple(columns[column][row] for column in range(row_count))
        for row in range(row_count)
    )


def _determinant_bareiss(matrix: tuple[tuple[int, ...], ...]) -> int:
    """Exact integer determinant via the fraction-free Bareiss algorithm."""
    if not matrix:
        return 1
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("matrix must be square")
    data = [list(row) for row in matrix]
    sign = 1
    previous_pivot = 1
    for pivot_index in range(size - 1):
        if data[pivot_index][pivot_index] == 0:
            swap = next(
                (
                    row
                    for row in range(pivot_index + 1, size)
                    if data[row][pivot_index] != 0
                ),
                None,
            )
            if swap is None:
                return 0
            data[pivot_index], data[swap] = data[swap], data[pivot_index]
            sign = -sign
        pivot = data[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    data[row][column] * pivot
                    - data[row][pivot_index] * data[pivot_index][column]
                )
                if numerator % previous_pivot != 0:
                    raise AssertionError("Bareiss exact division failed")
                data[row][column] = numerator // previous_pivot
        previous_pivot = pivot
    return sign * data[-1][-1]


def chart_determinant(tree: Tree) -> int:
    """Absolute determinant of the fixed-root-total imbalance chart matrix."""
    return abs(_determinant_bareiss(chart_matrix(tree)))


def split_flow_transform_determinant(tree: Tree) -> int:
    """Absolute determinant from unimodular split flows to imbalance coordinates."""
    return abs(_determinant_bareiss(split_flow_transform_matrix(tree)))


def chart_index_identity(tree: Tree) -> tuple[int, int]:
    """Return determinant index and internal-size product for comparison."""
    return chart_determinant(tree), chart_index_product(tree)
