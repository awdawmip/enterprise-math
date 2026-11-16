"""Verify the rank-three nine-coordinate one-read certificate using Python 3.

Without options, check every class, every syndrome, rank, and all counting
claims. Using --all-histories additionally generate every translated row,
check absence of overlaps in a byte array, and check all 5^9 rows occur.
"""
import argparse
from collections import Counter
from itertools import combinations, product
import json
from pathlib import Path

DIRECTORY = Path(__file__).resolve().parent


def check_laminar(points):
    blocks = {
        frozenset(i for i, row in enumerate(points) if row[column] == value)
        for column in range(9)
        for value in range(5)
    }
    return all(
        not (a & b) or a <= b or b <= a
        for a, b in combinations(blocks, 2)
    )


def verify(enumerate_all):
    certificate = json.loads((DIRECTORY / "nine_certificate.json").read_text())
    columns = certificate["columns"]
    templates = certificate["classes"]
    assert len(columns) == 9 and len(templates) == 8
    assert all(len(column) == 3 and all(v in range(5) for v in column) for column in columns)
    rows = tuple(zip(*columns))

    def syndrome(point):
        return tuple(sum(x*y for x,y in zip(point, row)) % 5 for row in rows)

    seen = set()
    for group in templates:
        assert 0 < len(group) <= 16
        assert all(len(p) == 9 and all(x in range(5) for x in p) for p in group)
        assert check_laminar(group)
        for p in group:
            s = syndrome(p)
            assert s not in seen
            seen.add(s)
    assert seen == set(product(range(5), repeat=3))
    # Surjectivity already checked by the 125 explicit rows.
    fiber_size = 5**(9-3)
    counts = {s: n * fiber_size for s,n in Counter(map(len, templates)).items()}
    upper9 = sum(counts.values())
    upper12 = 125 * upper9
    assert upper9 == 125000 and upper12 == 15625000
    assert sum(s*n for s,n in counts.items()) == 5**9
    result = {"template_sizes": list(map(len,templates)), "syndromes": len(seen),
              "message_size_histogram":dict(sorted(counts.items())), "messages_9":upper9,
              "messages_12":upper12}
    for n, upper in [(9,upper9),(12,upper12)]:
        lower=(5**n+15)//16
        assert (lower-1).bit_length() == (upper-1).bit_length() == (5**n-1).bit_length()-4
        result[f"lower_{n}"]=lower
        result[f"fixed_bits_{n}"]=(upper-1).bit_length()
    if enumerate_all:
        powers = [5**j for j in range(9)]
        covered = bytearray(5**9)
        translates = 0
        for base in product(range(5), repeat=9):
            if syndrome(base) != (0,0,0):
                continue
            translates += 1
            for group in templates:
                for point in group:
                    idx = sum(p*((a+b)%5) for p,a,b in zip(powers, base, point))
                    assert not covered[idx]
                    covered[idx] = 1
        assert translates == fiber_size and all(covered)
        result["kernel_translates"] = translates
        result["enumerated_histories"] = len(covered)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--all-histories", action="store_true")
    print(json.dumps(verify(parser.parse_args().all_histories),indent=2))
