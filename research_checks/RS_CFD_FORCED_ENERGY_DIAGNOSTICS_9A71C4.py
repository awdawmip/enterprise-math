#!/usr/bin/env python3
"""Verifier-owned forced-energy/source-work diagnostics for RS-CFD-TRAJECTORY-VERIFY-20260910.

This checker does not emulate spectralDNS. It validates only the algebra/storage-independent
contract that a native-host verifier may use for static/dynamic Source work diagnostics.
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass
from typing import Callable

import numpy as np

SEED = 20260921
N = 8
L = 2.0 * math.pi
DT_LEVELS = (0.4, 0.2, 0.1, 0.05)


def inner(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.mean(np.sum(a * b, axis=0)))


def kinetic_energy(u: np.ndarray) -> float:
    return 0.5 * inner(u, u)


def spectral_divergence_max(v: np.ndarray) -> float:
    """Return max |K·v_hat| for a real 3-vector field on a 2π-periodic cubic grid."""
    n = v.shape[1]
    dx = L / n
    kxy = 2.0 * math.pi * np.fft.fftfreq(n, d=dx)
    kz = 2.0 * math.pi * np.fft.rfftfreq(n, d=dx)
    vh = np.fft.rfftn(v, axes=(1, 2, 3))
    div = (
        kxy[:, None, None] * vh[0]
        + kxy[None, :, None] * vh[1]
        + kz[None, None, :] * vh[2]
    )
    return float(np.max(np.abs(div)))


@dataclass
class StepResult:
    u1: np.ndarray
    source_work: float
    total_stage_power: tuple[float, float, float, float]
    source_stage_power: tuple[float, float, float, float]


def rk4_step(
    u0: np.ndarray,
    t0: float,
    dt: float,
    rhs: Callable[[np.ndarray, float], np.ndarray],
    source: Callable[[np.ndarray, float], np.ndarray],
) -> StepResult:
    """Classical RK4 plus verifier-side source-work quadrature on the actual RK stages."""
    u1s = u0
    k1 = rhs(u1s, t0)
    f1 = source(u1s, t0)

    u2s = u0 + 0.5 * dt * k1
    k2 = rhs(u2s, t0 + 0.5 * dt)
    f2 = source(u2s, t0 + 0.5 * dt)

    u3s = u0 + 0.5 * dt * k2
    k3 = rhs(u3s, t0 + 0.5 * dt)
    f3 = source(u3s, t0 + 0.5 * dt)

    u4s = u0 + dt * k3
    k4 = rhs(u4s, t0 + dt)
    f4 = source(u4s, t0 + dt)

    u1 = u0 + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
    ws = dt * (
        inner(u1s, f1) / 6.0
        + inner(u2s, f2) / 3.0
        + inner(u3s, f3) / 3.0
        + inner(u4s, f4) / 6.0
    )
    return StepResult(
        u1=u1,
        source_work=float(ws),
        total_stage_power=(inner(u1s, k1), inner(u2s, k2), inner(u3s, k3), inner(u4s, k4)),
        source_stage_power=(inner(u1s, f1), inner(u2s, f2), inner(u3s, f3), inner(u4s, f4)),
    )


def build_fields() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    x = np.arange(N, dtype=float) * L / N
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    # curl(0,0,sin(x)sin(y)cos(z)): analytically divergence free.
    f_transverse = np.stack(
        [
            np.sin(X) * np.cos(Y) * np.cos(Z),
            -np.cos(X) * np.sin(Y) * np.cos(Z),
            np.zeros_like(X),
        ]
    )
    # grad(sin(x)sin(y)): deliberately longitudinal/non-solenoidal negative control.
    f_longitudinal = np.stack(
        [
            np.cos(X) * np.sin(Y),
            np.sin(X) * np.cos(Y),
            np.zeros_like(X),
        ]
    )
    # A deterministic real initial state with nonzero overlap with the forcing mode.
    u0 = 0.3 * f_transverse + 0.15 * np.stack(
        [np.cos(Y) * np.sin(Z), np.zeros_like(X), -np.sin(Y) * np.cos(Z)]
    )
    return u0, f_transverse, f_longitudinal


def main() -> None:
    np.random.seed(SEED)
    u0, f0, f_long = build_fields()
    checks: dict[str, bool] = {}
    metrics: dict[str, object] = {}

    div_trans = spectral_divergence_max(f0)
    div_long = spectral_divergence_max(f_long)
    metrics["transverse_source_max_abs_K_dot_Fhat"] = div_trans
    metrics["longitudinal_negative_control_max_abs_K_dot_Fhat"] = div_long
    checks["transverse_source_is_spectral_divergence_free"] = div_trans < 1e-10
    checks["longitudinal_negative_control_is_detected"] = div_long > 1.0

    t0 = 0.37
    f_const = lambda _u, _t: f0
    rhs_const = lambda u, t: f_const(u, t)
    r_const = rk4_step(u0, t0, 0.2, rhs_const, f_const)
    de_const = kinetic_energy(r_const.u1) - kinetic_energy(u0)
    const_defect = de_const - r_const.source_work
    metrics["constant_source_delta_E"] = de_const
    metrics["constant_source_RK4_weighted_source_work"] = r_const.source_work
    metrics["constant_source_balance_defect"] = const_defect
    checks["constant_source_source_only_balance_is_roundoff_exact"] = abs(const_defect) < 1e-13

    amp = lambda t: 1.0 + 0.2 * math.sin(t)
    f_dyn = lambda _u, t: amp(t) * f0
    rhs_dyn = lambda u, t: f_dyn(u, t)
    defects = []
    for dt in DT_LEVELS:
        r = rk4_step(u0, t0, dt, rhs_dyn, f_dyn)
        defects.append(abs((kinetic_energy(r.u1) - kinetic_energy(u0)) - r.source_work))
    ratios = [defects[i] / defects[i + 1] for i in range(len(defects) - 1)]
    metrics["dynamic_source_dt_levels"] = list(DT_LEVELS)
    metrics["dynamic_source_abs_balance_defects"] = defects
    metrics["dynamic_source_defect_halving_ratios"] = ratios
    checks["dynamic_source_defect_decreases_on_each_halving"] = all(
        defects[i + 1] < defects[i] for i in range(len(defects) - 1)
    )
    checks["dynamic_source_finest_defect_is_small"] = defects[-1] < 1e-12

    nu = 0.7
    f_forced = lambda _u, t: amp(t) * f0
    rhs_forced = lambda u, t: -nu * u + f_forced(u, t)
    r_forced = rk4_step(u0, t0, 0.1, rhs_forced, f_forced)
    de_forced = kinetic_energy(r_forced.u1) - kinetic_energy(u0)
    source_only_gap = de_forced - r_forced.source_work
    metrics["dissipative_forced_delta_E"] = de_forced
    metrics["dissipative_forced_source_work"] = r_forced.source_work
    metrics["dissipative_forced_delta_E_minus_source_work"] = source_only_gap
    checks["source_work_alone_is_not_total_energy_balance"] = abs(source_only_gap) > 1e-5

    f_bad = lambda _u, _t: f_long
    rhs_bad = lambda u, t: f_bad(u, t)
    r_bad = rk4_step(u0, t0, 0.1, rhs_bad, f_bad)
    bad_energy_defect = (kinetic_energy(r_bad.u1) - kinetic_energy(u0)) - r_bad.source_work
    metrics["longitudinal_source_energy_balance_defect"] = bad_energy_defect
    checks["energy_work_consistency_does_not_imply_incompressibility"] = (
        abs(bad_energy_defect) < 1e-13 and div_long > 1.0
    )

    # Dynamic scalar amplitude preserves the transverse spatial support/divergence condition.
    dyn_divs = [spectral_divergence_max(amp(t) * f0) for t in (0.0, 0.37, 0.5, 1.0)]
    metrics["dynamic_transverse_source_max_abs_K_dot_Fhat_samples"] = dyn_divs
    checks["dynamic_scalar_amplitude_preserves_transversality"] = max(dyn_divs) < 1e-10

    passed = sum(bool(v) for v in checks.values())
    result = {
        "schema": "RS_CFD_FORCED_ENERGY_DIAGNOSTICS_V1",
        "task_id": "RS-CFD-TRAJECTORY-VERIFY-20260910",
        "researcher_id": "EM-CFD-VFY-9A71C4",
        "seed": SEED,
        "grid_n": N,
        "checks": checks,
        "summary": {"passed": passed, "total": len(checks), "all_passed": passed == len(checks)},
        "metrics": metrics,
        "scope_boundary": {
            "certifies": [
                "the source-work diagnostic algebra used by this checker",
                "transversality of the synthetic positive-control forcing family",
                "orthogonality of energy-work and incompressibility diagnostics",
            ],
            "does_not_certify": [
                "spectralDNS host execution",
                "full Navier-Stokes energy balance",
                "dense-vs-hybrid trajectory equivalence",
                "PDE convergence or physical correctness",
            ],
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
