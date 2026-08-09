from collections import Counter
from itertools import product

from enterprise_math.p022_barlow_coordination_fibers import (
    absolute_imbalance_fiber_size,
    admissible_absolute_imbalances,
    energy_congruence_class,
    maximum_drift_energy,
    maximum_shell_cardinality,
    minimum_drift_energy,
    minimum_shell_cardinality,
    possible_shell_drift_energies,
    shell_cardinality_fiber_spectrum,
    shell_cardinality_from_energy,
    shell_energy_fiber_size,
    shell_energy_fiber_spectrum,
)


def _imbalance(word) -> int:
    return sum(word)


def test_absolute_imbalance_fibers_match_direct_word_enumeration() -> None:
    for radius in range(0, 10):
        words = tuple(product((-1, 1), repeat=radius))
        for drift in admissible_absolute_imbalances(radius):
            direct = sum(1 for word in words if abs(_imbalance(word)) == drift)
            assert absolute_imbalance_fiber_size(radius, drift) == direct
        assert sum(
            absolute_imbalance_fiber_size(radius, drift)
            for drift in admissible_absolute_imbalances(radius)
        ) == 2 ** radius


def test_energy_fiber_spectrum_matches_all_two_sided_short_windows() -> None:
    for radius in range(0, 7):
        words = tuple(product((-1, 1), repeat=radius))
        direct: Counter[int] = Counter()
        for left in words:
            left_drift = _imbalance(left)
            for right in words:
                right_drift = _imbalance(right)
                direct[left_drift * left_drift + right_drift * right_drift] += 1

        assert possible_shell_drift_energies(radius) == tuple(sorted(direct))
        assert dict(shell_energy_fiber_spectrum(radius)) == dict(direct)
        assert sum(size for _, size in shell_energy_fiber_spectrum(radius)) == 4 ** radius


def test_shell_cardinality_spectrum_is_exact_relabelling_of_energy_spectrum() -> None:
    for radius in range(0, 10):
        energy_spectrum = dict(shell_energy_fiber_spectrum(radius))
        cardinality_spectrum = dict(shell_cardinality_fiber_spectrum(radius))
        assert len(energy_spectrum) == len(cardinality_spectrum)
        for energy, fiber_size in energy_spectrum.items():
            shell = shell_cardinality_from_energy(radius, energy)
            assert cardinality_spectrum[shell] == fiber_size


def test_extreme_shell_cardinality_bounds_are_attained() -> None:
    for radius in range(1, 20):
        energies = possible_shell_drift_energies(radius)
        assert min(energies) == minimum_drift_energy(radius)
        assert max(energies) == maximum_drift_energy(radius)
        shells = tuple(shell_cardinality_from_energy(radius, energy) for energy in energies)
        assert min(shells) == minimum_shell_cardinality(radius)
        assert max(shells) == maximum_shell_cardinality(radius)


def test_energy_congruence_is_forced_but_not_every_congruent_value_is_represented() -> None:
    # Congruence is necessary.  Sum-of-two-squares arithmetic creates further
    # holes for sufficiently large radii.
    hole_seen = False
    for radius in range(1, 30):
        residue, modulus = energy_congruence_class(radius)
        energies = set(possible_shell_drift_energies(radius))
        for energy in range(min(energies), max(energies) + 1):
            if energy % modulus == residue and energy not in energies:
                hole_seen = True
                break
        if hole_seen:
            break
    assert hole_seen


def test_single_energy_fiber_formula_matches_direct_absolute_drift_sum() -> None:
    radius = 6
    for energy in possible_shell_drift_energies(radius):
        expected = 0
        for left in admissible_absolute_imbalances(radius):
            for right in admissible_absolute_imbalances(radius):
                if left * left + right * right == energy:
                    expected += absolute_imbalance_fiber_size(
                        radius, left
                    ) * absolute_imbalance_fiber_size(radius, right)
        assert shell_energy_fiber_size(radius, energy) == expected
