# BRC 残差优先试算：一百万以内的 100 个随机自然数

Progress-Event-ID: `brc-residual-priority-million-20261104-b0e94005`
At: `2026-11-04 13:07:21 UTC`
Status: executed experiment under an explicit provisional ordering convention.
Scientific source: `awdawmip/enterprise-math@9107f0215f7a724ff4117f8dac83712ec7ece698`.
Global control snapshot reused: `2827dbd8bdd216a1135fade833ca64144cd0c526`, verified 2026-11-04 10:58 UTC.
Conversation: `chat-brc-sort-b0e94005ad9c-20261103`.
Researcher-ID / Research-Activity-ID: unconfirmed; no formal task claim or admission asserted.

## 1. User correction and remaining semantic question

The current user request is: “计算1000000以内的100个随机数 关键是快速排出‘brc’顺序而不是大小顺序”.

The accepted target is BRC order for 100 random natural numbers within one million, with emphasis on rapid ordering. The previous natural-number numeric-ascending radix construction does not answer this corrected objective.

The inspected core/root/division interfaces define collapse and residual fields, but do not specify a unique comparator for arbitrary natural numbers. The multipath enrichment bridge's ordered paths and information-retention hierarchy also do not by themselves define a natural-number total order. This is a statement about the inspected sources, not an exhaustive claim that no such order exists anywhere in the project.

The following is therefore a **provisional working convention for a concrete, reviewable computation**, not an attributed user definition or a newly established canonical BRC order:

    k(n) = floor(sqrt(n))
    C(n) = k(n)^2
    r(n) = n - C(n)
    primary ordering: increasing r(n)
    equal residuals: retain original input order

The code's default root degree p=2 is source-backed. Residual priority and stable ties are choices for this experiment. User confirmation or a precise alternative BRC comparator remains needed to identify the intended order. This experiment preserves the original data for reuse with another comparator.

## 2. Reused arithmetic and source scope

