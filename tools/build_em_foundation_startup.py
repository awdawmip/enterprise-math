#!/usr/bin/env python3
"""Build exact, role-scoped reading projections of the EM foundation sources.

This is an offline document generator, not a research or admission service.
Classification is deliberately explicit: a new source field needs maintenance
review before a newly generated package can claim complete coverage. A failure
leaves the canonical sources and existing generated files untouched.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = "em-foundation-startup-projection/v1"
GENERATOR_VERSION = "1.0.0"
MAPPING_VERSION = "2026-11-07.1"
P000 = "p000_reality_foundation.json"
HEARTBEAT = "definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json"
RESIDUAL = "definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json"
JOINT = "definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json"
WEIGHTED = "definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json"
OUTPUTS = {
    "ordinary_research": "definitions/EM_FOUNDATION_STARTUP.json",
    "free_phase_a": "definitions/EM_FREE_A_FOUNDATION_STARTUP.json",
}


def _keys(text: str) -> tuple[str, ...]:
    return tuple(text.split())


# Whole values under these reviewed fields are copied, including nested
# conditions, exceptions and new nested values. Nothing is selected by keywords.
# Documentary fields contain source locators, not additional mandatory edges.
SOURCE_SPECS = {
    P000: {
        "schema": "ENTERPRISE_MATH_P000_REALITY_FOUNDATION_V5",
        "normative": _keys("""
            status priority_class authority_kind scope load_policy
            mandatory_companion_contracts axioms derived_foundation_state
            typed_semantics machine_invariants research_semantics conflict_policy
            hard_errors coordinate_address_contract coordinate_address_scope
            world_identity direct_user_research_constraint
        """),
        "metadata": _keys("schema effective research_constraint_updated"),
        "documentary": _keys("canonical_human_foundations"),
        "conditional": (),
    },
    HEARTBEAT: {
        "schema": "ENTERPRISE_MATH_HEARTBEAT_WORLD_CONTRACT_V1",
        "normative": _keys("""
            status authority_kind scope world_id world_name_zh world_name_en
            total_dimension spatial_dimension time_dimension spatial_coordinate_system
            spatial_model native_terminology native_positive_axes
            signed_primitive_direction_count native_axis_relation native_right_angle_degrees
            raw_spatial_fields final_cell_address event_layout time_role time_is_spatial_axis
            scale_is_complete_time phase_is_complete_time space_return_is_event_return
            distinguished_global_spatial_origin extra_state_is_extra_spatial_dimension
            fixed_heartbeat_program research_examples_are_world_axioms
            physical_time_calibration_claimed heartbeat_snapshot_semantics research_position
            invariants load_policy native_plane_exists all_research_basis time_modeling
            research_representation_scope
        """),
        "metadata": _keys("schema effective research_constraint_updated"),
        "documentary": _keys("canonical_sources human_definition human_definition_en"),
        "conditional": (),
    },
    RESIDUAL: {
        "schema": "ENTERPRISE_MATH_RESIDUAL_FIDELITY_V1",
        "normative": _keys("""
            status authority_kind position_id name_zh name_en dynamics_name_zh
            epistemic_status foundation state_semantics residual_classification
            compression cancellation research_success compatibility invariants
        """),
        "metadata": _keys("schema effective"),
        "documentary": _keys("human_definitions"),
        "conditional": (),
    },
    JOINT: {
        "schema": "ENTERPRISE_MATH_JOINT_RELATION_OBSERVER_PRESERVATION_V2",
        "normative": _keys("""
            status priority_class authority_kind scope load_policy canonical_statements_zh
            canonical_statement_en semantic_status road_pit_interpretation machine_invariants
            redundancy_certification_protocol observer_safety_contract arithmetic_specialization
            brc_binding anti_misread precedence
        """),
        "metadata": _keys("schema effective project"),
        "documentary": (),
        "conditional": (),
    },
    WEIGHTED: {
        "schema": "ENTERPRISE_MATH_WEIGHTED_BRC_GLOBAL_SUBSTRATE_V1",
        "normative": _keys("status scope authority purpose commitments phase_a_anti_anchoring"),
        "metadata": _keys("schema effective"),
        "documentary": _keys("""
            theorem_ledger theorem_ledger_addenda tool_method_id tool_method_addenda
            tool_module tool_module_addenda
        """),
        "conditional": _keys("""
            detailed_foundation finite_recurrent_foundation recurrent_interaction_foundation
            recurrent_port_foundation universal_histogram_foundation
            critical_degeneracy_foundation critical_orbit_foundation
            critical_ratio_jet_foundation reducible_critical_jet_foundation
            newton_recursion_foundation newton_handoff_resonance_foundation
            newton_fiber_quotient_foundation newton_observer_lattice_foundation
            newton_schedule_strata_foundation newton_selector_chambers_foundation
            newton_quadratic_selector_foundation
        """),
    },
}

# These are the explicit source edge semantics, not guesses from link names.
MANDATORY_LOAD_POLICIES = {
    "MANDATORY_AFTER_P000_AND_BEFORE_ANY_INFORMATION_REDUCING_PROJECTION_OR_FACTOR_COLLAPSE",
    "MANDATORY_WITH_P000_FOR_ALL_ENTERPRISE_MATH_RESEARCH",
    "MANDATORY_WITH_THIS_WORLD_CONTRACT",
}
CONDITIONAL_LOAD_POLICIES = {"BEFORE_INTERPRETING_OR_SERIALIZING_FINAL_CELL_ADDRESSES"}
DOCUMENTARY_LIST_FIELDS = {
    "canonical_human_foundations", "canonical_sources", "human_definitions",
    "theorem_ledger_addenda", "tool_method_addenda", "tool_module_addenda",
}


class ProjectionError(ValueError):
    def __init__(self, code: str, details: Any = None):
        self.code = code
        self.details = details
        super().__init__(code)


def git_blob(raw: bytes) -> str:
    return hashlib.sha1(f"blob {len(raw)}\0".encode("ascii") + raw).hexdigest()


def encoded(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
                       allow_nan=False) + "\n").encode("utf-8")


def _read_source(root: Path, path: str) -> tuple[bytes, dict[str, Any]]:
    try:
        raw = (root / path).read_bytes()
        data = json.loads(raw)
    except (OSError, ValueError, UnicodeError) as exc:
        raise ProjectionError("FOUNDATION_SOURCE_UNAVAILABLE", {"path": path}) from exc
    if not isinstance(data, dict):
        raise ProjectionError("EXPECTED_FOUNDATION_OBJECT", {"path": path})
    return raw, data


def _mandatory_edges(path: str, value: dict[str, Any]) -> list[str]:
    rows = value.get("mandatory_companion_contracts", [])
    if not isinstance(rows, list) or any(not isinstance(x, dict) for x in rows):
        raise ProjectionError("INVALID_MANDATORY_RELATION", {"path": path})
    rows = list(rows)
    if path == HEARTBEAT:
        position = value.get("research_position")
        if not isinstance(position, dict):
            raise ProjectionError("INVALID_MANDATORY_RELATION", {"path": path})
        rows.append({"path": position.get("machine_contract"),
                     "load_policy": position.get("load_policy")})
    edges: list[str] = []
    for row in rows:
        policy, target = row.get("load_policy"), row.get("path")
        if not isinstance(policy, str):
            raise ProjectionError("UNCLASSIFIED_MANDATORY_RELATION", {"path": path, "relation": row})
        if policy in CONDITIONAL_LOAD_POLICIES:
            continue
        if policy not in MANDATORY_LOAD_POLICIES or not isinstance(target, str):
            raise ProjectionError("UNCLASSIFIED_MANDATORY_RELATION", {"path": path, "relation": row})
        edges.append(target)
    return edges


def foundation_sources(root: Path) -> dict[str, tuple[bytes, dict[str, Any]]]:
    """Resolve explicit mandatory edges once, with cycle deduplication."""
    pending = [P000, WEIGHTED]
    sources: dict[str, tuple[bytes, dict[str, Any]]] = {}
    while pending:
        path = pending.pop(0)
        if path in sources:
            continue
        if path not in SOURCE_SPECS:
            raise ProjectionError("UNCLASSIFIED_FOUNDATION_SOURCE", {"path": path})
        raw, value = _read_source(root, path)
        sources[path] = raw, value
        pending.extend(_mandatory_edges(path, value))
    if set(sources) != set(SOURCE_SPECS):
        raise ProjectionError("MANDATORY_CLOSURE_CHANGED", {"paths": sorted(sources)})
    return dict(sorted(sources.items()))


def _coverage(sources: dict[str, tuple[bytes, dict[str, Any]]]) -> dict[str, Any]:
    report: dict[str, Any] = {kind + "_pointers": {} for kind in
                             ("normative", "conditional", "documentary", "metadata")}
    report["unclassified_pointers"] = {}
    report["missing_pointers"] = {}
    for path, (_, value) in sources.items():
        spec = SOURCE_SPECS[path]
        if value.get("schema") != spec["schema"]:
            raise ProjectionError("FOUNDATION_SCHEMA_CHANGED", {"path": path})
        classified: set[str] = set()
        for kind in ("normative", "conditional", "documentary", "metadata"):
            keys = set(spec[kind])
            if classified & keys:
                raise ProjectionError("OVERLAPPING_FIELD_MAPPING", {"path": path})
            classified |= keys
            report[kind + "_pointers"][path] = ["/" + key for key in sorted(keys)]
            if kind != "normative":
                for key in keys & set(value):
                    item = value[key]
                    valid = (isinstance(item, list) and all(isinstance(x, str) for x in item)
                             if key in DOCUMENTARY_LIST_FIELDS else isinstance(item, str))
                    if not valid:
                        raise ProjectionError("MAPPED_FIELD_TYPE_CHANGED", {"path": path, "pointer": "/" + key})
        unknown, missing = set(value) - classified, classified - set(value)
        if unknown:
            report["unclassified_pointers"][path] = ["/" + key for key in sorted(unknown)]
        if missing:
            report["missing_pointers"][path] = ["/" + key for key in sorted(missing)]
    report["complete"] = not (report["unclassified_pointers"] or report["missing_pointers"])
    return report


def build(root: Path = ROOT) -> tuple[dict[str, dict[str, Any]], dict[str, Any]]:
    sources = foundation_sources(root)
    coverage = _coverage(sources)
    if not coverage["complete"]:
        raise ProjectionError("FOUNDATION_MAPPING_INCOMPLETE", coverage)
    source_files, normative_payload = [], []
    for path, (raw, value) in sources.items():
        spec = SOURCE_SPECS[path]
        source_files.append({"path": path, "blob": git_blob(raw),
                             "metadata": {key: value[key] for key in spec["metadata"]}})
        normative_payload.append({"path": path,
                                  "values": {"/" + key: value[key] for key in spec["normative"]}})

    common = {
        "schema": SCHEMA,
        "kind": "generated_projection",
        "canonical_repo": "awdawmip/enterprise-math",
        "generator_version": GENERATOR_VERSION,
        "mapping_version": MAPPING_VERSION,
        "source_files": source_files,
        "normative_payload": normative_payload,
        "input_scope": "SOURCE_FOUNDATION_ONLY_CURRENT_CONTROL_RULES_READ_SEPARATELY",
    }
    phase_rule = sources[WEIGHTED][1]["phase_a_anti_anchoring"]
    if not isinstance(phase_rule, dict) or not isinstance(phase_rule.get("rule"), str):
        raise ProjectionError("MAPPED_FIELD_TYPE_CHANGED", {"path": WEIGHTED,
                                                          "pointer": "/phase_a_anti_anchoring/rule"})
    condition = phase_rule["rule"]
    ordinary = {
        **common,
        "coverage": {"profile": "ordinary_research", "complete": True},
        "conditional_routes": [{
            "path": WEIGHTED,
            "condition_pointer": "/phase_a_anti_anchoring/rule",
            "condition": condition,
            "values": {"/" + key: sources[WEIGHTED][1][key]
                       for key in SOURCE_SPECS[WEIGHTED]["conditional"]},
        }],
        "fallback": "EXACT_CANONICAL_SOURCES_AT_REQUIRED_SCIENTIFIC_VERSIONS",
    }
    free = {
        **common,
        "coverage": {"profile": "free_phase_a", "complete": True},
        "conditional_lookup": {
            "condition": condition,
            "selection": "EXACT_DEFINITION_OR_TOOL_FOR_THE_ALREADY_SELF_GENERATED_RELEVANT_PROBLEM",
            "reader": "tools/build_em_foundation_startup.py --lookup REQUEST.json",
            "availability": "REGISTERED_EXACT_SELECTORS_OR_EXISTING_STAGE_APPROPRIATE_EXACT_SOURCE_READ",
            "candidate_freeze_required_for_this_lookup": False,
            "current_result_comparison_and_dedup": "PHASE_B_AFTER_CANDIDATE_FREEZE",
        },
        "fallback": "SAME_SCIENTIFIC_INPUT_ROLE_SAFE_PACKAGE_OR_EXACT_ROLE_SAFE_SOURCE_READING",
        "exposure": "PRESERVE_ACTUAL_SOURCE_USE_AND_EXPOSURE; THIS_PACKAGE_DOES_NOT_CERTIFY_CLEAN_CONTEXT",
    }
    return {"ordinary_research": ordinary, "free_phase_a": free}, coverage


def _source_blobs(package: dict[str, Any]) -> dict[str, str]:
    return {item["path"]: item["blob"] for item in package["source_files"]}


def read_projection(root: Path = ROOT, profile: str = "ordinary_research",
                    scientific_blobs: dict[str, str] | None = None) -> dict[str, Any]:
    """Return a checked package or an in-memory exact role-safe reconstruction.

    The source checkout is the requested scientific input. A caller supplying
    explicit pins must match that input; current control rules never rebase it.
    No failure falls back to dumping the mixed raw Weighted-BRC document.
    """
    if profile not in OUTPUTS:
        raise ProjectionError("UNKNOWN_READING_PROFILE")
    try:
        expected = build(root)[0][profile]
        if scientific_blobs is not None and _source_blobs(expected) != scientific_blobs:
            raise ProjectionError("SCIENTIFIC_INPUT_MISMATCH")
        try:
            cached = json.loads((root / OUTPUTS[profile]).read_text(encoding="utf-8"))
        except (OSError, ValueError, UnicodeError):
            cached = None
        if cached == expected:
            return {"status": "READY", "mode": "GENERATED_PACKAGE", "package": cached}
        return {"status": "READY", "mode": "EXACT_ROLE_SAFE_RECONSTRUCTION", "package": expected}
    except ProjectionError as exc:
        # Missing/unclassified fields can contain B-only names. Keep the detail
        # on the maintainer build path, never in a Phase-A error or fallback.
        result = {"status": "UNAVAILABLE", "profile": profile, "code": exc.code,
                  "fallback": "USE_MATCHING_VALID_ROLE_SAFE_SCIENTIFIC_INPUT_OR_EXACT_ROLE_SAFE_SOURCE_READING",
                  "independent_work": "CONTINUE_WORK_NOT_DEPENDING_ON_THIS_READING"}
        if profile != "free_phase_a":
            result["details"] = exc.details
        return result


# This is a deliberately small positive-case adapter, not an exhaustive tool
# catalog. Other exact relevant sources retain their normal authorized reader.
RELATED_DEFINITION = "definitions/ENTERPRISE_BRC_WEIGHTED_LOG_FOUNDATION_20260902.md"
RELATED_HEADINGS = {
    "2. Positive weighted branch carrier",
    "3. Exact positive-path realizability",
    "4. Boolean support projection",
    "5. Effective multiplicity and logarithmic surplus",
    "6. Deterministic degeneration",
    "7. All-prefix safe weighted quotient",
    "8. Projective / gauge-compensated quotient",
    "9. One-state recurrent positive branches",
    "10. Global hard boundaries",
}
RELATED_TOOL = "src/enterprise_math/brc_weighted.py"
RELATED_TOOL_SYMBOLS = {"CWMState", "cwm_from_positive_weights", "is_positive_path_realizable"}


def _markdown_section(text: str, heading: str) -> str:
    lines = text.splitlines(keepends=True)
    headings: list[tuple[int, int, str]] = []
    fence_char, fence_length = None, 0
    for index, line in enumerate(lines):
        fence = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line.rstrip("\r\n"))
        if fence_char:
            if (fence and fence.group(1)[0] == fence_char
                    and len(fence.group(1)) >= fence_length and not fence.group(2).strip()):
                fence_char = None
            continue
        if fence:
            fence_char, fence_length = fence.group(1)[0], len(fence.group(1))
            continue
        match = re.match(r"^(#{1,6}) (.+?)\s*$", line)
        if not match:
            continue
        headings.append((index, len(match.group(1)), match.group(2)))
    if fence_char:
        raise ProjectionError("EXACT_SOURCE_STRUCTURE_UNSUPPORTED")
    matches = [(index, depth) for index, depth, name in headings if name == heading]
    if not matches:
        raise ProjectionError("EXACT_SELECTOR_NOT_FOUND")
    if len(matches) != 1:
        raise ProjectionError("EXACT_SELECTOR_AMBIGUOUS")
    start, depth = matches[0]
    stop = next((index for index, level, _ in headings if index > start and level <= depth), len(lines))
    return "".join(lines[start:stop]).rstrip() + "\n"


def _python_fragment(text: str, symbol: str) -> str:
    """Select the requested definition and its same-module static dependencies."""
    tree = ast.parse(text)
    providers: dict[str, ast.stmt] = {}
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            providers[node.name] = node
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                providers[alias.asname or alias.name.split(".")[0]] = node
        elif isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                if isinstance(target, ast.Name):
                    providers[target.id] = node
    if symbol not in providers:
        raise ProjectionError("EXACT_SELECTOR_NOT_FOUND")
    selected: dict[int, ast.stmt] = {}
    pending = [providers[symbol]]
    pending += [node for node in tree.body if isinstance(node, ast.ImportFrom)
                and node.module == "__future__"]
    while pending:
        node = pending.pop()
        if node.lineno in selected:
            continue
        selected[node.lineno] = node
        pending.extend(providers[name.id] for name in ast.walk(node)
                       if isinstance(name, ast.Name) and isinstance(name.ctx, ast.Load)
                       and name.id in providers)
    lines = text.splitlines(keepends=True)
    chunks = []
    for node in sorted(selected.values(), key=lambda item: item.lineno):
        decorators = getattr(node, "decorator_list", [])
        first = min([node.lineno] + [item.lineno for item in decorators])
        chunks.append("".join(lines[first - 1:node.end_lineno]).rstrip())
    return "\n\n".join(chunks) + "\n"


def read_related(root: Path, request: dict[str, Any]) -> dict[str, Any]:
    """Read one precise surface after the caller's actual question/typing choice.

    These supplied facts route the read; this tool cannot independently certify
    a question's origin. It does not freeze a candidate or confer novelty.
    """
    if (request.get("question_formed") is not True
            or request.get("structure_relevant") is not True):
        return {"status": "NOT_TRIGGERED", "profile": "free_phase_a",
                "code": "SELF_GENERATED_RELEVANT_PROBLEM_REQUIRED"}
    path, selector = request.get("path"), request.get("selector")
    if not isinstance(path, str) or not isinstance(selector, str):
        return {"status": "UNAVAILABLE", "profile": "free_phase_a", "code": "INVALID_EXACT_SELECTOR"}
    supported = ((path == RELATED_DEFINITION and selector in RELATED_HEADINGS)
                 or (path == RELATED_TOOL and selector in RELATED_TOOL_SYMBOLS))
    if not supported:
        return {"status": "UNAVAILABLE", "profile": "free_phase_a",
                "code": "EXACT_SELECTOR_NOT_REGISTERED",
                "fallback": "EXISTING_STAGE_APPROPRIATE_EXACT_SOURCE_READER"}
    try:
        raw = (root / path).read_bytes()
        if request.get("source_blob") is not None and request["source_blob"] != git_blob(raw):
            raise ProjectionError("SCIENTIFIC_INPUT_MISMATCH")
        text = raw.decode("utf-8")
        fragment = (_markdown_section(text, selector) if path == RELATED_DEFINITION
                    else _python_fragment(text, selector))
    except (OSError, UnicodeError, ValueError, SyntaxError) as exc:
        return {"status": "UNAVAILABLE", "profile": "free_phase_a",
                "code": exc.code if isinstance(exc, ProjectionError) else "EXACT_SOURCE_UNAVAILABLE"}
    return {"status": "READY", "profile": "free_phase_a", "phase_transition": False,
            "source": {"path": path, "blob": git_blob(raw), "selector": selector},
            "condition_evidence": "CALLER_SUPPLIED_QUESTION_AND_RELEVANCE_NOT_INDEPENDENTLY_CERTIFIED",
            "text": fragment}


def write_outputs(root: Path = ROOT) -> dict[str, Any]:
    packages, report = build(root)  # Validate all inputs before touching either file.
    data = {profile: encoded(value) for profile, value in packages.items()}
    for profile, raw in data.items():
        path = root / OUTPUTS[profile]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
    return {"status": "WRITTEN", "bytes": {key: len(value) for key, value in data.items()},
            "coverage": report}


def check_outputs(root: Path = ROOT) -> dict[str, Any]:
    packages, report = build(root)
    mismatched = [OUTPUTS[profile] for profile, value in packages.items()
                  if not (root / OUTPUTS[profile]).is_file()
                  or (root / OUTPUTS[profile]).read_bytes() != encoded(value)]
    return {"status": "MISMATCH" if mismatched else "PASS", "mismatched": mismatched,
            "bytes": {key: len(encoded(value)) for key, value in packages.items()},
            "coverage": report}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, epilog=(
        "Exit 0: success/ready; 1: generated-file mismatch; 2: source/input error or unavailable read. "
        "Build diagnostics are maintenance output, not Phase-A startup input."))
    actions = parser.add_mutually_exclusive_group(required=True)
    actions.add_argument("--write", action="store_true", help="validate inputs and write both packages")
    actions.add_argument("--check", action="store_true", help="compare deterministic outputs without writing")
    actions.add_argument("--read", choices=tuple(OUTPUTS), help="return only a role-appropriate read result")
    actions.add_argument("--lookup", type=Path, help="one already-relevant exact definition/tool request JSON")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--scientific-inputs", type=Path,
                        help="optional JSON path-to-blob mapping for --read; never update frozen pins")
    parser.add_argument("--report", type=Path, help="write full build coverage for maintainers only")
    args = parser.parse_args(argv)
    if args.report and (args.read or args.lookup):
        parser.error("--report is maintenance-only and cannot accompany a role read")
    if args.scientific_inputs and not args.read:
        parser.error("--scientific-inputs requires --read")
    try:
        if args.lookup:
            request = json.loads(args.lookup.read_text(encoding="utf-8"))
            if not isinstance(request, dict):
                raise ProjectionError("EXPECTED_LOOKUP_OBJECT")
            result = read_related(args.root, request)
        elif args.read:
            pins = (json.loads(args.scientific_inputs.read_text(encoding="utf-8"))
                    if args.scientific_inputs else None)
            if pins is not None and (not isinstance(pins, dict)
                                     or any(not isinstance(k, str) or not isinstance(v, str)
                                            for k, v in pins.items())):
                raise ProjectionError("EXPECTED_SCIENTIFIC_INPUT_MAP")
            result = read_projection(args.root, args.read, pins)
        else:
            result = write_outputs(args.root) if args.write else check_outputs(args.root)
            if args.report:
                args.report.write_bytes(encoded(result["coverage"]))
            # Normal maintenance success need not dump the full field map.
            result = {key: value for key, value in result.items() if key != "coverage"}
    except (OSError, ValueError, UnicodeError) as exc:
        result = {"status": "ERROR", "code": exc.code if isinstance(exc, ProjectionError)
                  else "INPUT_OR_OUTPUT_ERROR"}
        if not (args.read == "free_phase_a" or args.lookup):
            result["details"] = exc.details if isinstance(exc, ProjectionError) else str(exc)
        print(encoded(result).decode("utf-8"), end="")
        return 2
    print(encoded(result).decode("utf-8"), end="")
    if result["status"] == "MISMATCH":
        return 1
    return 0 if result["status"] in {"PASS", "WRITTEN", "READY", "NOT_TRIGGERED"} else 2


if __name__ == "__main__":
    sys.exit(main())
