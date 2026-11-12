"""Regression checks for adaptive guidance, not a research step checklist."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from control_plane import check_context_budget as checker
ROOT = Path(__file__).resolve().parents[1]
class ResearchAutonomyTests(unittest.TestCase):
    def test_exceeding_reading_targets_is_not_a_gate(self):
        policy = json.loads((ROOT / 'research_context_budget.json').read_text())
        policy['bounded_defaults'] = {k: 1000 for k in policy['bounded_defaults']}
        policy['static_hot_start_guard']['max_file_bytes'] = 1
        policy['static_hot_start_guard']['max_total_bytes'] = 2
        cold = policy['researcher_cold_start_envelope']
        cold['normal_remote_source_reads_before_math_max'] = 50
        cold['cold_start_raw_soft_max_bytes'] = 200000
        cold['cold_start_raw_hard_max_bytes'] = 100
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory) / 'policy.json'
            p.write_text(json.dumps(policy))
            with patch.object(checker, 'POLICY_PATH', p):
                result = checker.check()
        self.assertTrue(result['warnings'])
        self.assertEqual(result['reading_budget_mode'], 'ADAPTIVE_SOFT_GUIDANCE')
    def test_method_autonomy_preserves_blind_discovery(self):
        p = json.loads((ROOT / 'tool_invocation_policy.json').read_text())
        self.assertIn('ALTERNATIVE_APPROACH_CHOSEN', p['reuse_resolution']['states'])
        self.assertIn('ALTERNATIVE_IMPLEMENTATION_DOES_NOT_REQUIRE_CAPABILITY_GAP', p['invariants'])
        self.assertTrue(p['role_timing']['FREE_AXIOM_DISCOVERY_PHASE_A']['forbidden_as_question_prior'])
        m = json.loads((ROOT / 'research_priorities/research_method.json').read_text())
        self.assertTrue(m['application_contract']['may_skip_reorder_replace_methods'])
        self.assertFalse(m['free_phase_a']['method_rules_loaded'])
if __name__ == '__main__':
    unittest.main()
