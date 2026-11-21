"""Complete normalized five-mother necessary-condition enumeration.

This does not search for a twelve-class partition or exclude cost 9866.
The parent list is the inherited complete native 13-point class list.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
COORD = [(x // 25, x // 5 % 5, x % 5) for x in range(125)]
FIBERS = [sum(1 << x for x in range(125) if COORD[x][j] == a)
          for j in range(3) for a in range(5)]


def points(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def moved(mask, shift=(0, 0, 0), scale=1):
    ans = 0
    for x in points(mask):
        u = tuple((scale * COORD[x][j] + shift[j]) % 5 for j in range(3))
        ans |= 1 << (25 * u[0] + 5 * u[1] + u[2])
    return ans


def run(parent_path):
    data = parent_path.read_bytes()
    lines = data.decode().splitlines()
    # The original file has 250 masks followed by a parent-intersection row.
    mothers = set()
    for line in lines[:250]:
        lo, hi = map(int, line.split())
        mothers.add(lo | (hi << 64))
    assert len(mothers) == 250 and all(m.bit_count() == 13 for m in mothers)
    by_center = defaultdict(list)
    for m in sorted(mothers):
        center = []
        for j in range(3):
            counts = [(m & FIBERS[5*j+a]).bit_count() for a in range(5)]
            assert sorted(counts) == [2, 2, 2, 2, 5]
            center.append(counts.index(5))
        by_center[tuple(center)].append(m)
    assert len(by_center) == 125 and all(len(v) == 2 for v in by_center.values())
    # Verify the normalization action on the complete finite parent list.
    assert all(moved(m, scale=2) in mothers for m in mothers)
    for shift in COORD:
        assert all(moved(m, shift=shift) in mothers for m in mothers)
    anchor, other = by_center[(0, 0, 0)]
    assert moved(anchor, scale=2) == other and moved(other, scale=2) == anchor
    histogram = Counter()
    survivors = []
    total = 0
    for second in itertools.permutations(range(1, 5)):
        for third in itertools.permutations(range(1, 5)):
            for orientations in itertools.product(range(2), repeat=4):
                parents = [anchor]
                for i in range(1, 5):
                    parents.append(by_center[(i, second[i-1], third[i-1])][orientations[i-1]])
                union = 0
                for m in parents:
                    union |= m
                deficit = sum(max(11-(union & f).bit_count(), 0) for f in FIBERS)
                histogram[(union.bit_count(), deficit)] += 1
                total += 1
                if deficit == 0:
                    survivors.append({"mothers": [str(m) for m in parents],
                                      "union_size": union.bit_count()})
    assert total == 24*24*16 == 9216
    counts = Counter(row['union_size'] for row in survivors)
    assert counts == {57:420, 58:240, 59:120, 60:80, 61:60, 65:4}
    return {"status": "COMPLETE_NECESSARY_CONDITION_CLASSIFICATION",
            "review_status": "NOT_REVIEWED",
            "parent_sha256": hashlib.sha256(data).hexdigest(),
            "parent_count": 250, "normalization_action_verified": True,
            "normalized_parent_configurations": total,
            "fiber_capacity_survivors": len(survivors),
            "survivors_by_union_size": dict(sorted(counts.items())),
            "union_size_and_deficit_histogram": [list(k)+[v] for k,v in sorted(histogram.items())],
            "whole_partition_search": False,
            "survivors": survivors}


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--parents', type=Path, default=HERE.parent/'integer_cuts/mother12/native_sublevels/inputs/parent')
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    result = run(args.parents)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('survivors','union_size_and_deficit_histogram')}, sort_keys=True))
