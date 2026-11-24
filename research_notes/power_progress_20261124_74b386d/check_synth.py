"""Small source-audit witness for POWER 88, without editing the source algorithm.

Source: awdawmip/power@74b386de5f1ca8dcc662935f563c438e1cfeee7e
src/power/weapons/co_optimized_asymptotic_algebraic_synthesizer.py
Git blob: 217aa66a9a4fd255333a9d49241ce89a4e39a121

Only the original static early_abort_babai_decode method is AST-extracted.
The identity lattice makes the actual nearest lattice point unambiguous.
This is not a reimplementation or a test of the other synthesis stages.
"""
import ast
import hashlib
import json
import math
from pathlib import Path
from typing import List, Tuple

HERE = Path(__file__).resolve().parent
source = (HERE / "synth_code.py").read_bytes()
git_blob = hashlib.sha1(b"blob " + str(len(source)).encode() + b"\0" + source).hexdigest()
assert git_blob == "217aa66a9a4fd255333a9d49241ce89a4e39a121"
tree = ast.parse(source)
engine = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "CoOptimizedAsymptoticAlgebraicSynthesizerEngine")
method = next(n for n in engine.body if isinstance(n, ast.FunctionDef) and n.name == "early_abort_babai_decode")
assert len(method.decorator_list) == 1 and isinstance(method.decorator_list[0], ast.Name) and method.decorator_list[0].id == "staticmethod"
method.decorator_list = []  # bind the unchanged static function directly
module = ast.fix_missing_locations(ast.Module(body=[method], type_ignores=[]))
namespace = {"List": List, "Tuple": Tuple}
exec(compile(module, "<original POWER 88 static method>", "exec"), namespace)
decode = namespace["early_abort_babai_decode"]

basis = [[int(i == j) for j in range(5)] for i in range(5)]
target = [2, 0, 0, 0, 0]
residual, distance_bits, aborted = decode(basis, target, 1)
assert aborted is True
assert residual == target
# Exact lattice membership witness: target = 2 * first row.
assert target == [2 * x for x in basis[0]]

# The reported slack is a function of input bit length, modulus bit length
# and dimension alone; no shortest vector or successful root enters it.
slack = {str(dim): 928 * (0.5 * (1.0 - 1.0 / math.sqrt(dim))) - (928 / 2.0 - (1 << 64).bit_length()) for dim in (16, 24, 32)}
out = {
    "power_commit": "74b386de5f1ca8dcc662935f563c438e1cfeee7e",
    "source_git_blob": git_blob,
    "scope": "Unmodified original static method; no full pipeline or RSA timing rerun",
    "identity_lattice_early_abort_witness": {
        "basis": basis, "target": target, "bound_squared": 1,
        "returned_residual": residual, "returned_distance_bits": distance_bits,
        "aborted": aborted, "exact_closest_lattice_point": target,
        "exact_distance_squared": 0,
        "explanation": "Aborts before visiting the first basis row, which would cancel the entire remaining residual."
    },
    "slack_from_input_and_dimension_only": slack,
    "scope_note": "RSA probe reports zero early aborts; this witness refutes the general rejection rule but does not explain an observed RSA rejection."
}
(HERE / "check_synth_results.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(out, ensure_ascii=False, indent=2))
