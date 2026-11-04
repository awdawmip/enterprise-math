# 残差归类后数值升序：复杂度、专用算法与一个可验证的平方邻域捷径

Progress-Event-ID: `brc-classify-then-numeric-sort-20261105-b0e94005`
At: `2026-11-05T00:37:41+08:00`
Status: proved elementary reductions and an executed experimental implementation; not formal project admission or a general integer-sorting complexity breakthrough.
Conversation: `chat-brc-sort-b0e94005ad9c-20261103`.
Researcher-ID / Research-Activity-ID: unconfirmed under the previously reported terminal registration/reconciliation state.
Scientific source pin: `awdawmip/enterprise-math@9107f0215f7a724ff4117f8dac83712ec7ece698`.
GLOBAL_KNOWLEDGE read lease reused: `2827dbd8bdd216a1135fade833ca64144cd0c526`, actually verified 2026-11-04 10:58 UTC.

## 1. Current objective and correction

The user clarifies: “我的想法是，通过残差归类，再寻找从小到大的专用排序算法，能不能突破现有排序算法的复杂度”.

The final comparator is now explicitly numerical ascending order. BRC residual classification is an intermediate representation/algorithmic stage. This resolves the preceding ambiguity about “BRC order”; the previous residual-priority trial remains a useful intermediate-state experiment, not the final target. The 100 natural numbers within one million are a reproducible test case; asymptotic claims use variable n (record count) and U (maximum value).

The research question is which arithmetic structure reduces total work, including state extraction, classification, within-class ordering and global reconstruction. Comparison sorting, general integer sorting, distribution-specialized sorting, and implementation speed are distinct comparisons.

## 2. Primary literature and computation model

