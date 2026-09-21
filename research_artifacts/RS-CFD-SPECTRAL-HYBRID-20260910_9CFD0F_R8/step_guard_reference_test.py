import numpy as np
import json

C = np.array([0,1,2,3], dtype=int)
N = 10

def outside(x):
    mask = np.ones(N, dtype=bool)
    mask[C] = False
    return bool(np.any(x[mask] != 0))

def rhs_closed(u, source):
    out = np.zeros_like(u)
    out[0] = 0.25*u[1]*u[2] - 0.125*u[0] + source[0]
    out[1] = -0.5*u[0]*u[2] + 0.25*u[3] + source[1]
    out[2] = 0.75*u[0]*u[1] - 0.2*u[2] + source[2]
    out[3] = -0.1*u[3] + 0.05*u[1] + source[3]
    return out

def rk4(u, source, dt=0.01, midstage=None):
    k1 = rhs_closed(u, source)
    if midstage is not None: midstage(u, source, 1)
    k2 = rhs_closed(u + 0.5*dt*k1, source)
    if midstage is not None: midstage(u, source, 2)
    k3 = rhs_closed(u + 0.5*dt*k2, source)
    if midstage is not None: midstage(u, source, 3)
    k4 = rhs_closed(u + dt*k3, source)
    return u + dt*(k1 + 2*k2 + 2*k3 + k4)/6

def dense_fallback(u, source):
    return u + 0.01*(-0.1*u + source)

def guarded_step(u, source, update=None, midstage=None):
    pre_escape = outside(u) or outside(source)
    if pre_escape:
        u2 = dense_fallback(u, source)
        route = "DENSE_FALLBACK"
    else:
        u2 = rk4(u.copy(), source, midstage=midstage)
        route = "CERTIFIED_CARRIER"
    if update is not None:
        update(u2, source)
    return u2, route

def init():
    u = np.zeros(N, dtype=np.complex128)
    s = np.zeros(N, dtype=np.complex128)
    u[C] = [1+0.2j, -0.3+0.7j, 0.4-0.1j, 0.2+0.05j]
    s[C] = [0.01, -0.02j, 0.005+0.003j, -0.004]
    return u, s

u, s = init()
for _ in range(50):
    u, r = guarded_step(u, s)
    assert r == "CERTIFIED_CARRIER"
assert not outside(u)

u, s = init()
def post_update(u, source):
    u[7] = 3e-6 + 2e-6j
    source[8] = -4e-6j
u, r0 = guarded_step(u, s, update=post_update)
assert r0 == "CERTIFIED_CARRIER" and outside(u) and outside(s)
u, r1 = guarded_step(u, s)
assert r1 == "DENSE_FALLBACK"

u, s = init()
def state_update(u, source):
    u[9] = 7e-6
u, _ = guarded_step(u, s, update=state_update)
assert outside(u) and not outside(s)
u, r_state = guarded_step(u, s)
assert r_state == "DENSE_FALLBACK"

u, s = init()
def mutate_midstage(u, source, stage):
    if stage == 1:
        u[6] = 1e-5
u2, r_mid = guarded_step(u, s, midstage=mutate_midstage)
assert r_mid == "CERTIFIED_CARRIER" and outside(u2)

guard_array_scans_per_step = {
    "R5_state_plus_source_each_stage": 8,
    "R6_source_each_stage_state_inductive": 4,
    "R7_source_once_state_attested": 1,
    "R8_state_plus_source_once_boundary": 2,
}
result = {
    "schema": "ENTERPRISE_MATH_CFD_R8_STEP_BOUNDARY_GUARD_RESULT",
    "positive_50_steps_state_in_carrier": True,
    "between_step_state_and_source_escape_detected_before_next_integrate": True,
    "between_step_state_only_escape_detected_before_next_integrate": True,
    "noncanonical_midstage_mutation_invalidates_once_per_step_certificate": True,
    "guard_array_scans_per_step": guard_array_scans_per_step,
    "r8_reduction_vs_r5": 4.0,
    "r8_reduction_vs_r6": 2.0,
    "scope": "control-flow/support certificate only; not spectralDNS native trajectory or speedup evidence",
    "status": "PASS"
}
print(json.dumps(result, indent=2, sort_keys=True))
