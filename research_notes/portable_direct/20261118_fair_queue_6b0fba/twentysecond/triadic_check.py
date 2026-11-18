"""Constant-probe decoding for the R762EJ stripe basis of the positive terminal observer."""
import itertools
import json
from random import Random

NAMES = 'ABCD'
OMIT = {('A', 0), ('A', 1), ('A', 2), ('B', 0), ('B', 1), ('C', 0), ('C', 1), ('D', 0)}
BASE_KEEP = (('B', 2), ('C', 2), ('D', 1), ('D', 2))
SHIFTS = ((0, 0, 0), (1, 0, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1), (1, 1, 1))
CUBE = tuple(itertools.product(range(3), repeat=3))


def labels(q, x, y, z):
    return ((x % q, y % q, z % q, (x-y+z) % q),
            ((y+z) % 3, (x-z) % 3, (x+y) % 3, (y+z) % 3))


def header_row(point):
    x, y, z = point
    u = x-y+z
    t, m = labels(3, x, y, z)
    row = [1, x, y, z, x*x, y*y, z*z, u*u]
    for name, r in BASE_KEEP:
        j = NAMES.index(name)
        row.append(m[j] * int(t[j] == r))
    return [v % 3 for v in row + [u//3]]


def solve(rows, values):
    """Small F3 system only (the single header has 13 columns at every q)."""
    mat = [list(row)+[v % 3] for row, v in zip(rows, values)]
    dim = len(rows[0])
    for c in range(dim):
        pivot = next(i for i in range(c, len(mat)) if mat[i][c])
        mat[c], mat[pivot] = mat[pivot], mat[c]
        mult = mat[c][c]
        mat[c] = [v*mult % 3 for v in mat[c]]
        for i, row in enumerate(mat):
            if i != c and row[c]:
                mult = row[c]
                mat[i] = [(a-mult*b) % 3 for a, b in zip(row, mat[c])]
    assert all(not any(row) for row in mat[dim:])
    return [mat[i][-1] for i in range(dim)]


class Decoder:
    def __init__(self, q, coefficient):
        self.q = q
        self.cache = {}
        self.coefficient = coefficient
        self.low = None

    def at(self, x, y, z):
        point = tuple(v % self.q for v in (x, y, z))
        if point not in self.cache:
            self.cache[point] = self.coefficient(*point) % 3
        return self.cache[point]

    def section(self, axis, h, u, t, s):
        # Fix the chosen axis at u, the D fiber at t, and the D stripe at s.
        if axis == 'X':
            z = (2*(s-u+t)) % 3
            x, y = u, u+z-t
            return (self.at(x+h, y, z) - self.at(x, y, z)) % 3
        if axis == 'Y':
            y = u
            z = (s-y) % 3
            x = t+y-z
            return (self.at(x, y+h, z) - self.at(x, y, z)) % 3
        z = u
        y = (s-z) % 3
        x = t+y-z
        return (self.at(x, y, z+h) - self.at(x, y, z)) % 3

    def dg(self, name, h, r):
        # h must be zero modulo 3; all differences are in F3.
        if h % self.q == 0:
            return 0
        sec = self.section
        def b(u):
            return (sec('Y', h, u, 1, 0) - sec('Y', h, u, 0, 0)
                    + sec('X', h, 0, 1-h, 0) - sec('X', h, 0, -h, 0))
        def d(t):
            return b(0) - sec('Y', h, 0, t+h, 1) + sec('Y', h, 0, t+h, 0)
        if name == 'B':
            return b(r) % 3
        if name == 'D':
            return d(r) % 3
        if name == 'A':
            return (sec('X', h, r, 0, 1) - sec('X', h, r, 0, 0) - d(0)) % 3
        return (d(0) - sec('Z', h, r, 0, 1) + sec('Z', h, r, 0, 0)) % 3

    def header(self):
        vals = []
        for x, y, z in CUBE:
            u = x-y+z
            r = u % 3
            carry = u//3
            slope = self.dg('D', u-r, r)
            value = self.at(x, y, z) - (y+z)*slope
            if carry:
                at = r if carry > 0 else u
                value -= carry*self.section('X', 3, 0, at, 0)
            vals.append(value % 3)
        vec = solve([header_row(pt) for pt in CUBE], vals)
        self.low = dict(zip(BASE_KEEP, vec[8:12]))

    def coord(self, name, t):
        if self.low is None:
            self.header()
        r = t % 3
        return (self.dg(name, t-r, r) + self.low.get((name, r), 0)) % 3


def indices(q):
    return [(j, t) for j in NAMES for t in range(q) if (j, t) not in OMIT]


def coefficients(q, lam, elementary):
    """An integer BRC terminal difference in K; elementary additions belong to I."""
    def read(x, y, z):
        t, m = labels(q, x, y, z)
        total = 0
        for i, j in enumerate(NAMES):
            key = (j, t[i])
            total += lam.get(key, 0)*(int(m[i] == 0)-int(m[i] == 1))
            total += sum(elementary.get((j, t[i], b), 0)*(3*int(m[i] == b)-1) for b in (0, 1))
        return total
    return read


def checks(q, rng, exhaustive=False):
    keep = indices(q)
    trials = [dict(zip(keep, a)) for a in itertools.product(range(3), repeat=len(keep))] if exhaustive else []
    if q in (9, 27):
        trials.extend({key: 1} for key in keep)
    trials.extend({key: rng.randrange(-17, 18) for key in keep} for _ in range(2))
    max_calls = 0
    for n, lam in enumerate(trials):
        elementary = {(j, t, b): rng.randrange(-11, 12) for j in NAMES
                      for t in range(q) for b in (0, 1)} if n == len(trials)-1 else {}
        wave = coefficients(q, lam, elementary)
        d = Decoder(q, wave)
        decoded = [d.coord(*key) for key in keep]
        assert decoded == [lam.get(key, 0) % 3 for key in keep]
        max_calls = max(max_calls, len(d.cache))
        assert len(d.cache) <= 83+16*len(keep)
        if n == len(trials)-1 and q <= 9:
            for pt in itertools.product(range(q), repeat=3):
                assert sum(wave(*((a-b) % q for a, b in zip(pt, move))) for move in SHIFTS) == 0
    # Compare stripe representatives, including the omitted eight, to
    # the independently constructed dense indicator span in the small groups.
    dense = None
    if q in (3, 9):
        points = list(itertools.product(range(q), repeat=3))
        lmat = [[int(labels(q,*p)[0][NAMES.index(j)] == t) for p in points] for j in NAMES for t in range(q)]
        pivots = {}
        def insert(col):
            row = list(col)
            while any(row):
                pivot = next(i for i, z in enumerate(row) if z)
                if pivot not in pivots:
                    m = row[pivot]; pivots[pivot] = [v*m % 3 for v in row]; return True
                m = row[pivot]; row = [(v-m*w) % 3 for v,w in zip(row,pivots[pivot])]
            return False
        for col in lmat: insert(col)
        line_rank = len(pivots)
        for key in keep:
            wave=coefficients(q,{key:1},{})
            assert insert([wave(*p) % 3 for p in points])
        assert (line_rank,len(pivots)) == (4*q-4,8*q-12)
        for key in OMIT:
            wave = coefficients(q, {key: 1}, {})
            dec = Decoder(q, wave)
            recovered = coefficients(q, {p:dec.coord(*p) for p in keep}, {})
            saved = pivots
            pivots = {}
            for col in lmat: insert(col)
            assert not insert([(wave(*p)-recovered(*p)) % 3 for p in points])
            pivots = saved
        dense = [line_rank, len(pivots)]
    return {"q":q, "trials":len(trials), "quotient_trits":len(keep),
            "distinct_trits_queried_for_all_coordinates":max_calls, "small_dense_ranks":dense}


def main():
    rng = Random(20261118)
    out = [checks(q, rng, q == 3) for q in (3, 9, 27, 81, 243)]
    # Random access probes at a size for which the whole q^3 array is prohibitive.
    q = 3**15
    def lam(j,t): return 0 if (j,t) in OMIT else (t + t//3 + (t//27)**2 + 2*(t//243) + NAMES.index(j)) % 3
    def wave(x,y,z):
        t,m=labels(q,x,y,z)
        return sum(lam(j,t[i])*(int(m[i]==0)-int(m[i]==1))
                   +(t[i] % 11-5)*(3*int(m[i]==1)-1) for i,j in enumerate(NAMES))
    sparse=[]
    for key in [('A',q-1),('B',q//2),('C',q-6),('D',q//3+2)]:
        d=Decoder(q,wave)
        answer=d.coord(*key)
        assert answer==lam(*key) and len(d.cache)<=99
        sparse.append({"coordinate":key,"result":answer,"distinct_trits":len(d.cache)})
    print(json.dumps({"fixed_header_columns":13,"header_upper":83,"one_coordinate_upper":99,
                      "finite_checks":out,"random_access_large_q":q,"single_requests":sparse},indent=2))


if __name__=='__main__':
    main()
