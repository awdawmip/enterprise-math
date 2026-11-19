"""Arithmetic audits for scalar disagreement counts. Python 3, with wave 74 Smith elimination."""
import json
from collections import Counter
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations_with_replacement, product
from pathlib import Path


def valuation(value, p):
    assert value > 0
    count = 0
    while value % p == 0:
        value //= p
        count += 1
    return count


def log_order(exponents, value, p):
    return max((e - valuation(x, p) if x else 0 for e, x in zip(exponents, value)), default=0)


def layers(type_, height):
    return [sum(min(j, e) for e in type_) for j in range(height + 1)]


def class_type(image, p, height, target):
    histogram = Counter(log_order(target, x, p) for x in image)
    capacities = [valuation(sum(v for j, v in histogram.items() if j <= level), p)
                  for level in range(height + 1)]
    return type_from_capacities(capacities)


def type_from_capacities(capacities):
    columns = [capacities[j] - capacities[j - 1] for j in range(1, len(capacities))] + [0]
    return tuple(j + 1 for j in range(len(columns) - 1)
                 for _ in range(columns[j] - columns[j + 1]))


def mismatch(source, target, image_type, p, cap):
    K = max(target)
    b = layers(target, K)
    h = layers(image_type, K)
    count = sum(p ** b[min(cap, j) - 1] * (p ** h[j] - p ** h[j - 1])
                for j in range(1, K + 1))
    return 2 * p ** (sum(source) - h[-1]) * count


