"""Known FREE role layouts retain authority and staged-reading boundaries."""
import re
import unittest
from unittest import mock

from control_plane import check_current_control_authority as authority


class FreeRoleControlCompatibilityTests(unittest.TestCase):
    def setUp(self):
        self.role = authority.read("research_roles/EM_FREE_RESEARCHER_ROLE.md")
        self.reference = authority.read("research_roles/EM_FREE_PHASE_B_REFERENCE.en.md")

    def check_role(self, role=None, reference=None):
        with mock.patch.object(authority, "read", return_value=(
            self.reference if reference is None else reference
        )) as reader:
            authority.check_free_role_contract(self.role if role is None else role)
        return reader

    def test_current_v65_uses_only_the_exact_phase_b_reference(self):
        reader = self.check_role()
        reader.assert_called_once_with("research_roles/EM_FREE_PHASE_B_REFERENCE.en.md")

    def test_reviewed_v64_inline_layout_needs_no_new_reference(self):
        role = self.role.replace("CONTRACT V6.5", "CONTRACT V6.4")
        role = role.replace("[Phase-B reference](EM_FREE_PHASE_B_REFERENCE.en.md)", "inline obligations")
        obligations = self.reference.split("## Tool coverage and actual reuse\n", 1)[1]
        obligations = obligations.split("## Weighted-BRC comparison evidence", 1)[0]
        reader = self.check_role(role + "\n" + obligations)
        reader.assert_not_called()

    def test_unsupported_versions_are_not_accepted_by_a_body_decoy(self):
        for version in ("6.3", "6.6", "6.40", "6.50", "7.0", "99.0"):
            with self.subTest(version=version):
                role = self.role.replace("CONTRACT V6.5", f"CONTRACT V{version}")
                role += "\nHistorical ROLE-SPECIFIC CONTRACT V6.4 and V6.5.\n"
                with self.assertRaisesRegex(authority.ControlAuthorityError, "supported control version"):
                    self.check_role(role)

    def test_missing_malformed_inactive_and_duplicate_status_fail_closed(self):
        status = "Status: `ACTIVE / ROLE-SPECIFIC CONTRACT V6.5`"
        for replacement in (
            "", "Status: `ARCHIVED / ROLE-SPECIFIC CONTRACT V6.5`",
            "Status: ACTIVE / ROLE-SPECIFIC CONTRACT V6.5",
            "Status: `ACTIVE / ROLE-SPECIFIC CONTRACT V6.5.1`",
            status + "\n" + status,
            status + "\nStatus: `ARCHIVED / ROLE-SPECIFIC CONTRACT V6.4`",
        ):
            with self.subTest(replacement=replacement):
                with self.assertRaisesRegex(authority.ControlAuthorityError, "supported control version"):
                    self.check_role(self.role.replace(status, replacement))

    def test_version_acceptance_does_not_bypass_original_publication_and_phase_b_gates(self):
        for fragment, error in (
            ("Task publication: `research_task_publication_contract_v2.json`", "must use V2 publication"),
            ("Phase B — mandatory tool dedup and reuse resolution", "must require tool reuse resolution"),
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, self.role)
                with self.assertRaisesRegex(authority.ControlAuthorityError, error):
                    self.check_role(self.role.replace(fragment, "REMOVED"))

    def test_blindness_freeze_and_authority_boundaries_cannot_be_removed(self):
        for fragment in (
            "The shared toolbox/method inventory is hidden as a discovery prior before freeze",
            "Only a context clean before candidate generation may claim `BLINDNESS_STATUS = CLEAN`. Otherwise use `ANCHOR_EXPOSED`.",
            "Do not rewrite the frozen Phase-A candidate to force convergence.",
            "RAW_PHASE_A_CANDIDATE -> NO_TASK_PUBLICATION",
            "AUDITED_ELIGIBLE_CANDIDATE -> RESEARCHER_MAY_PUBLISH_V2_TASK",
            "TASK_PUBLICATION != WORKING_TRUTH",
            "TASK_PUBLICATION != FOUNDATION_PROMOTION",
            "WORKING_TRUTH != CANONICAL_FOUNDATION",
            "does not grant Driver authority", "QUESTION_FIRST -> TOOL_SECOND",
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, self.role)
                with self.assertRaisesRegex(authority.ControlAuthorityError, "missing control boundary"):
                    self.check_role(self.role.replace(fragment, "REMOVED"))

    def test_v65_reference_is_required_not_an_optional_fallback(self):
        role = self.role.replace("(EM_FREE_PHASE_B_REFERENCE.en.md)", "(other-reference.md)")
        with self.assertRaisesRegex(authority.ControlAuthorityError, "exact Phase-B reference"):
            self.check_role(role)
        with mock.patch.object(authority, "read", side_effect=FileNotFoundError("missing reference")):
            with self.assertRaises(FileNotFoundError):
                authority.check_free_role_contract(self.role)

    def test_phase_b_reference_cannot_drop_freeze_or_grant_new_authority(self):
        reference = " ".join(self.reference.split())
        for fragment in (
            "Status: `ACTIVE / PHASE-B REFERENCE / NO_NEW_MATHEMATICS`",
            "Open this reference after the candidate/no-go packet is frozen",
            "This reference grants no new role, task, Working Truth or Foundation authority.",
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, reference)
                with self.assertRaisesRegex(authority.ControlAuthorityError, "reference missing boundary"):
                    self.check_role(reference=reference.replace(fragment, "REMOVED"))

    def test_every_relocated_source_and_reuse_state_remains_required(self):
        for obligation in (
            "tool_invocation_policy.json", "enterprise_toolbox_registry.json",
            "research_method_inventory.json", "tools/enterprise_toolbox.py",
            "REUSE_APPLIED", "REUSE_EXECUTED", "COMPOSE_APPLIED",
            "REUSE_IDENTIFIED_EXECUTION_UNAVAILABLE", "EXTEND_EXISTING_TOOL",
            "CAPABILITY_GAP_CONFIRMED", "NOT_APPLICABLE",
        ):
            with self.subTest(obligation=obligation):
                fragment = f"`{obligation}`"
                self.assertIn(fragment, self.reference)
                with self.assertRaisesRegex(authority.ControlAuthorityError, "missing reuse obligation"):
                    self.check_role(reference=self.reference.replace(fragment, "REMOVED"))
        with self.assertRaisesRegex(authority.ControlAuthorityError, "coverage from actual use"):
            self.check_role(reference=self.reference.replace("A coverage hit is not itself tool use", "REMOVED"))

    def test_v65_lookup_cannot_expand_scope_or_erase_prior_exposure(self):
        for fragment in (
            "Once a question has independently formed and actually contains the relevant typed branch/recurrent structure",
            "do not preload a whole result/tool inventory or perform Phase-B comparison and dedup at this point",
            "A legal lookup does not certify clean prior context or erase actual tool use/exposure.",
            "Do not dump mixed raw source files, build coverage or catalog-bearing errors into Phase A.",
        ):
            with self.subTest(fragment=fragment):
                pattern = r"\s+".join(re.escape(word) for word in fragment.split())
                changed, count = re.subn(pattern, "REMOVED", self.role)
                self.assertEqual(1, count)
                with self.assertRaisesRegex(authority.ControlAuthorityError, "missing lookup boundary"):
                    self.check_role(changed)

    def test_full_current_authority_gate_uses_the_compatible_role_check(self):
        authority.check()
        original_read = authority.read
        with mock.patch.object(authority, "read", side_effect=lambda path:
                               self.role.replace("CONTRACT V6.5", "CONTRACT V6.6")
                               if path == "research_roles/EM_FREE_RESEARCHER_ROLE.md"
                               else original_read(path)):
            with self.assertRaisesRegex(authority.ControlAuthorityError, "supported control version"):
                authority.check()


if __name__ == "__main__":
    unittest.main()
