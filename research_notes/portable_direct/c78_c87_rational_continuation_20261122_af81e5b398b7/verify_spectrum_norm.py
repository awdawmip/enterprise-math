"""Exact checks of the closed norm formula for the actual C78 spectrum."""
from fractions import Fraction as F
from pathlib import Path
import json
from explicit_algebra import circuit, norm_matrix_at, determinant, evaluate

circuit_data = circuit()
points = [(3, 3, 2), (5, 4, 2), (8, 7, 4), (9, 9, 9),
          (16, 11, 8), (16, 16, 2), (17, 13, 7), (32, 27, 19)]
rows = []
for c, v, w in points:
    x, y = F(v, c), F(w, c)
    numerator = 50176**16*x**24*y**168*(x**9-256*y**9)**4*(1-256*x**15)**4
    denominator = ((1-448**4*x**51*y**9)*(1-1792**4*x**66*y**9))**4
    dn = determinant(norm_matrix_at(circuit_data["N"], x, y))
    dq = determinant(norm_matrix_at(circuit_data["Q"], x, y))
    assert dn == numerator and dq == denominator
    assert dq >= F(1, c**540)
    nr = dn/dq
    assert nr >= F(1, 16**16*c**288)
    rows.append({"c": c, "V": v, "W": w, "N_norm_equal": True,
                 "Q_norm_equal": True, "R_lower_bound_passed": True})
positive_rows = []
for c, v, w, r, s in [(32,32,2,F(1),F(1,2)),
                      (256,81,16,F(3,4),F(1,2)),
                      (625,256,81,F(4,5),F(3,5))]:
    assert r**4 == F(v,c) and s**4 == F(w,c)
    value = abs(evaluate(circuit_data["N"],r,s)/evaluate(circuit_data["Q"],r,s))
    lower = F(50176,805057*85**2*c**36)
    assert value >= lower
    positive_rows.append({"c":c,"V":v,"W":w,"r":str(r),"s":str(s),
                          "R_abs":str(value),"rational_lower_bound":str(lower)})
result={"status":"PASS","arithmetic":"arbitrary precision integers and Fraction",
        "norm_grid_points":rows,"positive_root_rational_points":positive_rows,
        "scope":"Finite implementation checks; universal proofs in SPECTRUM_NORM.md."}
Path(__file__).with_name("spectrum_norm_checks.json").write_text(
    json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"status":"PASS","norm_grid_points":len(rows),
                  "positive_root_rational_points":len(positive_rows)}))
