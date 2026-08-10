"""Exact two-stage normalization of a finite precision task schedule.

A sequential schedule assigns each state one local repair digit at each stage.
The declared stage radices are the maximum local branching factors.  The full
digit product can be packed bijectively into one mixed-radix code, eliminating
per-stage base-symbol ceiling overhead.  Only a subset of product codes may be
realized; ranking that subset yields the exact final joint quotient code and
eliminates incidence-capacity overhead.
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable, Mapping, Sequence

from .precision_incidence_geometry import integer_symbol_depth
from .precision_task_scheduling import order_profile

State = Hashable
Partition = Mapping[State, Hashable]


def _domain(states: Iterable[State]) -> tuple[State, ...]:
    domain = tuple(states)
    if not domain:
        raise ValueError("state domain must be nonempty")
    if len(domain) != len(set(domain)):
        raise ValueError("state domain must contain distinct states")
    return domain


def _validate_tasks(
    states: tuple[State, ...], tasks: Mapping[str, Partition], order: Sequence[str]
) -> dict[str, Partition]:
    family = dict(tasks)
    if not family:
        raise ValueError("at least one task partition is required")
    if len(order) != len(family) or set(order) != set(family):
        raise ValueError("order must contain every task name exactly once")
    state_set = set(states)
    for partition in family.values():
        if set(partition) != state_set:
            raise ValueError("every task partition must cover the state domain exactly")
    return family


def schedule_local_digits(
    states: Iterable[State], tasks: Mapping[str, Partition], order: Sequence[str]
) -> dict[str, object]:
    """Construct deterministic local repair digits for one task order.

    Within each current context block, realized labels of the next task are
    numbered by first occurrence in domain order.  The same digit alphabet is
    reused across different context blocks, exactly as in the P023 minimum
    repair theorem.
    """

    domain = _domain(states)
    family = _validate_tasks(domain, tasks, order)
    context = {state: () for state in domain}
    words: dict[State, list[int]] = {state: [] for state in domain}
    radices: list[int] = []

    for name in order:
        task = family[name]
        label_codes_by_context: dict[tuple[Hashable, ...], dict[Hashable, int]] = {}
        stage_digits: dict[State, int] = {}
        maximum = 1
        for state in domain:
            parent = context[state]
            codes = label_codes_by_context.setdefault(parent, {})
            label = task[state]
            if label not in codes:
                codes[label] = len(codes)
            stage_digits[state] = codes[label]
            maximum = max(maximum, len(codes))
        radices.append(maximum)
        for state in domain:
            digit = stage_digits[state]
            if digit >= maximum:
                raise AssertionError("local repair digit escaped declared stage radix")
            words[state].append(digit)
            context[state] = (*context[state], digit)

    frozen_words = {state: tuple(words[state]) for state in domain}
    final_class_count = len(set(frozen_words.values()))
    expected = int(order_profile(domain, family, order)["final_joint_class_count"])
    if final_class_count != expected:
        raise AssertionError("local repair words do not represent exact final joint classes")

    return {
        "order": tuple(order),
        "radices": tuple(radices),
        "digit_words": frozen_words,
        "final_joint_class_count": final_class_count,
    }


def mixed_radix_pack(digits: Sequence[int], radices: Sequence[int]) -> int:
    """Bijectively pack a full mixed-radix digit word into ``[0, product)``."""

    if len(digits) != len(radices) or not radices:
        raise ValueError("digits and nonempty radices must have the same length")
    value = 0
    for digit, radix in zip(digits, radices, strict=True):
        if isinstance(radix, bool) or not isinstance(radix, int) or radix < 1:
            raise ValueError("radices must be positive integers")
        if isinstance(digit, bool) or not isinstance(digit, int) or not 0 <= digit < radix:
            raise ValueError("each digit must lie in its declared radix")
        value = value * radix + digit
    return value


def mixed_radix_unpack(value: int, radices: Sequence[int]) -> tuple[int, ...]:
    """Inverse of ``mixed_radix_pack`` on the complete product alphabet."""

    if not radices:
        raise ValueError("radices must be nonempty")
    product = 1
    for radix in radices:
        if isinstance(radix, bool) or not isinstance(radix, int) or radix < 1:
            raise ValueError("radices must be positive integers")
        product *= radix
    if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value < product:
        raise ValueError("packed value lies outside product radix")
    digits = [0] * len(radices)
    remaining = value
    for index in range(len(radices) - 1, -1, -1):
        radix = radices[index]
        digits[index] = remaining % radix
        remaining //= radix
    if remaining != 0:
        raise AssertionError("mixed-radix unpack left a nonzero quotient")
    return tuple(digits)


def normalized_schedule_codes(
    states: Iterable[State],
    tasks: Mapping[str, Partition],
    order: Sequence[str],
    base: int = 2,
) -> dict[str, object]:
    """Return separate, packed-product, and realized-rank schedule encodings."""

    domain = _domain(states)
    data = schedule_local_digits(domain, tasks, order)
    radices = tuple(data["radices"])
    words = dict(data["digit_words"])

    product_capacity = 1
    separate_depth = 0
    for radix in radices:
        product_capacity *= radix
        separate_depth += integer_symbol_depth(radix, base)
    product_depth = integer_symbol_depth(product_capacity, base)

    packed = {state: mixed_radix_pack(words[state], radices) for state in domain}
    for state in domain:
        if mixed_radix_unpack(packed[state], radices) != words[state]:
            raise AssertionError("mixed-radix pack/unpack failed")

    realized_codes = tuple(sorted(set(packed.values())))
    rank = {code: index for index, code in enumerate(realized_codes)}
    ranked = {state: rank[packed[state]] for state in domain}
    realized_count = len(realized_codes)
    final_count = int(data["final_joint_class_count"])
    if realized_count != final_count:
        raise AssertionError("packed realized support changed final class count")

    joint_depth = integer_symbol_depth(realized_count, base)
    radix_slack = separate_depth - product_depth
    incidence_slack = product_depth - joint_depth
    if radix_slack < 0 or incidence_slack < 0:
        raise AssertionError("normalization slacks must be nonnegative")

    return {
        **data,
        "product_capacity": product_capacity,
        "separate_stage_depth": separate_depth,
        "product_depth": product_depth,
        "realized_joint_depth": joint_depth,
        "radix_slack_removed_by_packing": radix_slack,
        "incidence_slack_removed_by_realized_ranking": incidence_slack,
        "packed_codes": packed,
        "realized_packed_codes": realized_codes,
        "ranked_joint_codes": ranked,
    }
