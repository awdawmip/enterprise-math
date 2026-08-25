import json
import pathlib
import tempfile
import unittest

from tools import research_scheduler as rs
from tools import research_stale_candidates as stale

ROOT = pathlib.Path(__file__).resolve().parents[1]


def task(task_id="RS-STALE-WATCH"):
    return {
        "task_id": task_id,
        "title": task_id,
        "kind": "RESEARCH",
        "owner": "research/stale-watch-test",
        "base_state": "READY",
        "priority": "P1",
        "leverage": "HIGH",
        "frontier": "watchdog regression",
        "next_action": "continue",
        "dependencies": [],
        "source_refs": [],
        "last_progress_ref": "seed",
        "last_progress_at": "2026-08-25T11:00:00+08:00",
        "hard_block": None,
    }


def ev(kind, at, **extra):
    item = {
        "schema": rs.V2_SCHEMA,
        "event": kind,
        "task_id": "RS-STALE-WATCH",
        "at": at,
    }
    item.update(extra)
    return item


class StaleCandidateTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.tempdir.name)
        (self.root / "research_tasks").mkdir()
        self.config = json.loads((ROOT / "research_scheduler.json").read_text())
        self.config["conversation_stale_minutes"] = 10
        (self.root / "research_scheduler.json").write_text(json.dumps(self.config))
        (self.root / "research_scheduler_v1_legacy.json").write_text(
            json.dumps({"schema": "ENTERPRISE_MATH_RESEARCH_SCHEDULER_V1", "tasks": []})
        )

    def tearDown(self):
        self.tempdir.cleanup()

    def base_events(self):
        payload = task()
        return [
            ev(
                "PUBLISH",
                "2026-08-25T11:00:00+08:00",
                publisher_role="RESEARCH_DRIVER",
                publisher_id="EM-DVR-111AAA",
                task=payload,
                publication_ref="research_tasks/stale-watch.md@abcdef1",
            ),
            ev(
                "REVIEW_CLAIM",
                "2026-08-25T11:00:30+08:00",
                reviewer_id="EM-DVR-222BBB",
                review_claim_id="pub-review",
            ),
            ev(
                "APPROVE",
                "2026-08-25T11:01:00+08:00",
                reviewer_id="EM-DVR-222BBB",
                review_claim_id="pub-review",
                taskbook_ref="research_tasks/stale-watch.md@abcdef1",
                review_ref="reviews/stale-watch.md@abcdef2",
            ),
            ev(
                "CLAIM",
                "2026-08-25T11:02:00+08:00",
                claim_id="claim-live",
                execution_id="EM-RX-ABC123",
                actor_role="RESEARCHER",
                lease_minutes=60,
            ),
        ]

    def candidates(self, events, at="2026-08-25T11:13:00+08:00"):
        return stale.stale_candidates(
            self.config,
            events,
            now=rs.parse_time(at),
            root=self.root,
        )

    def test_live_claim_over_threshold_is_candidate_not_auto_orphan(self):
        rows = self.candidates(self.base_events())
        self.assertEqual(1, len(rows))
        self.assertEqual("STALE_CANDIDATE", rows[0]["classification"])
        self.assertFalse(rows[0]["auto_orphan_allowed"])
        self.assertEqual("claim-live", rows[0]["last_verified_ref"])
        self.assertEqual("REBUILD_DURABLE_FRONTIER_AND_VERIFY_LIVENESS", rows[0]["required_next_action"])

    def test_durable_progress_ref_refreshes_verified_liveness(self):
        events = self.base_events() + [
            ev(
                "PROGRESS",
                "2026-08-25T11:08:00+08:00",
                claim_id="claim-live",
                execution_id="EM-RX-ABC123",
                progress_ref="research/checkpoint.md@abcdef3",
                next_action="continue",
                lease_minutes=60,
            )
        ]
        self.assertEqual([], self.candidates(events))

    def test_progress_without_durable_ref_does_not_refresh_verified_liveness(self):
        events = self.base_events() + [
            ev(
                "PROGRESS",
                "2026-08-25T11:10:00+08:00",
                claim_id="claim-live",
                execution_id="EM-RX-ABC123",
                next_action="still working",
                lease_minutes=60,
            )
        ]
        rows = self.candidates(events)
        self.assertEqual(1, len(rows))
        self.assertEqual("2026-08-25T03:02:00+00:00", rows[0]["last_verified_action_at"])

    def test_heartbeat_does_not_refresh_verified_liveness(self):
        events = self.base_events() + [
            ev(
                "HEARTBEAT",
                "2026-08-25T11:12:00+08:00",
                claim_id="claim-live",
                execution_id="EM-RX-ABC123",
                lease_minutes=60,
            )
        ]
        rows = self.candidates(events)
        self.assertEqual(1, len(rows))
        self.assertEqual("STALE_CANDIDATE", rows[0]["classification"])

    def test_under_threshold_is_not_candidate(self):
        self.assertEqual([], self.candidates(self.base_events(), at="2026-08-25T11:09:00+08:00"))


if __name__ == "__main__":
    unittest.main()
