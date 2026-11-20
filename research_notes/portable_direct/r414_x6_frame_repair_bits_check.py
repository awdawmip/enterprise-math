"""Exact finite test of r414 signed-frame stabilizer and repair-bit spectrum."""
from itertools import permutations, product


def is_even(p):
    return sum(p[i] > p[j] for i in range(6) for j in range(i + 1, 6)) % 2 == 0


def apply(g, x):
    p, signs = g
    j = abs(x) - 1
    return (1 if x > 0 else -1) * signs[j] * p[j]


def run():
    G = [(p, signs) for p in permutations(range(1, 7)) if is_even(p)
         for signs in product((-1, 1), repeat=6)]
    assert len(G) == 23040
    all_axes = (1, 2, 3, 4, 5, 6)
    expected = [(23040, 15), (1920, 11), (192, 8), (24, 5),
                (4, 2), (2, 1), (1, 0)]
    for k, (size, bits) in enumerate(expected):
        suffix = all_axes[:k]
        K = [g for g in G if tuple(apply(g, x) for x in suffix) == suffix]
        orbit = {tuple(apply(g, x) for x in all_axes) for g in K}
        assert len(K) == size and len(orbit) == size
        assert (size - 1).bit_length() == bits
        print(f"k={k}, stabilizer={size}, largest_fiber={len(orbit)}, bits={bits}")
    K3 = [g for g in G if tuple(apply(g, x) for x in all_axes[:3]) == all_axes[:3]]
    orbit3 = {tuple(apply(g, x) for x in all_axes[3:]) for g in K3}
    assert len(orbit3) == 24
    print("r413 triadic candidate alphabet, L=E*: sharp 5 bits")


if __name__ == "__main__":
    run()
