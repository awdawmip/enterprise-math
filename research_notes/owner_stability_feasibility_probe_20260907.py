"""Independent integration probes; no edits to the solver/recovery implementation."""
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
EXPERIMENT = ROOT / "experiments" / "owner_joint_observer_20260907"
sys.path.insert(0, str(EXPERIMENT))

from sympy import Matrix
import recovery
from observer_certificate import Branch, all_three_axis_tables

point = (0,) * 6
tables = all_three_axis_tables((Branch("origin", point),))


class IncorrectRrefProposal:
    def rref(self):
        # This candidate has the right dimension, rank and sign, but wrong mass.
        return Matrix([[1, 2]]), (0,)


with patch.object(recovery, "Matrix", return_value=IncorrectRrefProposal()):
    answer = recovery.recover(tables)
assert answer["feasibility_method"] == "exact_phase_one_bland"
assert answer["distribution"] == ((point, Fraction(1)),)
assert answer["certificate_verified_on_original_equations"] is True

propagated = []
for error in (MemoryError("audit resource failure"), ArithmeticError("audit invariant failure"),
              RuntimeError("audit solver failure")):
    with patch.object(recovery, "Matrix", return_value=IncorrectRrefProposal()), \
         patch.object(recovery, "solve_nonnegative", side_effect=error):
        try:
            recovery.recover(tables)
        except type(error) as caught:
            assert caught is error
            assert not isinstance(caught, recovery.InfeasibleMarginalsError)
            propagated.append(type(error).__name__)
        else:
            raise AssertionError("solver failure was converted to a mathematical result")

files = ("recovery.py", "exact_feasibility.py", "test_recovery.py", "test_exact_feasibility.py")
result = {
    "status": "PASS",
    "evidence_type": "INDEPENDENT_EXACT_INTEGRATION_PROBE",
    "incorrect_rref_candidate": "REJECTED_BY_ORIGINAL_EQUATIONS_THEN_EXACT_RECOVERY",
    "execution_errors_propagated_without_infeasibility_relabel": propagated,
    "source_sha256": {name: hashlib.sha256((EXPERIMENT / name).read_bytes()).hexdigest() for name in files},
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps(result, indent=2))
