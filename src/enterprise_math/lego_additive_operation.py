"""Derive integer matrix operations from LEGO-style additive composition.

The primitive data are unit-slot generators and the image of each unit under an
operation.  A composition-preserving operation satisfies T(x+y)=T(x)+T(y) and
T(0)=0.  On free integer slot states this forces

    T(x) = sum_i x_i T(e_i).

An integer matrix is therefore only the coordinate table of the unit images;
it is not assumed as primitive ontology.
"""

from __future__ import annotations


Vector = tuple[int, ...]
Matrix = tuple[tuple[int, ...], ...]


def _require_vector(vector: Vector, name: str = "vector") -> None:
    if not isinstance(vector, tuple) or not vector:
        raise ValueError(f"{name} must be a non-empty tuple")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in vector):
        raise ValueError(f"{name} entries must be integers")


def compile_additive_operation(unit_images: tuple[Vector, ...]) -> Matrix:
    """Compile images T(e_i) into the coordinate matrix of the operation.

    `unit_images[i]` is the output state produced by one input unit in slot i.
    The returned matrix uses the standard convention `output = matrix * input`,
    so unit images become matrix columns.
    """
    if not isinstance(unit_images, tuple) or not unit_images:
        raise ValueError("unit_images must be a non-empty tuple")
    output_size = len(unit_images[0])
    if output_size == 0:
        raise ValueError("unit images must have positive output dimension")
    for image in unit_images:
        _require_vector(image, "unit image")
        if len(image) != output_size:
            raise ValueError("all unit images must share one output dimension")

    input_size = len(unit_images)
    return tuple(
        tuple(unit_images[column][row] for column in range(input_size))
        for row in range(output_size)
    )


def apply_integer_matrix(matrix: Matrix, state: Vector) -> Vector:
    """Apply an integer coordinate table to one LEGO slot-count state."""
    _require_vector(state, "state")
    if not isinstance(matrix, tuple) or not matrix:
        raise ValueError("matrix must be a non-empty tuple")
    if any(not isinstance(row, tuple) or len(row) != len(state) for row in matrix):
        raise ValueError("matrix column count must match state dimension")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for row in matrix
        for value in row
    ):
        raise ValueError("matrix entries must be integers")
    return tuple(
        sum(row[index] * state[index] for index in range(len(state)))
        for row in matrix
    )


def apply_additive_operation(unit_images: tuple[Vector, ...], state: Vector) -> Vector:
    """Apply T(x)=sum_i x_i T(e_i) directly from unit images."""
    _require_vector(state, "state")
    if len(unit_images) != len(state):
        raise ValueError("one unit image is required for each input slot")
    matrix = compile_additive_operation(unit_images)
    return apply_integer_matrix(matrix, state)


def add_states(left: Vector, right: Vector) -> Vector:
    """LEGO composition on signed integer slot states."""
    _require_vector(left, "left")
    _require_vector(right, "right")
    if len(left) != len(right):
        raise ValueError("state dimensions must match")
    return tuple(a + b for a, b in zip(left, right))


def additive_operation_preserves_composition(
    unit_images: tuple[Vector, ...],
    left: Vector,
    right: Vector,
) -> bool:
    """Executable check of T(x+y)=T(x)+T(y) for the compiled operation."""
    combined = apply_additive_operation(unit_images, add_states(left, right))
    separate = add_states(
        apply_additive_operation(unit_images, left),
        apply_additive_operation(unit_images, right),
    )
    return combined == separate


def unit_images_from_matrix(matrix: Matrix) -> tuple[Vector, ...]:
    """Recover the primitive unit effects from a coordinate matrix."""
    if not isinstance(matrix, tuple) or not matrix:
        raise ValueError("matrix must be a non-empty tuple")
    input_size = len(matrix[0])
    if input_size == 0:
        raise ValueError("matrix must have positive input dimension")
    if any(not isinstance(row, tuple) or len(row) != input_size for row in matrix):
        raise ValueError("matrix rows must have a common length")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for row in matrix
        for value in row
    ):
        raise ValueError("matrix entries must be integers")
    return tuple(
        tuple(matrix[row][column] for row in range(len(matrix)))
        for column in range(input_size)
    )


def nonnegative_unit_images(unit_images: tuple[Vector, ...]) -> bool:
    """Whether the operation preserves the unsigned LEGO monoid N^k -> N^m."""
    compile_additive_operation(unit_images)
    return all(value >= 0 for image in unit_images for value in image)