- [core.py](https://github.com/awdawmip/enterprise-math/blob/9107f0215f7a724ff4117f8dac83712ec7ece698/src/enterprise_math/core.py): default square collapse and integer-only root.
- [exact_arithmetic.py](https://github.com/awdawmip/enterprise-math/blob/9107f0215f7a724ff4117f8dac83712ec7ece698/src/enterprise_math/exact_arithmetic.py): root expressions and BRCRootTrace.
- [multipath enrichment bridge](https://github.com/awdawmip/enterprise-math/blob/9107f0215f7a724ff4117f8dac83712ec7ece698/definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md): path/provenance semantics, not the provisional comparator used here.

All residuals were obtained through existing brc_evaluate_root(root(n,2)), unchanged in behavior. Canonical module blobs are core.py cdb8ace10e4cc8bba13b70f4da306313efb24819, division.py bf0b1a6b6aeccc94578d11509c5bcd12ff930cb5, exact_arithmetic.py 35ea95b0916494b83a92386e3e313928362dd79e. The execution copies differ only in trailing newline whitespace. Reuse state: REUSE_EXECUTED.

This uses the project's arithmetic root trace, not CWM logarithmic surplus, physical-time ordering, or a native-X6 residual attribution claim.

## 3. Exact input

Generator: CPython random.Random(20261104); 100 independent randrange(1_000_001) draws. Sampling allows replacement; the realized sample has 100 distinct values. Bounds include both 0 and 1,000,000.

```text
776669, 662511, 219200, 338659, 388826, 523002, 620061, 21207, 239119, 406150,
6832, 680904, 903234, 567856, 614522, 854859, 983043, 649315, 726747, 77213,
479627, 393880, 918633, 29715, 470043, 911431, 716362, 168020, 904033, 573868,
494099, 740040, 250943, 876000, 881624, 852793, 898562, 120952, 815627, 299640,
722386, 305300, 223078, 116502, 807433, 715643, 335088, 577156, 528271, 522144,
861438, 551401, 819148, 517371, 404338, 557580, 473827, 328238, 190261, 775183,
436400, 784253, 221317, 160791, 633460, 231052, 712313, 38027, 999249, 941354,
558476, 330879, 757660, 516141, 542427, 12511, 853348, 536321, 368551, 517871,
399456, 458655, 203314, 259040, 867863, 691595, 890000, 846822, 545134, 827510,
816750, 13005, 552596, 784689, 482193, 559888, 233389, 578371, 325011, 802462
```

Sample minimum: 6832. Sample maximum: 999249.

## 4. Result under the working convention

```text
38027, 13005, 399456, 233389, 368551, 6832, 325011, 819148, 29715, 190261,
219200, 21207, 12511, 815627, 116502, 861438, 330879, 523002, 680904, 223078,
458655, 406150, 559888, 517371, 221317, 846822, 299640, 740040, 941354, 558476,
473827, 77213, 545134, 536321, 776669, 120952, 552596, 482193, 305300, 516141,
716362, 231052, 620061, 388826, 542427, 903234, 168020, 393880, 890000, 757660,
479627, 578371, 775183, 160791, 436400, 203314, 470043, 573868, 551401, 726747,
567856, 522144, 852793, 918633, 517871, 250943, 983043, 239119, 259040, 335088,
784253, 807433, 691595, 328238, 557580, 577156, 854859, 338659, 867863, 404338,
528271, 827510, 999249, 649315, 494099, 911431, 816750, 853348, 614522, 633460,
802462, 784689, 904033, 662511, 722386, 715643, 712313, 898562, 876000, 881624
```

The input-index column below is zero-based and preserves identity.

| Input index | Natural n | Root index k | Collapse C | Residual r |
|---:|---:|---:|---:|---:|
| 67 | 38027 | 195 | 38025 | 2 |
| 91 | 13005 | 114 | 12996 | 9 |
| 80 | 399456 | 632 | 399424 | 32 |
| 96 | 233389 | 483 | 233289 | 100 |
| 78 | 368551 | 607 | 368449 | 102 |
| 10 | 6832 | 82 | 6724 | 108 |
| 98 | 325011 | 570 | 324900 | 111 |
| 52 | 819148 | 905 | 819025 | 123 |
| 23 | 29715 | 172 | 29584 | 131 |
| 58 | 190261 | 436 | 190096 | 165 |
| 2 | 219200 | 468 | 219024 | 176 |
| 7 | 21207 | 145 | 21025 | 182 |
| 75 | 12511 | 111 | 12321 | 190 |
| 38 | 815627 | 903 | 815409 | 218 |
| 43 | 116502 | 341 | 116281 | 221 |
| 50 | 861438 | 928 | 861184 | 254 |
| 71 | 330879 | 575 | 330625 | 254 |
| 5 | 523002 | 723 | 522729 | 273 |
| 11 | 680904 | 825 | 680625 | 279 |
| 42 | 223078 | 472 | 222784 | 294 |
| 81 | 458655 | 677 | 458329 | 326 |
| 9 | 406150 | 637 | 405769 | 381 |
| 95 | 559888 | 748 | 559504 | 384 |
| 53 | 517371 | 719 | 516961 | 410 |
| 62 | 221317 | 470 | 220900 | 417 |
| 87 | 846822 | 920 | 846400 | 422 |
| 39 | 299640 | 547 | 299209 | 431 |
| 31 | 740040 | 860 | 739600 | 440 |
| 69 | 941354 | 970 | 940900 | 454 |
| 70 | 558476 | 747 | 558009 | 467 |
| 56 | 473827 | 688 | 473344 | 483 |
| 19 | 77213 | 277 | 76729 | 484 |
| 88 | 545134 | 738 | 544644 | 490 |
| 77 | 536321 | 732 | 535824 | 497 |
| 0 | 776669 | 881 | 776161 | 508 |
| 37 | 120952 | 347 | 120409 | 543 |
| 92 | 552596 | 743 | 552049 | 547 |
| 94 | 482193 | 694 | 481636 | 557 |
| 41 | 305300 | 552 | 304704 | 596 |
| 73 | 516141 | 718 | 515524 | 617 |
| 26 | 716362 | 846 | 715716 | 646 |
| 65 | 231052 | 480 | 230400 | 652 |
| 6 | 620061 | 787 | 619369 | 692 |
| 4 | 388826 | 623 | 388129 | 697 |
| 74 | 542427 | 736 | 541696 | 731 |
| 12 | 903234 | 950 | 902500 | 734 |
| 27 | 168020 | 409 | 167281 | 739 |
| 21 | 393880 | 627 | 393129 | 751 |
| 86 | 890000 | 943 | 889249 | 751 |
| 72 | 757660 | 870 | 756900 | 760 |
| 20 | 479627 | 692 | 478864 | 763 |
| 97 | 578371 | 760 | 577600 | 771 |
| 59 | 775183 | 880 | 774400 | 783 |
| 63 | 160791 | 400 | 160000 | 791 |
| 60 | 436400 | 660 | 435600 | 800 |
| 82 | 203314 | 450 | 202500 | 814 |
| 24 | 470043 | 685 | 469225 | 818 |
| 29 | 573868 | 757 | 573049 | 819 |
| 51 | 551401 | 742 | 550564 | 837 |
| 18 | 726747 | 852 | 725904 | 843 |
| 13 | 567856 | 753 | 567009 | 847 |
| 49 | 522144 | 722 | 521284 | 860 |
| 35 | 852793 | 923 | 851929 | 864 |
| 22 | 918633 | 958 | 917764 | 869 |
| 79 | 517871 | 719 | 516961 | 910 |
| 32 | 250943 | 500 | 250000 | 943 |
| 16 | 983043 | 991 | 982081 | 962 |
| 8 | 239119 | 488 | 238144 | 975 |
| 83 | 259040 | 508 | 258064 | 976 |
| 46 | 335088 | 578 | 334084 | 1004 |
| 61 | 784253 | 885 | 783225 | 1028 |
| 44 | 807433 | 898 | 806404 | 1029 |
| 85 | 691595 | 831 | 690561 | 1034 |
| 57 | 328238 | 572 | 327184 | 1054 |
| 55 | 557580 | 746 | 556516 | 1064 |
| 47 | 577156 | 759 | 576081 | 1075 |
| 15 | 854859 | 924 | 853776 | 1083 |
| 3 | 338659 | 581 | 337561 | 1098 |
| 84 | 867863 | 931 | 866761 | 1102 |
| 54 | 404338 | 635 | 403225 | 1113 |
| 48 | 528271 | 726 | 527076 | 1195 |
| 89 | 827510 | 909 | 826281 | 1229 |
| 68 | 999249 | 999 | 998001 | 1248 |
| 17 | 649315 | 805 | 648025 | 1290 |
| 30 | 494099 | 702 | 492804 | 1295 |
| 25 | 911431 | 954 | 910116 | 1315 |
| 90 | 816750 | 903 | 815409 | 1341 |
| 76 | 853348 | 923 | 851929 | 1419 |
| 14 | 614522 | 783 | 613089 | 1433 |
| 64 | 633460 | 795 | 632025 | 1435 |
| 99 | 802462 | 895 | 801025 | 1437 |
| 93 | 784689 | 885 | 783225 | 1464 |
| 28 | 904033 | 950 | 902500 | 1533 |
| 1 | 662511 | 813 | 660969 | 1542 |
| 40 | 722386 | 849 | 720801 | 1585 |
| 45 | 715643 | 845 | 714025 | 1618 |
| 66 | 712313 | 843 | 710649 | 1664 |
| 36 | 898562 | 947 | 896809 | 1753 |
| 33 | 876000 | 935 | 874225 | 1775 |
| 34 | 881624 | 938 | 879844 | 1780 |

There are 98 distinct residuals, from 2 to 1780. Ties:

```json
{
  "254": [
    861438,
    330879
  ],
  "751": [
    393880,
    890000
  ]
}
```

The first two outputs already distinguish this order from numerical order:
38027=195²+2 precedes 13005=114²+9 because 2<9, even though 38027>13005. Every record is preserved; equal residuals use original occurrence order.

## 5. Fast ordering and measured cost

Compute each input's root trace once and decorate the input with its residual. A stable sort then compares residual keys only. It does not require constructing all pairwise relations or repeatedly recalculating a key during comparisons.

For all 0<=n<=1,000,000, residual r lies in [0,1998]. If k<=999, r<=2k<=1998; if k=1000, the only allowed n is1,000,000 and r=0. The bound is attained at n=999999. Thus a dense stable bucket alternative uses1999 buckets.

Post-extraction comparison sorting has O(m log m) key comparison cost; dense bucket ordering uses O(m+1999) operations and O(m+1999) records/buckets. Both also include m root-trace evaluations. These formulae do not alone determine which is faster for m=100.

Actual environment: CPython 3.12.14, x86_64. The measurements below are microseconds per100-number batch. timeit performs7 repeats of each indicated call count; median is computed from per-call means. Timers cover local in-process work, excluding tool/network latency. Each timing category is measured independently, so its median is not required to sum exactly to another category.

| Operation | Median microseconds | Min | Max | Calls per repeat |
|---|---:|---:|---:|---:|
| brc_residual_extraction_100 | 494.897 | 484.989 | 504.182 | 200 |
| stable_sort_100_cached_keys | 3.476 | 3.336 | 3.611 | 2000 |
| bucket_sort_100_cached_keys | 125.423 | 121.084 | 133.766 | 500 |
| end_to_end_100 | 507.812 | 496.072 | 543.744 | 200 |

On this sample and these Python implementations, stable sorting of cached keys was faster than allocating and scanning1999 buckets. Root-state extraction dominated the whole batch. This is a local measurement, not a universal fastest-algorithm result or a performance guarantee for other hardware.

## 6. Validation and complete reproduction code

Actual execution exited0. Checks passed for:
- complete input occurrence preservation;
- increasing residual order and stable ties;
- exact n=C+r and C=k² reconstruction with valid residual bounds;
- equality of comparison-sort and bucket-sort outputs;
- square and million-boundary cases, including the exact residual upper bound;
- preservation of the input order for a list of perfect squares with equal residual0;
- this sample's output differing from numeric ascending order.

```python
"""Provisional square-residual-priority order for 100 random naturals.

Work convention: ascending square-collapse remainder, stable on ties.
This is not asserted to be a canonical definition of 'BRC order'.
"""
import json
import platform
import random
import statistics
import sys
import timeit
from operator import itemgetter

from enterprise_math.exact_arithmetic import brc_evaluate_root, root

UPPER = 1_000_000
COUNT = 100
SEED = 20261104
BUCKET_COUNT = 1999
RESIDUAL = itemgetter(4)


def extract_records(values):
    records = []
    for i, n in enumerate(values):
        if isinstance(n, bool) or not isinstance(n, int) or not 0 <= n <= UPPER:
            raise ValueError("expected a natural number from 0 through 1,000,000")
        trace = brc_evaluate_root(root(n, 2))
        records.append((i, n, trace.root_index,
                        trace.collapsed_radicand, trace.remainder))
    return records


def stable_residual_order(records):
    return sorted(records, key=RESIDUAL)


def stable_bucket_order(records):
    buckets = [[] for _ in range(BUCKET_COUNT)]
    for row in records:
        buckets[row[4]].append(row)
    return [row for bucket in buckets for row in bucket]


def end_to_end(values):
    return stable_residual_order(extract_records(values))


rng = random.Random(SEED)
values = [rng.randrange(UPPER + 1) for _ in range(COUNT)]
records = extract_records(values)
ordered = stable_residual_order(records)
bucket_ordered = stable_bucket_order(records)

assert ordered == bucket_ordered
assert len(ordered) == COUNT
assert sorted(row[0] for row in ordered) == list(range(COUNT))
assert all((x[4], x[0]) <= (y[4], y[0])
           for x, y in zip(ordered, ordered[1:]))
assert all(row[1] == row[3] + row[4]
           and row[3] == row[2] * row[2]
           and 0 <= row[4] <= 2 * row[2]
           for row in records)
assert [row[1] for row in ordered] != sorted(values)

edges = [0, 1, 2, 3, 4, 8, 9, 15, 16, 999_998, 999_999, 1_000_000]
edge_records = extract_records(edges)
assert max(row[4] for row in edge_records) == 1998
assert stable_residual_order(edge_records) == stable_bucket_order(edge_records)
square_ties = extract_records([1_000_000, 81, 16, 0, 81])
assert stable_residual_order(square_ties) == square_ties
assert stable_bucket_order(square_ties) == square_ties

def benchmark(function, number):
    samples = timeit.repeat(function, repeat=7, number=number)
    per_call = [t / number * 1e6 for t in samples]
    return {"median_us": statistics.median(per_call),
            "min_us": min(per_call), "max_us": max(per_call),
            "repeats": 7, "calls_per_repeat": number}

timings = {
    "brc_residual_extraction_100": benchmark(lambda: extract_records(values), 200),
    "stable_sort_100_cached_keys": benchmark(lambda: stable_residual_order(records), 2000),
    "bucket_sort_100_cached_keys": benchmark(lambda: stable_bucket_order(records), 500),
    "end_to_end_100": benchmark(lambda: end_to_end(values), 200),
}
groups = {}
for row in ordered:
    groups.setdefault(row[4], []).append(row[1])

print(json.dumps({
    "criterion_status": "PROVISIONAL_WORK_CONVENTION",
    "criterion": "square-collapse residual ascending; input order retained on ties",
    "seed": SEED, "sampling": "100 independent randrange(1_000_001) draws",
    "input": values,
    "records_schema": ["input_index_0", "n", "root_index", "collapse", "residual"],
    "ordered_records": ordered,
    "ordered_values": [row[1] for row in ordered],
    "sorted_residuals": [row[4] for row in ordered],
    "sample": {"minimum": min(values), "maximum": max(values),
               "distinct_values": len(set(values)),
               "distinct_residuals": len(groups),
               "residual_minimum": ordered[0][4], "residual_maximum": ordered[-1][4]},
    "residual_ties": {str(r): ns for r, ns in groups.items() if len(ns)>1},
    "first_numeric_inversion": next(
        [[a[1], a[4]], [b[1], b[4]]]
        for a, b in zip(ordered, ordered[1:]) if a[1] > b[1]),
    "timings": timings,
    "environment": {"python": sys.version.split()[0],
                    "implementation": platform.python_implementation(),
                    "machine": platform.machine()},
    "validation": "PASS: permutation, residual order, tie stability, reconstruction, bucket equivalence, boundaries",
}, ensure_ascii=False))
```

Run with the existing enterprise_math package available. In the current scratch runtime:

```sh
PYTHONPATH=/workspace/scratch/b0e94005ad9c/brc_sort_verification/src python brc_sort_verification/brc_residual_priority_experiment.py
```

## 7. Current frontier

The hundred-number experiment and its timing are complete **for the stated provisional comparator**. The user's intended BRC comparator is not inferred to be canonically settled. If it prioritizes a different residual, normalization, branch label, or recursive path order, reuse these input values and explicitly change the comparator before claiming the requested BRC order is complete.

Canonical identity/activity remains unconfirmed from the earlier terminal registration/reconciliation outcome; see bridge issue6652. This note is authorized draft persistence and does not assert session publication, ownership, mathematical admission, or shared task completion.
