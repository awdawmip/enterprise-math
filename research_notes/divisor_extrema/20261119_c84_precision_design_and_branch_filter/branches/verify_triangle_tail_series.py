#!/usr/bin/env python3
"""Independent rational-series check of the C84 exact triangle tail.

The geometric derivation is in triangle_geometry_review.md.  Only the already
certified square-root and zeta intervals are imported; no g quadrature or g
closed-form code is reused.  Every summation and tail bound uses Fraction.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import importlib.util
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
spec = importlib.util.spec_from_file_location(
    "c84_triangle_intervals", ROOT / "triangle" / "certify_constant.py"
)
intervals = importlib.util.module_from_spec(spec)
spec.loader.exec_module(intervals)


def moment(n):
    return F(4, (n + 1) * (n + 2) * (n + 3)) * sum(
        (F(2 ** (k + 1) - 1, (k + 2) * (n + 2 - k))
         for k in range(n + 2)), F(0)
    )


def term(n, radius):
    return F(comb(2 * n + 5, n), (2 * n + 5) * radius ** (2 * n + 5)) * moment(n)


def outward_decimal(interval, digits=24):
    scale = 10 ** digits
    lower = interval.lo * scale // intervals.Q
    upper = -((-interval.hi * scale) // intervals.Q)
    def show(n):
        return f"{n // scale}.{n % scale:0{digits}d}"
    return [show(lower), show(upper)]


def main():
    assert [moment(n) for n in range(4)] == [F(5, 6), F(29, 72), F(13, 45), F(19, 75)]
    radius, n_terms = 3, 256
    # For n >= 9, the Catalan-derived binomial ratio is <= 4.
    # M_(n+1) <= 2 M_n follows from the support 0 <= S <= 2.
    assert n_terms >= 9 and radius * radius > 8
    partial = sum((term(n, radius) for n in range(n_terms)), F(0))
    remainder = term(n_terms, radius) / (1 - F(8, radius * radius))
    I, Q = intervals.I, intervals.Q
    sqrt2, zeta = I.rat(2).sqrt(), intervals.ZETA
    si = I.cv(partial)
    ri = I.cv(remainder)
    series = I(si.lo, si.hi + ri.hi)
    result = sqrt2 / (2 * zeta * radius ** 3) + (6 * sqrt2 / zeta) * series

    saved = json.loads((ROOT / "triangle" / "certificate.json").read_text())
    previous = saved["tail"]
    old_lo = F(int(previous["lower_numerator"]), int(previous["denominator"]))
    old_hi = F(int(previous["upper_numerator"]), int(previous["denominator"]))
    # Independent certificates must overlap.  The original rectangle quadrature
    # is much wider; if later replaced by this series, exact equality is allowed.
    assert max(old_lo, F(result.lo, Q)) <= min(old_hi, F(result.hi, Q))
    out = {
        "method": "positive rational moment series; geometric tail ratio <= 8/R^2",
        "radius": radius,
        "terms": n_terms,
        "moments_0_to_3": [str(moment(n)) for n in range(4)],
        "tail_probability_coefficients_times_pi_squared": ["9/2", "15", "203/4", "936/5", "3762/5"],
        "series_remainder_bound": str(remainder),
        "tail_integral": result.json(),
        "strict_outward_decimal_enclosure": outward_decimal(result),
        "saved_certificate_overlap": True,
        "scope": "rational series independent of g quadrature; zeta and sqrt intervals reuse certified primitive arithmetic",
    }
    (HERE / "triangle_tail_series_checks.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n"
    )
    print(json.dumps({"checks": "passed", "tail_integral": result.json(),
                      "strict_outward_decimal_enclosure": outward_decimal(result)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
