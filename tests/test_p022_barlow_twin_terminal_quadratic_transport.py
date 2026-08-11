import pytest

from enterprise_math.p022_barlow_twin_terminal_quadratic_transport import (
    terminal_secondary_complete_escape_identity,
    terminal_secondary_high_support,
    terminal_secondary_index,
    terminal_secondary_interference_index,
)


def test_secondary_quadratic_high_support_on_both_interference_branches() -> None:
    expected = {
        # r=6: 2t-3=17 prime, so the t-1 term cancels and u=t-2.
        6: ((8, -1), (10, 1), (161, 1)),
        # r=21: 2t-3=77 composite, so u=t-1 survives.
        21: ((39, -1), (40, 1), (3041, 1)),
        36: ((69, -1), (70, 1), (9521, 1)),
        51: ((99, -1), (100, 1), (19601, 1)),
        96: ((189, -1), (190, 1), (71441, 1)),
    }
    for rank, support in expected.items():
        assert terminal_secondary_high_support(rank) == support
        assert support[-1][0] == terminal_secondary_index(rank) - 1
        assert support[0][0] == terminal_secondary_interference_index(rank)


def test_known_primitive_twin_examples_are_captured_before_secondary_transport() -> None:
    # q=13 and q=73 are primitive at r=6, but their first terminal row D_11
    # already has nonzero valuation.  The secondary theorem must refuse to
    # treat them as hypothetical complete-escape rows.
    for prime in (13, 73):
        with pytest.raises(ValueError, match="terminal defect has not cancelled"):
            terminal_secondary_complete_escape_identity(6, prime)
