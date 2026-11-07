"""Behavioral checks for exact foundation coverage and Phase-A information scope."""
from __future__ import annotations

import contextlib
import io
import json
from pathlib import Path
import shutil
import sys
import tempfile
import types
import unittest
from fractions import Fraction
from unittest.mock import patch

from tools import build_em_foundation_startup as startup


class FoundationStartupTests(unittest.TestCase):
    def make_root(self):
        tmp = tempfile.TemporaryDirectory(prefix="em-foundation-")
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        for path in [*startup.SOURCE_SPECS, startup.RELATED_DEFINITION, startup.RELATED_TOOL]:
            target = root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(startup.ROOT / path, target)
        return root

    def edit_json(self, root, path, edit):
        target = root / path
        value = json.loads(target.read_text(encoding="utf-8"))
        edit(value)
        target.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def request(self, path=None, selector=None, **extra):
        return {"question_formed": True, "structure_relevant": True,
                "path": path or startup.RELATED_DEFINITION,
                "selector": selector or "2. Positive weighted branch carrier", **extra}

    def test_mandatory_closure_and_normative_values_are_exact(self):
        packages, report = startup.build()
        self.assertTrue(report["complete"])
        self.assertFalse(report["unclassified_pointers"])
        self.assertEqual(set(startup.foundation_sources(startup.ROOT)), set(startup.SOURCE_SPECS))
        for profile, package in packages.items():
            with self.subTest(profile=profile):
                self.assertEqual(package["kind"], "generated_projection")
                self.assertEqual(set(startup._source_blobs(package)), set(startup.SOURCE_SPECS))
                for row in package["normative_payload"]:
                    source = json.loads((startup.ROOT / row["path"]).read_text(encoding="utf-8"))
                    for pointer, value in row["values"].items():
                        self.assertEqual(value, source[pointer[1:]])
                for row in package["source_files"]:
                    self.assertEqual(row["blob"], startup.git_blob((startup.ROOT / row["path"]).read_bytes()))

    def test_mandatory_cycles_deduplicate_and_conditional_address_is_not_preloaded(self):
        root = self.make_root()
        self.edit_json(root, startup.P000, lambda value: value["mandatory_companion_contracts"].append({
            "path": startup.P000, "load_policy": "MANDATORY_WITH_THIS_WORLD_CONTRACT"}))
        sources = startup.foundation_sources(root)
        self.assertEqual(len(sources), 5)
        self.assertNotIn("coordinate_address_contract.json", sources)
        self.assertEqual(len(startup.build(root)[0]["free_phase_a"]["source_files"]), 5)

    def test_unclassified_mandatory_edge_is_an_explicit_build_gap(self):
        root = self.make_root()
        self.edit_json(root, startup.P000, lambda value: value["mandatory_companion_contracts"].append({
            "path": "definitions/NEW_REQUIRED.json", "load_policy": "MANDATORY_WITH_THIS_WORLD_CONTRACT"}))
        with self.assertRaisesRegex(startup.ProjectionError, "UNCLASSIFIED_FOUNDATION_SOURCE"):
            startup.build(root)

    def test_phase_a_omits_documentary_catalogs_and_conditional_menu(self):
        root = self.make_root()
        self.edit_json(root, startup.WEIGHTED, lambda value: value.update(
            theorem_ledger="B_ONLY_CATALOG_SENTINEL", tool_method_id="B_ONLY_TOOL_SENTINEL"))
        packages, report = startup.build(root)
        free = packages["free_phase_a"]
        text = startup.encoded(free).decode()
        self.assertNotIn("B_ONLY_CATALOG_SENTINEL", text)
        self.assertNotIn("B_ONLY_TOOL_SENTINEL", text)
        self.assertNotIn("documentary_pointers", text)
        self.assertNotIn("unclassified_pointers", text)
        self.assertNotIn("conditional_routes", free)
        self.assertNotIn(startup.RELATED_DEFINITION, text)
        self.assertIn("/theorem_ledger", report["documentary_pointers"][startup.WEIGHTED])
        self.assertFalse(free["conditional_lookup"]["candidate_freeze_required_for_this_lookup"])

    def test_current_mandatory_commitments_are_never_shortened_for_phase_a(self):
        root = self.make_root()
        self.edit_json(root, startup.WEIGHTED, lambda value: value["commitments"].append(
            "REQUIRED_TYPED_CONDITION_WITH_EXCEPTION_SENTINEL"))
        packages, _ = startup.build(root)
        for package in packages.values():
            row = next(row for row in package["normative_payload"] if row["path"] == startup.WEIGHTED)
            self.assertIn("REQUIRED_TYPED_CONDITION_WITH_EXCEPTION_SENTINEL", row["values"]["/commitments"])

    def test_unclassified_source_field_keeps_outputs_and_safe_error_has_no_catalog(self):
        root = self.make_root()
        startup.write_outputs(root)
        original = {profile: (root / path).read_bytes() for profile, path in startup.OUTPUTS.items()}
        self.edit_json(root, startup.WEIGHTED, lambda value: value.update(
            B_ONLY_UNKNOWN_FIELD="B_ONLY_UNKNOWN_VALUE"))
        with self.assertRaisesRegex(startup.ProjectionError, "FOUNDATION_MAPPING_INCOMPLETE"):
            startup.write_outputs(root)
        for profile, path in startup.OUTPUTS.items():
            self.assertEqual((root / path).read_bytes(), original[profile])
        result = startup.read_projection(root, "free_phase_a")
        self.assertEqual(result["status"], "UNAVAILABLE")
        self.assertNotIn("B_ONLY", json.dumps(result))
        self.assertNotIn("details", result)

    def test_missing_or_malformed_source_preserves_previous_outputs(self):
        for fault in ("missing", "malformed"):
            with self.subTest(fault=fault):
                root = self.make_root()
                startup.write_outputs(root)
                original = {path: (root / path).read_bytes() for path in startup.OUTPUTS.values()}
                source = root / startup.RESIDUAL
                if fault == "missing":
                    source.unlink()
                else:
                    source.write_text('{"B_ONLY_BROKEN_SOURCE":', encoding="utf-8")
                with self.assertRaises(startup.ProjectionError):
                    startup.write_outputs(root)
                for path, value in original.items():
                    self.assertEqual((root / path).read_bytes(), value)
                self.assertNotIn("B_ONLY", json.dumps(startup.read_projection(root, "free_phase_a")))

    def test_documentary_type_change_is_not_silently_omitted(self):
        root = self.make_root()
        self.edit_json(root, startup.WEIGHTED, lambda value: value.update(
            theorem_ledger={"new_required_condition": True}))
        with self.assertRaisesRegex(startup.ProjectionError, "MAPPED_FIELD_TYPE_CHANGED"):
            startup.build(root)

    def test_invalid_relation_or_phase_rule_stays_a_bounded_phase_a_failure(self):
        mutations = (
            (startup.P000, lambda value: value["mandatory_companion_contracts"][0].update(
                load_policy=["B_ONLY_INVALID_POLICY"])),
            (startup.WEIGHTED, lambda value: value.update(
                phase_a_anti_anchoring={"rule": ["B_ONLY_INVALID_RULE"]})),
        )
        for path, mutation in mutations:
            with self.subTest(path=path):
                root = self.make_root()
                self.edit_json(root, path, mutation)
                result = startup.read_projection(root, "free_phase_a")
                self.assertEqual(result["status"], "UNAVAILABLE")
                self.assertNotIn("B_ONLY", json.dumps(result))
                self.assertNotIn("details", result)

    def test_cache_mismatch_uses_exact_safe_reconstruction(self):
        root = self.make_root()
        startup.write_outputs(root)
        self.edit_json(root, startup.OUTPUTS["free_phase_a"], lambda value: value.update(
            unsafe_catalog="B_ONLY_CORRUPT_CACHE"))
        result = startup.read_projection(root, "free_phase_a")
        self.assertEqual(result["status"], "READY")
        self.assertEqual(result["mode"], "EXACT_ROLE_SAFE_RECONSTRUCTION")
        self.assertNotIn("B_ONLY_CORRUPT_CACHE", json.dumps(result))

    def test_scientific_pins_do_not_follow_current_source_changes(self):
        root = self.make_root()
        startup.write_outputs(root)
        pins = startup._source_blobs(startup.build(root)[0]["free_phase_a"])
        self.edit_json(root, startup.RESIDUAL, lambda value: value["invariants"].append("NEW_TYPED_VALUE"))
        result = startup.read_projection(root, "free_phase_a", pins)
        self.assertEqual(result["status"], "UNAVAILABLE")
        self.assertEqual(result["code"], "SCIENTIFIC_INPUT_MISMATCH")
        self.assertNotIn("NEW_TYPED_VALUE", json.dumps(result))

    def test_determinism_and_check_is_read_only(self):
        root = self.make_root()
        startup.write_outputs(root)
        first = {path: (root / path).read_bytes() for path in startup.OUTPUTS.values()}
        self.assertEqual(startup.check_outputs(root)["status"], "PASS")
        (root / startup.OUTPUTS["ordinary_research"]).write_text("stale\n", encoding="utf-8")
        result = startup.check_outputs(root)
        self.assertEqual(result["status"], "MISMATCH")
        self.assertEqual((root / startup.OUTPUTS["ordinary_research"]).read_text(), "stale\n")
        startup.write_outputs(root)
        self.assertEqual(first, {path: (root / path).read_bytes() for path in startup.OUTPUTS.values()})

    def test_formed_relevant_unfrozen_problem_reads_exact_definition(self):
        result = startup.read_related(startup.ROOT, self.request(candidate_frozen=False))
        self.assertEqual(result["status"], "READY")
        self.assertFalse(result["phase_transition"])
        self.assertIn("## 2. Positive weighted branch carrier", result["text"])
        self.assertNotIn("## 3.", result["text"])
        self.assertNotIn("Canonical evidence and executable surfaces", result["text"])

    def test_unformed_or_irrelevant_problem_does_not_open_conditional_content(self):
        for facts in ({"question_formed": False}, {"structure_relevant": False}):
            with self.subTest(facts=facts):
                result = startup.read_related(startup.ROOT, self.request(**facts))
                self.assertEqual(result["status"], "NOT_TRIGGERED")
                self.assertNotIn("text", result)

    def test_catalog_or_malformed_selector_is_not_a_phase_a_read(self):
        for request in (self.request(selector="12. Canonical evidence and executable surfaces"),
                        self.request(path="B_ONLY_UNKNOWN_SOURCE", selector="B_ONLY_NAME"),
                        self.request(selector=["not a scalar"])):
            with self.subTest(request=request):
                result = startup.read_related(startup.ROOT, request)
                self.assertEqual(result["status"], "UNAVAILABLE")
                self.assertNotIn("B_ONLY", json.dumps(result))
                self.assertNotIn("text", result)

    def test_ambiguous_or_unclosed_definition_does_not_expand_to_catalog(self):
        for body in (
            "## 2. Positive weighted branch carrier\nSafe definition.\n```\n"
            "## 12. Canonical evidence and executable surfaces\nB_ONLY_CATALOG\n",
            "## 2. Positive weighted branch carrier\nFirst definition.\n"
            "## 2. Positive weighted branch carrier\nB_ONLY_DUPLICATE\n",
        ):
            root = self.make_root()
            (root / startup.RELATED_DEFINITION).write_text(body, encoding="utf-8")
            result = startup.read_related(root, self.request())
            self.assertEqual(result["status"], "UNAVAILABLE")
            self.assertNotIn("text", result)
            self.assertNotIn("B_ONLY", json.dumps(result))

    def test_relevant_tool_read_includes_required_source_dependencies(self):
        result = startup.read_related(startup.ROOT, self.request(
            path=startup.RELATED_TOOL, selector="cwm_from_positive_weights", candidate_frozen=False))
        self.assertEqual(result["status"], "READY")
        self.assertIn("class CWMState", result["text"])
        self.assertIn("def _positive_fraction", result["text"])
        self.assertNotIn("class OneStateRecurrentCWM", result["text"])
        module = types.ModuleType("em_related_fragment_fixture")
        with patch.dict(sys.modules, {module.__name__: module}):
            exec(compile(result["text"], "<exact-related-fragment>", "exec"), module.__dict__)
            value = module.cwm_from_positive_weights([Fraction(1), Fraction(2)])
        self.assertEqual((value.count, value.total, value.dominant), (2, Fraction(3), Fraction(2)))

    def test_lookup_source_pin_and_selector_diagnostics_are_safe(self):
        result = startup.read_related(startup.ROOT, self.request(source_blob="0" * 40))
        self.assertEqual(result["status"], "UNAVAILABLE")
        self.assertEqual(result["code"], "SCIENTIFIC_INPUT_MISMATCH")
        self.assertNotIn("text", result)

    def test_phase_a_cli_error_never_emits_build_coverage(self):
        root = self.make_root()
        self.edit_json(root, startup.WEIGHTED, lambda value: value.update(B_ONLY_SECRET_FIELD="B_ONLY_SECRET_VALUE"))
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            status = startup.main(["--root", str(root), "--read", "free_phase_a"])
        self.assertEqual(status, 2)
        self.assertEqual(json.loads(output.getvalue())["status"], "UNAVAILABLE")
        self.assertNotIn("B_ONLY", output.getvalue())

    def test_phase_a_entry_chain_routes_specific_comparison_catalogs_only_to_phase_b(self):
        paths = [
            "research_roles/EM_FREE_RESEARCHER_ROLE.md",
            "research_roles/EM_FREE_RESEARCHER_ROLE.zh-CN.md",
            "research_roles/EM_FREE_RESEARCHER_ANTI_ANCHORING_PROTOCOL.md",
            "research_roles/EM_FREE_RESEARCHER_ANTI_ANCHORING_PROTOCOL.zh-CN.md",
            "research_roles/EM_FREE_RESEARCHER_PHASE_A_INTEGRITY_SHELL.md",
            "definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md",
            "definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.zh-CN.md",
            startup.OUTPUTS["free_phase_a"],
        ]
        phase_b = (startup.ROOT / "research_roles/EM_FREE_PHASE_B_REFERENCE.en.md").read_text(encoding="utf-8")
        catalogs = ("enterprise_toolbox_registry.json", "research_method_inventory.json",
                    "t0.weighted_brc_cwm", "ENTERPRISE_BRC_WEIGHTED_LOG_THEOREM_LEDGER_20260902.json")
        for catalog in catalogs:
            self.assertIn(catalog, phase_b)
        for path in paths:
            with self.subTest(path=path):
                content = (startup.ROOT / path).read_text(encoding="utf-8")
                for catalog in catalogs:
                    self.assertNotIn(catalog, content)


if __name__ == "__main__":
    unittest.main()
