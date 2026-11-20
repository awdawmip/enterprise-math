"""Public synthetic development checks; no scientific or model benchmark runs."""
import copy
import json
from pathlib import Path
import unittest

from validate_evaluation import validate_comparison, validate_run

HERE = Path(__file__).resolve().parent


def valid():
    return json.loads((HERE / "fixtures" / "synthetic_valid_run.json").read_text(encoding="utf-8"))


def free_a():
    run = valid()
    run["mode_id"] = "M0_CURRENT"
    run["track"] = "FREE_A"
    run["exposure_profile"].update(stage="FREE_A", allowed_lookup="question_first_precise",
                                   withheld_nonmandatory_result_set_id="WITHHELD_NONMANDATORY_RESULT_SET")
    return run


def add_result(run):
    source = {"id": "synthetic-result", "identity": "synthetic://result", "version": "c" * 40,
              "kind": "result", "knowledge_role": "scientific", "classification": "public",
              "available_at": "2026-10-01T00:00:00Z",
              "claims": {"r1": {"status": "AUTHOR_DRAFT", "contract_digest": "synthetic-r1"}}}
    run["sources"].append(source)
    return source


def native_run():
    run = valid()
    run["mode_id"] = "M5_NOLLM_NATIVE"
    add_result(run)
    run["build"]["source_ids"].append("synthetic-result")
    run["attribution"].update(entry_basis="surface_observation", label="native_only",
                              native_source_ids=["synthetic-result"])
    run["events"].extend([
        {"type": "native_select", "source_id": "synthetic-result", "selection_id": "select1",
         "at": "2026-11-02T00:01:00Z", "exposed_to": "internal"},
        {"type": "read", "source_id": "synthetic-result", "selection_id": "select1",
         "at": "2026-11-02T00:02:00Z", "route": "access_after_native", "exposed_to": "research"},
    ])
    run["returned_claims"] = [{"id": "r1", "source_id": "synthetic-result",
                               "status": "AUTHOR_DRAFT", "contract_digest": "synthetic-r1"}]
    return run


def heldout_contract():
    # Synthetic metadata describes a proposed heldout run for validator testing.
    # This does not create or execute a real heldout task.
    run = valid()
    run["synthetic"] = False
    run["artifact_classification"] = "RESTRICTED_EVALUATION_METADATA"
    run["split"] = "heldout"
    run["split_manifest"]["heldout_family_ids"] = [run["case_family_id"]]
    return run


