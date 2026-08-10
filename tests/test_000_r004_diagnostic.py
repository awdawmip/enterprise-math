"""Temporary early diagnostic aggregator for PR #449.

Runs only the newly added R004 proposal test modules before the long repository
suite.  Removed immediately after the first real failure is localized.
"""

import importlib
import io
import unittest


MODULES = (
    "test_r004_causal_identifiability_projective",
    "test_r004_causal_resource_budget",
    "test_r004_counterfactual_coupling",
    "test_r004_coupled_master_measure",
    "test_r004_history_information_schedule",
    "test_r004_local_window_presampling",
    "test_r004_record_boundary_defect",
)


class R004ProposalDiagnostic(unittest.TestCase):
    def test_new_proposal_modules_in_isolation(self):
        suite = unittest.TestSuite()
        loader = unittest.defaultTestLoader
        for name in MODULES:
            module = importlib.import_module(name)
            suite.addTests(loader.loadTestsFromModule(module))

        stream = io.StringIO()
        result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
        if not result.wasSuccessful():
            details = stream.getvalue()
            self.fail("R004 proposal isolated suite failed:\n" + details[-12000:])


if __name__ == "__main__":
    unittest.main()
