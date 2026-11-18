"""Exact first-layer screen. Python 3.10+. Source checkout for the BRC calibration via --repo."""
import argparse
from collections import Counter
from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import sys

# Frozen before reading either region's labels. q=1+k*2**(n+2), h=n-1.
REGIONS = {"development": ((6, 1, 512),),
           "holdout": ((6, 513, 2048), (7, 1, 2048), (8, 1, 2048))}
PINS = {"brc_transport.py": "386f9b955a65aba938b08bf76f21330c612a7e7a396d0c3dd83523bfaaa9d4e7",
        "brc_histogram.py": "256ef167e2aee651c042195522a0013ba619f265f9e4d8fa24f07d3399695a67"}


def center(a, q):
    return (a + q // 2) % q - q // 2


def observe(n, q):
    """Generate only h preterminal edges. None means undecided by that rule."""
    value = center(2, q)
    cores, magnitudes = {}, set()
    first = {"unit": None, "magnitude": None, "core": None}
    witness = None
    for j in range(n):
        a = abs(value)
        b = (a & -a).bit_length() - 1
        m, e = a >> b, (1 << j) - b
        if a == 1 and first["unit"] is None:
            first["unit"] = j
        if a in magnitudes and first["magnitude"] is None:
            first["magnitude"] = j
        magnitudes.add(a)
        if m in cores:
            i, previous_e, previous_r = cores[m]
            if e != previous_e and witness is None:
                witness = (i, j, previous_r, value, previous_e, e)
                first["core"] = j
        else:
            cores[m] = (j, e, value)
        if j < n - 1:
            value = center(value * value, q)
    return first, witness


def run_region(name):
    sums = Counter()
    rows = []
    for n, lo, hi in REGIONS[name]:
        fermat = (1 << (1 << n)) + 1
        for k in range(lo, hi + 1):
            q = 1 + (k << (n + 2))
            first, witness = observe(n, q)
            # The independent integer label enters only after all three rule decisions.
            g = gcd(q, fermat)
            label = "proper" if q < fermat and g == q else "trivial" if q == fermat else "no"
            sums["N"] += 1
            sums["raw_odd_interval"] += (1 << (n + 1))
            sums["unfiltered_q_squares"] += n
            sums["raw_odd_interval_squares"] += n << (n + 1)
            sums["prefix_audit_squares"] += n - 1
            if label != "no":
                sums[label] += 1
            if g != 1:
                sums["positive_gcd"] += 1
            for rule in first:
                j = first[rule]
                if j is not None:
                    assert g == 1, (q, n, rule, g)
                    sums[rule + "_rejected"] += 1
                sums[rule + "_squares_with_fallback"] += n if j is None else j
            baseline = min((j for j in (first["unit"], first["magnitude"]) if j is not None), default=None)
            sums["both_baselines_rejected"] += baseline is not None
            sums["both_baselines_squares_with_fallback"] += n if baseline is None else baseline
            combined = min((j for j in (first["unit"],first["core"]) if j is not None), default=None)
            sums["combined_rejected"] += combined is not None
            sums["combined_squares_with_fallback"] += n if combined is None else combined
            sums["combined_probe_count"] += n if combined is None else combined + 1
            # The ledger is lossless: other k have no preterminal decision and gcd 1.
            if any(v is not None for v in first.values()) or g != 1:
                rows.append([n, k, q, first["unit"], first["magnitude"], witness, g, label])
    return {"counts": dict(sorted(sums.items())), "exceptions": rows}


def calibrate(repo):
    source = repo / "src" / "enterprise_math"
    for file, expected in PINS.items():
        assert sha256((source / file).read_bytes()).hexdigest() == expected, file
    sys.path.insert(0, str(repo / "src"))
    from enterprise_math.brc_transport import Affine

    # Exact affine lifts before projection, using only the declared first hidden digit.
    # Independent small cases include q=3 with its different initial section.
    lengths = []
    for q, h in ((3, 5), (9, 5), (25, 6), (641, 5)):
        r = center(2, q)
        u0 = (2 - r) // q
        composed = Affine.identity(1)
        rows = []
        for j in range(h):
            nxt = center(r*r, q)
            c = (r*r - nxt) // q
            step = Affine(((2*r,),), (c,))
            composed = composed.then(step)
            u = int(composed.apply((u0,))[0]) % q
            assert u == ((pow(2, 1 << (j+1), q*q) - nxt) // q) % q
            rows.append((r, c, nxt, u))
            r = nxt
        if q == 641:
            assert (r,u) == (-1,44)
        lengths.append((q,h,rows))
    return lengths


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("region",choices=(*REGIONS, "calibration"))
    p.add_argument("--repo", type=Path)
    p.add_argument("--ledger", type=Path)
    args = p.parse_args()
    if args.region == "calibration":
        if args.repo is None:
            p.error("calibration requires --repo /path/to/pinned/enterprise-math")
        print(json.dumps(calibrate(args.repo)))
        return
    result = run_region(args.region)
    blob = (json.dumps(result, separators=(",",":"), ensure_ascii=True)+"\n").encode()
    if args.ledger:
        args.ledger.write_bytes(blob)
    print(args.region, json.dumps(result["counts"]), "exceptions", len(result["exceptions"]),
          "ledger_sha256", sha256(blob).hexdigest())


if __name__ == "__main__":
    main()
