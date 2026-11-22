from fractions import Fraction as F
from pathlib import Path
import json
from explicit_algebra import determinant

def mul(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(3)),F(0)) for j in range(3)] for i in range(3)]

xs=[F(1,7),F(1,3),F(1),F(2),F(7,3),F(11)]
ts=[F(-3),F(-1),F(-1,4),F(0),F(2,5),F(1),F(4)]
count=0
for x in xs:
    m=[[F(0),F(0),F(0)],[F(1),F(0),x],[F(0),F(1),F(0)]]
    m2=mul(m,m)
    reduced=[[m2[i][j]-(x if i==j else 0) for j in range(3)] for i in range(3)]
    assert any(v for row in reduced for v in row)
    assert not any(v for row in mul(m,reduced) for v in row)
    for t in ts:
        ti_minus_m=[[(t if i==j else 0)-m[i][j] for j in range(3)] for i in range(3)]
        assert determinant(ti_minus_m)==t*(t*t-x)
        count+=1
result={"status":"PASS","arithmetic":"Fraction","characteristic_evaluations":count,
        "whole_algebra_original_annihilator_checks":len(xs),
        "reduced_polynomial_not_global_annihilator_checks":len(xs),
        "scope":"Finite mechanism check for zero-factor removal, not the full C78 correspondence."}
Path(__file__).with_name("zero_factor_checks.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result))
