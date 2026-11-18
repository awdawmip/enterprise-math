"""Marked genus-one transfer. Requires regina==7.4.1 and sympy==1.14.0."""
from collections import Counter
from functools import lru_cache, reduce
from itertools import combinations, permutations
from math import gcd, lcm
import json

import regina as R
from sympy import Matrix


def face_edges(omitted):
    return combinations([i for i in range(4) if i != omitted], 2)


def directed_edge(tet, u, v):
    i = R.Edge3.edgeNumber[u][v]
    orient = tet.edgeMapping(i)
    sign = 1 if (orient[0], orient[1]) == (u, v) else -1
    return tet.edge(i).index(), sign


@lru_cache(None)
def solid(cuts):
    t = R.Triangulation3()
    top = t.insertLayeredSolidTorus(*cuts)
    assert t.countVertices() == 1 and t.countBoundaryTriangles() == 2
    b = t.boundaryMap(2)
    matrix = Matrix(b.rows(), b.columns(), lambda i, j: b.entry(i, j).pythonValue())
    cocycles = matrix.T.nullspace()
    assert len(cocycles) == 1
    v = cocycles[0]
    denom = lcm(*[int(x.q) for x in v])
    whole = [int(x*denom) for x in v]
    divisor = reduce(gcd, whole)
    cochain = [x // divisor for x in whole]
    return t, top.index(), cochain


def read_edge(tet, values, u, v):
    i, sign = directed_edge(tet, u, v)
    return sign * values[i]


def boundary_maps(left, right):
    # Both boundaries have the two triangles opposite 3 and 2.
    perms = list(permutations(range(4)))
    for p in perms:
        if p[3] not in (2, 3):
            continue
        for q in perms:
            if q[2] != 5-p[3]:
                continue
            image = {}
            for f, perm in [(3, p), (2, q)]:
                for i, j in face_edges(f):
                    edge, sign = directed_edge(left, i, j)
                    target, other = directed_edge(right, perm[i], perm[j])
                    image.setdefault(edge, set()).add((target, sign*other))
            if len(image) == 3 and all(len(z) == 1 for z in image.values()):
                if len({next(iter(z))[0] for z in image.values()}) == 3:
                    yield p, q


def bezout(a, b):
    if b == 0:
        return (1 if a > 0 else -1), 0
    x, y = bezout(b, a % b)
    return y, x - (a//b)*y


def word_product(terms):
    out = []
    for term in terms:
        for letter in term:
            if out and out[-1] == -letter:
                out.pop()
            else:
                out.append(letter)
    return out


def power(letter, n):
    return [letter if n >= 0 else -letter] * abs(n)


def determinant(u, v):
    return u[0]*v[1] - u[1]*v[0]


def inverse(matrix, sign):
    (a, b), (c, d) = matrix
    return [[sign*d, -sign*b], [-sign*c, sign*a]]


def multiply(a, b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def arithmetic_witness(u, v):
    assert gcd(*u) == gcd(*v) == 1
    ku, kv = (u[1], -u[0]), (v[1], -v[0])
    lx = bezout(*u)
    assert u[0]*lx[0] + u[1]*lx[1] == 1 and determinant(ku, lx) == 1
    c = sum(x*y for x,y in zip(v, ku))
    d = sum(x*y for x,y in zip(v, lx))
    det = determinant(u,v)
    assert c == -det
    if abs(c) != 1:
        return det, None
    # r = y^c, s = x y^(-d). Signed indices refer to r and s.
    relators = {1: power(2, c), 2: [1] + power(2, -d)}
    D = {1: [2] + power(1, d*c), 2: power(1, c)}
    for generator, proof in D.items():
        words = []
        for i in proof:
            r = relators[abs(i)]
            words.append(r if i > 0 else [-j for j in reversed(r)])
        assert word_product(words) == [generator]
    basis = [[ku[0], kv[0]], [ku[1], kv[1]]]
    normalizer = inverse(basis, det)
    assert multiply(normalizer, basis) == [[1, 0], [0, 1]]
    return det, {'c': c, 'd': d, 'D': D, 'meridians_to_axes': normalizer}


BASE = R.Example3.threeSphere().isoSig()


def move(t, name, idx):
    e = t.edge(idx)
    if name == '3-2':
        return t.withPachner(e)
    if name == '2-0':
        return t.with20(e)
    return t.with21(e, int(name[-1]))


def descent(sig, transcript):
    # Log each kernel result in fixed operator and canonical edge order.
    if sig == BASE:
        transcript.append([sig, 'accept'])
        return []
    t = R.Triangulation3.fromIsoSig(sig)
    for name in ('3-2', '2-0', '2-1:0', '2-1:1'):
        attempted = []
        transcript.append([sig, name, attempted])
        for i in range(t.countEdges()):
            n = move(t, name, i)
            target = None if n is None else n.isoSig()
            attempted.append(target)
            if n is not None:
                assert n.size() < t.size()
                rest = descent(target, transcript)
                if rest is not None:
                    return [[name, i, target]] + rest
    transcript.append([sig, 'exhausted'])
    return None


def replay(sig, moves):
    for name, i, target in moves:
        tri = R.Triangulation3.fromIsoSig(sig)
        result = move(tri, name, i)
        assert result is not None and result.isoSig() == target
        sig = target
    assert sig == BASE


def run():
    controls = [(0,1),(1,1),(1,2),(1,3),(2,3),(3,5),(5,8)]
    stats = Counter()
    obs = []
    transcripts = {}
    signatures = {}
    for i, a in enumerate(controls):
        for b in controls[i:]:
            ta, ia, ua = solid(a)
            tb, ib, vb = solid(b)
            left, right = ta.tetrahedron(ia), tb.tetrahedron(ib)
            u = tuple(read_edge(left, ua, k, k+1) for k in (0,1))
            maps = list(boundary_maps(left, right))
            assert len(maps) == 12
            block = []
            for p, q in maps:
                v = tuple(read_edge(right, vb, p[k], p[k+1]) for k in (0,1))
                det, witness = arithmetic_witness(u, v)
                block.append(abs(det))
                tri = R.Triangulation3(ta)
                tri.insertTriangulation(tb)
                s, t = tri.tetrahedron(ia), tri.tetrahedron(ta.size()+ib)
                for f, j in ((3,p),(2,q)):
                    s.join(f, t, R.Perm4(*j))
                assert tri.isValid() and tri.isOrientable() and tri.isClosed()
                sig = tri.isoSig()
                if sig not in signatures:
                    raw = R.Triangulation3.fromIsoSig(sig)
                    h = raw.homology()
                    assert h.rank() == int(det == 0)
                    factors = [h.invariantFactor(i).pythonValue() for i in range(h.countInvariantFactors())]
                    assert factors == ([abs(det)] if abs(det) > 1 else [])
                    signatures[sig] = (raw.isSphere(), str(h))
                accepted, h1 = signatures[sig]
                expected_h1 = 'Z' if det == 0 else ('0' if abs(det) == 1 else f'Z_{abs(det)}')
                assert h1 == expected_h1 and accepted == (abs(det) == 1)
                entry = {'cuts':[a,b], 'face_maps':[''.join(map(str,z)) for z in (p,q)],
                         'u':u, 'v':v, 'det':det, 'isoSig':sig}
                if witness is not None:
                    entry.update(witness)
                    if sig not in transcripts:
                        log = []
                        trail = descent(sig, log)
                        transcripts[sig] = (trail, log)
                    trail = transcripts[sig][0]
                    if trail is not None:
                        replay(sig, trail)
                        entry['reducing_trace'] = trail
                        stats['reducing_traces'] += 1
                    stats['positive'] += 1
                elif det == 0:
                    stats['zero'] += 1
                else:
                    stats['nonunit'] += 1
                stats['gluings'] += 1
                obs.append(entry)
            c, d = b
            # Orient the boundary edges around one triangular face: the three
            # readings sum to zero. Relabelling permutes those three entries.
            spectrum = [abs(a[0]*j-a[1]*i) for i,j,_ in permutations((c,d,-c-d))]
            assert sorted(block) == sorted(spectrum+spectrum)
            if 0 < a[0] < a[1] and 0 < c < d:
                assert block.count(1) == 2*(abs(a[0]*d-a[1]*c) == 1)
    # Cross-check the height formula independently against primitive rational slopes.
    farey_counts = []
    for a, b in controls[2:]:
        for height in (11, 37, 128):
            positives = sum(2 for d in range(2, height+1) for c in range(1, d)
                            if abs(a*d-b*c) == 1)
            per_sign = [sum(1 for d in range(2,height+1)
                            if (a*d-sign)%b == 0 and 0 < (a*d-sign)//b < d)
                        for sign in (-1,1)]
            assert positives == 2*sum(per_sign)
            farey_counts.append([a,b,height,positives])
    height_totals = []
    for height in (1, 2, 3, 4, 5, 8, 13, 21):
        slopes = [(a,b) for b in range(1,height+1) for a in range(b+1) if gcd(a,b)==1]
        interior = len(slopes) - 2
        spheres = 0
        for i, (a,b) in enumerate(slopes):
            for c, d in slopes[i:]:
                spheres += 2*sum(abs(a*y-b*x)==1 for x,y,_ in permutations((c,d,-c-d)))
        assert spheres == 4*interior+4*height+12
        height_totals.append([height,interior,spheres,6*(interior+2)*(interior+3)])
    sigs = {s:{'regina_sphere':a, 'homology':h} for s,(a,h) in sorted(signatures.items())}
    return {'all_slopes_height_totals':height_totals, 'farey_counts':farey_counts, 'regina':R.versionString(), 'canonical_sphere':BASE, 'stats':dict(stats),
            'signatures':sigs, 'accepting_descent_logs':{k:v[1] for k,v in sorted(transcripts.items()) if v[0] is not None}, 'marked_gluings':obs}


if __name__ == '__main__':
    print(json.dumps(run(), ensure_ascii=False, indent=1))
