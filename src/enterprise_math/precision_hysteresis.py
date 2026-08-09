"""Precision-native threshold control for Enterprise Math E002.

The model is deliberately finite and integer-only.  A signed target error is
observed at an explicit precision ``d``.  Errors inside the target-centered
precision fiber are not assigned a hidden finer sign; the response law keeps
the previous relay state until a represented threshold is crossed.

This module is an engineering pressure-test and executable specification, not a
claim that hysteresis itself is novel.  It also keeps observation, response,
and plant update as separate layers so future-sufficiency failures remain
visible rather than being hidden in one controller function.
"""

from __future__ import annotations

from enum import Enum
from typing import Iterable, Sequence


class RelayState(str, Enum):
    OFF = "OFF"
    ON = "ON"


class ThresholdObservation(str, Enum):
    BELOW = "BELOW"
    COLLAPSED = "COLLAPSED"
    ABOVE = "ABOVE"


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _require_positive(name: str, value: int) -> None:
    _require_int(name, value)
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def _require_nonnegative(name: str, value: int) -> None:
    _require_int(name, value)
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")


def _require_state(state: RelayState) -> None:
    if not isinstance(state, RelayState):
        raise TypeError("state must be a RelayState")


def _ceil_div_nonnegative(numerator: int, denominator: int) -> int:
    _require_nonnegative("numerator", numerator)
    _require_positive("denominator", denominator)
    return (numerator + denominator - 1) // denominator


def threshold_observation(error: int, precision: int) -> ThresholdObservation:
    """Observe a signed target error at target-centered integer precision.

    ``BELOW`` means ``error <= -precision``.
    ``ABOVE`` means ``error >= precision``.
    Every integer strictly between those thresholds belongs to one collapsed
    target fiber.
    """
    _require_int("error", error)
    _require_positive("precision", precision)
    if error <= -precision:
        return ThresholdObservation.BELOW
    if error >= precision:
        return ThresholdObservation.ABOVE
    return ThresholdObservation.COLLAPSED


def precision_relay(
    error: int,
    state: RelayState,
    precision: int,
) -> RelayState:
    """Apply the E002 response law.

    A represented low-side separation turns the relay ON, a represented
    high-side separation turns it OFF, and the collapsed target fiber preserves
    the prior state.
    """
    _require_state(state)
    observation = threshold_observation(error, precision)
    if observation is ThresholdObservation.BELOW:
        return RelayState.ON
    if observation is ThresholdObservation.ABOVE:
        return RelayState.OFF
    return state


def compatible_relay_states(
    true_error: int,
    state: RelayState,
    precision: int,
    noise_radius: int,
) -> tuple[RelayState, ...]:
    """Exact MAY-set under bounded additive integer measurement disturbance."""
    _require_int("true_error", true_error)
    _require_state(state)
    _require_positive("precision", precision)
    _require_nonnegative("noise_radius", noise_radius)
    possible = {
        precision_relay(true_error + disturbance, state, precision)
        for disturbance in range(-noise_radius, noise_radius + 1)
    }
    return tuple(sorted(possible, key=lambda item: item.value))


def noise_immunity_precision(noise_radius: int) -> int:
    """Smallest integer precision whose central fiber contains [-N, N]."""
    _require_nonnegative("noise_radius", noise_radius)
    return noise_radius + 1


def total_variation(values: Sequence[int]) -> int:
    """Return integer total variation of a finite measured-error sequence."""
    for value in values:
        _require_int("sequence value", value)
    return sum(abs(right - left) for left, right in zip(values, values[1:]))


def switch_times(states: Sequence[RelayState]) -> tuple[int, ...]:
    """Indices at which a finite relay-state sequence changes value."""
    for state in states:
        _require_state(state)
    return tuple(
        index
        for index in range(1, len(states))
        if states[index] is not states[index - 1]
    )


def minimum_switch_spacing(precision: int, maximum_error_step: int) -> int:
    """Guaranteed samples between consecutive opposite switches.

    Opposite thresholds are ``2*precision`` apart.  If every adjacent measured
    error changes by at most ``maximum_error_step > 0``, at least
    ``ceil(2*precision / maximum_error_step)`` sample intervals are required.
    """
    _require_positive("precision", precision)
    _require_positive("maximum_error_step", maximum_error_step)
    return _ceil_div_nonnegative(2 * precision, maximum_error_step)


def switch_count_upper_bound(precision: int, variation: int) -> int:
    """Universal variation bound ``K <= 1 + floor(TV/(2d))``."""
    _require_positive("precision", precision)
    _require_nonnegative("variation", variation)
    return 1 + variation // (2 * precision)


