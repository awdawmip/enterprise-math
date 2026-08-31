#!/usr/bin/env python3
"""Deterministic checker for Enterprise Math native-semantics claim ledgers.

The checker is intentionally semantic-typing-first:
* text patterns only trigger completeness warnings;
* verdicts are computed from the declared base plus the typed dependency DAG;
* task-relative base declarations override default hazard strata;
* promotion certificates must match the semantic strength actually claimed.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

STRATA = {"I0", "N0", "N1", "N2", "N3"}
CLAIM_CLASSES = {"NATIVE", "CONDITIONAL", "READOUT", "CONTINUUM"}
VERDICTS = {"NATIVE_ADMISSIBLE", "CONDITIONAL_DERIVED", "READOUT_ONLY", "CONTINUUM_ONLY", "SEMANTIC_MISMATCH", "UNRESOLVED"}

KIND_DEFAULT_STRATUM = {"native_relation": "N0", "implementation_carrier": "I0", "choice": "N1", "operation": "N1", "metricization": "N1", "optimization": "N1", "stochastic_kernel": "N1", "future_language": "N1", "readout": "N2", "scalarization": "N2", "spectral_readout": "N2", "embedding_readout": "N2", "continuum": "N3", "imported_primitive": "N1"}

STRENGTH_RANK = {"SCALAR": 0, "QUOTIENT": 1, "RELATION": 2, "OBJECT": 3, "PRIMITIVE": 4}

TEXT_TRIGGERS = {
    "root_or_seed": re.compile(r"\b(root|seed|center)\b", re.I),
    "metricization": re.compile(r"shortest[- ]path|word metric|graph distance|equidistan|\bradius\b|\bshell\b", re.I),
    "embedding_readout": re.compile(r"euclidean|\bnorm\b|\blength\b|\bangle\b|\barea\b|\bvolume\b|covariance|convex hull|curvature", re.I),
    "propagation": re.compile(r"random walk|heat kernel|propagat|diffus|stochastic|brownian", re.I),
    "optimization": re.compile(r"optimi[sz]|minimi[sz]|maximi[sz]|surface_down|greedy", re.I),
    "spectral_readout": re.compile(r"fourier|bloch|spectr|zeta|moment", re.I),
    "continuum": re.compile(r"continuum|smooth|pde|lebesgue|gaussian", re.I),
}
TRIGGER_KINDS = {
    "root_or_seed": {"choice", "future_language"},
    "metricization": {"metricization", "readout", "scalarization"},
    "embedding_readout": {"embedding_readout", "readout", "continuum"},
    "propagation": {"operation", "stochastic_kernel", "future_language", "continuum"},
    "optimization": {"optimization", "operation"},
    "spectral_readout": {"spectral_readout", "readout", "continuum"},
    "continuum": {"continuum"},
}

@dataclass(frozen=True)
class Finding:
    code: str
    message: str
    def as_dict(self) -> dict[str, str]:
        return {"code": self.code, "message": self.message}

def _load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))

def _as_set(value: Any) -> set[str]:
    if value is None: return set()
    if isinstance(value, str): return {value}
    if isinstance(value, list): return {str(x) for x in value}
    raise TypeError(f"expected string/list, got {type(value).__name__}")

def _dependency_map(claim: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], list[Finding]]:
    findings: list[Finding] = []
    out: dict[str, dict[str, Any]] = {}
    deps = claim.get("dependencies", [])
    if not isinstance(deps, list): return {}, [Finding("NSA-LEDGER-DEPS", "dependencies must be a list")]
    for raw in deps:
        if not isinstance(raw, dict) or not isinstance(raw.get("id"), str):
            findings.append(Finding("NSA-LEDGER-DEPS", "each dependency needs a string id")); continue
        did = raw["id"]
        if did in out:
            findings.append(Finding("NSA-LEDGER-DUP", f"duplicate dependency id: {did}")); continue
        out[did] = raw
    return out, findings

def _graph_findings(deps: dict[str, dict[str, Any]], base: set[str]) -> list[Finding]:
    findings: list[Finding] = []
    for did, dep in deps.items():
        for parent in dep.get("depends_on", []) or []:
            if parent not in deps and parent not in base:
                findings.append(Finding("NSA-LEDGER-DANGLING", f"{did} depends on undeclared symbol {parent}"))
    visiting: set[str] = set(); visited: set[str] = set()
    def dfs(node: str) -> None:
        if node in visited: return
        if node in visiting:
            findings.append(Finding("NSA-LEDGER-CYCLE", f"dependency cycle contains {node}")); return
        visiting.add(node)
        for parent in deps[node].get("depends_on", []) or []:
            if parent in deps: dfs(parent)
        visiting.remove(node); visited.add(node)
    for did in deps: dfs(did)
    return findings

def _effective_stratum(dep: dict[str, Any], base: set[str]) -> tuple[str | None, list[Finding]]:
    findings: list[Finding] = []
    did = dep["id"]; claimed = dep.get("claimed_stratum"); kind = dep.get("kind")
    if claimed not in STRATA:
        findings.append(Finding("NSA-TYPE-MISSING", f"{did} has invalid claimed_stratum {claimed!r}")); return None, findings
    if kind not in KIND_DEFAULT_STRATUM:
        findings.append(Finding("NSA-KIND-MISSING", f"{did} has unknown kind {kind!r}")); return None, findings
    if did in base:
        if claimed != "N0": findings.append(Finding("NSA-BASE-TYPE", f"declared N0 primitive {did} must be typed N0, not {claimed}"))
        return "N0", findings
    expected = KIND_DEFAULT_STRATUM[kind]
    if claimed == "N0" and expected not in {"N0", "I0"}:
        findings.append(Finding("NSA-UNDERSTATED-STRATUM", f"{did} is introduced as {kind} (default {expected}) but was reported N0 without being declared in the task base"))
    elif claimed == "I0" and expected != "I0":
        findings.append(Finding("NSA-I0-MISUSE", f"{did} was labeled implementation-only I0 but its declared kind {kind} is semantic ({expected})"))
    return expected, findings

def _promotion_certificate(claim: dict[str, Any]) -> tuple[bool, list[Finding]]:
    cert = claim.get("definability_certificate")
    if not isinstance(cert, dict): return False, [Finding("NSA-CERT-MISSING", "native promotion over derived dependencies requires a definability_certificate")]
    required_true = ["construction_from_n0", "choice_independent", "automorphism_invariant", "no_hidden_imported_primitive", "transitive_dependency_closure_checked"]
    findings: list[Finding] = []
    for key in required_true:
        if cert.get(key) is not True: findings.append(Finding("NSA-CERT-INCOMPLETE", f"certificate flag {key} is not true"))
    have = cert.get("semantic_strength"); need = claim.get("promotion_target_strength")
    if have not in STRENGTH_RANK or need not in STRENGTH_RANK:
        findings.append(Finding("NSA-CERT-STRENGTH", "certificate and promotion target need valid semantic_strength values"))
    elif STRENGTH_RANK[have] < STRENGTH_RANK[need]:
        findings.append(Finding("NSA-CERT-STRENGTH", f"certificate proves only {have} invariance but claim promotes a stronger {need}"))
    refs = cert.get("evidence_refs")
    if not isinstance(refs, list) or not refs: findings.append(Finding("NSA-CERT-EVIDENCE", "promotion certificate needs at least one evidence_ref"))
    return not findings, findings

def _trigger_warnings(claim: dict[str, Any], deps: dict[str, dict[str, Any]], base: set[str]) -> list[Finding]:
    text = str(claim.get("claim_text", "")); kinds = {str(d.get("kind")) for d in deps.values()}; base_text = " ".join(sorted(base)).lower(); warnings: list[Finding] = []
    for name, regex in TEXT_TRIGGERS.items():
        if not regex.search(text): continue
        if kinds & TRIGGER_KINDS[name]: continue
        if any(tok in base_text for tok in ("metric", "distance", "root", "seed", "embedding", "euclidean", "continuum")): continue
        warnings.append(Finding("NSA-TEXT-TRIGGER", f"claim text triggers {name} but the ledger has no corresponding typed dependency/base acknowledgement"))
    return warnings

def check_claim(claim: dict[str, Any]) -> dict[str, Any]:
    claim_id = str(claim.get("claim_id", "<missing>")); proposed = claim.get("proposed_claim_class")
    if proposed not in CLAIM_CLASSES:
        return {"claim_id": claim_id, "verdict": "UNRESOLVED", "inferred_class": None, "effective_strata": [], "findings": [Finding("NSA-CLAIM-CLASS", f"invalid proposed_claim_class {proposed!r}").as_dict()], "trigger_warnings": [], "weakest_valid_restatement": claim.get("weakest_valid_restatement")}
    base = _as_set(claim.get("declared_n0_primitives")); deps, dep_findings = _dependency_map(claim); structural = list(dep_findings); structural.extend(_graph_findings(deps, base))
    critical = _as_set(claim.get("critical_symbols")); coverage = base | set(deps)
    for symbol in sorted(critical - coverage): structural.append(Finding("NSA-DEPENDENCY-OMITTED", f"theorem-critical symbol {symbol} is absent from base/dependency closure"))
    effective: dict[str, str] = {}; typing_findings: list[Finding] = []
    for did, dep in deps.items():
        stratum, fs = _effective_stratum(dep, base); typing_findings.extend(fs)
        if stratum is not None: effective[did] = stratum
    warnings = _trigger_warnings(claim, deps, base)
    if structural:
        verdict = "UNRESOLVED"; inferred = None; findings = structural + typing_findings
    else:
        semantic_strata = {s for s in effective.values() if s != "I0"}; has_n3 = "N3" in semantic_strata; has_n2 = "N2" in semantic_strata; has_n1 = "N1" in semantic_strata; has_derived = has_n1 or has_n2 or has_n3
        if has_n3: inferred = "CONTINUUM_ONLY"
        elif has_n2: inferred = "READOUT_ONLY"
        elif has_n1: inferred = "CONDITIONAL_DERIVED"
        else: inferred = "NATIVE_ADMISSIBLE"
        findings = list(typing_findings)
        if proposed == "NATIVE":
            if not has_derived and not typing_findings: verdict = "NATIVE_ADMISSIBLE"
            else:
                cert_ok, cert_findings = _promotion_certificate(claim); findings.extend(cert_findings); verdict = "NATIVE_ADMISSIBLE" if cert_ok and not typing_findings else "SEMANTIC_MISMATCH"
        else:
            verdict = "SEMANTIC_MISMATCH" if typing_findings else inferred
    result = {"claim_id": claim_id, "verdict": verdict, "inferred_class": inferred, "effective_strata": sorted(set(effective.values())), "findings": [f.as_dict() for f in findings], "trigger_warnings": [f.as_dict() for f in warnings], "weakest_valid_restatement": claim.get("weakest_valid_restatement")}
    assert result["verdict"] in VERDICTS
    return result

def check_document(doc: Any) -> dict[str, Any]:
    if isinstance(doc, dict) and "claims" in doc: claims = doc["claims"]
    elif isinstance(doc, list): claims = doc
    elif isinstance(doc, dict): claims = [doc]
    else: raise TypeError("input must be a claim object, a list, or {'claims': [...]}")
    if not isinstance(claims, list): raise TypeError("claims must be a list")
    results = [check_claim(c) for c in claims]; counts: dict[str, int] = {}
    for r in results: counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    return {"schema": "ENTERPRISE_MATH_NATIVE_SEMANTICS_CHECK_RESULT_V1", "counts": counts, "results": results}

def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("ledger", type=Path); parser.add_argument("--output", type=Path); args = parser.parse_args(); result = check_document(_load(args.ledger)); text = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True); args.output.write_text(text, encoding="utf-8")
    else: print(text, end="")
    return 1 if any(r["verdict"] in {"SEMANTIC_MISMATCH", "UNRESOLVED"} for r in result["results"]) else 0

if __name__ == "__main__": raise SystemExit(main())
