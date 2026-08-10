from enterprise_math.poset_witness_count_horizon import (
    analyze_count_horizon,
    parity_collision_signature,
    parity_families_on_antichain,
)
from enterprise_math.poset_witness_count_zeta import count_required_labels


def test_count_recovery_horizon_is_width_on_chain_and_antichain():
    chain = tuple(range(4))
    chain_leq = frozenset((i, j) for i in chain for j in chain if i <= j)
    assert analyze_count_horizon(chain, chain_leq, 1).exact_recovery_guaranteed

    antichain, antichain_leq, _, _ = parity_families_on_antichain(4)
    assert not analyze_count_horizon(antichain, antichain_leq, 3).exact_recovery_guaranteed
    assert analyze_count_horizon(antichain, antichain_leq, 4).exact_recovery_guaranteed


def test_even_odd_families_are_indistinguishable_below_full_width():
    for width in range(2, 7):
        for arity_cap in range(width):
            even_signature, odd_signature = parity_collision_signature(width, arity_cap)
            assert even_signature == odd_signature


def test_full_width_query_separates_even_and_odd_families():
    for width in range(1, 7):
        elements, leq, even, odd = parity_families_on_antichain(width)
        full = frozenset(elements)
        even_count = count_required_labels(elements, leq, even, full)
        odd_count = count_required_labels(elements, leq, odd, full)
        assert {even_count, odd_count} == {0, 1}


def test_parity_collision_counts_have_closed_form_on_proper_queries():
    width = 5
    elements, leq, even, odd = parity_families_on_antichain(width)
    for size in range(width):
        required = frozenset(range(size))
        expected = 1 << (width - size - 1)
        assert count_required_labels(elements, leq, even, required) == expected
        assert count_required_labels(elements, leq, odd, required) == expected
