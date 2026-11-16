"""Exact finite checks of the signed-X6 two-axis BRC restriction by named steps.

Uses the project's pinned signed_brc.py from the repository, a sibling, or SIGNED_BRC_PATH.
"""
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations

from check_weighted import load_signed_brc

shortest_path_multiplicity = load_signed_brc().shortest_path_multiplicity


@lru_cache(maxsize=None)
def options(n, k):
    return tuple(combinations(range(n), k))


@lru_cache(maxsize=None)
def words(n):
    result = []
    for x_positions in options(2*n, n):
        result.append("".join("X" if j in x_positions else "Y" for j in range(2*n)))
    assert len(result) == shortest_path_multiplicity((n, n, 0, 0, 0, 0))
    return tuple(result)


@lru_cache(maxsize=None)
def operator(word, k):
    """BRC alternatives are distinguished by the actual two chosen source subsets."""
    positions = {c: [i for i, step in enumerate(word) if step == c] for c in "XY"}
    n = len(positions["X"])
    assert len(positions["Y"]) == n
    branch_counts = Counter()
    for chosen_x in options(n, k):
        x = tuple(positions["X"][i] for i in chosen_x)
        for chosen_y in options(n, k):
            y = tuple(positions["Y"][i] for i in chosen_y)
            ordered_ids = sorted(x + y)
            coarse_word = "".join(word[i] for i in ordered_ids)
            branch_counts[coarse_word] += 1
    assert sum(branch_counts.values()) == len(options(n, k))**2
    return branch_counts


@lru_cache(maxsize=None)
def observables(word):
    x = [i for i, step in enumerate(word) if step == "X"]
    y = [i for i, step in enumerate(word) if step == "Y"]
    n = len(x)
    matrix = [[int(i < j) for j in y] for i in x]
    s = sum(map(sum, matrix))
    a = Q(s, n*n)
    row = [Q(sum(r), n) - a for r in matrix]
    column = [Q(sum(c), n) - a for c in zip(*matrix)]
    energy = (sum(v*v for v in row) + sum(v*v for v in column)) / n
    return s, a, energy


def variance(n):
    return Q(2*n + 1, 12*n*n)


def run():
    cells = reverse_values = semigroup_rows = uniform_rows = 0
    for n in range(2, 6):
        for k in range(1, n+1):
            total = len(options(n, k))**2
            column_mass = Counter()
            fine_tag_sum = Counter()
            integrated_loss = Q(0)
            for w in words(n):
                _, a, energy = observables(w)
                bins = operator(w, k)
                actual_mean = Q(0)
                conditional_variance = Q(0)
                for u, multiplicity in bins.items():
                    au = observables(u)[1]
                    probability = Q(multiplicity, total)
                    actual_mean += probability * au
                    conditional_variance += probability * (au - a)**2
                    column_mass[u] += multiplicity
                    fine_tag_sum[u] += multiplicity * a
                f = Q(n-k, k*(n-1))
                assert actual_mean == a
                assert conditional_variance == f*f*a*(1-a) + f*(1-f)*energy
                integrated_loss += conditional_variance
                cells += 1
                for j in range(1, k):
                    via = Counter()
                    for u, mult in bins.items():
                        for v, count in operator(u, j).items():
                            via[v] += mult * count
                    direct = operator(w, j)
                    assert set(via) == set(direct)
                    denom_via = total * len(options(k, j))**2
                    denom_direct = len(options(n, j))**2
                    assert all(value * denom_direct == direct[v] * denom_via for v, value in via.items())
                    semigroup_rows += 1
            assert integrated_loss / len(words(n)) == variance(k) - variance(n)
            assert set(column_mass) == set(words(k))
            for u in words(k):
                assert column_mass[u] * len(words(k)) == total * len(words(n))
                mean_fine = fine_tag_sum[u] / column_mass[u]
                assert mean_fine - Q(1, 2) == variance(n) / variance(k) * (observables(u)[1] - Q(1, 2))
                reverse_values += 1
            uniform_rows += 1

    def tag_bins(w, k):
        result = Counter()
        for u, multiplicity in operator(w, k).items():
            result[observables(u)[0]] += multiplicity
        return tuple(result[t] for t in range(k*k+1))

    pair = "XXYYYX", "XYXYXY"
    assert all(observables(w)[1] == Q(2, 3) for w in pair)
    assert tag_bins(pair[0], 2) == (0, 0, 6, 0, 3)
    assert tag_bins(pair[1], 2) == (0, 1, 2, 5, 1)
    assert cells == 1612
    print("pointwise mean and conditional variance:", cells)
    print("semigroup rows:", semigroup_rows)
    print("uniform pushforward and unconditional squared-error identities:", uniform_rows)
    print("pointwise reverse regression:", reverse_values)
    print("N=3 -> k=2 witness:", tuple(tag_bins(w, 2) for w in pair))


if __name__ == "__main__":
    run()
