#!/usr/bin/env python3
"""Exact checker for the native filament chiral double cover and arithmetic glue."""

from __future__ import annotations

from itertools import combinations


def epsilon(j: int) -> int:
    return j & 1


def eta(j: int, chi: int) -> int:
    num = 3 * j * j + chi * epsilon(j)
    assert num % 2 == 0
    return num // 2


def word(k: int, q: int, chi: int, a: int, b: int) -> tuple[int, ...]:
    return tuple((a + b * j + eta(j, chi)) % q for j in range(k))


def packet(k: int, r: int, c: int) -> tuple[int, ...]:
    chi = 1 if r % 2 == 0 else -1
    return tuple(c + 3 * r * j + eta(j, chi) for j in range(k))


def numerator(i: int, j: int, vi: int, vj: int, s: int) -> int:
    return (
        2 * (vj - vi)
        - 3 * (j * j - i * i)
        - s * (epsilon(j) - epsilon(i))
    )


def decode_two(i: int, j: int, vi: int, vj: int):
    assert i < j
    d = j - i
    out = []
    for s in (1, -1):
        q_s = numerator(i, j, vi, vj, s)
        den = 6 * d
        if q_s % den:
            continue
        r = q_s // den
        if s != (1 if r % 2 == 0 else -1):
            continue
        c = vi - 3 * r * i - eta(i, s)
        out.append((s, r, c))
    return out


def check_access_structure(k: int, q: int) -> None:
    words = {
        (chi, a, b): word(k, q, chi, a, b)
        for chi in (1, -1)
        for a in range(q)
        for b in range(q)
    }
    assert len(set(words.values())) == 2 * q * q

    for size in range(1, k + 1):
        for positions in combinations(range(k), size):
            seen = {}
            collision = False
            for key, w in words.items():
                projection = tuple(w[j] for j in positions)
                if projection in seen and seen[projection] != key:
                    collision = True
                    break
                seen[projection] = key

            authorized = (
                size >= 3
                and any(j % 2 == 0 for j in positions)
                and any(j % 2 == 1 for j in positions)
            )
            assert collision == (not authorized), (k, q, positions)

    # Every two-coordinate projection is uniform and mode-blind.
    for i, j in combinations(range(k), 2):
        images = []
        for chi in (1, -1):
            counts = {}
            for a in range(q):
                for b in range(q):
                    projection = (
                        word(k, q, chi, a, b)[i],
                        word(k, q, chi, a, b)[j],
                    )
                    counts[projection] = counts.get(projection, 0) + 1
            assert len(counts) == q * q
            assert set(counts.values()) == {1}
            images.append(counts)
        assert images[0] == images[1]

    # Explicit parity-bridge syndrome.
    for chi in (1, -1):
        for a in range(q):
            for b in range(q):
                v = word(k, q, chi, a, b)
                y = [(2 * v[j] - 3 * j * j) % q for j in range(k)]
                for u, vv in combinations(range(k), 2):
                    if epsilon(u) != epsilon(vv):
                        continue
                    for w in range(k):
                        if epsilon(w) == epsilon(u):
                            continue
                        omega = (
                            (vv - u) * y[w]
                            + (w - vv) * y[u]
                            - (w - u) * y[vv]
                        ) % q
                        recovered = (
                            (1 if epsilon(u) == 0 else -1)
                            * omega
                            * pow(vv - u, -1, q)
                        ) % q
                        assert recovered == chi % q


def check_probe_channel_dichotomy() -> None:
    # Replay many integer packets and all two-probe positions.
    for k in range(3, 10):
        for r in range(-40, 41):
            chi = 1 if r % 2 == 0 else -1
            vals = packet(k, r, 10_000 + 17 * r)
            for i, j in combinations(range(k), 2):
                d = j - i
                nums = {s: numerator(i, j, vals[i], vals[j], s) for s in (1, -1)}
                assert nums[-chi] - nums[chi] in (-2, 2)

                if epsilon(i) == epsilon(j):
                    # The offset vanishes; only the parity lock distinguishes sheets.
                    assert nums[1] == nums[-1]
                    common_r = nums[chi] // (6 * d)
                    assert common_r == r
                    assert (1 if common_r % 2 == 0 else -1) == chi
                elif d == 1:
                    # Both pre-slopes are integral; exactly one is a multiple of 3.
                    slopes = {s: nums[s] // (2 * d) for s in (1, -1)}
                    assert all(nums[s] % (2 * d) == 0 for s in (1, -1))
                    assert slopes[chi] == 3 * r
                    assert slopes[chi] % 3 == 0
                    assert slopes[-chi] % 3 != 0
                else:
                    # Opposite parity implies odd d; the false pre-slope is nonintegral.
                    assert d % 2 == 1 and d > 1
                    assert nums[chi] % (2 * d) == 0
                    assert nums[-chi] % (2 * d) != 0


def check_integer_glue() -> None:
    for k in range(3, 10):
        for r in range(-40, 41):
            c = 10_000 + 17 * r
            vals = packet(k, r, c)
            expected = (1 if r % 2 == 0 else -1, r, c)
            for i, j in combinations(range(k), 2):
                assert decode_two(i, j, vals[i], vals[j]) == [expected], (
                    k, r, c, i, j
                )

    # Frozen sharp-nine Cell windows.  These starts are two shells earlier than
    # the corresponding five-flower-window starts.
    even_packet = (
        171283421, 171315481, 171347543, 171379609, 171411677,
        171443749, 171475823, 171507901, 171539981,
    )
    odd_packet = (
        17434825207, 17435148641, 17435472079, 17435795519,
        17436118963, 17436442409, 17436765859, 17437089311,
        17437412767,
    )

    for vals, r in ((even_packet, 10686), (odd_packet, 107811)):
        expected_chi = 1 if r % 2 == 0 else -1
        decoded_sequences = set()
        for i, j in combinations(range(9), 2):
            out = decode_two(i, j, vals[i], vals[j])
            assert len(out) == 1
            chi, recovered_r, c = out[0]
            assert chi == expected_chi and recovered_r == r
            regenerated = packet(9, recovered_r, c)
            assert regenerated == vals
            decoded_sequences.add(regenerated)
        assert len(decoded_sequences) == 1


def main() -> None:
    for k, q in (
        (3, 5), (4, 7), (5, 7), (6, 7),
        (7, 11), (8, 11), (9, 11),
    ):
        check_access_structure(k, q)
    check_probe_channel_dichotomy()
    check_integer_glue()

    print("CHIRAL_DOUBLE_COVER_SIZE=2*q^2")
    print("ACCESS_IFF=MIXED_PARITY_AND_AT_LEAST_3")
    print("EVERY_TWO_PROBE_PROJECTION=PERFECTLY_MODE_BLIND")
    print("PARITY_BRIDGE_SYNDROME=PASS")
    print("SAME_PARITY_SELECTOR=CHANNEL2")
    print("NONADJACENT_PARITY_BRIDGE_SELECTOR=INDEX_DISTANCE")
    print("ADJACENT_PARITY_BRIDGE_SELECTOR=CHANNEL3")
    print("ANY_TWO_INDEXED_INTEGER_VALUES=UNIQUE_NATIVE_DECODER")
    print("SHARP9_ALL_PAIR_DECODERS=PASS")


if __name__ == "__main__":
    main()
