"""Run inside the evidence directory after running the paired C++ benchmark."""
import csv
from collections import defaultdict
from pathlib import Path
from statistics import median

base = Path(__file__).resolve().parent
for raw_name, output_name, group_count in [("raw.csv", "summary.csv", 540),
                                             ("holdout.csv", "holdout_summary.csv", 360)]:
    banks = defaultdict(list)
    with (base / raw_name).open() as file:
        for row in csv.DictReader(file):
            key = (row["family"], row["method"], int(row["n"]), int(row["bank"]))
            banks[key].append(int(row["ns"]))
    assert len(banks) == group_count and all(len(values) == 3 for values in banks.values())
    groups = defaultdict(list)
    for (family, method, n, bank), observations in banks.items():
        groups[family, method, n].append(median(observations))
    previous = {}
    with (base / output_name).open("w") as file:
        writer = csv.writer(file)
        writer.writerow(["family", "method", "n", "median_ms", "ns_per_key", "adjacent_ratio",
                         "min_bank_median_ms", "max_bank_median_ms"])
        for (family, method, n), values in sorted(groups.items()):
            assert len(values) == 3
            elapsed = median(values)
            key = family, method
            ratio = elapsed / previous[key] if key in previous else None
            writer.writerow([family, method, n, f"{elapsed/1e6:.6f}", f"{elapsed/n:.4f}",
                             f"{ratio:.4f}" if ratio is not None else "", min(values)/1e6, max(values)/1e6])
            previous[key] = elapsed
