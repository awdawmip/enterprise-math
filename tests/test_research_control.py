import json
import pathlib
import unittest

from tools import research_control as rc

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = json.loads((ROOT / "research_control_state_machine.json").read_text())


def base(profile="STANDARD_RESEARCH"):
    return {
        "actor": {"role":"RESEARCHER","mode":"TASK_RESEARCH","identity_state":"REGISTERED"},
        "object": {"control_profile":profile,"task_id":"RS-X","task_lineage":"NEW_DIRECTION"},
        "runtime": {"scheduler_state":"IN_PROGRESS","dispatch_state":"LEASED"},
        "information": {"firewall":"NONE","freeze_state":"NOT_REQUIRED","source_exposure":"NORMAL"},
        "evidence": {
            "source_status":"PROVED_SOURCE","independent_status":"NOT_REQUIRED","driver_verdict":"PENDING",
            "formalization_status":"NOT_APPLICABLE","benchmark_status":"NOT_APPLICABLE","canonical_status":"NONCANONICAL"
        },
        "routing": {"working_truth":"ACTIVE","method_harvest":"PENDING","successor_gate":"NOT_APPLICABLE","route_disposition":"PENDING"},
        "parent": {"objective":"OPEN","completion_basis":"NONE","next_executable_action":"continue work"},
        "terminal_output": False
    }


