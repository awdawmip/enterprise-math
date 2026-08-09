from itertools import product

from enterprise_math.p022_barlow_repair_polynomial import chamber_successors
from enterprise_math.p022_barlow_stabilizer_lifting import (
    apply_b2,
    b2_elements,
    edge_stabilizer,
    local_event_branch_factor,
    local_stabilizer_index,
    stabilizer_product_lift_count,
    verify_local_stabilizer_event_identity,
    verify_path_stabilizer_lifting,
    vertex_stabilizer,
)
from enterprise_math.p022_barlow_two_sided_repair import (
    unordered_absolute_pair_history,
)


def _words(length: int):
    return tuple(tuple(word) for word in product((-1, 1), repeat=length))


def test_b2_group_has_eight_distinct_signed_permutations_on_generic_state() -> None:
    elements = b2_elements()
    assert len(elements) == 8
    generic = (2, 5)
    images = {apply_b2(element, generic) for element in elements}
    assert len(images) == 8


def test_vertex_stabilizers_have_expected_wall_sizes() -> None:
    assert len(vertex_stabilizer((0, 0))) == 8
    assert len(vertex_stabilizer((0, 4))) == 2
    assert len(vertex_stabilizer((3, 3))) == 2
    assert len(vertex_stabilizer((2, 5))) == 1


def test_local_stabilizer_index_equals_event_branch_factor_for_all_small_transitions() -> None:
    for a in range(0, 8):
        for b in range(a, 9):
            source = (a, b)
            for target in chamber_successors(source):
                stabilizer, event = verify_local_stabilizer_event_identity(
                    source, target
                )
                assert stabilizer == event
                assert stabilizer in (1, 2, 4)
                assert local_stabilizer_index(source, target) == (
                    len(vertex_stabilizer(source))
                    // len(edge_stabilizer(source, target))
                )


def test_named_wall_transition_indices() -> None:
    # Origin releases two sign labels at once.
    assert local_stabilizer_index((0, 0), (1, 1)) == 4
    # Coordinate wall departure releases one sign label.
    assert local_stabilizer_index((0, 2), (1, 3)) == 2
    # Diagonal split releases one side-exchange label.
    assert local_stabilizer_index((2, 2), (1, 3)) == 2
    # Remaining on the diagonal preserves the swap stabilizer: no repair bit.
    assert local_stabilizer_index((2, 2), (3, 3)) == 1
    # Generic interior transition has no stabilizer ambiguity.
    assert local_stabilizer_index((1, 4), (2, 5)) == 1


def test_stabilizer_product_recovers_every_short_microscopic_fiber() -> None:
    for length in range(0, 7):
        words = _words(length)
        histories = {
            unordered_absolute_pair_history(left, right)
            for left in words
            for right in words
        }
        for history in histories:
            stabilizer, event, existing = verify_path_stabilizer_lifting(history)
            assert stabilizer == event == existing
            assert stabilizer_product_lift_count(history) == existing


def test_repeated_wall_resets_accumulate_beyond_terminal_stabilizer_scale() -> None:
    history = (
        (1, 1),
        (0, 0),
        (1, 1),
        (0, 0),
        (1, 1),
    )
    assert stabilizer_product_lift_count(history) == 64
    assert len(vertex_stabilizer(history[-1])) == 2
