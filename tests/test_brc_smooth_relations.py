from __future__ import annotations

import unittest

from enterprise_math.brc_multiplier_factor_scan import admissible_root_state_sequence
from enterprise_math.brc_smooth_relations import (
    GF2RelationAccumulator,
    congruence_from_dependency,
    factor_base,
    factor_over_base,
    first_layered_smooth_factor_witness,
    relation_from_multiplier_state,
)


class BRCSmoothRelationTests(unittest.TestCase):
    def test_exact_factor_base_factorization(self) -> None:
        base = factor_base(11)
        self.assertEqual(base, (2, 3, 5, 7, 11))
        self.assertEqual(factor_over_base(2**3 * 3 * 11**2, base), (3, 1, 0, 0, 2))
        self.assertIsNone(factor_over_base(13, base))

    def test_cross_multiplier_dependency_factors_14111(self) -> None:
        # 14111 = 103*137.  Two t=0 BRC strips give
        # m=1: x=119, D=50=2*5^2
        # m=8: x=336, D=8=2^3
        # Their parity vectors agree, so D1*D2=20^2 and the cross-strip
        # dependency yields a nontrivial square congruence modulo N.
        n = 14111
        base = factor_base(50)
        states = {state.multiplier: state for state in admissible_root_state_sequence(n)}
        r1 = relation_from_multiplier_state(states[1], 0, base)
        r8 = relation_from_multiplier_state(states[8], 0, base)
        self.assertIsNotNone(r1)
        self.assertIsNotNone(r8)
        assert r1 is not None and r8 is not None
        self.assertEqual((r1.x, r1.gap), (119, 50))
        self.assertEqual((r8.x, r8.gap), (336, 8))
        self.assertEqual(r1.parity_mask, r8.parity_mask)

        accumulator = GF2RelationAccumulator(base)
        self.assertIsNone(accumulator.add(r1))
        dependency = accumulator.add(r8)
        self.assertIsNotNone(dependency)
        assert dependency is not None
        congruence = congruence_from_dependency(tuple(accumulator.relations), dependency)
        self.assertEqual(congruence.y_mod_n, 20)
        self.assertIn(congruence.nontrivial_factor, (103, 137))

    def test_relation_multiplier_is_generator_not_dependency_coordinate(self) -> None:
        n = 14111
        base = factor_base(50)
        states = {state.multiplier: state for state in admissible_root_state_sequence(n)}
        relations = [
            relation_from_multiplier_state(states[m], 0, base)
            for m in (1, 8)
        ]
        self.assertTrue(all(relation is not None for relation in relations))
        for relation in relations:
            assert relation is not None
            self.assertEqual(
                (relation.x * relation.x - relation.gap) % n,
                0,
            )
        # No condition on the product of multiplier labels is required.
        self.assertNotEqual(1 * 8, 1)

    def test_layered_reference_collector_finds_factor(self) -> None:
        witness = first_layered_smooth_factor_witness(
            14111,
            smooth_bound=50,
            point_limit=10,
        )
        self.assertIsNotNone(witness)
        assert witness is not None
        self.assertIn(witness.factor, (103, 137))
        self.assertLessEqual(witness.points_examined, 10)
        self.assertGreaterEqual(witness.smooth_relations, 2)

    def test_full_exponents_survive_parity_projection(self) -> None:
        n = 14111
        base = factor_base(50)
        states = {state.multiplier: state for state in admissible_root_state_sequence(n)}
        r1 = relation_from_multiplier_state(states[1], 0, base)
        r8 = relation_from_multiplier_state(states[8], 0, base)
        assert r1 is not None and r8 is not None
        self.assertEqual(r1.parity_mask, r8.parity_mask)
        self.assertNotEqual(r1.exponents, r8.exponents)
        # Parity is sufficient for dependency detection, but the unequal full
        # exponent vectors are needed to reconstruct the square side y.


if __name__ == "__main__":
    unittest.main()
