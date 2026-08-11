import itertools
import unittest

from enterprise_math.integer_action_capability_monotone_universality import (
    all_action_subsets,
    compile_monotone_capability_family,
    verify_monotone_capability_compilation,
)
from enterprise_math.monotone_design_formulaic_execution import (
    compile_and_verify_formulaic_monotone_family,
    monotone_compilation_action_masks,
    monotone_formulaic_execution_matches_literal,
    preserving_subset_matches_formulaic_cover,
)


def all_nonempty_upward_closed_families(action_count):
    subsets = all_action_subsets(action_count)
    full = frozenset(range(action_count))
    result = []
    for selector in itertools.product((0, 1), repeat=len(subsets)):
        family = frozenset(
            subset
            for subset, keep in zip(subsets, selector, strict=True)
            if keep
        )
        if not family or full not in family:
            continue
        upward = True
        for subset in family:
            for candidate in subsets:
                if subset.issubset(candidate) and candidate not in family:
                    upward = False
                    break
            if not upward:
                break
        if upward:
            result.append(family)
    return tuple(result)


class MonotoneDesignFormulaicExecutionTests(unittest.TestCase):
    def test_all_three_action_nonempty_upward_closed_families(self):
        families = all_nonempty_upward_closed_families(3)
        # Dedekind number M(3)=20 includes the constantly-false family.  The
        # parent compiler excludes the empty preserving family, leaving19.
        self.assertEqual(len(families), 19)

        checked_words = 0
        checked_subsets = 0
        for family in families:
            compilation = compile_and_verify_formulaic_monotone_family(
                3,
                tuple(family),
                max_word_length=4,
            )
            self.assertTrue(verify_monotone_capability_compilation(compilation))

            for subset in all_action_subsets(3):
                expected = subset in family
                self.assertEqual(
                    preserving_subset_matches_formulaic_cover(
                        compilation,
                        tuple(sorted(subset)),
                    ),
                    expected,
                )
                checked_subsets += 1

            for length in range(5):
                for word in itertools.product(range(3), repeat=length):
                    self.assertTrue(
                        monotone_formulaic_execution_matches_literal(
                            compilation,
                            word,
                        )
                    )
                    checked_words += 1

        self.assertEqual(checked_subsets, 19 * 8)
        self.assertEqual(checked_words, 19 * sum(3**length for length in range(5)))

    def test_arbitrary_antichain_geometry_still_executes_by_or(self):
        # Minimal preserving subsets {0} and {1,2}; unequal sizes, non-matroid
        # basis geometry, but the compiled execution law is still OR on masks.
        subsets = all_action_subsets(3)
        family = frozenset(
            subset
            for subset in subsets
            if frozenset({0}).issubset(subset)
            or frozenset({1, 2}).issubset(subset)
        )
        compilation = compile_monotone_capability_family(3, tuple(family))
        self.assertFalse(compilation.trivial_all_preserving)
        self.assertTrue(verify_monotone_capability_compilation(compilation))
        masks = monotone_compilation_action_masks(compilation)
        self.assertEqual(len(masks), 3)
        for word in ((0,), (1, 2), (2, 1, 2), (1, 0, 2, 0)):
            self.assertTrue(monotone_formulaic_execution_matches_literal(compilation, word))

    def test_all_preserving_trivial_family_has_identity_execution(self):
        family = all_action_subsets(3)
        compilation = compile_monotone_capability_family(3, family)
        self.assertTrue(compilation.trivial_all_preserving)
        self.assertEqual(monotone_compilation_action_masks(compilation), (0, 0, 0))
        self.assertTrue(monotone_formulaic_execution_matches_literal(compilation, (0, 1, 2, 0)))
        for subset in family:
            self.assertTrue(
                preserving_subset_matches_formulaic_cover(
                    compilation,
                    tuple(sorted(subset)),
                )
            )

    def test_formulaic_effect_masks_live_on_maximal_false_witness_universe(self):
        # Preserving iff at least two of three actions are selected.
        subsets = all_action_subsets(3)
        family = frozenset(subset for subset in subsets if len(subset) >= 2)
        compilation = compile_monotone_capability_family(3, tuple(family))
        self.assertEqual(len(compilation.maximal_false_subsets), 3)
        masks = monotone_compilation_action_masks(compilation)
        # Each action excludes exactly one maximal singleton-false set and covers
        # the other two false witnesses in the Set-Cover dual.
        self.assertEqual(tuple(mask.bit_count() for mask in masks), (2, 2, 2))

    def test_validation(self):
        compilation = compile_monotone_capability_family(
            2,
            (frozenset({0, 1}),),
        )
        with self.assertRaises(ValueError):
            preserving_subset_matches_formulaic_cover(compilation, (2,))


if __name__ == "__main__":
    unittest.main()
