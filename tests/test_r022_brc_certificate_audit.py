import importlib.util
import pathlib
import sys
import unittest

MODULE = pathlib.Path(__file__).parents[1] / "experiments" / "r022_brc_certificate_audit.py"
spec = importlib.util.spec_from_file_location("r022_brc_certificate_audit", MODULE)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


class CertificateAuditTests(unittest.TestCase):
    def test_context_scoped_ncc_reuses_failure_over_a_class(self):
        r = mod.find_reusable_ncc()
        self.assertTrue(r["sound"])
        self.assertGreater(r["failure_depth"], 0)
        self.assertGreater(r["certified_branches"], 1)

    def test_ncc_must_include_context_dependency(self):
        r = mod.find_context_invalidation_witness()
        self.assertTrue(r["context_omission_would_false_prune"])
        self.assertGreaterEqual(r["failure_depth"], 2)

    def test_width_cap_is_not_exact_without_prune_certificate(self):
        r = mod.budget_truncation_kill()
        self.assertFalse(r["exact_without_prune_certificate"])
        self.assertEqual(r["lost_results"], (1,))

    def test_exactness_strata_are_distinct(self):
        s = mod.exactness_strata()
        self.assertIn("connector exact-state duplicate elimination under fixed context", s["exact_local_reduction"])
        self.assertIn("timeout kill and fixed k->k-1 rollback", s["not_exact_without_extra_certificate"])


if __name__ == "__main__":
    unittest.main()
