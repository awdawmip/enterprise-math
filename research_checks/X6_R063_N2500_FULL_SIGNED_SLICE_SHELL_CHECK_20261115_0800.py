"""Exact P000 V5 selected signed Z^3 shell at G=2500 (not R063 replay)."""
from collections import defaultdict
from math import factorial, isqrt


def words(v):
    total = sum(map(abs, v))
    result = factorial(total)
    for x in v:
        result //= factorial(abs(x))
    return result


def enumerate_shell(n):
    radius = isqrt(n)
    shell = {}
    for a in range(-radius, radius + 1):
        for b in range(-radius, radius + 1):
            c2 = n - a * a - b * b
            if c2 < 0:
                continue
            c = isqrt(c2)
            if c * c == c2:
                for z in ((0,) if c == 0 else (-c, c)):
                    shell[(a, b, z)] = words((a, b, z))
    return shell


def check(n):
    shell = enumerate_shell(n)
    grouped = defaultdict(list)
    for vector, count in shell.items():
        grouped[tuple(sorted(map(abs, vector)))].append(count)
    groups = []
    for key, values in sorted(grouped.items()):
        assert len(set(values)) == 1
        groups.append((key, len(values), values[0], len(values) * values[0]))
    assert sum(g[1] for g in groups) == len(shell)
    assert sum(g[3] for g in groups) == sum(shell.values())
    return shell, groups


if __name__ == '__main__':
    s25, g25 = check(25)
    assert len(s25) == 30 and sum(s25.values()) == 846
    s, groups = check(2500)
    expected = [
        ((0, 0, 50), 6, 1, 6),
        ((0, 14, 48), 24, 29078984349975, 697895624399400),
        ((0, 30, 40), 24, 55347740058143507128, 1328345761395444171072),
        ((18, 24, 40), 48, 146667819424252202137117683587961000, 7040055332364105702581648812222128000),
        ((24, 30, 32), 48, 559453321977660597511933995509550527400, 26853759454927708680572831784458425315200),
    ]
    assert groups == expected, (groups, expected)
    support_counts = {k: sum(sum(x != 0 for x in v) == k for v in s) for k in (1, 2, 3)}
    assert support_counts == {1: 6, 2: 48, 3: 96}
    assert len(s) == 150
    total = sum(s.values())
    assert total == 26860799510260072787603759892561716013678
    pair_mass = sum(b for v, b in s.items() if sum(x != 0 for x in v) <= 2)
    assert pair_mass == 1328346459291068570478
    assert total - pair_mass == 26860799510260072786275413433270647443200
    for orbit, n_endpoints, per_endpoint, contribution in groups:
        print(orbit, n_endpoints, per_endpoint, contribution)
    print('support_counts', support_counts)
    print('full_mass', total)
    print('support_le2_mass', pair_mass)
    print('PASS_X6_R063_N2500_SIGNED_Z3_SHELL_NOT_ORIGINAL_BENCHMARK')
