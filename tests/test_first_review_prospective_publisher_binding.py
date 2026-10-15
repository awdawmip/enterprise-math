"""Exercise the real first-review writer without bootstrapping a research store.

Only the command and native receipt-construction functions are AST-loaded from
the selected Source tree. Authority, record validation, storage and follow-up
are explicit isolated boundaries. No fixture identity is live authority, and
these tests do not validate Taskbook mathematics or execute scientific code.

RR133_FIRST_REVIEW_SOURCE_ROOT optionally selects another exact Source tree for
the same assertions, so the baseline and candidate can be compared unchanged.
"""
from __future__ import annotations

import argparse
import ast
import contextlib
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest import mock


SOURCE_ROOT = Path(os.environ.get(
    "RR133_FIRST_REVIEW_SOURCE_ROOT", str(Path(__file__).resolve().parents[1])
))
FIELD = "prospective_result_authority_binding"
EXACT_REQUEST = {
    "schema": "ENTERPRISE_MATH_RR133_PROSPECTIVE_BINDING_REQUEST_V2",
    "historical_result_id": "RR-1337737608BDE3D7E620",
    "historical_packet_id": "DFU-1337737608BDE3D7E622",
    "historical_source_publication_id": "TP2-5D9C21A7B40E683F1C52",
    "supersedes_publication_id": "TP2-3F7A91C4E82D105B6A38",
}
DRIVER = "EM-DVR-PUB001"
SESSION = "MCP-first-review-isolated-fixture"
STAMP = "2026-10-15T03:00:00+00:00"
SOURCE_COMMIT = "1" * 40


def _load_functions(path, names, namespace):
    """Compile actual function bodies; never execute a module's imports/startup."""
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    selected = [node for node in tree.body
                if isinstance(node, ast.FunctionDef) and node.name in names]
    if {node.name for node in selected} != set(names):
        raise AssertionError(f"required Source functions missing from {path}")
    module = ast.Module(body=[
        ast.ImportFrom(module="__future__", names=[ast.alias(name="annotations")], level=0),
        *selected,
    ], type_ignores=[])
    ast.fix_missing_locations(module)
    exec(compile(module, str(path), "exec"), namespace)
    return namespace


class FixtureResultError(ValueError):
    pass


class FixtureContinuationError(ValueError):
    pass


class FixtureDriverError(ValueError):
    pass


class FixtureCandidateError(ValueError):
    pass


class FixtureTransactionError(ValueError):
    pass


class FixtureFollowupError(ValueError):
    pass


class ReachedCurrentSourceAfterPublisherGuard(Exception):
    """Stop before Task preparation, after the actual prospective publisher guard."""