- [MIT 6.006, Lecture 7](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/bf7d79105762bf79bbc0925438e1468a_MIT6_006F11_lec07.pdf): the Omega(n log n) lower bound is in the comparison model. Integer addressing/digit operations enable counting/radix algorithms. Counting takes O(n+U); radix with base b takes O((n+b) ceil(log_b(U+1))). Polynomial-size universes permit linear word-RAM sorting.
- [Franceschini, Muthukrishnan, Patrascu, Radix Sorting With No Extra Space, ESA 2007](https://arxiv.org/abs/0706.4107): stable O(n) sorting for O(log n)-bit words, with constant auxiliary words.
- [Belazzougui, Brodal, Nielsen, SWAT 2014](https://cs.au.dk/~gerth/papers/swat14sort.pdf): representative general integer-sorting bounds and expected linear time under word size Omega(log²n log log n). Its introduction states the Han–Thorup expected O(n sqrt(log log n)) bound. These are cited as established results, not a claimed exhaustive November2026 frontier review.
- [Dong, Dhulipala, Gu, Sun, PPoPP 2024](https://www.cs.ucr.edu/~yihans/papers/2024/PPoPP24/integer-sort.pdf): parallel integer sorting theory/practice and exploiting duplicates. This is contextual evidence that structure-specialized improvements are useful; its work/span model is not being transferred to the sequential BRC prototype.

Unless otherwise specified, displayed structural costs count O(1)-word arithmetic, addressing and record moves. Exact integer root is represented by T_root(U), division by T_div(U). The standard word-RAM model does not automatically make an exact root primitive constant time. Python big-integer bit costs are not silently counted as unit bit operations.

For U<=1,000,000<2^20, ordinary radix bases128 and1024 require respectively3 and2 passes. These are relevant baselines for the concrete example.

## 3. Existing BRC implementation reused

[exact_arithmetic.py](https://github.com/awdawmip/enterprise-math/blob/9107f0215f7a724ff4117f8dac83712ec7ece698/src/enterprise_math/exact_arithmetic.py) supplies typed exact division and root traces. [core.py](https://github.com/awdawmip/enterprise-math/blob/9107f0215f7a724ff4117f8dac83712ec7ece698/src/enterprise_math/core.py) supplies integer roots by doubling/binary search.

Source reuse: REUSE_EXECUTED for brc_evaluate_root and brc_evaluate_division. Local modules have the same functional bytes as these immutable source blobs, with an extra trailing newline. The added anchored predictor is an experimental arithmetic specialization that emits an explicit BRCRootTrace after an exact basin certificate; it is not silently called the canonical implementation.

The similarly named brc_neighbor_square_lift_shortcut.py was inspected. It concerns multiplier/Fermat factor probes from local square divisors, rather than this batch-sorting anchor formula; it was not substituted for the required sorting computation.

This is ordinary natural-number BRC arithmetic. No native-X6 state or physical-time attribution is asserted.

## 4. Proven residual-first reconstruction

For x>=0 define k=floor(sqrt(x)) and r=x-k². Then 0<=r<=2k and numerical order is exactly lexicographic order on (k,r).

Proof: k_a<k_b implies a<(k_a+1)²<=k_b²<=b. Equal k reduces comparison to r. The converse follows by symmetry.

Consequently:
1. Stable counting by residual r.
2. Stable counting by root index k.
3. Emit original records.

This yields stable numerical ascending order. Residual classes need not themselves be disjoint numerical intervals; the second stable pass restores the correct basin priority.

Example input [102,99,101,121,100]:
- residual-first order: [121,100,101,102,99];
- subsequent stable root-index pass: [99,100,101,102,121].

Let B=k_max-k_min+1 and D=r_max-r_min+1. Offset counting arrays give

    T = n*T_root(U) + O(n+B+D),
    auxiliary records/counters = O(n+B+D).

The minima/maxima are obtained by linear scans. Since B+D=O(sqrt(U)+1), a dense global bound is n*T_root(U)+O(n+sqrt(U)). If B+D=O(n), the classification/reconstruction stage is linear. These bounds have no input-distribution assumption.

For the reused million-range random sample, B=918, D=1779. A separate structured near-square sample has B=20, D=8, while the ordinary numerical span is34569. Small B+D is therefore a concrete candidate structural parameter, not equivalent to small numerical span.

## 5. Random-input specialization via ordered BRC basins

### 5.1 Cubic basins

For x=k³+r, the intervals [k³,(k+1)³) are ordered. Group by k, stably sort r inside each group, concatenate groups by increasing k.

For independent uniform input from0..K^p-1, fixed p, bucket probabilities satisfy

    p_k=((k+1)^p-k^p)/K^p <= p/K.

If m_k is a bucket occupancy, independence gives

    E sum(m_k²) = n+n(n-1)sum(p_k²)
                 <= n+p*n(n-1)/K.

Insertion sorting within buckets and scanning the bucket array therefore have expected structural cost

    O(n+K+p*n²/K).

For fixed p and K=Theta(n), this is expected O(n), excluding root extraction. The worst case of this particular insertion-sort variant can still have quadratic within-bucket work.

For n100,U1,000,000,p3, buckets0..99 have widths3k²+3k+1; bucket100 contains the endpoint value1,000,000. Sampling is with replacement, so this endpoint bucket can contain repeated records. Exact values:

    sum(p_k²) = 178207921/9901009901
    E sum(m_k²) = 278.18974382823416

The actual sample used47 occupied cubic buckets, maximum load6, with93 local residual comparisons. These local comparisons exclude root computation and bucket management.

The existing source root implementation uses O(log(K+1)) doubling/binary-search rounds per root for fixed p, and the facade invokes root computation twice. At K=Theta(n), the current full cubic implementation still has an O(n log n) root-round upper bound. Sorting-stage linearity does not erase that cost.

### 5.2 Balanced division baseline

A more balanced baseline uses b=ceil((U+1)/n) and x=bq+r, computed with the existing BRC division facade. There are at most n nonempty-index positions in the global quotient range, and each bucket probability is at most b/(U+1). Under independent uniform inputs in a sufficiently large universe, local insertion sorting has expected O(n) work; the full cost is O(n*T_div(U)+n).

For the actual100-number sample, b=10001, occupied quotient buckets=61, maximum load=5, and local residual comparisons=47. This is a classical bucket-sorting construction expressed through the existing exact BRC arithmetic, included as a genuine baseline.

## 6. New derivation in this turn: one anchor root can replace per-item roots

Consider an explicitly structured family

    x=(K+j)²+e,
    0<=j<B, 0<=e<D, K>=1.

Assume

    (B-1)² + D-1 < 2K.                  (A)

Then j²+e<2K, so

    x-K² = 2K*j + j²+e,
    floor((x-K²)/(2K)) = j.             (B)

Thus one exact BRC division recovers the exact root index K+j; the canonical square residual is then x-(K+j)²=e. Condition(A) also ensures e<2K<=2(K+j)+1, so this is indeed the floor-root basin.

K need not be supplied by the data generator: compute the root of the minimum input once. If that changes the anchor from K to K+j_min, the remaining j span shrinks and the denominator2K grows; the same sufficient bound remains valid.

### Certified use on arbitrary natural inputs

The prototype computes a candidate

    khat = K + floor((x-K²)/(2K)),

then checks

    0 <= x-khat² < 2*khat+1.

This certificate is exactly khat²<=x<(khat+1)² and uniquely identifies floor(sqrt(x)). It emits an explicit BRCRootTrace when the check passes; otherwise it invokes the existing complete root facade.

For arbitrary x>=K² and its true root K+j, the candidate is never below the true root, since j²+r>=0. The two-sided basin certificate remains sufficient without relying on this observation. K=0 uses the source-root fallback to avoid division by zero. Repeated occurrences of the minimum reuse its valid trace while retaining original indices.

If f is the number of fallback records, the full structural/arithmetic cost is

    O(T_root(U) + n*T_div(U) + f*T_root(U) + n+B+D).

On the family satisfying(A), f=0. With constant-time single-word division and B+D=O(n), the bound becomes O(T_root(U)+n). If the anchor is already present it is O(n); if U is polynomial in n, the reference anchor-root O(log U) rounds are also absorbed by O(n). Large integer costs must be evaluated separately.

This is a sufficient-condition specialization and an exact certified predictor. It is not claimed to improve general integer-sorting bounds or to be globally novel. The useful result is that a specific residual structure removes almost all complete root calls while preserving the final sorting target.

### Executed specialization

For K900,B20,D8:

    (B-1)²+D-1 =368 <1800=2K.

On a separately generated100-number structured sample, the prototype used:
- full root evaluations: 1;
- division evaluations: 99;
- successful predictions: 99;
- fallbacks: 0.

The unchanged uniformly sampled million-range input had0 successful predictions and99 fallbacks. It does not satisfy the useful near-square-band structure. This is evidence to guide routing/adaptation, not a universal classification benefit.

Validation covered53 parameter families satisfying(A),26 general cases, and2896 values excluding the final two samples. Every computed state matched the existing root implementation; all certified families had zero fallback. Final stable numeric order was checked.

## 7. Actual performance, measured anew for the numerical-order objective

These are CPython prototype timings in microseconds per100-number batch, including validation/trace and Python-loop costs as implemented. Seven repeated batches were used; statistics are medians of per-call mean times. Network/tool delays are excluded. The standard-library sort and the Python-written prototypes have different implementation overhead, so this is a measurement of current implementations, not a controlled comparison at equal low-level optimization.

```json
{
  "numeric_python_sorted_end_to_end": {
    "median_us": 2.2038998009520583,
    "min_us": 2.1069921989692375,
    "max_us": 2.464517999032978,
    "repeat": 7,
    "number": 5000
  },
  "radix128_three_pass_end_to_end": {
    "median_us": 41.052796004805714,
    "min_us": 40.05610800231807,
    "max_us": 43.28577699925518,
    "repeat": 7,
    "number": 1000
  },
  "square_two_pass_given_brc_states": {
    "median_us": 112.70943999988958,
    "min_us": 111.50384400389157,
    "max_us": 138.79234199703205,
    "repeat": 7,
    "number": 500
  },
  "square_two_pass_end_to_end": {
    "median_us": 608.8245400314918,
    "min_us": 586.4566850141273,
    "max_us": 635.596779975458,
    "repeat": 7,
    "number": 200
  },
  "cube_bucket_given_brc_states": {
    "median_us": 36.6818010006682,
    "min_us": 34.4422010020935,
    "max_us": 38.690913999744225,
    "repeat": 7,
    "number": 1000
  },
  "cube_bucket_end_to_end": {
    "median_us": 449.83288000366883,
    "min_us": 432.0155200184672,
    "max_us": 492.6441600036924,
    "repeat": 7,
    "number": 200
  },
  "division_bucket_given_brc_states": {
    "median_us": 34.64605799672427,
    "min_us": 34.12598499562591,
    "max_us": 37.32986599789001,
    "repeat": 7,
    "number": 1000
  },
  "division_bucket_end_to_end": {
    "median_us": 235.48830999061465,
    "min_us": 232.16020332862777,
    "max_us": 242.84841667395085,
    "repeat": 7,
    "number": 300
  },
  "near_square_two_pass_given_brc_states": {
    "median_us": 29.874206004024018,
    "min_us": 29.637571002240293,
    "max_us": 31.570118000672668,
    "repeat": 7,
    "number": 1000
  },
  "near_square_two_pass_end_to_end": {
    "median_us": 579.8818800030858,
    "min_us": 531.9921249974868,
    "max_us": 642.7053350125789,
    "repeat": 7,
    "number": 200
  },
  "near_square_python_sorted_end_to_end": {
    "median_us": 2.4715225998079404,
    "min_us": 2.3807220000890084,
    "max_us": 2.7047736002714373,
    "repeat": 7,
    "number": 5000
  }
}
```

The original random sample's complete BRC prototypes are slower than the current standard-library baseline. The measurement identifies state extraction and record construction as significant work and keeps the baseline honest.

On the separate structured sample the anchored specialization reduced its own complete reference pipeline from546.177us to395.047us, a27.67% reduction. Standard-library sorting on that sample took2.272us.

## 8. Complete algorithm and reproduction code

Save the first block as residual_classification_numeric_sort.py and the second as anchored_square_residual_sort.py in the same directory, with the source-pinned enterprise_math package on PYTHONPATH.

```python
"""Residual classification followed by final numerical order.

Uses the existing BRC root/division facade for all scientific decompositions.
The elementary radix comparator is a separate integer-sort baseline.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import ceil
from operator import itemgetter
import json
import random
import statistics
import timeit

from enterprise_math.exact_arithmetic import (
    root, division, brc_evaluate_root, brc_evaluate_division,
)

UPPER = 1_000_000
SEED = 20261104
# State: (original value, coarse index, residual, original position).


def root_states(values, degree):
    result = []
    for i, value in enumerate(values):
        trace = brc_evaluate_root(root(value, degree))
        result.append((value, trace.root_index, trace.remainder, i))
    return result


def division_states(values, upper):
    if not values:
        return [], 1
    n = len(values)
    width = brc_evaluate_division(division(upper+n, n)).quotient
    width = max(width, 1)
    result = []
    for i, value in enumerate(values):
        trace = brc_evaluate_division(division(value, width))
        result.append((value, trace.quotient, trace.remainder, i))
    return result, width


def stable_count(records, column, low, high):
    counts = [0] * (high-low+1)
    for row in records:
        counts[row[column]-low] += 1
    offset = 0
    for j, count in enumerate(counts):
        counts[j] = offset
        offset += count
    out = [None] * len(records)
    for row in records:
        digit = row[column]-low
        out[counts[digit]] = row
        counts[digit] += 1
    return out


def square_residual_then_basin(records):
    if not records:
        return []
    rlow = min(row[2] for row in records)
    rhigh = max(row[2] for row in records)
    klow = min(row[1] for row in records)
    khigh = max(row[1] for row in records)
    stage1 = stable_count(records, 2, rlow, rhigh)
    return stable_count(stage1, 1, klow, khigh)


def basin_then_local_residual(records):
    if not records:
        return [], {"bins": 0, "occupied": 0, "max_occupancy": 0,
                    "local_residual_comparisons": 0, "sum_occupancy_squared": 0}
    low = min(row[1] for row in records)
    high = max(row[1] for row in records)
    buckets = [[] for _ in range(high-low+1)]
    for row in records:
        buckets[row[1]-low].append(row)
    comparisons = 0
    for bucket in buckets:
        for j in range(1, len(bucket)):
            item = bucket[j]
            pos = j
            while pos:
                comparisons += 1
                if bucket[pos-1][2] <= item[2]:
                    break
                bucket[pos] = bucket[pos-1]
                pos -= 1
            bucket[pos] = item
    out = [row for bucket in buckets for row in bucket]
    return out, {
        "bins": len(buckets),
        "occupied": sum(bool(b) for b in buckets),
        "max_occupancy": max(map(len, buckets), default=0),
        "local_residual_comparisons": comparisons,
        "sum_occupancy_squared": sum(len(b)**2 for b in buckets),
    }


def radix128(values):
    out = list(values)
    if not out:
        return out
    for shift in (0, 7, 14):
        counts = [0] * 128
        for value in out:
            counts[(value >> shift) & 127] += 1
        offset = 0
        for i, count in enumerate(counts):
            counts[i] = offset
            offset += count
        target = [0] * len(out)
        for value in out:
            digit = (value >> shift) & 127
            target[counts[digit]] = value
            counts[digit] += 1
        out = target
    return out


def check(values, upper):
    expected = sorted(range(len(values)), key=values.__getitem__)
    square = root_states(values, 2)
    cube = root_states(values, 3)
    div, _ = division_states(values, upper)
    for result in (square_residual_then_basin(square),
                   basin_then_local_residual(cube)[0],
                   basin_then_local_residual(div)[0]):
        assert [row[3] for row in result] == expected, (values, result)
    assert radix128(values) == sorted(values)


def measure(fn, number):
    per_batch_us = [t/number*1e6 for t in timeit.repeat(fn, repeat=7, number=number)]
    return {"median_us": statistics.median(per_batch_us),
            "min_us": min(per_batch_us), "max_us": max(per_batch_us),
            "repeat": 7, "number": number}


def run_experiment():
    exhaustive = 0
    for length in range(6):
        for data in product((0, 1, 7, 8), repeat=length):
            check(list(data), 8)
            exhaustive += 1
    
    rng = random.Random(SEED)
    sample = [rng.randrange(UPPER+1) for _ in range(100)]
    for _ in range(60):
        values = [rng.randrange(UPPER+1) for _ in range(100)]
        check(values, UPPER)
    
    edge_cases = [
        [], [0]*100, [UPPER]*100,
        [0,1,2,3,4,7,8,9,26,27,28,999_998,999_999,UPPER],
        list(range(100)), list(range(99,-1,-1)),
        [999_999]*100,
    ]
    for values in edge_cases:
        check(values, UPPER)
    
    near_square = [(900+rng.randrange(20))**2+rng.randrange(8)
                   for _ in range(100)]
    check(sample, UPPER)
    check(near_square, UPPER)
    
    sq = root_states(sample, 2)
    cb = root_states(sample, 3)
    dv, div_width = division_states(sample, UPPER)
    sq_near = root_states(near_square, 2)
    cube_ordered, cube_stats = basin_then_local_residual(cb)
    div_ordered, div_stats = basin_then_local_residual(dv)
    square_stats = {
        "basin_span_B": max(r[1] for r in sq)-min(r[1] for r in sq)+1,
        "residual_span_D": max(r[2] for r in sq)-min(r[2] for r in sq)+1,
    }
    near_stats = {
        "basin_span_B": max(r[1] for r in sq_near)-min(r[1] for r in sq_near)+1,
        "residual_span_D": max(r[2] for r in sq_near)-min(r[2] for r in sq_near)+1,
        "numeric_span": max(near_square)-min(near_square)+1,
    }
    
    timings = {
        "numeric_python_sorted_end_to_end": measure(lambda: sorted(sample), 5000),
        "radix128_three_pass_end_to_end": measure(lambda: radix128(sample), 1000),
        "square_two_pass_given_brc_states": measure(lambda: square_residual_then_basin(sq), 500),
        "square_two_pass_end_to_end": measure(
            lambda: square_residual_then_basin(root_states(sample, 2)), 200),
        "cube_bucket_given_brc_states": measure(lambda: basin_then_local_residual(cb), 1000),
        "cube_bucket_end_to_end": measure(
            lambda: basin_then_local_residual(root_states(sample, 3)), 200),
        "division_bucket_given_brc_states": measure(lambda: basin_then_local_residual(dv), 1000),
        "division_bucket_end_to_end": measure(
            lambda: basin_then_local_residual(division_states(sample, UPPER)[0]), 300),
        "near_square_two_pass_given_brc_states": measure(
            lambda: square_residual_then_basin(sq_near), 1000),
        "near_square_two_pass_end_to_end": measure(
            lambda: square_residual_then_basin(root_states(near_square, 2)), 200),
        "near_square_python_sorted_end_to_end": measure(lambda: sorted(near_square), 5000),
    }
    
    widths = [(k+1)**3-k**3 for k in range(100)] + [1]
    sum_probability_squared = sum(Fraction(width, UPPER+1)**2 for width in widths)
    expected_energy = 100 + 100*99*sum_probability_squared
    
    print(json.dumps({
        "input": sample, "sorted_values": sorted(sample),
        "cube_stats": cube_stats, "division_stats": div_stats,
        "division_width": div_width, "square_stats": square_stats,
        "near_square_stats": near_stats,
        "cube_uniform_probability_squared": str(sum_probability_squared),
        "cube_expected_sum_occupancy_squared": float(expected_energy),
        "timings": timings,
        "verification": {"exhaustive_arrays": exhaustive, "random_100_arrays": 60,
                         "edge_cases": len(edge_cases), "sample_and_structured": 2,
                         "result": "PASS for stable numerical order"},
    }, ensure_ascii=False))


if __name__ == '__main__':
    run_experiment()
```

```python
"""Certified anchored square-state predictor for structured natural inputs.

Experimental BRC arithmetic specialization: one anchor root, exact division
traces, exact root-basin certificate, and source-root fallback when needed.
"""
import json
import random
from enterprise_math.exact_arithmetic import (
    root, division, brc_evaluate_root, brc_evaluate_division, BRCRootTrace,
)
from residual_classification_numeric_sort import (
    root_states, square_residual_then_basin, measure,
)

def brc_anchored_square_states(values):
    values = list(values)
    if any(isinstance(x, bool) or not isinstance(x, int) or x < 0 for x in values):
        raise ValueError("non-negative integers required")
    stats = {"full_root_calls": 0, "division_calls": 0, "prediction_hits": 0,
             "anchor_reuses": 0, "fallbacks": 0, "anchor_root": None}
    if not values:
        return [], stats
    anchor_value = min(values)
    anchor = brc_evaluate_root(root(anchor_value, 2))
    stats["full_root_calls"] = 1
    stats["anchor_root"] = anchor.root_index
    K = anchor.root_index
    rows = []
    for i, value in enumerate(values):
        if value == anchor_value:
            trace = anchor
            stats["anchor_reuses"] += 1
        elif K == 0:
            trace = brc_evaluate_root(root(value, 2))
            stats["full_root_calls"] += 1
            stats["fallbacks"] += 1
        else:
            prediction = brc_evaluate_division(
                division(value-anchor.collapsed_radicand, 2*K))
            stats["division_calls"] += 1
            candidate = K + prediction.quotient
            collapsed = candidate*candidate
            residual = value-collapsed
            if 0 <= residual < 2*candidate+1:
                trace = BRCRootTrace(
                    radicand=value, degree=2, root_index=candidate,
                    collapsed_radicand=collapsed, remainder=residual,
                    next_power=(candidate+1)*(candidate+1),
                    evaluation_kind="BRC_ANCHORED_SQUARE_ROOT_EVALUATION",
                )
                stats["prediction_hits"] += 1
            else:
                trace = brc_evaluate_root(root(value, 2))
                stats["full_root_calls"] += 1
                stats["fallbacks"] += 1
        rows.append((value, trace.root_index, trace.remainder, i))
    return rows, stats


def brc_anchored_square_sort(values):
    rows, stats = brc_anchored_square_states(values)
    return square_residual_then_basin(rows), stats


def run_experiment():
    verified = 0
    certified_families = 0
    maximum_certified_fallbacks = 0
    rng = random.Random(20261105)

    for K in (1, 2, 3, 10, 100, 900, 10**9):
        for B in (1, 2, 4, 20):
            for D in (1, 2, 8):
                if (B-1)**2+D-1 >= 2*K:
                    continue
                values = [(K+j)**2+e for j in range(B) for e in range(D)]
                rng.shuffle(values)
                rows, stats = brc_anchored_square_states(values)
                assert rows == root_states(values, 2)
                assert stats["fallbacks"] == 0
                maximum_certified_fallbacks = max(maximum_certified_fallbacks,
                                                 stats["fallbacks"])
                certified_families += 1
                verified += len(values)

    generic_cases = [
        [], [0]*100, [0, 1, 7, 8, 9, 1_000_000],
        [81, 99, 100, 120, 121],
        [900**2, 900**2+1799, 900**2+1800, 901**2],
        [1, 2, 3, 4, 8, 9, 15, 16, 24, 25],
    ]
    for _ in range(20):
        generic_cases.append([rng.randrange(1_000_001) for _ in range(100)])

    for values in generic_cases:
        rows, stats = brc_anchored_square_states(values)
        assert rows == root_states(values, 2)
        ordered = square_residual_then_basin(rows)
        assert [r[3] for r in ordered] == sorted(range(len(values)), key=values.__getitem__)
        verified += len(values)

    uniform_rng = random.Random(20261104)
    uniform = [uniform_rng.randrange(1_000_001) for _ in range(100)]
    structured_rng = random.Random(20261105)
    structured = [(900+structured_rng.randrange(20))**2+structured_rng.randrange(8)
                  for _ in range(100)]
    uniform_rows, uniform_stats = brc_anchored_square_states(uniform)
    structured_rows, structured_stats = brc_anchored_square_states(structured)
    assert uniform_rows == root_states(uniform, 2)
    assert structured_rows == root_states(structured, 2)
    ordered, _ = brc_anchored_square_sort(structured)
    assert [r[0] for r in ordered] == sorted(structured)

    timings = {
        "structured_reference_root_then_two_pass": measure(
            lambda: square_residual_then_basin(root_states(structured, 2)), 200),
        "structured_anchored_root_then_two_pass": measure(
            lambda: brc_anchored_square_sort(structured), 300),
        "structured_python_sorted": measure(lambda: sorted(structured), 5000),
    }
    print(json.dumps({
        "condition": "(B-1)^2+D-1 < 2K",
        "certified_families": certified_families,
        "generic_cases": len(generic_cases),
        "verified_values_excluding_final_samples": verified,
        "maximum_certified_fallbacks": maximum_certified_fallbacks,
        "uniform_stats": uniform_stats,
        "structured_parameters": {"K": 900, "B": 20, "D": 8,
                                  "left_bound": 368, "right_bound": 1800},
        "structured_stats": structured_stats,
        "structured_values": structured,
        "structured_sorted_values": [row[0] for row in ordered],
        "timings": timings,
        "validation": "PASS: exact source-state equality, stable numerical order, zero certified fallback",
    }, ensure_ascii=False))

if __name__ == "__main__":
    run_experiment()
```

The initial module-import issue after extracting the benchmark helper was corrected by placing measure at module scope; the successful anchored experiment ran after that correction. No mathematical output is based on the aborted import.

## 9. Exact experiment receipts

Core sorting experiment:

```json
{
  "input": [
    776669,
    662511,
    219200,
    338659,
    388826,
    523002,
    620061,
    21207,
    239119,
    406150,
    6832,
    680904,
    903234,
    567856,
    614522,
    854859,
    983043,
    649315,
    726747,
    77213,
    479627,
    393880,
    918633,
    29715,
    470043,
    911431,
    716362,
    168020,
    904033,
    573868,
    494099,
    740040,
    250943,
    876000,
    881624,
    852793,
    898562,
    120952,
    815627,
    299640,
    722386,
    305300,
    223078,
    116502,
    807433,
    715643,
    335088,
    577156,
    528271,
    522144,
    861438,
    551401,
    819148,
    517371,
    404338,
    557580,
    473827,
    328238,
    190261,
    775183,
    436400,
    784253,
    221317,
    160791,
    633460,
    231052,
    712313,
    38027,
    999249,
    941354,
    558476,
    330879,
    757660,
    516141,
    542427,
    12511,
    853348,
    536321,
    368551,
    517871,
    399456,
    458655,
    203314,
    259040,
    867863,
    691595,
    890000,
    846822,
    545134,
    827510,
    816750,
    13005,
    552596,
    784689,
    482193,
    559888,
    233389,
    578371,
    325011,
    802462
  ],
  "sorted_values": [
    6832,
    12511,
    13005,
    21207,
    29715,
    38027,
    77213,
    116502,
    120952,
    160791,
    168020,
    190261,
    203314,
    219200,
    221317,
    223078,
    231052,
    233389,
    239119,
    250943,
    259040,
    299640,
    305300,
    325011,
    328238,
    330879,
    335088,
    338659,
    368551,
    388826,
    393880,
    399456,
    404338,
    406150,
    436400,
    458655,
    470043,
    473827,
    479627,
    482193,
    494099,
    516141,
    517371,
    517871,
    522144,
    523002,
    528271,
    536321,
    542427,
    545134,
    551401,
    552596,
    557580,
    558476,
    559888,
    567856,
    573868,
    577156,
    578371,
    614522,
    620061,
    633460,
    649315,
    662511,
    680904,
    691595,
    712313,
    715643,
    716362,
    722386,
    726747,
    740040,
    757660,
    775183,
    776669,
    784253,
    784689,
    802462,
    807433,
    815627,
    816750,
    819148,
    827510,
    846822,
    852793,
    853348,
    854859,
    861438,
    867863,
    876000,
    881624,
    890000,
    898562,
    903234,
    904033,
    911431,
    918633,
    941354,
    983043,
    999249
  ],
  "cube_stats": {
    "bins": 82,
    "occupied": 47,
    "max_occupancy": 6,
    "local_residual_comparisons": 93,
    "sum_occupancy_squared": 312
  },
  "division_stats": {
    "bins": 100,
    "occupied": 61,
    "max_occupancy": 5,
    "local_residual_comparisons": 47,
    "sum_occupancy_squared": 206
  },
  "division_width": 10001,
  "square_stats": {
    "basin_span_B": 918,
    "residual_span_D": 1779
  },
  "near_square_stats": {
    "basin_span_B": 20,
    "residual_span_D": 8,
    "numeric_span": 34569
  },
  "cube_uniform_probability_squared": "178207921/9901009901",
  "cube_expected_sum_occupancy_squared": 278.18974382823416,
  "timings": {
    "numeric_python_sorted_end_to_end": {
      "median_us": 2.2038998009520583,
      "min_us": 2.1069921989692375,
      "max_us": 2.464517999032978,
      "repeat": 7,
      "number": 5000
    },
    "radix128_three_pass_end_to_end": {
      "median_us": 41.052796004805714,
      "min_us": 40.05610800231807,
      "max_us": 43.28577699925518,
      "repeat": 7,
      "number": 1000
    },
    "square_two_pass_given_brc_states": {
      "median_us": 112.70943999988958,
      "min_us": 111.50384400389157,
      "max_us": 138.79234199703205,
      "repeat": 7,
      "number": 500
    },
    "square_two_pass_end_to_end": {
      "median_us": 608.8245400314918,
      "min_us": 586.4566850141273,
      "max_us": 635.596779975458,
      "repeat": 7,
      "number": 200
    },
    "cube_bucket_given_brc_states": {
      "median_us": 36.6818010006682,
      "min_us": 34.4422010020935,
      "max_us": 38.690913999744225,
      "repeat": 7,
      "number": 1000
    },
    "cube_bucket_end_to_end": {
      "median_us": 449.83288000366883,
      "min_us": 432.0155200184672,
      "max_us": 492.6441600036924,
      "repeat": 7,
      "number": 200
    },
    "division_bucket_given_brc_states": {
      "median_us": 34.64605799672427,
      "min_us": 34.12598499562591,
      "max_us": 37.32986599789001,
      "repeat": 7,
      "number": 1000
    },
    "division_bucket_end_to_end": {
      "median_us": 235.48830999061465,
      "min_us": 232.16020332862777,
      "max_us": 242.84841667395085,
      "repeat": 7,
      "number": 300
    },
    "near_square_two_pass_given_brc_states": {
      "median_us": 29.874206004024018,
      "min_us": 29.637571002240293,
      "max_us": 31.570118000672668,
      "repeat": 7,
      "number": 1000
    },
    "near_square_two_pass_end_to_end": {
      "median_us": 579.8818800030858,
      "min_us": 531.9921249974868,
      "max_us": 642.7053350125789,
      "repeat": 7,
      "number": 200
    },
    "near_square_python_sorted_end_to_end": {
      "median_us": 2.4715225998079404,
      "min_us": 2.3807220000890084,
      "max_us": 2.7047736002714373,
      "repeat": 7,
      "number": 5000
    }
  },
  "verification": {
    "exhaustive_arrays": 1365,
    "random_100_arrays": 60,
    "edge_cases": 7,
    "sample_and_structured": 2,
    "result": "PASS for stable numerical order"
  }
}
```

Anchored predictor experiment:

```json
{
  "condition": "(B-1)^2+D-1 < 2K",
  "certified_families": 53,
  "generic_cases": 26,
  "verified_values_excluding_final_samples": 2896,
  "maximum_certified_fallbacks": 0,
  "uniform_stats": {
    "full_root_calls": 100,
    "division_calls": 99,
    "prediction_hits": 0,
    "anchor_reuses": 1,
    "fallbacks": 99,
    "anchor_root": 82
  },
  "structured_parameters": {
    "K": 900,
    "B": 20,
    "D": 8,
    "left_bound": 368,
    "right_bound": 1800
  },
  "structured_stats": {
    "full_root_calls": 1,
    "division_calls": 99,
    "prediction_hits": 99,
    "anchor_reuses": 1,
    "fallbacks": 0,
    "anchor_root": 900
  },
  "structured_values": [
    817218,
    844562,
    833571,
    833573,
    819032,
    844566,
    819027,
    810004,
    824469,
    811808,
    813611,
    842726,
    837227,
    840895,
    815416,
    824470,
    811808,
    811808,
    835402,
    844566,
    844563,
    822650,
    822649,
    844561,
    820837,
    831748,
    831744,
    817223,
    840893,
    839060,
    828104,
    831748,
    813607,
    813605,
    833569,
    822651,
    813608,
    835401,
    817222,
    826281,
    813606,
    828100,
    811807,
    810005,
    837231,
    844566,
    815412,
    837231,
    844562,
    810002,
    842728,
    819032,
    826285,
    833573,
    829928,
    833575,
    820841,
    829922,
    811801,
    839058,
    833573,
    844568,
    839063,
    828100,
    822654,
    839060,
    826283,
    811805,
    844564,
    828103,
    810001,
    844567,
    820838,
    828100,
    831744,
    839063,
    822651,
    828105,
    829925,
    828107,
    824468,
    833576,
    813608,
    817220,
    842728,
    840896,
    817222,
    844562,
    844567,
    839058,
    829923,
    844565,
    835403,
    835400,
    833575,
    817220,
    844565,
    826284,
    826283,
    840892
  ],
  "structured_sorted_values": [
    810001,
    810002,
    810004,
    810005,
    811801,
    811805,
    811807,
    811808,
    811808,
    811808,
    813605,
    813606,
    813607,
    813608,
    813608,
    813611,
    815412,
    815416,
    817218,
    817220,
    817220,
    817222,
    817222,
    817223,
    819027,
    819032,
    819032,
    820837,
    820838,
    820841,
    822649,
    822650,
    822651,
    822651,
    822654,
    824468,
    824469,
    824470,
    826281,
    826283,
    826283,
    826284,
    826285,
    828100,
    828100,
    828100,
    828103,
    828104,
    828105,
    828107,
    829922,
    829923,
    829925,
    829928,
    831744,
    831744,
    831748,
    831748,
    833569,
    833571,
    833573,
    833573,
    833573,
    833575,
    833575,
    833576,
    835400,
    835401,
    835402,
    835403,
    837227,
    837231,
    837231,
    839058,
    839058,
    839060,
    839060,
    839063,
    839063,
    840892,
    840893,
    840895,
    840896,
    842726,
    842728,
    842728,
    844561,
    844562,
    844562,
    844562,
    844563,
    844564,
    844565,
    844565,
    844566,
    844566,
    844566,
    844567,
    844567,
    844568
  ],
  "timings": {
    "structured_reference_root_then_two_pass": {
      "median_us": 546.1768500026665,
      "min_us": 532.7140950248577,
      "max_us": 575.2092850161716,
      "repeat": 7,
      "number": 200
    },
    "structured_anchored_root_then_two_pass": {
      "median_us": 395.04721668587683,
      "min_us": 390.5731033106955,
      "max_us": 438.3015966595849,
      "repeat": 7,
      "number": 300
    },
    "structured_python_sorted": {
      "median_us": 2.271699800621718,
      "min_us": 2.1755773996119387,
      "max_us": 3.461071399215143,
      "repeat": 7,
      "number": 5000
    }
  },
  "validation": "PASS: exact source-state equality, stable numerical order, zero certified fallback"
}
```

The baseline sorting validation consists of1365 exhaustive arrays,60 arrays of100 random naturals,7 edge cases and2 exact/structured samples:1434 arrays total, each verified for stable numerical output. The predictor checks are additional.

## 10. Research frontier

Completed:
- final-objective correction: residual classification is intermediate; output is numerical order;
- correct stable two-pass reconstruction and the B+D complexity parameter;
- cubic random-bucket expectation, with exact root costs retained;
- a concrete anchored-square sufficient condition that removes per-item full roots;
- actual reference execution, independent mathematical review, and reproducible measurements.

The next useful improvement target is an adaptive residual mechanism with cheap classification, ordered reconstruction and a provable small exceptional set. This can be evaluated on structured families and against both comparison and integer-radix baselines. A separate general integer-sorting breakthrough would require a bound in the same model and for the same input class as the corresponding published results.

No formal Task-ID, CLAIM, Result, Review or admission was created by this research note. Identity/activity remains unconfirmed under the previously recorded bridge outcome; authorized research reporting and draft preservation follow the portable research protocol.
