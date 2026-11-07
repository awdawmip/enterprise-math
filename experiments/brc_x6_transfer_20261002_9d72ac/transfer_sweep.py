#!/usr/bin/env python3
"""Conditional residual transport on two finite channels in a fixed native X6 chart.

The six signed raw coordinates are spatial; n is a separate operation-order
index. These declared kernels are not P000 dynamics or physical calibration.
Full spatial-law TV is distinct from TV on archived, decorated histories.
"""
from __future__ import annotations

import argparse
import csv
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
import gzip
import hashlib
import io
import itertools
import json
import math
from pathlib import Path
import platform
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
from enterprise_math.brc_transport import Affine, EffectHistogram, MomentState, eye

HORIZON = 4096
P_GRID = ["0", "0.01", "0.1", "0.25", "0.5", "0.75", "1"]
D_GRID = ["0", "0.001", "0.01"]
ANCHOR = (0,) * 6
AXES = [tuple(int(i == j) for j in range(6)) for i in range(6)]
FAMILIES = {
    "active_permutation_6": AXES,
    "signed_unit_channel_12": [
        tuple(AXES[i // 2][j] + (AXES[(i // 2 + 1) % 6][j] if i % 2 else 0)
              for j in range(6)) for i in range(12)]}
SAMPLE_TIMES = {0, 1, 2, 3, 4, 5, 6, 10, 11, 12, 16, 32, 64, 128, 256,
                512, 1024, 2048, 3072, 4096}


def case_id(family, p, d):
    return family + "_p" + p.replace(".", "p") + "_d" + d.replace(".", "p")


def branch_rates(p, d):
    return {"I": (1-d)*(1-p), "A": (1-d)*p, "R": d}


def apply_branch(index, branch, count):
    """Index -1 is the chosen chart-anchor Cell, fixed under all branches."""
    if branch == "R" or index == -1:
        return -1
    if branch == "I":
        return index
    if branch == "A":
        return (index+1) % count
    raise ValueError(branch)


def decode_history(family, word, initial="mu"):
    """Lossless ordered branch ID plus initial law determines the full raw trace."""
    sites = FAMILIES[family]
    index = 0 if initial == "mu" else -1
    trace = [sites[index] if index >= 0 else ANCHOR]
    for branch in word:
        index = apply_branch(index, branch, len(sites))
        trace.append(sites[index] if index >= 0 else ANCHOR)
    return trace


def fraction_step(law, p, d):
    """Independent full endpoint-law update, including anchor mass at index -1."""
    count = len(law)-1
    output = [F(0)]*(count+1)
    rates = branch_rates(p, d)
    for index in range(-1, count):
        for branch, rate in rates.items():
            output[apply_branch(index, branch, count)] += law[index]*rate
    return output


def projected_tv(law_mu, law_nu, sites, selected):
    """TV after raw-coordinate readout, preserving signed differences first."""
    pushed = {}
    for index, cell in list(enumerate(sites)) + [(-1, ANCHOR)]:
        key = tuple(cell[j] for j in selected)
        pushed[key] = pushed.get(key, F(0)) + law_mu[index]-law_nu[index]
    return sum(abs(value) for value in pushed.values())/2


def exact_audit():
    out = {"case_count": 0, "exact_full_law_timepoints": 0,
           "full_word_enumeration_timepoints": 0, "enumerated_leaf_histories": 0,
           "production_BRC_degree_two_timepoints": 0}
    for family, sites in FAMILIES.items():
        count = len(sites)
        for p_text, d_text in itertools.product(P_GRID, D_GRID):
            p, d = F(p_text), F(d_text)
            mu = [F(1)] + [F(0)]*count
            nu = [F(0)]*count + [F(1)]
            conditional = [F(1)] + [F(0)]*(count-1)
            survival = F(1)
            for n in range(33):
                assert sum(mu) == sum(nu) == sum(conditional) == 1
                assert mu[-1] == 1-survival and nu[-1] == 1
                assert mu[:-1] == [survival*q for q in conditional]
                assert sum(abs(x-y) for x, y in zip(mu, nu))/2 == survival
                for selected in [(i,) for i in range(6)] + [(0, 1, 2), (3, 4, 5)]:
                    expected = survival*sum(conditional[i] for i, cell in enumerate(sites)
                                            if any(cell[j] for j in selected))
                    assert projected_tv(mu, nu, sites, selected) == expected
                out["exact_full_law_timepoints"] += 1
                mu, nu = fraction_step(mu, p, d), fraction_step(nu, p, d)
                conditional = [(1-p)*conditional[i]+p*conditional[(i-1) % count] for i in range(count)]
                survival *= 1-d
            out["case_count"] += 1
        # Enumerate ordered, distinct words. Do not collapse them to advance counts.
        for p, d in [(F(1, 2), F(0)), (F(1, 4), F(1, 100))]:
            rates = branch_rates(p, d)
            for n in range(7):
                law = [F(0)]*(count+1)
                for word in itertools.product("IAR", repeat=n):
                    weight = math.prod(rates[b] for b in word)
                    if weight:
                        trace = decode_history(family, word)
                        endpoint = sites.index(trace[-1]) if trace[-1] != ANCHOR else -1
                        law[endpoint] += weight
                        out["enumerated_leaf_histories"] += 1
                expected = [F(1)] + [F(0)]*count
                for _ in range(n):
                    expected = fraction_step(expected, p, d)
                assert law == expected
                out["full_word_enumeration_timepoints"] += 1
    # Actual reuse of T0_BRC, whose global affine scope covers the 6-cycle family.
    permutation = tuple(tuple(F(j == (i-1) % 6) for j in range(6)) for i in range(6))
    zero_matrix = tuple((F(0),)*6 for _ in range(6))
    for p, d in [(F(1, 2), F(0)), (F(1, 4), F(1, 100))]:
        actions = {"I": Affine(eye(6), ANCHOR), "A": Affine(permutation, ANCHOR),
                   "R": Affine(zero_matrix, ANCHOR)}
        packet = EffectHistogram.from_terms(6, [(w, actions[b], 1)
                    for b, w in branch_rates(p, d).items() if w])
        moment = MomentState.from_point(AXES[0])
        law = [F(1)] + [F(0)]*6
        for n in range(17):
            matrix = moment.to_matrix()
            augmented = [tuple(cell)+(1,) for cell in AXES] + [ANCHOR+(1,)]
            expected = tuple(tuple(sum(law[k]*augmented[k][i]*augmented[k][j] for k in range(7))
                                   for j in range(7)) for i in range(7))
            assert matrix == expected
            out["production_BRC_degree_two_timepoints"] += 1
            moment = moment.then(packet)
            law = fraction_step(law, p, d)
    for i, source in enumerate(FAMILIES["signed_unit_channel_12"]):
        target = FAMILIES["signed_unit_channel_12"][(i+1) % 12]
        step = tuple(y-x for x, y in zip(source, target))
        assert sum(abs(x) for x in step) == 1
        assert sum(x*x for x in step) == 1
    # Spatial invisibility does not license discarding a state: it can return.
    assert decode_history("active_permutation_6", "A"*6)[-1] == AXES[0]
    assert decode_history("signed_unit_channel_12", "A"*12)[-1] == AXES[0]
    assert all(decode_history("signed_unit_channel_12", "A"*n)[-1][0] == 0 for n in range(2, 11))
    assert decode_history("signed_unit_channel_12", "A"*11)[-1][0] == 1
    out["status"] = "PASS"
    return out


def conditional_series(count, p_text, horizon):
    p = float(p_text)
    values = np.empty((horizon+1, count))
    w = np.zeros(count)
    w[0] = 1
    max_error = max_mass_error = max_bound_excess = 0.0
    # A posteriori discrepancy against independent 60-digit recurrence and an
    # a priori conservative arithmetic bound are both recorded; no renormalizing.
    with localcontext() as context:
        context.prec = 60
        pd = D(p_text)
        reference = [D(1)] + [D(0)]*(count-1)
        for n in range(horizon+1):
            values[n] = w
            max_error = max(max_error, max(float(abs(D.from_float(float(w[i]))-reference[i])) for i in range(count)))
            max_mass_error = max(max_mass_error, abs(float(sum(w))-1))
            w = (1-p)*w+p*np.roll(w, 1)
            reference = [(1-pd)*reference[i]+pd*reference[(i-1) % count] for i in range(count)]
    assert max_error < 1e-12 and max_mass_error < 1e-12
    assert np.min(values) >= 0
    # For n steps, perturbations from two weighted terms and addition accumulate
    # at most O(n*eps) in l1 because the exact transition is stochastic. 32*n*eps
    # safely includes probability-representation error and output arithmetic.
    numerical_bound = 32*max(1, horizon)*np.finfo(float).eps
    assert count*max_error < numerical_bound
    if 0 < p < 1:
        contraction = math.sqrt(1-2*p*(1-p)*(1-math.cos(2*math.pi/count)))
        mixing_bounds = 0.5*math.sqrt(count-1)*np.exp(np.arange(horizon+1)*math.log(contraction))
        actual_tv = 0.5*np.sum(np.abs(values-1/count), axis=1)
        max_bound_excess = float(np.max(actual_tv-mixing_bounds))
        assert max_bound_excess <= numerical_bound
    else:
        contraction = 1.0
    return values, {"reference_precision": 60, "compared_timepoints": horizon+1,
        "max_absolute_site_probability_error": max_error, "max_mass_error": max_mass_error,
        "conservative_l1_arithmetic_bound": numerical_bound,
        "spectral_bound_excess_including_roundoff": max_bound_excess,
        "spectral_contraction": contraction, "status": "PASS"}


def inverse_time_fit(values, horizon):
    if horizon < 4096:
        return {"status": "NOT_RUN_REQUIRES_HORIZON_4096"}
    train_n = np.arange(1, 17, dtype=float)
    train = values[1:17]
    held_n = np.arange(2049, 4097, dtype=float)
    held = values[2049:4097]
    if np.any(train <= 0):
        return {"status": "EXCLUDED_NONPOSITIVE_TRAINING_TV"}
    coefficient = float(np.dot(1/train_n, train)/np.dot(1/train_n, 1/train_n))
    prediction = coefficient/held_n
    rmse = float(np.sqrt(np.mean((prediction-held)**2)))
    scale = float(np.sqrt(np.mean(held**2)))
    return {"status": "FIT", "train": [1, 16], "heldout": [2049, 4096],
        "coefficient_C": coefficient, "train_points": 16, "heldout_points": 2048,
        "heldout_rmse": rmse, "heldout_normalized_rmse": rmse/scale if scale else None,
        "heldout_max_absolute_error": float(np.max(np.abs(prediction-held))),
        "last_prediction": float(prediction[-1]), "last_actual": float(held[-1]),
        "meaning": "deterministic approximation error, not statistical inference"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE)
    parser.add_argument("--horizon", type=int, default=HORIZON)
    parser.add_argument("--audit-only", action="store_true")
    args = parser.parse_args()
    assert args.horizon >= 32
    audit = exact_audit()
    if args.audit_only:
        print(json.dumps(audit, indent=2))
        return
    args.output.mkdir(parents=True, exist_ok=True)
    series_path = args.output / "transfer_series.csv.gz"
    summary = {"schema_version": 1, "researcher_id": "EM-BRCMARKOV-9D72AC",
        "activity_id": "RA-BRCMARKOV-20261002-9D72AC", "horizon": args.horizon,
        "spatial_dimension": 6, "time_dimension": 1,
        "coordinate_type": "internal signed raw lattice chart relative to a chosen Cell anchor; not final Cell addresses",
        "dynamics_status": "declared conditional channel kernels; not P000 primitive physical dynamics",
        "residual": "signed spatial measure delta_n=mu_n-nu_n; TV=0.5*sum(abs(delta)); not gamma4, energy, or signed amplitude",
        "full_spatial_vs_history": "Full spatial TV sees all six current coordinates. Archived initial states and ordered history laws remain richer; reset does not erase the external archive.",
        "initial_laws": {"mu": "point mass at raw e1", "nu": "point mass at chosen raw anchor zero"},
        "branch_provenance": {"alphabet": ["I", "A", "R"], "word": "ordered tuple (b1,...,bn), never replaced by unordered counts",
            "probability": "product q(b_t), q(I)=(1-d)(1-p), q(A)=(1-d)p, q(R)=d",
            "multiplicity": "Every positive-probability ordered word is a distinct branch; coincident endpoints do not identify words.",
            "representation": "exact generative history law via rational parameters, branch maps, initial state, and decode_history; not explicit exponential enumeration at long n",
            "future_scope": "The declared future kernels depend only on current full raw spatial state; spatial readouts after any future branch-word composition factor through that state. History-sensitive feedback is excluded from this certificate, and the history law remains separately reconstructible."},
        "readouts": {"axis_j": "raw signed coordinate x_j", "axes123": "raw coordinate triple (x1,x2,x3)",
                     "axes456": "raw coordinate triple (x4,x5,x6)",
                     "sum_axis_tv": "sum of six marginal TVs; not itself full spatial TV or a conservation law"},
        "families": {}, "cases": [], "audit": {"exact": audit, "floating_references": []},
        "versions": {"python": platform.python_version(), "numpy": np.__version__},
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    header = ["family", "case", "n", "survival", "delta_anchor"] + [f"delta_site_{i:02d}" for i in range(12)] + [
        "tv_spatial"] + [f"tv_axis_{i+1}" for i in range(6)] + ["tv_axes123", "tv_axes456", "sum_axis_tv", "conditional_mass_error", "conditional_uniform_tv"]
    with series_path.open("wb") as binary, gzip.GzipFile(filename="", fileobj=binary, mode="wb", mtime=0, compresslevel=9) as gz, io.TextIOWrapper(gz, encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(header)
        for family, sites in FAMILIES.items():
            count = len(sites)
            coords = np.asarray(sites, dtype=int)
            visible = np.column_stack([coords[:, i] != 0 for i in range(6)] + [np.any(coords[:, :3] != 0, axis=1), np.any(coords[:, 3:] != 0, axis=1)]).astype(float)
            stationary = np.mean(visible, axis=0)
            steps = [tuple(sites[(i+1) % count][j]-sites[i][j] for j in range(6)) for i in range(count)]
            summary["families"][family] = {"site_count": count, "raw_sites": sites, "advance_displacements": steps,
                "anchor": ANCHOR, "advance_from_anchor": ANCHOR,
                "advance_type": "active S6 coordinate permutation macro-operation" if count == 6 else "declared routing along single signed native unit steps",
                "reset_type": "explicit many-to-one map to anchor, not a spatial primitive-step law",
                "stationary_conditional_axis_tv": stationary[:6].tolist(),
                "stationary_conditional_axes123_tv": float(stationary[6]),
                "stationary_conditional_axes456_tv": float(stationary[7]),
                "stationary_scope": "0<p<1 conditional on no reset; absolute readout TV additionally multiplies survival",
                "pointwise_period_p1": count}
            for p_text in P_GRID:
                weights, numeric_audit = conditional_series(count, p_text, args.horizon)
                numeric_audit.update(family=family, p=p_text)
                summary["audit"]["floating_references"].append(numeric_audit)
                conditional_readouts = weights @ visible
                for d_text in D_GRID:
                    cid = case_id(family, p_text, d_text)
                    n_all = np.arange(args.horizon+1)
                    d = float(d_text)
                    survival = np.exp(n_all*math.log1p(-d)) if d else np.ones(args.horizon+1)
                    delta_sites = weights*survival[:, None]
                    full_tv = (np.sum(np.abs(delta_sites), axis=1)+survival)/2
                    readouts = conditional_readouts*survival[:, None]
                    sum_axes = np.sum(readouts[:, :6], axis=1)
                    uniform_tv = 0.5*np.sum(np.abs(weights-1/count), axis=1)
                    mass_error = np.sum(weights, axis=1)-1
                    max_invariant_error = float(np.max(np.abs(full_tv-survival)))
                    assert max_invariant_error < numeric_audit["conservative_l1_arithmetic_bound"]
                    assert np.all(readouts <= full_tv[:, None]+numeric_audit["conservative_l1_arithmetic_bound"])
                    samples = []
                    for n in range(args.horizon+1):
                        numbers = [survival[n], -survival[n]] + list(delta_sites[n]) + [None]*(12-count) + [full_tv[n]] + list(readouts[n]) + [sum_axes[n], mass_error[n], uniform_tv[n]]
                        writer.writerow([family, cid, n]+["" if x is None else format(float(x), ".17g") for x in numbers])
                        if n in SAMPLE_TIMES or n == args.horizon:
                            samples.append({"n": n, "survival": float(survival[n]), "tv_spatial": float(full_tv[n]),
                                "tv_axis": readouts[n, :6].tolist(), "tv_axes123": float(readouts[n, 6]),
                                "tv_axes456": float(readouts[n, 7]), "sum_axis_tv": float(sum_axes[n]),
                                "conditional_uniform_tv": float(uniform_tv[n])})
                    fits = {"status": "NOT_IN_PREDECLARED_FIT_SUBSET"}
                    if p_text == "1":
                        fits = {"status": "PERIODIC_CONDITIONAL_SPATIAL_ORBIT_NOT_POWER_LAW_FITTED"}
                    elif d_text == "0" and p_text in ["0.01", "0.1", "0.5"]:
                        fits = {"axis1_C_over_n": inverse_time_fit(readouts[:, 0], args.horizon),
                                "axes123_C_over_n": inverse_time_fit(readouts[:, 6], args.horizon),
                                "full_spatial_C_over_n": inverse_time_fit(full_tv, args.horizon)}
                    rates = branch_rates(F(p_text), F(d_text))
                    summary["cases"].append({"id": cid, "family": family, "p": p_text, "d": d_text,
                        "branch_probabilities_exact": {key: str(value) for key, value in rates.items()},
                        "rows": args.horizon+1, "max_absolute_full_tv_survival_error": max_invariant_error,
                        "last": samples[-1], "samples": samples, "short_window_fits": fits,
                        "pointwise_behavior": "stationary conditional mixing" if 0 < float(p_text) < 1 else "static conditional state" if p_text == "0" else "periodic conditional state",
                        "full_spatial_tv_exact": "(1-d)^n",
                        "n_positive_histories": "a^n, where a is the number of positive branch probabilities; each ordered word distinct"})
                    print(cid, flush=True)
    summary["case_count"] = len(summary["cases"])
    summary["timepoint_rows"] = summary["case_count"]*(args.horizon+1)
    summary["csv"] = {"path": series_path.name, "bytes": series_path.stat().st_size,
        "sha256": hashlib.sha256(series_path.read_bytes()).hexdigest(), "columns": header,
        "law_reconstruction": "delta(anchor)=-survival, delta(site_i)=stored value; mu=delta+nu with nu(anchor)=1. Keep signed delta directly: subtracting rounded mu(anchor) from 1 can lose tiny surviving differences. Unused site columns are empty, not extra hidden sites.",
        "digits": 17, "compression": "gzip mtime=0, empty filename"}
    summary["audit"]["status"] = "PASS"
    (args.output/"transfer_results.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2, allow_nan=False)+"\n")
    print(json.dumps({"status": "PASS", "cases": summary["case_count"], "rows": summary["timepoint_rows"], "gzip_bytes": summary["csv"]["bytes"], "exact_audit": audit}, indent=2))


if __name__ == "__main__":
    main()
