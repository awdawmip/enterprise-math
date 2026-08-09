"""P011-style collapse from stacking signs to local FCC/HCP context bits.

For a sign word delta_0,...,delta_(L-1), define context bits

    chi_i = 1[delta_(i-1) != delta_i],  i=1..L-1.

The context word determines the whole sign trajectory once the initial sign is
chosen.  Hence every context-word fiber contains exactly two sign words related
by global sign reversal.  The collapse therefore forgets exactly one global
orientation/chirality bit:

    2^L raw sign words -> 2^(L-1) context words,
    every fiber size = 2.

Its canonical finite collision spectrum is J_1=2^L, J_2=2^(L-1), J_k=0 for
k>=3.  Whether the global sign bit may be deleted in a physical model remains a
future-language question.
"""

from __future__ import annotations

from collections import Counter
from itertools import product
from math import comb


def _validate_signs(signs: tuple[int, ...]) -> None:
    if not isinstance(signs, tuple) or not signs:
        raise ValueError("sign word must be a non-empty tuple")
    if any(sign not in (-1, 1) for sign in signs):
        raise ValueError("sign word entries must be +/-1")


def context_word(signs: tuple[int, ...]) -> tuple[int, ...]:
    _validate_signs(signs)
    return tuple(int(left != right) for left, right in zip(signs, signs[1:]))


def reconstruct_signs(context: tuple[int, ...], initial_sign: int) -> tuple[int, ...]:
    if initial_sign not in (-1, 1):
        raise ValueError("initial sign must be +/-1")
    if any(bit not in (0, 1) for bit in context):
        raise ValueError("context bits must be 0/1")
    signs = [initial_sign]
    for bit in context:
        signs.append(signs[-1] if bit == 0 else -signs[-1])
    return tuple(signs)


def context_fiber(context: tuple[int, ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    positive = reconstruct_signs(context, 1)
    negative = reconstruct_signs(context, -1)
    return positive, negative


def global_sign_reverse(signs: tuple[int, ...]) -> tuple[int, ...]:
    _validate_signs(signs)
    return tuple(-sign for sign in signs)


def every_context_fiber_has_size_two(length: int) -> bool:
    if isinstance(length, bool) or not isinstance(length, int) or length <= 0:
        raise ValueError("length must be positive")
    counts = Counter(
        context_word(tuple(signs))
        for signs in product((-1, 1), repeat=length)
    )
    return len(counts) == (1 << max(0, length - 1)) and set(counts.values()) == {2}


def stacking_context_collision_spectrum(
    length: int,
    maximum_order: int | None = None,
) -> tuple[int, ...]:
    if isinstance(length, bool) or not isinstance(length, int) or length <= 0:
        raise ValueError("length must be positive")
    limit = (1 << length) if maximum_order is None else maximum_order
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
        raise ValueError("maximum_order must be positive")
    fiber_count = 1 << max(0, length - 1)
    return tuple(
        fiber_count * comb(2, order) if order <= 2 else 0
        for order in range(1, limit + 1)
    )


def context_observation_forgets_only_global_sign(signs: tuple[int, ...]) -> bool:
    context = context_word(signs)
    fiber = set(context_fiber(context))
    return fiber == {signs, global_sign_reverse(signs)}
