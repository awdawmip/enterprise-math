"""Recompute the archived open-pipe mass-flow comparison using Python 3.10+."""
import argparse
import bisect
import hashlib
import io
import json
import math
import sys
import urllib.request
import zipfile
from fractions import Fraction
from pathlib import Path

SHA = "1be2060781ac6b1acf19ecda3db4ea8da1223ed03f3e0c301f06ce95eba1bc90"
PAGE = "https://data.mendeley.com/datasets/zhtdbbwr8d/1"
URL = ("https://data.mendeley.com/public-files/datasets/zhtdbbwr8d/files/"
       "e8661d61-d718-4377-9b66-a7a73931c7c9/file_downloaded")
PREFIX = "Raw_data_sets/Open_pipe_flow_test/Mass_Flow_Rate/"
PRESSURES = (10, 15, 20, 21, 23)  # hundredths of a bar, from dataset README
TEST = (10, 15, 21, 23)


def fetch(path):
    if path:
        data = path.read_bytes()
    else:
        req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0",
                                                   "Referer": PAGE, "Accept": "*/*"})
        with urllib.request.urlopen(req, timeout=45) as response:
            data = response.read(302500)
    if len(data) != 302499 or hashlib.sha256(data).hexdigest() != SHA:
        raise ValueError("archive digest or size mismatch")
    return data


def read_records(z, tag, p):
    path = PREFIX + f"{tag}_set_{PRESSURES.index(p) + 1}.txt"
    data = z.read(path)
    records = {}
    for line in data.decode("ascii").splitlines():
        fields = line.split()
        if not fields:
            continue
        if len(fields) == 3:
            assert int(fields[0]) == len(records)
        else:
            assert len(fields) == 2
        t, y = map(Fraction, fields[-2:])
        tick = round(10 * t)
        assert abs(t - Fraction(tick, 10)) <= Fraction(4, 10**7)
        assert tick == len(records) and tick not in records
        records[tick] = y
    assert sorted(records) == list(range(len(records))) and len(records) >= 101
    return records, hashlib.sha256(data).hexdigest()


def minimal_knots(y, tol):
    # A chord from i to j is legal precisely when its slope satisfies
    # every preceding strip at i<h<j. Bounds use the original rational data.
    n = len(y)
    dist, pred = [n + 1] * n, [-1] * n
    dist[0] = 0
    for i in range(n - 1):
        lo = hi = None
        for j in range(i + 1, n):
            d = j - i
            slope = (y[j] - y[i]) / d
            if (lo is None or lo <= slope <= hi) and dist[i] + 1 < dist[j]:
                dist[j], pred[j] = dist[i] + 1, i
            lower, upper = slope - tol / d, slope + tol / d
            lo = lower if lo is None else max(lo, lower)
            hi = upper if hi is None else min(hi, upper)
            if lo > hi:
                break
    path = [n - 1]
    while path[-1]:
        path.append(pred[path[-1]])
    return list(reversed(path))


def check_direct(y, tol):
    # Independent explicit enumeration of every chord; paths counted by DP.
    n = len(y)
    distance = list(range(n))
    for j in range(1, n):
        for i in range(j):
            if distance[i] + 1 >= distance[j]:
                continue
            if all(abs((j - i) * y[h] - (j - h) * y[i] - (h - i) * y[j])
                   <= (j - i) * tol for h in range(i + 1, j)):
                distance[j] = distance[i] + 1
    return distance[-1]


def polygon(y, knots, t):
    if not knots[0] <= t <= knots[-1]:
        raise ValueError("out-of-domain query")
    k = min(bisect.bisect_right(knots, t) - 1, len(knots) - 2)
    i, j = knots[k:k + 2]
    return y[i] + ((y[j] - y[i]) / (j - i)) * (t - i)


def metrics(truth, candidate):
    err = [a - b for a, b in zip(candidate, truth, strict=True)]
    total = math.fsum(float(y)**2 for y in truth)
    return {"max_abs_kg_s": round(max(map(abs, map(float, err))), 10),
            "relative_l2": round(math.sqrt(math.fsum(float(e)**2 for e in err) / total), 12),
            "index_of_max": max(range(len(err)), key=lambda i: abs(err[i]))}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--archive", type=Path, help="optional local Raw_data_sets.zip")
    ap.add_argument("--out", type=Path, help="optional output JSON")
    args = ap.parse_args()
    data = fetch(args.archive)
    full, native, hashes = {}, {}, {}
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        for p in PRESSURES:
            full[p], f = read_records(z, "CFD", p)
            native[p], g = read_records(z, "ROM", p)
            hashes[str(p)] = {"CFD": f, "ROM": g, "identical_bytes": f == g,
                              "CFD_rows": len(full[p]), "ROM_rows": len(native[p])}
    y = [full[20][i] for i in range(101)]
    all_knots = list(range(101))
    profiles, paths = {}, {}
    for key in ("0.01", "0.05", "0.10", "0.25", "0.50"):
        tol = Fraction(key)
        knots = minimal_knots(y, tol)
        assert check_direct(y, tol) == len(knots) - 1
        error = max(abs(polygon(y, knots, Fraction(i)) - y[i]) for i in all_knots)
        assert error <= tol
        profiles[key] = {"number": len(knots), "knots_in_tenths": knots,
                         "exact_training_max": str(error)}
        paths[key] = knots
    scores = {}
    for p in TEST:
        c, n = full[p], native[p]
        truth = [c[j] for j in range(94)]
        blk = {"Galerkin_0_to_10": metrics([c[j] for j in all_knots], [n[j] for j in all_knots]),
               "Galerkin_0_to_9.3": metrics(truth, [n[j] for j in range(94)])}
        for label, exponent in (("quadratic", 2.0), ("seven_fourths", 1.75)):
            r = p / 20
            scale, speed = r**(1 / exponent), r**(1 - 1 / exponent)
            horizon = min(100, math.floor(100 / speed))
            assert horizon >= 93
            ref = [scale * polygon(y, all_knots, speed * j) for j in range(94)]
            compact = [scale * polygon(y, paths["0.10"], speed * j) for j in range(94)]
            observed_gap = max(abs(a - b) for a, b in zip(compact, ref))
            assert observed_gap <= scale * .1 + 1e-12
            blk[label] = {"last_supported_tenth_s": horizon, "full_trace": metrics(truth, ref),
                          "knots_0.10": metrics(truth, compact),
                          "measured_compression_gap": round(observed_gap, 10),
                          "certified_compression_bound": round(scale * .1, 10)}
        scores[str(p)] = blk
    res = {"archive": {"doi": "10.17632/zhtdbbwr8d.1", "sha256": SHA, "bytes": len(data)},
           "case": "Open_pipe_flow_test/Mass_Flow_Rate", "pressure_unit_keys": "0.01 bar",
           "primary_training_hundredths": 20, "posterior_common_ticks": [0, 93],
           "native_file_checks": hashes, "training_knots": profiles, "held_out_metrics": scores}
    out = json.dumps(res, indent=2, ensure_ascii=False) + "\n"
    if args.out:
        args.out.write_text(out, encoding="utf-8")
    else:
        sys.stdout.write(out)


if __name__ == "__main__":
    main()
