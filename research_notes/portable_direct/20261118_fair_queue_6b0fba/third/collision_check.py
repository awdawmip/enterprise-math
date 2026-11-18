"""Replay the n=15 Q30 certificate. Requires Python 3, C++17, and geng 2.8.9 or its graph6 stream."""
import argparse
from functools import lru_cache
import hashlib
import json
from math import comb, factorial
from pathlib import Path
import re
import subprocess
import tempfile

DIR = Path(__file__).resolve().parent
ROW = re.compile(r"r=(\d+) reps=(\d+) in_nonunique_seed_buckets=(\d+) repeats=(\d+) orbit=(\d+) aut:(.*)")


@lru_cache(None)
def all_graphs(n1, n2, n3):
    """Count labeled realizations of a fixed degree assignment; omit isolated labels."""
    counts = [0, n1, n2, n3]
    d = next((j for j in (3, 2, 1) if counts[j]), 0)
    if not d:
        return 1
    counts[d] -= 1
    a, b, c = counts[1:]
    total = 0
    for i in range(min(d, a) + 1):
        for j in range(min(d - i, b) + 1):
            k = d - i - j
            if k <= c:
                ways = comb(a, i) * comb(b, j) * comb(c, k)
                total += ways * all_graphs(a - i + j, b - j + k, c - k)
    return total


@lru_cache(None)
def connected(r, s):
    """Fixed labels of degrees 3 and 2, with multiplicative choices for the first component."""
    if r == 0:
        return factorial(s - 1) // 2 if s >= 3 else 0
    result = all_graphs(0, s, r)
    for i in range(1, r + 1):
        for j in range(s + 1):
            if (i, j) != (r, s):
                result -= comb(r - 1, i - 1) * comb(s, j) * connected(i, j) * all_graphs(0, s - j, r - i)
    return result


def require(test, message):
    if not test:
        raise ValueError(message)


def check_census(lines, cert):
    require(len(lines) == len(cert["sectors"]) + 1, "unexpected rows or explicit collision")
    require(lines[0] == f'cycle_excluded {cert["cycle_excluded"]} seed_histograms {cert["seed_histograms"]}', "seed census")
    require([s["degree3"] for s in cert["sectors"]] == list(range(2, 16, 2)), "missing sector")
    for line, expected in zip(lines[1:], cert["sectors"]):
        match = ROW.fullmatch(line)
        require(match is not None, f"malformed row {line}")
        r, reps, amb, repeats, orbit = map(int, match.groups()[:5])
        aut_hist = {k: int(v) for k, v in (pair.split(":") for pair in match[6].split())}
        observed = dict(degree3=r, representatives=reps, in_nonunique_seed_buckets=amb,
                        packet_repeats=repeats, fixed_label_orbit_sum=orbit,
                        automorphism_order_multiplicities=aut_hist)
        require(observed == expected, f"stored values differ at r={r}")
        require(repeats == 0 and sum(aut_hist.values()) == reps, f"packet or automorphism totals r={r}")
        group = factorial(r) * factorial(15 - r)
        require(all(group % int(a) == 0 for a in aut_hist), f"nonintegral orbit sizes r={r}")
        recomputed = sum((group // int(a)) * count for a, count in aut_hist.items())
        require(orbit == recomputed == connected(r, 15 - r), f"incomplete coverage r={r}")
    require(cert["cycle_excluded"] + sum(s["representatives"] for s in cert["sectors"]) == cert["generator"]["graph6_lines"], "representative total")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--geng", help="path or executable name of nauty geng 2.8.9")
    source.add_argument("--g6", type=Path, help="existing output of the pinned geng invocation")
    parser.add_argument("--cxx", default="c++", help="C++17 compiler")
    args = parser.parse_args()
    cert = json.loads((DIR / "collision_certificate.json").read_text())
    gen = cert["generator"]
    with tempfile.TemporaryDirectory(prefix="q30-n15-") as tmp:
        work = Path(tmp)
        g6 = args.g6
        if args.geng:
            g6 = work / "g15.g6"
            with g6.open("wb") as stream:
                subprocess.run([args.geng, *gen["args"]], stdout=stream, check=True)
        content = g6.read_bytes()
        require(len(content) == gen["graph6_bytes"] and content.count(b"\n") == gen["graph6_lines"], "graph6 census")
        require(hashlib.sha256(content).hexdigest() == gen["graph6_sha256"], "graph6 integrity pin")
        executable = work / "collision_check"
        subprocess.run([args.cxx, "-std=c++17", "-O3", str(DIR / "collision_check.cpp"), "-o", str(executable)], check=True)
        run = subprocess.run([str(executable), str(g6)], text=True, stdout=subprocess.PIPE, check=True)
        check_census(run.stdout.splitlines(), cert)
        print(run.stdout, end="")
        print("Exact n=15 packet and connected-orbit checks passed.")


if __name__ == "__main__":
    main()
