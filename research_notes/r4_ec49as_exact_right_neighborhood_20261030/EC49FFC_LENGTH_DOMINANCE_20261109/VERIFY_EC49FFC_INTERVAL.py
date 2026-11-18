"""Exact exhaustive audit of complete BRC key horizon reuse in frozen H2..H9 model."""
import json
from collections import Counter

SCIENCE_PIN = 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'


def run():
    actual_pairs = set()
    keys = set()
    positive_pairs = set()
    for h in range(2, 10):
        for z in range(1, (h + 1) // 2 + 1):
            for t in range(h + 2 - 2 * z):
                for f in range(h + 2 - 2 * z - t):
                    g = h + 1 - 2 * z - t - f
                    x = t + 2 * z + f
                    y = t + g
                    key = (x, y, z)
                    actual_pairs.add((h, key))
                    keys.add(key)
                    if x > 0 and y > 0 and z > 0:
                        positive_pairs.add((h, key))
    histogram = Counter()
    positive_histogram = Counter()
    longest_keys = []
    for key in keys:
        x, y, z = key
        h_min = max(2, x - 1, y + 2 * z - 1)
        h_max = min(9, x + y - 1)
        expected = set(range(h_min, h_max + 1))
        observed = {h for h in range(2, 10) if (h, key) in actual_pairs}
        assert expected == observed, (key, expected, observed)
        count = len(expected)
        histogram[count] += 1
        if min(key) > 0:
            positive_histogram[count] += 1
        if count == 5:
            longest_keys.append({'key': list(key), 'horizons': sorted(expected),
                                 'native_microstep_length': 2 * (x + y + z - 1)})
        for h in expected:
            t = x + y - h - 1
            f = h + 1 - y - 2 * z
            g = h + 1 - x
            a = z - 1
            e = z
            assert min(t, f, g, a) >= 0
            assert a + t + e + f + g == h
            assert 2 * a + 4 * t + 4 * e + 2 * f + 2 * g == 2 * (x + y + z - 1)

    assert (len(actual_pairs), len(keys), len(positive_pairs)) == (294, 164, 270)
    assert sorted(histogram.items()) == [(1, 80), (2, 49), (3, 25), (4, 9), (5, 1)]
    assert sorted(positive_histogram.items()) == [(1, 56), (2, 49), (3, 25), (4, 9), (5, 1)]
    assert longest_keys == [{'key': [6, 4, 1], 'horizons': [5, 6, 7, 8, 9],
                             'native_microstep_length': 20}]
    return {
        'science_pin': SCIENCE_PIN,
        'horizons': [2, 3, 4, 5, 6, 7, 8, 9],
        'count_admissible_pairs': len(actual_pairs),
        'distinct_full_keys': len(keys),
        'strict_positive_pairs': len(positive_pairs),
        'all_key_horizon_length_histogram': dict(sorted(histogram.items())),
        'strict_positive_key_horizon_length_histogram': dict(sorted(positive_histogram.items())),
        'longest_reusable_key': longest_keys[0],
        'exact_checks': 'PASS'
    }


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, ensure_ascii=False))
