from pathlib import Path
import unittest

import tools.research_execution_state as ex
import tools.research_taskbook as rt


ROOT = Path(__file__).resolve().parents[1]
F5AR = ROOT / "research_tasks" / "COHERENT_BRC_F5AR_INDEPENDENT_BRANCH_ONTOLOGY_AXIOM_ADMISSION_REPLICATION_20260825.md"


class LiveResearchExecutionControlTests(unittest.TestCase):
    def setUp(self):
        self.machine = ex.load_machine(ROOT)

    def test_f5ar_policy_stamp_is_current(self):
        meta, _ = rt.split_taskbook(F5AR.read_text(encoding="utf-8"))
        self.assertEqual(meta["policy_review"]["policy_digest"], rt.policy_digest(ROOT))
        self.assertEqual(meta["policy_review"]["review_state"], "PASS")

    def test_f5ar_composite_dispatch_audit_passes(self):
        self.assertEqual(rt.audit_taskbook(F5AR, root=ROOT, dispatch=True), [])

    def test_current_blind_tool_verification_shape_is_machine_expressible(self):
        spec = {
            "task_id": "RS-TRIAXIAL-DIRECTIONAL-DEFECT-INDEPENDENT-TOOL-VERIFICATION",
            "authority_kind": "DRIVER_DISPATCH_ENVELOPE",
            "authority_ref": "driver_handoff:TRIAXIAL_DIRECTIONAL_DEFECT_INDEPENDENT_TOOL_VERIFICATION_HANDOFF_20260825",
            "execution_gates": [
                {
                    "gate_id": "START-STAMP",
                    "phase": "PRE_MATH",
                    "must_precede": ["MATHEMATICAL_SOURCE_READ", "MATHEMATICAL_DERIVATION"],
                    "evidence": {"kind": "REMOTE_EXECUTION_STAMP_VERIFIED"},
                },
                {
                    "gate_id": "INDEPENDENT-RETURN-FROZEN",
                    "phase": "MID_EXECUTION",
                    "must_precede": ["POST_FREEZE_SOURCE_READ"],
                    "evidence": {"kind": "INDEPENDENT_RETURN_AND_CHECKER_FROZEN"},
                },
            ],
        }
        body = (
            "Before mathematics, create and remotely verify the execution stamp. "
            "Current toolbox/prior-art material remains withheld until the independent return and checker are frozen."
        )
        self.assertEqual(ex.audit_execution_spec(spec, self.machine, authority_body=body), [])

        meta = {
            "execution_state_policy": "INHERIT_GLOBAL",
            "execution_gates": spec["execution_gates"],
        }
        allowed, blockers = ex.allowed_task_action(
            meta, self.machine, "IN_PROGRESS", "MATHEMATICAL_SOURCE_READ", {"START-STAMP"}
        )
        self.assertTrue(allowed)
        self.assertEqual(blockers, [])

        allowed, blockers = ex.allowed_task_action(
            meta, self.machine, "IN_PROGRESS", "POST_FREEZE_SOURCE_READ", {"START-STAMP"}
        )
        self.assertFalse(allowed)
        self.assertEqual(blockers, ["INDEPENDENT-RETURN-FROZEN"])

        allowed, blockers = ex.allowed_task_action(
            meta,
            self.machine,
            "IN_PROGRESS",
            "POST_FREEZE_SOURCE_READ",
            {"START-STAMP", "INDEPENDENT-RETURN-FROZEN"},
        )
        self.assertTrue(allowed)
        self.assertEqual(blockers, [])


if __name__ == "__main__":
    unittest.main()