class ContractChecks(unittest.TestCase):
    def assertRejected(self, run, fragment):
        errors = validate_run(run)
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_valid_public_development_fixture(self):
        self.assertEqual(validate_run(valid()), [])

    def test_free_a_exact_definition_before_freeze_is_allowed(self):
        run = free_a()
        run["events"].extend([
            {"type": "question_formed", "question_id": "q1", "at": "2026-11-02T00:01:00Z"},
            {"type": "read", "source_id": "synthetic-definition", "question_id": "q1",
             "relevance_declared": True, "at": "2026-11-02T00:02:00Z", "route": "direct"},
        ])
        self.assertEqual(validate_run(run), [])

    def test_free_a_keeps_mandatory_foundation_even_when_it_contains_prior_results(self):
        run = free_a()
        run["sources"][0]["claims"] = {
            "inherited-foundation-result": {"status": "MANDATORY_FOUNDATION",
                                            "contract_digest": "synthetic-inherited-contract"}}
        run["helper"]["result_exposure_scope"] = "WITHHELD_NONMANDATORY_RESULT_SET"
        self.assertEqual(validate_run(run), [])

    def test_free_a_definition_requires_formed_relevant_question(self):
        run = free_a()
        run["events"].append(
            {"type": "read", "source_id": "synthetic-definition", "question_id": "q1",
             "relevance_declared": True, "at": "2026-11-02T00:01:00Z", "route": "direct"})
        self.assertRejected(run, "precedes its formed question")

    def test_free_a_rejects_result_catalog(self):
        run = free_a()
        run["sources"][0]["kind"] = "result_catalog"
        self.assertRejected(run, "exposes result/catalog")

    def test_free_a_rejects_task_input_that_task_baseline_allows(self):
        run = free_a()
        run["sources"][0]["kind"] = "task_input"
        self.assertRejected(run, "FREE_A eligible source pool")
        self.assertRejected(run, "FREE_A memory build")
        self.assertRejected(run, "FREE_A exposure")
        task_run = native_run()
        task_run["sources"][0]["kind"] = "task_input"
        self.assertEqual(validate_run(task_run), [])

    def test_free_a_checks_all_declared_visible_content_channels(self):
        for event_type in ("title_preview", "preview", "error_output", "tool_output", "source_exposure"):
            with self.subTest(event_type=event_type):
                run = free_a()
                source = add_result(run)
                source["kind"] = "result_catalog"
                run["events"].append({"type": event_type, "source_id": "synthetic-result",
                                      "at": "2026-11-02T00:01:00Z", "exposed_to": "research"})
                self.assertRejected(run, "exposure exposes result/catalog")

    def test_free_a_rejects_unknown_source_bearing_event(self):
        run = free_a()
        run["events"].append({"type": "opaque_summary", "source_id": "synthetic-definition",
                              "at": "2026-11-02T00:01:00Z", "exposed_to": "research"})
        self.assertRejected(run, "unknown source-bearing event type")

    def test_free_a_precise_preview_after_formed_question_is_allowed(self):
        run = free_a()
        run["events"].extend([
            {"type": "question_formed", "question_id": "q1", "at": "2026-11-02T00:01:00Z"},
            {"type": "preview", "source_ids": ["synthetic-definition"], "question_id": "q1",
             "relevance_declared": True, "at": "2026-11-02T00:02:00Z", "exposed_to": "research"},
        ])
        self.assertEqual(validate_run(run), [])

    def test_free_a_projected_lexical_view_can_pair_with_current_entry(self):
        a = free_a()
        b = copy.deepcopy(a)
        b["run_id"] = "synthetic-free-view"
        b["mode_id"] = "M2_FREE_A_VIEW"
        b["index_build_id"] = "SYNTHETIC_PROJECTED_INDEX"
        self.assertEqual(validate_comparison({"intervention": "memory_only", "runs": [a, b]}), [])

    def test_free_a_projected_view_rejects_result_in_build(self):
        run = free_a()
        run["mode_id"] = "M2_FREE_A_VIEW"
        add_result(run)
        run["build"]["source_ids"].append("synthetic-result")
        self.assertRejected(run, "memory build uses additional result")

    def test_free_a_projected_view_rejects_extra_result_ranking_influence(self):
        run = free_a()
        run["mode_id"] = "M2_FREE_A_VIEW"
        run["build"]["used_withheld_results_for_index_or_ranking"] = True
        self.assertRejected(run, "build/ranking exposure")

    def test_free_a_rejects_result_trained_helper_even_without_returned_text(self):
        run = free_a()
        run["helper"]["trained_on_project_results"] = True
        run["helper"]["training_cutoff_at"] = "2026-10-01T00:00:00Z"
        self.assertRejected(run, "no result-trained recommender")

    def test_future_scientific_source_is_rejected(self):
        run = valid()
        run["sources"][0]["available_at"] = "2026-11-03T00:00:00Z"
        self.assertRejected(run, "future scientific material")

    def test_current_governance_is_not_frozen_to_old_science_cutoff(self):
        run = valid()
        run["sources"][0].update(
            knowledge_role="governance", kind="current_governance",
            available_at="2026-11-03T00:00:00Z")
        self.assertEqual(validate_run(run), [])

    def test_answer_material_cannot_enter_eligible_pool(self):
        run = valid()
        run["sources"][0]["kind"] = "reference_answer"
        self.assertRejected(run, "withheld evaluator material")

    def test_research_principal_cannot_read_answer_store(self):
        run = heldout_contract()
        run["isolation"]["answer_store_readable_by"].append("memory_builder")
        self.assertRejected(run, "can read evaluator answers")

    def test_train_and_test_dependency_overlap_is_rejected(self):
        run = heldout_contract()
        run["split_manifest"]["train_family_ids"] = [run["case_family_id"]]
        self.assertRejected(run, "dependency families overlap")

    def test_heldout_questions_cannot_guide_placement(self):
        run = heldout_contract()
        run["build"]["saw_heldout_questions"] = True
        self.assertRejected(run, "question exposure during memory build")

    def test_native_nollm_rejects_oracle_object_entry(self):
        run = valid()
        run["mode_id"] = "M5_NOLLM_NATIVE"
        run["attribution"]["entry_basis"] = "answer_object_id"
        self.assertRejected(run, "not selected from Surface")

    def test_native_selection_then_access_and_baseline_load_is_allowed(self):
        self.assertEqual(validate_run(native_run()), [])

    def test_native_only_direct_result_read_cannot_hide_as_access(self):
        run = native_run()
        run["events"][-1]["route"] = "direct"
        run["attribution"]["native_source_ids"] = []
        self.assertRejected(run, "observed fallback read")
        self.assertRejected(run, "returned claim lacks native/Access")

    def test_native_access_requires_preceding_selection(self):
        run = native_run()
        run["events"] = [run["events"][0], run["events"][-1]]
        self.assertRejected(run, "lacks a preceding native selection")

    def test_native_title_preview_does_not_support_full_returned_claim(self):
        run = native_run()
        run["events"][-1]["type"] = "title_preview"
        run["attribution"]["native_source_ids"] = []
        self.assertRejected(run, "returned claim lacks native/Access")

    def test_fallback_cannot_be_claimed_as_native_only(self):
        run = valid()
        run["mode_id"] = "M5_NOLLM_NATIVE"
        run["attribution"].update(
            entry_basis="surface_observation", label="native_only",
            fallback_source_ids=["synthetic-foundation"])
        run["events"][0]["route"] = "fallback"
        self.assertRejected(run, "credited as native-only")

    def test_unreported_fallback_event_still_blocks_native_only_credit(self):
        run = valid()
        run["mode_id"] = "M5_NOLLM_NATIVE"
        run["attribution"].update(entry_basis="surface_observation", label="native_only",
                                  fallback_source_ids=[])
        run["events"][0]["route"] = "fallback"
        self.assertRejected(run, "observed fallback read")

    def test_private_content_cannot_be_exported_to_public_artifact(self):
        run = valid()
        run["sources"][0]["classification"] = "restricted"
        run["exports"] = [{"classification": "public",
                           "contains_source_ids": ["synthetic-foundation"]}]
        self.assertRejected(run, "public export")

    def test_author_draft_cannot_be_relabelled_as_accepted(self):
        run = valid()
        run["sources"][0]["claims"] = {
            "claim1": {"status": "AUTHOR_DRAFT", "contract_digest": "synthetic-contract"}}
        run["returned_claims"] = [{"id": "claim1", "source_id": "synthetic-foundation",
                                  "status": "ACCEPTED", "contract_digest": "synthetic-contract"}]
        self.assertRejected(run, "changes declared source status")

    def test_candidate_connection_cannot_become_proved_transfer(self):
        run = valid()
        run["relations"] = [{"kind": "ANALOGY_CANDIDATE", "asserted_proved_transfer": True}]
        self.assertRejected(run, "promoted to proved transfer")

    def test_memory_only_comparison_cannot_change_reasoning_model(self):
        a, b = valid(), valid()
        b["run_id"] = "synthetic-second-arm"
        b["mode_id"] = "M3_HYBRID"
        b["main_model_revision"] = "DIFFERENT_SYNTHETIC_MAIN"
        errors = validate_comparison({"intervention": "memory_only", "runs": [a, b]})
        self.assertTrue(any("changes main_model_revision" in error for error in errors))

    def test_memory_only_compares_actual_source_versions_and_identity(self):
        for field, value in (("version", "d" * 40), ("identity", "synthetic://different-source"),
                             ("knowledge_role", "governance"), ("classification", "restricted")):
            with self.subTest(field=field):
                a, b = valid(), valid()
                b["sources"][0][field] = value
                errors = validate_comparison({"intervention": "memory_only", "runs": [a, b]})
                self.assertTrue(any("actual eligible source" in error for error in errors), errors)

    def test_memory_only_cannot_change_helper_training(self):
        a, b = valid(), valid()
        b["helper"].update(trained_on_project_results=True, training_cutoff_at="2026-10-01T00:00:00Z")
        errors = validate_comparison({"intervention": "memory_only", "runs": [a, b]})
        self.assertTrue(any("fixed helper configuration" in error for error in errors), errors)

    def test_memory_only_cannot_change_declared_exposure(self):
        a, b = valid(), valid()
        b["exposure_profile"]["allowed_lookup"] = "different_exposure_rule"
        errors = validate_comparison({"intervention": "memory_only", "runs": [a, b]})
        self.assertTrue(any("changes exposure_profile" in error for error in errors), errors)

    def test_learned_helper_is_separate_with_fixed_candidates(self):
        a, b = valid(), valid()
        a["candidate_pool_id"] = b["candidate_pool_id"] = "synthetic-same-candidates"
        b["mode_id"] = "M6_TRAINED_HELPER"
        b["helper"].update(trained_on_project_results=True, training_cutoff_at="2026-10-01T00:00:00Z",
                           training_manifest_digest="d" * 64)
        self.assertEqual(validate_comparison({"intervention": "learned_helper", "runs": [a, b]}), [])

    def test_learned_helper_cannot_change_candidates(self):
        a, b = valid(), valid()
        a["candidate_pool_id"], b["candidate_pool_id"] = "pool-a", "pool-b"
        errors = validate_comparison({"intervention": "learned_helper", "runs": [a, b]})
        self.assertTrue(any("changes candidate pool" in error for error in errors), errors)

    def test_comparison_rejects_nonobject_run_without_crashing(self):
        errors = validate_comparison({"intervention": "memory_only", "runs": [None, valid()]})
        self.assertTrue(any("run must be an object" in error for error in errors))

    def test_synthetic_fixture_cannot_claim_benchmark_winner(self):
        run = valid()
        run["claim_scope"] = "BEST_MEMORY_MODE"
        self.assertRejected(run, "cannot claim model/benchmark performance")

    def test_unknown_cost_remains_valid_and_unmeasured(self):
        run = valid()
        self.assertIsNone(run["cost"]["billed_cost"])
        self.assertEqual(validate_run(run), [])


if __name__ == "__main__":
    unittest.main()
