"""Task-local predictive-state checker for the post-#1161 first-return successor.

The observer is the exact first-balance-return count by future length.  The full
history of a still-alive two-letter word compresses to the absolute multiplicity
imbalance d=|#A-#B|.  Exact all-horizon prediction needs unbounded d, while a
future horizon h has exactly h+2 predictive classes: d=0, d=1,...,d=h, and one
far class d>h.

No floating point, pi, square roots, or external packages are used.
"""

from __future__ import annotations

from math import comb


def first_hit_count(distance: int, steps: int) -> int:
    """Number of +/-1 walks from positive distance to first hit zero at `steps`.

    State 0 is terminal: its length-zero observation is 1 and it has no later
    first-hit event.  For d>0 the classical ballot/reflection count is

        d/steps * C(steps, (steps-d)/2)

    when parity and range permit it.
    """
    if distance < 0 or steps < 0:
        raise ValueError("distance and steps must be nonnegative")
    if distance == 0:
        return int(steps == 0)
    if steps == 0 or steps < distance or (steps - distance) % 2:
        return 0
    down_extra = (steps - distance) // 2
    numerator = distance * comb(steps, down_extra)
    if numerator % steps:
        raise AssertionError("ballot count lost integrality")
    return numerator // steps


def predictive_signature(distance: int, horizon: int) -> tuple[int, ...]:
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    return tuple(first_hit_count(distance, steps) for steps in range(horizon + 1))


def first_return_word_count(n: int) -> int:
    """First balance from zero at length 2n, including either first letter."""
    if n < 1:
        raise ValueError("n must be positive")
    return 2 * first_hit_count(1, 2 * n - 1)


def run() -> dict[str, object]:
    # First-return shell agreement with the Catalan formula.
    shell_counts: list[int] = []
    for n in range(1, 65):
        value = first_return_word_count(n)
        catalan = comb(2 * (n - 1), n - 1) // n
        if value != 2 * catalan:
            raise AssertionError(f"first-return/Catalan mismatch at n={n}")
        shell_counts.append(value)

    # Finite-horizon minimal predictive quotient: h+2 classes.
    horizon_class_counts: list[int] = []
    for horizon in range(0, 33):
        # Include several states beyond the horizon to test the common far class.
        signatures = {
            distance: predictive_signature(distance, horizon)
            for distance in range(0, 2 * horizon + 6)
        }
        class_count = len(set(signatures.values()))
        expected = horizon + 2
        if class_count != expected:
            raise AssertionError(
                f"horizon {horizon}: expected {expected} classes, got {class_count}"
            )

        far_signature = predictive_signature(horizon + 1, horizon)
        for distance in range(horizon + 1, 2 * horizon + 6):
            if signatures[distance] != far_signature:
                raise AssertionError("states beyond horizon did not collapse to one far class")

        # d=0..h must be pairwise distinct; earliest nonzero return time identifies d.
        near = [signatures[d] for d in range(horizon + 1)]
        if len(set(near)) != horizon + 1:
            raise AssertionError("near predictive states were incorrectly merged")
        horizon_class_counts.append(class_count)

    # All-horizon fixed-finite-state no-go witness: the first 64 distances are
    # pairwise distinguishable already by horizons up to their larger value.
    for left in range(1, 65):
        for right in range(left + 1, 65):
            horizon = right
            if predictive_signature(left, horizon) == predictive_signature(right, horizon):
                raise AssertionError("distinct counter values were not predictively separated")

    # Explicit same-time/same-terminal-history collision used in the G0 argument.
    # AAAA and AAAB are both still alive after four recoalesced diamond blocks,
    # but their absolute imbalances are 4 and 2, so earliest future return differs.
    witness = {
        "history_left": "AAAA",
        "history_right": "AAAB",
        "same_block_time": 4,
        "left_imbalance": 4,
        "right_imbalance": 2,
        "left_earliest_future_return": 4,
        "right_earliest_future_return": 2,
    }
    if first_hit_count(4, 2) != 0 or first_hit_count(2, 2) != 1:
        raise AssertionError("explicit G0 collision witness lost distinguishing future")

    return {
        "first_return_shells_checked": 64,
        "first_eight_shell_counts": shell_counts[:8],
        "finite_horizons_checked": 33,
        "horizon_class_counts_h0_to_h8": horizon_class_counts[:9],
        "pairwise_counter_states_checked": 64,
        "g0_collision_witness": witness,
    }


if __name__ == "__main__":
    result = run()
    expected = {
        "first_return_shells_checked": 64,
        "first_eight_shell_counts": [2, 2, 4, 10, 28, 84, 264, 858],
        "finite_horizons_checked": 33,
        "horizon_class_counts_h0_to_h8": [2, 3, 4, 5, 6, 7, 8, 9, 10],
        "pairwise_counter_states_checked": 64,
        "g0_collision_witness": {
            "history_left": "AAAA",
            "history_right": "AAAB",
            "same_block_time": 4,
            "left_imbalance": 4,
            "right_imbalance": 2,
            "left_earliest_future_return": 4,
            "right_earliest_future_return": 2,
        },
    }
    if result != expected:
        raise SystemExit(f"unexpected predictive-counter output: {result!r}")
    for key, value in result.items():
        print(f"{key}={value}")
