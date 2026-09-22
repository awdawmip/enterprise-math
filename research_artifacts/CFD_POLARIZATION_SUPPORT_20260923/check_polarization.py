"""Exact finite Fourier/BRC witness, not a native CFD benchmark.

All coefficients below are imaginary integer numerators over an unevaluated
denominator4. No division, floating simulation or amplitude pruning is used.
"""
from __future__ import annotations

import ast
import dataclasses
import hashlib
import json
import sys
import types
from pathlib import Path


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def raw_vortex(spectrum):
    result = {}
    branches = []
    for p, u in sorted(spectrum.items()):
        for q, v in sorted(spectrum.items()):
            k = tuple(x + y for x, y in zip(p, q))
            term = tuple(q[j] * dot(u, v) - v[j] * dot(q, u) for j in range(3))
            result[k] = tuple(a + b for a, b in zip(result.get(k, (0, 0, 0)), term))
            branches.append({"p": p, "q": q, "k": k, "raw_i_numerator_over_4": term})
    return {k: v for k, v in result.items() if any(v)}, branches


def describe(spectrum):
    raw, branches = raw_vortex(spectrum)
    outputs = []
    projected_support = []
    for k, numerator in sorted(raw.items()):
        k2 = dot(k, k)
        pressure_numerator = dot(k, numerator)
        projected = tuple(k2 * numerator[j] - k[j] * pressure_numerator for j in range(3))
        if any(projected):
            projected_support.append(k)
        outputs.append({"k": k, "raw": {"imaginary_numerator": numerator, "denominator": 4},
                        "pressure_interface_sigma": {"imaginary_numerator": pressure_numerator, "denominator": 4 * k2},
                        "projected": {"imaginary_numerator": projected, "denominator": 4 * k2}})
    return {"inputs": [{"k": k, "real_vector_numerator": v, "denominator": 2,
                        "modal_energy_numerator": dot(v, v), "modal_energy_denominator": 4}
                       for k, v in sorted(spectrum.items())],
            "ordered_pair_count": len(branches), "branches": branches,
            "raw_support_size": len(raw), "projected_support": projected_support,
            "outputs": outputs}


def reuse_native_carrier(source):
    text = source.read_text(encoding="utf-8")
    tree = ast.parse(text)
    names = {"ClosureResult", "_neg", "_add", "_in_box", "truncated_additive_carrier"}
    selected = [node for node in tree.body if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name in names]
    assert {node.name for node in selected} == names
    # Original pure integer AST nodes are executed unchanged; no NumPy-dependent
    # host code is imported and no callback/native-host execution is claimed.
    module = types.ModuleType("_original_native_carrier_integer_subset")
    module.dataclass = dataclasses.dataclass
    sys.modules[module.__name__] = module
    prefix = ast.parse("from __future__ import annotations\n").body
    assembled = ast.Module(body=prefix + selected, type_ignores=[])
    exec(compile(ast.fix_missing_locations(assembled), str(source), "exec"), module.__dict__)
    return module.truncated_additive_carrier, hashlib.sha256(source.read_bytes()).hexdigest(), hashlib.sha256(ast.dump(assembled, include_attributes=False).encode()).hexdigest()


def main():
    here = Path(__file__).resolve().parent
    source = here.joinpath("static_carrier_native_adapter_source.py")
    closure, source_hash, subset_hash = reuse_native_carrier(source)
    e1, em1, e2, em2 = (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)
    shear = {e1: (0, 0, 1), em1: (0, 0, 1), e2: (0, 0, 1), em2: (0, 0, 1)}
    contrast = {e1: (0, 1, 0), em1: (0, 1, 0), e2: (0, 0, 1), em2: (0, 0, 1)}
    for field in (shear, contrast):
        assert all(dot(k, v) == 0 for k, v in field.items())
        assert all(field[tuple(-x for x in k)] == v for k, v in field.items())
    assert set(shear) == set(contrast)
    assert {k: dot(v, v) for k, v in shear.items()} == {k: dot(v, v) for k, v in contrast.items()}
    first, second = describe(shear), describe(contrast)
    assert first["ordered_pair_count"] == second["ordered_pair_count"] == 16
    assert first["raw_support_size"] == second["raw_support_size"] == 8
    assert first["projected_support"] == []
    assert set(second["projected_support"]) == {(a, b, 0) for a in (-1, 1) for b in (-1, 1)}
    for output in first["outputs"]:
        assert output["pressure_interface_sigma"]["imaginary_numerator"] != 0
    k = (1, 1, 0)
    r1 = next(o for o in first["outputs"] if tuple(o["k"]) == k)
    r2 = next(o for o in second["outputs"] if tuple(o["k"]) == k)
    assert tuple(r1["raw"]["imaginary_numerator"]) == (1, 1, 0)
    assert tuple(r2["raw"]["imaginary_numerator"]) == (0, 0, -1)
    routes = []
    for limit in (128, 384):
        route = closure(shear, cutoff=15, limit=limit)
        assert route.status == "FALLBACK_DENSE" and route.lower_bound == limit + 1
        routes.append(dataclasses.asdict(route))
    result = {"schema": "CFD_EXACT_POLARIZATION_OBSERVER_COUNTEREXAMPLE_V1",
              "status": "EXACT_INTEGER_CHECK_PASS", "n": 32, "cutoff": 15,
              "carrier_size_proved_by_lattice_argument": 31 * 31,
              "same_support": True, "same_modal_energies": True,
              "shear": first, "contrast": second, "native_integer_closure_calls": routes,
              "reused_adapter_source_sha256": source_hash, "unchanged_selected_ast_sha256": subset_hash,
              "native_spectralDNS_host_executed": False, "timings_measured": False,
              "pressure_scope": "sigma=(k dot raw)/|k|^2, not an asserted physical-pressure convention",
              "arithmetic": "Integer numerators with explicit unevaluated denominators and formal i; no quotient materialized",
              "conclusion": "Boolean support plus modal energy cannot determine the projected nonlinear output. A common-polarization certificate can identify an invariant family while preserving nonzero raw Vortex and sigma.",
              "acceptance": "Direct-user mathematical support, no parent Task claim or formal Driver Acceptance"}
    here.joinpath("certificate.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status": result["status"], "ordered_pairs_per_field": 16, "carrier": 961,
                      "raw_support_sizes": [8, 8], "projected_support_sizes": [0, 4],
                      "closure_routes": [r["status"] for r in routes], "native_host_executed": False}))


if __name__ == "__main__":
    main()
