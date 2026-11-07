"""Exact integer control checks for already-certified absence residues.

This module consumes H, not an unread request table.  The exhaustive loop is
a finite mathematical checker of coverage; it does not execute BRC commands.
"""

from __future__ import annotations

import json
from math import gcd
from pathlib import Path


def parameters(r: int) -> tuple[int, int, int, int]:
    m_full = r + 1
    radix = 1 << (m_full - 1).bit_length()
    block_width = gcd(m_full, radix)
    return radix, block_width, radix // block_width, m_full // block_width


def block_of(residue: int, radix: int, width: int) -> int:
    return ((residue - 1) % radix) // width


def support(h: tuple[int, ...], radix: int, width: int) -> tuple[int, ...]:
    return tuple(sorted({block_of(u, radix, width) for u in h}))


def cyclic_gaps(s: tuple[int, ...], length: int) -> tuple[int, ...]:
    if not s:
        return ()
    return tuple(b - a for a, b in zip(s, s[1:])) + (length + s[0] - s[-1],)


def uncovered_phases(r: int, h: tuple[int, ...]) -> int:
    radix, width, length, m = parameters(r)
    s = support(h, radix, width)
    if not s:
        return length
    return sum(max(0, gap - m) for gap in cyclic_gaps(s, length))


def small_cover(r: int, h: tuple[int, ...]) -> tuple[int, ...] | None:
    """Return a one/two-residue all-period subcertificate when it exists."""
    radix, width, length, m = parameters(r)
    if m == length:
        return h[:1] or None
    k = length - m
    for i, u in enumerate(h):
        for v in h[i + 1:]:
            distance = (block_of(v, radix, width) - block_of(u, radix, width)) % length
            if k <= distance <= m:
                return (u, v)
    return None


def one_point_repair_blocks(r: int, h: tuple[int, ...]) -> tuple[int, ...]:
    """Block choices whose one new certified residue repairs a coverage gap.

    If H already covers, every block is returned.  Empty H can be repaired by
    one residue exactly in the power-of-two family (one block in that case).
    """
    radix, width, length, m = parameters(r)
    s = support(h, radix, width)
    if not s:
        return tuple(range(length)) if m == length else ()
    gaps = cyclic_gaps(s, length)
    largest = max(gaps)
    if largest <= m:
        return tuple(range(length))
    a = s[gaps.index(largest)]
    return tuple((a + x) % length for x in range(largest - m, m + 1))


def finite_library_covers(r: int, h: tuple[int, ...], targets: tuple[int, ...]) -> bool:
    m_full = r + 1
    radix, _, _, _ = parameters(r)
    hs = set(h)
    return all(hs & {(1 + t * m_full + c) % radix for c in range(m_full)} for t in targets)


