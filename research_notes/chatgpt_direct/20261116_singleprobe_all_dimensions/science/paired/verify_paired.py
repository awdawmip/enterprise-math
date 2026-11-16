"""Check a one-probe partition for 9 old five-valued symbols.
Inputs are a tiny explicit certificate. This script uses only Python's standard library.
Run 'python verify_paired.py --full' to enumerate every old input.
"""
import json
from collections import Counter
from itertools import product
from pathlib import Path
import sys


def laminar(points):
    blocks = [{w for w in points if w[j] == a}
              for j in range(len(points[0])) for a in range(5)]
    return all(not (a & b) or a <= b or b <= a for a in blocks for b in blocks)


def syndrome(x, rows):
    return tuple(sum(a * v for a, v in zip(row, x)) % 5 for row in rows)


def coset_cover(description):
    rows = description['projection_rows']
    W = description['witness']
    n = len(W[0])
    # All projection rows have independent images.
    image = {syndrome(w, rows) for w in product(range(5), repeat=n)
             if sum(bool(x) for x in w) <= len(rows)}
    assert len(image) == 5**len(rows)
    reps, sizes = {}, []
    for k, group in enumerate(description['classes']):
        perm = group['permutations']
        assert len(perm) == n and all(sorted(p) == list(range(5)) for p in perm)
        shift = next(w for w in product(range(5), repeat=n)
                     if syndrome(w, rows) == tuple(group['shift']))
        W1 = [tuple((shift[j]+perm[j][v]) % 5 for j,v in enumerate(w)) for w in W]
        assert laminar(W1)
        before = len(reps)
        for w in W1:
            reps.setdefault(syndrome(w, rows), (k,w))
        sizes.append(len(reps)-before)
    return rows, reps, sizes


def run(full):
    cert = json.loads(Path(__file__).with_name("paired_certificate.json").read_text())
    e_rows, outer, sizes = coset_cover(cert['eight'])
    f_rows, inner, residual_sizes = coset_cover(cert['five'])
    assert e_rows == [[1,0,0,1]*2,[0,1,0,1]*2,[0,0,1,1]*2] and len(inner) == 25
    # x[j+4] plus x[j] equals an individual pair sum; t fixes the fourth sum.
    # The first three pair sums equal syndrome components minus t.
    # Free parameters (x[0:4], last) form a 5D inner copy. All remaining
    # coordinates are coordinatewise relabelings of these four or constants.
    missing = sorted(set(product(range(5), repeat=3)) - set(outer))
    count = len(sizes)*5**6 + len(missing)*5*len(residual_sizes)*5**3
    assert count <= 2**17 and 5**9 > 16*(2**16)
    result = dict(covered=len(outer), sizes=sizes, missing=missing,
                  residual_sizes=residual_sizes, n9=count, n12=125*count)
    if full:
        hist = Counter()
        for sums in product(range(5), repeat=4):
            t = sums[3]
            s = tuple((z+t)%5 for z in sums[:3])
            for variables in product(range(5),repeat=4):
                w8 = variables + tuple((c-v)%5 for c,v in zip(sums,variables))
                for v in range(5):
                    if s in outer:
                        k, w = outer[s]
                        key = (0, k, tuple((a-b)%5 for a,b in zip(w8,w)), v)
                    else:
                        y = variables+(v,)
                        k, w = inner[syndrome(y,f_rows)]
                        key = (1, s, t, k, tuple((a-b)%5 for a,b in zip(y,w)))
                    hist[key] += 1
        assert len(hist)==count and sum(hist.values()) == 5**9 and max(hist.values()) <=16
        result["all_inputs"] = sum(hist.values())
        result["class_sizes"] = sorted(Counter(hist.values()).items())
    return result

if __name__ == "__main__":
    print(json.dumps(run("--full" in sys.argv), indent=2))
