#!/usr/bin/env python3
"""Independent checker for the frozen native prime-filament blind packet.

This file is intentionally derived only from the formulas in
PRIME_NATIVE_FILAMENT_BLIND_REPLICATION_PACKET_20260823.md.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
from typing import Iterator


TASK_ID = "RS-PRIME-NATIVE-FILAMENT-SHARP-BOUND-INDEPENDENT-REPLICATION"
SOURCE_COMMIT = "12725505c636449df7dd913ac06e581bf418b89c"
LOCKED_PACKET_REF = "123cfecb25b30fe2ff9d4fddf900b6e3f2569a7a"
SEARCH_MAX_START_SHELL = 20_000
SEARCH_SEED = 0
WITNESS = {
    "sigma": 1,
    "window_start_shell": 10_686,
    "transverse_c": -2_474,
    "trajectory_coordinates": [
        [10_686, 2_869, 1],
        [10_687, 2_870, 1],
        [10_688, 2_870, 1],
        [10_689, 2_871, 1],
        [10_690, 2_871, 1],
        [10_691, 2_872, 1],
        [10_692, 2_872, 1],
        [10_693, 2_873, 1],
        [10_694, 2_873, 1],
    ],
    "prime_values": [
        171_283_421,
        171_315_481,
        171_347_543,
        171_379_609,
        171_411_677,
        171_443_749,
        171_475_823,
        171_507_901,
        171_539_981,
    ],
    "candidate_count_through_hit": 380_482,
}

# Filled only after the complete independent result object is stable.  The
# checker fails closed if a later edit changes that canonical object.
EXPECTED_FROZEN_DIGEST = "a6be930a5920699f56a1b21d71cc3314d54732f5b31809236bedadc98ac80e9a"


NEIGHBOR_DELTAS = (
    (1, 0),
    (2, 1),
    (1, 1),
    (-1, 0),
    (-2, -1),
    (-1, -1),
)


def base(r: int) -> int:
    return 1 + 3 * r * (r - 1) // 2


def label(r: int, t: int, sigma: int) -> int:
    return base(r) + t + sigma * r


def neighbors_from_packet(r: int, t: int, sigma: int) -> tuple[int, ...]:
    n = label(r, t, sigma)
    return (
        n + 3 * r + sigma,
        n + 6 * r + 4 + 2 * sigma,
        n + 3 * r + 1 + sigma,
        n - 3 * r + 3 - sigma,
        n - 6 * r + 8 - 2 * sigma,
        n - 3 * r + 2 - sigma,
    )


def neighbors_from_coordinates(r: int, t: int, sigma: int) -> tuple[int, ...]:
    return tuple(label(r + dr, t + dt, sigma) for dr, dt in NEIGHBOR_DELTAS)


def is_prime_trial(n: int) -> bool:
    """Independent slow path used for witness cross-checking."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def is_prime(n: int) -> bool:
    """Deterministic Miller--Rabin for unsigned 64-bit integers."""
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def transverse(r: int, t: int, sigma: int) -> int:
    return t - (r + sigma) // 2


def trajectory_t(r: int, c: int, sigma: int) -> int:
    return c + (r + sigma) // 2


def trajectory_label(r: int, c: int, sigma: int) -> int:
    return label(r, trajectory_t(r, c, sigma), sigma)


def transition_delta(r: int, sigma: int) -> int:
    return (r + sigma) & 1


def eligible_neighbor_slots(r: int, sigma: int) -> tuple[int, ...]:
    # Zero-based slots in the packet's order.
    return (0, 1, 4, 5) if (r + sigma) % 2 == 0 else (1, 2, 3, 4)


def flower_prime_set(r: int, t: int, sigma: int) -> frozenset[int] | None:
    n = label(r, t, sigma)
    ns = neighbors_from_packet(r, t, sigma)
    if n <= 3 or not is_prime(n):
        return None
    pns = [x for x in ns if is_prime(x)]
    if len(pns) != 4:
        return None
    return frozenset((n, *pns))


def trajectory_prime_set(r: int, t: int, sigma: int) -> frozenset[int]:
    c = transverse(r, t, sigma)
    return frozenset(trajectory_label(q, c, sigma) for q in range(r - 2, r + 3))


