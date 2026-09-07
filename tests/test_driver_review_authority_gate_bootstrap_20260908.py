"""The standalone Driver gate consumes the canonical, source-validated view."""
from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import research_driver_authority as authority
from control_plane import check_driver_review_authority_fault_isolated as gate
from control_plane import research_control_bootstrap as bootstrap
from control_plane import research_driver_review_authority_fault_isolation as isolation
from test_research_task_record_compatibility import _write_semantic_fixture

ROOT = Path(__file__).resolve().parents[1]
ALIAS_REVIEW = "research_result_reviews/RR-16ADB5F4DE72A332B509/DR-2E05A15480A51DF3BD43.json"
VALID_RESULT = "RR-00F7FFAA06553D90B4AC"
MISSING_PIN_REVIEW = "DR-98D79A8522754B43637A"
WITHHELD_REVIEW = "DR-1337737608BDE3D7E621"


def _load(root, rel):
    return json.loads((root / rel).read_text(encoding="utf-8"))


def _write(root, rel, value):
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes((json.dumps(value, indent=2) + "\n").encode("utf-8"))


def _view():
    import research_driver_followup
    from tools import research_dispatch, research_result_records, research_task_records

    return {
        "results": {r["result_id"]: r for r in research_result_records.iter_results(ROOT)},
        "reviews": {r["review_id"]: r for r in research_result_records.iter_reviews(ROOT)},
        "packets": research_driver_followup.iter_packets(ROOT),
        "current": research_task_records.current_records(ROOT),
        "definitions": {r["task_id"]: r for r in research_dispatch.merged_definitions(ROOT)},
    }


def _fresh_order_snapshot(order):
    """Fresh processes distinguish standalone admission from prior bootstrap."""
    if order == "bootstrap-first":
        bootstrap.install(ROOT)
        initial = _view()
    else:
        assert not getattr(authority, "_raw_authority_review_pin_compat_installed", False)
        initial = None
    errors = gate.audit()
    assert not errors, errors
    first = _view()
    bootstrap.install(ROOT)
    errors = gate.audit()
    assert not errors, errors
    second = _view()
    assert first == second
    if initial is not None:
        assert initial == second
    return second


class DriverReviewAuthorityGateBootstrapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        bootstrap.install(ROOT)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.review = _load(ROOT, ALIAS_REVIEW)
        self.review["review_id"] = "DR-GATE-FIXTURE"
        self.review_path = f"research_result_reviews/{self.review['result_id']}/DR-GATE-FIXTURE.json"
        self.alias_payload = _load(ROOT, authority.COMPATIBILITY)
        self.alias = next(r for r in self.alias_payload["id_aliases"]
                          if r["raw_authority_record_id"] == self.review["driver_authority_record_id"])
        self.alias_payload["id_aliases"] = [self.alias]
        for rel in (authority.CONTRACT, authority.CONTROL_POLICY, self.alias["record_path"]):
            path = self.root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes((ROOT / rel).read_bytes())
        _write(self.root, authority.COMPATIBILITY, self.alias_payload)
        _write(self.root, self.review_path, self.review)
        primary = _load(ROOT, isolation.QUARANTINE_FILE)
        primary["entries"] = [next(r for r in primary["entries"]
                                   if r["review_id"] == "DR-2F834647FD94CAF46D05")]
        pinned = primary["entries"][0]["review_record_path"]
        path = self.root / pinned
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes((ROOT / pinned).read_bytes())
        _write(self.root, isolation.QUARANTINE_FILE, primary)
        _write_semantic_fixture(self.root)

    def test_standalone_workflow_cli_passes_in_a_fresh_process(self):
        run = subprocess.run([sys.executable, "control_plane/check_driver_review_authority_fault_isolated.py"],
                             cwd=ROOT, capture_output=True, text=True, timeout=90)
        self.assertEqual(0, run.returncode, run.stdout + run.stderr)
        self.assertIn("PASS: source-backed Driver authority is valid on the operational review view", run.stdout)
        self.assertEqual("", run.stderr)

    def test_fresh_cli_first_and_bootstrap_first_keep_the_same_public_views(self):
        snapshots = []
        for order in ("gate-first", "bootstrap-first"):
            output = self.root / f"{order}.json"
            code = (
                "import json,sys; from pathlib import Path; "
                "sys.path.insert(0,str(Path.cwd()/'tests')); "
                "from test_driver_review_authority_gate_bootstrap_20260908 import _fresh_order_snapshot; "
                "Path(sys.argv[2]).write_text(json.dumps(_fresh_order_snapshot(sys.argv[1]),sort_keys=True),encoding='utf-8')"
            )
            run = subprocess.run([sys.executable, "-c", code, order, str(output)], cwd=ROOT,
                                 capture_output=True, text=True, timeout=180)
            self.assertEqual(0, run.returncode, run.stdout + run.stderr)
            snapshots.append(json.loads(output.read_text(encoding="utf-8")))
        self.assertEqual(snapshots[0], snapshots[1])
        self.assertTrue(all(snapshots[0][key]
                            for key in ("results", "reviews", "packets", "current", "definitions")))

    def test_valid_result_survives_its_separately_invalid_review(self):
        from control_plane import research_result_authority_fault_isolation as result_isolation
        from tools import research_result_records

        self.assertEqual([], gate.audit())
        self.assertIn(VALID_RESULT, {r["result_id"] for r in research_result_records.iter_results(ROOT)})
        reviews = {r["review_id"] for r in research_result_records.iter_reviews(ROOT)}
        self.assertNotIn(MISSING_PIN_REVIEW, reviews)
        self.assertIn(MISSING_PIN_REVIEW, isolation.validated_quarantines(ROOT))
        self.assertNotIn(VALID_RESULT, result_isolation.validated_rows(ROOT))
        self.assertNotIn(WITHHELD_REVIEW, reviews)
        self.assertIn(WITHHELD_REVIEW, result_isolation.validated_review_rows(ROOT))
        self.assertNotIn(WITHHELD_REVIEW, isolation.validated_quarantines(ROOT))
        raw = _load(ROOT, f"research_result_reviews/{VALID_RESULT}/{MISSING_PIN_REVIEW}.json")
        self.assertTrue(authority.review_authority_errors(raw, ROOT))

    def test_raw_alias_requires_its_exact_active_record_and_source_comment(self):
        self.assertEqual([], authority.review_authority_errors(self.review, self.root))
        active = authority.require_active_driver(self.review["driver_id"], self.review["reviewed_at"], self.root)
        self.assertEqual(self.alias["normalized_authority_record_id"], active["authority_record_id"])
        self.assertEqual(self.alias["raw_authority_record_id"], active["_raw_authority_record_id"])
        for field in ("driver_authority_record_id", "driver_authority_source_comment_id"):
            with self.subTest(field=field):
                changed = copy.deepcopy(self.review)
                changed[field] = "DA-FORGED" if field.endswith("record_id") else 1
                self.assertTrue(authority.review_authority_errors(changed, self.root))

    def test_raw_alias_byte_and_normalized_identity_drift_fail_closed(self):
        source = self.root / self.alias["record_path"]
        original = source.read_bytes()
        source.write_bytes(original + b"\n")
        self.assertIn("immutable authority record blob drift", "\n".join(authority.review_authority_errors(self.review, self.root)))
        source.write_bytes(original)
        self.alias["normalized_authority_record_id"] = "DA-FORGED"
        _write(self.root, authority.COMPATIBILITY, self.alias_payload)
        self.assertIn("normalized authority id does not equal current formula",
                      "\n".join(authority.review_authority_errors(self.review, self.root)))

    def test_standalone_gate_still_rejects_unregistered_bad_authority(self):
        # Each process changes only the input root, and starts with no installed
        # compatibility layers. No bootstrap/source/authority validator is mocked.
        code = (
            "import sys; from pathlib import Path; "
            "from control_plane import check_driver_review_authority_fault_isolated as g; "
            "g.ROOT=Path(sys.argv[1]); raise SystemExit(g.main())"
        )
        valid = subprocess.run([sys.executable, "-c", code, str(self.root)], cwd=ROOT,
                               capture_output=True, text=True, timeout=60)
        self.assertEqual(0, valid.returncode, valid.stdout + valid.stderr)
        self.review["driver_authority_source_comment_id"] = 1
        _write(self.root, self.review_path, self.review)
        invalid = subprocess.run([sys.executable, "-c", code, str(self.root)], cwd=ROOT,
                                 capture_output=True, text=True, timeout=60)
        self.assertEqual(1, invalid.returncode, invalid.stdout + invalid.stderr)
        self.assertEqual("", invalid.stderr)
        self.assertEqual(
            "ERROR: " + self.review_path + ": driver_authority_record_id does not pin active authority",
            invalid.stdout.strip(),
        )

    def test_known_quarantine_pin_drift_is_not_hidden_by_canonical_bootstrap(self):
        row = _load(self.root, isolation.QUARANTINE_FILE)["entries"][0]
        path = self.root / row["review_record_path"]
        path.write_bytes(path.read_bytes() + b"\n")
        with patch.object(gate, "ROOT", self.root):
            errors = gate.audit()
        self.assertTrue(any("review record blob drift" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
