#!/usr/bin/env python3
"""Reproducible stationary Markov-sign fourth-cumulant sweep.

One existing mechanism, thirty parameter cases; timepoints are not independent
replicates. Decimal(50) trajectory computation, binary64 least-squares diagnostics.
Run from anywhere; defaults save beside this source. --audit-only skips export.
"""
from __future__ import annotations

import argparse
import csv
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
import gzip
import hashlib
import io
import json
import math
from pathlib import Path
import platform
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
from enterprise_math.brc_transport import Affine, EffectHistogram, eye, ma, point_moment, sm

PRECISION = 50
HORIZON = 65536
TRAIN_WINDOWS = [(1, 16), (129, 512), (2049, 8192), (8193, 32768)]
FIXED_MODELS = ["constant", "C/n", "C/n^2", "C/n+D/n^2", "signed_free_power"]
REGULAR_RHOS = ["-1", "-0.999999", "-0.9999", "-0.999", "-0.99", "-0.9",
                "-0.75", "-0.5", "-0.4", "-0.3", "-0.2", "-0.1", "0", "0.1",
                "0.25", "0.5", "0.75", "0.9", "0.99", "0.999", "0.9999",
                "0.999999", "1"]
CRITICAL_OFFSETS = ["-0.01", "-0.0001", "-0.000001", "0", "0.000001", "0.0001", "0.01"]
SAMPLES = set([1, 2, 3, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048,
               4096, 8192, 16384, 32768, 65536])


def cases(precision=PRECISION):
    with localcontext() as ctx:
        ctx.prec = precision
        star = D(3).sqrt() - 2
        out = [{"id": "rho_" + r.replace("-", "m").replace(".", "p"),
                "expression": r, "rho": D(r), "offset": None} for r in REGULAR_RHOS]
        out += [{"id": "star_" + o.replace("-", "m").replace(".", "p"),
                 "expression": "sqrt(3)-2" + ("+" + o if not o.startswith("-") else o),
                 "rho": star + D(o), "offset": o} for o in CRITICAL_OFFSETS]
        return sorted(out, key=lambda c: c["rho"])


def stable_step(rho, a, variance, h, kappa):
    """All right-hand sides use the old state; works with Decimal or Fraction."""
    t = rho * a
    t2 = t * t
    return (t + 1, variance + 2*t + 1,
            rho*h - 6*t2 - 6*t - 2,
            kappa + 4*rho*h - 12*t2 - 8*t - 2)


def conditional_step(raw, rho):
    zero = raw[-1][0] * 0
    out = {s: [zero] * 5 for s in (-1, 1)}
    for source in (-1, 1):
        for target in (-1, 1):
            p = (1 + rho*source*target)/2
            for k in range(5):
                out[target][k] += p * sum(math.comb(k, j) * target**(k-j) * raw[source][j]
                                          for j in range(k+1))
    return out


def theory(case):
    r = case["rho"]
    if abs(r) == 1:
        return {"status": "NONMIXING_ENDPOINT", "C": None, "E": None,
                "gamma": "-2" if r == 1 else "odd n: -2; even n: undefined (zero variance)"}
    diffusion = (1+r)/(1-r)
    b = diffusion - 3*diffusion**3
    v0 = -2*r/(1-r)**2
    k0 = 4*r*(4*r*r+7*r+4)/(1-r)**4
    c = b/diffusion**2
    e = 4*r*(2*r*r-r+2)/((1-r)**2*(1+r)**2)
    critical = case["offset"] == "0"
    if critical:
        # The declared parameter is algebraic; these identities are exact.
        b, c, v0, k0, e = D(0), D(0), D(1)/3, D(-1), D(-3)
    crossover = -e/c if c else None
    cumulant_zero = -k0/b if b else None
    return {"status": "FIXED_RHO_MIXING_ASYMPTOTIC",
            "D": str(diffusion), "B": str(b), "v0": str(v0), "k0": str(k0),
            "C": str(c), "E": str(e), "critical_exact": critical,
            "positive_asymptotic_zero_estimate_n": str(crossover) if crossover and crossover > 0 else None,
            "positive_linear_cumulant_zero_estimate_n": str(cumulant_zero) if cumulant_zero and cumulant_zero > 0 else None,
            "zero_estimate_warning": "Formal roots of truncated expansions, not observed or guaranteed zero crossings; invalid before transients decay. The linear-cumulant root uses n*B+k0=0.",
            "correlation_relaxation_scale": str(1/(1-abs(r))),
            "expansion": "gamma4=C/n+E/n^2+O(n^-3)+polynomial(n)*rho^n/n^2; fixed |rho|<1"}


