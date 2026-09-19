from __future__ import annotations

import argparse
import json
import math
import sys
from collections import Counter
from functools import lru_cache
from pathlib import Path

# Reproduced from awdawmip/Nollm main 88d63b32329fbbcd18028de1ac83b2db3c988e33
# packages/nollm-core/src/nollm_core/approximate_coverage.py
# blob fb1f19515b888ed9f01417b5e857c2146c418a66
Q40 = 1 << 40
Q16 = 1 << 16
SAMPLE_SUBDIVISION = 4
SAMPLE_COUNT = 96
TRANSFORMS = {
    "coverage_up": (
        649918386859, -408555777664, 408555777664, 1058474164523,
        375230555604, -489009980729, 235879788213, 569464183794,
    ),
    "coverage_down": (
        1496908518890, 577785121758, -577785121758, 919123397132,
        864240536333, -113779425125, -333584395581, 805343972007,
    ),
}
HEX_VERTICES_Q40 = (
    (952205001410, 549755813888), (0, 1099511627776),
    (-952205001410, 549755813888), (-952205001410, -549755813888),
    (0, -1099511627776), (952205001410, -549755813888),
)
HEX_DIRS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))


def hdist(a, b=(0, 0)):
    dq, dr = a[0] - b[0], a[1] - b[1]
    return max(abs(dq), abs(dr), abs(dq + dr))


def ring_cells(radius: int):
    if radius <= 0:
        raise ValueError("radius must be positive")
    q, r = 0, -radius
    out = []
    for dq, dr in HEX_DIRS:
        for _ in range(radius):
            out.append((q, r))
            q += dq
            r += dr
    assert (q, r) == (0, -radius)
    assert len(out) == 6 * radius
    assert all(hdist(x) == radius for x in out)
    assert all(hdist(out[i], out[(i + 1) % len(out)]) == 1 for i in range(len(out)))
    return tuple(out)


def ring_cell(radius: int, index: int):
    """O(1) cell lookup in exactly the same cyclic order as ring_cells()."""
    if radius <= 0:
        raise ValueError("radius must be positive")
    j = index % (6 * radius)
    side, u = divmod(j, radius)
    if side == 0: return u, -radius
    if side == 1: return radius, -radius + u
    if side == 2: return radius - u, u
    if side == 3: return -u, radius
    if side == 4: return -radius, radius - u
    return -radius + u, -u


def dlog_table(b: int):
    M, Q = 1 << b, 1 << (b + 2)
    table = {}
    x = 1
    for t in range(M):
        table[x] = t
        x = x * 5 % Q
    assert len(table) == M and x == 1
    return table


def carrier(n: int, b: int, table):
    if n <= 0:
        raise ValueError("positive n required")
    Q = 1 << (b + 2)
    v = (n & -n).bit_length() - 1
    u = (n >> v) % Q
    eps = 0 if u % 4 == 1 else 1
    a = u if eps == 0 else (-u) % Q
    return v, eps, table[a]


def unique_carrier_formula(L: int, b: int):
    if not (0 <= b <= L - 2):
        raise ValueError
    return (L - b) * (1 << (b + 1)) - 1


def max_fiber_formula(L: int, b: int):
    return 1 << max(0, L - b - 2)


def annulus_state(M: int, R0: int, h: int, t: int):
    radius = R0 + h
    j = (t * (6 * radius)) // M
    return ring_cell(radius, j)


def build_realized(N: int, b: int):
    M = 1 << b
    table = dlog_table(b)
    R0 = (M + 5) // 6
    carr = [None]
    for n in range(1, N):
        carr.append(carrier(n, b, table))
    max_h = max(2 * v + e for v, e, _ in carr[1:])
    coords = [None]
    for v, e, t in carr[1:]:
        coords.append(annulus_state(M, R0, 2 * v + e, t))
    return M, R0, carr, coords, max_h


def round_ratio(numerator: int, denominator: int):
    sign = -1 if numerator < 0 else 1
    quotient, remainder = divmod(abs(numerator), denominator)
    doubled = remainder * 2
    if doubled > denominator or (doubled == denominator and quotient % 2):
        quotient += 1
    return sign * quotient


def centroid(first, second, fw, sw, denominator):
    return (
        round_ratio(fw * first[0] + sw * second[0], denominator),
        round_ratio(fw * first[1] + sw * second[1], denominator),
    )


