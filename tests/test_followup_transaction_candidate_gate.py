"""Fresh-process local follow-up transactions retain exact candidate boundaries."""
from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import unittest

REPO = Path(__file__).resolve().parents[1]
CASES = (
    "taskset", "closure", "bad_candidate", "duplicate_before", "duplicate_after",
    "taskbook_drift", "publication_drift", "coordinated_drift", "result_missing",
    "second_review", "objective_reopen", "isolation_pin_drift", "stale_isolation", "packet_drift",
)


def run_case(case):
    import copy
    import contextlib
    import hashlib
    import io
    import tempfile
    from unittest import mock

    sys.path[:0] = [str(REPO), str(REPO.joinpath("tests"))]
    from control_plane import research_control_bootstrap as bootstrap
    from control_plane import research_driver_followup_transaction as tx
    from control_plane import check_driver_followup_nonoperational_review_fault_isolated as checker
    from control_plane import research_driver_followup_fault_isolation as isolation
    from control_plane import research_result_review_audit_fault_isolation as review_isolation
    from tools import research_task_records, research_taskbook, research_result_records
    import research_driver_followup as impl
    import research_driver_followup_guard as guard
    from test_research_task_record_compatibility import _write_current_record, _write_semantic_fixture

    with tempfile.TemporaryDirectory(prefix="em-followup-candidate-") as directory:
        root = Path(directory)

        def write(relative, value):
            path = root.joinpath(relative)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes((json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
            return path

        def capture(relative):
            path = root.joinpath(relative)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(REPO.joinpath(relative).read_bytes())
            return json.loads(path.read_bytes()) if relative.endswith(".json") else None

        # Preserve an actual exact historical review/packet isolation chain.
        registry = json.loads(REPO.joinpath(isolation.QUARANTINE_FILE).read_bytes())
        old = next(row for row in registry["entries"] if
                   row.get("source_review_basis") == isolation.AUDIT_SOURCE and
                   row.get("isolation_kind") == isolation.PACKET_ONLY)
        write(isolation.QUARANTINE_FILE, {**registry, "entries": [old]})
        review_registry = json.loads(REPO.joinpath(review_isolation.QUARANTINE_FILE).read_bytes())
        old_review = next(row for row in review_registry["entries"] if row["review_id"] == old["review_id"])
        write(review_isolation.QUARANTINE_FILE, {**review_registry, "entries": [old_review]})
        capture(old["packet_path"])
        historical_review = capture(old_review["review_record_path"])
        capture(old_review["result_record_path"])
        capture(historical_review["review_path"])

        # Existing helper makes a real independently blocked semantic fixture;
        # canonical bootstrap/validators run, with no authority grants mocked.
        _write_semantic_fixture(root)
        policy = capture("research_taskbook_policy.json")
        for relative in policy["policy_inputs"]:
            capture(relative)
        # Guard keeps its immutable legacy membership contract, not timestamps.
        baseline = capture("research_driver_followup_legacy_reviews.json")
        raw_reviews = research_result_records._base._RAW_ITER_REVIEWS(REPO)
        by_id = {row["review_id"]: row for row in raw_reviews}
        for review_id in baseline["review_ids"]:
            capture(by_id[review_id]["_review_path"])

        # Full bootstrap requires its real nonempty Driver fault basis.
        driver_registry = json.loads(REPO.joinpath("research_driver_review_authority_quarantines.json").read_bytes())
        driver_fault = driver_registry["entries"][0]
        write("research_driver_review_authority_quarantines.json", {**driver_registry, "entries": [driver_fault]})
        capture(driver_fault["review_record_path"])
        capture("research_driver_authority_contract.json")
        capture("research_control_event_authorization.json")

        parent, driver = "OBJ-FOLLOWUP-FIXTURE", "EM-DVR-01E1D9"
        reviewed_at, created_at = "2026-09-08T08:00:00+00:00", "2026-09-08T09:00:00+00:00"
        authority = research_result_records._driver_authority.require_active_driver(driver, reviewed_at, REPO)
        capture(authority["_record_path"])

        def source(label):
            task_id, result_id, publication_id = "RS-" + label, "RR-" + label, "TP2-" + label
            _write_current_record(root, task_id=task_id, publication_id=publication_id,
                                  parent_objective_id=parent, publisher_role="RESEARCH_DRIVER",
                                  publisher_id=driver, published_at=reviewed_at)
            result = {"record_schema": research_result_records.RESULT_SCHEMA,
                      "task_id": task_id, "result_id": result_id, "publication_id": publication_id,
                      "execution_record_id": "ER-" + label, "method_harvest": "RESULT_ONLY",
                      "next_control_plane_recommendation": "Bounded fixture follow-up.",
                      "frozen_at": reviewed_at}
            rp = f"research_result_records/{task_id}/{result_id}.json"
            write(rp, result)
            result["_record_path"] = rp
            artifact = root.joinpath("fixtures", label + ".md")
            artifact.parent.mkdir(exist_ok=True)
            artifact.write_bytes(("Temporary fixture review " + label + "\n").encode())
            review = research_result_records.review_result(
                result=result, driver_id=driver, disposition="REQUEST_REVISION", review_path=artifact,
                destination_class="NONE", destination_ref_or_none="", reviewed_at=reviewed_at, root=root,
            )
            review.update(driver_authority_record_id=authority["authority_record_id"],
                          driver_authority_source_comment_id=authority["source_comment_id"])
            write(f"research_result_reviews/{result_id}/{review['review_id']}.json", review)
            return result, review

        result, review = source("CANDIDATE-SOURCE")
        source("UNRELATED-PENDING")
        # An unregistered historical packet error remains raw diagnostic history.
        historical_path = "research_driver_followups/DR-UNRELATED-OLD/DFU-UNRELATED-OLD.json"
        write(historical_path, {"packet_id": "DFU-UNRELATED-OLD", "review_id": "DR-UNRELATED-OLD"})
        closure = case in {"closure", "objective_reopen"}
        objective_path = write("research_objective_heads/OBJ-FOLLOWUP-FIXTURE.json",
                               {"objective_id": parent, "objective_status": "CLOSED" if closure else "ACTIVE"})
        task = {"task_id": "RS-FOLLOWUP-CANDIDATE", "title": "Candidate transaction fixture",
                "task_role": "REVISION", "task_lineage": "REPLAY", "identity_lane": "FIXTURE",
                "frontier": "Temporary test only.", "next_action": "Check transaction boundaries.",
                "research_value": "Preserve exact candidate bindings.",
                "mother_question": "Does the candidate retain its exact sources?",
                "frozen_inputs_and_scope": "Only this temporary fixture.",
                "hard_target_and_required_outputs": "One bounded fixture taskbook.",
                "research_value_to_preserve": "Immutable test source history.",
                "success_kill_and_return_criteria": "Reject changed candidate sources."}
        spec = {"decision": "PARENT_OBJECTIVE_CLOSURE" if closure else "TASK_SET_PUBLISHED",
                "gate_decisions": [{"gate": gate, "decision": "NOT_REQUIRED", "reason": "Fixture scope.",
                                    "evidence_refs": []} for gate in impl.GATES],
                "tasks": [] if closure else [task]}
        bootstrap.install(root)
        guard._bind_guard(root)
        assert checker.audit(root) == []
        before = {path: path.read_bytes() for path in root.rglob("*") if path.is_file()}
        raw_before = impl.audit(root)
        assert any("DR-UNRELATED-OLD" in error for error in raw_before)
        assert any("no automatic follow-up" in error for error in raw_before)

        frozen = {}
        build_packet = impl.build_packet

        def build(**kwargs):
            packet = build_packet(**kwargs)
            if case == "bad_candidate":
                packet["source_publication_id"] = "TP2-WRONG"
            frozen.update(copy.deepcopy(packet))
            return packet

        def packet_path():
            return root.joinpath("research_driver_followups", review["review_id"], frozen["packet_id"] + ".json")

        mutated = set()
        external = set()
        real_check = checker.audit

        def check_with_tamper(local_root):
            new_records = [p for p in root.joinpath("research_task_records").glob("*/*.json") if p not in before]
            if case in {"taskbook_drift", "publication_drift", "coordinated_drift"}:
                rp = new_records[0]
                record = json.loads(rp.read_bytes())
                book = root.joinpath(record["taskbook_path"])
                if case != "publication_drift":
                    book.write_bytes(book.read_bytes() + b"\nChanged during postcheck.\n")
                    mutated.add(book)
                if case == "publication_drift":
                    record["research_value"] = "Changed non-binding metadata."
                if case == "coordinated_drift":
                    record["taskbook_blob_sha1"] = research_task_records.taskbook_blob(book)
                if case != "taskbook_drift":
                    rp.write_bytes(tx._task_record_bytes(record)); mutated.add(rp)
            elif case == "duplicate_after":
                external.add(write("research_driver_followups/DR-OTHER/DFU-COPY.json", frozen))
            elif case == "packet_drift":
                path = packet_path()
                path.write_bytes(path.read_bytes() + b"\n")
                mutated.add(path)
            elif case == "result_missing":
                root.joinpath(result["_record_path"]).unlink()
                mutated.add(root.joinpath(result["_record_path"]))
            elif case == "second_review":
                additional = copy.deepcopy(review)
                additional["review_id"] = "DR-SECOND-FIXTURE"
                external.add(write(f"research_result_reviews/{result['result_id']}/DR-SECOND-FIXTURE.json", additional))
            elif case == "objective_reopen":
                value = json.loads(objective_path.read_bytes()); value["objective_status"] = "ACTIVE"
                objective_path.write_bytes((json.dumps(value) + "\n").encode()); mutated.add(objective_path)
            elif case == "isolation_pin_drift":
                path = root.joinpath(old["packet_path"])
                path.write_bytes(path.read_bytes() + b"\n"); mutated.add(path)
            elif case == "stale_isolation":
                path = root.joinpath(review_isolation.QUARANTINE_FILE)
                value = json.loads(path.read_bytes())
                value["entries"][0]["allowed_review_audit_errors"].append("nonexistent error")
                path.write_bytes((json.dumps(value) + "\n").encode()); mutated.add(path)
            return real_check(local_root)

        if case == "duplicate_before":
            extra = {"packet_id": "DFU-OTHER-ID", "review_id": review["review_id"]}
            external.add(write(f"research_driver_followups/{review['review_id']}/DFU-OTHER-ID.json", extra))
        failed = None
        with mock.patch.object(impl, "build_packet", side_effect=build), \
             mock.patch.object(checker, "audit", side_effect=check_with_tamper), \
             contextlib.redirect_stdout(io.StringIO()):
            try:
                packet = tx.materialize(review_id=review["review_id"], spec=spec, created_at=created_at, root=root)
            except Exception as exc:
                failed = str(exc)
        successful = case in {"taskset", "closure"}
        if successful:
            assert failed is None, failed
            assert packet_path().read_bytes() == tx._packet_bytes(frozen)
            assert impl.audit(root), "raw historical diagnostics must remain visible"
        else:
            assert failed is not None, "bad candidate unexpectedly succeeded"
            expected = {
                "bad_candidate": "packet source publication mismatch",
                "duplicate_before": "existing review/packet identity",
                "duplicate_after": "unique exact review packet",
                "taskbook_drift": "follow-up taskbook blob drift",
                "publication_drift": "source differs from frozen candidate bytes",
                "coordinated_drift": "source differs from frozen candidate bytes",
                "result_missing": "unknown review", "second_review": "unknown review",
                "objective_reopen": "canonical parent Objective head is CLOSED",
                "isolation_pin_drift": "packet blob drift",
                "stale_isolation": "exact audit error set drift",
                "packet_drift": "differs from frozen candidate bytes",
            }[case]
            assert expected in failed, failed
            if packet_path() not in mutated:
                assert not packet_path().exists(), failed
            remaining_new = {p for p in root.rglob("*") if p.is_file()} - set(before)
            assert remaining_new <= mutated | external, remaining_new
            if case in {"taskbook_drift", "publication_drift", "coordinated_drift", "packet_drift"}:
                assert "refused rollback because candidate changed" in failed, failed
                assert all(p.exists() for p in mutated)
        for path, content in before.items():
            if path not in mutated:
                assert path.read_bytes() == content, path
        print(json.dumps({"case": case, "status": "PASS", "success_expected": successful,
                          "failure": failed, "new_frozen_packet_id": frozen.get("packet_id"),
                          "historical_raw_errors_before": len(raw_before),
                          "history_preserved_except_deliberate_fault_injection": True}))


class FollowupTransactionCandidateGateTests(unittest.TestCase):
    def check_case(self, case):
        environment = os.environ.copy()
        environment.pop("PYTHONPATH", None)
        run = subprocess.run([sys.executable, "-B", "-X", "utf8", str(Path(__file__).resolve()),
                              "--case", case], cwd=REPO, env=environment,
                             capture_output=True, text=True, encoding="utf-8", timeout=60)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        self.assertEqual(json.loads(run.stdout)["status"], "PASS")
        print(run.stdout, end="")


for case_name in CASES:
    setattr(FollowupTransactionCandidateGateTests, "test_" + case_name,
            lambda self, case=case_name: self.check_case(case))


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--case":
        run_case(sys.argv[2])
    else:
        unittest.main()