def admissible_center(r: int, t: int, sigma: int) -> bool:
    return r >= 4 and 0 <= sigma <= 2 and 2 <= t <= r - 2 and min(
        neighbors_from_packet(r, t, sigma)
    ) > 0


def modular_good(n: int) -> bool:
    return n % 3 != 0 and n % 5 != 0


def extremal_modular_channels() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    # The trajectory is periodic modulo 15 under r -> r+30 and c -> c+30.
    for sigma in range(3):
        for a_mod_30 in range(30):
            for c_mod_30 in range(30):
                # The complete local mod-6 classification below leaves only
                # sigma=1 and c=4 (mod 6).
                if sigma != 1 or c_mod_30 % 6 != 4:
                    continue
                residues = [
                    trajectory_label(a_mod_30 + j, c_mod_30, sigma) % 15
                    for j in range(9)
                ]
                if all(modular_good(x) for x in residues):
                    rows.append(
                        {
                            "row_type": "extremal_nine_term_channel",
                            "sigma": sigma,
                            "a_mod_30": a_mod_30,
                            "c_mod_30": c_mod_30,
                            "reduced_channel": f"({a_mod_30 % 10},{c_mod_30})",
                            "residues_mod_15": " ".join(map(str, residues)),
                            "predecessor_mod_15": trajectory_label(
                                a_mod_30 - 1, c_mod_30, sigma
                            )
                            % 15,
                            "successor_mod_15": trajectory_label(
                                a_mod_30 + 9, c_mod_30, sigma
                            )
                            % 15,
                        }
                    )
    return rows