def decode(source, target, p, cap, distance):
    K = max(target)
    if distance == 0:
        return 0, [0] * (cap - 1)
    b = layers(target, K)
    exponent = sum(source) + valuation(2, p) - valuation(distance, p)
    residual = distance * p ** exponent // (2 * p ** sum(source))
    known = [0]
    for j in range(1, cap):
        power = p ** b[j - 1]
        assert residual % power == 0
        h = valuation(residual // power + p ** known[-1], p)
        residual -= power * (p ** h - p ** known[-1])
        known.append(h)
    assert residual == p ** b[cap - 1] * (p ** exponent - p ** known[-1])
    return exponent, known[1:]


def injections(source, target, p):
    if not source:
        return 1
    K = max(source)
    a = [sum(e >= j for e in source) for j in range(1, K + 1)] + [0]
    b = [sum(e >= j for e in target) for j in range(1, K + 1)]
    if any(x > y for x, y in zip(a, b)):
        return 0
    count = Fraction(p ** sum(x * y for x, y in zip(a, b)))
    for i in range(K):
        for j in range(a[i + 1], a[i]):
            count *= 1 - Fraction(1, p ** (b[i] - j))
    assert count.denominator == 1
    return count.numerator


def count_types(source, target, p):
    counts = {}
    for rank in range(1 + min(len(source), len(target))):
        for type_ in combinations_with_replacement(range(1, min(max(source), max(target)) + 1), rank):
            value = Fraction(injections(type_, source, p) * injections(type_, target, p),
                             injections(type_, type_, p))
            assert value.denominator == 1
            if value:
                counts[type_] = value.numerator
    return counts


def elements(type_, p):
    return list(product(*(range(p ** e) for e in type_)))


def map_value(images, u, target, p):
    return tuple(sum(x * y[i] for x, y in zip(u, images)) % p ** e
                 for i, e in enumerate(target))


def compressed_menu(source, target, p):
    W = source + target
    height = max(W)
    def shell(type_, j):
        h = layers(type_, j)
        return p ** h[j] - p ** h[j - 1]
    def times_p(type_):
        return tuple(e - 1 for e in type_ if e > 1)
    totals = [0, 0]
    for j in range(1, height + 1):
        unit_count = (p - 1) * p ** (j - 1)
        all_count = shell(W, j) - shell(target, j)
        divisible = shell(times_p(W), j) - shell(times_p(target), j)
        assert all_count % unit_count == (all_count - divisible) % unit_count == 0
        totals[0] += all_count // unit_count
        totals[1] += (all_count - divisible) // unit_count
    # Reconstruct the scalar observations on every nonvertical address by full reads.
    points = elements(W, p)
    pW = {tuple(p * z % p ** e for z, e in zip(a, W)) for a in points}
    moduli = tuple(p ** e for e in W)
    cyclic = {}
    for a in points:
        if not any(a[:len(source)]):
            continue
        members = tuple(sorted(tuple(t * z % v for z, v in zip(a, moduli))
                               for t in range(p ** log_order(W, a, p))))
        cyclic.setdefault(members, a)
    maximal = [a for a in cyclic.values() if a not in pW]
    assert [len(cyclic), len(maximal)] == totals
    dictionary = {}
    for a in maximal:
        for t in range(1, p ** log_order(W, a, p)):
            x = tuple(t * z % v for z, v in zip(a, moduli))
            if any(x[:len(source)]):
                dictionary.setdefault(x, (a, valuation(t, p)))
    assert len(dictionary) == (p ** sum(source) - 1) * p ** sum(target)
    return totals, dictionary


def word_case(source, target, p, raw_log_span, matrix_check):
    K = max(target)
    k = max(K, max(source))
    a_size, b_size = len(source), len(target)
    controls, values = elements(source, p), elements(target, p)
    allowed = [[z for z in values if log_order(target, z, p) <= e] for e in source]
    base_word = [log_order(target, v, p) for u in controls for v in values]
    menu, dictionary = compressed_menu(source, target, p)
    histogram = Counter()
    checks = 0
    written = {}
    pair_words = []
    pair_maps = []
    for images in product(*allowed):
        projections = [map_value(images, u, target, p) for u in controls]
        type_ = class_type(set(projections), p, K, target)
        histogram[type_] += 1
        h = layers(type_, K)
        word = []
        A0 = [[(p ** (k - e) if i == j else 0) for j in range(a_size)] + [0] * b_size
              for i, e in enumerate(source)]
        B0 = [[row[j] for row in images] + [(p ** e if j == i else 0) for i in range(b_size)]
              for j, e in enumerate(target)]
        if matrix_check:
            base = raw_log_span(A0 + B0, p, k) - raw_log_span(A0, p, k)
        for u, image in zip(controls, projections):
            for v in values:
                y = tuple((x - z) % (p ** e) for x, z, e in zip(v, image, target))
                entry = log_order(target, y, p)
                if matrix_check:
                    A = [row + [p ** (k - e) * x] for row, e, x in zip(A0, source, u)]
                    B = [row + [x] for row, x in zip(B0, v)]
                    actual = raw_log_span(A + B, p, k) - raw_log_span(A, p, k) - base
                    assert actual == entry
                    checks += 1
                word.append(entry)
        header = {u + v: value for (u, v), value in zip(product(controls, values), word)}
        assert all(header[x] == max(0, header[representative] - offset)
                   for x, (representative, offset) in dictionary.items())
        ds = []
        for cap in range(1, K + 1):
            d = sum(min(x, cap) != min(z, cap) for x, z in zip(word, base_word))
            assert mismatch(source, target, type_, p, cap) == d
            assert decode(source, target, p, cap, d) == (h[-1], h[1:cap])
            ds.append(d)
        written[type_] = ds
        if len(pair_words) < 40:
            pair_words.append(word)
            pair_maps.append(projections)
    named_pairs = 0
    for i in range(len(pair_words)):
        for j in range(i):
            diff = {tuple((a - b) % (p ** e) for a, b, e in zip(y, z, target))
                    for y, z in zip(pair_maps[i], pair_maps[j])}
            type_ = class_type(diff, p, K, target)
            for cap in range(1, K + 1):
                observed = sum(min(x, cap) != min(z, cap) for x, z in zip(pair_words[i], pair_words[j]))
                assert observed == mismatch(source, target, type_, p, cap)
            named_pairs += 1
    assert dict(histogram) == count_types(source, target, p)
    minimum = min(ds[-1] for t, ds in written.items() if t)
    assert minimum == 2 * (len(controls) - len(controls) // p)
    return {"p": p, "control_exponents": source, "target_exponents": target,
            "maps": sum(histogram.values()), "direct_matrix_increments": checks,
            "nonvertical_cyclic_and_maximal_read_cost_per_history": menu,
            "additional_distinct_named_map_pairs": named_pairs, "minimum_distance": minimum,
            "type_multiplicity_and_distances": [[t, count, written[t]] for t, count in sorted(histogram.items())]}


def subgroup(generators, p, K, rank):
    modulus = p ** K
    zero = (0,) * rank
    members = {zero}
    for generator in generators:
        prev = list(members)
        layer = zero
        for _ in range(1, modulus):
            layer = tuple((a + b) % modulus for a, b in zip(layer, generator))
            if layer in members:
                break
            members.update(tuple((x + y) % modulus for x, y in zip(start, layer)) for start in prev)
    return members


def reunion_check(p, K):
    m = p ** K
    target = elements((K, K), p)
    def add(x, y):
        return tuple((i + j) % m for i, j in zip(x, y))
    def coset_index(group):
        idx = {}
        reps = []
        for x in target:
            if x not in idx:
                for y in group:
                    idx[add(x, y)] = len(reps)
                reps.append(x)
        return idx, reps

    # Histories have different vertical collections and different control projections.
    examples = [((1,), (p,), [(p, 0)], [(0, p)], (1, 0), (0, 1)),
                ((1,), (1,), [(p, 0)], [], (0, 0), (1, 0)),
                ((1,), (1,), [(p, 0)], [], (0, 0), (0, p)),
                ((1,), (p,), [], [], (0, 0), (1, 0))]
    out = []
    for a, b, ms, ns, y, z in examples:
        gens1 = [a + y] + [(0,) + v for v in ms]
        gens2 = [b + z] + [(0,) + v for v in ns]
        X, Z, joined = [subgroup(g, p, K, 3) for g in (gens1, gens2, gens1 + gens2)]
        M = {v[1:] for v in X if v[0] == 0}
        N = {v[1:] for v in Z if v[0] == 0}
        J = {v[1:] for v in joined if v[0] == 0}
        P = {v[0] for v in X} & {v[0] for v in Z}
        lifts1 = {v[0]: v[1:] for v in sorted(X)}
        lifts2 = {v[0]: v[1:] for v in sorted(Z)}
        logs = [0]
        counts = []
        for level in range(1, K + 1):
            group = subgroup(ms + ns + list(M) + list(N) + [(p ** level, 0), (0, p ** level)], p, K, 2)
            labels, reps = coset_index(group)
            distance = sum((labels[v] == labels[lifts1[u]]) != (labels[v] == labels[lifts2[u]])
                           for u in P for v in reps)
            d = Fraction(1, 1 - Fraction(distance, 2 * len(P)))
            assert d.denominator == 1
            quotient = len(reps) // d.numerator
            assert quotient * d.numerator == len(reps)
            direct = {labels[j] for j in J}
            assert len(direct) == d
            counts.append(distance)
            logs.append(valuation(quotient, p))
        cotype = type_from_capacities(logs)
        predicted = tuple(sorted(K - e for e in (0,) * (2 - len(cotype)) + cotype if e < K))
        actual = class_type(J, p, K, (K, K))
        assert predicted == actual
        out.append({"first_generators": gens1, "second_generators": gens2, "control_intersection_size": len(P),
                    "vertical_sizes": [len(M), len(N), len(J)], "binary_distances": counts,
                    "merged_type": actual})
    return out


if __name__ == "__main__":
    old = Path(__file__).resolve().parents[1] / "seventyfourth" / "probes_check.py"
    spec = spec_from_file_location("r004_previous", old)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    cases = [((1,), (1,), 2, True), ((1, 2), (1, 2), 2, True),
             ((1, 2), (3,), 2, True), ((3,), (1, 2), 2, True), ((2, 2), (1, 2), 2, False),
             ((1, 1), (1, 1), 3, True), ((1, 2), (2,), 3, False),
             ((2,), (1, 2), 3, False), ((1,), (2,), 5, True)]
    print(json.dumps({"full_words": [word_case(a, b, p, module.log_span, check) for a, b, p, check in cases],
                      "mergers": [dict(p=p, k=k, cases=reunion_check(p, k)) for p, k in [(2, 2), (2, 3), (3, 2)]]},
                     ensure_ascii=False, indent=2))
