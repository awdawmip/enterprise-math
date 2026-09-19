import copy
import json
import re
import tempfile
import unittest
from pathlib import Path

from control_plane import researcher_startup_packet as startup


SECTIONS = {
    "Mother question": "What is the exact question?",
    "Frozen inputs and scope": "Keep the frozen scope.",
    "Hard target and required outputs": "Produce one exact certificate.",
    "Research value to preserve": "Preserve the current frontier.",
    "Success, kill, and return criteria": "Return on proof or exact obstruction.",
}


class ResearcherStartupPacketTests(unittest.TestCase):
    def make_root(self, *, long_projection: bool = False) -> tuple[Path, dict]:
        temp = tempfile.TemporaryDirectory(prefix="em-startup-packet-")
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "research_task_records" / "T1").mkdir(parents=True)
        (root / "research_tasks").mkdir()
        (root / "research_returns").mkdir()
        (root / "research_returns" / "R1.md").write_text("durable frontier\n", encoding="utf-8")
        policy = {
            "researcher_cold_start_envelope": {
                "compact_packet_hard_max_bytes": 8192,
                "normal_remote_source_reads_before_math_max": 2,
            }
        }
        (root / "research_context_budget.json").write_text(
            json.dumps(policy), encoding="utf-8"
        )
        body_sections = dict(SECTIONS)
        if long_projection:
            body_sections["Frozen inputs and scope"] = "x" * 12000
        meta = {
            "task_id": "T1",
            "last_progress_ref": "branch@deadbeef / research_returns/R1.md",
            "dependencies": [
                {"target": "logical dependency", "satisfied": True}
            ],
        }
        body = "<!-- ENTERPRISE_MATH_TASK_V1\n" + json.dumps(meta) + "\n-->\n\n# T1\n\n"
        for name, value in body_sections.items():
            body += f"## {name}\n\n{value}\n\n"
        taskbook = root / "research_tasks" / "T1.md"
        taskbook.write_text(body, encoding="utf-8")
        sha1 = startup._git_blob_sha1(taskbook.read_bytes())
        publication = {
            "record_schema": "ENTERPRISE_MATH_TASK_PUBLICATION_RECORD_V2",
            "task_id": "T1",
            "publication_id": "P1",
            "taskbook_path": "research_tasks/T1.md",
            "taskbook_blob_sha1": sha1,
        }
        (root / "research_task_records" / "T1" / "P1.json").write_text(
            json.dumps(publication), encoding="utf-8"
        )
        receipt = {
            "request_id": "req-1",
            "generated_at": "2026-09-07T00:00:00Z",
            "source_sha": "abc123",
            "kind": "RESEARCH",
            "immutable_receipt_path": "control_plane/chatgpt_dispatch_receipts/req-1.json",
            "route": {
                "action": "CLAIM_NEW_OWNER",
                "new_claim_required": True,
                "owner_claim_preserved": False,
                "reason": "fixture",
                "startup_transport": {"control_epoch": "E1"},
                "target": {
                    "task_id": "T1",
                    "publication_id": "P1",
                    "title": "fixture task",
                    "identity_lane": "L1",
                    "owner": "research/t1",
                    "state": "READY",
                    "dispatch_state": "NEEDS_DISPATCH",
                    "claim_id": None,
                    "researcher_id": None,
                    "lease_until": None,
                    "frontier": "advance exact fixture",
                    "next_action": "start",
                },
            },
        }
        return root, receipt

    def test_inline_projection_is_exact_and_dependency_is_bounded(self):
        root, receipt = self.make_root()
        packet = startup.build_packet(receipt, root)
        self.assertEqual(packet["schema"], startup.SCHEMA)
        self.assertEqual(packet["task"]["projection_mode"], "INLINE_EXACT_TASKBOOK_SECTIONS")
        self.assertEqual(packet["task"]["projection"]["Mother question"], SECTIONS["Mother question"])
        self.assertNotIn("ENTERPRISE_MATH_TASK_V1", json.dumps(packet))
        self.assertEqual(
            packet["read_plan"]["first_dependency_ref"],
            "research_returns/R1.md",
        )
        self.assertLessEqual(packet["packet_bytes"], 8192)
        self.assertEqual(packet["diagnostics"]["load_policy"], "TRIGGERED_ONLY")

    def test_oversize_projection_falls_back_without_semantic_truncation(self):
        root, receipt = self.make_root(long_projection=True)
        packet = startup.build_packet(receipt, root)
        self.assertEqual(
            packet["task"]["projection_mode"],
            "EXACT_TASKBOOK_REQUIRED_PACKET_BUDGET",
        )
        self.assertIsNone(packet["task"]["projection"])
        self.assertLessEqual(packet["packet_bytes"], 8192)

    def test_no_dispatch_target_stays_minimal(self):
        root, receipt = self.make_root()
        receipt["route"]["action"] = "NO_DISPATCH"
        receipt["route"]["target"] = None
        packet = startup.build_packet(receipt, root)
        self.assertIsNone(packet["task"])
        self.assertIsNone(packet["read_plan"]["first_dependency_ref"])
        self.assertLessEqual(packet["packet_bytes"], 8192)

    def test_taskbook_digest_mismatch_fails_closed(self):
        root, receipt = self.make_root()
        publication_path = root / "research_task_records" / "T1" / "P1.json"
        publication = json.loads(publication_path.read_text(encoding="utf-8"))
        publication["taskbook_blob_sha1"] = "sha1:" + "0" * 40
        publication_path.write_text(json.dumps(publication), encoding="utf-8")
        with self.assertRaises(startup.StartupPacketError):
            startup.build_packet(receipt, root)

    def test_documented_fresh_request_matches_the_actual_bridge_envelope(self):
        repo = Path(__file__).resolve().parents[1]
        protocol = (repo / "docs/RESEARCHER_STARTUP_CONTEXT_PROTOCOL.md").read_text(encoding="utf-8")
        workflow = (repo / ".github/workflows/chatgpt-control-dispatch-bridge.yml").read_text(encoding="utf-8")
        example = re.search(r"```json\n(.*?)\n```", protocol, re.DOTALL)
        self.assertIsNotNone(example)
        request = json.loads(example.group(1))
        self.assertEqual(set(request), {"schema", "request_id", "kind"})
        schema_line = next(line for line in workflow.splitlines()
                           if "jq -r '.schema // empty'" in line)
        self.assertEqual(request["schema"], schema_line.rsplit(' = "', 1)[1].removesuffix('"'))
        id_line = next(line.strip() for line in workflow.splitlines()
                       if line.strip().startswith('if [[ ! "$request_id" =~ '))
        id_pattern = id_line.removeprefix('if [[ ! "$request_id" =~ ').removesuffix(' ]]; then')
        self.assertRegex(request["request_id"], id_pattern)
        kind_case = re.search(r'case "\$kind" in\s+([A-Z|]+)\)', workflow)
        self.assertIsNotNone(kind_case)
        self.assertIn(request["kind"], kind_case.group(1).split("|"))
        self.assertEqual(request["kind"], "RESEARCH")

    def test_typed_actions_and_claim_bindings_need_no_legacy_registry(self):
        for action, claim_needed, owner_preserved in (
            ("CLAIM_NEW_OWNER", True, False),
            ("ADOPT_OWNER_CLAIM", False, True),
            ("VERIFY_SESSION_LIVENESS", False, True),
            ("NO_DISPATCH", False, False),
        ):
            with self.subTest(action=action):
                root, receipt = self.make_root()
                self.assertFalse((root / "research_task_registry.json").exists())
                route = receipt["route"]
                route.update(action=action, new_claim_required=claim_needed,
                             owner_claim_preserved=owner_preserved)
                if owner_preserved:
                    route["target"].update(claim_id="claim-1", researcher_id="researcher-1",
                                           lease_until="2026-09-07T04:00:00Z")
                if action == "NO_DISPATCH":
                    route["target"] = None
                packet = startup.build_packet(receipt, root)
                self.assertEqual(packet["action"], action)
                self.assertEqual(packet["new_claim_required"], claim_needed)
                self.assertEqual(packet["owner_claim_preserved"], owner_preserved)
                self.assertEqual(packet["source_sha"], receipt["source_sha"])
                self.assertEqual(packet["request_id"], receipt["request_id"])
                if route["target"] is None:
                    self.assertIsNone(packet["task"])
                else:
                    for key in ("task_id", "publication_id", "identity_lane", "owner",
                                "claim_id", "researcher_id", "lease_until"):
                        self.assertEqual(packet["task"][key], route["target"][key])
                self.assertFalse((root / "research_task_registry.json").exists())
                self.assertLessEqual(packet["packet_bytes"], 8192)


    def rewrite_metadata(self, root, metadata):
        taskbook = root / "research_tasks/T1.md"
        body = "<!-- ENTERPRISE_MATH_TASK_V1\n" + json.dumps(metadata) + "\n-->\n"
        body += "\n".join(f"## {name}\n\n{value}\n" for name, value in SECTIONS.items())
        taskbook.write_text(body, encoding="utf-8")
        path = root / "research_task_records/T1/P1.json"
        publication = json.loads(path.read_text(encoding="utf-8"))
        publication["taskbook_blob_sha1"] = startup._git_blob_sha1(taskbook.read_bytes())
        path.write_text(json.dumps(publication), encoding="utf-8")

    def liveness_fixture(self, targets):
        root, receipt = self.make_root()
        receipt["route"].update(action="VERIFY_SESSION_LIVENESS", target=None,
                                new_claim_required=False, owner_claim_preserved=True,
                                targets=targets)
        return root, receipt

    def test_liveness_targets_keep_exact_owner_scope_without_bulk(self):
        target = dict(target_key="T1::C1::L1", surface="COHORT_LANE", task_id="T1",
                      execution_cohort_id="C1", execution_lane_id="L1", claim_id="claim-1",
                      owner_lease_until="2026-09-17T05:00:00Z", ignored_events="x" * 20000)
        root, receipt = self.liveness_fixture([target])
        packet = startup.build_packet(receipt, root)
        view = packet["liveness_targets"]
        self.assertEqual(view["items"], [{k: v for k, v in target.items() if k != "ignored_events"}])
        self.assertEqual((view["total"], view["omitted"], view["next_index"]), (1, 0, None))
        self.assertEqual(view["receipt_json_pointer"], "/route/targets")
        self.assertIsNone(packet["task"])
        self.assertFalse(packet["new_claim_required"])
        self.assertNotIn("ignored_events", json.dumps(packet))

    def test_liveness_prefix_is_bounded_and_omission_is_explicit(self):
        targets = [dict(target_key=f"T{i}", task_id=f"T{i}", claim_id=f"C{i}") for i in range(50)]
        root, receipt = self.liveness_fixture(targets)
        view = startup.build_packet(receipt, root)["liveness_targets"]
        self.assertEqual(view["items"], targets[:20])
        self.assertEqual((view["total"], view["omitted"], view["next_index"]), (50, 30, 20))
        self.assertEqual(view["scope"], "DIAGNOSTIC_ONLY_NO_SELECTION_OR_CLAIM")

    def test_liveness_size_trim_never_loses_the_remainder_pointer(self):
        targets = [dict(target_key=f"T{i}", task_id=f"T{i}", claim_id="x" * 1500) for i in range(25)]
        root, receipt = self.liveness_fixture(targets)
        packet = startup.build_packet(receipt, root)
        view = packet["liveness_targets"]
        shown = len(view["items"])
        self.assertTrue(0 < shown < 20)
        self.assertEqual(view["items"], targets[:shown])
        self.assertEqual(view["total"], shown + view["omitted"])
        self.assertEqual(view["next_index"], shown)
        self.assertEqual(view["receipt_path"], receipt["immutable_receipt_path"])
        self.assertEqual(packet["packet_bytes"], len(startup._serialized_packet(packet)))
        self.assertLessEqual(packet["packet_bytes"], 8192)

    def test_single_oversize_liveness_target_remains_explicit_not_no_dispatch(self):
        root, receipt = self.liveness_fixture([dict(task_id="T1", claim_id="x" * 20000)])
        packet = startup.build_packet(receipt, root)
        self.assertEqual(packet["action"], "VERIFY_SESSION_LIVENESS")
        self.assertEqual(packet["liveness_targets"]["items"], [])
        self.assertEqual(packet["liveness_targets"]["omitted"], 1)
        self.assertEqual(packet["liveness_targets"]["next_index"], 0)

    def test_cohort_scope_and_route_fields_survive_projection(self):
        root, receipt = self.make_root()
        route = receipt["route"]
        route.update(surface="COHORT_LANE", target_key="T1::C1::L1", required_guard="exact guard")
        scope = dict(execution_cohort_id="C1", execution_lane_id="L1", output_prefix="research/L1/",
                     lane_output_prefix="research/L1/")
        route["target"].update(scope)
        packet = startup.build_packet(receipt, root)
        for key in scope:
            self.assertEqual(packet["task"][key], scope[key])
        for key in ("surface", "target_key", "required_guard"):
            self.assertEqual(packet[key], route[key])

    def test_adoption_uses_live_frontier_and_preserves_guard(self):
        root, receipt = self.make_root()
        (root / "research_returns/R2.md").write_text("new frontier\n", encoding="utf-8")
        receipt["route"].update(action="ADOPT_OWNER_CLAIM", new_claim_required=False,
                                owner_claim_preserved=True, required_guard="tools/research_runtime_guard.py adopt")
        receipt["route"]["target"].update(last_progress_ref="research_returns/R2.md",
                                          last_progress_at="2026-09-17T03:00:00Z", claim_id="claim-1")
        packet = startup.build_packet(receipt, root)
        self.assertEqual(packet["read_plan"]["first_dependency_ref"], "research_returns/R2.md")
        self.assertEqual(packet["task"]["last_progress_ref"], "research_returns/R2.md")
        self.assertEqual(packet["task"]["last_progress_at"], "2026-09-17T03:00:00Z")
        self.assertEqual(packet["required_guard"], receipt["route"]["required_guard"])
        self.assertEqual(packet["task"]["claim_id"], "claim-1")
        self.assertFalse(packet["new_claim_required"])

    def test_unresolved_live_frontier_does_not_select_old_work(self):
        root, receipt = self.make_root()
        receipt["route"]["target"]["last_progress_ref"] = "RR-CURRENT-UNRESOLVED"
        packet = startup.build_packet(receipt, root)
        self.assertIsNone(packet["read_plan"]["first_dependency_ref"])
        self.assertEqual(packet["task"]["last_progress_ref"], "RR-CURRENT-UNRESOLVED")

    def test_publication_id_sentinel_does_not_mask_declared_dependency(self):
        root, receipt = self.make_root()
        self.rewrite_metadata(root, {"task_id": "T1", "dependencies": ["research_returns/R1.md"]})
        receipt["route"]["target"]["last_progress_ref"] = "P1"
        packet = startup.build_packet(receipt, root)
        self.assertEqual(packet["read_plan"]["first_dependency_ref"], "research_returns/R1.md")

    def test_string_dependencies_keep_plain_and_explicit_refs(self):
        for ref in ("research_returns/R1.md", "research_returns/R1.md@main",
                    "research_returns/R1.md@" + "a" * 40,
                    "research_returns/absent-here.md@release/v1"):
            with self.subTest(ref=ref):
                root, receipt = self.make_root()
                self.rewrite_metadata(root, {"task_id": "T1", "dependencies": [ref]})
                packet = startup.build_packet(receipt, root)
                self.assertEqual(packet["read_plan"]["first_dependency_ref"], ref)
                self.assertEqual(packet["read_plan"]["dependency_ref_verification"],
                                 "SOURCE_READ_REQUIRED_PRESERVE_DECLARED_REF")

    def test_live_immutable_github_url_is_not_rebased_to_local_file(self):
        root, receipt = self.make_root()
        ref = "https://github.com/awdawmip/enterprise-math/blob/" + "b" * 40 + "/research_returns/R1.md"
        receipt["route"]["target"]["last_progress_ref"] = ref
        packet = startup.build_packet(receipt, root)
        self.assertEqual(packet["read_plan"]["first_dependency_ref"], ref)
        self.assertEqual(packet["task"]["last_progress_ref"], ref)

    def test_malformed_pinned_refs_do_not_fall_through_to_unpinned_path(self):
        root, _ = self.make_root()
        for ref in ("research_returns/R1.md@", "research_returns/R1.md@../other",
                    "../research_returns/R1.md", "/research_returns/R1.md",
                    "https://github.com/foreign/repo/blob/main/research_returns/R1.md"):
            with self.subTest(ref=ref):
                self.assertIsNone(startup._existing_repo_path(root, [ref]))

    def test_external_taskbook_bytes_are_reported_not_called_whole_startup(self):
        root, receipt = self.make_root(long_projection=True)
        packet = startup.build_packet(receipt, root)
        size = len((root / "research_tasks/T1.md").read_bytes())
        self.assertEqual(packet["task"]["taskbook_bytes"], size)
        self.assertEqual(packet["read_plan"]["external_taskbook_bytes"], size)
        self.assertEqual(packet["read_plan"]["packet_plus_external_taskbook_bytes"],
                         packet["packet_bytes"] + size)
        self.assertEqual(packet["read_plan"]["context_accounting"],
                         "PACKET_AND_EXTERNAL_TASKBOOK_ONLY_NOT_END_TO_END")
        self.assertEqual(packet["packet_bytes"], len(startup._serialized_packet(packet)))
        self.assertLessEqual(packet["packet_bytes"], 8192)

    def test_inline_projection_does_not_double_count_taskbook(self):
        root, receipt = self.make_root()
        packet = startup.build_packet(receipt, root)
        self.assertEqual(packet["read_plan"]["external_taskbook_bytes"], 0)
        self.assertEqual(packet["read_plan"]["packet_plus_external_taskbook_bytes"], packet["packet_bytes"])
        self.assertEqual(packet["packet_bytes"], len(startup._serialized_packet(packet)))

    def test_oversize_nonprojection_metadata_still_fails_closed(self):
        root, receipt = self.make_root()
        receipt["route"]["reason"] = "x" * 20000
        with self.assertRaises(startup.StartupPacketError):
            startup.build_packet(receipt, root)

    def test_satisfied_dictionary_dependency_stays_skipped(self):
        root, receipt = self.make_root()
        self.rewrite_metadata(root, {"task_id": "T1", "dependencies": [
            {"path": "research_returns/R1.md", "satisfied": True},
            {"path": "research_returns/R1.md@fixed-ref", "satisfied": False}]})
        packet = startup.build_packet(receipt, root)
        self.assertEqual(packet["read_plan"]["first_dependency_ref"], "research_returns/R1.md@fixed-ref")


    def test_ambiguous_live_ref_keeps_original_and_requires_resolution(self):
        root, receipt = self.make_root()
        ref = "branch@deadbeef / research_returns/R1.md"
        receipt["route"]["target"]["last_progress_ref"] = ref
        packet = startup.build_packet(receipt, root)
        self.assertIsNone(packet["read_plan"]["first_dependency_ref"])
        self.assertEqual(packet["task"]["last_progress_ref"], ref)

    def test_packet_build_does_not_mutate_receipt(self):
        root, receipt = self.liveness_fixture([dict(task_id="T1", claim_id="x" * 20000)])
        before = copy.deepcopy(receipt)
        startup.build_packet(receipt, root)
        self.assertEqual(receipt, before)

    def test_ref_only_branch_token_is_not_an_exact_file_dependency(self):
        root, _ = self.make_root()
        self.assertIsNone(startup._existing_repo_path(root, ["branch@deadbeef"]))
        self.assertIsNone(startup._existing_repo_path(root, ["research_returns\\R1.md@main"]))


if __name__ == "__main__":
    unittest.main()
