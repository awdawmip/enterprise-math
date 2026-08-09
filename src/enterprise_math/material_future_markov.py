"""Pure material-observable Markov state over finite clearance futures.

This module deliberately removes geometry diagnostics from the task state.  It
starts from the material-aware P024 quotient on represented positive clearance
states and extends the same pure response semantics across already-outside
states whenever the material observable cannot distinguish them.

For a declared horizon ``h`` the state stores only

    (W_h, c_1, ..., c_n),

where ``W_h`` is the finite material response word and ``c_i`` are material-
visible capped axis deficits.  No raw escape depth, inside/outside bit, collapse
factor, or clearance coordinate is retained.

The state is closed under one named primitive action while decrementing the
remaining horizon.  When the response word is constant, the task cannot tell
whether the chosen axis is geometrically active, so every action has the same
next pure state.  When the word is nonconstant, a zero capped deficit identifies
an active axis exactly.

Primitive contact and underresolved material states remain outside this pure
state domain because the declared material observable is not defined there by
this module.  A separate geometry/diagnostic wrapper may retain those facts.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_future_precision import (
    OUTSIDE,
    REPRESENTED,
    compile_material_future_precision,
    material_response_word,
    material_visible_deficit_cap,
)


@dataclass(frozen=True)
class PureMaterialFutureState:
    horizon: int
    response_word: tuple[int, ...]
    capped_deficits: tuple[int, ...]

    @property
    def dimension(self) -> int:
        return len(self.capped_deficits)


def _validated_pure_state(state: PureMaterialFutureState) -> int:
    if (
        isinstance(state.horizon, bool)
        or not isinstance(state.horizon, int)
        or state.horizon < 0
    ):
        raise ValueError("horizon must be a non-negative integer")
    if len(state.response_word) != state.horizon + 1:
        raise ValueError("response_word length must equal horizon+1")
    if not state.capped_deficits:
        raise ValueError("pure material state must have positive dimension")
    cap = material_visible_deficit_cap(state.response_word)
    for value in state.capped_deficits:
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("capped deficits must be non-negative integers")
        if value > cap:
            raise ValueError("capped deficit exceeds material-visible cap")
    if cap > 0 and not any(value == 0 for value in state.capped_deficits):
        raise ValueError("nonconstant material state must retain an active axis")
    if cap == 0 and any(state.capped_deficits):
        raise ValueError("constant material word must erase every direction deficit")
    return cap


def compile_pure_material_future_state(
    clearance: tuple[int, ...] | list[int],
    collapse_factor: int,
    response_samples: tuple[int, ...] | list[int],
    horizon: int,
) -> PureMaterialFutureState:
    """Compile the pure task state from represented or already-outside geometry.

    Primitive contact and underresolved geometry are rejected because this
    module intentionally does not invent a material observable for them.
    """
    diagnostic = compile_material_future_precision(
        clearance,
        collapse_factor,
        response_samples,
        horizon,
    )
    dimension = len(tuple(clearance))
    if diagnostic.status == REPRESENTED:
        state = PureMaterialFutureState(
            horizon=horizon,
            response_word=diagnostic.response_word,
            capped_deficits=diagnostic.capped_deficits,
        )
        _validated_pure_state(state)
        return state
    if diagnostic.status == OUTSIDE:
        word = material_response_word(response_samples, 0, horizon)
        state = PureMaterialFutureState(
            horizon=horizon,
            response_word=word,
            capped_deficits=(0,) * dimension,
        )
        _validated_pure_state(state)
        return state
    raise ValueError(
        "pure material future is undefined for primitive-contact or underresolved state"
    )


def advance_pure_material_future_state(
    state: PureMaterialFutureState,
    axis: int,
) -> PureMaterialFutureState:
    """Consume one named +e_axis action using only the pure quotient state."""
    cap = _validated_pure_state(state)
    if state.horizon == 0:
        raise ValueError("cannot consume an action at horizon zero")
    if isinstance(axis, bool) or not isinstance(axis, int):
        raise ValueError("axis must be an integer")
    if axis < 0 or axis >= state.dimension:
        raise ValueError("axis is outside the pure material state dimension")

    next_horizon = state.horizon - 1

    if cap == 0:
        # The entire response word is constant.  Active/nonactive geometry is
        # task-invisible, and prefix/suffix words coincide.
        next_word = state.response_word[:-1]
        result = PureMaterialFutureState(
            horizon=next_horizon,
            response_word=next_word,
            capped_deficits=(0,) * state.dimension,
        )
        _validated_pure_state(result)
        return result

    deficits = state.capped_deficits
    if deficits[axis] == 0:
        # Active axis: raw escape depth decreases by one, hence W_h -> W_h[1:].
        next_word = state.response_word[1:]
        next_cap = material_visible_deficit_cap(next_word)
        next_deficits = tuple(
            0 if index == axis else min(value + 1, next_cap)
            for index, value in enumerate(deficits)
        )
    else:
        # Nonactive axis: scalar depth is unchanged, hence W_h -> W_h[:-1].
        next_word = state.response_word[:-1]
        next_cap = material_visible_deficit_cap(next_word)
        next_deficits = tuple(
            min(value - 1, next_cap)
            if index == axis
            else min(value, next_cap)
            for index, value in enumerate(deficits)
        )

    result = PureMaterialFutureState(
        horizon=next_horizon,
        response_word=next_word,
        capped_deficits=next_deficits,
    )
    _validated_pure_state(result)
    return result