def score(y, prediction):
    error = prediction - y
    rmse = float(np.sqrt(np.mean(error*error)))
    rms_y = float(np.sqrt(np.mean(y*y)))
    maximum = float(np.max(np.abs(y)))
    return {"n": int(len(y)), "rmse": rmse,
            "normalized_rmse": rmse/rms_y if rms_y else None,
            "max_absolute_error": float(np.max(np.abs(error))),
            "normalized_max_absolute_error": float(np.max(np.abs(error)))/maximum if maximum else None,
            "wrong_sign_count": int(np.count_nonzero(prediction*y < 0)),
            "true_zero_count": int(np.count_nonzero(y == 0)),
            "predicted_zero_count": int(np.count_nonzero(prediction == 0))}


def fit_all(values, horizon):
    n_all = np.arange(1, horizon+1, dtype=float)
    valid = np.isfinite(values)
    output = []
    for lo, hi in TRAIN_WINDOWS:
        if hi >= horizon:
            continue
        train = valid & (n_all >= lo) & (n_all <= hi)
        held = valid & (n_all > hi)
        nt, nh = n_all[train], n_all[held]
        yt, yh = values[train], values[held]
        window = {"train": [lo, hi], "heldout": [hi+1, horizon],
                  "train_valid": int(sum(train)), "heldout_valid": int(sum(held)),
                  "train_undefined": hi-lo+1-int(sum(train)),
                  "heldout_undefined": horizon-hi-int(sum(held)), "models": {}}
        for model in FIXED_MODELS:
            if model == "signed_free_power":
                if np.any(yt == 0) or not (np.all(yt > 0) or np.all(yt < 0)):
                    window["models"][model] = {"status": "EXCLUDED_TRAIN_SIGN_CHANGE_OR_ZERO",
                        "reason": "No real logarithm of absolute value is fitted across training zeros or mixed signs."}
                    continue
                # Uses training signs only. A heldout sign reversal is a scored failure.
                exponent, log_amplitude = np.polyfit(np.log(nt), np.log(np.abs(yt)), 1)
                amplitude = float(np.sign(yt[0])*np.exp(log_amplitude))
                prediction_train = amplitude*np.exp(exponent*np.log(nt))
                prediction_held = amplitude*np.exp(exponent*np.log(nh))
                coefficients = {"signed_amplitude": amplitude, "power_exponent": float(exponent)}
                objective = "least squares in log(abs(gamma4)); training sign retained"
            else:
                powers = {"constant": [0], "C/n": [-1], "C/n^2": [-2], "C/n+D/n^2": [-1, -2]}[model]
                x = np.column_stack([nt**p for p in powers])
                scale = np.linalg.norm(x, axis=0)
                coef = np.linalg.lstsq(x/scale, yt, rcond=None)[0]/scale
                prediction_train = x @ coef
                prediction_held = np.column_stack([nh**p for p in powers]) @ coef
                coefficients = {str(p): float(c) for p, c in zip(powers, coef)}
                objective = "ordinary least squares on signed gamma4; normalized design columns"
            window["models"][model] = {"status": "FIT", "coefficients": coefficients,
                "objective": objective, "training": score(yt, prediction_train),
                "heldout": score(yh, prediction_held)}
        output.append(window)
    return output


