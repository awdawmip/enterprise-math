from __future__ import annotations
import importlib.util
import json
import platform
import shutil
import statistics
import time
from pathlib import Path

import numpy as np

SEED = 20260921
RK_A = np.array([1/6, 1/3, 1/3, 1/6], dtype=float)
RK_B = np.array([0.5, 0.5, 1.0], dtype=float)


def outside_nonzero(a: np.ndarray, mask: np.ndarray) -> bool:
    return bool(np.any(a[:, ~mask] != 0))


def synthetic_rhs(u: np.ndarray, source: np.ndarray, mask: np.ndarray) -> np.ndarray:
    # Support-preserving finite witness only: all generated terms are masked into C.
    out = np.zeros_like(u)
    mixed = 0.125 * u + 0.03125j * u + source
    out[:, mask] = mixed[:, mask]
    return out


def rk4_step(u0: np.ndarray, source: np.ndarray, mask: np.ndarray) -> tuple[np.ndarray, list[bool]]:
    u = u0.copy()
    u1 = u0.copy()
    u2 = u0.copy()
    stage_escape = []
    for rk in range(4):
        stage_escape.append(outside_nonzero(u, mask))
        rhs = synthetic_rhs(u, source, mask)
        if rk < 3:
            u = u1 + RK_B[rk] * 0.01 * rhs
        u2 = u2 + RK_A[rk] * 0.01 * rhs
    return u2, stage_escape


