"""Exact path-formal BRC checks for source-labelled V17/V38 branches."""
import hashlib
import importlib.util
import itertools
import sys
from collections import Counter
from contextlib import redirect_stdout
from fractions import Fraction
from io import StringIO
from pathlib import Path


source = Path(sys.argv[1])
raw = source.read_bytes()
assert hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest() == "328c328d76e5766261f590afa710671b0a81f0cb"
spec = importlib.util.spec_from_file_location("pinned_transport", source)
native = importlib.util.module_from_spec(spec)
with redirect_stdout(StringIO()):
    spec.loader.exec_module(native)

triads = list(itertools.combinations(range(6), 3))
edges = [(s, t) for s in triads for t in triads if len(set(s) & set(t)) == 2]
initial = {}
children = {}


def parity(mapping, parent):
    positions = [parent.index(a) for a in mapping]
    return sum(a > b for i, a in enumerate(positions) for b in positions[i + 1:]) % 2


for s, t in edges:
    dst = native.transport_slots({a: a for a in s}, s, t)
    initial[s, t] = Counter({tuple(dst[b] for b in t): 1})
    children[s, t] = [u for u in triads
                      if len(set(u) & set(s)) == len(set(u) & set(t)) == 2]
    assert len(children[s, t]) == 4


def pair(left, right, pivot):
    counts = Counter()
    for m, a in left.items():
        for n, b in right.items():
            counts[tuple(m[pivot.index(k)] for k in n)] += a * b
    return counts


def next_depth(lookup):
    result = {}
    for s, t in edges:
        counts = Counter()
        for u in children[s, t]:
            counts.update(pair(lookup[s, u], lookup[u, t], u))
        result[s, t] = counts
    return result


def direct_class(s, t, u):
    x, = set(s) - set(t)
    z, = set(t) - set(s)
    if len(set(s) & set(t) & set(u)) == 2:
        return next(iter(initial[s, t]))
    k, = (set(s) & set(t)) - set(u)
    return tuple(k if v == z else x if v == k else v for v in t)


for s, t in edges:
    for u in children[s, t]:
        assert pair(initial[s, u], initial[u, t], u) == Counter({direct_class(s, t, u): 1})


def raw_leaves(s, t, depth):
    if depth == 0:
        yield (s, t)
        return
    for u in children[s, t]:
        for left in raw_leaves(s, u, depth - 1):
            for right in raw_leaves(u, t, depth - 1):
                yield left + right[1:]


def path_transport(word):
    colors = {a: a for a in word[0]}
    for a, b in zip(word, word[1:]):
        colors = native.transport_slots(colors, a, b)
    return tuple(colors[a] for a in word[-1])


def star_power(diagonal, passes):
    dist = {i: Fraction(int(i == 0)) for i in range(3)}
    for _ in range(passes):
        off = (1 - diagonal) / 2
        dist = {0: diagonal*dist[0] + off*(dist[1]+dist[2]),
                1: off*dist[0] + (1-off)*dist[1],
                2: off*dist[0] + (1-off)*dist[2]}
    return dist[0]


rows = {}
table = initial
for depth in range(1, 6):
    table = next_depth(table)
    total = 4 ** (2 ** depth - 1)
    for s, t in edges:
        hist = table[s, t]
        parent, = initial[s, t]
        assert sum(hist.values()) == total
        assert sum(n for w, n in hist.items() if parity(w, parent)) * 2 == total
        tv = sum(abs(Fraction(n,total) - Fraction(1,6)) for n in
                 (hist.get(w,0) for w in itertools.permutations(s))) / 2
        assert tv <= Fraction(2,3) * Fraction(3,4) ** (2 ** (depth-1) - 1)
        if depth <= 2:
            assert Counter(path_transport(w) for w in raw_leaves(s, t, depth)) == hist
    base = (0,1,2)
    dest = (1,2,3)
    h = table[base, dest]
    rows[depth] = (total, h[(1,2,0)], len(h))
    if depth == 2:
        assert sorted(h.values()) == [4,6,6,14,14,20]
    if depth == 1:
        pos = dest.index(3)
        stay = sum(n for w,n in h.items() if w[pos] == 0)
        assert Fraction(stay,total) == Fraction(1,2)

# Alternating coarse word S,T,S,... with one local refinement per edge.
s, t = (0,1,2),(1,2,3)
one = next_depth(initial)
for length in range(1, 25):
    current = Counter({s:1})
    for k in range(length):
        a,b = (s,t) if k % 2 == 0 else (t,s)
        current = pair(current,one[a,b],a)
    for origin in s:
        for destination in s:
            # Identify both endpoints by the direct alternating transport.
            final_axis = 3 if length % 2 and destination == 0 else destination
            final = t if length % 2 else s
            hits_named = sum(count for frame, count in current.items()
                             if frame[final.index(final_axis)] == origin)
            p = {0: -2, 1: 1, 2: 1}
            q = {0: 0, 1: 1, 2: -1}
            predicted = (Fraction(1,3)
                         + Fraction(p[origin]*p[destination],6)*Fraction(1,4)**length
                         + Fraction(q[origin]*q[destination],2)*Fraction(3,4)**length)
            assert Fraction(hits_named,4**length) == predicted
    target = t if length % 2 else s
    target_anchor = 3 if length % 2 else 0
    hits = sum(n for w,n in current.items() if w[target.index(target_anchor)] == 0)
    assert Fraction(hits,4**length) == (1+2*Fraction(1,4)**length)/3
    assert Fraction(hits,4**length) == star_power(Fraction(1,2),length)
print("directed_edges",len(edges),"two_step_branches",sum(map(len,children.values())))
print("depth, total branches, direct-frame count, distinct frames")
for d, row in rows.items():
    print(d, *row)
print("exact path enumeration at depth 1,2; recursion at depths 1..5; alternating lengths 1..24: PASS")

# Two different classifications of V38 control histories: lookup of one origin,
# and complete frame, use the actual project's two ordered loop packets.
def named_sequence(packets):
    state = {a:a for a in native.BASE}
    for packet in packets:
        state = native.loop_transport(packet,state)
    return tuple(state[a] for a in native.BASE)

A, B, Ai, Bi = native.A, native.B, native.Ai, native.Bi
C = (A, B, Ai, Bi)
assert named_sequence(C) != named_sequence((A,Ai,B,Bi))
assert all(a != b for a,b in zip(named_sequence(C), named_sequence((A,Ai,B,Bi))))
print("nine named-source/detector pairs per alternating length: PASS")
