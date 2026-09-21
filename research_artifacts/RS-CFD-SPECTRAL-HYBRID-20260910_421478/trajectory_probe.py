#!/usr/bin/env python3
"""Bounded continuation probe for RS-CFD-SPECTRAL-HYBRID-20260910.

This file integrates the previously proved exact axis-generator selector with the
pinned native adapter's support-gather boundary and records a conservative
amortized cost horizon. It does not emulate spectralDNS and does not claim an
original-host run.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import ceil, gcd, prod
from numbers import Integral
import importlib.util
import json
import platform
import shutil
from typing import Iterable

import numpy as np

Vec = tuple[int, int, int]


@dataclass(frozen=True)
class ClosureResult:
    status: str
    carrier_size: int | None
    lower_bound: int
    rounds: int
    pair_tests: int
    carrier: tuple[Vec, ...] | None


@dataclass(frozen=True)
class AxisCertificate:
    gcds: Vec
    carrier_size: int
    source_size: int
    status: str
    carrier: tuple[Vec, ...] | None


def _neg(v: Vec) -> Vec:
    return (-v[0], -v[1], -v[2])


def _add(p: Vec, q: Vec) -> Vec:
    return (p[0] + q[0], p[1] + q[1], p[2] + q[2])


def _in_box(v: Vec, cutoff: int) -> bool:
    return all(-cutoff <= x <= cutoff for x in v)


def truncated_additive_carrier(seed: Iterable[Vec], cutoff: int, limit: int) -> ClosureResult:
    C = {tuple(map(int, v)) for v in seed}
    C |= {_neg(v) for v in tuple(C)}
    if any(not _in_box(v, cutoff) for v in C):
        raise ValueError("seed outside retained cube")
    if len(C) > limit:
        return ClosureResult("FALLBACK_DENSE", None, len(C), 0, 0, None)
    rounds = 0
    pair_tests = 0
    while True:
        rounds += 1
        L = sorted(C)
        new: set[Vec] = set()
        for i, p in enumerate(L):
            for q in L[i:]:
                pair_tests += 1
                r = _add(p, q)
                if _in_box(r, cutoff) and r not in C and r not in new:
                    new.add(r)
                    rn = _neg(r)
                    if rn not in C and rn not in new:
                        new.add(rn)
                    if len(C) + len(new) > limit:
                        return ClosureResult("FALLBACK_DENSE", None, limit + 1, rounds, pair_tests, None)
        if not new:
            return ClosureResult("CERTIFIED_STATIC_CARRIER", len(C), len(C), rounds, pair_tests, tuple(sorted(C)))
        C |= new


def axis_certificate(seed: Iterable[Vec], cutoff: int, limit: int) -> AxisCertificate | None:
    if not isinstance(cutoff, Integral) or isinstance(cutoff, bool) or cutoff < 0:
        raise ValueError("cutoff must be a nonnegative integer")
    if not isinstance(limit, Integral) or isinstance(limit, bool) or limit < 0:
        raise ValueError("limit must be a nonnegative integer")
    S: set[Vec] = set()
    for v in seed:
        v = tuple(v)
        if len(v) != 3 or any(not isinstance(x, Integral) or isinstance(x, bool) for x in v):
            raise ValueError("seed requires exact integer triples")
        p = tuple(int(x) for x in v)
        if any(abs(x) > cutoff for x in p):
            raise ValueError("seed outside retained cube")
        S.add(p)
        S.add(tuple(-x for x in p))
    if not S:
        return AxisCertificate((0, 0, 0), 0, 0, "EXACT_EMPTY", ())
    ds = tuple(gcd(*(abs(p[j]) for p in S)) for j in range(3))
    for j, d in enumerate(ds):
        if d:
            g = tuple(d if k == j else 0 for k in range(3))
            if g not in S:
                return None
    size = prod(2 * (cutoff // d) + 1 if d else 1 for d in ds)
    if size > limit:
        return AxisCertificate(ds, size, len(S), "EXACT_SIZE_DENSE_FALLBACK", None)
    axes = [range(-(cutoff // d) * d, (cutoff // d) * d + 1, d) if d else (0,) for d in ds]
    C = tuple(product(*axes))
    assert len(C) == size
    return AxisCertificate(ds, size, len(S), "EXACT_AXIS_GENERATOR_CARRIER", C)


def select_carrier(seed: Iterable[Vec], cutoff: int, limit: int):
    """Proof-preserving route: exact fast certificate, else frozen general detector."""
    S = tuple(seed)
    cert = axis_certificate(S, cutoff, limit)
    if cert is not None:
        return cert.carrier, {
            "route": cert.status,
            "proof": "AXIS_GCD_GENERATORS_PRESENT",
            "gcds": cert.gcds,
            "carrier_size": cert.carrier_size,
            "lower_bound": cert.carrier_size,
            "pair_tests": 0,
        }
    result = truncated_additive_carrier(S, cutoff, limit)
    return result.carrier, {
        "route": result.status,
        "proof": "ORIGINAL_TRUNCATED_ADDITIVE_CLOSURE",
        "carrier_size": result.carrier_size,
        "lower_bound": result.lower_bound,
        "pair_tests": result.pair_tests,
    }


def build_fixed_rfft_gather_repaired(carrier: Iterable[Vec], n: int):
    """Pinned gather with the required empty-support shape repair."""
    p = np.asarray(tuple(carrier), dtype=np.int64).reshape(-1, 3)
    ix = np.empty(len(p), dtype=np.int64)
    iy = np.empty(len(p), dtype=np.int64)
    iz = np.empty(len(p), dtype=np.int64)
    conj = np.zeros(len(p), dtype=np.bool_)
    for i, (x, y, z) in enumerate(p):
        if z >= 0:
            ix[i], iy[i], iz[i] = x % n, y % n, z
        else:
            ix[i], iy[i], iz[i], conj[i] = (-x) % n, (-y) % n, -z, True
    return p, ix, iy, iz, conj


def amortized_break_even(fft_cold_ms: float, route_cold_ms: float,
                         fft_warm_ms: float, route_warm_ms: float) -> dict:
    """Smallest total trajectory count whose median affine cost no longer loses."""
    warm_saving = fft_warm_ms - route_warm_ms
    cold_penalty = route_cold_ms - fft_cold_ms
    if warm_saving <= 0:
        return {
            "finite_horizon": False,
            "reason": "route has no positive warm saving against FFT",
            "cold_penalty_ms": cold_penalty,
            "warm_saving_ms_per_reuse": warm_saving,
        }
    n = 1 if cold_penalty <= 0 else ceil(1.0 + cold_penalty / warm_saving)
    route_total = route_cold_ms + (n - 1) * route_warm_ms
    fft_total = fft_cold_ms + (n - 1) * fft_warm_ms
    before_n = max(1, n - 1)
    route_before = route_cold_ms + (before_n - 1) * route_warm_ms
    fft_before = fft_cold_ms + (before_n - 1) * fft_warm_ms
    return {
        "finite_horizon": True,
        "smallest_total_trajectories": n,
        "cold_penalty_ms": cold_penalty,
        "warm_saving_ms_per_reuse": warm_saving,
        "at_horizon_route_total_ms": route_total,
        "at_horizon_fft_total_ms": fft_total,
        "one_before_route_total_ms": route_before,
        "one_before_fft_total_ms": fft_before,
        "model": "one measured cold median + (n-1) measured warm medians; descriptive, not CI",
    }


def dependency_probe() -> dict:
    modules = ["numpy", "scipy", "numba", "spectralDNS", "shenfun", "mpi4py", "mpi4py_fft", "pyfftw"]
    return {
        "python": platform.python_version(),
        "modules": {m: importlib.util.find_spec(m) is not None for m in modules},
        "executables": {name: shutil.which(name) for name in ("mpiexec", "mpirun", "fftw-wisdom")},
        "original_host_runnable_from_python_env": all(importlib.util.find_spec(m) is not None for m in ("spectralDNS", "shenfun")),
    }


def run_regressions() -> dict:
    c, meta = select_carrier([], 7, 384)
    assert c == () and meta["route"] == "EXACT_EMPTY"
    p, *rest = build_fixed_rfft_gather_repaired(c, 16)
    assert p.shape == (0, 3)
    assert all(len(x) == 0 for x in rest)

    c, meta = select_carrier([(1, 1, 0), (-1, -1, 0)], 7, 384)
    assert meta["proof"] == "ORIGINAL_TRUNCATED_ADDITIVE_CLOSURE"
    assert len(c) == 15

    seed = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]
    c, meta = select_carrier(seed, 7, 384)
    assert meta["proof"] == "AXIS_GCD_GENERATORS_PRESENT"
    assert meta["carrier_size"] == 225 and len(c) == 225

    c, meta = select_carrier(seed + [(0, 0, 1), (0, 0, -1)], 7, 384)
    assert c is None and meta["route"] == "EXACT_SIZE_DENSE_FALLBACK"
    assert meta["carrier_size"] == 3375

    horizons = {
        "xy225": amortized_break_even(61.924833999910334, 537.9565430000639, 55.441, 18.554),
        "xy35": amortized_break_even(61.819903000014165, 496.29963900008534, 56.098, 4.541),
        "xyz3375_dense_warm_only": amortized_break_even(56.478, 58.352, 56.478, 58.352),
        "random48_dense_warm_only": amortized_break_even(55.726, 57.796, 55.726, 57.796),
    }
    assert horizons["xy225"]["smallest_total_trajectories"] == 14
    assert horizons["xy35"]["smallest_total_trajectories"] == 10
    assert horizons["xyz3375_dense_warm_only"]["finite_horizon"] is False
    assert horizons["random48_dense_warm_only"]["finite_horizon"] is False

    return {
        "schema": "CFD_HYBRID_CONTINUATION_PROBE_V1",
        "status": "BOUNDED_CHECKPOINT_NOT_HOST_EXECUTION",
        "regressions": {
            "empty_support_rank2_repair": "PASS",
            "diagonal_missing_axis_witness_declines_fast_path": "PASS",
            "xy_axis_generator_carrier_225": "PASS",
            "xyz_exact_size_dense_fallback_3375": "PASS",
        },
        "amortized_horizons": horizons,
        "capability": dependency_probe(),
        "brc": {
            "resolution": ["EXTEND_EXISTING_TOOL", "REUSE_EXECUTED"],
            "carrier": "exact signed Boolean wavevector support for route selection only",
            "retained_information": ["complex amplitudes", "phase", "conjugacy", "pair multiplicity", "dense fallback"],
            "discarded_information_for_routing_only": "none beyond coefficient values not used by support-route selector",
        },
    }


if __name__ == "__main__":
    print(json.dumps(run_regressions(), indent=2, sort_keys=True))
