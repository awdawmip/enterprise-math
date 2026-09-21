import json
import numpy as np

SEED = 20260921
N = 8
NU = 0.07
DT = 0.01


def wavenumbers(n):
    kx = np.fft.fftfreq(n) * n
    ky = np.fft.fftfreq(n) * n
    kz = np.fft.rfftfreq(n) * n
    return np.meshgrid(kx, ky, kz, indexing="ij")


K = np.stack(wavenumbers(N), axis=0)
K2 = np.sum(K * K, axis=0)


def kdot(v):
    return np.sum(K * v, axis=0)


def max_kdot(v):
    return float(np.max(np.abs(kdot(v))))


def project(v):
    out = np.array(v, dtype=np.complex128, copy=True)
    dot = kdot(out)
    denom = np.where(K2 == 0, 1.0, K2)
    out -= K * (dot / denom)
    return out


def solver_pressure_diffusion(raw_rhs, u_hat, nu=NU):
    # Exact algebra of pinned spectralDNS NS.py:add_pressure_diffusion.
    denom = np.where(K2 == 0, 1.0, K2)
    p_hat = np.sum(raw_rhs * (K / denom), axis=0)
    rhs = np.array(raw_rhs, dtype=np.complex128, copy=True)
    rhs -= K * p_hat
    rhs -= nu * K2 * u_hat
    return rhs, p_hat


def deterministic_raw_rhs(u_hat):
    # Host-independent witness: arbitrary unprojected convection-like field.
    # The verifier claim uses only that the pinned solver projects this part.
    return ((0.37 + 0.11j) * np.roll(u_hat, 1, axis=1)
            + (0.23 - 0.07j) * np.roll(u_hat, 1, axis=2))


def rhs(u_hat, source):
    raw = deterministic_raw_rhs(u_hat)
    projected_diffused, p_hat = solver_pressure_diffusion(raw, u_hat)
    return projected_diffused + source, p_hat


def rk4_step(u0, source_stages):
    k1, _ = rhs(u0, source_stages[0])
    k2, _ = rhs(u0 + 0.5 * DT * k1, source_stages[1])
    k3, _ = rhs(u0 + 0.5 * DT * k2, source_stages[2])
    k4, _ = rhs(u0 + DT * k3, source_stages[3])
    return u0 + DT * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0


rng = np.random.default_rng(SEED)
shape = (3, N, N, N // 2 + 1)

u_raw = rng.normal(size=shape) + 1j * rng.normal(size=shape)
u = project(u_raw)

raw_rhs = rng.normal(size=shape) + 1j * rng.normal(size=shape)
pd_rhs, p_hat = solver_pressure_diffusion(raw_rhs, u)

source_raw = rng.normal(size=shape) + 1j * rng.normal(size=shape)
source_transverse = project(source_raw)

phi = np.zeros((N, N, N // 2 + 1), dtype=np.complex128)
phi[1, 2, 1] = 1.25 - 0.4j
source_longitudinal = K * phi

rhs_transverse = pd_rhs + source_transverse
rhs_longitudinal = pd_rhs + source_longitudinal

# Pressure is computed before Source in pinned NS.py and is therefore identical
# irrespective of which Source is added afterwards.
pd_rhs_2, p_hat_2 = solver_pressure_diffusion(raw_rhs, u)

zero = np.zeros(shape, dtype=np.complex128)
u_rk_transverse = rk4_step(u, [source_transverse] * 4)
u_rk_zero = rk4_step(u, [zero] * 4)
u_rk_escape = rk4_step(
    u, [source_transverse, source_longitudinal,
        source_transverse, source_transverse])

tol = 5e-12
metrics = {
    "seed": SEED,
    "n": N,
    "initial_divergence_kdot_max": max_kdot(u),
    "projected_convection_plus_diffusion_kdot_max": max_kdot(pd_rhs),
    "transverse_source_kdot_max": max_kdot(source_transverse),
    "rhs_with_transverse_source_kdot_max": max_kdot(rhs_transverse),
    "longitudinal_source_kdot_max": max_kdot(source_longitudinal),
    "rhs_with_longitudinal_source_kdot_max": max_kdot(rhs_longitudinal),
    "pressure_recompute_difference_max": float(np.max(np.abs(p_hat - p_hat_2))),
    "rk4_zero_source_final_kdot_max": max_kdot(u_rk_zero),
    "rk4_transverse_source_final_kdot_max": max_kdot(u_rk_transverse),
    "rk4_one_longitudinal_stage_final_kdot_max": max_kdot(u_rk_escape),
}

checks = {
    "initial_projection_is_solenoidal": metrics["initial_divergence_kdot_max"] < tol,
    "solver_projection_plus_diffusion_preserves_solenoidality": metrics["projected_convection_plus_diffusion_kdot_max"] < tol,
    "transverse_source_is_solenoidal": metrics["transverse_source_kdot_max"] < tol,
    "transverse_source_preserves_rhs_solenoidality": metrics["rhs_with_transverse_source_kdot_max"] < tol,
    "longitudinal_source_breaks_rhs_solenoidality": metrics["rhs_with_longitudinal_source_kdot_max"] > 1e-6,
    "pressure_is_source_blind_in_pinned_ordering": metrics["pressure_recompute_difference_max"] == 0.0,
    "rk4_zero_source_preserves_solenoidality": metrics["rk4_zero_source_final_kdot_max"] < tol,
    "rk4_transverse_source_preserves_solenoidality": metrics["rk4_transverse_source_final_kdot_max"] < tol,
    "rk4_longitudinal_stage_is_detected": metrics["rk4_one_longitudinal_stage_final_kdot_max"] > 1e-8,
}

out = {
    "schema": "RS_CFD_SOURCE_DIVERGENCE_DIAGNOSTIC_V1",
    "source_authority": {
        "repository": "spectralDNS/spectralDNS",
        "blob_sha1": "6a11909d1e2c1d529d382952c4c9d77e7073645c",
        "functions": ["get_divergence", "add_pressure_diffusion", "ComputeRHS", "get_pressure"],
    },
    "algebraic_contract": {
        "pre_source": "K·R_pre = -nu*K^2*(K·U); hence zero when U is solenoidal",
        "post_source": "K·R_post = K·Source when U is solenoidal because Source is added after pressure projection",
        "forced_validity_precondition": "For incompressible-valid forced trajectories, every RK-stage Source must satisfy K·Source = 0 (within declared floating tolerance).",
        "negative_control": "A Source with longitudinal component may still match dense-vs-hybrid numerically, but it is not an incompressible-valid trajectory certificate under this pinned solver ordering.",
    },
    "tolerance": tol,
    "metrics": metrics,
    "checks": checks,
    "passed": all(checks.values()),
}

print(json.dumps(out, indent=2, sort_keys=True))
if not out["passed"]:
    raise SystemExit(1)
