import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools import research_lane_claims as lane_claims
from tools import research_scheduler as scheduler


def write_json(path: Path, value: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class LaneScopedClaimTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for pid in ("TP2-P1", "TP2-P2"):
            write_json(
                self.root / "research_task_records" / "RS-T" / f"{pid}.json",
                {
                    "record_schema": "ENTERPRISE_MATH_TASK_PUBLICATION_RECORD_V2",
                    "task_id": "RS-T",
                    "publication_id": pid,
                    "record_state": "ACTIVE",
                    "claimable": True,
                    "taskbook_path": f"research_tasks/{pid}.md",
                    "taskbook_blob_sha1": "sha1:" + ("1" if pid == "TP2-P1" else "2") * 40,
                },
            )
        write_json(
            self.root / "research_execution_cohorts" / "RS-T" / "EC-1.json",
            {
                "schema": "ENTERPRISE_MATH_PARALLEL_EXECUTION_COHORT_V1",
                "cohort_id": "EC-1",
                "task_id": "RS-T",
                "record_state": "ACTIVE",
                "opened_by": "EM-DVR-ABC123",
                "opened_at": "2026-08-27T00:00:00+00:00",
                "lanes": [
                    {
                        "lane_id": "route-a",
                        "publication_id": "TP2-P1",
                        "lane_role": "RESEARCH",
                        "purpose": "route A",
                        "output_prefix": "research_returns/parallel/EC-1/route-a/",
                    },
                    {
                        "lane_id": "route-b",
                        "publication_id": "TP2-P2",
                        "lane_role": "AUDIT",
                        "purpose": "route B",
                        "output_prefix": "research_returns/parallel/EC-1/route-b/",
                    },
                ],
                "two_reference_passes_required": True,
                "synthesis_required": True,
                "working_truth_granted": False,
                "canonical_promotion_granted": False,
            },
        )

    def task_definition(self, record, root):
        return {
            "task_id": "RS-T",
            "title": "test",
            "kind": "RESEARCH",
            "owner": "TEST",
            "base_state": "READY",
            "priority": "P1",
            "leverage": "HIGH",
            "frontier": "test",
            "next_action": "test",
            "dependencies": [],
            "source_refs": [],
            "evidence_status": "REGISTERED_TASK",
            "last_progress_ref": record["publication_id"],
            "last_progress_at": "2026-08-27T00:00:00+00:00",
            "hard_block": None,
            "tags": [],
            "claim_lease_minutes": 120,
            "identity_lane": "TEST",
            "publication_id": record["publication_id"],
            "taskbook_blob_sha1": record["taskbook_blob_sha1"],
            "registration_source": "IMMUTABLE_TASK_RECORD",
        }

    def auth(self, comment_id):
        return {
            "server_authenticated": True,
            "issue_number": 240,
            "comment_id": comment_id,
            "author_login": "awdawmip",
            "author_user_id": 30957095,
            "author_association": "OWNER",
            "control_authorized": True,
            "created_at": "2026-08-27T00:01:00+00:00",
            "updated_at": "2026-08-27T00:01:00+00:00",
            "body_sha256": "sha256:" + "a" * 64,
            "edited": False,
            "performed_via_github_app": "chatgpt-codex-connector",
        }

    def claim(self, lane_id, pid, claim_id, comment_id, output):
        return {
            "schema": "ENTERPRISE_MATH_SCHEDULER_EVENT_V1",
            "event": "CLAIM",
            "task_id": "RS-T",
            "actor": "descriptive-only",
            "at": "2026-08-27T00:01:00+00:00",
            "claim_id": claim_id,
            "publication_id": pid,
            "execution_cohort_id": "EC-1",
            "execution_lane_id": lane_id,
            "theorem_owner": "TEST_OWNER",
            "execution_branch": f"research/{lane_id}",
            "execution_branch_base": "b" * 40,
            "allowed_outputs": [output],
            "lease_minutes": 120,
            "_github": self.auth(comment_id),
        }

    def patch_definition(self):
        return mock.patch.object(
            lane_claims.research_dispatch,
            "registered_definition",
            side_effect=self.task_definition,
        )

    def test_two_lanes_on_same_task_win_independently(self):
        events = [
            self.claim(
                "route-a",
                "TP2-P1",
                "claim-a",
                1001,
                "research_returns/parallel/EC-1/route-a/result.md",
            ),
            self.claim(
                "route-b",
                "TP2-P2",
                "claim-b",
                1002,
                "research_returns/parallel/EC-1/route-b/result.md",
            ),
        ]
        now = scheduler.parse_time("2026-08-27T00:02:00+00:00")
        with self.patch_definition():
            a = lane_claims.reduce_lane("RS-T", "EC-1", "route-a", events, now=now, root=self.root)
            b = lane_claims.reduce_lane("RS-T", "EC-1", "route-b", events, now=now, root=self.root)
        self.assertEqual("LEASED", a["dispatch_state"])
        self.assertEqual("LEASED", b["dispatch_state"])
        self.assertEqual("claim-a", a["claim_id"])
        self.assertEqual("claim-b", b["claim_id"])

    def test_first_valid_claim_wins_within_one_lane_only(self):
        events = [
            self.claim(
                "route-a",
                "TP2-P1",
                "first",
                1001,
                "research_returns/parallel/EC-1/route-a/first.md",
            ),
            self.claim(
                "route-a",
                "TP2-P1",
                "second",
                1002,
                "research_returns/parallel/EC-1/route-a/second.md",
            ),
        ]
        with self.patch_definition():
            state = lane_claims.reduce_lane(
                "RS-T",
                "EC-1",
                "route-a",
                events,
                now=scheduler.parse_time("2026-08-27T00:02:00+00:00"),
                root=self.root,
            )
        self.assertEqual("first", state["claim_id"])
        self.assertTrue(any("not dispatchable" in row["reason"] for row in state["ignored_events"]))

    def test_lane_claim_must_use_lane_publication(self):
        event = self.claim(
            "route-a",
            "TP2-P2",
            "wrong-pub",
            1001,
            "research_returns/parallel/EC-1/route-a/result.md",
        )
        with self.patch_definition():
            state = lane_claims.reduce_lane(
                "RS-T",
                "EC-1",
                "route-a",
                [event],
                now=scheduler.parse_time("2026-08-27T00:02:00+00:00"),
                root=self.root,
            )
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])
        self.assertTrue(any("publication_id" in row["reason"] for row in state["ignored_events"]))

    def test_lane_claim_cannot_escape_output_prefix(self):
        event = self.claim(
            "route-a",
            "TP2-P1",
            "escape",
            1001,
            "research_returns/parallel/EC-1/route-b/escape.md",
        )
        with self.patch_definition():
            state = lane_claims.reduce_lane(
                "RS-T",
                "EC-1",
                "route-a",
                [event],
                now=scheduler.parse_time("2026-08-27T00:02:00+00:00"),
                root=self.root,
            )
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])
        self.assertTrue(any("output_prefix" in row["reason"] for row in state["ignored_events"]))

    def test_winning_binding_contains_exact_lane_scope(self):
        event = self.claim(
            "route-b",
            "TP2-P2",
            "claim-b",
            1002,
            "research_returns/parallel/EC-1/route-b/result.md",
        )
        with self.patch_definition():
            binding = lane_claims.winning_lane_claim_binding(
                "RS-T",
                "EC-1",
                "route-b",
                [event],
                now=scheduler.parse_time("2026-08-27T00:02:00+00:00"),
                root=self.root,
            )
        self.assertEqual("TP2-P2", binding["publication_id"])
        self.assertEqual("EC-1", binding["execution_cohort_id"])
        self.assertEqual("route-b", binding["execution_lane_id"])
        self.assertEqual("claim-b", binding["claim_id"])
        self.assertEqual("AUDIT", binding["lane_role"])
        self.assertTrue(binding["allowed_outputs"][0].startswith(binding["lane_output_prefix"]))


if __name__ == "__main__":
    unittest.main()
