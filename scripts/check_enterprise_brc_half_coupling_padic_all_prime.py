#!/usr/bin/env python3
"""Exact regression checker for the Enterprise BRC half-coupling p-adic target.

This script is regression support only.  It does not constitute an all-prime proof.
It uses two independent exact-integer evaluators on a small range and the faster
hypergeometric recurrence on the full requested range.
"""
from __future__ import annotations

import argparse
import json
from math import comb, isqrt


def primes_upto(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for q in range(2, isqrt(limit) + 1):
        if sieve[q]:
            start = q * q
            sieve[start : limit + 1 : q] = b"\x00" * (((limit - start) // q) + 1)
    return [q for q in range(2, limit + 1) if sieve[q]]


def chi_minus_three(p: int) -> int:
    """For primes p>3, (-3/p)=(p/3)."""
    if p <= 3:
        raise ValueError("p must exceed 3")
    return 1 if p % 3 == 1 else -1


def summation_recurrence(p: int) -> int:
    """Evaluate S_p modulo p^3 by the exact hypergeometric recurrence."""
    modulus = p**3
    a = 1  # a_0
    total = 1
    for k in range(p - 1):
        numerator = (2 * k + 1) * (3 * k + 1) * (3 * k + 2)
        denominator = 36 * (k + 1) ** 3
        # k+1 < p, hence denominator is invertible modulo p^3.
        a = a * (numerator % modulus) * pow(denominator, -1, modulus) % modulus
        n = k + 1
        total = (total + (6 * n + 1) * a) % modulus
    return total


def summation_direct(p: int) -> int:
    """Independent exact evaluator from binomial integers and 216^{-n}."""
    modulus = p**3
    inv216 = pow(216, -1, modulus)
    power = 1
    total = 0
    for n in range(p):
        integer_kernel = comb(2 * n, n) ** 2 * comb(3 * n, n)
        total = (total + (6 * n + 1) * (integer_kernel % modulus) * power) % modulus
        power = power * inv216 % modulus
    return total


def vp_integer(value: int, p: int) -> int:
    out = 0
    while value and value % p == 0:
        value //= p
        out += 1
    return out


def predicted_kernel_valuation(n: int, p: int) -> int:
    """For 0<=n<p: v_p(C(2n,n)^2 C(3n,n))."""
    return (2 * n) // p + (3 * n) // p


def block_diagnostic(p: int) -> dict[str, object]:
    """Split exact weighted residues by the kernel valuation 0,1,2,3."""
    modulus = p**3
    inv216 = pow(216, -1, modulus)
    power = 1
    counts = [0, 0, 0, 0]
    residues = [0, 0, 0, 0]
    for n in range(p):
        integer_kernel = comb(2 * n, n) ** 2 * comb(3 * n, n)
        valuation = vp_integer(integer_kernel, p)
        predicted = predicted_kernel_valuation(n, p)
        if valuation != predicted:
            raise AssertionError((p, n, valuation, predicted))
        counts[valuation] += 1
        residues[valuation] = (
            residues[valuation]
            + (6 * n + 1) * (integer_kernel % modulus) * power
        ) % modulus
        power = power * inv216 % modulus
    return {
        "p": p,
        "counts_by_vp_0_1_2_3": counts,
        "weighted_residues_mod_p3_by_vp_0_1_2_3": residues,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=10_000)
    parser.add_argument("--crosscheck-max-prime", type=int, default=199)
    args = parser.parse_args()

    primes = [p for p in primes_upto(args.max_prime) if p > 3]
    failures: list[dict[str, int]] = []
    for p in primes:
        got = summation_recurrence(p)
        expected = (p * chi_minus_three(p)) % (p**3)
        if got != expected:
            failures.append({"p": p, "got": got, "expected": expected})

    cross_primes = [p for p in primes if p <= args.crosscheck_max_prime]
    cross_failures: list[dict[str, int]] = []
    valuation_failures: list[dict[str, int]] = []
    valuation_checks = 0
    for p in cross_primes:
        fast = summation_recurrence(p)
        direct = summation_direct(p)
        if fast != direct:
            cross_failures.append({"p": p, "recurrence": fast, "direct": direct})
        for n in range(p):
            integer_kernel = comb(2 * n, n) ** 2 * comb(3 * n, n)
            actual = vp_integer(integer_kernel, p)
            predicted = predicted_kernel_valuation(n, p)
            valuation_checks += 1
            if actual != predicted:
                valuation_failures.append(
                    {"p": p, "n": n, "actual": actual, "predicted": predicted}
                )

    diagnostic_primes = [p for p in (5, 7, 11, 13, 17, 19, 23) if p <= args.max_prime]
    diagnostics = [block_diagnostic(p) for p in diagnostic_primes]

    ok = not failures and not cross_failures and not valuation_failures
    result = {
        "schema": "ENTERPRISE_BRC_HALF_COUPLING_PADIC_REGRESSION_V1",
        "status": "PASS" if ok else "FAIL",
        "target": "S_p == p*(-3/p) (mod p^3)",
        "max_prime_bound": args.max_prime,
        "primes_tested": len(primes),
        "largest_prime_tested": primes[-1] if primes else None,
        "target_failures": failures,
        "independent_direct_crosscheck_max_prime": args.crosscheck_max_prime,
        "independent_direct_crosschecks": len(cross_primes),
        "independent_direct_crosscheck_failures": cross_failures,
        "valuation_formula_checks": valuation_checks,
        "valuation_formula_failures": valuation_failures,
        "block_diagnostics": diagnostics,
        "proof_status": "FINITE_REGRESSION_ONLY_NOT_A_PROOF",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
