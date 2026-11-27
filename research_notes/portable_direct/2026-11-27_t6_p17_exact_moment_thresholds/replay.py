"""Sharp p17 signed-mass bounds after adjoining exact reciprocal moments."""
from hashlib import sha256
import json
from math import lcm
from pathlib import Path
import argparse
from fractions import Fraction

from tail import verify_variable_tail

from exact import read_lattice, congruences, dot, signed_mass, model, enumerate_ball, split_witness, WEIGHTS
from flint import fmpz_mat
from sympy import Matrix, gcdex

DENOMINATOR_LCM = lcm(*range(1, 17))
PINS = (
    (13055, 266009),
    (35121, 33355),
    (120168, 1411),
    (740792, 11353),
    (2579053, 905),
    (9499607, 691),
    (12056149, 7),
)

def unweight(rows):
    return tuple(tuple(x//w for x,w in zip(row,WEIGHTS)) for row in rows)

def weight(rows):
    return tuple(tuple(x*w for x,w in zip(row,WEIGHTS)) for row in rows)

def kernel_of_row(rows, row):
    """Use determinant-1 Bezout row operations, then delete the nonzero pivot."""
    rows = list(rows)
    pivot = dot(rows[0], row)
    for i in range(1, len(rows)):
        value = dot(rows[i], row)
        if not value:
            continue
        s, t, g = map(int, gcdex(pivot, value))
        a, b = rows[0], rows[i]
        x, y = -value//g, pivot//g
        assert s*y - t*x == 1
        rows[0] = tuple(s*v+t*w for v, w in zip(a,b))
        rows[i] = tuple(x*v+y*w for v, w in zip(a,b))
        pivot = g
    if pivot == 0:
        return tuple(rows)
    assert dot(rows[0], row) == pivot
    assert all(dot(candidate, row) == 0 for candidate in rows[1:])
    return tuple(rows[1:])

def reduce_rows(rows, augmented):
    weighted = weight(rows)
    embedded = fmpz_mat([[*r,sum(r)] if augmented else r for r in weighted])
    reduced, change = embedded.lll(transform=True)
    transform = Matrix([[int(change[i,j]) for j in range(change.ncols())]
                        for i in range(change.nrows())])
    assert abs(transform.det()) == 1 and change * embedded == reduced
    output = tuple(tuple(int(reduced[i,j]) for j in range(16)) for i in range(reduced.nrows()))
    result = unweight(output)
    assert weight(result) == output
    return result

def moments(row):
    return tuple(sum(Fraction(u,(17*j)**k) for j,u in enumerate(row,1)) for k in range(7))

def restrict_layers(initial, bounds, metric, limit=6):
    previous = initial
    for k, (bound, expected) in enumerate(bounds[:limit + 1]):
        row = tuple((DENOMINATOR_LCM//j)**k for j in range(1,17))
        previous = reduce_rows(kernel_of_row(previous,row),True)
        assert len(previous) == 15-k
        assert all(congruences(r)==(0,)*6 and moments(r)[:k+1]==(0,)*(k+1)
                   for r in previous)
        augmented = metric == "augmented"
        reduced = previous if augmented else reduce_rows(previous,False)
        weighted = weight(reduced)
        count, vectors = enumerate_ball(model(weighted,augmented),bound)
        if augmented and expected is not None:
            assert count["ellipsoid_points"] == expected, count
        output = []
        for gauge, w, coeff in vectors:
            assert gauge == bound, (k,gauge,bound)
            assert tuple(dot(coeff,col) for col in zip(*weighted))==w
            u = unweight([w])[0]
            assert weight([u])==(w,)
            assert congruences(u)==(0,)*6 and moments(u)[:k+1]==(0,)*(k+1)
            balanced_budget = (bound+1)//2
            witness = split_witness(u,balanced_budget,balanced_budget)
            assert witness is not None, (k, balanced_budget)
            assert moments(witness["x"])[:k+1] == moments(witness["y"])[:k+1]
            output.append({"unweighted_difference":u, "signed_masses":signed_mass(w),
                           "balanced_budget": balanced_budget, "balanced_witness":witness})
        assert len(output)==1, (k, output)
        yield {"moment_order":k, "rank":len(previous), "threshold":bound,
               "enumeration":count,"minimizers_up_to_sign":output}

def analyzed_pair(path):
    raw = path.read_bytes()
    assert sha256(raw).hexdigest()=="a0abdf6b02c7db4871ce392fa53ed7d304ae98a1590869e432c3103f2c19a255"
    obj = json.loads(raw)["balanced_collision"]
    x,y = obj["x"],obj["y"]
    z = tuple(a-b for a,b in zip(x,y))
    mx,my,mz = moments(x),moments(y),moments(z)
    assert congruences(x)==congruences(y)==tuple(obj["target"]) and mx[0]-my[0]==13
    return {"M0": [mx[0].numerator,my[0].numerator], "moment_difference": [str(m) for m in mz],
            "target":congruences(x), "mass":obj["masses"]}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("basis",type=Path)
    parser.add_argument("previous_collision",type=Path)
    parser.add_argument("--metric", choices=("augmented","euclidean"), default="augmented")
    parser.add_argument("--skip-tail", action="store_true")
    args=parser.parse_args()
    basis = read_lattice(args.basis)
    new_layers = list(restrict_layers(unweight(basis), PINS, args.metric))
    report = {"metric":args.metric, "previous_balanced_pair":analyzed_pair(args.previous_collision),
              "layers":new_layers}
    if not args.skip_tail:
        report["variable_tail"] = verify_variable_tail(basis)
    print(json.dumps(report, sort_keys=True))

if __name__=="__main__":
    main()