def fraction_audit():
    checks = {"rational_parameter_cases": 0, "exact_stable_vs_raw_timepoints": 0,
              "production_BRC_degree_two_timepoints": 0, "explicit_distribution_timepoints": 0}
    # Includes mixing, both endpoints, independent case and extreme rational inputs.
    for rho in map(F, ["-1", "-999999/1000000", "-1/2", "-3/10", "0", "1/2", "999999/1000000", "1"]):
        checks["rational_parameter_cases"] += 1
        a = v = h = k4 = F(0)
        raw = {s: [F(1, 2), F(0), F(0), F(0), F(0)] for s in (-1, 1)}
        matrices = {s: sm(F(1, 2), point_moment((0,))) for s in (-1, 1)}
        edges = {(s, t): EffectHistogram.from_terms(1, [((1+rho*s*t)/2, Affine(eye(1), (F(t),)), 1)])
                 for s in (-1, 1) for t in (-1, 1) if (1+rho*s*t)/2 > 0}
        dist = {(s, 0): F(1, 2) for s in (-1, 1)}
        for n in range(1, 33):
            a, v, h, k4 = stable_step(rho, a, v, h, k4)
            raw = conditional_step(raw, rho)
            rv = sum(raw[s][2] for s in (-1, 1))
            assert v == rv
            assert k4 == sum(raw[s][4] for s in (-1, 1))-3*rv*rv
            assert a == sum(s*raw[s][1] for s in (-1, 1))
            assert h == sum(s*raw[s][3] for s in (-1, 1))-3*v*a
            assert v == n+2*sum((n-j)*rho**j for j in range(1, n))
            checks["exact_stable_vs_raw_timepoints"] += 1
            if n <= 16:
                nxt = {s: ((F(0), F(0)), (F(0), F(0))) for s in (-1, 1)}
                for (s, t), edge in edges.items():
                    nxt[t] = ma(nxt[t], edge.moment_action(matrices[s]))
                matrices = nxt
                for s in (-1, 1):
                    assert matrices[s] == ((raw[s][2], raw[s][1]), (raw[s][1], raw[s][0]))
                checks["production_BRC_degree_two_timepoints"] += 1
            if n <= 10:
                nxt_dist = {}
                for (s, x), weight in dist.items():
                    for t in (-1, 1):
                        key = (t, x+t)
                        nxt_dist[key] = nxt_dist.get(key, F(0))+weight*(1+rho*s*t)/2
                dist = nxt_dist
                for s in (-1, 1):
                    assert [sum(p*x**j for (t, x), p in dist.items() if t == s) for j in range(5)] == raw[s]
                checks["explicit_distribution_timepoints"] += 1
    return checks


def decimal_raw_audit():
    """Independent unnormalized conditional raw moments at 80 digits to n=4096."""
    result = {"precision": 80, "horizon": 4096, "parameter_cases": 0,
              "compared_timepoints": 0, "max_scaled_variance_error": "0", "max_scaled_kappa_error": "0"}
    maxv = maxk = D(0)
    with localcontext() as ctx:
        ctx.prec = 80
        selected = [c for c in cases(80) if c["id"] in {"star_0", "star_m0p000001", "star_0p000001", "rho_m0p999999", "rho_0p999999", "rho_m0p5"}]
        for case in selected:
            rho = case["rho"]
            a = v = h = k4 = D(0)
            raw = {s: [D("0.5"), D(0), D(0), D(0), D(0)] for s in (-1, 1)}
            for n in range(1, 4097):
                a, v, h, k4 = stable_step(rho, a, v, h, k4)
                raw = conditional_step(raw, rho)
                rv = sum(raw[s][2] for s in (-1, 1))
                rk = sum(raw[s][4] for s in (-1, 1))-3*rv*rv
                maxv = max(maxv, abs(v-rv)/max(D(1), abs(rv)))
                maxk = max(maxk, abs(k4-rk)/max(D(1), abs(rk)))
                result["compared_timepoints"] += 1
            result["parameter_cases"] += 1
    assert maxv < D("1e-65") and maxk < D("1e-62"), (maxv, maxk)
    result.update(max_scaled_variance_error=str(maxv), max_scaled_kappa_error=str(maxk), status="PASS")
    return result


