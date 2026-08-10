from __future__ import annotations

import importlib.util
from itertools import combinations
from math import gcd
from pathlib import Path
import unittest


MODULE_PATH = Path(__file__).parents[1] / "experiments" / "r007_precision_tower.py"
spec = importlib.util.spec_from_file_location("r007_precision_tower", MODULE_PATH)
assert spec is not None and spec.loader is not None
tower = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tower)


class R007PrecisionTowerTests(unittest.TestCase):
    def test_lcm_tower_changes_exactly_at_prime_powers(self) -> None:
        previous = tower.lcm_ceiling(1)
        for N in range(2, 250):
            current = tower.lcm_ceiling(N)
            tick = tower.prime_power_tick(N)
            self.assertEqual(current != previous, tick is not None)
            if tick is not None:
                p, _k = tick
                self.assertEqual(current // previous, p)
                self.assertEqual(tower.big_omega(current), tower.big_omega(previous) + 1)
            previous = current

    def test_recovery_threshold_is_exact(self) -> None:
        for x in range(1, 300):
            threshold = tower.recovery_threshold(x)
            self.assertEqual(tower.precision_projection(x, threshold), x)
            for N in range(1, threshold):
                self.assertNotEqual(tower.precision_projection(x, N), x)

    def test_first_distinguishing_precision_is_exact(self) -> None:
        for x in range(1, 120):
            for y in range(1, 120):
                threshold = tower.first_distinguishing_precision(x, y)
                if x == y:
                    self.assertIsNone(threshold)
                    continue
                assert threshold is not None
                for N in range(1, threshold):
                    self.assertEqual(
                        tower.precision_projection(x, N),
                        tower.precision_projection(y, N),
                    )
                self.assertNotEqual(
                    tower.precision_projection(x, threshold),
                    tower.precision_projection(y, threshold),
                )

    def test_prime_power_tick_is_conditional_binary_split(self) -> None:
        for N in range(2, 26):
            profile = tower.tick_split_profile(N)
            if tower.prime_power_tick(N) is None:
                self.assertIsNone(profile)
                continue
            assert profile is not None
            old_count, split_count, new_count = profile
            old = tower.lcm_ceiling(N - 1)
            new = tower.lcm_ceiling(N)
            self.assertEqual(old_count, tower.divisor_count(old))
            self.assertEqual(new_count, tower.divisor_count(new))
            actual_split = 0
            for z in tower.positive_divisors(old):
                refinements = {
                    gcd(x, new)
                    for x in tower.positive_divisors(new)
                    if gcd(x, old) == z
                }
                if len(refinements) == 2:
                    actual_split += 1
                else:
                    self.assertEqual(len(refinements), 1)
            self.assertEqual(actual_split, split_count)

    def test_one_step_signature_already_determines_all_composites(self) -> None:
        probe_families = [
            (2,),
            (2, 3),
            (4, 6),
            (6, 10, 15),
            (4, 9, 25),
        ]
        for probes in probe_families:
            C = tower.future_envelope(probes)
            states = tower.positive_divisors(C * 6)
            for x in states:
                for y in states:
                    same_one_step = (
                        tower.one_step_signature(x, probes)
                        == tower.one_step_signature(y, probes)
                    )
                    same_all_composites = (
                        tower.subset_trace(x, probes)
                        == tower.subset_trace(y, probes)
                    )
                    self.assertEqual(same_one_step, same_all_composites)
                    self.assertEqual(
                        same_one_step,
                        gcd(x, C) == gcd(y, C),
                    )

    def test_supernatural_profiles_form_compatible_finite_projections(self) -> None:
        profiles = [
            {2: None},
            {2: None, 3: 2},
            {2: 4, 3: None, 5: 1},
            {2: 3, 7: 2},
        ]
        for profile in profiles:
            for N in range(1, 40):
                qN = tower.supernatural_projection(profile, N)
                for M in range(N, 40):
                    qM = tower.supernatural_projection(profile, M)
                    self.assertEqual(gcd(qM, tower.lcm_ceiling(N)), qN)

    def test_prime_power_token_downset_realizes_gcd_lcm_geometry(self) -> None:
        from math import lcm
        for x in range(1, 100):
            for y in range(1, 100):
                self.assertEqual(
                    tower.prime_power_tokens(gcd(x, y)),
                    tower.prime_power_tokens(x) & tower.prime_power_tokens(y),
                )
                self.assertEqual(
                    tower.prime_power_tokens(lcm(x, y)),
                    tower.prime_power_tokens(x) | tower.prime_power_tokens(y),
                )
        for N in range(1, 150):
            self.assertTrue(
                all(p**k <= N for p, k in tower.precision_token_ball(N))
            )

    def test_maximal_prime_power_basis_is_exact_bounded_envelope_basis(self) -> None:
        from math import lcm
        for N in range(2, 80):
            basis = tower.maximal_prime_power_basis(N)
            envelope = 1
            for value in basis:
                envelope = lcm(envelope, value)
            self.assertEqual(envelope, tower.lcm_ceiling(N))
            self.assertEqual(len(basis), tower.little_omega(tower.lcm_ceiling(N)))
            for i, a in enumerate(basis):
                for b in basis[i + 1 :]:
                    self.assertGreater(a * b, N)

        for N in range(2, 11):
            target = tower.lcm_ceiling(N)
            minimum = None
            values = tuple(range(1, N + 1))
            for size in range(1, len(values) + 1):
                found = False
                for subset in combinations(values, size):
                    envelope = 1
                    for value in subset:
                        envelope = lcm(envelope, value)
                    if envelope == target:
                        minimum = size
                        found = True
                        break
                if found:
                    break
            self.assertEqual(minimum, len(tower.maximal_prime_power_basis(N)))


if __name__ == "__main__":
    unittest.main()
