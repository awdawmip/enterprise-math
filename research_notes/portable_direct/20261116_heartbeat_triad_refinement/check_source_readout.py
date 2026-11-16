"""Exact V38 checks for one-tree source readouts and endpoint ambiguity.

Run with Python 3 and pass the original V38 check_nonabelian_multicircuit.py.
The full four-branch rule and the designated marker are comparison assumptions.
"""
import argparse
import hashlib
import importlib.util
import itertools
from collections import Counter
from contextlib import redirect_stdout
from fractions import Fraction as F
from io import StringIO
from pathlib import Path


START = (0, 1, 2)
END = (0, 1, 3)
FLAT4, FLAT5 = (0, 1, 4), (0, 1, 5)
BEND1, BEND2 = (0, 2, 3), (1, 2, 3)
MARKED_LEFT = (1, 2, 4)
ORDER = (FLAT4, FLAT5, BEND1, BEND2)
PORTS = tuple(itertools.combinations(range(6), 3))
FRAMES = tuple(itertools.permutations(START))
V38_GIT_BLOB = "328c328d76e5766261f590afa710671b0a81f0cb"


def pinned_transport(path):
    payload = path.read_bytes()
    framed = b"blob " + str(len(payload)).encode() + b"\0" + payload
    if hashlib.sha1(framed).hexdigest() != V38_GIT_BLOB:
        raise ValueError("The V38 input does not match its pinned Git blob.")
    spec = importlib.util.spec_from_file_location("source_readout_v38", path)
    mod = importlib.util.module_from_spec(spec)
    with redirect_stdout(StringIO()):
        spec.loader.exec_module(mod)
    return mod.transport_slots


def adj(s, t):
    return len(set(s) & set(t)) == 2


def midpoints(s, t):
    assert adj(s, t)
    return [u for u in PORTS if adj(s, u) and adj(u, t)]


def histories(transport):
    branches = []
    assert tuple(midpoints(START, END)) == ORDER
    for root in ORDER:
        for left, right in itertools.product(midpoints(START, root),
                                             midpoints(root, END)):
            route = (START, left, root, right, END)
            sources = {a: a for a in START}
            for s, t in zip(route, route[1:]):
                assert adj(s, t)
                sources = transport(sources, s, t)
            branches.append((root, left, right, tuple(sources[a] for a in END)))
    assert len(branches) == len(set(branches)) == 64
    return branches


def source_and_frame_laws(branches, weights, strength):
    mass = dict(zip(ORDER, weights))
    source, frame = Counter(), Counter()
    for root, left, _, end_frame in branches:
        left_mass = F(1, 4)
        if root == FLAT4:
            left_mass = (1 - strength) / 4 + strength * (left == MARKED_LEFT)
        w = mass[root] * left_mass / 4
        source[left] += w
        frame[end_frame] += w
    assert sum(source.values()) == sum(frame.values()) == 1
    return source, frame


def five_bins(source):
    r5 = 4 * source[FLAT4]
    b1 = 4 * source[BEND2]
    b2 = 4 * source[BEND1]
    r4 = 1 - r5 - b1 - b2
    return (r4, r5, b1, b2), r4 - 4 * source[FLAT5]


def three_bins(source, flat_total, b2):
    # The omitted third category in this readout is "all other left sources".
    e = 4 * source[MARKED_LEFT] - b2
    d = 4 * source[FLAT5]
    r4 = (e + 3 * d) / 4
    return r4, flat_total - r4, (e - d) / 4


def weight_grid(den):
    for a in range(den + 1):
        for b in range(den - a + 1):
            for c in range(den - a - b + 1):
                yield tuple(F(x, den) for x in (a, b, c, den - a - b - c))


def check(transport):
    branches = histories(transport)
    strengths = (F(0), F(1, 4), F(2, 3), F(1))
    checked = Counter()
    for den in (3, 6, 10):
        for weights in weight_grid(den):
            r4, r5, _, b2 = weights
            zero_law = None
            for t in strengths:
                source, frame = source_and_frame_laws(branches, weights, t)
                recovered, product = five_bins(source)
                assert recovered == weights and product == t * r4
                assert three_bins(source, r4 + r5, b2) == (r4, r5, product)
                if r4:
                    assert product / r4 == t
                elif zero_law is None:
                    zero_law = (source, frame)
                else:
                    assert (source, frame) == zero_law
                checked[den] += 1
    assert checked == {3: 80, 6: 336, 10: 1144}

    # Each parameter point lies in the interior; both have r4*t = 1/8.
    weights_a, ta = (F(1, 4), F(1, 4), F(1, 4), F(1, 4)), F(1, 2)
    weights_b, tb = (F(3, 8), F(1, 8), F(1, 4), F(1, 4)), F(1, 3)
    sa, fa = source_and_frame_laws(branches, weights_a, ta)
    sb, fb = source_and_frame_laws(branches, weights_b, tb)
    assert fa == fb and set(fa) == set(FRAMES)
    assert five_bins(sa) != five_bins(sb)
    assert [sa[FLAT4], sb[FLAT4]] == [F(1, 16), F(1, 32)]
    print("64 distinct typed depth-two histories; all adjacent steps use pinned V38.")
    print("Exact parameter records by denominator:", sorted(checked.items()))
    print("Five-bin and three-bin recovery:", sum(checked.values()), "checks passed.")
    print("Interior endpoint collision (lexicographic frame order):",
          [str(fa[frame]) for frame in FRAMES])
    print("The two source frequencies for V=014 are 1/16 and 1/32.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("v38_source", type=Path)
    check(pinned_transport(parser.parse_args().v38_source))