class ReviewWriterHarness:
    def __init__(self, *, prospective=True, current_authority=True,
                 session=SESSION, existing=False, supplied_spec=True):
        # This path is never created. The storage stub records intended bytes.
        self.root = SOURCE_ROOT / "isolated-first-review-fixture-not-written"
        self.events = []
        self.committed = []
        self.real_boundary = None
        self.extra_modules = {}
        self.result = {
            "result_id": "RR-FIRSTREVIEW-FIXTURE",
            "task_id": "RS-N-COUPLED-PUBLIC-N-DISTRIBUTIONAL-NONEXTERNALIZABILITY",
            "publication_id": "TP2-FIRSTREVIEW-FIXTURE",
        }
        self.authority = {
            "authority_record_id": "DA-FIRSTREVIEW-FIXTURE",
            "source_comment_id": 123,
            "source_body": json.dumps({"driver_id": DRIVER, "session_id": SESSION}),
        }
        self.args = argparse.Namespace(
            result_id=self.result["result_id"], driver_id=DRIVER,
            disposition="ACCEPTED", review_path="driver_reviews/first-review-fixture.md",
            destination_class="FOLLOWUP_TASK", destination_ref_or_none="",
            reviewed_at=STAMP, reviewer_session_id=session,
            reviewer_contribution_ids_json="[]", source_commit=SOURCE_COMMIT,
            followup_spec="first-review-fixture.json" if supplied_spec else None,
            followup_created_at=STAMP,
        )
        # Taskbook/body validation is deliberately outside this call-boundary test.
        self.spec = {
            "decision": "TASK_SET_PUBLISHED", "gate_decisions": [],
            "tasks": [{
                "task_id": "RS-N-COUPLED-PUBLIC-EFFECTIVE-RESOURCE-COVERAGE-OR-ESCAPE-CLASSIFICATION",
                "task_role": "MATHEMATICAL_CONTINUATION",
            }],
        }
        if prospective:
            self.spec[FIELD] = copy.deepcopy(EXACT_REQUEST)

        self.continuation = types.ModuleType("control_plane.research_continuation")
        self.continuation.ContinuationError = FixtureContinuationError
        self.continuation.require_review_authority = mock.Mock(
            return_value=copy.deepcopy(self.authority) if current_authority else None)
        self.continuation.verify_source_snapshot = mock.Mock(return_value=SOURCE_COMMIT)
        self.control_plane = types.ModuleType("control_plane")
        self.control_plane.__path__ = []
        self.control_plane.research_continuation = self.continuation

        receipt_path = SOURCE_ROOT / "control_plane/research_continuation_write_authority.py"
        receipt_tree = ast.parse(receipt_path.read_text(encoding="utf-8"))
        schema = next(ast.literal_eval(node.value) for node in receipt_tree.body
                      if isinstance(node, ast.Assign)
                      and any(isinstance(target, ast.Name) and target.id == "SCHEMA"
                              for target in node.targets))
        receipt_namespace = _load_functions(
            receipt_path, {"payload_digest", "build_receipt"},
            {"json": json, "hashlib": hashlib, "copy": copy, "SCHEMA": schema},
        )
        self.payload_digest = receipt_namespace["payload_digest"]
        self.build_receipt = mock.Mock(side_effect=receipt_namespace["build_receipt"])
        self.preflight = mock.Mock()
        self.materialize = mock.Mock(side_effect=self._materialize)
        self.review_state = mock.Mock(return_value={
            "review_state": "AWAITING_REVIEW_INTAKE",
            "review_ids": ["DR-EXISTING-FIXTURE", "DR-FIRSTREVIEW-FIXTURE"],
        })
        self.commit = mock.Mock(side_effect=self._commit)
        self.review_candidate = mock.Mock()
        self.record_factory = mock.Mock(side_effect=self._review_record)
        namespace = {
            "argparse": argparse, "Path": Path, "json": json,
            "ROOT": self.root, "REVIEW_ROOT": self.root / "research_result_reviews",
            "ResultRecordError": FixtureResultError,
            "_install_canonical_write_view": mock.Mock(),
            "result_map": mock.Mock(return_value={self.result["result_id"]: self.result}),
            "iter_reviews": mock.Mock(return_value=[{
                "result_id": self.result["result_id"], "review_id": "DR-EXISTING-FIXTURE",
            }] if existing else []),
            "_load_followup_spec": mock.Mock(return_value=(
                self.spec, self.root / "first-review-fixture.json")),
            "_now": lambda value: value or STAMP,
            "_safe_id": lambda value, label: value,
            "review_result": self.record_factory,
            "_preflight_first_review_followup": self.preflight,
            "_canonical_transaction_audit": mock.Mock(return_value=[]),
            "_driver_authority": types.SimpleNamespace(
                DriverAuthorityError=FixtureDriverError,
                require_active_driver=mock.Mock(return_value=copy.deepcopy(self.authority)),
                review_authority_errors=mock.Mock(return_value=[]),
                valid_records=mock.Mock(return_value=[copy.deepcopy(self.authority)])),
            "_write_authority": types.SimpleNamespace(
                build_receipt=self.build_receipt, receipt_error=mock.Mock(return_value=None)),
            "_candidate_validation": types.SimpleNamespace(
                ImmutableCandidateValidationError=FixtureCandidateError,
                require_valid_review_candidate=self.review_candidate),
            "_write_tx": types.SimpleNamespace(
                ImmutableWriteTransactionError=FixtureTransactionError,
                PlannedFile=lambda path, content: types.SimpleNamespace(path=path, content=content),
                json_bytes=lambda record: (json.dumps(record, sort_keys=True) + "\n").encode(),
                commit=self.commit),
            "_driver_followup": types.SimpleNamespace(materialize=self.materialize),
            "_review_evidence": types.SimpleNamespace(state=self.review_state),
        }
        self.namespace = _load_functions(
            SOURCE_ROOT / "tools/research_result_records.py",
            {"command_review_with_authority"}, namespace,
        )
        self.output = io.StringIO()

    def _review_record(self, **kwargs):
        record = {
            "record_schema": "ENTERPRISE_MATH_RESEARCH_RESULT_REVIEW_V1",
            "review_id": "DR-FIRSTREVIEW-FIXTURE",
            **{key: value for key, value in self.result.items() if not key.startswith("_")},
            "driver_id": kwargs["driver_id"], "disposition": kwargs["disposition"],
            "reviewed_at": kwargs["reviewed_at"], "review_path": str(kwargs["review_path"]),
            "destination_class": kwargs["destination_class"],
            "destination_ref_or_none": kwargs["destination_ref_or_none"], "terminal": True,
        }
        if self.real_boundary is not None:
            record["result_record_path"] = self.result["_record_path"]
            record["result_record_sha256"] = self.real_boundary.file_digest(self.result["_record_path"])
        return record

    def _commit(self, planned, *, postcheck):
        self.events.append("commit")
        self.committed.extend((item.path, bytes(item.content)) for item in planned)
        if self.real_boundary is not None:
            for item in planned:
                item.path.parent.mkdir(parents=True, exist_ok=True)
                item.path.write_bytes(item.content)
        errors = postcheck()
        if errors:
            raise FixtureTransactionError(str(errors))

    def _materialize(self, **kwargs):
        self.events.append("materialize")
        if self.real_boundary is not None:
            return self.real_boundary.materialize(**kwargs)
        return {"packet_id": "DFU-FIRSTREVIEW-FIXTURE", "review_id": kwargs["review_id"]}

    def run(self):
        # Imports made inside the real command resolve only to these boundaries.
        with mock.patch.dict(sys.modules, {
            "control_plane": self.control_plane,
            "control_plane.research_continuation": self.continuation,
            **self.extra_modules,
        }), contextlib.redirect_stdout(self.output):
            return self.namespace["command_review_with_authority"](self.args)


