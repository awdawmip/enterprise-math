from enterprise_math.divisor_layer_lift import (
    divisor_count_small,
    factor_forcing_target,
    is_squarefree_semiprime_small,
    local_composite_divisor_layers,
    minimal_divisor_layer_lift_small,
    neighborhood_profile,
    predicted_minimal_encoder_lift,
    squarefree_prime_layer_encoder,
)


def test_basic_divisor_counts() -> None:
    assert divisor_count_small(1) == 1
    assert divisor_count_small(12) == 6
    assert divisor_count_small(36) == 9
    assert divisor_count_small(210) == 16


def test_multiplicative_obstruction_classifier() -> None:
    assert factor_forcing_target(4, 6)
    assert factor_forcing_target(4, 10)
    assert not factor_forcing_target(4, 8)
    assert not factor_forcing_target(4, 12)
    assert factor_forcing_target(2, 9)


def test_squarefree_prime_layer_encoder() -> None:
    assert squarefree_prime_layer_encoder(2, 6) == 3
    assert squarefree_prime_layer_encoder(2, 10) == 5
    assert squarefree_prime_layer_encoder(2, 14) == 7
    assert squarefree_prime_layer_encoder(3, 12) == 3
    assert squarefree_prime_layer_encoder(2, 8) is None


def test_semiprime_encoder_minimal_lifts() -> None:
    # n=3*11.  T=2*r forces lambda=p_min^(r-2).
    assert predicted_minimal_encoder_lift((3, 11), 6) == 3
    assert predicted_minimal_encoder_lift((3, 11), 10) == 27
    assert predicted_minimal_encoder_lift((3, 11), 14) == 243
    assert minimal_divisor_layer_lift_small(33, 6, 10) == 3
    assert minimal_divisor_layer_lift_small(33, 10, 40) == 27
    assert minimal_divisor_layer_lift_small(33, 14, 300) == 243


def test_encoder_formula_over_small_squarefree_semiprimes() -> None:
    for n in range(6, 250):
        if not is_squarefree_semiprime_small(n):
            continue
        # Recover factors only for validation of this small-number probe.
        factors = tuple(p for p in range(2, n + 1) if n % p == 0 and all(p % q for q in range(2, int(p**0.5) + 1)))
        factors = tuple(p for p in factors if p < n)
        assert len(factors) == 2
        predicted = predicted_minimal_encoder_lift(factors, 6)
        assert predicted is not None
        assert divisor_count_small(n * predicted) == 6
        assert minimal_divisor_layer_lift_small(n, 6, predicted) == predicted


def test_neighborhood_keeps_all_layers() -> None:
    profile = neighborhood_profile(35, 2)
    assert profile.source_tau == 4
    assert profile.layers == local_composite_divisor_layers(35, 2)
    assert any(layer == 6 for _, layer in profile.layers)
    assert 6 in profile.factor_forcing_layers
    assert 6 in profile.strong_encoder_layers


def test_small_range_radius2_opportunity_counts() -> None:
    # Frozen exact finite diagnostic for 20 <= n < 1000.
    semiprimes = [n for n in range(20, 1000) if is_squarefree_semiprime_small(n)]
    any_forcing = 0
    strong = 0
    tau6 = 0
    modal_strong = 0
    for n in semiprimes:
        profile = neighborhood_profile(n, 2)
        any_forcing += bool(profile.factor_forcing_layers)
        strong += bool(profile.strong_encoder_layers)
        tau6 += 6 in profile.strong_encoder_layers
        modal = profile.modal_layer
        modal_strong += bool(modal and squarefree_prime_layer_encoder(2, modal) is not None)
    assert len(semiprimes) == 284
    assert any_forcing == 181
    assert strong == 146
    assert tau6 == 118
    assert modal_strong == 47
