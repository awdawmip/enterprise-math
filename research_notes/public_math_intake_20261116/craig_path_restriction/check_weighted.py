"""Exact checks for the area tilt and source-preserving positive path weights."""

import hashlib
import importlib.util
import os
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path

BRC_COMMIT = "c4d450536bf71ed87fd74555295ec60485262f0a"
BRC_BLOB = "300a96e3dc24bf6fff73743037a0347a8bc83176"
BRC_PATH = Path("experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py")


def load_signed_brc():
    """Use the supplied original kernel only after checking its immutable blob."""
    configured = os.environ.get("SIGNED_BRC_PATH")
    here = Path(__file__).resolve().parent
    candidates = ([Path(configured)] if configured else
                  [here / "signed_brc.py", *(p / BRC_PATH for p in (here, *here.parents))])
    for path in candidates:
        if not path.is_file():
            continue
        data = path.read_bytes()
        oid = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        if oid != BRC_BLOB:
            continue
        spec = importlib.util.spec_from_file_location("verified_signed_brc", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    raise RuntimeError(f"Provide SIGNED_BRC_PATH for {BRC_COMMIT}:{BRC_PATH}, blob {BRC_BLOB}")


def words(m):
    for chosen in combinations(range(2*m), m):
        positions = frozenset(chosen)
        yield "".join("X" if i in positions else "Y" for i in range(2*m))


def area(word):
    horizontal = 0
    value = 0
    for step in word:
        if step == "X":
            horizontal += 1
        else:
            value += horizontal
    return value


def source_subwords(word, k):
    """Each retained position tuple records one source witness, even for equal subwords."""
    groups = [[i for i, step in enumerate(word) if step == label] for label in "XY"]
    for horizontal in combinations(groups[0], k):
        for vertical in combinations(groups[1], k):
            positions = tuple(sorted(horizontal + vertical))
            yield positions, "".join(word[i] for i in positions)


def law_weight(word, a, b):
    r, s = word.count("X"), word.count("Y")
    result = Fraction(1)
    for step in word:
        if step == "X":
            result *= Fraction(r*a, r*a+s*b)
            r -= 1
        else:
            result *= Fraction(s*b, r*a+s*b)
            s -= 1
    return result


def multiply(left, right):
    coeff = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            coeff[i+j] += x*y
    return coeff


def check_minor(n):
    selected = ("YXYX", "XYYX", "XYXY")
    H = {u: [0]*(n*n+1) for u in selected}
    witnesses = 0
    for word in words(n):
        degree = area(word)
        for _, u in source_subwords(word, 2):
            witnesses += 1
            if u in H:
                H[u][degree] += 1
    cross = multiply(H[selected[0]], H[selected[2]])
    square = multiply(H[selected[1]], H[selected[1]])
    difference = [x-y for x,y in zip(cross,square)]
    if n == 3:
        factors = [[-4], [0,0,0,0,0,1], [1,-2,1], [1,1,1], [1,2,1,2,1]]
    else:
        half = [6,57,201,502,807,1241,1741,2264,2477,2576]
        positive = half + half[-2::-1]
        factors = [[-1], [0,0,0,0,0,1], [1,-2,1], [1,0,1], positive]
    expected = [1]
    for factor in factors:
        expected = multiply(expected, factor)
    assert difference == expected + [0]*(len(difference)-len(expected))
    assert witnesses == comb(2*n, n) * comb(n, 2)**2
    return witnesses


def check_families():
    signed_brc = load_signed_brc()
    comparisons = variances = 0
    for m in range(1, 6):
        universe = list(words(m))
        assert len(universe) == signed_brc.shortest_path_multiplicity((m,m,0,0,0,0))
        down = {k: {w: Counter(u for _,u in source_subwords(w,k)) for w in universe}
                for k in range(1,m+1)}
        for a,b in [(1,1), (2,1), (1,3), (5,2)]:
            law = {w: law_weight(w,a,b) for w in universe}
            assert sum(law.values()) == 1
            p = Fraction(a, a+b)
            mean = sum(v*Fraction(area(w),m*m) for w,v in law.items())
            assert mean == p
            variance = sum(v*(Fraction(area(w),m*m)-mean)**2 for w,v in law.items())
            cov_x = Fraction(a*b*b, (a+b)**2*(a+2*b))
            cov_y = Fraction(a*a*b, (a+b)**2*(2*a+b))
            assert variance == (p*(1-p)+(m-1)*(cov_x+cov_y))/(m*m)
            variances += 1
            for k, fibers in down.items():
                out = defaultdict(Fraction)
                total = comb(m,k)**2
                for w, multiplicities in fibers.items():
                    for u, count in multiplicities.items():
                        out[u] += law[w] * Fraction(count,total)
                assert out == {u: law_weight(u,a,b) for u in words(k)}
                comparisons += 1
    return comparisons, variances


if __name__ == "__main__":
    print("uniform-deletion minors, source-witness counts:", {n:check_minor(n) for n in (3,4)})
    comparisons, variances = check_families()
    print(f"PASS: {comparisons} exact full projected laws; {variances} exact means and variances")
