"""Describe the 250 minimum-cost twelve-point classes by their centres and two templates."""
from collections import Counter, defaultdict
from itertools import combinations, product

POINTS = list(product(range(5), repeat=3))


def translate(shape, centre):
    return frozenset(tuple((x + dx) % 5 for x, dx in zip(point, centre)) for point in shape)


def templates():
    direct = set()
    for a, b in product((2, 3), (1, 4)):
        direct.update(((a, b, 0), (b, 0, a), (0, a, b)))
    mirror = {(y, x, z) for x, y, z in direct}
    return direct, mirror


def describe(classes=None):
    direct, mirror = templates()
    translated = [(centre, sign, translate(shape, centre))
                  for centre in POINTS for sign, shape in enumerate((direct, mirror))]
    assert len({shape for _, _, shape in translated}) == 250
    if classes is not None:
        assert {sum(1 << (25*x + 5*y + z) for x, y, z in shape) for _, _, shape in translated} == set(classes)
    counts = Counter()
    allowed = [centre for centre, _, shape in translated if direct.isdisjoint(shape)]
    assert len(allowed) == len(set(allowed)) == 113
    assert set(allowed) == set(POINTS) - mirror
    for centre, sign, shape in translated:
        if not direct.isdisjoint(shape):
            continue
        lengths = [min(v, 5 - v) for v in centre if v]
        counts[len(lengths), len(set(lengths)), sign] += 1
    expected = {(2, 1, 0):24, (1, 1, 1):12, (2, 2, 0):12,
                (3, 2, 1):48, (3, 1, 0):16, (0, 0, 1):1}
    assert counts == expected
    return counts


def describe_large_classes(classes):
    """Regenerate the full low-cost 11-, 12-, and 13-point families."""
    direct, mirror = templates()
    origin = (0, 0, 0)
    representatives = defaultdict(list)
    for shape in (direct, mirror):
        full = shape | {origin}
        representatives[13, 1296].append(full)
        representatives[12, 1104].append(shape)
        for boundary in shape:
            representatives[12, 1116].append(full - {boundary})
            representatives[11, 936].append(shape - {boundary})
        for a, b in combinations(shape, 2):
            if all((x + y) % 5 == 0 for x, y in zip(a, b)):
                representatives[11, 936].append(full - {a, b})
            elif all(x != 0 or y != 0 for x, y in zip(a, b)):
                representatives[11, 944].append(full - {a, b})
    full = direct | {origin}
    pair_positions = Counter()
    for centre in POINTS:
        lengths = [min(v, 5 - v) for v in centre if v]
        for sign, shape in enumerate((direct, mirror)):
            if full.isdisjoint(translate(shape | {origin}, centre)):
                pair_positions[len(lengths), len(set(lengths)), sign] += 1
    assert pair_positions == {(2,1,0):24, (1,1,1):12, (3,2,1):48, (3,1,0):16}
    for key, shapes in representatives.items():
        generated = set()
        for shape in shapes:
            for centre in POINTS:
                mask = sum(1 << (25*x + 5*y + z) for x, y, z in translate(shape, centre))
                assert mask not in generated
                generated.add(mask)
        assert generated == set(classes[key]), key


if __name__ == '__main__':
    for orbit, count in sorted(describe().items()):
        print(*orbit, count)
