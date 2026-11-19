"""Rebuild and run the two integer certificates. Requires Python 3.8+ and C++17."""
from fractions import Fraction
from math import gcd
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import os
import subprocess

PRIME = 17
MODULUS = PRIME**6
GRID = 12_252_240
BUDGET = 2331
HERE = Path(__file__).resolve().parent

# Discovery used lattice reduction. These fixed witnesses are checked by
# ordinary integer arithmetic, so neither a lattice library nor its output
# convention is part of verification.
CASES = [
    ("neighbors", (17, 34, 51, 68, 85, 102), [
        [277,173,74,-260,538,-656], [127,-223,302,468,-1169,-798],
        [-163,657,158,333,-5,-524], [-35,370,-178,-543,-1930,410],
        [-77,-342,-854,77,667,-1699], [-361,-237,257,-1543,423,-1182],
    ]),
    ("shifted", (17, 34, 51, 68, 85, 119), [
        [22,-82,227,-651,-74,1608], [326,-277,364,-649,95,-419],
        [178,474,-497,-603,-897,-392], [57,58,711,1099,377,1168],
        [-75,-385,-923,432,-658,1142], [-3,-46,384,-269,-2475,-1757],
    ]),
]


def minor(matrix, row, col):
    return [r[:col]+r[col+1:] for i,r in enumerate(matrix) if i != row]


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    return sum((-1)**j * a * determinant(minor(matrix, 0, j))
               for j,a in enumerate(matrix[0]) if a)


def multiset_count(parts):
    counts = [1] + [0]*BUDGET
    for d in parts:
        for fee in range(d-1, BUDGET+1):
            counts[fee] += counts[fee-(d-1)]
    return sum(counts)


def header_array(sequence):
    if isinstance(sequence, (list, tuple)):
        return "{" + ",".join(header_array(x) for x in sequence) + "}"
    return str(sequence)


def character_data(pivots, short_rows):
    a = [[pow(d//PRIME, -j, MODULUS) for d in pivots] for j in range(1,7)]
    det = determinant(a)
    assert gcd(det, MODULUS) == 1
    invdet = pow(det, -1, MODULUS)
    inv = [[((-1)**(i+j)*determinant(minor(a,j,i))*invdet)%MODULUS
            for j in range(6)] for i in range(6)]
    weights = [[sum(row[k]*inv[k][j] for k in range(6))%MODULUS
                for j in range(6)] for row in short_rows]
    for i,row in enumerate(weights):
        for j in range(6):
            assert row[j] % PRIME**(5-j) == 0
            assert (sum(row[k]*a[k][j] for k in range(6))-short_rows[i][j])%MODULUS == 0
    index = abs(determinant(short_rows))
    assert index == PRIME**15
    bounds = []
    for row in short_rows:
        rates = [Fraction(t,d-1) for t,d in zip(row,pivots)] + [Fraction(0)]
        width = BUDGET*(max(rates)-min(rates))
        bounds.append(width.numerator//width.denominator+1)
    assert 2*max(bounds) < MODULUS
    return index, weights, bounds


def run_case(name, pivots, matrix, parts):
    index, weights, bounds = character_data(pivots, matrix)
    with TemporaryDirectory(prefix="t6-seventeen-") as temp:
        folder = Path(temp)
        header = folder/"certificate.hpp"
        header.write_text("\n".join([
            f"constexpr int modulus={MODULUS}, budget={BUDGET}, divisor_grid={GRID};",
            f"constexpr int pivots[6]={header_array(pivots)};",
            f"constexpr int weights[6][6]={header_array(weights)};",
            f"constexpr int exclusive_bound[6]={header_array(bounds)};",
        ])+"\n",encoding="ascii")
        binary = folder/name
        subprocess.run([os.environ.get("CXX","c++"), "-std=c++17", "-O3",
                        "-I", str(folder), str(HERE/f"seventeen_{name}.cpp"),
                        "-o", str(binary)],check=True)
        result = json.loads(subprocess.check_output([str(binary)]))
    assert result["tails"] == multiset_count([d for d in parts if d not in pivots])
    assert result["real_hits"] == 0
    if name == "shifted":
        assert result["control_hits"] == result["empty_vs_control"] == 1
    return {"pivots":pivots, "budget_box_exclusive_bounds":bounds,
            "absolute_determinant":index, **result}


def control(parts):
    # All these are true source columns. The two budgets are deliberately larger.
    diff = {17:-1,34:22,51:7,68:-17,85:9,102:-2,119:-6,136:2,
            153:2,170:1,204:4,221:-5,238:2,255:-8,272:2,306:2,357:2,374:1}
    assert set(diff) <= set(parts)
    residual = [sum(z*pow(d//PRIME,-j,PRIME**j) for d,z in diff.items())%PRIME**j
                for j in range(1,7)]
    assert residual == [0]*6
    fees = [sum((d-1)*max(0,s*z) for d,z in diff.items()) for s in (1,-1)]
    assert fees == [6098,5197]
    return {"signed_difference":sorted(diff.items()), "side_fees":fees,
            "six_local_residues":residual, "zeroth_moment_difference":sum(diff.values())}


if __name__ == "__main__":
    layer = [d for d in range(PRIME,BUDGET+2,PRIME) if GRID%d == 0]
    assert len(layer) == 59 and GRID//PRIME == 720720
    result = {"budget_per_side":BUDGET, "initial_divisor_grid":GRID,
              "reduced_divisor_grid":GRID//PRIME, "layer_denominators":layer,
              "one_side_count_including_empty":multiset_count(layer),
              "relaxed_positive_control":control(layer)}
    for name, pivots, rows in CASES:
        result[name] = run_case(name,pivots,rows,layer)
    print(json.dumps(result,indent=2,sort_keys=True))