def audit_precision(saved_samples, horizon):
    result = {"reference_precision": 80, "computed_precision": PRECISION, "parameter_cases": 0,
              "compared_sample_timepoints": 0, "max_scaled_variance_error": "0", "max_scaled_kappa_error": "0"}
    maxv = maxk = D(0)
    with localcontext() as ctx:
        ctx.prec = 80
        selected = [c for c in cases(80) if c["id"] in {"star_0", "star_m0p000001", "star_0p000001", "rho_m0p999999", "rho_0p999999"}]
        for case in selected:
            a = v = h = k4 = D(0)
            for n in range(1, horizon+1):
                a, v, h, k4 = stable_step(case["rho"], a, v, h, k4)
                if n in saved_samples[case["id"]]:
                    oldv, oldk = saved_samples[case["id"]][n]
                    maxv = max(maxv, abs(v-D(oldv))/max(D(1), abs(v)))
                    maxk = max(maxk, abs(k4-D(oldk))/max(D(1), abs(k4)))
                    result["compared_sample_timepoints"] += 1
            result["parameter_cases"] += 1
    assert maxv < D("1e-38") and maxk < D("1e-35"), (maxv, maxk)
    result.update(max_scaled_variance_error=str(maxv), max_scaled_kappa_error=str(maxk), status="PASS")
    return result


