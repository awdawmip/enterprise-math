#!/usr/bin/env python3
"""Finite proof-translation falsifier; this program does not prove the imported theorem.

Fixed eight discriminating primes, no inherited 77-prime scan and no LIFT.
All arithmetic before the declared modular observations is exact Fraction.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import types

ROOT = Path(__file__).resolve().parent
PRIMES = (13, 19, 37, 43, 61, 67, 109, 139)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def load_frozen_sources():
    manifest = json.loads((ROOT / "REUSED_SOURCE_MANIFEST.json").read_text())
    for item in manifest["files"]:
        data = (ROOT / item["bundle_path"]).read_bytes()
        require(hashlib.sha256(data).hexdigest() == item["sha256"], "source SHA-256 mismatch")
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        require(blob == item["git_blob"], "source Git blob mismatch")
    modules = []
    for name, suffix in (("frozen_parent", "reflected_derivative_product_bridge"),
                         ("frozen_legendre", "terminating_jacobi_jet_certificate_independent")):
        path = ROOT / ("check_enterprise_brc_half_coupling_inert_plus_" + suffix + ".py")
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        modules.append(module)
    # A private namespace exposes the unmodified flat files to their original
    # relative imports. No installed enterprise_math package is used.
    package_name = "_cm24_frozen_brc_subset"
    package = types.ModuleType(package_name)
    package.__path__ = [str(ROOT)]
    package.__package__ = package_name
    sys.modules[package_name] = package
    brc_weighted = importlib.import_module(package_name + ".brc_weighted")
    return manifest, modules[0], modules[1], brc_weighted


def fraction_text(value):
    return f"{value.numerator}/{value.denominator}"


def rational_valuation(value, prime):
    """Task-local scalar observer; zero is deliberately outside this interface."""
    require(value != 0, "valuation of zero not used in this certificate")
    numerator, denominator = abs(value.numerator), value.denominator
    result = 0
    while numerator % prime == 0:
        numerator //= prime
        result += 1
    while denominator % prime == 0:
        denominator //= prime
        result -= 1
    return result


def theorem_coefficients(prime):
    # A_k=(1/2)_k(1/3)_k(2/3)_k/(k!)^3 * (1/2)^k.
    terms = [Fraction(1)]
    for k in range(prime - 1):
        terms.append(terms[-1] * Fraction((2*k+1)*(3*k+1)*(3*k+2), 36*(k+1)**3))
    return terms


def legendre_symbol(value, prime):
    residue = pow(value % prime, (prime - 1) // 2, prime)
    return -1 if residue == prime - 1 else residue


def check_prime(prime, parent, legendre, brc):
    require(prime in set(parent.primes_below(prime + 1)), "input is not prime")
    require(prime % 24 in (13, 19), "outside frozen target residue classes")
    m = (prime - 1) // 6
    require(prime == 6*m + 1, "integer parameter mismatch")
    inv2 = pow(2, -1, prime)
    require(legendre_symbol(inv2, prime) == -1, "wrong (1-lambda)/p sign")
    require(legendre_symbol(-6, prime) == -1, "wrong CM inertness sign")
    require(Fraction(1, 6) == -m + Fraction(prime, 6), "first displacement mismatch")
    require(Fraction(1, 3) == -2*m + Fraction(prime, 3), "second displacement mismatch")

    bs = parent.direct_Bs(prime)
    aa = theorem_coefficients(prime)
    require(aa[1] == Fraction(1, 18), "hypergeometric parameter/argument normalization mismatch")
    valuations = [rational_valuation(b, prime) for b in bs]
    require(valuations == [0 if k <= m else 1 if k <= 2*m else 2 for k in range(prime)],
            "frozen coefficient valuation interface mismatch")
    convolution = [sum((bs[i] * bs[n-i] for i in range(max(0, n-prime+1), min(prime-1, n)+1)),
                       Fraction(0)) for n in range(2*prime-1)]
    require(convolution[:prime] == aa, "low-degree finite Clausen coefficient identity failed")

    g = sum(bs, Fraction(0))
    h = sum(((12*k+1)*b for k, b in enumerate(bs)), Fraction(0))
    w = sum(((6*k+1)*a for k, a in enumerate(aa)), Fraction(0))
    tail = sum(((6*n+1)*convolution[n] for n in range(prime, 2*prime-1)), Fraction(0))
    require(g*h == w+tail, "6-versus-12 weighted finite Clausen identity failed")
    tail_pairs = [(i, j) for i in range(prime) for j in range(prime) if i+j >= prime]
    pair_valuation_min = min(valuations[i] + valuations[j] for i, j in tail_pairs)
    require(pair_valuation_min >= 2, "a discarded tail branch is visible modulo p^2")
    require(parent.frac_mod(tail, prime**2) == 0, "tail quotient lost p^2 precision")
    require(parent.frac_mod(w, prime**2) == prime, "imported weighted theorem finite instance failed")
    require(parent.frac_mod(g*h, prime**2) == prime, "translated product congruence failed")

    q0, qp = legendre.q_value_and_derivative(m, prime)
    require(q0 == 0 and qp != 0, "accepted CM0/SIMPLE interface failed")
    unit = -6*qp % prime
    require(parent.frac_mod(h, prime) == unit, "frozen h-to-Q derivative normalization failed")
    g_mod_p2 = parent.frac_mod(g, prime**2)
    require(g_mod_p2 % prime == 0, "division by p not integral")
    divided_mod_p = g_mod_p2 // prime
    require(divided_mod_p == parent.frac_mod(g / prime, prime), "division/readout order mismatch")
    require(divided_mod_p * unit % prime == 1, "UR finite instance failed")

    # The existing positive CWM implementation checks this exact positive branch carrier.
    # The signed derivative remains a separate modular readout and is never fed to CWM.
    cwm_g = brc.cwm_from_positive_weights(bs)
    cwm_h = brc.cwm_from_positive_weights([(12*k+1)*b for k, b in enumerate(bs)])
    cwm_product = brc.cwm_propagate(cwm_g, cwm_h)
    require(cwm_g.count == prime and cwm_g.total == g, "CWM g carrier mismatch")
    require(cwm_h.count == prime and cwm_h.total == h, "CWM h carrier mismatch")
    require(cwm_product.count == prime**2 and cwm_product.total == g*h, "CWM product mismatch")

    wrong_w = sum(((12*k+1)*a for k, a in enumerate(aa)), Fraction(0))
    wrong_h = sum(((6*k+1)*b for k, b in enumerate(bs)), Fraction(0))
    faults = {
        "3f2_weight_12_instead_of_6": (parent.frac_mod(wrong_w, prime**2)-prime) % (prime**2),
        "2f1_weight_6_instead_of_12": (divided_mod_p*parent.frac_mod(wrong_h, prime)-1) % prime,
        "ordinary_instead_of_supersingular_sign": (parent.frac_mod(w, prime**2)+prime) % (prime**2),
        "positive_instead_of_negative_Q_derivative": (divided_mod_p*(6*qp)-1) % prime,
        "g_reduced_mod_p_before_dividing_p": ((parent.frac_mod(g, prime)//prime)*unit-1) % prime,
    }
    require(all(value != 0 for value in faults.values()), "a deliberate bad translation escaped")
    record = {
        "p": prime, "class_mod_24": prime % 24, "m": m,
        "cm_inert_symbol": -1, "argument_symbol": -1, "supersingular_theorem_sign": -1,
        "combined_theorem_multiplier": 1,
        "g_mod_p2": g_mod_p2, "h_mod_p": parent.frac_mod(h, prime),
        "W_mod_p2": parent.frac_mod(w, prime**2), "gh_mod_p2": parent.frac_mod(g*h, prime**2),
        "tail_mod_p2": 0, "tail_pair_count": len(tail_pairs), "tail_pair_valuation_min": pair_valuation_min,
        "Q_mod_p": q0, "Q_derivative_mod_p": qp, "g_over_p_mod_p": divided_mod_p,
        "UR_product_mod_p": 1, "clausen_low_coefficients_checked": prime,
        "cwm_counts": [cwm_g.count, cwm_h.count, cwm_product.count],
        "negative_control_nonzero_defects": faults,
    }
    trace = {
        "p": prime, "m": m, "B_k": [fraction_text(x) for x in bs],
        "A_k": [fraction_text(x) for x in aa], "B_valuations": valuations,
        "g": fraction_text(g), "h": fraction_text(h), "W": fraction_text(w), "tail": fraction_text(tail),
        "provenance": {
            "input_branch_ids": "(p,k), 0<=k<p; arrays retain that exact order",
            "product_branch_ids": "(p,i,j), 0<=i,j<p",
            "product_branch_weight": "B_i * (12*j+1) * B_j",
            "weighted_Clausen_coalescence": "at n=i+j, swap-paired weight is (6*n+1)*B_i*B_j",
            "tail_domain": "all ordered (i,j) with 0<=i,j<p and i+j>=p",
            "reconstruction": "Full ordered pair carrier is exactly reconstructed from B_k and this domain; no historical path equality is asserted.",
        },
    }
    return record, trace


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "RUN.json")
    args = parser.parse_args()
    started = time.monotonic()
    manifest, parent, legendre, brc = load_frozen_sources()
    records, traces = [], []
    for prime in PRIMES:
        record, trace = check_prime(prime, parent, legendre, brc)
        records.append(record)
        traces.append(trace)
    raw_trace = json.dumps(traces, sort_keys=True, separators=(",", ":")).encode()
    trace_path = args.output.with_name("EXACT_TRACE.json.gz")
    trace_path.write_bytes(gzip.compress(raw_trace, mtime=0))
    report = {
        "status": "PASS", "finite_falsification_only_not_theorem_proof": True,
        "scope": "First-digit UR proof translation; no LIFT or mod-p^3 claim",
        "source_commit": manifest["source_commit"], "fixed_primes": list(PRIMES),
        "class_counts": {str(c): sum(p % 24 == c for p in PRIMES) for c in (13, 19)},
        "import_interface": {"theorem": "Chisholm-Deines-Long-Nebe-Swisher 2013 Theorem 1",
                             "d": 3, "a": 6, "lambda": "1/2", "reduction": "supersingular",
                             "CM_good_reduction_all_prime_applicability": "external proof obligation; not established by this checker"},
        "reused_calls": {"frozen_parent": ["direct_Bs", "frac_mod", "primes_below"],
                         "frozen_legendre": ["q_value_and_derivative"],
                         "brc_weighted": ["cwm_from_positive_weights", "cwm_propagate"]},
        "reuse_resolution": "REUSE_EXECUTED", "records": records,
        "negative_control_cases_detected": sum(len(r["negative_control_nonzero_defects"]) for r in records),
        "trace": {"path": trace_path.name, "uncompressed_sha256": hashlib.sha256(raw_trace).hexdigest(),
                  "gzip_sha256": hashlib.sha256(trace_path.read_bytes()).hexdigest(),
                  "uncompressed_bytes": len(raw_trace), "gzip_bytes": trace_path.stat().st_size},
        "elapsed_seconds": round(time.monotonic()-started, 6),
    }
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"status": "PASS", "primes": len(records), "negative_controls_detected": report["negative_control_cases_detected"],
                      "finite_only": True, "output": str(args.output), "elapsed_seconds": report["elapsed_seconds"]}))


if __name__ == "__main__":
    main()
