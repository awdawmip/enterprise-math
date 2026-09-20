"""Source-unit regression for ordinary priority constraints, without remote I/O.

Execute actual router/selector function ASTs, not rewritten implementations.
Mock the repository/event inputs and runtime-liveness leaf only. These tests
are not live dispatch, full repository integration or CLAIM verification.
Run: python -m unittest discover -s tests -p test_priority_scoped_dispatch.py -v
"""
from __future__ import annotations

import argparse
import ast
import copy
import io
import json
from contextlib import redirect_stdout, redirect_stderr
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Iterable, Mapping
import sys
import unittest
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
POLICY = {"selection_policy": {
    "state_order": ["HANDOFF_READY", "READY"],
    "priority_order": ["P0", "P1", "P2", "P3"],
    "leverage_order": ["FOUNDATION", "VERY_HIGH", "HIGH", "MEDIUM", "LOW"],
}}
NOW = datetime(2026, 9, 20, tzinfo=timezone.utc)


def load_functions(path, names, namespace):
    parsed = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    nodes = [n for n in parsed.body if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name in names]
    if {n.name for n in nodes} != set(names):
        raise AssertionError(f"missing source functions: {set(names) - {n.name for n in nodes}}")
    future = ast.ImportFrom(module="__future__", names=[ast.alias(name="annotations")], level=0)
    unit = ast.fix_missing_locations(ast.Module(body=[future, *nodes], type_ignores=[]))
    exec(compile(unit, str(path), "exec"), namespace)


def task(name, priority="P0", kind="RESEARCH", state="READY", dispatch_state="NEEDS_DISPATCH", **extras):
    return dict(task_id=name, priority=priority, kind=kind, state=state,
                dispatch_state=dispatch_state, leverage="HIGH", **extras)


