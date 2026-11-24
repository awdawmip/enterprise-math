"""Read-only audit probes of fixed POWER 74b386d source copies.

To avoid executing unrelated package initialization, load the unmodified AST of
Cohen LLL, the Mahler module, and the 86 module with repository imports omitted.
The existing functions/classes run unchanged. The unused Sturm object is not
constructed; the engine is instantiated through __new__ and receives the real
Mahler class. No numerical routine, branching condition, or lattice is mocked.
"""
import ast
import dataclasses
import json
import math
from pathlib import Path
import sys
import types

BASE = Path(__file__).resolve().parent
module = types.ModuleType("power_85_86_readonly_audit")
sys.modules[module.__name__] = module
ns = module.__dict__

def load_selected(relative_path, only_function=None):
    path = BASE / relative_path
    tree = ast.parse(path.read_text(), filename=str(path))
    nodes = []
    for node in tree.body:
        if isinstance(node, ast.ImportFrom) and (node.level or (node.module or "").startswith("power")):
            continue
        if only_function is not None and not (
            isinstance(node, (ast.Import, ast.ImportFrom))
            or isinstance(node, ast.FunctionDef) and node.name == only_function
        ):
            continue
        nodes.append(node)
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(path), "exec"), ns)

load_selected("src/power/weapons/high_dim_cohen_bkz_polytope.py", "cohen_exact_integer_lll")
load_selected("src/power/weapons/padic_mahler_measure_hyperbolic_lattice.py")
load_selected("src/power/weapons/simultaneous_coppersmith_multi_candidate_lattice.py")
Mahler = ns["PadicMahlerMeasureHyperbolicLatticeEngine"]
Engine = ns["SimultaneousCoppersmithMultiCandidateLatticeEngine"]

def engine(tier):
    obj = Engine.__new__(Engine)
    obj.tier = tier
    obj.dimension = obj.TIER_DIMENSIONS[tier]
    obj.mahler_engine = Mahler()
    obj.isolator = None  # Never read in scan_candidate_stream.
    return obj

out = {"source_commit": "74b386de5f1ca8dcc662935f563c438e1cfeee7e"}
p, q, m = 503, 509, 16
n = p * q
true_pair = (p % m, q % m)
x, y = (p - true_pair[0]) // m, (q - true_pair[1]) // m
out["true_candidate"] = {"n": n, "p": p, "q": q, "m": m, "residues": true_pair, "quotient_root": [x, y], "gcd_p_residue_n": math.gcd(true_pair[0], n)}
out["scans"] = []
cases = [
    ("actual_test_inputs_defaults", "16D_CANONICAL", [(1, 1), (3, 5), true_pair, (7, 9)], None),
    ("true_residue_gate_passes", "16D_CANONICAL", [true_pair], 5),
    ("true_residue_gate_passes", "24D_CANONICAL", [true_pair], 5),
    ("given_factor_positive_control", "16D_CANONICAL", [(p, q)], 5),
]
for label, tier, pairs, bits in cases:
    res = engine(tier).scan_candidate_stream(n=n, m_sieve=m, candidates=pairs, max_quotient_bits=bits)
    out["scans"].append({"case": label, "tier": tier, "max_quotient_bits": bits,
                         "is_success": res.is_success, "factors": res.factors,
                         "candidates_tested": res.candidates_tested,
                         "closest_vector_bits": res.closest_vector_bits,
                         "gate_threshold": n.bit_length() - 4})

out["canonical_geometry"] = []
for dim in (16, 24):
    mat, _, _ = Mahler.assemble_mahler_optimal_matrix(n, 0, 0, m, 32, 32, f"{dim}D_MAHLER")
    reduced, _ = engine(f"{dim}D_CANONICAL").pre_reduce_canonical_basis(n, m, 32, 32)
    target = [true_pair[0] * true_pair[1] - n, true_pair[1] * m * 32, true_pair[0] * m * 32] + [0] * (dim - 3)
    residual, dist_bits = Engine.babai_nearest_plane_decode(reduced, target)
    out["canonical_geometry"].append({"dimension": dim,
        "off_diagonal_nonzero_count": sum(mat[i][j] != 0 for i in range(dim) for j in range(dim) if i != j),
        "reduced_is_permutation_of_input": sorted(map(tuple, mat)) == sorted(map(tuple, reduced)),
        "residual_first_three": residual[:3],
        "residual_other_nonzero_count": sum(v != 0 for v in residual[3:]),
        "distance_bits": dist_bits})

telemetry = json.loads((BASE / "docs/grand_unified_asymptotic_algebraic_pipeline_results.json").read_text())
out["pipeline85_first_fermat_step"] = []
for case in telemetry["phase1_multiscale_solves"]:
    nn = case["n"]
    pp, qq = case["factors"]
    a = math.isqrt(nn)
    if a * a < nn:
        a += 1
    diff = a * a - nn
    bb = math.isqrt(diff)
    out["pipeline85_first_fermat_step"].append({"n_bits": nn.bit_length(), "factors": [pp, qq],
        "reported_method": case["method"], "ceil_sqrt_n": a, "a_squared_minus_n": diff,
        "defect_is_square": bb * bb == diff,
        "first_step_factors_match": sorted([a-bb, a+bb]) == sorted([pp, qq])})

print(json.dumps(out, indent=2))