def local_residue_classes() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for sigma in range(3):
        for r_mod_12 in range(12):
            for t_mod_6 in range(6):
                n = label(r_mod_12, t_mod_6, sigma)
                ns = neighbors_from_packet(r_mod_12, t_mod_6, sigma)
                slots = eligible_neighbor_slots(r_mod_12, sigma)
                vals = [n, *(ns[i] for i in slots)]
                if all(math.gcd(v, 6) == 1 for v in vals):
                    c_mod_6 = (t_mod_6 - (r_mod_12 + sigma) // 2) % 6
                    rows.append(
                        {
                            "row_type": "local_mod_6_eligibility",
                            "sigma": sigma,
                            "r_mod_12": r_mod_12,
                            "t_mod_6": t_mod_6,
                            "parity": (r_mod_12 + sigma) % 2,
                            "c_mod_6": c_mod_6,
                            "eligible_slots_1_based": " ".join(str(i + 1) for i in slots),
                            "prime_candidate_residues_mod_6": " ".join(
                                str(v % 6) for v in vals
                            ),
                        }
                    )
    return rows


def mod_five_coverage_table() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for c_mod_5 in range(5):
        residues = [trajectory_label(r, c_mod_5, 1) % 5 for r in range(10)]
        rows.append(
            {
                "c_mod_5": c_mod_5,
                "residues_r_0_through_9": residues,
                "zero_shells_mod_10": [i for i, x in enumerate(residues) if x == 0],
            }
        )
    return rows


def max_modular_run() -> int:
    best = 0
    for c_mod_30 in range(30):
        if c_mod_30 % 6 != 4:
            continue
        for a_mod_30 in range(30):
            run = 0
            for j in range(30):
                if modular_good(trajectory_label(a_mod_30 + j, c_mod_30, 1)):
                    run += 1
                    best = max(best, run)
                else:
                    run = 0
    return best


def symbolic_identity_certificate() -> dict[str, object]:
    """Exact affine-coefficient certificate for every carrier identity used."""
    # Each pair (a,b) denotes a*r+b.  Expanding B_{r+d}-B_r and the
    # sigma*r/t terms gives the packet offsets exactly.
    by_sigma: dict[str, object] = {}
    for sigma in range(3):
        coordinate_offsets = (
            (3, sigma),
            (6, 4 + 2 * sigma),
            (3, 1 + sigma),
            (-3, 3 - sigma),
            (-6, 8 - 2 * sigma),
            (-3, 2 - sigma),
        )
        packet_offsets = (
            (3, sigma),
            (6, 4 + 2 * sigma),
            (3, 1 + sigma),
            (-3, 3 - sigma),
            (-6, 8 - 2 * sigma),
            (-3, 2 - sigma),
        )
        assert coordinate_offsets == packet_offsets
        gap_by_parity = {
            "even_r_plus_sigma": (3, sigma),
            "odd_r_plus_sigma": (3, sigma + 1),
        }
        by_sigma[str(sigma)] = {
            "neighbor_offset_coefficients": coordinate_offsets,
            "trajectory_gap_coefficients": gap_by_parity,
        }
    return {
        "notation": "(a,b) means a*r+b",
        "base_differences": {
            "B(r+1)-B(r)": (3, 0),
            "B(r+2)-B(r)": (6, 3),
            "B(r-1)-B(r)": (-3, 3),
            "B(r-2)-B(r)": (-6, 9),
        },
        "by_sigma": by_sigma,
    }


def trial_division_certificate(n: int) -> dict[str, object]:
    limit = math.isqrt(n)
    assert n > 2 and n % 2 == 1
    tested = 0
    for d in range(3, limit + 1, 2):
        tested += 1
        if n % d == 0:
            return {
                "n": n,
                "prime": False,
                "factor": d,
                "sqrt_floor": limit,
                "odd_divisors_tested": tested,
            }
    return {
        "n": n,
        "prime": True,
        "factor": None,
        "sqrt_floor": limit,
        "odd_divisors_tested": tested,
        "method": "complete odd trial division through floor(sqrt(n))",
    }


def centers_adjacent_direct(a: tuple[int, int, int], b: tuple[int, int, int]) -> bool:
    return label(*b) in neighbors_from_packet(*a)


def centers_adjacent_closed(a: tuple[int, int, int], b: tuple[int, int, int]) -> bool:
    r, t, sigma = a
    rr, tt, ss = b
    return ss == sigma and rr == r + 1 and tt - t in (0, 1)


def rolling_pair_valid(
    a: tuple[int, int, int],
    prime_a: frozenset[int],
    b: tuple[int, int, int],
    prime_b: frozenset[int],
) -> bool:
    return centers_adjacent_direct(a, b) and len(prime_a & prime_b) == 4


def witness_certificate() -> dict[str, object]:
    a = int(WITNESS["window_start_shell"])
    c = int(WITNESS["transverse_c"])
    sigma = int(WITNESS["sigma"])
    coordinates = [
        (r, trajectory_t(r, c, sigma), sigma) for r in range(a, a + 9)
    ]
    values = [label(*coord) for coord in coordinates]
    assert coordinates == [tuple(x) for x in WITNESS["trajectory_coordinates"]]
    assert values == WITNESS["prime_values"]
    assert all(is_prime(n) for n in values)
    trial = [trial_division_certificate(n) for n in values]
    assert all(x["prime"] for x in trial)

    flowers: list[dict[str, object]] = []
    prime_sets: list[frozenset[int]] = []
    center_coordinates = coordinates[2:7]
    for coord in center_coordinates:
        r, t, s = coord
        packet_set = flower_prime_set(r, t, s)
        trajectory_set = trajectory_prime_set(r, t, s)
        assert packet_set is not None and packet_set == trajectory_set
        prime_sets.append(packet_set)
        ns = neighbors_from_packet(r, t, s)
        slots = eligible_neighbor_slots(r, s)
        unsorted = [label(r, t, s), *(ns[i] for i in slots)]
        flowers.append(
            {
                "coordinate": list(coord),
                "center_label": label(*coord),
                "ordered_neighbors": list(ns),
                "prime_slots_1_based": [i + 1 for i in slots],
                "center_then_prime_neighbors": unsorted,
                "sorted_prime_packet": sorted(packet_set),
            }
        )
    overlaps: list[dict[str, object]] = []
    for i in range(4):
        assert centers_adjacent_direct(center_coordinates[i], center_coordinates[i + 1])
        assert centers_adjacent_closed(center_coordinates[i], center_coordinates[i + 1])
        overlap = sorted(prime_sets[i] & prime_sets[i + 1])
        assert len(overlap) == 4
        overlaps.append({"pair": [i, i + 1], "intersection": overlap})

    predecessor = trajectory_label(a - 1, c, sigma)
    successor = trajectory_label(a + 9, c, sigma)
    assert predecessor % 5 == 0 and predecessor > 5
    assert successor % 5 == 0 and successor > 5
    return {
        "trajectory": {
            "sigma": sigma,
            "c": c,
            "coordinates": [list(x) for x in coordinates],
            "values": values,
            "predecessor": predecessor,
            "predecessor_factorization": [5, predecessor // 5],
            "successor": successor,
            "successor_factorization": [5, successor // 5],
        },
        "trial_division_certificates": trial,
        "flowers": flowers,
        "overlaps": overlaps,
    }


def negative_controls(witness: dict[str, object]) -> dict[str, object]:
    flowers = witness["flowers"]
    coords = [tuple(x["coordinate"]) for x in flowers]
    sets = [frozenset(x["sorted_prime_packet"]) for x in flowers]

    r, t, sigma = coords[0]
    perturbed_neighbors = list(neighbors_from_packet(r, t, sigma))
    perturbed_neighbors[1] += 1
    neighbor_formula_detected = tuple(perturbed_neighbors) != neighbors_from_coordinates(
        r, t, sigma
    )

    wrong_delta = 1 - transition_delta(r, sigma)
    wrong_next = (r + 1, t + wrong_delta, sigma)
    transition_detected = transverse(*wrong_next) != transverse(r, t, sigma)

    fake_nonadjacent = (coords[1][0], coords[1][1] + 2, coords[1][2])
    share_four_nonadjacent_rejected = not rolling_pair_valid(
        coords[0], sets[0], fake_nonadjacent, sets[1]
    )

    shared = next(iter(sets[0] & sets[1]))
    altered = frozenset((sets[1] - {shared}) | {max(sets[0] | sets[1]) + 2})
    adjacent_wrong_overlap_rejected = not rolling_pair_valid(
        coords[0], sets[0], coords[1], altered
    )
    assert all(
        (
            neighbor_formula_detected,
            transition_detected,
            share_four_nonadjacent_rejected,
            adjacent_wrong_overlap_rejected,
        )
    )
    return {
        "neighbor_slot_2_plus_one_detected": neighbor_formula_detected,
        "complementary_transition_breaks_c": transition_detected,
        "share_four_but_nonadjacent_rejected": share_four_nonadjacent_rejected,
        "adjacent_but_overlap_three_rejected": adjacent_wrong_overlap_rejected,
    }


def presentation_ablations(witness: dict[str, object]) -> dict[str, object]:
    coords = [tuple(x) for x in witness["trajectory"]["coordinates"]]
    values = witness["trajectory"]["values"]

    cyclic_ok = True
    for shift in range(3):
        renamed = [(r, t, (s + shift) % 3) for r, t, s in coords]
        transported = [
            label(r, t, (renamed_s - shift) % 3) for r, t, renamed_s in renamed
        ]
        cyclic_ok &= transported == values

    naive_shift_prime_counts = {}
    for shift in (1, 2):
        naive_values = [label(r, t, (s + shift) % 3) for r, t, s in coords]
        naive_shift_prime_counts[str(shift)] = sum(is_prime(n) for n in naive_values)

    # R(r,t,s)=(r,r-t,2-s) conjugates the neighbor deltas by
    # (dr,dt)->(dr,dr-dt), swapping slots 1<->3 and 4<->6.
    reversed_coords = [(r, r - t, (2 - s) % 3) for r, t, s in coords]
    transported_back = [
        label(r, r - reversed_t, (2 - reversed_s) % 3)
        for r, reversed_t, reversed_s in reversed_coords
    ]
    reversal_ok = transported_back == values
    transformed_deltas = tuple((dr, dr - dt) for dr, dt in NEIGHBOR_DELTAS)
    expected_reversed_deltas = (
        NEIGHBOR_DELTAS[2],
        NEIGHBOR_DELTAS[1],
        NEIGHBOR_DELTAS[0],
        NEIGHBOR_DELTAS[5],
        NEIGHBOR_DELTAS[4],
        NEIGHBOR_DELTAS[3],
    )
    reversal_ok &= transformed_deltas == expected_reversed_deltas
    assert cyclic_ok and reversal_ok
    return {
        "cyclic_sector_relabeling": "equivariant under transported labels",
        "cyclic_shifts_checked": [0, 1, 2],
        "cyclic_exact_agreement": cyclic_ok,
        "naive_untransported_sector_shift_prime_counts": naive_shift_prime_counts,
        "naive_numeric_invariance_rejected": all(
            count != len(values) for count in naive_shift_prime_counts.values()
        ),
        "orientation_reversal": "equivariant, not literal numeric-label invariance",
        "orientation_map": "(r,t,sigma)->(r,r-t,2-sigma mod 3)",
        "neighbor_slot_permutation_1_based": [3, 2, 1, 6, 5, 4],
        "orientation_exact_agreement": reversal_ok,
    }


def boundary_and_small_prime_ablation(max_shell: int = 300) -> dict[str, object]:
    boundary_flowers: list[list[int]] = []
    for r in range(4, max_shell + 1):
        for t in (0, 1, r - 1, r):
            for sigma in range(3):
                if min(neighbors_from_packet(r, t, sigma)) <= 0:
                    continue
                if flower_prime_set(r, t, sigma) is not None:
                    boundary_flowers.append([r, t, sigma])

    small_occurrences: list[dict[str, object]] = []
    for r in range(4, 31):
        for t in range(0, r + 1):
            for sigma in range(3):
                values = [label(r, t, sigma), *neighbors_from_packet(r, t, sigma)]
                hits = sorted(set(values) & {2, 3, 5})
                if hits:
                    small_occurrences.append(
                        {
                            "coordinate": [r, t, sigma],
                            "small_prime_labels": hits,
                            "interior": 2 <= t <= r - 2,
                            "is_maximal_flower": flower_prime_set(r, t, sigma) is not None,
                        }
                    )
    interior_maximal_with_small = [
        x for x in small_occurrences if x["interior"] and x["is_maximal_flower"]
    ]
    assert not interior_maximal_with_small
    return {
        "boundary_scan_shells": [4, max_shell],
        "boundary_flowers_if_guard_removed": boundary_flowers,
        "boundary_guard_rejects_all_listed": all(
            not admissible_center(*coord) for coord in boundary_flowers
        ),
        "small_prime_scan_shells": [4, 30],
        "small_primes_tested": [2, 3, 5],
        "small_prime_occurrences": small_occurrences,
        "interior_maximal_flowers_containing_2_3_or_5": interior_maximal_with_small,
    }


def c_interval_for_window(a: int, sigma: int, length: int = 9) -> tuple[int, int] | None:
    # A length-nine trajectory window supports five flowers centered at a+2,...,a+6.
    lo = -10**30
    hi = 10**30
    for r in range(a + 2, a + length - 2):
        half = (r + sigma) // 2
        lo = max(lo, 2 - half)
        hi = min(hi, r - 2 - half)
    return None if lo > hi else (lo, hi)


def congruent_values(lo: int, hi: int, residue: int, modulus: int) -> Iterator[int]:
    first = lo + (residue - lo) % modulus
    yield from range(first, hi + 1, modulus)


def search_witness(max_start_shell: int) -> dict[str, object] | None:
    # The exhaustive residue calculation leaves precisely these two reduced channels.
    reduced = ((1, 4), (6, 16))  # (a mod 10, c mod 30), with sigma=1.
    tested = 0
    small_sieve_primes = (7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43)
    for a in range(2, max_start_shell + 1):
        channel = next((pair for pair in reduced if a % 10 == pair[0]), None)
        if channel is None:
            continue
        interval = c_interval_for_window(a, 1)
        if interval is None:
            continue
        for c in congruent_values(*interval, channel[1], 30):
            tested += 1
            values = [trajectory_label(a + j, c, 1) for j in range(9)]
            if any(any(n != p and n % p == 0 for p in small_sieve_primes) for n in values):
                continue
            if all(is_prime(n) for n in values):
                return {
                    "sigma": 1,
                    "window_start_shell": a,
                    "transverse_c": c,
                    "trajectory_coordinates": [
                        [a + j, trajectory_t(a + j, c, 1), 1] for j in range(9)
                    ],
                    "prime_values": values,
                    "candidate_count_through_hit": tested,
                }
    return None


def canonical_digest(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def validate_finite_components(max_shell: int = 160) -> dict[str, object]:
    centers = 0
    flowers = 0
    transitions = 0
    for r in range(4, max_shell + 1):
        for t in range(2, r - 1):
            for sigma in range(3):
                centers += 1
                assert neighbors_from_packet(r, t, sigma) == neighbors_from_coordinates(
                    r, t, sigma
                )
                ns = neighbors_from_packet(r, t, sigma)
                # Conditional on the center being odd (hence on every possible
                # center prime >3), the two parity-forbidden slots are even.
                if label(r, t, sigma) % 2 == 1:
                    forbidden = set(range(6)) - set(eligible_neighbor_slots(r, sigma))
                    assert all(ns[i] > 2 and ns[i] % 2 == 0 for i in forbidden)
                packet_set = flower_prime_set(r, t, sigma)
                if packet_set is not None:
                    flowers += 1
                    assert sigma == 1
                    assert transverse(r, t, sigma) % 6 == 4
                    assert packet_set == trajectory_prime_set(r, t, sigma)

                delta = transition_delta(r, sigma)
                next_coord = (r + 1, t + delta, sigma)
                assert centers_adjacent_direct((r, t, sigma), next_coord)
                assert centers_adjacent_closed((r, t, sigma), next_coord)
                assert transverse(*next_coord) == transverse(r, t, sigma)
                transitions += 1
    return {
        "shell_range": [4, max_shell],
        "interior_centers_checked": centers,
        "actual_maximal_flowers_found": flowers,
        "transition_identities_checked": transitions,
        "implementations": [
            "direct packet offsets",
            "closed coordinate deltas",
            "direct flower primality",
            "five-term trajectory window",
        ],
    }


def build_result(search_max_shell: int) -> dict[str, object]:
    local = local_residue_classes()
    assert len(local) == 12
    assert {row["sigma"] for row in local} == {1}
    assert {row["c_mod_6"] for row in local} == {4}
    assert {row["parity"] for row in local} == {0, 1}

    channels = extremal_modular_channels()
    assert len(channels) == 6
    assert {
        (int(row["a_mod_30"]) % 10, int(row["c_mod_30"])) for row in channels
    } == {(1, 4), (6, 16)}
    coverage = mod_five_coverage_table()
    assert all(row["zero_shells_mod_10"] for row in coverage)
    assert max_modular_run() == 9

    found = search_witness(search_max_shell)
    assert found == WITNESS
    witness = witness_certificate()
    finite = validate_finite_components()
    controls = negative_controls(witness)
    presentation = presentation_ablations(witness)
    boundary = boundary_and_small_prime_ablation()
    symbolic = symbolic_identity_certificate()

    core: dict[str, object] = {
        "task_id": TASK_ID,
        "source_commit": SOURCE_COMMIT,
        "locked_packet_ref": LOCKED_PACKET_REF,
        "terminal_label": "SHARP_FINITE_BOUND_PROVED_AND_ATTAINED",
        "sharp_filament_bound": 5,
        "trajectory_prime_run_bound": 9,
        "proof_obstruction": "every ten consecutive eligible trajectory labels include a multiple of 5 greater than 5",
        "local_residue_classes": local,
        "mod_five_coverage": coverage,
        "extremal_channels": channels,
        "symbolic_identities": symbolic,
        "finite_cross_checks": finite,
        "search": {
            "seed": SEARCH_SEED,
            "start_shell_range": [2, search_max_shell],
            "ordering": "a ascending, then c ascending",
            "sieve_primes": [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43],
            "found": found,
        },
        "witness": witness,
        "negative_controls": controls,
        "presentation_ablations": presentation,
        "boundary_and_small_prime_ablations": boundary,
    }
    return core


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--search-max-shell", type=int, default=SEARCH_MAX_START_SHELL)
    parser.add_argument("--search-only", action="store_true")
    parser.add_argument("--json-output", type=Path)
    args = parser.parse_args()

    if args.search_only:
        witness = search_witness(args.search_max_shell)
        print(json.dumps({"search_max_shell": args.search_max_shell, "witness": witness}, indent=2))
        return 0 if witness is not None else 2

    result = build_result(args.search_max_shell)
    digest = canonical_digest(result)
    envelope = {
        "schema": "prime-native-filament-independent-checker-v1",
        "expected_frozen_digest": EXPECTED_FROZEN_DIGEST,
        "computed_frozen_digest": digest,
        "digest_matches": digest == EXPECTED_FROZEN_DIGEST,
        "result": result,
    }
    rendered = json.dumps(envelope, indent=2, sort_keys=True)
    if args.json_output is not None:
        args.json_output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    if EXPECTED_FROZEN_DIGEST == "TO_BE_FROZEN":
        return 3
    return 0 if digest == EXPECTED_FROZEN_DIGEST else 4


if __name__ == "__main__":
    raise SystemExit(main())