class ControlStateTests(unittest.TestCase):
    def test_spec_covers_current_control_classes(self):
        self.assertEqual([], rc.validate_spec(SPEC))

    def test_scheduler_config_forbids_same_task_replication_verdict(self):
        cfg=json.loads((ROOT / "research_scheduler.json").read_text())
        self.assertNotIn("REQUEST_INDEPENDENT_REPLICATION", cfg["review_contract"]["verdicts"])
        self.assertEqual("research_control_state_machine.json", cfg["cross_layer_control"])

    def test_prime_fusion_f1_formalization(self):
        s=base("FORMALIZATION"); s["evidence"].update(source_status="REPAIRED_FROZEN",independent_status="CLOSED",driver_verdict="ACCEPTED",formalization_status="IN_PROGRESS"); s["routing"].update(method_harvest="CLASSIFIED",route_disposition="CLOSE"); s["math_change_policy"]="NO_NEW_MATHEMATICS"
        self.assertEqual([], rc.validate_snapshot(s,SPEC))

    def test_formalization_repair_required_is_rejected(self):
        s=base("FORMALIZATION"); s["evidence"]["source_status"]="REPAIR_REQUIRED"; s["evidence"]["formalization_status"]="IN_PROGRESS"; s["math_change_policy"]="NO_NEW_MATHEMATICS"
        self.assertTrue(any("frozen" in e for e in rc.validate_snapshot(s,SPEC)))

    def test_native_prime_blind_audit_closure(self):
        s=base("INDEPENDENT_AUDIT"); s["information"].update(firewall="TASK_BLIND_FORWARD",freeze_state="FROZEN",source_exposure="POST_FREEZE_ONLY"); s["evidence"].update(independent_status="CLOSED",source_status="FROZEN"); s["independence_status"]="CLEAN_INDEPENDENT_CONTEXT"; s["execution_context"]="ctx-b"; s["source_execution_context"]="ctx-a"
        self.assertEqual([], rc.validate_snapshot(s,SPEC))

    def test_blind_audit_cannot_close_before_freeze(self):
        s=base("INDEPENDENT_AUDIT"); s["information"].update(firewall="TASK_BLIND_FORWARD",freeze_state="REQUIRED_NOT_FROZEN",source_exposure="WITHHELD"); s["evidence"]["independent_status"]="CLOSED"
        self.assertTrue(any("raw freeze" in e for e in rc.validate_snapshot(s,SPEC)))

    def test_fq010_pending_blocks_canonical(self):
        s=base("FOUNDATION_DISPOSITION"); s["actor"]={"role":"FOUNDATION_STEWARD","mode":"VERIFY_OR_MAINTAIN","identity_state":"REGISTERED"}; s["evidence"]["foundation_gate"]="PENDING"; s["evidence"]["canonical_status"]="CANONICAL"; s["routing"]["working_truth"]="INACTIVE"
        self.assertTrue(any("Foundation disposition" in e for e in rc.validate_snapshot(s,SPEC)))

    def test_valley_negative_benchmark_cannot_be_l4(self):
        s=base("BENCHMARK"); s["evidence"]["benchmark_status"]="NEGATIVE"; s["result_level"]="L4"
        self.assertTrue(any("L4" in e for e in rc.validate_snapshot(s,SPEC)))

    def test_third_sector_positive_claim_requires_fair_cost(self):
        s=base("BENCHMARK"); s["evidence"]["benchmark_status"]="PARTIAL"; s["performance_claim"]="POSITIVE"; s["fair_baseline"]=False; s["cost_accounting"]="PARTIAL"
        errors=rc.validate_snapshot(s,SPEC); self.assertTrue(any("fair baseline" in e for e in errors))

    def test_prime_fusion_package_cannot_freeze_with_repair_open(self):
        s=base("INTEGRATION"); s["evidence"]["package_status"]="FROZEN"; s["evidence"]["source_status"]="REPAIR_REQUIRED"; s["evidence"]["independent_status"]="CLOSED"
        self.assertTrue(any("source repair" in e for e in rc.validate_snapshot(s,SPEC)))

    def test_cbrc_f5r_orphan_migration_profile_is_valid_nonterminal(self):
        s=base("INDEPENDENT_AUDIT"); s["runtime"]={"scheduler_state":"ORPHANED","dispatch_state":"ORPHAN_RECOVERY"}; s["information"].update(firewall="TASK_BLIND_FORWARD",freeze_state="REQUIRED_NOT_FROZEN",source_exposure="WITHHELD"); s["evidence"].update(source_status="FROZEN",independent_status="REQUIRED_OPEN"); s["routing"]["working_truth"]="ACTIVE"; s["parent"]["next_executable_action"]="MIGRATE/ADOPT with preserved blind packet and fresh context"
        self.assertEqual([], rc.validate_snapshot(s,SPEC))

    def test_independent_replication_same_task_handoff_rejected(self):
        s=base(); s["runtime"]={"scheduler_state":"HANDOFF_READY","dispatch_state":"NEEDS_DISPATCH"}; s["routing"].update(route_disposition="OPEN_INDEPENDENT_REPLICATION_CHILD",child_task_id="RS-X",child_task_ref="x@abcdef1",independence_protocol="blind")
        errors=rc.validate_snapshot(s,SPEC); self.assertGreaterEqual(len(errors),2)

    def test_accept_requires_method_harvest_and_route(self):
        s=base(); s["evidence"]["driver_verdict"]="ACCEPTED"
        errors=rc.validate_snapshot(s,SPEC); self.assertTrue(any("method-harvest" in e for e in errors)); self.assertTrue(any("route disposition" in e for e in errors))

    def test_open_parent_with_next_action_cannot_terminal_stop(self):
        s=base(); s["terminal_output"]=True
        self.assertTrue(any("active-turn" in e for e in rc.validate_snapshot(s,SPEC)))

    def test_review_event_requires_harvest_evidence_and_route(self):
        ev={"schema":rc.V2_SCHEMA,"event":"REVIEW","task_id":"RS-X","verdict":"ACCEPT","review_ref":"r@abcdef1"}
        self.assertGreaterEqual(len(rc.validate_events([ev],SPEC)),3)

    def test_same_task_replication_verdict_forbidden(self):
        ev={"schema":rc.V2_SCHEMA,"event":"REVIEW","task_id":"RS-X","verdict":"REQUEST_INDEPENDENT_REPLICATION","review_ref":"r@abcdef1","method_harvest":"NO_TOOL_PAYLOAD","evidence_class":"SOURCE_ONLY","route_disposition":"PARK"}
        self.assertTrue(any("forbidden" in e for e in rc.validate_events([ev],SPEC)))

    def test_replication_child_review_event(self):
        ev={"schema":rc.V2_SCHEMA,"event":"REVIEW","task_id":"RS-PARENT","verdict":"PARK","review_ref":"r@abcdef1","method_harvest":"RESULT_ONLY","evidence_class":"SOURCE_ONLY","route_disposition":"OPEN_INDEPENDENT_REPLICATION_CHILD","child_task_id":"RS-CHILD","child_task_ref":"research_tasks/child.md@abcdef2","independence_protocol":"CLEAN_NEW_CONTEXT_BLIND_PACKET"}
        self.assertEqual([], rc.validate_events([ev],SPEC))

    def test_approve_event_requires_content_gate_binding(self):
        bad={"schema":rc.V2_SCHEMA,"event":"APPROVE","task_id":"RS-X","taskbook_ref":"x@abcdef1","review_ref":"r@abcdef2"}
        self.assertEqual(2,len(rc.validate_events([bad],SPEC)))
        good=dict(bad,taskbook_audit="PASS",policy_digest="sha256:abc")
        self.assertEqual([],rc.validate_events([good],SPEC))


if __name__ == "__main__": unittest.main()
