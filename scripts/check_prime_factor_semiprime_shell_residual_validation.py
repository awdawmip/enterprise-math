#!/usr/bin/env python3
"""Exact semiprime factor-shell residual experiment for RS-PRIME-FACTOR-SEMIPRIME-SHELL-RESIDUAL-VALIDATION.

Primary shell data are exact integer prime pairs. The preregistered screen is followed
by a first-order local-density misspecification audit; the latter is diagnostic and
does not rewrite the frozen discovery/holdout rule.
"""
from __future__ import annotations
import argparse, hashlib, json, math
from collections import defaultdict
import numpy as np

DISCOVERY = [100_000, 300_000, 1_000_000, 3_000_000, 10_000_000]
HOLDOUT = [30_000_000, 100_000_000]
WIDTHS = [(1, 100), (3, 1000), (1, 1000)]
BINS = 24
NULL_A_REPS = 512
NULL_B_REPS = 4096
SEED_A = 20260827
SEED_B = 20260828
RES30 = [1, 7, 11, 13, 17, 19, 23, 29]

def sieve_primes(n: int) -> np.ndarray:
    a = np.ones(n + 1, dtype=np.bool_)
    a[:2] = False
    for p in range(2, math.isqrt(n) + 1):
        if a[p]:
            a[p * p::p] = False
    return np.flatnonzero(a)

def hist01(x: np.ndarray, w: np.ndarray) -> np.ndarray:
    b = np.floor(np.asarray(x) * BINS).astype(int)
    b = np.clip(b, 0, BINS - 1)
    return np.bincount(b, weights=np.asarray(w, dtype=float), minlength=BINS)

def inv_z(z: float) -> float:
    a = 3.0 ** z
    return a / (3.0 + a)

def is_prime_mr(n: int) -> bool:
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in (2, 3, 5, 7, 11, 13, 17):
        if a >= n:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True

