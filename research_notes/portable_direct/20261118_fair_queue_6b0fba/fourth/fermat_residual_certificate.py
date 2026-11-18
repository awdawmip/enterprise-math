"""Standalone short-order certificates and exact prefix-fibre cross-check. No project imports."""
from collections import Counter, defaultdict
from functools import reduce
import json
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def relation(q, n, delta, sign):
    if q < 3 or q % 2 == 0 or n < 1 or sign not in (-1, 1) or not 0 < delta < (1 << n):
        raise ValueError("relation outside the strict preterminal budget")
    y, squares, multiplications = 2, 0, 0
    for bit in bin(delta)[3:]:
        y = y * y % q
        squares += 1
        if bit == "1":
            y = 2 * y % q
            multiplications += 1
    if y != sign % q:
        raise ValueError("incorrect signed power")
    return squares, multiplications


def check_ledgers():
    for region in ("development", "holdout"):
        stats = Counter()
        data = json.loads((ROOT / f"fermat_residual_{region}.json").read_text())
        for n, k, q, unit, magnitude, witness, common, label in data["exceptions"]:
            assert q == 1 + (k << (n + 2))
            if witness is None:
                continue
            i, j, a, b, ei, ej = witness
            assert 0 <= i < j < n and 0 < abs(ei-ej) <= 1 << j
            rows = [(i, a, ei), (j, b, ej)]
            odd = []
            for t, r, exponent in rows:
                assert 2 * abs(r) < q and r % q == pow(2, 1 << t, q)
                v = (abs(r) & -abs(r)).bit_length() - 1
                assert exponent == (1 << t) - v
                odd.append(abs(r) >> v)
            assert odd[0] == odd[1]
            sign = 1 if (a>0) == (b>0) else -1
            s, m = relation(q, n, abs(ei - ej), sign)
            stats.update(rejections=1, certificate_squares=s, certificate_doublings=m)
            assert common == 1 and label == "no"
        assert stats["rejections"] == data["counts"]["core_rejected"]
        print(region, dict(stats))


def check_fibres():
    universe = range(5, 514, 2)
    for h in range(6):
        groups = defaultdict(set)
        for q in universe:
            prefix = []
            all_zero = True
            for j in range(h+1):
                x = 1 << (1 << j)
                a = x % q
                r = a-q if 2*a>q else a
                if j:
                    c = (prefix[-1]**2 - r) // q
                    if c:
                        all_zero = False
                        assert (prefix[-1]**2-r)//c == q
                prefix.append(r)
            assert all_zero == (q > 2*(1 << (1 << h)))
            groups[tuple(prefix)].add(q)
        for z, observed in groups.items():
            d = reduce(gcd, (abs(a*a-b) for a,b in zip(z,z[1:])), 0)
            exact = {q for q in universe if q>2*max(map(abs,z)) and d%q==0}
            assert observed == exact
    n, h = 6, 4
    pair = (274177, 274433)
    assert all(q % 256 == 1 and q > 2*(1 << (1 << h)) for q in pair)
    assert [((1 << (1 << n)) + 1) % q == 0 for q in pair] == [True,False]
    print("all prefix fibres for 255 odd q, h=0..5; opposite-label zero-carry witness verified")


if __name__ == "__main__":
    check_ledgers()
    check_fibres()
