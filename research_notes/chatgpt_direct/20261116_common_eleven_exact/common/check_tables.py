"""Verify the two label tables using only the original endpoint semantics."""
from collections import Counter, defaultdict
from itertools import combinations, product
from pathlib import Path
import json

from packing import no_ten

HERE = Path(__file__).resolve().parent
POINTS = list(product(range(5), repeat=3))


def table(filename, labels):
    code = list(map(int, (HERE / filename).read_text().split()))
    assert len(code) == 125 and set(code) == set(range(labels))
    return code


def audit(code):
    counts = Counter()
    forbidden = set()
    for d, start in product((1, 3), POINTS):
        receipts = defaultdict(list)
        for i, point in enumerate(POINTS):
            axes = tuple(j for j in range(3) if (point[j] - start[j]) % 5 in (0, d))
            receipts[axes].append((i, tuple(point[j] for j in axes)))
        for axes, group in receipts.items():
            for (i,a), (j,b), (k,c) in combinations(group, 3):
                if len({a,b,c}) == 3:
                    forbidden.add((i,j,k))
            by_label = defaultdict(list)
            for i, output in group:
                by_label[code[i]].append(output)
            for outputs in by_label.values():
                possibilities = sorted(set(outputs))
                assert len(possibilities) <= 2
                if len(possibilities) == 2:
                    a,b = possibilities
                    j = next(k for k in range(len(axes)) if a[k] != b[k])
                    decode = {p[j] == start[axes[j]]: p for p in possibilities}
                    assert len(decode) == 2
                    assert all(decode[p[j] == start[axes[j]]] == p for p in outputs)
                counts[len(possibilities)-1] += len(outputs)
    assert len(forbidden) == 47000
    assert not any(code[i] == code[j] == code[k] for i,j,k in forbidden)
    assert sum(counts.values()) == 31250
    return dict(reads=dict(sorted(counts.items())), sizes=sorted(Counter(code).values())), forbidden


def main():
    eleven, forbidden = audit(table("best11.txt", 11))
    twelve, _ = audit(table("twelve.txt", 12))
    proof = no_ten(forbidden)
    assert proof["minimum_messages_at_least"] == 11
    print(json.dumps(dict(eleven=eleven, twelve=twelve, no_ten=proof), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
