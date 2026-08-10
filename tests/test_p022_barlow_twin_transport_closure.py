from enterprise_math.p022_barlow_twin_transport_closure import (
    first_open_prime_threshold,
    scaled_twin_n1_high_support,
    scaled_twin_n2_high_support,
    strict_transport_ceiling,
    strict_transport_upper_gate,
)


def test_scaled_twin_final_gate_supports() -> None:
    assert scaled_twin_n1_high_support(36) == ((54, 1), (55, -1), (108, 1))
    assert scaled_twin_n2_high_support(36) == ((36, -1), (37, 1), (109, 1))
    assert scaled_twin_n2_high_support(90) == ((90, -1), (91, 1), (271, 1))


def test_upper_gate_chooses_the_existing_defect() -> None:
    # r=1884,q=6833 is a structural upper survivor at the preceding gate;
    # 6r+1=11305 is composite, so the 3r+1 defect is selected.
    assert strict_transport_upper_gate(1884, 6833) == (5653, -1)
    # r=90,q=353 has 6r+1=541 prime, so closure shifts one step.
    assert strict_transport_upper_gate(90, 353) == (272, 1)


def test_strict_window_has_uniform_ceiling_and_next_open_threshold() -> None:
    assert strict_transport_ceiling(69, 227) == 209
    assert first_open_prime_threshold(6) == 23
    assert first_open_prime_threshold(36) == 143
