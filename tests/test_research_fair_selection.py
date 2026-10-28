"""Offline scheduler fixtures. No research execution or repository writes.

The router import's whole-repository bootstrap is isolated here; the actual pure
router, reducer and continuation CAS execute over fixture states. This is not a
test of native repository publication/result authority or production deployment.
"""
import copy
import socket
import unittest
from contextlib import nullcontext
from collections import Counter
from datetime import datetime, timedelta, timezone
from unittest.mock import patch

from control_plane import research_control_bootstrap
with patch.object(research_control_bootstrap, "install"):
    import research_control_dispatch as router
from tools import research_runtime_reducer as rr
from tools import research_fair_selection as fair

BASE = datetime(2026, 10, 28, tzinfo=timezone.utc)
POLICY = rr.load_policy()


def task(name, priority="P0", **kw):
    return dict(task_id=name, priority=priority, kind="RESEARCH", base_state="READY",
                last_progress_at=BASE.isoformat(), next_action="continue", **kw)


def reduce(source, events=(), now=None):
    return rr.reduce_task(source, events, default_lease_minutes=120, now=now or BASE)


def event(name, kind, sequence, claim_id=None, **kw):
    return dict(task_id=name, event=kind, claim_id=claim_id,
                at=(BASE + timedelta(seconds=sequence)).isoformat(),
                _github={"comment_id": sequence + 1}, **kw)


def service(state, sequence, claim_id=None):
    """Extend a synthetic availability/accepted-CLAIM trace after real reducer admission."""
    name = state["task_id"]
    source = task(name, state["priority"], parent_task_id=state.get("parent_task_id"))
    claim_id = claim_id or f"c-{sequence}"
    events = [event(name, "CLAIM", sequence, claim_id),
              event(name, "HANDOFF", sequence + 1, claim_id, next_action="resume",
                    handoff_scope="CONTINUATION")]
    added = reduce(source, events, BASE + timedelta(seconds=sequence + 2))
    assert not added["ignored_events"]
    # Initial READY was already present. The appended trace uses actual reducer
    # acceptance, then continues from the same released frontier.
    state["scheduling_trace"].extend(added["scheduling_trace"][1:])
    state["last_progress_at"] = added["last_progress_at"]
    return state


class FairSelectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.socket_patch = patch.object(socket, "socket", side_effect=AssertionError("network forbidden"))
        cls.dns_patch = patch.object(socket, "getaddrinfo", side_effect=AssertionError("DNS forbidden"))
        cls.socket_patch.start()
        cls.dns_patch.start()

    @classmethod
    def tearDownClass(cls):
        cls.dns_patch.stop()
        cls.socket_patch.stop()

    def pool(self):
        return [reduce(task(f"RS-{p}", p)) for p in POLICY["selection_policy"]["priority_weights"]]

    def test_sequential_1000_successes_match_configured_shares_and_restarts(self):
        states = self.pool()
        counts = Counter()
        maximum_gap = Counter()
        previous = {}
        for step in range(1000):
            chosen = rr.select_state(copy.deepcopy(states) if step % 100 == 0 else states, POLICY)
            p = chosen["priority"]
            counts[p] += 1
            maximum_gap[p] = max(maximum_gap[p], step - previous.get(p, 0))
            previous[p] = step
            service(next(s for s in states if s["task_id"] == chosen["task_id"]), 3 * step + 1)
        self.assertEqual(dict(counts), {"P0": 400, "P1": 300, "P2": 200, "P3": 100})
        self.assertLessEqual(maximum_gap["P3"], 10)
        print("FAIR_SEQUENTIAL", dict(counts), "max_gap", dict(maximum_gap))

    def test_eight_old_snapshot_terminals_converge_without_global_lock(self):
        states = [reduce(task(f"RS-{p}-{terminal}", p)) for terminal in range(8)
                  for p in POLICY["selection_policy"]["priority_weights"]]
        counts = Counter()
        # Every terminal has a disjoint task set and the same old global snapshot.
        # All eight successful distinct-task CLAIMs must be charged, not one vote.
        for batch in range(200):
            chosen = []
            for terminal in range(8):
                pool = [s for s in states if s["task_id"].endswith(f"-{terminal}")]
                chosen.append(rr.select_state(states, POLICY, candidates=pool))
            for offset, choice in enumerate(chosen):
                counts[choice["priority"]] += 1
                state = next(s for s in states if s["task_id"] == choice["task_id"])
                service(state, 3 * (batch * 8 + offset) + 1)
        for p, weight in POLICY["selection_policy"]["priority_weights"].items():
            self.assertLessEqual(abs(counts[p] - 1600 * weight / 100), 8)
        self.assertGreater(counts["P3"], 0)
        print("FAIR_CONCURRENT_8", dict(counts), "successes", sum(counts.values()))

    def test_missing_priority_borrows_without_comeback_debt(self):
        states = self.pool()
        # P3 is unavailable through the first 100 successes.
        p3 = states[3]
        p3["scheduling_trace"][0]["eligible"] = False
        p3["dispatch_state"] = "BLOCKED"
        for step in range(100):
            chosen = rr.select_state(states, POLICY)
            self.assertNotEqual("P3", chosen["priority"])
            service(next(s for s in states if s["task_id"] == chosen["task_id"]), 3 * step + 1)
        p3["dispatch_state"] = "NEEDS_DISPATCH"
        p3["scheduling_trace"].append(dict(event="AVAILABLE", eligible=True,
            at=(BASE + timedelta(seconds=301)).isoformat(), comment_id=302, phase=2))
        first_twenty = []
        for step in range(100, 120):
            chosen = rr.select_state(states, POLICY)
            first_twenty.append(chosen["priority"])
            service(next(s for s in states if s["task_id"] == chosen["task_id"]), 3 * step + 2)
        self.assertEqual(first_twenty.count("P3"), 2)
        self.assertFalse(any(first_twenty[i:i+2] == ["P3", "P3"] for i in range(19)))

    def test_direction_parent_chain_and_waiting_not_name_similarity(self):
        states = [reduce(task("root-a", "P1")), reduce(task("root-b", "P1")),
                  reduce(task("a-next", "P1", parent_task_id="root-a")),
                  reduce(task("a-next-next", "P1", parent_task_id="a-next"))]
        # Old roots are only provenance, not runnable candidates.
        states[0]["dispatch_state"] = states[1]["dispatch_state"] = "COMPLETE"
        for state in states[:2]:
            state["scheduling_trace"][0]["eligible"] = False
        states.append(reduce(task("b-next", "P1", parent_task_id="root-b")))
        counts = Counter()
        for step in range(100):
            chosen = rr.select_state(states, POLICY)
            counts[chosen["fair_selection"]["direction"]] += 1
            service(next(s for s in states if s["task_id"] == chosen["task_id"]), 3 * step + 1)
        self.assertEqual(counts, {"root-a": 50, "root-b": 50})
        unrelated = [reduce(task("same-looking-1", "P1")), reduce(task("same-looking-2", "P1"))]
        self.assertEqual(len(set(fair.directions(unrelated).values())), 2)
        unrelated[1]["last_progress_at"] = "2020-01-01T00:00:00Z"
        self.assertEqual(rr.select_state(unrelated, POLICY)["task_id"], "same-looking-2")

    def test_duplicate_failed_renewal_and_expiry_accounting(self):
        t = task("one")
        events = [event("one", "CLAIM", 1, "c1"),
                  event("one", "CLAIM", 2, "foreign"),
                  event("one", "HEARTBEAT", 3, "c1"),
                  event("one", "PROGRESS", 4, "c1", progress_ref="exact.md"),
                  event("one", "HANDOFF", 5, "c1", next_action="resume", handoff_scope="CONTINUATION"),
                  event("one", "CLAIM", 6, "c1"),
                  event("one", "CLAIM", 7207, "c2")]
        state = reduce(t, events, BASE + timedelta(seconds=7208))
        claims = [e for e in state["scheduling_trace"] if e["event"] == "CLAIM"]
        self.assertEqual([e["claim_id"] for e in claims], ["c1", "c2"])
        self.assertEqual(state["claim_id"], "c2")
        self.assertEqual(len(state["ignored_events"]), 1)
        self.assertEqual(events[0]["claim_id"], "c1")

    def test_current_owner_cas_is_not_changed(self):
        from control_plane.research_continuation import continuation_cas_reason
        state = reduce(task("owned"), [event("owned", "CLAIM", 1, "c1")], BASE + timedelta(seconds=2))
        stale = event("owned", "CLAIM", 3, "c2", continuation={"expected_previous_claim_id": "wrong"})
        self.assertIsNotNone(continuation_cas_reason(state, stale))
        after = reduce(task("owned"), [event("owned", "CLAIM", 1, "c1"), stale], BASE + timedelta(seconds=4))
        self.assertEqual(after["claim_id"], "c1")
        self.assertEqual(len([e for e in after["scheduling_trace"] if e["event"] == "CLAIM"]), 1)

    def test_expired_successor_cas_race_has_one_winner_and_one_service(self):
        from control_plane import research_continuation as continuation
        initial = event("owned", "CLAIM", 1, "c1")
        old = reduce(task("owned"), [initial], BASE + timedelta(seconds=7300))
        expected = dict(schema=continuation.SCHEMA, mode="RESUME",
            expected_previous_claim_id="c1", expected_previous_comment_id=2,
            previous_researcher_id=old["last_researcher_id"], session_id="new-session", frontier={})
        one = event("owned", "CLAIM", 7301, "c2", continuation=expected,
                    researcher_id="EM-NEW-123456", session_id="new-session")
        one["_github"].update(server_authenticated=True, control_authorized=True, edited=False)
        two = copy.deepcopy(one)
        two.update(claim_id="c3", at=(BASE + timedelta(seconds=7302)).isoformat())
        two["_github"]["comment_id"] = 7303
        result = reduce(task("owned"), [initial, one, two], BASE + timedelta(seconds=7303))
        self.assertEqual(result["claim_id"], "c2")
        self.assertIn("CAS changed", result["ignored_events"][0]["reason"])
        self.assertEqual([e["claim_id"] for e in result["scheduling_trace"] if e["event"] == "CLAIM"], ["c1", "c2"])

    def test_untrusted_event_never_reaches_service_accounting(self):
        source = {**task("registered"), "registration_source": "IMMUTABLE_TASK_RECORD"}
        forged = event("registered", "CLAIM", 1, "forged")
        accepted, rejected = router.research_dispatch._event_authentication_filter(source, [forged])
        self.assertEqual(accepted, [])
        self.assertTrue(rejected)
        result = reduce(source, accepted)
        self.assertFalse(any(e["event"] == "CLAIM" for e in result["scheduling_trace"]))

    def test_recovery_and_fresh_compete_active_owner_does_not(self):
        owned = reduce(task("owned", "P3"), [event("owned", "CLAIM", 1, "owner")], BASE + timedelta(seconds=2))
        owned["lease_until"] = (BASE + timedelta(hours=2)).isoformat()
        fresh = reduce(task("new", "P0"))
        target = dict(surface=router.ORDINARY_TASK, state=owned)
        observation = {"owned": dict(claim_id="owner", activity_evidence_kind="TASK_RESEARCH_RESPONSE",
                                     last_verified_activity_at=BASE.isoformat())}
        before = copy.deepcopy(owned)
        chosen = router.route_from_candidates([target], observations=observation,
            now=BASE + timedelta(minutes=20), fresh_task=fresh, fresh_lane=None,
            policy=POLICY, states=[owned, fresh])
        self.assertEqual(chosen["target_key"], "new")
        self.assertEqual(owned, before)
        active = router.route_from_candidates([target], observations=observation,
            now=BASE + timedelta(minutes=1), fresh_task=None, fresh_lane=None,
            policy=POLICY, states=[owned])
        self.assertEqual(active["action"], "NO_DISPATCH")

    def test_metadata_fallback_and_policy_validation(self):
        state = dict(task_id="old", priority="P2", kind="RESEARCH", dispatch_state="NEEDS_DISPATCH")
        result = rr.select_state([state], POLICY)
        self.assertEqual(result["fair_selection"]["missing_history_tasks"], 1)
        self.assertNotIn("scheduling_trace", result)
        for weights in ({}, {"P0": 40}, {"P0": 40, "P1": 30, "P2": 20, "P3": 0}):
            policy = copy.deepcopy(POLICY)
            policy["selection_policy"]["priority_weights"] = weights
            self.assertTrue(rr.validate_policy(policy))

    def test_direction_metadata_is_projection_only_not_immutable_definition(self):
        from tools import research_dispatch_core as core
        record = dict(task_id="child", parent_task_id="parent", published_at=BASE.isoformat())
        meta = task("child", parent_task_id="parent")
        with patch.object(core, "_parse_taskbook", return_value=meta):
            definition = router.research_dispatch._ORIGINAL_REGISTERED_DEFINITION(record)
        self.assertNotIn("parent_task_id", definition)
        raw_state = {"task_id": "child"}
        with patch.object(core, "_dispatch_result_read_snapshot", side_effect=lambda root: nullcontext()), \
             patch.object(core, "merged_definitions", return_value=[definition]), \
             patch.object(core, "reduce_definition", return_value=raw_state), \
             patch.object(core.research_task_records, "current_records", return_value={"child": record}):
            states = core.effective_states([], now=BASE)
        self.assertEqual(states[0]["parent_task_id"], "parent")
        self.assertNotIn("parent_task_id", definition)


if __name__ == "__main__":
    unittest.main()