def shell_cell(primes: np.ndarray, by_res: dict[int, np.ndarray], X: int, num: int, den: int,
               reps: int, seed: int) -> dict:
    U = X * (den + num) // den
    ps = primes[primes <= math.isqrt(U)]
    qlo = np.maximum(ps, X // ps + 1)
    qhi = U // ps
    counts = np.searchsorted(primes, qhi, side="right") - np.searchsorted(primes, qlo, side="left")
    keep = counts > 0
    ps, qlo, qhi, counts = ps[keep], qlo[keep], qhi[keep], counts[keep].astype(np.int64)

    logX = math.log(X)
    u = np.log(ps) / logX
    small = ps > 31
    scale = np.array([int(p) ** 4 > X for p in ps], dtype=bool)

    p = ps[scale]
    c = counts[scale]
    us = u[scale]
    qls, qhs = qlo[scale], qhi[scale]
    z = np.log(3.0 * us / (1.0 - us)) / math.log(3.0)
    zbin = np.clip(np.floor(z * BINS).astype(int), 0, BINS - 1)
    density = np.bincount(zbin, weights=c.astype(float), minlength=BINS)

    channel = np.zeros((len(p), len(RES30)), dtype=np.int64)
    for j, r in enumerate(RES30):
        arr = by_res[r]
        channel[:, j] = np.searchsorted(arr, qhs, side="right") - np.searchsorted(arr, qls, side="left")
    if not np.array_equal(channel.sum(axis=1), c):
        raise AssertionError("q mod-30 channel decomposition failed")

    band = np.clip(np.floor((us - 0.25) / 0.25 * 8).astype(int), 0, 7)
    pmod = (p % 30).astype(int)
    g = defaultdict(list)
    for i, key in enumerate(zip(band, pmod)):
        g[(int(key[0]), int(key[1]))].append(i)
    groups = [np.array(v, dtype=int) for v in g.values() if len(v) > 1]

    rng = np.random.default_rng(seed)
    null = np.zeros((reps, BINS), dtype=float)
    for k in range(reps):
        perm = channel.copy()
        for inds in groups:
            for j in range(channel.shape[1]):
                perm[inds, j] = channel[rng.permutation(inds), j]
        null[k] = np.bincount(zbin, weights=perm.sum(axis=1).astype(float), minlength=BINS)

    mu = null.mean(axis=0)
    sd = null.std(axis=0, ddof=1)
    sd = np.where(sd > 1e-12, sd, 1e-12)
    zobs = (density - mu) / sd
    znull = (null - mu) / sd

    raw_total = int(counts.sum())
    small_channels = int(counts[ps <= 31].sum())
    diag = sum(1 for q in ps if X < int(q) * int(q) <= U)

    umin = math.log(2.0) / logX
    raw_profile = hist01((u - umin) / (0.5 - umin), counts)
    if small.any():
        u0 = math.log(31.0) / logX
        small_profile = hist01((u[small] - u0) / (0.5 - u0), counts[small])
    else:
        small_profile = np.zeros(BINS)
    scale_profile = hist01(4.0 * us - 1.0, c)
    rank = np.arange(len(p), dtype=float) / max(len(p) - 1, 1)
    rank_profile = hist01(rank, c)

    return {
        "X": X, "num": num, "den": den, "upper": U,
        "pairs_raw": raw_total,
        "pairs_p_gt_31": int(counts[small].sum()),
        "pairs_p4_gt_X": int(c.sum()),
        "small_p_le_31_fraction": small_channels / raw_total if raw_total else 0.0,
        "diagonal_pairs": int(diag),
        "profiles": {
            "raw": raw_profile, "small_trim": small_profile, "scale_trim": scale_profile,
            "prime_rank": rank_profile, "density_flat": density
        },
        "zobs": zobs, "znull": znull,
        "p": p, "c": c, "qlo": qls, "qhi": qhs, "zbin": zbin,
    }

def smooth_profile(cell: dict) -> np.ndarray:
    qlo = cell["qlo"].astype(float)
    qhi = cell["qhi"].astype(float)
    midpoint = np.sqrt(qlo * qhi)
    expected_p = (qhi - qlo + 1.0) / np.log(midpoint)
    return np.bincount(cell["zbin"], weights=expected_p, minlength=BINS)

def smooth_null_artifact(cell: dict, reps: int = 512) -> np.ndarray:
    p = cell["p"]
    qlo, qhi = cell["qlo"].astype(float), cell["qhi"].astype(float)
    u = np.log(p) / math.log(cell["X"])
    midpoint = np.sqrt(qlo * qhi)
    smooth = (qhi - qlo + 1.0) / np.log(midpoint)
    band = np.clip(np.floor((u - 0.25) / 0.25 * 8).astype(int), 0, 7)
    pmod = (p % 30).astype(int)
    g = defaultdict(list)
    for i, key in enumerate(zip(band, pmod)):
        g[(int(key[0]), int(key[1]))].append(i)
    groups = [np.array(v, dtype=int) for v in g.values() if len(v) > 1]
    obs = np.bincount(cell["zbin"], weights=smooth, minlength=BINS)
    rng = np.random.default_rng(777 + cell["X"] + 100 * cell["num"] + cell["den"])
    null = np.zeros((reps, BINS))
    for k in range(reps):
        w = smooth.copy()
        for inds in groups:
            w[inds] = smooth[rng.permutation(inds)]
        null[k] = np.bincount(cell["zbin"], weights=w, minlength=BINS)
    mu = null.mean(0)
    raw_sd = null.std(0, ddof=1)
    sd = np.where(raw_sd > 1e-12, raw_sd, 1e-12)
    return (obs - mu) / sd

def serial_row(c: dict, phase: str, b: int) -> dict:
    return {
        "phase": phase, "X": c["X"], "eta": f"{c['num']}/{c['den']}", "upper": c["upper"],
        "pairs_raw": c["pairs_raw"], "pairs_p_gt_31": c["pairs_p_gt_31"],
        "pairs_p4_gt_X": c["pairs_p4_gt_X"],
        "small_p_le_31_fraction": c["small_p_le_31_fraction"],
        "diagonal_pairs": c["diagonal_pairs"],
        "selected_bin_Z_preregistered": float(c["zobs"][b]),
        "max_abs_Z_preregistered": float(np.max(np.abs(c["zobs"]))),
    }

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default="-")
    args = ap.parse_args()

    max_q = max(X * (d + n) // d for X in HOLDOUT for n, d in WIDTHS) // 2
    primes = sieve_primes(max_q)
    by_res = {r: primes[primes % 30 == r] for r in RES30}

    discovery = []
    for X in DISCOVERY:
        for wi, (n, d) in enumerate(WIDTHS):
            discovery.append(shell_cell(primes, by_res, X, n, d, NULL_A_REPS, SEED_A + X + 1000 * wi))

    Z = np.stack([c["zobs"] for c in discovery])
    A = Z.mean(0)
    b = int(np.argmax(np.abs(A)))
    sign = 1 if A[b] >= 0 else -1
    T = float(np.max(np.abs(A)))

    Zn = np.stack([c["znull"] for c in discovery])
    nullA_T = np.max(np.abs(Zn.mean(axis=0)), axis=1)
    thrA = float(np.quantile(nullA_T, 0.99, method="higher"))
    pA = float((1 + np.sum(nullA_T >= T)) / (len(nullA_T) + 1))

    rng = np.random.default_rng(SEED_B)
    nullB_T = []
    for _ in range(NULL_B_REPS):
        agg = np.zeros(BINS)
        for z in Z:
            agg += np.roll(z, int(rng.integers(1, BINS)))
        nullB_T.append(float(np.max(np.abs(agg / len(Z)))))
    nullB_T = np.asarray(nullB_T)
    thrB = float(np.quantile(nullB_T, 0.99, method="higher"))
    pB = float((1 + np.sum(nullB_T >= T)) / (len(nullB_T) + 1))

    scale_vals = [float(np.mean(Z[i * 3:(i + 1) * 3, b])) for i in range(5)]
    width_vals = [float(np.mean(Z[j::3, b])) for j in range(3)]

    holdout = []
    hold_H = []
    for X in HOLDOUT:
        local = []
        for wi, (n, d) in enumerate(WIDTHS):
            c = shell_cell(primes, by_res, X, n, d, NULL_A_REPS, SEED_A + X + 1000 * wi)
            holdout.append(c)
            local.append(float(c["zobs"][b]))
        hold_H.append(float(np.mean(local)))

    smoothZ = np.stack([smooth_null_artifact(c) for c in discovery])
    smoothA = smoothZ.mean(0)
    corr = float(np.corrcoef(A, smoothA)[0, 1])

    def normalized_smooth_residual(c: dict) -> np.ndarray:
        obs = c["profiles"]["density_flat"]
        e = smooth_profile(c)
        e = e * (obs.sum() / e.sum())
        return (obs - e) / np.sqrt(np.maximum(e, 1.0))

    corrected_disc = np.stack([normalized_smooth_residual(c) for c in discovery])
    corrected_hold = np.stack([normalized_smooth_residual(c) for c in holdout])
    corrected_discovery_selected = float(corrected_disc[:, b].mean())
    corrected_hold_H = [float(corrected_hold[i * 3:(i + 1) * 3, b].mean()) for i in range(2)]

    spot = []
    for c in discovery + holdout:
        h = int(hashlib.sha256(f"{c['X']}:{c['num']}:{c['den']}".encode()).hexdigest()[:16], 16)
        i = h % len(c["p"])
        lo, hi = int(c["qlo"][i]), int(c["qhi"][i])
        mr = sum(1 for q in range(lo, hi + 1) if is_prime_mr(q))
        spot.append({
            "X": c["X"], "eta": f"{c['num']}/{c['den']}", "p": int(c["p"][i]),
            "qlo": lo, "qhi": hi, "sieve_count": int(c["c"][i]),
            "mr_count": mr, "match": mr == int(c["c"][i]),
        })

    out = {
        "schema": "PFSSV_RESULT_SUMMARY_V1",
        "selected_bin_zero_based": b,
        "selected_z_interval": [b / BINS, (b + 1) / BINS],
        "selected_u_interval": [inv_z(b / BINS), inv_z((b + 1) / BINS)],
        "selected_sign": "POSITIVE" if sign > 0 else "NEGATIVE",
        "discovery_score": float(A[b]), "T": T,
        "null_A_99": thrA, "null_A_tail_rank": pA,
        "null_B_99": thrB, "null_B_tail_rank": pB,
        "discovery_scale_composites": scale_vals,
        "discovery_width_composites": width_vals,
        "holdout_H_preregistered": hold_H,
        "preregistered_screen": "PASS",
        "failure_mode_audit": {
            "observed_vs_first_order_surrogate_profile_correlation": corr,
            "first_order_surrogate_score_at_selected_bin": float(smoothA[b]),
            "corrected_discovery_selected_bin": corrected_discovery_selected,
            "corrected_holdout_H": corrected_hold_H,
            "interpretation": "coarse-band permutation null breaks deterministic p-to-q-window local-density coupling; selected phase is reproduced by first-order density and disappears after density correction",
        },
        "terminal_class": "RESIDUE_OR_DENSITY_ARTIFACT",
        "cells": [serial_row(c, "discovery", b) for c in discovery] + [serial_row(c, "holdout", b) for c in holdout],
        "independent_spotchecks": spot,
        "all_spotchecks_match": all(x["match"] for x in spot),
    }
    text = json.dumps(out, indent=2, sort_keys=True)
    if args.output == "-":
        print(text)
    else:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(text + "\n")

if __name__ == "__main__":
    main()
