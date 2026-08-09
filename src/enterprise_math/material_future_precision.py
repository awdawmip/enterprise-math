"""Material-observable future precision as a strict quotient of raw escape depth.

This module composes the canonical P024 clearance-horizon state with a declared
finite material response branch ``R(depth)``.  The geometry may distinguish
residual escape depth exactly while the task observes only the material sample.
Material plateaus can therefore erase spatial detail that raw-depth futures
would otherwise force.

For one represented isotropic positive-clearance state, write

    q = max_i g_i,
    k = d-q,
    r_i = q-g_i.

At horizon h define the material response word

    W_h(k) = (R(k), R((k-1)_+), ..., R((k-h)_+)).

If the word is constant, no progress inside the horizon is material-visible and
all relative axis deficits are discardable.  Otherwise let ``c0`` be the first
step where the word differs from its initial sample and put

    H_R = h-c0+1.

The coarsest named-axis material-future signature is

    (W_h(k), min(r_1,H_R), ..., min(r_n,H_R)).

Any deficit >=H_R cannot reach even the first material-visible response boundary
within h actions.  Every smaller deficit is necessary: spending ``r_i+c0``
actions on that named axis distinguishes it from any larger deficit.

The theorem does not require monotonic response values; only the finite response
word is observed.  This module intentionally treats branch depth/capacity as
separate from material amplitude precision, measurement scale, and spatial
factor.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import comb

REPRESENTED = "REPRESENTED"
UNDERRESOLVED = "UNDERRESOLVED"
OUTSIDE = "OUTSIDE"
PRIMITIVE_CONTACT = "PRIMITIVE_CONTACT"


def _require_nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _validated_response_samples(
    response_samples: tuple[int, ...] | list[int],
) -> tuple[int, ...]:
    samples = tuple(response_samples)
    if not samples:
        raise ValueError("response_samples must be nonempty")
    for sample in samples:
        if isinstance(sample, bool) or not isinstance(sample, int):
            raise ValueError("response samples must be integers")
    return samples


def material_response_word(
    response_samples: tuple[int, ...] | list[int],
    depth: int,
    horizon: int,
) -> tuple[int, ...]:
    """Return the depth-decrement response word visible for one scalar state."""
    samples = _validated_response_samples(response_samples)
    _require_nonnegative("depth", depth)
    _require_nonnegative("horizon", horizon)
    if depth >= len(samples):
        raise ValueError("depth is not represented by the material branch")
    return tuple(samples[max(depth - step, 0)] for step in range(horizon + 1))


def material_visible_deficit_cap(response_word: tuple[int, ...] | list[int]) -> int:
    """Return H_R, or 0 when the whole horizon lies on one response plateau."""
    word = tuple(response_word)
    if not word:
        raise ValueError("response_word must be nonempty")
    first = word[0]
    for step, sample in enumerate(word[1:], start=1):
        if sample != first:
            horizon = len(word) - 1
            return horizon - step + 1
    return 0


@dataclass(frozen=True)
class MaterialFuturePrecisionState:
    """Coarsest named-axis future signature for one material response task."""

    dimension: int
    collapse_factor: int
    horizon: int
    status: str
    escape_depth: int | None
    response_word: tuple[int, ...]
    visible_deficit_cap: int
    capped_deficits: tuple[int, ...]


def compile_material_future_precision(
    clearance: tuple[int, ...] | list[int],
    collapse_factor: int,
    response_samples: tuple[int, ...] | list[int],
    horizon: int,
) -> MaterialFuturePrecisionState:
    """Compile one isotropic positive-clearance material-future quotient state."""
    _require_positive("collapse_factor", collapse_factor)
    _require_nonnegative("horizon", horizon)
    samples = _validated_response_samples(response_samples)
    state = tuple(clearance)
    if not state:
        raise ValueError("clearance state must be nonempty")
    for value in state:
        _require_nonnegative("clearance coordinate", value)

    if any(value >= collapse_factor for value in state):
        return MaterialFuturePrecisionState(
            dimension=len(state),
            collapse_factor=collapse_factor,
            horizon=horizon,
            status=OUTSIDE,
            escape_depth=0,
            response_word=material_response_word(samples, 0, horizon),
            visible_deficit_cap=0,
            capped_deficits=(),
        )
    if not any(state):
        return MaterialFuturePrecisionState(
            dimension=len(state),
            collapse_factor=collapse_factor,
            horizon=horizon,
            status=PRIMITIVE_CONTACT,
            escape_depth=None,
            response_word=(),
            visible_deficit_cap=0,
            capped_deficits=(),
        )

    q = max(state)
    depth = collapse_factor - q
    if depth >= len(samples):
        return MaterialFuturePrecisionState(
            dimension=len(state),
            collapse_factor=collapse_factor,
            horizon=horizon,
            status=UNDERRESOLVED,
            escape_depth=depth,
            response_word=(),
            visible_deficit_cap=0,
            capped_deficits=(),
        )

    word = material_response_word(samples, depth, horizon)
    cap = material_visible_deficit_cap(word)
    deficits = tuple(q - value for value in state)
    return MaterialFuturePrecisionState(
        dimension=len(state),
        collapse_factor=collapse_factor,
        horizon=horizon,
        status=REPRESENTED,
        escape_depth=depth,
        response_word=word,
        visible_deficit_cap=cap,
        capped_deficits=tuple(min(deficit, cap) for deficit in deficits),
    )


def _action_count_vectors(dimension: int, horizon: int) -> tuple[tuple[int, ...], ...]:
    """Enumerate commutative named-action counts in one deterministic order."""
    result: list[tuple[int, ...]] = []
    for total in range(horizon + 1):
        def recurse(index: int, remaining: int, prefix: list[int]) -> None:
            if index == dimension - 1:
                result.append(tuple(prefix + [remaining]))
                return
            for count in range(remaining + 1):
                recurse(index + 1, remaining - count, prefix + [count])
        recurse(0, total, [])
    return tuple(result)


def full_material_future_signature(
    clearance: tuple[int, ...] | list[int],
    collapse_factor: int,
    response_samples: tuple[int, ...] | list[int],
    horizon: int,
) -> tuple[int, ...]:
    """Independent full-state material future used as a differential oracle."""
    samples = _validated_response_samples(response_samples)
    state = tuple(clearance)
    if not state:
        raise ValueError("clearance state must be nonempty")
    if not any(state) or any(value >= collapse_factor for value in state):
        raise ValueError("oracle requires one positive inside clearance state")
    depth = collapse_factor - max(state)
    if depth >= len(samples):
        raise ValueError("oracle requires a represented material depth")

    outputs = []
    for actions in _action_count_vectors(len(state), horizon):
        post = tuple(
            value + count for value, count in zip(state, actions, strict=True)
        )
        if any(value >= collapse_factor for value in post):
            residual_depth = 0
        else:
            residual_depth = collapse_factor - max(post)
        outputs.append(samples[residual_depth])
    return tuple(outputs)


def material_future_class_count(
    dimension: int,
    collapse_factor: int,
    response_samples: tuple[int, ...] | list[int],
    horizon: int,
) -> int:
    """Return exact named-axis classes over represented positive clearance states.

    Depths sharing the same response word merge.  At one response word W, let
    q_max be the largest q=d-k among depths producing W.  The union of allowed
    capped-deficit vectors is exactly the positive cap box at
    ``m=min(H_R(W),q_max)``.
    """
    _require_positive("dimension", dimension)
    _require_positive("collapse_factor", collapse_factor)
    _require_nonnegative("horizon", horizon)
    samples = _validated_response_samples(response_samples)
    max_depth = min(len(samples) - 1, collapse_factor - 1)
    by_word: dict[tuple[int, ...], tuple[int, int]] = {}
    for depth in range(1, max_depth + 1):
        word = material_response_word(samples, depth, horizon)
        cap = material_visible_deficit_cap(word)
        q = collapse_factor - depth
        if word in by_word:
            old_cap, old_q = by_word[word]
            if old_cap != cap:
                raise AssertionError("identical response word changed its visible cap")
            by_word[word] = (cap, max(old_q, q))
        else:
            by_word[word] = (cap, q)

    total = 0
    for cap, q_max in by_word.values():
        m = min(cap, q_max)
        total += (m + 1) ** dimension - m**dimension
    return total


def permutation_symmetric_material_future_class_count(
    dimension: int,
    collapse_factor: int,
    response_samples: tuple[int, ...] | list[int],
    horizon: int,
) -> int:
    """Exact material-future classes after full coordinate-permutation quotient."""
    _require_positive("dimension", dimension)
    _require_positive("collapse_factor", collapse_factor)
    _require_nonnegative("horizon", horizon)
    samples = _validated_response_samples(response_samples)
    max_depth = min(len(samples) - 1, collapse_factor - 1)
    by_word: dict[tuple[int, ...], tuple[int, int]] = {}
    for depth in range(1, max_depth + 1):
        word = material_response_word(samples, depth, horizon)
        cap = material_visible_deficit_cap(word)
        q = collapse_factor - depth
        previous = by_word.get(word)
        by_word[word] = (cap, q if previous is None else max(previous[1], q))

    return sum(
        comb(dimension + min(cap, q_max) - 1, min(cap, q_max))
        for cap, q_max in by_word.values()
    )