def make_mask(n: int) -> np.ndarray:
    mask = np.zeros((n, n, n // 2 + 1), dtype=bool)
    # Small, explicitly closed-for-this-synthetic-witness carrier footprint.
    coords = [(0,0,0),(1,0,0),(n-1,0,0),(2,0,0),(n-2,0,0)]
    for x,y,z in coords:
        mask[x,y,z] = True
    return mask


def randomized_support_witness(trials: int = 64, n: int = 16) -> dict:
    rng = np.random.default_rng(SEED)
    mask = make_mask(n)
    all_ok = True
    max_outside = 0.0
    for _ in range(trials):
        u = np.zeros((3,n,n,n//2+1), dtype=np.complex128)
        source = np.zeros_like(u)
        for arr in (u, source):
            vals = rng.normal(size=(3, mask.sum())) + 1j*rng.normal(size=(3, mask.sum()))
            arr[:, mask] = vals
        for _step in range(8):
            u, flags = rk4_step(u, source, mask)
            all_ok = all_ok and not any(flags) and not outside_nonzero(u, mask)
            if np.any(~mask):
                max_outside = max(max_outside, float(np.max(np.abs(u[:, ~mask]))))
    # Negative control: an external mutation of state is invisible to a Source-only scan.
    u = np.zeros((3,n,n,n//2+1), dtype=np.complex128)
    source = np.zeros_like(u)
    outside_idx = tuple(np.argwhere(~mask)[0])
    u[(0,) + outside_idx] = 1.0 + 2.0j
    conservative_detects = outside_nonzero(u, mask) or outside_nonzero(source, mask)
    source_only_detects = outside_nonzero(source, mask)

    # Stronger-tier negative control: if Source can mutate during a four-stage step,
    # a single step-entry Source scan is insufficient whereas per-stage scanning catches it.
    source_mid = np.zeros_like(source)
    step_entry_source_scan = outside_nonzero(source_mid, mask)
    source_mid[(1,) + outside_idx] = 3.0 - 1.0j
    per_stage_source_scan_after_mutation = outside_nonzero(source_mid, mask)
    return {
        "trials": trials,
        "steps_per_trial": 8,
        "support_preserved": bool(all_ok),
        "max_outside_abs": max_outside,
        "negative_control_external_state_mutation": {
            "conservative_state_plus_source_detects": conservative_detects,
            "source_only_detects": source_only_detects,
            "expected_source_only_miss": bool(conservative_detects and not source_only_detects),
        },
        "negative_control_midstep_source_mutation": {
            "step_entry_source_scan_detects": step_entry_source_scan,
            "per_stage_source_scan_after_mutation_detects": per_stage_source_scan_after_mutation,
            "expected_once_per_step_miss": bool((not step_entry_source_scan) and per_stage_source_scan_after_mutation),
        },
    }


def scan_benchmark(n: int = 64, repetitions: int = 80) -> dict:
    rng = np.random.default_rng(SEED + 1)
    mask = np.zeros((n,n,n//2+1), dtype=bool)
    mask[:3,:3,:2] = True
    state = np.zeros((3,n,n,n//2+1), dtype=np.complex128)
    source = np.zeros_like(state)
    state[:, mask] = rng.normal(size=(3,mask.sum())) + 1j*rng.normal(size=(3,mask.sum()))
    source[:, mask] = rng.normal(size=(3,mask.sum())) + 1j*rng.normal(size=(3,mask.sum()))

    # Warmup.
    for _ in range(5):
        outside_nonzero(state, mask); outside_nonzero(source, mask)

    conservative_stage = []
    source_stage = []
    conservative_step4 = []
    source_stage4 = []
    source_once_step4 = []
    for _ in range(repetitions):
        t = time.perf_counter_ns()
        _ = outside_nonzero(state, mask) or outside_nonzero(source, mask)
        conservative_stage.append(time.perf_counter_ns() - t)
        t = time.perf_counter_ns()
        _ = outside_nonzero(source, mask)
        source_stage.append(time.perf_counter_ns() - t)

        t = time.perf_counter_ns()
        for _rk in range(4):
            _ = outside_nonzero(state, mask) or outside_nonzero(source, mask)
        conservative_step4.append(time.perf_counter_ns() - t)
        t = time.perf_counter_ns()
        for _rk in range(4):
            _ = outside_nonzero(source, mask)
        source_stage4.append(time.perf_counter_ns() - t)
        t = time.perf_counter_ns()
        _ = outside_nonzero(source, mask)
        source_once_step4.append(time.perf_counter_ns() - t)
    c = statistics.median(conservative_stage)
    ss = statistics.median(source_stage)
    c4 = statistics.median(conservative_step4)
    ss4 = statistics.median(source_stage4)
    so4 = statistics.median(source_once_step4)
    return {
        "n": n,
        "complex_coefficients_per_field": int(state.size),
        "repetitions": repetitions,
        "per_stage": {
            "state_plus_source_median_ns": int(c),
            "source_only_median_ns": int(ss),
            "saved_ns": int(c - ss),
            "ratio_state_plus_source_over_source_only": float(c / ss) if ss else None
        },
        "four_stage_rk4_group": {
            "state_plus_source_every_stage_median_ns": int(c4),
            "source_every_stage_median_ns": int(ss4),
            "source_once_per_step_median_ns": int(so4),
            "state_plus_source_over_source_once_ratio": float(c4 / so4) if so4 else None
        },
        "scope": "local_numpy_microbenchmark_not_native_spectralDNS_timing",
    }


def environment_probe() -> dict:
    modules = ["numpy", "scipy", "numba", "spectralDNS", "shenfun", "mpi4py", "mpi4py_fft", "pyfftw"]
    commands = ["mpiexec", "mpirun", "fftw-wisdom", "fftw-wisdom-to-conf"]
    return {
        "python": platform.python_version(),
        "modules": {m: bool(importlib.util.find_spec(m)) for m in modules},
        "commands": {c: shutil.which(c) for c in commands},
        "native_host_ready": all(importlib.util.find_spec(m) is not None for m in ["spectralDNS", "shenfun", "mpi4py", "mpi4py_fft", "pyfftw"]),
    }


def main() -> None:
    witness = randomized_support_witness()
    bench = scan_benchmark()
    env = environment_probe()
    checks = {
        "support_witness_pass": witness["support_preserved"] and witness["max_outside_abs"] == 0.0,
        "negative_control_external_state_pass": witness["negative_control_external_state_mutation"]["expected_source_only_miss"],
        "negative_control_midstep_source_pass": witness["negative_control_midstep_source_mutation"]["expected_once_per_step_miss"],
        "native_host_unavailable_here": not env["native_host_ready"],
    }
    result = {
        "schema": "EM_CFD_NATIVE_HOST_PREFLIGHT_R6_V1",
        "seed": SEED,
        "checks": checks,
        "all_local_checks_pass": all(checks.values()),
        "candidate_contract": {
            "name": "PINNED_RK4_DERIVED_STATE_SUPPORT_GUARD_ELISION_CANDIDATE",
            "status": "NOT_ACTIVATED_NATIVE_HOST_PENDING",
            "tiers": {
                "conservative": "scan state and Source before every sparse nonlinear call",
                "pinned_rk4_source_each_stage": "after initial state certification, derive stage-state support by RK4 induction and scan Source before each stage",
                "pinned_rk4_source_once_per_step": "requires the stronger attestation that Source cannot change during a four-stage RK4 step and that step boundaries are exact"
            },
            "required_attestations": [
                "exact task-pinned RK4 stage algebra matches the audited four-stage affine update",
                "no callback or host code mutates RK stage state outside ComputeRHS/RK4 between guards",
                "nonlinear sparse output is complete on certified carrier C",
                "Nyquist masking only deletes support",
                "pressure projection and diffusion are modewise",
                "Source is scanned at the frequency justified by its mutation contract"
            ],
            "fallback": "retain conservative state_plus_source exact scan whenever any attestation is absent",
        },
        "finite_support_witness": witness,
        "scan_microbenchmark": bench,
        "environment": env,
        "claims_not_made": [
            "native spectralDNS execution",
            "native spectralDNS speedup",
            "PDE theorem",
            "universal state-scan redundancy outside the exact pinned host contract",
        ],
    }
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