def run_case(case, output, horizon):
    path = output / ("markov_"+case["id"]+".csv.gz")
    values = np.full(horizon, np.nan)
    samples = []
    precision_samples = {}
    flip_count = zero_count = null_count = 0
    first_flips = []
    previous = None
    a = v = h = k4 = D(0)
    rho = case["rho"]
    with path.open("wb") as binary:
        with gzip.GzipFile(filename="", mode="wb", fileobj=binary, compresslevel=9, mtime=0) as gz:
            with io.TextIOWrapper(gz, encoding="utf-8", newline="") as stream:
                writer = csv.writer(stream, lineterminator="\n")
                writer.writerow(["case", "n", "variance", "kappa4", "gamma4", "status"])
                for n in range(1, horizon+1):
                    a, v, h, k4 = stable_step(rho, a, v, h, k4)
                    assert v >= 0
                    gamma = k4/(v*v) if v else None
                    status = "OK" if v else "ZERO_VARIANCE_NORMALIZATION_UNDEFINED"
                    if gamma is not None:
                        values[n-1] = float(gamma)
                        sign = 1 if gamma > 0 else -1 if gamma < 0 else 0
                        if previous is not None and previous[1]*sign < 0:
                            flip_count += 1
                            if len(first_flips) < 32:
                                first_flips.append([previous[0], n])
                        previous = (n, sign)
                        zero_count += int(sign == 0)
                    else:
                        null_count += 1
                        previous = None  # Never bridge an undefined timepoint.
                    writer.writerow([case["id"], n, format(v, ".17g"), format(k4, ".17g"),
                                     format(gamma, ".17g") if gamma is not None else "", status])
                    if n in SAMPLES or n == horizon:
                        precision_samples[n] = (str(v), str(k4))
                        samples.append({"n": n, "variance": str(v), "kappa4": str(k4),
                                        "gamma4": str(gamma) if gamma is not None else None, "status": status})
    fits = fit_all(values, horizon)
    theory_values = theory(case)
    tail_gamma = values[-1] if np.isfinite(values[-1]) else None
    tail = {"n": horizon, "gamma4": float(tail_gamma) if tail_gamma is not None else None,
            "n_gamma4": float(horizon*tail_gamma) if tail_gamma is not None else None,
            "n2_gamma4": float(horizon*horizon*tail_gamma) if tail_gamma is not None else None}
    if theory_values["C"] is not None and tail_gamma is not None:
        c = float(theory_values["C"])
        tail["n2_times_gamma_minus_C_over_n"] = float(horizon*horizon*(tail_gamma-c/horizon))
    return ({"id": case["id"], "rho_expression": case["expression"], "rho_numeric": str(rho),
             "critical_offset": case["offset"], "rows": horizon, "undefined_rows": null_count,
             "exact_zero_gamma_rows": zero_count, "adjacent_sign_flip_count": flip_count,
             "first_32_adjacent_sign_flips": first_flips, "samples": samples, "tail": tail,
             "theory": theory_values, "fit_windows": fits,
             "file": {"path": path.name, "bytes": path.stat().st_size,
                      "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}}, precision_samples)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE)
    parser.add_argument("--horizon", type=int, default=HORIZON)
    parser.add_argument("--audit-only", action="store_true")
    args = parser.parse_args()
    assert args.horizon >= 32
    args.output.mkdir(parents=True, exist_ok=True)
    audit = {"exact": fraction_audit(), "independent_conditional_raw": decimal_raw_audit()}
    if args.audit_only:
        print(json.dumps(audit, indent=2))
        return
    output_cases, saved_samples = [], {}
    with localcontext() as ctx:
        ctx.prec = PRECISION
        for case in cases():
            result, samples = run_case(case, args.output, args.horizon)
            output_cases.append(result)
            saved_samples[case["id"]] = samples
            print(f"{case['id']}: {args.horizon} rows, {result['file']['bytes']} bytes", flush=True)
    audit["50_vs_80_digit_long_horizon"] = audit_precision(saved_samples, args.horizon)
    audit["status"] = "PASS"
    summary = {"schema_version": 1, "researcher_id": "EM-BRCMARKOV-9D72AC",
        "activity_id": "RA-BRCMARKOV-20261002-9D72AC",
        "prior_source_commit": "46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c",
        "mechanism": "stationary two-state Markov signs; one existing mechanism",
        "new_mechanism_count": 0, "parameter_case_count": len(output_cases),
        "timepoint_rows": len(output_cases)*args.horizon,
        "independent_parameter_case_claim": "30 declared parameter cases; deterministic related trajectories, not statistical independent replicates",
        "horizon": args.horizon, "decimal_precision": PRECISION, "CSV_significant_digits": 17,
        "critical_parameter": {"exact_expression": "sqrt(3)-2", "decimal_computation": "50 significant digits; independent repeat at 80 digits",
                               "exact_C": 0, "exact_E": -3, "parameter_roundoff_note": "Algebraic expression is authoritative; Decimal approximation used only for finite trajectories."},
        "fit_protocol": {"models": FIXED_MODELS, "train_windows": TRAIN_WINDOWS,
            "heldout": "all valid integer n after each training endpoint through horizon",
            "leakage": "Each fit receives training values only. Heldout signs do not determine exclusions.",
            "normalized_rmse": "sqrt(mean(error^2))/sqrt(mean(observed^2)); null if denominator zero",
            "normalized_max_absolute_error": "max(abs(error))/max(abs(observed)); null if denominator zero",
            "warning": "Errors are deterministic approximation diagnostics, not p-values, confidence intervals or independent validation sets.",
            "free_power": "Signed amplitude times n^power; log fit only on nonzero, sign-consistent training data; heldout sign changes remain failures."},
        "versions": {"python": platform.python_version(), "numpy": np.__version__},
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "audit": audit, "cases": output_cases}
    text = json.dumps(summary, ensure_ascii=False, indent=2, allow_nan=False)+"\n"
    (args.output/"markov_results.json").write_text(text)
    print(json.dumps({"status": "PASS", "parameter_cases": len(output_cases),
                      "rows": summary["timepoint_rows"], "gzip_bytes": sum(c["file"]["bytes"] for c in output_cases),
                      "audit": audit}, indent=2), flush=True)


if __name__ == "__main__":
    main()
