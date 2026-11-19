"""Finite RAW windows and an independent check of the moving Mellin residue.

Requires python-flint==0.9.0 and the published round-92 finite Green checker.
Only derived numerical bounds and exact finite algebra are written to stdout.
"""

import hashlib
import importlib.util
import json
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
from flint import acb, acb_series, arb, ctx


def load_raw_reader():
    path = Path(__file__).resolve().parents[1] / "ninetysecond" / "zeros_check.py"
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != "74f004261b0c21eedadee3dc9efb1d86f7f83729231d4b1e9340a61390a60e10":
        raise ValueError("The round-92 Green reader differs from the verified source")
    spec = importlib.util.spec_from_file_location("road_green_92", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, digest


def residue_polynomial(m, a, coefficients):
    """Coefficients in the scaled variable y = a*t, after removing a*exp(r*t)."""
    p = [F(0)] * m
    for j in range(1, m+1):
        for k in range(j):
            p[k] += (comb(m, j) * (-1)**j * a**(j-1-k)
                     * coefficients[j-1-k] / factorial(k))
    return p


def eval_poly(p, y):
    result = F(0)
    for coefficient in reversed(p):
        result = result*y + coefficient
    return result


def product_residue(m, a, t, coefficients):
    """Independent extraction of [z^-1](1-a/z)^m A(z) exp(t*z)."""
    negatives = [1]
    for _ in range(m):
        new = [F(0)]*(len(negatives)+1)
        for j, value in enumerate(negatives):
            new[j] += value
            new[j+1] -= a*value
        negatives = new
    exp_t = [F(1)]
    for k in range(1, m):
        exp_t.append(exp_t[-1]*t/k)
    return sum(negatives[j]*sum(coefficients[k]*exp_t[j-1-k] for k in range(j))
               for j in range(1, m+1))


def local_model():
    checks = 0
    for m in range(1,13):
        for a in (F(1,5), F(1,31), F(1,128)):
            coefficients = []
            for k in range(m):
                previous = coefficients[-1] if k else 0
                numerator_coefficient = int(k in (0,1,2))
                coefficients.append((numerator_coefficient-previous)/(1+a))
            p = residue_polynomial(m, a, coefficients)
            for y in (F(0), F(1,4), F(2), F(9,2)):
                assert a*eval_poly(p, y) == product_residue(m, a, y/a, coefficients)
                checks += 1
    laguerre_coefficients = residue_polynomial(2, F(1,16), [F(1), F(0)])
    assert laguerre_coefficients == [-2, 1]
    examples = []
    for denominator in [8,16,32,64]:
        a = F(1,denominator)
        first = a*eval_poly(laguerre_coefficients, F(2))
        second = a*eval_poly(laguerre_coefficients, 2+a/4)
        assert first == 0 and second == a*a/4
        examples.append({"a": str(a), "t=2/a": str(first), "t=2/a+1/4": str(second)})
    return {"rational_coefficient_and_residue_checks": checks,
            "double_pole_cancellation_in_the_model_after_removing_the_exponential": examples}


def first_zero(reader):
    rho = acb.zeta_zero(1)
    derivative = acb_series([rho, 1], 2).zeta()[1]
    assert not abs(derivative).contains(0)
    results = []
    for k in [5,10,15,20]:
        a = reader.ball(F(1, 2**k))
        pole = rho - a
        residue = pole.zeta()/(pole*derivative)
        assert abs(residue) > 0
        shift = a*a/64
        s = pole + shift
        original_field = (s.zeta()/(s+a).zeta()-1)/s - 1/((1+a).zeta()*(s-1))
        direct = shift*original_field
        relative_discrepancy = abs(direct/residue-1)
        assert relative_discrepancy < a/32
        reduced = abs(residue/a + 1/rho)/a
        assert 0 < reduced < 1
        results.append({"a": f"2^-{k}", "absolute_error_of_the_scaled_residue_divided_by_a":
                        reader.bracket(reduced, 13), "direct_field_relative_error_at_shift_a2_over_64":
                        reader.bracket(relative_discrepancy, 17)})
    return {"zero_ordinate": reader.bracket(rho.imag), "arithmetic_first_zero_probes": results}


def main():
    reader, source_hash = load_raw_reader()
    ctx.prec = 192
    # Each right endpoint is +1/2 in the ordinary logarithmic coordinate.
    windows = [reader.raw_window(n, F(1,4), F(1,4)+F(1, 2*n)) for n in (8,16,24,32)]
    result = {"flint_version_required": "0.9.0", "precision_bits": ctx.prec,
              "green_reader_sha256": source_hash,
              "actual_fixed_log_width_windows": windows, "local_algebra": local_model(),
              "arithmetic_residue": first_zero(reader)}
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