@lru_cache(maxsize=1)
def sample_offsets_q40():
    denominator = 3 * SAMPLE_SUBDIVISION
    out = []
    for sector, first in enumerate(HEX_VERTICES_Q40):
        second = HEX_VERTICES_Q40[(sector + 1) % 6]
        for i in range(SAMPLE_SUBDIVISION):
            for j in range(SAMPLE_SUBDIVISION - i):
                out.append(centroid(first, second, 3 * i + 1, 3 * j + 1, denominator))
        for i in range(SAMPLE_SUBDIVISION - 1):
            for j in range(SAMPLE_SUBDIVISION - 1 - i):
                out.append(centroid(first, second, 3 * i + 2, 3 * j + 2, denominator))
    assert len(out) == SAMPLE_COUNT
    return tuple(out)


@lru_cache(maxsize=2)
def compiled_offsets(direction):
    m = TRANSFORMS[direction]
    return tuple(
        (
            round_ratio(m[4] * x + m[5] * y, Q40),
            round_ratio(m[6] * x + m[7] * y, Q40),
        )
        for x, y in sample_offsets_q40()
    )


def nearest_axial_q40(q_fixed, r_fixed):
    x_fixed, z_fixed, y_fixed = q_fixed, r_fixed, -q_fixed - r_fixed
    x = round_ratio(x_fixed, Q40)
    z = round_ratio(z_fixed, Q40)
    y = round_ratio(y_fixed, Q40)
    dx = abs(x * Q40 - x_fixed)
    dz = abs(z * Q40 - z_fixed)
    dy = abs(y * Q40 - y_fixed)
    if dx >= dz and dx >= dy:
        x = -y - z
    elif dz >= dy:
        z = -x - y
    return x, z


@lru_cache(maxsize=8192)
def phase_footprint(direction, phase_q, phase_r):
    counts = {}
    for qo, ro in compiled_offsets(direction):
        target = nearest_axial_q40(phase_q + qo, phase_r + ro)
        counts[target] = counts.get(target, 0) + 1
    return tuple((q, r, count) for (q, r), count in sorted(counts.items()))


@lru_cache(maxsize=8192)
def expand_hits(q, r, direction):
    m = TRANSFORMS[direction]
    cq = m[0] * q + m[1] * r
    cr = m[2] * q + m[3] * r
    bq, pq = divmod(cq, 2 * Q40)
    br, pr = divmod(cr, 2 * Q40)
    aq, ar = 2 * bq, 2 * br
    hits = {(aq + qq, ar + rr): count for qq, rr, count in phase_footprint(direction, pq, pr)}
    assert sum(hits.values()) == SAMPLE_COUNT
    return hits


