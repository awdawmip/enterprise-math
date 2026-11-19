"""Exact Schur and pressure-gradient ports on the orthogonal unit duct."""
import argparse
import json
import re
from fractions import Fraction as Q
from pathlib import Path


def chain(positions):
    m = len(positions)
    lengths = [b - a for a, b in zip([0] + positions, positions + [1])]
    conductance = [1 / Q(x) for x in lengths]
    diag = [conductance[i] + conductance[i + 1] for i in range(m)]
    off = [-x for x in conductance[1:-1]]
    return diag, off


def multiply(diag, off, u):
    result = [a * x for a, x in zip(diag, u)]
    for i, c in enumerate(off):
        result[i] += c * u[i+1]
        result[i+1] += c * u[i]
    return result


def eliminate(diag, off, keep):
    rows = [{i: value} for i, value in enumerate(diag)]
    for i, value in enumerate(off):
        rows[i][i+1] = rows[i+1][i] = value
    kept = set(keep)
    for i, row in enumerate(rows):
        if i in kept:
            continue
        pivot = row.pop(i)
        for j in row:
            del rows[j][i]
            for k in row:
                rows[j][k] = rows[j].get(k, 0) - row[j]*row[k]/pivot
    return [rows[i][i] for i in keep], [rows[i][j] for i, j in zip(keep, keep[1:])]


def det_chain(diag, off):
    prev, val = 1, diag[0]
    for a, c in zip(diag[1:], off):
        prev, val = val, a * val - c * c * prev
    return val


def schur(n, block, residue):
    m = n // block
    keep = list(range(residue, n, block))
    x = [Q(2*i+1, 2*n) for i in range(n)]
    s, edge = eliminate(*chain(x), keep)
    assert (s, edge) == chain([x[i] for i in keep])
    base, be = chain([Q(2*i+1, 2*m) for i in range(m)])
    theta = Q(2*residue+1, 2*block)
    prod = 1 / (4*theta*(1-theta))
    total = 2 + Q(2*m-1, m)*(prod-1)
    det0 = det_chain(base, be)
    # m+1 distinct tests certify the whole degree-m determinant polynomial.
    for z in range(m+1):
        lhs = det_chain([a-z*b for a,b in zip(s,base)], [a-z*b for a,b in zip(edge,be)])
        assert lhs == det0*(1-z)**(m-2)*(z*z-total*z+prod)
    return {"cells": n, "retained": m, "block": block, "offset": residue,
            "det_ratio": str(prod), "pair_sum": str(total),
            "coarse_midpoint_flux_evaluated_on_real_ports":
            [str(1/(2*theta)), str(1/(2*(1-theta)))]}


def green_tests():
    report = []
    for n in range(1, 33):
        x = [Q(2*i+1, 2*n) for i in range(n)]
        diag, off = chain(x)
        green = [[min(a,b)*(1-max(a,b)) for b in x] for a in x]
        for i,row in enumerate(green):
            assert multiply(diag,off,row) == [int(i == j) for j in range(n)]
        norm = max(map(sum,green))
        assert norm == Q(n,8) + Q(n%2,8*n)
        a = sum(z*z for z in x)
        b = sum(z*(1-z) for z in x)
        assert a+b == Q(n,2) and a-b == Q(n*n-1,6*n)
        if n in (1,5,32):
            report.append([n,str(norm),str(a+b),str(a-b)])
    x = [Q(i*i+1, 45) for i in range(1,7)]
    diag, off = chain(x)
    for i,a in enumerate(x):
        response = [min(a,b)*(1-max(a,b)) for b in x]
        assert multiply(diag, off, response) == [int(i==j) for j in range(len(x))]
        assert response[0]/x[0] == 1-a and response[-1]/(1-x[-1]) == a
    return report


def native_file(path):
    raw = Path(path).read_text()
    match = re.search(r'internalField\s+nonuniform\s+List<scalar>\s+(\d+)\s*\(([^)]*)\)', raw)
    n = int(match[1])
    phat = list(map(Q, match[2].split()))
    assert n == 32 and len(phat) == n
    assert re.search(r'left\s*\{[^}]*fixedValue[^}]*uniform\s+1;', raw)
    assert re.search(r'right\s*\{[^}]*fixedValue[^}]*uniform\s+0;', raw)
    assert re.search(r'sides\s*\{[^}]*zeroGradient', raw)
    x = [Q(2*i+1,2*n) for i in range(n)]
    a = multiply(*chain(x),phat)
    residual = [-v for v in a]
    residual[0] += 2*n
    error = [1-z-v for z,v in zip(x, phat)]
    left = -sum((1-z)*r for z,r in zip(x,residual))
    right = sum(z*r for z,r in zip(x,residual))
    assert left == 1-2*n*(1-phat[0]) and right == 1-2*n*phat[-1]
    assert max(map(abs,error)) <= Q(n,8)*max(map(abs,residual))
    return {"decimal_file_n": n, "error_infinity": str(max(map(abs,error))),
            "analytic_affine_load_integrated_residual_infinity": str(max(map(abs,residual))),
            "left_true_minus_saved": str(left), "right_true_minus_saved": str(right)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--saved-p", help="read optional native uncompressed OpenFOAM ASCII field")
    args = parser.parse_args()
    report = {"green_checks":green_tests(),
              "schur": [schur(n,b,b-1) for n in (32,128,512) for b in (8,16)]}
    for m in range(2,8):
        for b in range(1,7):
            for r in range(b):
                schur(m*b,b,r)
    report["extra_offset_cases"] = 126
    if args.saved_p:
        report["source"] = native_file(args.saved_p)
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