class RealPublisherBoundary:
    """Actual Source call chain; only catalogue/authority lookups are fixtures."""

    def __init__(self, harness, root):
        self.harness = harness
        self.root = root
        self.observed_binding = None
        harness.real_boundary = self
        harness.root = root
        harness.namespace.update(ROOT=root, REVIEW_ROOT=root / "research_result_reviews")
        harness.namespace["_load_followup_spec"].return_value = (harness.spec, root / "spec.json")
        result_path = f"research_result_records/{harness.result['task_id']}/{harness.result['result_id']}.json"
        self.write_json(result_path, harness.result)
        harness.result["_record_path"] = result_path
        authority_path = "research_driver_authority/DA-FIRSTREVIEW-FIXTURE.json"
        harness.authority.update(
            _record_path=authority_path,
            source_body_sha256=hashlib.sha256(harness.authority["source_body"].encode()).hexdigest(),
        )
        self.write_json(authority_path, harness.authority)
        harness.continuation.require_review_authority.return_value = copy.deepcopy(harness.authority)
        harness.namespace["_driver_authority"].require_active_driver.return_value = copy.deepcopy(harness.authority)
        harness.namespace["_driver_authority"].valid_records.return_value = [copy.deepcopy(harness.authority)]

        self.authority_module = types.ModuleType("research_driver_authority")
        self.authority_module.require_active_driver = mock.Mock(return_value=copy.deepcopy(harness.authority))
        self.guard = types.ModuleType("research_driver_followup_guard")
        self.guard.authority_map = lambda root: {"DR-FIRSTREVIEW-FIXTURE": self.review_view()}
        self.guard._immutable_review_map = self.guard.authority_map
        self.impl = types.ModuleType("research_driver_followup")
        self.impl.DriverFollowupError = FixtureFollowupError
        self.impl.review_map = self.guard.authority_map
        self.impl.result_map = lambda root: {harness.result["result_id"]: harness.result}
        self.impl.review_requires_followup = lambda review: True
        self.impl._source_parent_objective = lambda *args: "OBJ-FIRSTREVIEW-FIXTURE"
        self.impl._gate_map = lambda gates: gates
        self.impl._forced_gate_rules = mock.Mock()
        self.impl._now = lambda value=None: value or STAMP
        self.impl.DECISIONS = {"TASK_SET_PUBLISHED"}
        functions = _load_functions(SOURCE_ROOT / "research_driver_followup.py", {
            "_materialization_binding", "_result_record_pin", "_source_review_record_pin",
        }, {
            "Path": Path, "json": json, "hashlib": hashlib,
            "DriverFollowupError": FixtureFollowupError,
            "result_map": self.impl.result_map, "_now": self.impl._now,
        })
        self.actual_binding = functions["_materialization_binding"]

        def capture_binding(*args, **kwargs):
            self.observed_binding = self.actual_binding(*args, **kwargs)
            return self.observed_binding

        self.impl._materialization_binding = capture_binding
        self.prospective = types.ModuleType("control_plane.research_prospective_result_authority_binding")
        self.prospective.__dict__.update(json=json, REQUEST=copy.deepcopy(EXACT_REQUEST), FIELD=FIELD)
        _load_functions(
            SOURCE_ROOT / "control_plane/research_prospective_result_authority_binding.py",
            {"_require", "_canonical", "validate_request"}, self.prospective.__dict__,
        )
        harness.control_plane.research_prospective_result_authority_binding = self.prospective
        self.task_records = types.ModuleType("tools.research_task_records")
        self.task_records.current_records = mock.Mock(side_effect=ReachedCurrentSourceAfterPublisherGuard)
        tools_module = types.ModuleType("tools")
        tools_module.__path__ = []
        tools_module.research_task_records = self.task_records
        self.followup_commit = mock.Mock()
        transaction = _load_functions(
            SOURCE_ROOT / "control_plane/research_driver_followup_transaction.py", {"materialize"}, {
                "ROOT": root, "Path": Path,
                "DriverFollowupTransactionError": FixtureTransactionError,
                "_tx": types.SimpleNamespace(commit=self.followup_commit),
            },
        )
        self.impl.materialize = transaction["materialize"]
        self.guard.__dict__.update(
            ROOT=root, Path=Path, DriverFollowupError=FixtureFollowupError,
            baseline_audit=mock.Mock(return_value=[]), _bind_guard=mock.Mock(), _impl=self.impl,
            _canonical_results=lambda: types.SimpleNamespace(DESTINATION_CLASSES={"FOLLOWUP_TASK"}),
        )
        _load_functions(SOURCE_ROOT / "research_driver_followup_guard.py", {"materialize"}, self.guard.__dict__)
        harness.extra_modules = {
            "research_driver_authority": self.authority_module,
            "research_driver_followup_guard": self.guard,
            "research_driver_followup": self.impl,
            "control_plane.research_prospective_result_authority_binding": self.prospective,
            "tools": tools_module, "tools.research_task_records": self.task_records,
        }

    def write_json(self, relative, value):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, sort_keys=True) + "\n", encoding="utf-8")

    def file_digest(self, relative):
        return "sha256:" + hashlib.sha256((self.root / relative).read_bytes()).hexdigest()

    def review_view(self):
        relative = f"research_result_reviews/{self.harness.result['result_id']}/DR-FIRSTREVIEW-FIXTURE.json"
        return {
            **json.loads((self.root / relative).read_text(encoding="utf-8")),
            "_review_path": relative, "review_authority_kind": "IMMUTABLE_REVIEW",
            "source_review_ids": ["DR-FIRSTREVIEW-FIXTURE"],
        }

    def materialize(self, **kwargs):
        try:
            self.guard.materialize(**kwargs)
        except ReachedCurrentSourceAfterPublisherGuard:
            return {"state": "STOPPED_AFTER_REAL_PROSPECTIVE_PUBLISHER_GUARD"}
        raise AssertionError("fixture must stop before Task preparation or publication")


