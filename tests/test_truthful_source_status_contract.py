"""Document/machine reporting contract checks; not proof of any client's I/O."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class TruthfulSourceStatusContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.policy = json.loads((ROOT / 'final_response_identity_policy.json').read_text())
        cls.identity = json.loads((ROOT / 'research_identity_state_machine.json').read_text())
        cls.status = cls.policy['source_status_reporting']
        cls.doc = (ROOT / 'docs/RESEARCH_IDENTITY_PROTOCOL.md').read_text()
        cls.portable = (ROOT / 'docs/PORTABLE_RESEARCH_PROTOCOL.md').read_text()


    def test_footer_display_is_english_without_new_read_exemption(self):
        self.assertEqual(self.status['display_language'], 'en')
        self.assertIn('brief warning reasons in English', self.status['display_language_rule'])
        self.assertEqual(self.status['read_states'], {
            'READ_OK': 'Verified', 'READ_LEASED': 'Verified snapshot reused',
            'READ_FAILED': '⚠ Read failed', 'READ_UNKNOWN': '⚠ Unconfirmed'})
        self.assertEqual(self.status['write_states'], {
            'WRITE_OK': 'Written and verified', 'WRITE_NOT_REQUIRED': 'Not required',
            'WRITE_NOT_DONE': '⚠ Not written', 'WRITE_FAILED': '⚠ Write failed',
            'WRITE_PENDING': '⚠ Unconfirmed', 'WRITE_UNKNOWN': '⚠ Unconfirmed'})
        self.assertIn('⚠ Identity unconfirmed', self.status['unresolved_identity'])
        self.assertIn('Read=', self.status['template'])
        self.assertIn('Write=', self.status['template'])
        self.assertIn('brief warning reasons must be English', self.doc)
        self.assertIn('Write=Not required', self.portable)

    def test_both_active_contracts_require_visible_status(self):
        self.assertTrue(self.policy['ordering']['marker_required'])
        self.assertTrue(self.identity['final_response']['marker_required'])
        self.assertTrue(self.status['required'])
        self.assertIn('MANDATORY_TRUTHFUL', self.policy['core_invariant'])

    def test_current_read_and_valid_lease_are_not_a_remembered_sha(self):
        self.assertEqual(set(self.status['read_states']), {'READ_OK', 'READ_LEASED', 'READ_FAILED', 'READ_UNKNOWN'})
        self.assertIn('actual successful required-source read', self.status['read_success_requires'])
        self.assertIn('actual verification time and ref retained', self.status['read_lease_requires'])
        self.assertIn('still-valid applicable source freshness policy', self.status['read_lease_requires'])
        self.assertIn('refresh when current state matters', self.status['read_lease_requires'])

    def test_success_requires_actual_publication_and_completion_evidence(self):
        required = ' '.join(self.status['write_success_requires'])
        self.assertIn('all required destinations published', required)
        self.assertIn('actual successful remote readback or authoritative completion receipt', required)
        self.assertIn('exact operation/artifact', required)
        self.assertEqual(self.status['write_states']['WRITE_OK'], 'Written and verified')

    def test_every_incomplete_state_is_visibly_warned(self):
        for state in ('WRITE_NOT_DONE', 'WRITE_FAILED', 'WRITE_PENDING', 'WRITE_UNKNOWN'):
            with self.subTest(state=state):
                self.assertTrue(self.status['write_states'][state].startswith('⚠'))
        for state in ('READ_FAILED', 'READ_UNKNOWN'):
            self.assertTrue(self.status['read_states'][state].startswith('⚠'))
        self.assertIn('brief specific reason and affected destination', self.status['incomplete_write_requires'])

    def test_unknown_operation_requires_reconciliation_not_duplicate(self):
        self.assertIn('preserve uncertain operation identity and reconcile before any retry', self.status['incomplete_write_requires'])

    def test_no_write_task_does_not_create_artificial_write_or_hide_failure(self):
        self.assertTrue(self.status['no_synthetic_write'])
        self.assertIn('failed, denied, pending or unattempted required write is not N/A', self.status['write_not_required_requires'])
        self.assertEqual(self.status['write_states']['WRITE_NOT_REQUIRED'], 'Not required')

    def test_read_and_multiple_write_targets_remain_independent(self):
        self.assertIn('read and write independently', self.status['per_target_rule'])
        self.assertIn('one successful write never hides another incomplete write', self.status['per_target_rule'])

    def test_control_mode_does_not_fabricate_research_identity(self):
        c = self.policy['control_plane_finalization']
        self.assertFalse(c['research_role_footer_required'])
        self.assertTrue(c['source_status_footer_required'])
        self.assertFalse(c['research_runtime_identity_gate_applies_merely_because_control_mode_is_active'])
        self.assertIn('without inventing a research-role identity', c['rule'])
        self.assertFalse(self.policy['pre_final_permission_gate']['caller_supplied_registration_is_authority'])
        self.assertFalse(self.policy['pre_final_permission_gate']['caller_supplied_parent_status_is_authority'])

    def test_no_optional_conflict_in_touched_entry_contracts(self):
        for text in (self.doc, self.portable):
            for old in ('Optional visible identity marker', 'requires no identity footer', '可选身份尾标'):
                self.assertNotIn(old, text)
        self.assertIn('## 8. Mandatory truthful identity and source-status footer', self.doc)
        self.assertIn('EM-Source-Status', self.portable)

    def test_no_claim_of_platform_wide_enforcement_or_new_authority(self):
        self.assertIn('not platform-wide prompt injection', self.status['coverage_boundary'])
        self.assertIn('bypass denied STOP', self.status['authority_boundary'])
        self.assertIn('without per-step hashing', self.status['authority_boundary'])


if __name__ == '__main__':
    unittest.main()
