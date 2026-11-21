"""Rebuild and exhaust the local optimum-successor certificate from original menus."""
import argparse
import json
import os
import subprocess
import sys
from collections import defaultdict
from functools import cache
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory

HERE = Path(__file__).resolve().parent


def mask(row):
    return sum(1 << x for x in row)


def verify(previous):
    second = previous / "previous/previous/previous/previous/previous"
    third = second.parent
    os.environ["NATIVE_PROBE_PREVIOUS"] = str(second)
    sys.path[:0] = [str(third / "group"), str(second / "curve"), str(second / "bounds")]
    from generate import maps
    from prior_bounds import observation_file
    from verify import cheap_line_partitions, lower, MINIMA
    from cyclic11 import observations, class_cost
    old = cheap_line_partitions(20)
    for k in (21, 22, 23):
        assert {s for s in range(1, 14) if MINIMA[s] + lower(125 - s, k - 1) == lower(125, k)} == {5, 6}
    witness = json.loads((HERE / "twenty_transition.json").read_text())
    assert old == witness["old"]
    with TemporaryDirectory() as folder:
        work = Path(folder)
        observation_file(work / "observations")
        for name, source in [("bank", previous / "nesting/bank.cpp"), ("exclude", HERE / "local_twenty.cpp"), ("optimize", HERE / "optimize_twenty.cpp")]:
            subprocess.run(["c++", "-std=c++17", "-O3", "-mpopcnt", str(source), "-o", str(work / name)], check=True)
        subprocess.run([str(work / "bank"), str(work / "observations"), str(work / "seeds")], stdout=subprocess.DEVNULL, check=True)
        seeds = defaultdict(set)
        for line in (work / "seeds").read_text().splitlines():
            s, price, *row = map(int, line.split())
            if s in (5, 6):
                seeds[s].add(tuple(row))
        linear, translations, _ = maps()
        bank = {}
        for s, rows in seeds.items():
            rotated = {tuple(sorted(f[x] for x in row)) for row in rows for f in linear}
            bank[s] = sorted({tuple(sorted(f[x] for x in row)) for row in rotated for f in translations})
        assert {s: len(rows) for s, rows in bank.items()} == {5: 3300, 6: 12000}
        with (work / "input").open("w") as stream:
            for row in old:
                print(len(row), *row, file=stream)
            for s in (5, 6):
                print(len(bank[s]), file=stream)
                for row in bank[s]:
                    print(*row, file=stream)
        raw = subprocess.check_output([str(work / "exclude"), str(work / "input"), "0", "5"], text=True)
        exclusions = [json.loads(line) for line in raw.splitlines()]
        assert [r["extra_sixes_exhausted"] for r in exclusions] == list(range(5))
        assert exclusions[-1] == {"extra_sixes_exhausted": 4, "nodes": 1597234, "regions": 1941}
        raw = subprocess.check_output([str(work / "optimize"), str(work / "input"), "5", "6"], text=True)
        found = [json.loads(line) for line in raw.splitlines()]
        assert found[-1] == {"extra_sixes_exhausted": 5, "nodes": 29891922, "regions": 3003, "solutions": 5, "best_moved": 41}
        assert any({frozenset(r) for r in x.get("groups", [])} == {frozenset(r) for r in witness["new"]} for x in found)
    bad, menus = observations()
    lookup = {s: set(map(frozenset, rows)) for s, rows in bank.items()}
    def audit(rows):
        assert sorted(x for r in rows for x in r) == list(range(125))
        assert not any(bad[a][b] >> c & 1 for r in rows for a, b, c in combinations(sorted(r), 3))
        assert sum(class_cost(r, menus) for r in rows) == lower(125, len(rows))
    old_sets = set(map(frozenset, old))
    new = list(map(frozenset, witness["new"]))
    audit(old); audit(new)
    common = old_sets & set(new)
    assert len(common) == 10
    old_local = tuple(old_sets - common)
    new_local = tuple(set(new) - common)
    @cache
    def assign(i, used):
        if i == len(old_local):
            return 0
        return max(len(old_local[i] & row) + assign(i + 1, used | (1 << j)) for j, row in enumerate(new_local) if not used >> j & 1)
    assert sum(map(len, old_local)) - assign(0, 0) == 41
    orbit = set()
    for t in range(5):
        def shift(row):
            return frozenset(5 * (x // 5) + (x + t) % 5 for x in row)
        assert set(map(shift, old_sets)) == old_sets
        image = frozenset(map(shift, new))
        audit(image)
        assert len(image & old_sets) == 10
        orbit.add(image)
    assert len(orbit) == 5
    def moves(rows):
        removable = {x: i for i, row in enumerate(rows) if len(row) == 6 for x in row if row - {x} in lookup[5]}
        return [q for q in lookup[5] if all(x in removable for x in q) and len({removable[x] for x in q}) == 5]
    choices = moves(new)
    assert len(choices) == 1
    q = choices[0]
    assert sorted(q) == [3, 46, 62, 94, 105]
    next_rows = [r - q for r in new] + [q]
    audit(next_rows)
    assert not moves(next_rows)
    return json.loads((HERE / "result.json").read_text())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--previous", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(verify(args.previous.resolve()), indent=2, sort_keys=True))
