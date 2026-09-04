"""Task-local checker for hidden-fiber capacity forced by repeated AGM diamonds.

At block time m, every branch history reaches the same recoalesced carrier
terminal.  For every positive d<=m with d congruent to m mod 2, the word

    A^((m+d)/2) B^((m-d)/2)

has no earlier balanced prefix and ends with imbalance +d.  Swapping A/B gives
-d.  Hence any exact hidden lift over the same (carrier terminal,time=m) needs
at least ceil(m/2) unlabeled predictive states and twice that many
branch-resolved states.
"""

from __future__ import annotations


def imbalance(word: str) -> int:
    return word.count("A") - word.count("B")


def is_alive(word: str) -> bool:
    z = 0
    for letter in word:
        z += 1 if letter == "A" else -1
        if z == 0:
            return False
    return True


def positive_witness(m: int, d: int) -> str:
    if m < 1 or d < 1 or d > m or (m - d) % 2:
        raise ValueError("d must be a positive parity-compatible imbalance")
    a = (m + d) // 2
    b = (m - d) // 2
    return "A" * a + "B" * b


def run() -> dict[str, object]:
    max_time = 256
    total_witnesses = 0
    for m in range(1, max_time + 1):
        positive_ds = list(range(1 if m % 2 else 2, m + 1, 2))
        if len(positive_ds) != (m + 1) // 2:
            raise AssertionError("unlabeled capacity count mismatch")

        signed_states: set[int] = set()
        for d in positive_ds:
            word = positive_witness(m, d)
            if len(word) != m or not is_alive(word) or imbalance(word) != d:
                raise AssertionError(f"positive witness failed at m={m}, d={d}")
            swapped = word.translate(str.maketrans({"A": "B", "B": "A"}))
            if not is_alive(swapped) or imbalance(swapped) != -d:
                raise AssertionError(f"negative witness failed at m={m}, d={d}")
            signed_states.add(d)
            signed_states.add(-d)
            total_witnesses += 2

        if len(signed_states) != 2 * ((m + 1) // 2):
            raise AssertionError("branch-resolved capacity count mismatch")

    return {
        "times_checked": max_time,
        "last_unlabeled_capacity_lower_bound": (max_time + 1) // 2,
        "last_resolved_capacity_lower_bound": 2 * ((max_time + 1) // 2),
        "explicit_alive_witnesses_checked": total_witnesses,
    }


if __name__ == "__main__":
    result = run()
    expected = {
        "times_checked": 256,
        "last_unlabeled_capacity_lower_bound": 128,
        "last_resolved_capacity_lower_bound": 256,
        "explicit_alive_witnesses_checked": 33024,
    }
    if result != expected:
        raise SystemExit(f"unexpected hidden-fiber capacity output: {result!r}")
    for key, value in result.items():
        print(f"{key}={value}")