def thermostat_step(
    error: int,
    state: RelayState,
    precision: int,
    heat_step: int,
    cool_step: int,
) -> tuple[int, RelayState]:
    """One noiseless controller-then-plant step.

    ``ON`` increases the target error by ``heat_step`` and ``OFF`` decreases it
    by ``cool_step``.  Both plant increments are positive integers.
    """
    _require_int("error", error)
    _require_state(state)
    _require_positive("precision", precision)
    _require_positive("heat_step", heat_step)
    _require_positive("cool_step", cool_step)
    output = precision_relay(error, state, precision)
    next_error = error + heat_step if output is RelayState.ON else error - cool_step
    return next_error, output


def thermostat_trace(
    initial_error: int,
    initial_state: RelayState,
    precision: int,
    heat_step: int,
    cool_step: int,
    steps: int,
) -> tuple[tuple[int, RelayState], ...]:
    """Return ``(error, state)`` samples before each plant update plus terminal state."""
    _require_int("initial_error", initial_error)
    _require_state(initial_state)
    _require_positive("precision", precision)
    _require_positive("heat_step", heat_step)
    _require_positive("cool_step", cool_step)
    _require_nonnegative("steps", steps)
    error = initial_error
    state = initial_state
    trace = [(error, state)]
    for _ in range(steps):
        error, state = thermostat_step(
            error,
            state,
            precision,
            heat_step,
            cool_step,
        )
        trace.append((error, state))
    return tuple(trace)


def next_switch_witness(
    error: int,
    state: RelayState,
    precision: int,
    heat_step: int,
    cool_step: int,
) -> bool:
    """One bit saying whether the next plant update crosses the opposite threshold."""
    _require_int("error", error)
    _require_state(state)
    _require_positive("precision", precision)
    _require_positive("heat_step", heat_step)
    _require_positive("cool_step", cool_step)
    current_output = precision_relay(error, state, precision)
    if current_output is RelayState.ON:
        return error + heat_step >= precision
    return error - cool_step <= -precision


def one_step_future_key(
    error: int,
    state: RelayState,
    precision: int,
    heat_step: int,
    cool_step: int,
) -> tuple[ThresholdObservation, RelayState, bool]:
    """Task-relative repaired coarse state for one additional relay decision."""
    return (
        threshold_observation(error, precision),
        state,
        next_switch_witness(error, state, precision, heat_step, cool_step),
    )


def two_relay_outputs(
    error: int,
    state: RelayState,
    precision: int,
    heat_step: int,
    cool_step: int,
) -> tuple[RelayState, RelayState]:
    """Current relay output and output at the next sampled decision."""
    current_output = precision_relay(error, state, precision)
    next_error = error + heat_step if current_output is RelayState.ON else error - cool_step
    next_output = precision_relay(next_error, current_output, precision)
    return current_output, next_output


def thermostat_invariant_bounds(
    precision: int,
    heat_step: int,
    cool_step: int,
) -> tuple[int, int]:
    """Finite invariant error interval for the noiseless thermostat map."""
    _require_positive("precision", precision)
    _require_positive("heat_step", heat_step)
    _require_positive("cool_step", cool_step)
    return -precision - cool_step + 1, precision + heat_step - 1


def upper_switch_return(
    upper_error: int,
    precision: int,
    heat_step: int,
    cool_step: int,
) -> dict[str, int]:
    """Exact next upper-switch sample after one OFF/ON excursion.

    The input is an upper switch sample in ``[d, d+h-1]``.  The returned
    dictionary contains the number of OFF plant steps, the lower switch sample,
    the number of ON plant steps, and the next upper switch sample.
    """
    _require_int("upper_error", upper_error)
    _require_positive("precision", precision)
    _require_positive("heat_step", heat_step)
    _require_positive("cool_step", cool_step)
    if not precision <= upper_error <= precision + heat_step - 1:
        raise ValueError("upper_error must lie in [precision, precision + heat_step - 1]")

    off_steps = _ceil_div_nonnegative(upper_error + precision, cool_step)
    lower_error = upper_error - off_steps * cool_step
    on_steps = _ceil_div_nonnegative(precision - lower_error, heat_step)
    next_upper_error = lower_error + on_steps * heat_step
    return {
        "off_steps": off_steps,
        "lower_error": lower_error,
        "on_steps": on_steps,
        "next_upper_error": next_upper_error,
    }


def apply_relay_to_errors(
    errors: Iterable[int],
    initial_state: RelayState,
    precision: int,
) -> tuple[RelayState, ...]:
    """Apply the relay to a finite measured-error stream without a plant model."""
    _require_state(initial_state)
    _require_positive("precision", precision)
    state = initial_state
    outputs: list[RelayState] = []
    for error in errors:
        _require_int("error", error)
        state = precision_relay(error, state, precision)
        outputs.append(state)
    return tuple(outputs)
