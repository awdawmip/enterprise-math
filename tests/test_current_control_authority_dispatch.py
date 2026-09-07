import unittest
from datetime import datetime, timezone
from unittest import mock

import research_control_dispatch as dispatch
from control_plane import check_current_control_authority as authority
from tools import research_dispatch_core, research_runtime


NOW = datetime(2026, 9, 7, 1, 30, tzinfo=timezone.utc)


def fresh(task_id, *, kind="RESEARCH", priority="P2"):
    return {
        "task_id": task_id,
        "kind": kind,
        "state": "READY",
        "dispatch_state": "NEEDS_DISPATCH",
        "priority": priority,
        "leverage": "MEDIUM",
    }


class CurrentControlAuthorityDispatchTests(unittest.TestCase):
    def test_current_router_passes_authority_gate(self):
        authority.check()

    def test_authority_gate_rejects_bypassed_canonical_selection(self):
        original_read = authority.read
        router = original_read("research_control_dispatch.py")
        for required in (
            "states = research_dispatch.effective_states(events, now=now, root=root)",
            "policy = research_runtime_reducer.load_policy(root)",
            "fresh_task = research_runtime_reducer.select_state(states, policy, kind=kind)",
        ):
            with self.subTest(required=required):
                changed = router.replace(required, "pass  # canonical selection removed")
                self.assertNotEqual(router, changed)
                with mock.patch.object(
                    authority,
                    "read",
                    side_effect=lambda path: changed
                    if path == "research_control_dispatch.py"
                    else original_read(path),
                ):
                    with self.assertRaisesRegex(
                        authority.ControlAuthorityError, "canonical fresh selection"
                    ):
                        authority.check()

    def route(self, states, leased, observations=None):
        events = []
        with mock.patch.object(
            dispatch.research_dispatch, "effective_states", return_value=states
        ) as effective, mock.patch.object(
            dispatch, "_leased_targets", return_value=leased
        ) as owners, mock.patch.object(
            dispatch, "_fresh_lane", return_value=None
        ) as lanes, mock.patch.object(
            dispatch.research_publication_fault_isolation,
            "validated_quarantines",
            return_value={},
        ), mock.patch.object(
            dispatch.research_task_integrity_fault_isolation,
            "validated_quarantines",
            return_value={},
        ):
            result = dispatch.route_control(events, now=NOW, observations=observations)
        effective.assert_called_once_with(events, now=NOW, root=dispatch.ROOT)
        self.assertIs(states, owners.call_args.kwargs["states"])
        self.assertIs(states, lanes.call_args.kwargs["states"])
        return result

    def test_shared_snapshot_preserves_canonical_fresh_priority_and_kind(self):
        states = [
            fresh("RS-LOW"),
            fresh("GV-HIGH", kind="GOVERNANCE", priority="P0"),
            fresh("RS-HIGH", priority="P1"),
            dict(fresh("RS-OWNED", priority="P0"), dispatch_state="LEASED"),
        ]
        with mock.patch.object(
            research_dispatch_core, "effective_states", return_value=states
        ):
            expected = research_dispatch_core.select_task([], now=NOW)
        self.assertEqual("RS-HIGH", expected["task_id"])
        result = self.route(states, [])
        self.assertEqual(research_runtime.CLAIM_NEW_OWNER, result["action"])
        self.assertEqual(expected, result["target"])

    def test_stale_existing_claim_precedes_fresh_task_on_shared_snapshot(self):
        owner = {
            "task_id": "RS-RECOVER",
            "kind": "RESEARCH",
            "state": "IN_PROGRESS",
            "dispatch_state": "LEASED",
            "claim_id": "existing-winning-claim",
            "researcher_id": "EM-LIVE-TEST",
            "actor": "tester",
            "lease_until": "2026-09-07T02:00:00+00:00",
        }
        result = self.route(
            [owner, fresh("RS-FRESH", priority="P0")],
            [{"surface": dispatch.ORDINARY_TASK, "state": owner}],
            {
                owner["task_id"]: {
                    "claim_id": owner["claim_id"],
                    "activity_evidence_kind": "TASK_RESEARCH_RESPONSE",
                    "last_verified_activity_at": "2026-09-07T01:00:00+00:00",
                }
            },
        )
        self.assertEqual(research_runtime.ADOPT_OWNER_CLAIM, result["action"])
        self.assertEqual(owner["claim_id"], result["claim_id"])
        self.assertFalse(result["new_claim_required"])


if __name__ == "__main__":
    unittest.main()
