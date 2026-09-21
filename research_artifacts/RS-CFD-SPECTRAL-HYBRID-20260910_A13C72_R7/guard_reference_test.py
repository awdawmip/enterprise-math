import json
import numpy as np

CARRIER = np.array([True, True, False, False])

def outside_support(x):
    x = np.asarray(x)
    return bool(np.any(x[..., ~CARRIER] != 0))

def rhs(u, source):
    # Stand-in for any carrier-preserving nonlinear+projection+diffusion map.
    # The task-local property under test is control-flow placement of Source scans.
    out = np.zeros_like(u)
    out[..., CARRIER] = -u[..., CARRIER]
    out = out + source
    return out

def rk4_step(u0, source, dt=0.1, midstage_callback=None):
    # Mirrors the pinned spectralDNS RK4 dataflow: u1=step entry, u2 accumulator,
    # four RHS calls, no application update callback in the canonical host path.
    u1 = u0.copy()
    u2 = u0.copy()
    a = (1/6, 1/3, 1/3, 1/6)
    b = (1/2, 1/2, 1)
    u = u0.copy()
    for rk in range(4):
        if midstage_callback is not None:
            midstage_callback(rk, u, source)
        r = rhs(u, source)
        if rk < 3:
            u = u1 + b[rk] * dt * r
        u2 = u2 + a[rk] * dt * r
    return u2

def canonical_solve_two_steps():
    u = np.array([1.0, -0.5, 0.0, 0.0])
    source = np.array([0.2, 0.0, 0.0, 0.0])
    scans = []
    # Exact contract: scan immediately before integrate(), application update only after it.
    for step in range(2):
        scans.append(outside_support(source))
        assert not scans[-1]
        u = rk4_step(u, source)
        assert not outside_support(u)
        # Application update occurs after full RK4. Change Source support here for next step.
        if step == 0:
            source[:] = np.array([0.1, 0.0, 0.0, 0.0])
    return scans, u.tolist()

def detects_between_step_update():
    u = np.array([1.0, 0.0, 0.0, 0.0])
    source = np.zeros(4)
    assert not outside_support(source)
    u = rk4_step(u, source)
    # Post-step update injects an escape.
    source[2] = 1.0
    # Next pre-integrate scan catches before any RHS call of the next step.
    return outside_support(source)

def negative_noncanonical_midstage():
    u = np.array([1.0, 0.0, 0.0, 0.0])
    source = np.zeros(4)
    assert not outside_support(source)
    def mutate(rk, _u, s):
        if rk == 1:
            s[2] = 1.0
    out = rk4_step(u, source, midstage_callback=mutate)
    # This is the failure mode once-per-step scanning cannot guard.
    return outside_support(out)

def main():
    scans, u = canonical_solve_two_steps()
    result = {
        "canonical_pre_step_scans": scans,
        "canonical_state_remains_in_carrier": not outside_support(np.array(u)),
        "post_step_source_escape_detected_before_next_integrate": detects_between_step_update(),
        "noncanonical_midstage_mutation_breaks_once_per_step_guard": negative_noncanonical_midstage(),
        "status": "PASS"
    }
    assert result["canonical_pre_step_scans"] == [False, False]
    assert result["canonical_state_remains_in_carrier"]
    assert result["post_step_source_escape_detected_before_next_integrate"]
    assert result["noncanonical_midstage_mutation_breaks_once_per_step_guard"]
    print(json.dumps(result, sort_keys=True))

if __name__ == "__main__":
    main()
