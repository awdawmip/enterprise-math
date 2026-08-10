import unittest

from enterprise_math.bounded_local_law_code import (
    code_is_injective_on_values,
    decode_local_code,
    reconstruct_exact_quotient_from_local_code,
    reflective_local_code_reproduces_exact_sequence,
)
from enterprise_math.bounded_local_law_reflection import (
    bounded_local_law_reflection_report,
    primitive_weighted_chain_collision_fixture,
    weighted_local_aggregate_alphabet,
)


class BoundedLocalLawCodeTests(unittest.TestCase):
    def test_parity_alone_is_not_reflective_on_zero_one_two(self):
        alphabet = frozenset({0, 1, 2})
        parity = lambda value: value % 2
        self.assertFalse(code_is_injective_on_values(alphabet, parity))

    def test_support_times_parity_is_reflective_on_zero_one_two(self):
        alphabet = frozenset({0, 1, 2})
        support_parity = lambda value: (value != 0, value % 2)
        self.assertTrue(code_is_injective_on_values(alphabet, support_parity))
        self.assertEqual(decode_local_code((False, 0), alphabet, support_parity), 0)
        self.assertEqual(decode_local_code((True, 1), alphabet, support_parity), 1)
        self.assertEqual(decode_local_code((True, 0), alphabet, support_parity), 2)

    def test_non_algebraic_local_code_can_recover_exact_weighted_machine(self):
        states, family, observation = primitive_weighted_chain_collision_fixture()
        alphabet = weighted_local_aggregate_alphabet(states, family)
        self.assertEqual(alphabet, frozenset({0, 1, 2}))

        # This code has no declared addition/multiplication at all.  It is only a
        # local finite label.  Reflection-before-compose is still exact because
        # the code is injective on the local law alphabet.
        names = {0: "zero", 1: "one", 2: "two"}
        code = lambda value: names.get(value, "outside-local-alphabet")
        self.assertTrue(code_is_injective_on_values(alphabet, code))
        self.assertTrue(
            reflective_local_code_reproduces_exact_sequence(
                states,
                family,
                observation,
                code,
            )
        )

        modular_report = bounded_local_law_reflection_report(
            states,
            family,
            observation,
            modulus=3,
        )
        reconstructed = reconstruct_exact_quotient_from_local_code(
            modular_report.exact_partition,
            states,
            family,
            code,
        )
        self.assertEqual(reconstructed, modular_report.exact_quotient_matrices)

    def test_code_may_collapse_large_derived_values_without_harming_local_reflection(self):
        states, family, observation = primitive_weighted_chain_collision_fixture()

        # Local values are only 0,1,2; outside that finite alphabet the code is
        # deliberately destructive.  In particular exact derived 4 is not meant
        # to be carried by the code.  It will be generated after decoding the
        # local machine and composing in Z.
        code = lambda value: value if value in (0, 1, 2) else "collapsed-derived"
        self.assertTrue(
            reflective_local_code_reproduces_exact_sequence(
                states,
                family,
                observation,
                code,
            )
        )
        self.assertEqual(code(4), code(99))

    def test_signed_local_alphabet_can_use_arbitrary_symbol_code(self):
        alphabet = frozenset({-1, 0, 1, 2})
        symbols = {-1: "neg", 0: "zero", 1: "one", 2: "two"}
        code = symbols.__getitem__
        self.assertTrue(code_is_injective_on_values(alphabet, code))
        for exact, encoded in symbols.items():
            self.assertEqual(decode_local_code(encoded, alphabet, code), exact)

    def test_noninjective_code_is_rejected_by_reflection_compiler(self):
        states, family, observation = primitive_weighted_chain_collision_fixture()
        with self.assertRaises(ValueError):
            reflective_local_code_reproduces_exact_sequence(
                states,
                family,
                observation,
                lambda value: value % 2,
            )


if __name__ == "__main__":
    unittest.main()
