"""Count all weighted histories and check each selected physical endpoint separates outputs."""
import json
from collections import Counter, defaultdict
from itertools import product
from pathlib import Path
import sys

def verify(labels):
    points = list(product(range(5), repeat=3))
    assert len(labels) == len(points) and set(labels) == set(range(12))
    counts = Counter()
    reads_by_class = [0] * 12
    sizes = [labels.count(i) for i in range(12)]
    witnesses = Counter()
    for delta in (1, 3):
        for start in points:
            groups = defaultdict(list)
            for history, label in zip(points, labels):
                axes = tuple(i for i in range(3) if (history[i] - start[i]) % 5 in (0, delta))
                output = tuple(history[i] for i in axes)
                groups[label, axes].append(output)
            for (label, axes), outputs in groups.items():
                possibilities = sorted(set(outputs))
                assert len(possibilities) <= 2
                read = len(possibilities) == 2
                counts[int(read)] += len(outputs)
                if read:
                    left, right = possibilities
                    j = next(k for k in range(len(axes)) if left[k] != right[k])
                    # The two possible old endpoints on this active axis map to two distinct replies.
                    table = {output[j] == start[axes[j]]: output for output in possibilities}
                    assert len(table) == 2
                    assert all(table[output[j] == start[axes[j]]] == output for output in outputs)
                    reads_by_class[label] += len(outputs)
                    witnesses[axes[j]] += len(outputs)
    assert sum(counts.values()) == 31250
    assert counts[1] == sum(reads_by_class)
    return dict(class_sizes=sizes, reads_by_class=reads_by_class, zero_reads=counts[0],
                one_read=counts[1], selected_axes=dict(sorted(witnesses.items())))

if __name__ == "__main__":
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("twelve.txt")
    report = verify(list(map(int, path.read_text().split())))
    print(json.dumps(report, indent=2))
