"""Certified pruning bounds for finite 2D scalar and 3D vector Fourier maps.

A reusable plan takes *distinct, fully expanded* signed wavevectors. Rows of a
field are tuples of complex (binary64) components. Keep is a Boolean per row.
The integer/rational bound is rounded upward only once on return.
"""
from collections import defaultdict
from fractions import Fraction
import math

from leray_check import exact_column_norm


def ceil_ratio(a, b):
    return -(-a // b)


def bit_ceiling(x):
    return (x - 1).bit_length()


def upward(numerator, denominator):
    if numerator < 0 or denominator <= 0:
        raise ValueError("expected a nonnegative ratio")
    try:
        value = numerator / denominator
    except OverflowError:
        return math.inf
    if math.isinf(value):
        return value
    n, d = value.as_integer_ratio()
    if n * denominator < numerator * d:
        return math.nextafter(value, math.inf)
    return value


def validated_points(points, dim, cutoff):
    points = tuple(map(tuple, points))
    if type(cutoff) is not int or cutoff < 1:
        raise ValueError("positive integer cutoff required")
    if len(set(points)) != len(points):
        raise ValueError("wavevector labels must be unique")
    for pt in points:
        if (len(pt) != dim or any(type(k) is not int or abs(k) > cutoff for k in pt)
                or not any(pt)):
            raise ValueError("full signed nonzero wavevectors in the declared box required")
    return points


def masses(rows, keep, size, dim):
    if len(rows) != size or len(keep) != size or any(type(k) is not bool for k in keep):
        raise ValueError("one row and Boolean per signed wavevector required")
    # Align the dyadic denominators once. A reduced binary64 denominator is a power of two.
    ratios, exponent = [], 0
    for row in rows:
        if len(row) != dim:
            raise ValueError("wrong number of field components")
        terms = []
        for z in row:
            if type(z) not in (float, complex):
                raise ValueError("binary64 scalar or complex required")
            parts = (z.real, z.imag)
            if not all(map(math.isfinite, parts)):
                raise ValueError("nonfinite Fourier input")
            pair = []
            for value in parts:
                n, d = abs(value).as_integer_ratio()
                e = d.bit_length() - 1
                exponent = max(exponent, e)
                pair.append((n,e))
            terms.append(pair)
        ratios.append(terms)
    aligned = [[sum(n << (exponent-e) for n,e in pair) for pair in row] for row in ratios]
    return aligned, exponent


class ScalarPlan:
    def __init__(self, points, cutoff, bits=24, *, angular=True):
        self.points = validated_points(points, 2, cutoff)
        if type(bits) is not int or bits < 1:
            raise ValueError("positive integer precision required")
        self.radial_scale = 1 << (bits + bit_ceiling(cutoff))
        self.basic = []
        shells = defaultdict(list)
        angles = []
        max_radius = 1
        for i,(x,y) in enumerate(self.points):
            d = x*x + y*y
            self.basic.append((ceil_ratio(self.radial_scale*(abs(x)+abs(y)),d), max(abs(x),abs(y))))
            if angular:
                if x < 0 or (x == 0 and y < 0):
                    x,y = -x,-y
                angles.append((x == 0, Fraction(y,x) if x else 0))
                shells[d].append((i,x,y))
                max_radius = max(max_radius,d)
        self.shells = None
        if angular:
            ranks = {a:r for r,a in enumerate(sorted(set(angles)),1)}
            self.nangle = len(ranks)
            self.detail_scale = 1 << (bits+1+2*bit_ceiling(max_radius))
            self.shells = [(self.detail_scale//d, ceil_ratio(self.detail_scale,d),
                            [(i,x,y,ranks[angles[i]]) for i,x,y in shell])
                           for d,shell in sorted(shells.items())]

    def bound(self, rows, keep, *, detailed=False):
        aligned,e = masses(rows,keep,len(self.points),1)
        m = [row[0] for row in aligned]
        if detailed:
            if self.shells is None:
                raise ValueError("angular plan required")
            n = self.angular_total(m,keep)
            return upward(n,self.detail_scale << (2*e))
        a, b = [0,0], [0,0]
        for mass, (coefficient, radius), retained in zip(m,self.basic,keep):
            a[retained] += mass * coefficient
            b[retained] += mass * radius
        n = a[1]*b[0] + a[0]*b[1] + a[0]*b[0]
        return upward(n,self.radial_scale << (2*e))

    def angular_total(self, m, keep):
        all_rows, discarded = AngularTree(self.nangle), AngularTree(self.nangle)
        total = 0
        for lo,hi,shell in self.shells:
            # Equal-radius pairs contribute exactly zero, including different directions.
            for i,x,y,rank in shell:
                tree = discarded if keep[i] else all_rows
                total += m[i]*tree.contribution(rank,x,y,lo)
            for i,x,y,rank in shell:
                mx,my = m[i]*x,m[i]*y
                vector = (mx,my,hi*mx,hi*my)
                all_rows.add(rank,vector)
                if not keep[i]:
                    discarded.add(rank,vector)
        return total


class AngularTree:
    def __init__(self, count):
        self.tree = [[0]*4 for _ in range(count+1)]
        self.total = [0]*4

    def add(self, rank, values):
        for j,v in enumerate(values):
            self.total[j] += v
        while rank < len(self.tree):
            row = self.tree[rank]
            for j,v in enumerate(values):
                row[j] += v
            rank += rank & -rank

    def contribution(self, rank, x, y, current_lo):
        left = [0]*4
        while rank:
            row = self.tree[rank]
            for j,v in enumerate(row):
                left[j] += v
            rank -= rank & -rank
        sx,sy,ux,uy = [2*value - t for value,t in zip(left,self.total)]
        value = (ux-current_lo*sx)*y - (uy-current_lo*sy)*x
        assert value >= 0
        return value


class VelocityPlan:
    def __init__(self, points, cutoff):
        self.points = validated_points(points,3,cutoff)
        self.norm = exact_column_norm(cutoff)
        self.weights = [tuple(map(abs,p)) for p in self.points]

    def bound(self, rows, keep):
        m,e = masses(rows,keep,len(self.points),3)
        a,b = [[0]*3 for _ in range(2)], [[0]*3 for _ in range(2)]
        for row,vector,retained in zip(m,self.weights,keep):
            mass = sum(row)
            for j in range(3):
                a[retained][j] += row[j]
                b[retained][j] += vector[j]*mass
        terms = sum(a[1][j]*b[0][j]+a[0][j]*b[1][j]+a[0][j]*b[0][j] for j in range(3))
        return upward(self.norm.numerator*terms,self.norm.denominator << (2*e))
