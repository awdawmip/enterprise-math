"""Small independent checks for the finite rational C78/C87 readout bridge."""
import json
from fractions import Fraction as Q
from pathlib import Path
from exact_inventory import (SOURCE_COMMIT, kernel_tail_ratios,
                             positive_path_tail_ratios, readout, unique_count)


def integer_cube_ceiling(c):
    b = 1
    while b**3 < c:
        b += 1
    return b


def main():
    points = set()
    base_templates = 0
    for c in range(2, 13):
        base_templates += c*(c-1)//2
        stocks = (c, c+1, c+integer_cube_ceiling(c), 2*c)
        for v in range(2, c+1):
            for w in range(2, v+1):
                points.update((n, v, w) for n in stocks)
    points.update(((64, 40, 20), (65, 40, 20), (128, 40, 20)))
    for n, v, w in sorted(points):
        kernel = kernel_tail_ratios(n, v, w)
        positive = positive_path_tail_ratios(n, v, w)
        assert kernel == positive, (n, v, w)
        assert all(x > 0 for x in kernel)

    witnesses = []
    for n, v, w in ((2, 2, 2), (8, 6, 3), (9, 6, 3), (16, 6, 3)):
        witnesses.append({"n": n, "v": v, "w": w,
                          "tail_ratios": [str(x) for x in kernel_tail_ratios(n, v, w)],
                          "g": str(readout(n, v, w))})
    # Same c=8 templates on c,c+1,c+ceil(c**(1/3)),2c; original C78 offsets.
    offsets = (Q(0), Q(1, 3), Q(2, 5), Q(3, 7))
    stocks = (8, 9, 10, 16)
    bins = []
    for p in (6, 9, 12):
        bins.append({"p": p,
                     "counts": [unique_count(8, (8, n), p, (offsets[0], offsets[j]))
                                for j, n in enumerate(stocks[1:], 1)]})
    result = {
        "source_commit": SOURCE_COMMIT,
        "arithmetic": "fractions.Fraction; no floating point, Gamma, log or roots",
        "base_inventory_range": [2, 12],
        "base_templates": base_templates,
        "distinct_inventory_templates_checked": len(points),
        "individual_tail_equalities": 3*len(points),
        "positive_path_tail_mass_partition_checked": True,
        "all_equalities_passed": True,
        "witnesses": witnesses,
        "c8_exact_bin_counts": {"stocks": list(stocks), "templates": 28,
                                "offsets": [str(x) for x in offsets], "rows": bins},
        "proof_scope": "The general finite-kernel identity has a written algebraic proof. These finite checks validate its implementation; they do not establish C78/C87 asymptotics."
    }
    output = Path(__file__).with_name("exact_inventory_checks.json")
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({k: v for k, v in result.items() if k != "witnesses"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
