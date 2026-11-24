#!/usr/bin/env python3
"""Exact finite checks of the geometric Green identities and positive bounds."""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import argparse
import hashlib
import json
import random

ROOT = Path(__file__).resolve().parent


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode()


def fixed_cases():
    rng = random.Random(20261124)
    rows = []
    shapes = [(a, b, m) for a, b in [(4, 3), (5, 4), (3, 2)]
              for m in range(2, 15)]
    shapes.append((4, 3, 40))
    for a, b, m in shapes:
        xs = [a**j * b**(m-j) for j in range(m+1)]
        patterns = {
            "flat": [0] + [1]*(m-1) + [0],
            "mixed": [0] + [rng.randrange(-40, 41) for _ in range(m-1)] + [0],
            "alternating": [0] + [(-1)**j*(10**6+j) for j in range(1, m)] + [0],
            "critical_plateau": [0] + [isqrt(x) for x in xs[1:-1]] + [0],
        }
        for pattern, residual in patterns.items():
            intercept, slope = rng.randrange(-20, 21), rng.randrange(-20, 21)
            qs = [intercept+slope*x+z for x, z in zip(xs, residual)]
            rows.append({"a": a, "b": b, "M": m, "pattern": pattern,
                         "x": xs, "q": qs})
    return {"schema": "RH_GEOMETRIC_GREEN_FIXED_INPUTS_V1",
            "seed": 20261124, "cases": rows}


def green(r, m, j, k):
    return ((r**min(j, k)-1)*(r**m-r**max(j, k))
            / ((r-1)*r**k*(r**m-1)))


def log_upper(r, terms=60):
    z = (r-1)/(r+1)
    lo = 2*sum((z**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    tail = 2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
    return lo+tail


def below_surd_multiple(lhs, rhs, a, b):
    # C_r^2 = c0+c1*sqrt(a*b), checked without numerical square roots.
    c0 = F(a*a+6*a*b+b*b, (a-b)**2)
    c1 = F(4*(a+b), (a-b)**2)
    difference = lhs-c0*rhs
    return difference <= 0 or difference**2 <= c1*c1*a*b*rhs*rhs


def verify(data):
    kernel_cache = {}
    impulses = 0
    integer_points = 0
    maximum_ratio = F(0)
    maximum_case = None
    results = []
    for index, case in enumerate(data["cases"]):
        a, b, m = case["a"], case["b"], case["M"]
        r = F(a, b)
        xs = list(map(F, case["x"]))
        qs = list(map(F, case["q"]))
        assert 1 < r <= 2 and all(xs[j+1] == r*xs[j] for j in range(m))
        key = a, b, m
        if key not in kernel_cache:
            kernel = [[F(0)]*(m+1) for _ in range(m+1)]
            for j in range(1, m):
                for k in range(1, m):
                    kernel[j][k] = green(r, m, j, k)
                    assert kernel[j][k] > 0
                    unscaled_bound = (F(1) if j >= k else r**(j-k))/(r-1)
                    assert kernel[j][k] <= unscaled_bound
            for k in range(1, m):
                for j in range(1, m):
                    value = ((r+1)*kernel[j][k]-r*kernel[j-1][k]
                             -kernel[j+1][k])
                    assert value == (1 if j == k else 0)
                    impulses += 1
            kernel_cache[key] = kernel
        kernel = kernel_cache[key]
        chord = [qs[0]+(x-xs[0])*(qs[-1]-qs[0])/(xs[-1]-xs[0]) for x in xs]
        residual = [q-j for q, j in zip(qs, chord)]
        ts = [F(0)]*(m+1)
        forcing = [F(0)]*(m+1)
        for j in range(1, m):
            ts[j] = ((qs[j]-qs[j-1])/(xs[j]-xs[j-1])
                     -(qs[j+1]-qs[j])/(xs[j+1]-xs[j]))
            forcing[j] = (r-1)*xs[j]*ts[j]
            assert forcing[j] == (r+1)*qs[j]-r*qs[j-1]-qs[j+1]
        for j in range(1, m):
            assert sum((kernel[j][k]*forcing[k] for k in range(1, m)), F(0)) == residual[j]
            assert max(residual[j], 0) <= sum(
                (kernel[j][k]*max(forcing[k], 0) for k in range(1, m)), F(0))
        node_energy = sum((max(residual[j], 0)**2/xs[j] for j in range(1, m)), F(0))
        tent_energy = sum((xs[j]*max(ts[j], 0)**2 for j in range(1, m)), F(0))
        assert below_surd_multiple(node_energy, tent_energy, a, b)
        if tent_energy:
            ratio = node_energy/tent_energy
            if ratio > maximum_ratio:
                maximum_ratio, maximum_case = ratio, index
        scanned = 0
        if m <= 4:
            discrete = F(0)
            for j in range(m):
                left, right = int(xs[j]), int(xs[j+1])
                for n in range(left, right):
                    z = ((right-n)*residual[j]+(n-left)*residual[j+1])/(right-left)
                    discrete += max(z, 0)**2/(n*n)
                    scanned += 1
            # The closed right endpoint is retained; its residual is exactly zero.
            discrete += max(residual[-1], 0)**2/(xs[-1]**2)
            scanned += 1
            assert discrete <= (log_upper(r)+1/xs[0])*node_energy
            integer_points += scanned
        results.append({"case": index, "M": m, "pattern": case["pattern"],
                        "integer_points_checked": scanned,
                        "green_identity": True, "positive_comparison": True,
                        "sharp_constant_energy_inequality": True})
    return {
        "schema": "RH_GEOMETRIC_GREEN_CERTIFICATE_V1", "status": "PASS",
        "arithmetic": "Exact rational arithmetic; quadratic-surd comparison by sign-safe squaring; logarithm upper bound by a positive convergent series with explicit tail.",
        "cases": len(results), "distinct_geometries": len(kernel_cache),
        "green_impulse_entries_checked": impulses,
        "closed_integer_points_checked": integer_points,
        "maximum_observed_energy_ratio_squared": {
            "case": maximum_case, "numerator": str(maximum_ratio.numerator),
            "denominator": str(maximum_ratio.denominator),
            "diagnostic_decimal": float(maximum_ratio)},
        "large_M_policy": "For M>4 only finite node/kernel algebra is evaluated; no exponentially long integer road is scanned.",
        "results": results,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT/"geometric_green_certificate.json")
    args = parser.parse_args()
    fixed = ROOT/"fixed_green_cases.json"
    if fixed.exists():
        data = json.loads(fixed.read_text())
    else:
        data = fixed_cases()
        fixed.write_bytes(canonical(data))
    certificate = verify(data)
    certificate["fixed_input_sha256"] = hashlib.sha256(fixed.read_bytes()).hexdigest()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(canonical(certificate))
    print(json.dumps({key: certificate[key] for key in [
        "status", "cases", "distinct_geometries", "green_impulse_entries_checked",
        "closed_integer_points_checked", "maximum_observed_energy_ratio_squared"]}))


if __name__ == "__main__":
    main()