def exhaustive(max_r: int = 15) -> dict:
    rows = []
    total_sets = total_deletions = total_corridor_checks = total_small_covers = 0
    for r in range(1, max_r + 1):
        radix, width, length, m = parameters(r)
        m_full = r + 1
        v = radix - r
        windows = tuple(
            sum(1 << ((1 + t * m_full + c) % radix) for c in range(m_full))
            for t in range(length)
        )
        tuples = [tuple(u for u in range(radix) if mask >> u & 1) for mask in range(1 << radix)]
        misses = []
        small_covers_checked = 0
        for mask, h in enumerate(tuples):
            exact = sum((mask & w) == 0 for w in windows)
            assert uncovered_phases(r, h) == exact, (r, h, exact)
            misses.append(exact)
            if len(h) >= v:
                cert = small_cover(r, h)
                assert cert is not None and uncovered_phases(r, cert) == 0, (r, h, cert)
                small_covers_checked += 1

        deletion_checks = corridor_checks = 0
        for mask, h in enumerate(tuples):
            if misses[mask]:
                continue
            for removed in h:
                remainder_mask = mask ^ (1 << removed)
                remainder = tuples[remainder_mask]
                old_s = support(h, radix, width)
                remaining_s = support(remainder, radix, width)
                if old_s == remaining_s:
                    predicted = 0
                elif not remaining_s:
                    predicted = length
                else:
                    lost_block = block_of(removed, radix, width)
                    i = old_s.index(lost_block)
                    old_gaps = cyclic_gaps(old_s, length)
                    merged = old_gaps[i - 1] + old_gaps[i]
                    predicted = max(0, merged - m)
                assert predicted == misses[remainder_mask], (r, h, removed, predicted)
                deletion_checks += 1
                if misses[remainder_mask]:
                    corridor = set(one_point_repair_blocks(r, remainder))
                    for u in range(radix):
                        actual = misses[remainder_mask | (1 << u)] == 0
                        assert actual == (block_of(u, radix, width) in corridor), (r, remainder, u)
                        corridor_checks += 1

        row = {
            "r": r, "M": m_full, "B": radix, "g": width, "L": length, "m": m,
            "certificate_subsets": len(tuples),
            "two_or_one_point_certificate_checks": small_covers_checked,
            "single_residue_deletion_checks": deletion_checks,
            "one_point_repair_candidate_checks": corridor_checks,
        }
        rows.append(row)
        total_sets += len(tuples)
        total_deletions += deletion_checks
        total_corridor_checks += corridor_checks
        total_small_covers += small_covers_checked

    # Required scoped examples distinguish all target phases and the actual d=3 library.
    assert finite_library_covers(6, (3,), (0, 1, 2))
    assert uncovered_phases(6, (3,)) == 1
    assert not finite_library_covers(6, (3,), (5,))
    assert uncovered_phases(14, (3,)) == 1
    assert uncovered_phases(7, (3,)) == 0
    assert uncovered_phases(8, (0, 5, 10)) == 0
    assert small_cover(8, (0, 5, 10)) is None

    # With r=8, overwriting residue 1 by 8 leaves the central one-point repair corridor occupied.
    old_requests = {1, 2, 3, 4, 5, 7, 9, 10}
    new_requests = (old_requests - {1}) | {8}
    available = set(range(16)) - new_requests
    assert {0, 8}.isdisjoint(old_requests)
    assert uncovered_phases(8, (0, 8)) == 0
    assert uncovered_phases(8, (0,)) == 7
    corridor_residues = {
        u for u in range(16)
        if block_of(u, 16, 1) in one_point_repair_blocks(8, (0,))
    }
    assert corridor_residues == {7, 8, 9}
    assert available.isdisjoint(corridor_residues)
    assert {0, 6, 14} <= available
    assert uncovered_phases(8, (0, 6, 14)) == 0

    return {
        "status": "PASS",
        "scope": "All r=1..15 and all subsets H of Z/BZ; exact integer coverage control only",
        "physical_BRC_execution": False,
        "counts": {
            "certificate_subsets": total_sets,
            "two_or_one_point_certificate_checks": total_small_covers,
            "single_residue_deletion_checks": total_deletions,
            "one_point_repair_candidate_checks": total_corridor_checks,
        },
        "rows": rows,
        "examples": {
            "r6_singleton3": {"finite_targets_0_1_2_covered": True, "missed_full_period_target": 5},
            "r14_singleton3": {"missed_full_period_target": 13},
            "r7_singleton3": {"all_targets_covered": True},
            "r8_three_point_cover_with_no_covering_pair": [0, 5, 10],
            "r8_one_point_repair_gap": {
                "old_requests": sorted(old_requests), "new_requests": sorted(new_requests),
                "remaining_certificate": [0], "one_point_repair_residues": sorted(corridor_residues),
                "safe_two_additions": [6, 14],
            },
        },
    }


if __name__ == "__main__":
    result = exhaustive()
    Path(__file__).with_name("coverage_geometry_checks.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({"status": result["status"], "counts": result["counts"]}, ensure_ascii=False))
