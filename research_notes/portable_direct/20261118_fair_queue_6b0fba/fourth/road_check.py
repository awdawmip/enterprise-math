"""Exact rational enclosures for finite midpoint, cell and Green energies of the full road."""
from fractions import Fraction as F
import json
from pathlib import Path
from functools import lru_cache
from math import isqrt

GRID = 1 << 80


def floor(x):
    return x.numerator // x.denominator


def ceil(x):
    return -floor(-x)


def outward(lo, hi):
    return F(floor(lo * GRID), GRID), F(ceil(hi * GRID), GRID)


def point(x):
    return F(x), F(x)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[1], a[1] - b[0]


def mul(a, b):
    values = [x * y for x in a for y in b]
    return outward(min(values), max(values))


def square(a):
    return outward(0 if a[0] <= 0 <= a[1] else min(a[0]**2, a[1]**2), max(a[0]**2, a[1]**2))


@lru_cache(None)
def root(n, k):
    """Bracket n**(-1/k) exactly on the grid. k is a power of two."""
    if k < 1 or k & (k - 1):
        raise ValueError("k must be a power of two")
    b = GRID**k // n
    for _ in range(k.bit_length() - 1):
        b = isqrt(b)
    assert n*b**k <= GRID**k < n*(b+1)**k
    return F(b, GRID), F(b + (n*b**k != GRID**k), GRID)


def density(k, cutoff):
    z = point(0)
    for n in range(1, cutoff + 1):
        z = add(z, mul(point(F(1,n)), root(n,k)))
    low = z[0] + k*root(cutoff+1,k)[0]
    high = z[1] + k*root(cutoff,k)[1]
    return outward(1/high, 1/low)


def factors(n):
    for p in range(2, isqrt(n)+1):
        if n % p == 0:
            yield p
            while n % p == 0:
                n //= p
    if n > 1:
        yield n


def mass(n, k):
    w = point(1)
    for p in factors(n):
        w = mul(w, sub(point(1), root(p,k)))
    return w


def cell_log(n):
    """log(1+1/n) = 2 atanh(1/(2n+1)); the first omitted power is 49."""
    t = F(1, 2*n+1)
    value = 2*sum(t**j/j for j in range(1, 49, 2))
    return outward(value, value + 2*t**49/(49*(1-t*t)))


def decimal_interval(t, digits=10):
    factor = 10**digits
    def fmt(i):
        return f"{i//factor}.{i%factor:0{digits}d}"
    return "[" + fmt(floor(t[0]*factor)) + ", " + fmt(ceil(t[1]*factor)) + "]"


def energy(k, h=128, cutoff=4096):
    c = density(k, cutoff)
    w = [point(0)]*2 + [mass(n,k) for n in range(2,h+1)]
    a = [point(0)]
    for n in range(1,h+1):
        a.append(add(a[-1], w[n]))
    logs = [point(0)] + [cell_log(n) for n in range(1,h)]
    c2 = square(c)
    midpoint, cells = point(0), c2  # (0,1) contributes c²
    for n in range(1,h):
        b = sub(a[n], mul(c, point(n+F(1,2))))
        midpoint = add(midpoint, mul(square(b), point(F(1,n*n))))
        lin = mul(mul(mul(c,a[n]), logs[n]), point(2))
        quad = mul(square(a[n]), point(F(1,n*(n+1))))
        cells = add(cells, add(sub(quad, lin), c2))
    pair, cross, log_hn = point(0), point(0), point(0)
    for n in range(h, 1, -1):
        if n<h:
            log_hn = add(log_hn, logs[n])
        block = mul(w[n], add(w[n], mul(point(2),a[n-1])))
        pair = add(pair, mul(block, point(F(1,n)-F(1,h))))
        cross = add(cross, mul(w[n], log_hn))
    green = add(sub(pair, mul(mul(point(2),c), cross)), mul(c2,point(h)))
    overlap = max(cells[0],green[0]), min(cells[1],green[1])
    assert 0 < overlap[0] <= overlap[1]
    # Both decompositions enclose exactly the same raw energy.
    return c, midpoint, cells, green, overlap, max(hi-lo for lo,hi in w)


def main():
    ledger = Path(__file__).with_name("road_bound_ledger.json")
    rows = json.loads(ledger.read_text())["finite_protocol"]["rows"]
    assert [r["k"] for r in rows] == [4,8,16]
    for row in rows:
        k = row["k"]
        c,d,cell,green,both,wm = energy(k)
        for name, value in [("c", c), ("D", d), ("raw_Q", both)]:
            assert decimal_interval(value) == "[" + ", ".join(row[name]) + "]"
        assert ceil(wm*GRID) == row["weight_width_grid_units"]
        print(f"k={k} H=128 T=4096  c={decimal_interval(c)}  D[1,127]={decimal_interval(d)}")
        print(" raw cells",decimal_interval(cell),"green",decimal_interval(green),"intersection",decimal_interval(both))
        print(" road weight width on grid <=",ceil(wm*GRID),"/ 2^80", "density width", float(c[1]-c[0]))


if __name__ == "__main__":
    main()
