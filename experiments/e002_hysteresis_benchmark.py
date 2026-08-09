"""Deterministic engineering smoke benchmark for E002 precision hysteresis.

This benchmark does not claim that E002 outperforms classical symmetric
hysteresis.  In fact it verifies that the E002 relay is trajectory-equivalent
to a classical relay with thresholds at ``-d`` and ``+d``.  The engineering
question is whether ``d`` is already an intrinsic resolution coordinate rather
than an independently tuned deadband parameter.
"""

from enterprise_math.precision_hysteresis import (
    RelayState,
    minimum_switch_spacing,
    precision_relay,
    switch_count_upper_bound,
    switch_times,
    total_variation,
)


DISTURBANCE_CYCLE = (2, -2, 1, -1, 2, -2, -1, 1)
SAMPLES = 200
PRECISION = 4
HEAT_STEP = 1
COOL_STEP = 1


def memoryless_zero_relay(error: int, state: RelayState) -> RelayState:
    if error < 0:
        return RelayState.ON
    if error > 0:
        return RelayState.OFF
    return state


def classical_symmetric_hysteresis(
    error: int,
    state: RelayState,
    half_width: int,
) -> RelayState:
    if error <= -half_width:
        return RelayState.ON
    if error >= half_width:
        return RelayState.OFF
    return state


def run_controller(kind: str) -> dict[str, object]:
    physical_error = 0
    state = RelayState.OFF
    measured_errors: list[int] = []
    physical_errors: list[int] = []
    states: list[RelayState] = []

    for index in range(SAMPLES):
        disturbance = DISTURBANCE_CYCLE[index % len(DISTURBANCE_CYCLE)]
        measured_error = physical_error + disturbance
        measured_errors.append(measured_error)
        physical_errors.append(physical_error)

        if kind == "memoryless":
            state = memoryless_zero_relay(measured_error, state)
        elif kind == "precision":
            state = precision_relay(measured_error, state, PRECISION)
        elif kind == "classical":
            state = classical_symmetric_hysteresis(measured_error, state, PRECISION)
        else:
            raise ValueError(f"unknown controller kind: {kind}")

        states.append(state)
        physical_error += HEAT_STEP if state is RelayState.ON else -COOL_STEP

    times = switch_times(states)
    spacings = [right - left for left, right in zip(times, times[1:])]
    return {
        "measured_errors": tuple(measured_errors),
        "physical_errors": tuple(physical_errors),
        "states": tuple(states),
        "switches": len(times),
        "minimum_observed_switch_spacing": min(spacings) if spacings else 0,
    }


def main() -> None:
    memoryless = run_controller("memoryless")
    precision = run_controller("precision")
    classical = run_controller("classical")

    if precision["states"] != classical["states"]:
        raise AssertionError("precision relay diverged from equivalent symmetric hysteresis")

    measured_errors = precision["measured_errors"]
    variation = total_variation(measured_errors)
    maximum_step = max(
        abs(right - left)
        for left, right in zip(measured_errors, measured_errors[1:])
    )

    print(f"samples={SAMPLES}")
    print(f"disturbance_radius={max(abs(value) for value in DISTURBANCE_CYCLE)}")
    print(f"precision={PRECISION}")
    print(f"memoryless_switches={memoryless['switches']}")
    print(f"precision_switches={precision['switches']}")
    print(f"classical_symmetric_hysteresis_switches={classical['switches']}")
    print(f"measured_total_variation={variation}")
    print(f"measured_max_step={maximum_step}")
    print(
        "guaranteed_switch_spacing="
        f"{minimum_switch_spacing(PRECISION, maximum_step)}"
    )
    print(
        "observed_min_switch_spacing="
        f"{precision['minimum_observed_switch_spacing']}"
    )
    print(
        "variation_switch_bound="
        f"{switch_count_upper_bound(PRECISION, variation)}"
    )
    print(f"physical_error_min={min(precision['physical_errors'])}")
    print(f"physical_error_max={max(precision['physical_errors'])}")


if __name__ == "__main__":
    main()