class PriorityScopeTests(unittest.TestCase):
    def setUp(self):
        selector_ns = dict(datetime=datetime, timezone=timezone)
        load_functions(ROOT / "tools/research_runtime_reducer.py", {"parse_time", "select_state"}, selector_ns)
        self.states = []
        self.lanes = {}
        self.runtime = SimpleNamespace(
            ADOPT_OWNER_CLAIM="ADOPT_OWNER_CLAIM", CLAIM_NEW_OWNER="CLAIM_NEW_OWNER",
            KEEP_CURRENT_SESSION="KEEP_CURRENT_SESSION", NO_DISPATCH="NO_DISPATCH",
            parse_time=selector_ns["parse_time"],
            dispatch_decision=Mock(side_effect=lambda state, **kw: {
                "action": state.get("fixture_action", "VERIFY_SESSION_LIVENESS")}),
        )
        self.dispatch = SimpleNamespace(
            effective_states=Mock(side_effect=lambda *a, **kw: self.states),
            load_events=Mock(return_value=[]),
        )
        self.lane = SimpleNamespace(
            lane_states=Mock(side_effect=lambda key, *a, **kw: self.lanes.get(key, [])),
            select_lane=Mock(side_effect=lambda key, *a, **kw: next(
                (s for s in self.lanes.get(key, []) if s["dispatch_state"] == "NEEDS_DISPATCH"), None)),
        )
        self.ns = dict(
            ROOT=ROOT, Mapping=Mapping, Any=Any, Path=Path, argparse=argparse,
            json=json, datetime=datetime, timezone=timezone,
            ORDINARY_TASK="ORDINARY_TASK", COHORT_LANE="COHORT_LANE",
            SESSION_ACTIVITY_KINDS={"TASK_RESEARCH_RESPONSE", "DURABLE_EXECUTION_PROGRESS"},
            SESSION_OBSERVATION_SCHEMA="ENTERPRISE_MATH_SESSION_LIVENESS_OBSERVATIONS_V2",
            research_dispatch=self.dispatch, research_lane_dispatch=self.lane,
            research_runtime=self.runtime,
            research_runtime_reducer=SimpleNamespace(
                load_policy=Mock(return_value=POLICY), select_state=selector_ns["select_state"]),
            research_startup_transport=SimpleNamespace(attach=lambda value: value),
            research_publication_fault_isolation=SimpleNamespace(validated_quarantines=lambda root: []),
            research_task_integrity_fault_isolation=SimpleNamespace(validated_quarantines=lambda root: []),
            research_activity=SimpleNamespace(overview=lambda *a, **kw: {"items": [], "has_more": False}),
            _assigned_driver_route=Mock(return_value={"assigned": "driver"}),
            _assigned_research_route=Mock(return_value={"assigned": "research"}),
        )
        load_functions(ROOT / "research_control_dispatch.py", {
            "ControlDispatchError", "_target_key", "_state_target_key", "_owner_scope_activity",
            "_leased_targets", "_fresh_lane", "_adoption_result", "route_from_candidates",
            "route_control", "main", "_load_observation_payload", "parse_session_observations",
        }, self.ns)

    def route(self, **kw):
        return self.ns["route_control"]([], now=NOW, **kw)

    def test_p0_ready_is_not_displaced_by_p2_handoff(self):
        self.states = [task("P2-old", "P2", state="HANDOFF_READY"), task("P0-new")]
        self.assertEqual(self.route()["target_key"], "P2-old")
        result = self.route(priority="P0")
        self.assertEqual(result["target_key"], "P0-new")
        self.assertEqual(result["selection_filter"], {"kind": "RESEARCH", "priority": "P0"})

    def test_foreign_priority_recovery_is_outside_scope(self):
        self.states = [task("P2-stale", "P2", dispatch_state="LEASED", claim_id="old",
                            fixture_action="ADOPT_OWNER_CLAIM"), task("P0-ready")]
        self.assertEqual(self.route()["action"], "ADOPT_OWNER_CLAIM")
        result = self.route(priority="P0")
        self.assertEqual(result["target_key"], "P0-ready")
        self.assertEqual(result["action"], "CLAIM_NEW_OWNER")

    def test_same_priority_stale_recovery_preserves_claim(self):
        self.states = [task("P0-stale", dispatch_state="LEASED", claim_id="winning-claim",
                            researcher_id="existing-owner", fixture_action="ADOPT_OWNER_CLAIM"), task("P0-new")]
        result = self.route(priority="P0")
        self.assertEqual(result["claim_id"], "winning-claim")
        self.assertTrue(result["owner_claim_preserved"])
        self.assertFalse(result["new_claim_required"])

    def test_unknown_p0_owner_is_not_no_dispatch(self):
        self.states = [task("P0-owned", dispatch_state="LEASED", claim_id="owner"), task("P2-new", "P2")]
        self.assertEqual(self.route(priority="P0")["action"], "VERIFY_SESSION_LIVENESS")

    def test_empty_scope_never_falls_back_to_p2(self):
        self.states = [task("P2-ready", "P2")]
        result = self.route(priority="P0")
        self.assertEqual(result["action"], "NO_DISPATCH")
        self.assertNotIn("target", result)
        self.assertIn("RESEARCH/P0", result["reason"])

    def test_blocked_reviewed_and_terminal_p0_are_not_claimed(self):
        for status in ("BLOCKED", "AWAITING_REVIEW", "COMPLETE", "DORMANT"):
            with self.subTest(status=status):
                self.states = [task("unavailable", dispatch_state=status), task("P2-new", "P2")]
                self.assertEqual(self.route(priority="P0")["action"], "NO_DISPATCH")

    def test_kind_and_priority_intersect(self):
        self.states = [task("gov", kind="GOVERNANCE")]
        self.assertEqual(self.route(priority="P0")["action"], "NO_DISPATCH")
        self.assertEqual(self.route(priority="P0", kind="ANY")["target_key"], "gov")
        self.assertEqual(self.route(priority="P0", kind="GOVERNANCE")["target_key"], "gov")

    def test_p0_cohort_lane_remains_scoped_to_parent(self):
        self.states = [task("p0cohort", dispatch_state="COHORT_ACTIVE"),
                       task("p2cohort", "P2", dispatch_state="COHORT_ACTIVE")]
        self.lanes = {
            "p0cohort": [task("p0cohort", execution_cohort_id="c0", execution_lane_id="l0")],
            "p2cohort": [task("p2cohort", "P2", execution_cohort_id="c2", execution_lane_id="l2")],
        }
        result = self.route(priority="P0")
        self.assertEqual(result["target_key"], "p0cohort::c0::l0")
        self.assertEqual(result["surface"], "COHORT_LANE")
        self.assertEqual(self.lane.select_lane.call_args.args[0], "p0cohort")

    def test_filter_does_not_mutate_states_or_claims(self):
        self.states = [task("p0"), task("p2", "P2", claim_id="keep")]
        before = copy.deepcopy(self.states)
        self.route(priority="P0")
        self.assertEqual(self.states, before)
        self.dispatch.effective_states.assert_called_once()

    def test_invalid_priority_is_fail_closed_before_reduction(self):
        for priority in ("", "p0", "P4", " P0", False, 0, [], {}, "ANY"):
            with self.subTest(priority=priority):
                with self.assertRaises(self.ns["ControlDispatchError"]):
                    self.route(priority=priority)
        self.dispatch.effective_states.assert_not_called()

    def test_priority_cannot_mix_with_exact_assignment(self):
        for field in ("assigned_driver_task", "assigned_research_task"):
            with self.subTest(field=field):
                with self.assertRaises(self.ns["ControlDispatchError"]):
                    self.route(priority="P0", **{field: {}})
        self.ns["_assigned_driver_route"].assert_not_called()
        self.ns["_assigned_research_route"].assert_not_called()

    def test_existing_assignment_entries_remain_unchanged(self):
        self.assertEqual(self.route(assigned_driver_task={}), {"assigned": "driver"})
        self.assertEqual(self.route(assigned_research_task={}), {"assigned": "research"})
        self.dispatch.effective_states.assert_not_called()

    def test_unfiltered_output_has_no_new_scope_fields(self):
        self.states = [task("any")]
        result = self.route()
        self.assertNotIn("selection_filter", result)
        self.assertEqual(result["reason"], "fresh canonical task selector returned a dispatchable target")

    def test_cli_passes_priority_to_canonical_route(self):
        route = Mock(return_value={"action": "NO_DISPATCH"})
        self.ns["route_control"] = route
        with patch.object(sys, "argv", ["router", "--events", "server.json", "--kind", "ANY", "--priority", "P0"]), redirect_stdout(io.StringIO()):
            self.assertEqual(self.ns["main"](), 2)
        self.assertEqual(route.call_args.kwargs["priority"], "P0")
        self.assertEqual(route.call_args.kwargs["kind"], "ANY")

    def test_cli_requires_event_snapshot_for_priority(self):
        with patch.object(sys, "argv", ["router", "--priority", "P0"]):
            with self.assertRaises(self.ns["ControlDispatchError"]):
                self.ns["main"]()
        self.dispatch.load_events.assert_not_called()

    def test_cli_rejects_unknown_priority(self):
        with patch.object(sys, "argv", ["router", "--priority", "P4"]), redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as caught:
                self.ns["main"]()
        self.assertEqual(caught.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
