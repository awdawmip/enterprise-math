from __future__ import annotations

import importlib.util
import unittest
from collections import Counter, deque
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "experiments" / "r007_resource_polynomial_calculus.py"
spec = importlib.util.spec_from_file_location("r007_resource_polynomial_calculus", MODULE_PATH)
assert spec is not None and spec.loader is not None
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[i]] for i in range(len(right)))


def local_cap_shift_bfs(alpha: int) -> Counter[int]:
    identity = tuple(range(alpha + 1))
    shift = tuple(min(j + 1, alpha) for j in range(alpha + 1))
    caps = [tuple(min(j, ceiling) for j in range(alpha + 1)) for ceiling in range(alpha)]
    generators = (shift, *caps)
    distance = {identity: 0}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for generator in generators:
            nxt = compose(generator, current)
            if nxt not in distance:
                distance[nxt] = distance[current] + 1
                queue.append(nxt)
    return Counter(distance.values())


class R007ResourcePolynomialCalculusTests(unittest.TestCase):
    def test_parallel_and_serial_composition_recover_antichain_and_chain_extremes(self) -> None:
        parallel = (1,)
        serial = (1,)
        for _ in range(6):
            parallel = mod.parallel_resource(parallel, mod.singleton_resource())
            serial = mod.serial_resource(serial, mod.singleton_resource())
        self.assertEqual(parallel, mod.antichain_resource(6))
        self.assertEqual(serial, mod.chain_resource(6))

    def test_divisor_cap_resource_has_tau_omega_Omega_readings(self) -> None:
        for exponents in ((1,), (3,), (1, 1, 1), (2, 3), (1, 2, 4)):
            poly = mod.gcd_cap_resource(exponents)
            table, primitive, worst = mod.resource_summary(poly)
            tau = 1
            for alpha in exponents:
                tau *= alpha + 1
            self.assertEqual(table, tau - 1)
            self.assertEqual(primitive, sum(exponents))
            self.assertEqual(worst, len(exponents))

    def test_shift_semantics_swaps_storage_and_worst_depth(self) -> None:
        for exponents in ((1,), (3,), (1, 1, 1), (2, 3), (1, 2, 4)):
            cap = mod.resource_summary(mod.gcd_cap_resource(exponents))
            shift = mod.resource_summary(mod.saturating_shift_resource(exponents))
            self.assertEqual(cap[0], shift[0])
            self.assertEqual(shift[1], cap[2])
            self.assertEqual(shift[2], cap[1])

    def test_local_cap_shift_depth_polynomial_matches_exact_bfs(self) -> None:
        for alpha in range(1, 7):
            spectrum = local_cap_shift_bfs(alpha)
            expected = mod.local_cap_shift_resource(alpha)
            self.assertEqual(tuple(spectrum.get(k, 0) for k in range(alpha + 1)), expected)
            self.assertEqual(sum(expected), mod.cap_shift_semantic_count_formula((alpha,)))

    def test_independent_prime_cap_shift_resources_multiply(self) -> None:
        for exponents in ((1, 1), (1, 2), (2, 2), (1, 2, 3)):
            poly = mod.cap_shift_resource(exponents)
            table, primitive, worst = mod.resource_summary(poly)
            self.assertEqual(table + 1, mod.cap_shift_semantic_count_formula(exponents))
            self.assertEqual(primitive, sum(exponents) + len(exponents))
            self.assertEqual(worst, sum(exponents))


if __name__ == "__main__":
    unittest.main()