class FirstReviewProspectivePublisherBindingTests(unittest.TestCase):
    def assert_no_write_or_materialization(self, harness):
        harness.commit.assert_not_called()
        harness.materialize.assert_not_called()
        self.assertEqual([], harness.committed)
        self.assertEqual([], harness.events)

    def test_first_prospective_review_forwards_authenticated_publisher_after_receipted_dr(self):
        harness = ReviewWriterHarness()
        self.assertEqual(0, harness.run())
        harness.continuation.require_review_authority.assert_called_once_with(
            harness.result, harness.args, root=harness.root)
        self.assertEqual(["commit", "materialize"], harness.events)
        self.assertEqual(1, len(harness.committed))
        record = json.loads(harness.committed[0][1])
        receipt = record["write_authorization"]
        self.assertEqual("REVIEW", receipt["kind"])
        self.assertEqual("ENTERPRISE_MATH_CONTROL_WRITE_AUTHORIZATION_V1", receipt["schema"])
        self.assertEqual(harness.payload_digest(record), receipt["payload_sha256"])
        self.assertEqual({
            "authority_record_id": harness.authority["authority_record_id"],
            "session_id": SESSION, "driver_id": DRIVER,
        }, receipt["principal"])
        self.assertEqual(SESSION, record["reviewer_session_id"])
        self.assertEqual(receipt, harness.preflight.call_args.kwargs["review_candidate"]["write_authorization"])
        harness.materialize.assert_called_once_with(
            review_id=record["review_id"], spec=harness.spec,
            created_at=STAMP, root=harness.root,
            publishing_driver_id=DRIVER, publisher_session_id=SESSION,
        )

    def test_prospective_request_without_current_authority_rejects_before_dr_commit(self):
        harness = ReviewWriterHarness(current_authority=False)
        with self.assertRaises(FixtureResultError):
            harness.run()
        self.assert_no_write_or_materialization(harness)

    def test_real_command_guard_transaction_and_binding_validate_raw_pins_before_task_work(self):
        with tempfile.TemporaryDirectory(prefix="rr133-first-review-boundary-") as directory:
            harness = ReviewWriterHarness()
            boundary = RealPublisherBoundary(harness, Path(directory))
            # With the old writer, the actual transaction rejects binding=None;
            # with the fix, real binding validation reaches the controlled stop.
            self.assertEqual(0, harness.run())
            binding = boundary.observed_binding
            self.assertIsInstance(binding, dict)
            self.assertEqual(DRIVER, binding["driver_id"])
            self.assertEqual(SESSION, binding["session_id"])
            self.assertEqual("ENTERPRISE_MATH_FOLLOWUP_PUBLISHER_BINDING_V1", binding["schema"])
            self.assertEqual(boundary.file_digest(harness.authority["_record_path"]), binding["authority_record_sha256"])
            self.assertEqual(boundary.file_digest(harness.result["_record_path"]), binding["source_result_record_sha256"])
            raw_review_path = harness.committed[0][0].relative_to(boundary.root).as_posix()
            self.assertEqual([{
                "review_id": "DR-FIRSTREVIEW-FIXTURE", "record_path": raw_review_path,
                "record_sha256": boundary.file_digest(raw_review_path),
            }], binding["source_review_records"])
            self.assertEqual(["commit", "materialize"], harness.events)
            boundary.task_records.current_records.assert_called_once_with(boundary.root)
            boundary.followup_commit.assert_not_called()
            self.assertEqual(2, boundary.authority_module.require_active_driver.call_count)
            receipt = json.loads(harness.committed[0][1])["write_authorization"]
            self.assertEqual(SESSION, receipt["principal"]["session_id"])
            self.assertEqual("REVIEW", receipt["kind"])

    def test_actual_binding_preserves_both_none_legacy_return(self):
        namespace = _load_functions(
            SOURCE_ROOT / "research_driver_followup.py", {"_materialization_binding"}, {},
        )
        self.assertIsNone(namespace["_materialization_binding"](
            "DR-FIRSTREVIEW-FIXTURE", None, None, STAMP, SOURCE_ROOT, require_current=True,
        ))

    def test_prospective_request_without_nonempty_session_rejects_before_dr_commit(self):
        for session in (None, "", "   "):
            with self.subTest(session=session):
                harness = ReviewWriterHarness(session=session)
                # The held DA contains a valid session: the writer must not infer it.
                self.assertEqual(SESSION, json.loads(harness.authority["source_body"])["session_id"])
                with self.assertRaises(FixtureResultError):
                    harness.run()
                self.assert_no_write_or_materialization(harness)

    def test_prospective_request_without_session_argument_does_not_infer_one(self):
        harness = ReviewWriterHarness()
        del harness.args.reviewer_session_id
        with self.assertRaises(FixtureResultError):
            harness.run()
        self.assert_no_write_or_materialization(harness)

    def test_ordinary_first_review_keeps_legacy_materialize_keyword_shape(self):
        harness = ReviewWriterHarness(prospective=False)
        self.assertEqual(0, harness.run())
        self.assertEqual(["commit", "materialize"], harness.events)
        harness.materialize.assert_called_once_with(
            review_id="DR-FIRSTREVIEW-FIXTURE", spec=harness.spec,
            created_at=STAMP, root=harness.root,
        )
        self.assertIn("write_authorization", json.loads(harness.committed[0][1]))

    def test_ordinary_first_review_keeps_sessionless_compatibility_when_gate_is_disabled(self):
        harness = ReviewWriterHarness(prospective=False, current_authority=False, session=None)
        del harness.args.reviewer_session_id
        self.assertEqual(0, harness.run())
        harness.materialize.assert_called_once_with(
            review_id="DR-FIRSTREVIEW-FIXTURE", spec=harness.spec,
            created_at=STAMP, root=harness.root,
        )
        self.assertNotIn("write_authorization", json.loads(harness.committed[0][1]))

    def test_ordinary_gov_task_only_first_review_keeps_legacy_keyword_shape(self):
        harness = ReviewWriterHarness(prospective=False)
        harness.spec.update(
            decision="TASK_SCOPE_CLOSURE_PORTFOLIO_CONTINUATION", tasks=[], terminal_scope="TASK",
            portfolio_continuation={"fixture": "Task-only preflight is a separate boundary"},
        )
        self.assertEqual(0, harness.run())
        harness.materialize.assert_called_once_with(
            review_id="DR-FIRSTREVIEW-FIXTURE", spec=harness.spec,
            created_at=STAMP, root=harness.root,
        )

    def test_second_review_remains_deferred_without_materialization(self):
        harness = ReviewWriterHarness(existing=True, supplied_spec=False)
        self.assertEqual(0, harness.run())
        self.assertEqual(["commit"], harness.events)
        harness.materialize.assert_not_called()
        harness.preflight.assert_not_called()
        harness.review_state.assert_called_once_with(harness.result["result_id"], harness.root)
        payload = json.loads(harness.output.getvalue())
        self.assertEqual("DEFERRED_UNTIL_EXACT_REVIEW_SYNTHESIS", payload["followup"]["state"])
        self.assertEqual("AWAITING_REVIEW_INTAKE", payload["followup"]["review_state"])

    def test_second_review_with_followup_spec_still_rejects_before_write(self):
        harness = ReviewWriterHarness(existing=True)
        with self.assertRaisesRegex(FixtureResultError, "second-or-later review"):
            harness.run()
        self.assert_no_write_or_materialization(harness)


if __name__ == "__main__":
    unittest.main()
