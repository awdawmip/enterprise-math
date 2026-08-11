import pytest

from enterprise_math.p022_barlow_twin_terminal_simple_excess import (
    simple_secondary_quotient_zero_saturation,
)


def test_known_r6_primitives_are_captured_before_secondary_saturation() -> None:
    # q=13 and q=73 are primitive at r=6, but the first terminal defect does
    # not vanish, so the deep simple-saturation theorem must not activate.
    for prime in (13, 73):
        with pytest.raises(ValueError, match="terminal defect has not cancelled"):
            simple_secondary_quotient_zero_saturation(6, prime)
