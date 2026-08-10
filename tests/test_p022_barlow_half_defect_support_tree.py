from enterprise_math.p022_barlow_half_defect_support_tree import (
    half_defect_exact_support,
    half_defect_support_tree,
    prime_halving_candidate_indices,
    prime_halving_node_count_crude_bound,
    prime_halving_nodes,
    support_tree_contains_exact_support,
    target_dangerous_offset_floor,
    target_low_support_bound,
    target_support_location_holds,
)
from enterprise_math.p022_barlow_low_order_defect_reduction import _is_prime


def test_prime_halving_tree_contains_recursive_basis_indices() -> None:
    assert prime_halving_nodes(27) == (3, 7)
    assert set(prime_halving_candidate_indices(27)) == {1, 2, 3, 4}
    for value in range(1, 500):
        assert len(prime_halving_nodes(value)) <= prime_halving_node_count_crude_bound(value)


def test_half_defect_tree_contains_exact_support() -> None:
    for prime in range(7, 2000):
        if prime % 24 not in (5, 23) or not _is_prime(prime):
            continue
        # p=5 is excluded above; p-2 is automatically composite in these target classes.
        assert support_tree_contains_exact_support(prime)
        assert set(half_defect_exact_support(prime)) <= set(half_defect_support_tree(prime))


def test_target_ap_low_support_bounds_are_exactly_located() -> None:
    examples = {
        29: (5, 9),
        53: (9, 17),
        101: (17, 33),
        173: (29, 57),
        197: (33, 65),
        269: (45, 89),
    }
    for prime, (bound, offset_floor) in examples.items():
        assert target_low_support_bound(prime) == bound
        assert target_dangerous_offset_floor(prime) == offset_floor
        assert target_support_location_holds(prime)


def test_target_support_bound_through_small_prime_range() -> None:
    for prime in range(7, 5000):
        if prime % 24 not in (5, 23) or not _is_prime(prime):
            continue
        assert target_support_location_holds(prime)
        midpoint = (prime - 1) // 2
        bound = target_low_support_bound(prime)
        exact = half_defect_exact_support(prime)
        assert all(index <= bound for index in exact if index != midpoint - 1)
