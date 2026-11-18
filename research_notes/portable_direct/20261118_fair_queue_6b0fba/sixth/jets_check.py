"""Reconstruct signed native paths, tensor products and exact integer witnesses."""
import argparse
from collections import Counter, defaultdict
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, groupby, product
import json
from math import comb, prod


def jet(steps, degree):
    out = {(): 1}
    for s in steps:
        for word, count in list(out.items()):
            if len(word) < degree:
                dest = word + (abs(s),)
                out[dest] = out.get(dest, 0) + (count if s > 0 else -count)
        out = {w: v for w, v in out.items() if v}
    return out


def tensor_product(left, right, degree):
    out = Counter()
    for x, v in left.items():
        for y, z in right.items():
            if len(x) + len(y) <= degree:
                out[x + y] += v * z
    return {w: v for w, v in out.items() if v}


def dagger(w):
    return tuple(-s for s in reversed(w))


def local(bits, triad=(1, 2, 3)):
    x, y, z = triad
    orbit = (x, -y, z, -x, y, -z)
    steps = []
    for i, outer in enumerate(bits):
        a, b = orbit[i], orbit[(i + 1) % 6]
        steps.extend((b, -a) if outer else (-a, b))
    return tuple(steps)


def subsequence_coefficient(steps, target):
    counts = [1] + [0] * len(target)
    positions = {axis: [i for i in range(len(target) - 1, -1, -1) if target[i] == axis]
                 for axis in set(target)}
    for s in steps:
        sign = 1 if s > 0 else -1
        for i in positions.get(abs(s), ()):
            counts[i + 1] += sign * counts[i]
    return counts[-1]


def run_key(w):
    return tuple((axis, len(group), sum(s > 0 for s in group))
                 for axis, group in ((a, list(g)) for a, g in groupby(w, key=abs)))


def recover(poly):
    degree = max(map(len, poly))
    [word] = [w for w in poly if len(w) == degree]
    sign = poly[word]
    runs = []
    i = 0
    for axis, group in groupby(word):
        length = len(list(group))
        shorter = word[:i] + word[i + 1:]
        signed_sum = sign * poly.get(shorter, 0)
        runs.append((axis, length, (length + signed_sum) // 2))
        i += length
    return tuple(runs)


def freeze(poly):
    return tuple(sorted(poly.items()))


def run(frozen):
    out = {}
    words_checked = 0
    fibers = 0
    for alphabet, max_len in (((-2, -1, 1, 2), 6), ((-3, -2, -1, 1, 2, 3), 4)):
        for n in range(max_len + 1):
            hist = Counter()
            seen = {}
            for w in product(alphabet, repeat=n):
                poly = jet(w, n)
                key = run_key(w)
                assert recover(poly) == key
                if key in seen:
                    assert seen[key] == freeze(poly)
                else:
                    seen[key] = freeze(poly)
                hist[key] += 1
                degree_from_tensors = sum(poly.get((i,), 0) ** 2 - 2 * poly.get((i, i), 0)
                                          for i in set(map(abs, alphabet)))
                assert degree_from_tensors == n or n < 2
                words_checked += 1
            assert len(set(seen.values())) == len(seen)
            assert all(v == prod(comb(length, plus) for _, length, plus in key)
                       for key, v in hist.items())
            fibers += len(hist)
    out['full_jet_words_checked_in_two_populations'] = words_checked
    out['full_jet_class_counts_summed'] = fibers
    a, b = local((0,) * 6), local((1, 0, 0, 0, 0, 0))
    assert jet((1, -1), 2) == jet((-1, 1), 2) == {(): 1, (1, 1): -1}
    out['all_degree_collision_grade2'] = [[1, -1], [-1, 1]]
    u, v = a, b
    leading = []
    for n in range(11):
        degree = 2 * n + 2
        assert len(u) == len(v) == 12 * 2 ** n and u[0] != v[0]
        target = (1, 2) + (3,) * (2 * n)
        difference = subsequence_coefficient(u, target) - subsequence_coefficient(v, target)
        assert difference == (-1) ** n * 2 ** (n * (n + 1) // 2)
        if n <= 3:
            pu, pv = jet(u, degree), jet(v, degree)
            differing = [len(w) for w in pu.keys() | pv.keys() if pu.get(w) != pv.get(w)]
            assert min(differing) == degree
            assert pu.get(target, 0) - pv.get(target, 0) == difference
        leading.append([n, len(u), degree, difference])
        u, v = u + v, v + u
    out['n_grade_first_degree_witness_coefficient'] = leading
    f = None
    if frozen:
        spec = spec_from_file_location('frozen_local', frozen)
        f = module_from_spec(spec)
        spec.loader.exec_module(f)
    for triad in combinations(range(1, 7), 3):
        values = defaultdict(set)
        for bits in product(range(2), repeat=6):
            w = local(bits, triad)
            for d in (1, 2, 3):
                p = jet(w, d)
                values[d].add(freeze(p))
                split = 5
                assert p == tensor_product(jet(w[:split], d), jet(w[split:], d), d)
                assert jet(dagger(w), d) == {k[::-1]: v * (-1) ** len(k) for k, v in p.items()}
                if f and triad == (1, 2, 3):
                    frozen_steps = f.path_steps(bits)
                    w2 = tuple((i + 1) * sign for i, sign in map(f.step_letter, frozen_steps))
                    assert w2 == w
                    assert {tuple(i - 1 for i in key): v for key, v in p.items() if len(key) == d} == f.jet(frozen_steps, d)
        assert [len(values[d]) for d in (1, 2, 3)] == [1, 27, 64]
    out['triads_times_one_cycle_branch_words'] = 20 * 64
    out['one_cycle_classes_d1_d2_d3'] = [1, 27, 64]
    if frozen:
        out['frozen_order_layer_comparisons'] = 64 * 3
    return out


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--frozen-checker', help='path to cited check_rotation_path_dagger_jet.py')
    print(json.dumps(run(parser.parse_args().frozen_checker), indent=2))
