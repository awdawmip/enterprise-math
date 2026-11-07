from fractions import Fraction

from enterprise_math.brc_binary_first_return import (
    FAR,
    counter_factorization_holds,
    finite_horizon_resolved_class_count,
    finite_horizon_unlabeled_class_count,
    first_balance_return_count,
    first_return_mass,
    graded_naturality_holds,
    predictive_signature,
    quotient_states,
    renewal_coefficient_identity,
    signed_memory,
    swap_memory,
    unlabeled_memory,
)


def test_first_return_shells_and_renewal() -> None:
    assert [first_balance_return_count(n) for n in range(1, 9)] == [
        2,
        2,
        4,
        10,
        28,
        84,
        264,
        858,
    ]
    assert [first_return_mass(n) for n in range(1, 9)] == [
        Fraction(1, 2),
        Fraction(1, 8),
        Fraction(1, 16),
        Fraction(5, 128),
        Fraction(7, 256),
        Fraction(21, 1024),
        Fraction(33, 2048),
        Fraction(429, 32768),
    ]
    assert all(renewal_coefficient_identity(n) for n in range(1, 65))


def test_signed_and_unlabeled_memory_laws() -> None:
    for left in range(17):
        for right in range(17):
            z = signed_memory(left, right)
            assert signed_memory(right, left) == swap_memory(z)
            assert unlabeled_memory(z) == unlabeled_memory(-z)
            for common in range(9):
                assert signed_memory(left + common, right + common) == z


def test_predictive_class_counts() -> None:
    for horizon in range(13):
        signatures = {
            distance: predictive_signature(distance, horizon)
            for distance in range(0, 2 * horizon + 7)
        }
        assert len(set(signatures.values())) == finite_horizon_unlabeled_class_count(horizon)
        far_signature = predictive_signature(horizon + 1, horizon)
        assert all(
            predictive_signature(distance, horizon) == far_signature
            for distance in range(horizon + 1, 2 * horizon + 7)
        )
        assert finite_horizon_resolved_class_count(horizon) == 2 * horizon + 2


def test_graded_counter_factorization_and_naturality() -> None:
    for high in range(1, 17):
        for distance in range(0, 3 * high + 10):
            assert counter_factorization_holds(high, distance)
        for low in range(1, high + 1):
            for state in quotient_states(high):
                assert graded_naturality_holds(high, low, state)


def test_far_state_present_once() -> None:
    for horizon in range(9):
        states = quotient_states(horizon)
        assert states[-1] == FAR
        assert states.count(FAR) == 1
