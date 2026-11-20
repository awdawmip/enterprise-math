#!/usr/bin/env python3
"""C84 deterministic certificate for the Haar triangle constant.

Only Python's integer arithmetic is used in the proof computation.  All
transcendentals are enclosed using Taylor remainders and integer square roots.
The printed decimals are for display; certificate endpoints are exact rationals.
See ../TRIANGLE_CONSTANT.md for the geometric inequalities being integrated.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from math import gcd, isqrt
from pathlib import Path
import time

BITS = 112
Q = 1 << BITS


def ceildiv(a, b):
    assert b > 0
    return -((-a) // b)


class I:
    """Closed interval [lo/Q,hi/Q]; every operation rounds outwards."""
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        self.lo = int(lo)
        self.hi = self.lo if hi is None else int(hi)
        assert self.lo <= self.hi

    @staticmethod
    def rat(n, d=1):
        assert d > 0
        return I((n * Q) // d, ceildiv(n * Q, d))

    @staticmethod
    def cv(x):
        if isinstance(x, I):
            return x
        if isinstance(x, Fraction):
            return I.rat(x.numerator, x.denominator)
        assert isinstance(x, int)
        return I.rat(x)

    def __add__(self, x):
        x = I.cv(x)
        return I(self.lo + x.lo, self.hi + x.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, x):
        return self + (-I.cv(x))

    def __rsub__(self, x):
        return I.cv(x) + (-self)

    def __mul__(self, x):
        x = I.cv(x)
        v = [self.lo*x.lo, self.lo*x.hi, self.hi*x.lo, self.hi*x.hi]
        return I(min(v)//Q, ceildiv(max(v), Q))

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = I.cv(x)
        assert x.lo > 0 or x.hi < 0
        if x.hi < 0:
            return (-self) / (-x)
        v = [Fraction(a*Q, b) for a in (self.lo, self.hi)
             for b in (x.lo, x.hi)]
        a, b = min(v), max(v)
        return I(a.numerator//a.denominator,
                 ceildiv(b.numerator, b.denominator))

    def __rtruediv__(self, x):
        return I.cv(x) / self

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        a, b = I.rat(1), self
        while n:
            if n & 1:
                a = a*b
            b = b*b
            n >>= 1
        return a

    def sqrt(self):
        assert self.lo >= 0
        lo = isqrt(self.lo * Q)
        hi = isqrt(self.hi * Q)
        if hi*hi < self.hi*Q:
            hi += 1
        return I(lo, hi)

    def nonnegative(self):
        assert self.hi >= 0
        return I(max(0, self.lo), self.hi)

    def json(self):
        return {"lower_numerator": str(self.lo), "upper_numerator": str(self.hi),
                "denominator": str(Q), "decimal": [decimal(self.lo), decimal(self.hi)]}


def decimal(n):
    with localcontext() as ctx:
        ctx.prec = 24
        return str(Decimal(n)/Decimal(Q))


def log(x):
    x = I.cv(x)
    assert x.lo > 0
    # Five half-angle steps ensure a small atanh argument on our input range.
    for _ in range(5):
        x = x.sqrt()
    z = (x-1)/(x+1)
    az = I(max(abs(z.lo), abs(z.hi)))
    assert az.hi < Q//2
    n = 24
    term = z
    total = I.rat(0)
    for j in range(n):
        total += term/(2*j+1)
        term *= z*z
    rem = az**(2*n+1)/((2*n+1)*(1-az*az))
    return 64*(total + I(-rem.hi, rem.hi))


def atan(x):
    x = I.cv(x)
    assert x.lo >= 0
    for _ in range(3):
        x = x/(1+(1+x*x).sqrt())
    assert x.hi < Q//4
    n = 24
    term = x
    total = I.rat(0)
    for j in range(n):
        total += ((-1)**j)*term/(2*j+1)
        term *= x*x
    rem = x**(2*n+1)/(2*n+1)
    return 8*(total + I(-rem.hi, rem.hi))


PI = 16*atan(I.rat(1, 5))-4*atan(I.rat(1, 239))
ZETA = PI*PI/6
C1 = 7/(8*ZETA)
LOG2 = log(2)


@lru_cache(None)
def density(s: Fraction):
    """Certified f(s), the normalized area density of three triangle points."""
    if s >= 1 or s <= 0:
        return I.rat(0)
    x = I.cv(s)
    lx = log(x)
    common = 12*(1-x)-6*(1+24*x+6*x*lx)*lx
    if s < Fraction(1, 4):
        t = (1-4*x).sqrt()
        u = log((1+t)/(1-t))/2
        value = common-12*(1+26*x)*t*u-144*x*(1+x)*(PI*PI/9-u*u)
    else:
        t = (4*x-1).sqrt()
        u = PI/3-atan(t)
        value = common-12*(1+26*x)*t*u-144*x*(1+x)*u*u
    return value.nonnegative()


def phi(n):
    return sum(gcd(k, n) == 1 for k in range(1, n+1))


@lru_cache(None)
def moments(a: Fraction):
    """B,C and their determinant-one summands, all nondecreasing in a."""
    if not a:
        z = I.rat(0)
        return z, z, z, z
    av = I.cv(a)
    bsum = sum((I.rat(phi(n), n)*density(Fraction(n, 2)/a)
                for n in range(1, (2*a).numerator//(2*a).denominator+1)), I.rat(0))
    csum = sum((I.rat(phi(n), n)*density(Fraction(n)/a)
                for n in range(1, a.numerator//a.denominator+1)), I.rat(0))
    return (av*av/(4*ZETA)*bsum, av*av/(8*ZETA)*csum,
            av*av/(4*ZETA)*density(Fraction(1, 2)/a),
            av*av/(8*ZETA)*density(Fraction(1)/a))


def area_cell(l: Fraction, h: Fraction):
    """Bounds valid throughout l<A<h, not merely at mesh points."""
    assert 0 < l < h <= Fraction(9, 2)
    lv, hv = I.cv(l), I.cv(h)
    bl, cl, b1l, c1l = moments(l)
    bh, ch, b1h, c1h = moments(h)
    dl, dh = C1*lv*lv, C1*hv*hv
    if h <= Fraction(3, 2):
        # Exact probability on A<3/2: A-cA²+B_1-C_1.
        lower = (lv-dh+b1l-c1h).lo
        upper = (hv-dl+b1h-c1l).hi
    else:
        bdlo = max(0, (bl-ch).lo)
        # D<=ceil(2h) holds a.e. on this open cell.
        m = ceildiv((2*h).numerator, (2*h).denominator)
        lower = (lv-dh+2*I(bdlo)/m).lo
        factor = I.rat(1) if h <= 4 else I.rat(3, 4)
        bdup = (bh-factor*cl).hi
        upper = (hv-dl+I(bdup)).hi
        # All k are optional integer moment upper bounds; k=1 often suffices.
        for k in range(2, 12):
            upper = min(upper, (hv-2*dl/(k+1)+2*I(bdup)/(k*(k+1))).hi)
    lower = max(0, lower)
    if l >= 1:
        lower = max(lower, (3/(16*ZETA*hv*hv)).lo)
        upper = min(upper, (lv/(lv*lv-lv+1)).hi)
    upper = min(upper, hv.hi, Q)
    assert 0 <= lower <= upper
    weight = 4*(hv.sqrt()-lv.sqrt())
    return I(lower, upper)*weight


def J(y):
    if y == 0:
        return I.rat(0)
    x = I.cv(y)
    return x**3*log(x)/6-5*x**3/36


@lru_cache(None)
def g(x: Fraction):
    if x <= 0:
        return I.rat(1)
    if x >= 2:
        return I.rat(0)
    xv = I.cv(x)
    if x <= 1:
        v = (-2*J(2-x)+2*LOG2*xv*xv+4*J(x)+6*J(1-x)
             +(I.rat(1, 2)-4*LOG2)*xv+8*LOG2/3-I.rat(7, 18))
    else:
        v = (-2*J(x)+2*LOG2*xv*xv+2*J(x-1)
             -(I.rat(3, 2)+4*LOG2)*xv+8*LOG2/3+I.rat(19, 18))
    return v.nonnegative()


def tail_certificate(mesh):
    """Exact kappa tail on r>=3, bounded by monotone one-dimensional cells."""
    total = I.rat(0)
    def qx(x):
        return 2/(3+(9-4*I.cv(x)).sqrt())
    for j in range(2*mesh):
        l, h = Fraction(j, mesh), Fraction(j+1, mesh)
        # g is nonincreasing, q_x is increasing.
        lower = (g(h)*qx(l)**5).lo
        upper = (g(l)*qx(h)**5).hi
        total += I(lower, upper)/mesh
    root2 = I.rat(2).sqrt()
    return root2/(54*ZETA)+6*root2/(5*ZETA)*total


def certify(mesh=1024, tail_mesh=1024):
    assert mesh % 2 == 0
    started = time.monotonic()
    half = I.rat(1, 2)
    # A<1/2 is exactly A-cA², integrated without a mesh.
    head = 4*half**1*half.sqrt()/3-4*C1*half**2*half.sqrt()/5
    middle = I.rat(0)
    for j in range(mesh//2, 9*mesh//2):
        middle += area_cell(Fraction(j, mesh), Fraction(j+1, mesh))
    tail = tail_certificate(tail_mesh)
    whole = head+middle+tail
    return {
        "schema": "C84_TRIANGLE_INTEGER_INTERVAL_V1",
        "method": "exact integer outward intervals; monotone area and tail cells",
        "precision_bits": BITS,
        "area_mesh_per_unit": mesh,
        "tail_mesh_per_unit": tail_mesh,
        "area_domain": ["1/2", "9/2"],
        "tail_domain": ["3", "infinity"],
        "pi": PI.json(), "zeta2": ZETA.json(),
        "head": head.json(), "middle": middle.json(), "tail": tail.json(),
        "kappa3": whole.json(),
        "coarse_rational_enclosure": ["759/500", "2379/1000"],
        "density_values_cached": density.cache_info().currsize,
        "seconds": round(time.monotonic()-started, 3),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def quick_verify(path=None):
    """Exact certificate arithmetic and elementary interval smoke checks.

    This verifies recorded arithmetic, not all cell evaluations.  Use --full
    (or the default computation) to independently recompute the mesh enclosure.
    """
    path = Path(path or Path(__file__).with_name("certificate.json"))
    d = json.loads(path.read_text())
    assert d["precision_bits"] == BITS
    def read(k):
        x = d[k]
        assert int(x["denominator"]) == Q
        return I(int(x["lower_numerator"]), int(x["upper_numerator"]))
    whole = read("head")+read("middle")+read("tail")
    want = read("kappa3")
    assert (whole.lo, whole.hi) == (want.lo, want.hi)
    low, high = map(Fraction, d["coarse_rational_enclosure"])
    assert low < Fraction(want.lo, Q) <= Fraction(want.hi, Q) < high
    assert PI.lo <= read("pi").lo <= read("pi").hi <= PI.hi
    assert log(1).lo <= 0 <= log(1).hi
    assert g(Fraction(0)).lo == Q and g(Fraction(2)).hi == 0
    assert density(Fraction(1)).hi == 0
    assert density(Fraction(1, 2)).lo > 0
    assert d["source_sha256"] == hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    assert d["schema"] == "C84_TRIANGLE_INTEGER_INTERVAL_V1"
    return {"ok": True, "checks": 9, "scope": "recorded sum, source digest and elementary intervals",
            "kappa3": want.json()}


def verify_saved_certificate(path=None):
    """Stable integration hook; same documented scope as quick_verify."""
    return quick_verify(path)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--mesh", type=int, default=1024)
    p.add_argument("--tail-mesh", type=int, default=1024)
    p.add_argument("--output", type=Path, default=Path(__file__).with_name("certificate.json"))
    p.add_argument("--quick", action="store_true")
    p.add_argument("--full", action="store_true", help="explicit synonym for the default full computation")
    a = p.parse_args()
    if a.quick:
        print(json.dumps(quick_verify(a.output), ensure_ascii=False, indent=2))
        return
    d = certify(a.mesh, a.tail_mesh)
    a.output.write_text(json.dumps(d, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({k: d[k] for k in ("kappa3", "tail", "seconds", "density_values_cached")}, indent=2))
    print(json.dumps(quick_verify(a.output), indent=2))


if __name__ == "__main__":
    main()
