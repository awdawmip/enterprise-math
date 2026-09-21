"""Independent r2c trajectory diagnostics for RS-CFD-TRAJECTORY-VERIFY-20260910.

This checker is host-independent: it specifies the exact half-spectrum Hermitian planes
for the spectralDNS storage shape (3,n,n,n//2+1), records physical kinetic energy, and
self-tests the diagnostics using NumPy-generated real fields. It does not claim a native
spectralDNS rerun.
"""
from __future__ import annotations
import json
import numpy as np

ATOL = 5e-12
RTOL = 5e-11

def _infer_even_n_from_r2c(a: np.ndarray) -> int:
    nzr = int(a.shape[-1])
    if nzr < 2:
        raise ValueError("r2c axis must contain at least DC and one positive-frequency slot")
    return 2 * (nzr - 1)

def hermitian_boundary_report(u_hat: np.ndarray, *, atol: float = ATOL, rtol: float = RTOL) -> dict:
    """Check all stored Hermitian pair constraints for an even-size real-to-complex 3D FFT.

    For shape (..., nx, ny, n//2+1), the negative-kz partner of an interior 0<kz<n/2
    coefficient is not stored. Therefore only kz=0 and kz=n/2 are self-contained planes.
    On each such plane:
        U(-kx,-ky,kz) = conj(U(kx,ky,kz)).
    """
    a = np.asarray(u_hat)
    if a.ndim < 3:
        raise ValueError("expected at least 3 spectral axes")
    nx, ny, nzr = map(int, a.shape[-3:])
    n = _infer_even_n_from_r2c(a)
    if nx != n or ny != n:
        raise ValueError(f"checker is frozen for cubic even host arrays; got {(nx, ny, nzr)}")
    scale = float(np.max(np.abs(a))) if a.size else 0.0
    tol = float(atol + rtol * scale)
    worst_residual = 0.0
    worst_index = None
    plane_reports = []
    for kz in (0, n // 2):
        plane = a[..., :, :, kz]
        plane_worst = 0.0
        plane_index = None
        for ix in range(n):
            nix = (-ix) % n
            for iy in range(n):
                niy = (-iy) % n
                lhs = plane[..., nix, niy]
                rhs = np.conj(plane[..., ix, iy])
                r = float(np.max(np.abs(lhs - rhs)))
                if r > plane_worst:
                    plane_worst = r
                    plane_index = [ix, iy, kz]
                if r > worst_residual:
                    worst_residual = r
                    worst_index = [ix, iy, kz]
        plane_reports.append({
            "kz": kz,
            "max_residual": plane_worst,
            "worst_index": plane_index,
            "pass": bool(plane_worst <= tol),
        })
    return {
        "storage": "r2c-even-cube",
        "n": n,
        "stored_shape": list(a.shape),
        "checked_planes": [0, n // 2],
        "interior_kz_policy": "NEGATIVE_KZ_PARTNER_NOT_STORED; do not invent a stored-pair check",
        "scale": scale,
        "tolerance": tol,
        "max_residual": worst_residual,
        "worst_index": worst_index,
        "planes": plane_reports,
        "pass": bool(worst_residual <= tol),
    }

def physical_kinetic_energy(u_real: np.ndarray) -> float:
    """0.5 * spatial mean of |u|^2 for component-first real velocity."""
    u = np.asarray(u_real)
    if u.ndim < 4:
        raise ValueError("expected component-first 3D real velocity")
    if not np.isrealobj(u):
        raise ValueError("u_real must be real")
    return float(0.5 * np.mean(np.sum(np.asarray(u, dtype=np.float64) ** 2, axis=0)))

def numpy_rfftn_parseval_energy(u_hat: np.ndarray) -> float:
    """Energy implied by NumPy's default unnormalised rfftn, used only as a checker self-test."""
    h = np.asarray(u_hat)
    n = _infer_even_n_from_r2c(h)
    if h.shape[-3:] != (n, n, n // 2 + 1):
        raise ValueError("expected cubic even r2c array")
    w = np.ones(n // 2 + 1, dtype=np.float64)
    if n // 2 > 1:
        w[1:-1] = 2.0
    weighted = np.sum(np.abs(h) ** 2 * w.reshape((1, 1, 1, -1)))
    N = n ** 3
    return float(0.5 * weighted / (N ** 2))

def energy_series_report(energies, *, zero_source: bool, atol: float = 1e-12, rtol: float = 1e-10) -> dict:
    e = np.asarray(energies, dtype=np.float64)
    if e.ndim != 1 or e.size < 2 or not np.isfinite(e).all():
        raise ValueError("finite 1D energy series with >=2 entries required")
    deltas = np.diff(e)
    tol = float(atol + rtol * max(float(abs(e[0])), 1.0))
    increases = np.flatnonzero(deltas > tol)
    return {
        "count": int(e.size),
        "initial": float(e[0]),
        "final": float(e[-1]),
        "min": float(e.min()),
        "max": float(e.max()),
        "max_step_increase": float(max(float(deltas.max()), 0.0)),
        "zero_source": bool(zero_source),
        "monotonic_nonincrease_gate_applied": bool(zero_source),
        "increase_indices": increases.tolist(),
        "pass": bool(increases.size == 0) if zero_source else None,
        "forced_policy": None if zero_source else "RECORD_SERIES_ONLY; forcing may inject energy, so monotonic decay is not a valid generic gate",
    }

def endpoint_refinement_report(coarse: np.ndarray, fine: np.ndarray) -> dict:
    a = np.asarray(coarse)
    b = np.asarray(fine)
    if a.shape != b.shape:
        raise ValueError("coarse and fine endpoint arrays must have identical shapes")
    absolute = float(np.max(np.abs(a - b)))
    scale = float(max(np.max(np.abs(b)), 1e-30))
    return {"absolute_max": absolute, "relative_to_fine_max": absolute / scale}

def self_test(seed: int = 20260921) -> dict:
    rng = np.random.default_rng(seed)
    n = 8
    u = rng.normal(size=(3, n, n, n))
    h = np.fft.rfftn(u, axes=(-3, -2, -1))
    herm = hermitian_boundary_report(h)
    ep = physical_kinetic_energy(u)
    es = numpy_rfftn_parseval_energy(h)

    bad_zero = h.copy()
    bad_zero[0, 1, 2, 0] += 1j * 1e-6
    bad_zero_report = hermitian_boundary_report(bad_zero)

    bad_nyq = h.copy()
    bad_nyq[1, 2, 3, n // 2] += 1e-6
    bad_nyq_report = hermitian_boundary_report(bad_nyq)

    interior = h.copy()
    interior[2, 1, 1, 1] += (2e-6 + 3e-6j)
    interior_report = hermitian_boundary_report(interior)
    interior_real = np.fft.irfftn(interior, s=(n, n, n), axes=(-3, -2, -1))

    zero_source_energy = energy_series_report(np.exp(-0.03 * np.arange(6)), zero_source=True)
    forced_energy = energy_series_report([1.0, 1.1, 1.05, 1.2], zero_source=False)

    checks = {
        "real_field_boundary_conjugacy": herm["pass"],
        "parseval_energy": abs(ep - es) <= 5e-13,
        "kz0_violation_detected": not bad_zero_report["pass"],
        "nyquist_violation_detected": not bad_nyq_report["pass"],
        "interior_kz_not_falsely_pair_checked": interior_report["pass"] and np.isrealobj(interior_real),
        "zero_source_decay_gate": zero_source_energy["pass"],
        "forced_energy_not_misgated": forced_energy["pass"] is None,
    }
    return {
        "schema": "ENTERPRISE_MATH_CFD_TRAJECTORY_DIAGNOSTIC_SELFTEST_V1",
        "seed": seed,
        "n": n,
        "checks": checks,
        "pass": all(checks.values()),
        "reference": {
            "physical_energy": ep,
            "numpy_rfftn_parseval_energy": es,
            "energy_absolute_difference": abs(ep - es),
            "boundary_report": herm,
            "kz0_injected_residual": bad_zero_report["max_residual"],
            "nyquist_injected_residual": bad_nyq_report["max_residual"],
            "interior_kz_boundary_residual": interior_report["max_residual"],
            "zero_source_energy": zero_source_energy,
            "forced_energy": forced_energy,
        },
    }

if __name__ == "__main__":
    result = self_test()
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["pass"] else 1)