def normalize_q16(raw):
    total = sum(raw)
    result = [(x * Q16) // total for x in raw]
    order = sorted(range(len(raw)), key=lambda i: (-((raw[i] * Q16) % total), i))
    for i in order[: Q16 - sum(result)]:
        result[i] += 1
    return tuple(result)


@lru_cache(maxsize=8192)
def expand_q16(q, r, direction):
    hits = expand_hits(q, r, direction)
    items = sorted(hits.items())
    weights = normalize_q16([count for _target, count in items])
    return tuple((target, weight, count) for (target, count), weight in zip(items, weights))


@lru_cache(maxsize=8192)
def support2(q, r, direction):
    # Support-only observer: MIN_HIT_COUNT=1 in the published contract, so Q16
    # normalization is irrelevant to target membership and is intentionally not
    # evaluated here. Exact hit-count identities remain available separately.
    result = set()
    for mid in expand_hits(q, r, direction):
        result.update(expand_hits(mid[0], mid[1], direction))
    return frozenset(result)

def clear_coverage_caches():
    phase_footprint.cache_clear()
    expand_hits.cache_clear()
    expand_q16.cache_clear()
    support2.cache_clear()


def support_distance_metrics(A, B):
    """Return min support distance and Hausdorff distance in one pair scan."""
    A = tuple(A); B = tuple(B)
    min_a = [1 << 60] * len(A)
    min_b = [1 << 60] * len(B)
    minimum = 1 << 60
    for i, x in enumerate(A):
        xq, xr = x
        best_a = min_a[i]
        for j, y in enumerate(B):
            dq, dr = xq - y[0], xr - y[1]
            d = max(abs(dq), abs(dr), abs(dq + dr))
            if d < best_a: best_a = d
            if d < min_b[j]: min_b[j] = d
            if d < minimum: minimum = d
        min_a[i] = best_a
    return minimum, max(max(min_a), max(min_b))


def relation_stats_range(coords, k, direction, steps, lo, hi):
    overlap = 0
    mind = Counter()
    hd = Counter()
    count = 0
    stop = min(hi, (len(coords) - 1) // k + 1)
    for n in range(lo, stop):
        a, b = coords[n], coords[k * n]
        if steps == 1:
            A = expand_hits(a[0], a[1], direction).keys()
            B = expand_hits(b[0], b[1], direction).keys()
        else:
            A = support2(a[0], a[1], direction)
            B = support2(b[0], b[1], direction)
        dmin, dh = support_distance_metrics(A, B)
        overlap += dmin == 0
        mind[dmin] += 1
        hd[dh] += 1
        count += 1
        if count % 2048 == 0:
            clear_coverage_caches()
    return {
        "pairs": count,
        "overlap_count": overlap,
        "minimum_support_distance_histogram": dict(sorted(mind.items())),
        "hausdorff_histogram": dict(sorted(hd.items())),
    }


def _combine_relation_chunks(chunks):
    pairs = sum(x["pairs"] for x in chunks)
    overlap = sum(x["overlap_count"] for x in chunks)
    mind, hd = Counter(), Counter()
    for x in chunks:
        mind.update({int(k): v for k, v in x["minimum_support_distance_histogram"].items()})
        hd.update({int(k): v for k, v in x["hausdorff_histogram"].items()})
    return {
        "pairs": pairs,
        "overlap_count": overlap,
        "overlap_ratio": overlap / pairs,
        "minimum_support_distance_histogram": dict(sorted(mind.items())),
        "hausdorff_histogram": dict(sorted(hd.items())),
        "max_hausdorff": max(hd),
    }


def annulus_theorem_check(M: int, max_h: int):
    R0 = (M + 5) // 6
    if 6 * (R0 + max_h) >= 2 * M:
        raise ValueError("declared t-step <=2 regime not satisfied")
    # The O(1) formula is certified against the constructive enumerator on
    # representative radii, then used for the exhaustive state grid.
    for radius in (R0, R0 + max_h):
        enumerated = ring_cells(radius)
        assert all(ring_cell(radius, j) == cell for j, cell in enumerate(enumerated))
    coords = {(h, t): annulus_state(M, R0, h, t) for h in range(max_h + 1) for t in range(M)}
    assert len(set(coords.values())) == (max_h + 1) * M
    t_hist, h1_hist, h2_hist = Counter(), Counter(), Counter()
    for h in range(max_h + 1):
        for t in range(M):
            t_hist[hdist(coords[h, t], coords[h, (t + 1) % M])] += 1
            if h + 1 <= max_h:
                h1_hist[hdist(coords[h, t], coords[h + 1, t])] += 1
            if h + 2 <= max_h:
                h2_hist[hdist(coords[h, t], coords[h + 2, t])] += 1
    assert max(t_hist) <= 2
    assert h1_hist == Counter({1: max_h * M})
    assert h2_hist == Counter({2: (max_h - 1) * M})
    return {
        "M": M, "R0": R0, "max_h": max_h,
        "states": (max_h + 1) * M,
        "t_plus_1_distance_histogram": dict(sorted(t_hist.items())),
        "h_plus_1_distance_histogram": dict(sorted(h1_hist.items())),
        "h_plus_2_distance_histogram": dict(sorted(h2_hist.items())),
    }


def source_relation_hist(coords, k):
    hist = Counter(hdist(coords[n], coords[k * n]) for n in range(1, (len(coords) - 1) // k + 1))
    return {"pairs": sum(hist.values()), "histogram": dict(sorted(hist.items())), "max_distance": max(hist)}


def main():
    L, N = 16, 1 << 16
    batch_path = Path(__file__).with_name("coverage_relation_batches.json")
    batch_doc = json.loads(batch_path.read_text(encoding="utf-8"))
    assert batch_doc["schema"] == "NOLLM_Q40_ANNULUS_RELATION_BATCHES_V1"
    assert batch_doc["population_N"] == N
    batch_map = {}
    for entry in batch_doc["entries"]:
        key = (entry["b"], entry["direction"], entry["multiplier"], entry["steps"])
        assert key not in batch_map
        result = entry["result"]
        assert result["pairs"] == (N - 1) // entry["multiplier"]
        assert sum(int(v) for v in result["minimum_support_distance_histogram"].values()) == result["pairs"]
        assert sum(int(v) for v in result["hausdorff_histogram"].values()) == result["pairs"]
        assert result["overlap_count"] == int(result["minimum_support_distance_histogram"].get("0", result["minimum_support_distance_histogram"].get(0, 0)))
        assert result["max_hausdorff"] == max(int(k) for k in result["hausdorff_histogram"])
        batch_map[key] = result
    assert len(batch_map) == 16
    formula_grid = []
    for b in range(6, 15):
        M = 1 << b
        table = dlog_table(b)
        carr = [carrier(n, b, table) for n in range(1, N)]
        observed = len(set(carr))
        formula = unique_carrier_formula(L, b)
        assert observed == formula
        fibers = Counter(carr)
        assert max(fibers.values()) == max_fiber_formula(L, b)
        R0 = (M + 5) // 6
        formula_grid.append({
            "b": b, "M": M, "distinct_carriers": observed,
            "formula": formula, "max_fiber": max(fibers.values()),
            "annulus_R0": R0, "annulus_outer_R": R0 + 31,
        })

    experiments = {}
    for b in (11, 14):
        M, R0, carr, coords, _rings = build_realized(N, b)
        source = {"times_2": source_relation_hist(coords, 2), "times_5": source_relation_hist(coords, 5)}
        physical = {}
        for direction in ("coverage_up", "coverage_down"):
            physical[direction] = {}
            for k in (2, 5):
                physical[direction][f"times_{k}"] = {
                    "one_step": batch_map[(b, direction, k, 1)],
                    "two_steps": batch_map[(b, direction, k, 2)],
                }
        experiments[str(b)] = {
            "M": M, "R0": R0, "outer_R": R0 + 31,
            "distinct_integer_carriers": len(set(carr[1:])),
            "positive_integers": N - 1,
            "source_generator_distances": source,
            "q40_coverage": physical,
        }

    annulus = annulus_theorem_check(1 << 11, 31)

    assert expand_hits(0, 0, "coverage_up") == {(0, 0): 96}
    down0 = expand_q16(0, 0, "coverage_down")
    assert dict((target, weight) for target, weight, _count in down0)[(0, 0)] == 49152
    assert sorted(weight for target, weight, _count in down0 if target != (0, 0)) == [2730, 2730, 2731, 2731, 2731, 2731]

    result = {
        "schema": "NOLLM_DYADIC_ANNULUS_Q40_COVERAGE_VERIFICATION_V1",
        "status": "EXACT_ANNULUS_DERIVATION_PLUS_FINITE_PRODUCTION_KERNEL_OBSERVER",
        "source": {
            "nollm_main": "88d63b32329fbbcd18028de1ac83b2db3c988e33",
            "approximate_coverage_blob": "fb1f19515b888ed9f01417b5e857c2146c418a66",
            "coverage_contract_blob": "f08885e526248597edbd840b134bf7dbb26e1420",
            "fixed_point_blob": "9ea00e3c84a82f480c692a6ca0ca717a579dab60",
        },
        "population": {"L": L, "N": N, "positive": N - 1},
        "annulus_embedding": annulus,
        "carrier_identity_formula": {
            "law": "U(L,b)=(L-b)*2^(b+1)-1 for 0<=b<=L-2",
            "max_fiber": "2^(L-b-2)",
            "formula_grid": formula_grid,
            "critical_note": "b≈L/2 is geometrically compact but many-to-one; retain integer identity or an explicit repair coordinate",
        },
        "experiments": experiments,
        "claim_boundary": [
            "annulus locality and carrier-count formulas are exact for the declared finite model",
            "Q40 coverage statistics are exhaustive finite measurements on N=65536 for b=11 and b=14",
            "coverage reproduction uses exact published integer constants and rounding, not Nollm package execution",
            "no production geometry, runtime, semantic placement or X6 definition is modified",
            "support locality is not a semantic-recall theorem or infinite-scale theorem",
        ],
    }
    out = Path(__file__).with_name("results.json")
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "PASS": True,
        "b11": experiments["11"],
        "b14": experiments["14"],
    }, ensure_ascii=False, indent=2))


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--relation-worker", nargs=6,
                        metavar=("B", "DIRECTION", "K", "STEPS", "LO", "HI"))
    args = parser.parse_args()
    if args.relation_worker:
        b, direction, k, steps, lo, hi = args.relation_worker
        b, k, steps, lo, hi = map(int, (b, k, steps, lo, hi))
        _M, _R0, _carr, coords, _rings = build_realized(1 << 16, b)
        clear_coverage_caches()
        print(json.dumps(relation_stats_range(coords, k, direction, steps, lo, hi),
                         sort_keys=True))
        return
    main()


if __name__ == "__main__":
    cli()
