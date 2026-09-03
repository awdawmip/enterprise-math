"""Finite no-pi cross-family consistency check for free research #1161.

This compares two independently defined internal completion constants without
assuming that either one is classical pi:

* #1161 Pi_*: bounded by the AGM dyadic certificate checker;
* #1159 tau: tau=2 W_inf, with exact Wallis partial product W_N and
  1 < W_inf/W_N <= (4N+2)/(4N+1).

Agreement of finite decimal cells is evidence/consistency only, not a proof
that Pi_*=tau.
"""

from __future__ import annotations

from fractions import Fraction

from check_free_research_1161_agm_dyadic_certificate import run as agm_run


def wallis_product(n: int) -> Fraction:
    if n < 1:
        raise ValueError("n must be positive")
    value = Fraction(1)
    for r in range(1, n + 1):
        value *= Fraction((2 * r) ** 2, (2 * r - 1) * (2 * r + 1))
    return value


def wallis_tau_bounds(n: int) -> tuple[Fraction, Fraction]:
    w = wallis_product(n)
    lower = 2 * w
    upper = lower * Fraction(4 * n + 2, 4 * n + 1)
    return lower, upper


def decimal_cell(x: Fraction, digits: int) -> int:
    scale = 10**digits
    return (x.numerator * scale) // x.denominator


def format_cell(cell: int, digits: int) -> str:
    text = str(cell)
    if len(text) <= digits:
        text = "0" * (digits + 1 - len(text)) + text
    return text[:-digits] + "." + text[-digits:]


def run() -> dict[str, object]:
    # #1159 finite rational Wallis certificate.
    wallis_n = 10_000
    tau_lo, tau_hi = wallis_tau_bounds(wallis_n)
    tau_cell_lo = decimal_cell(tau_lo, 4)
    tau_cell_hi = decimal_cell(tau_hi, 4)
    if tau_cell_lo != tau_cell_hi:
        raise AssertionError("tau bounds do not share the requested decimal cell")

    # #1161 independently certified endogenous Pi_* cell.
    agm = agm_run(bits=300, steps=2)
    agm_n2 = [row for row in agm if row[0] == 2]
    if agm_n2 != [(2, 7, "3.1415926")]:
        raise AssertionError(f"unexpected AGM n=2 certificate: {agm_n2!r}")

    tau_prefix = format_cell(tau_cell_lo, 4)
    agm_prefix = agm_n2[0][2][: 2 + 4]  # '3.' plus four decimal digits
    if tau_prefix != agm_prefix:
        raise AssertionError("independent completion cells disagree")

    return {
        "wallis_n": wallis_n,
        "tau_certified_decimal_cell_4": tau_prefix,
        "agm_step": 2,
        "agm_certified_decimal_places": 7,
        "agm_prefix": agm_n2[0][2],
        "shared_four_decimal_cell": tau_prefix,
        "equality_proved": False,
    }


if __name__ == "__main__":
    result = run()
    expected = {
        "wallis_n": 10_000,
        "tau_certified_decimal_cell_4": "3.1415",
        "agm_step": 2,
        "agm_certified_decimal_places": 7,
        "agm_prefix": "3.1415926",
        "shared_four_decimal_cell": "3.1415",
        "equality_proved": False,
    }
    if result != expected:
        raise SystemExit(f"unexpected cross-family output: {result!r}")
    for key, value in result.items():
        print(f"{key}={value}")
