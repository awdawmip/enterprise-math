"""Exact replay of finite witness joins and their scalar congruence content."""
import itertools
import json
import math
import random
from collections import Counter


def product(left, right):
    return tuple(tuple(sum(a*b for a, b in zip(row, col)) for col in zip(*right)) for row in left)


def identity(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def alignments(blocks):
    choices = [tuple(itertools.permutations(block)) for block in blocks]
    for parts in itertools.product(*choices):
        n = sum(map(len, blocks))
        perm = list(range(n))
        for block, order in zip(blocks, parts):
            for i, j in zip(block, order):
                perm[i] = j
        yield tuple(tuple(int(j == perm[i]) for j in range(n)) for i in range(n))


def exact_hist(matrices, blocks):
    result = Counter()
    for align in itertools.product(*(alignments(b) for b in blocks)):
        value = matrices[0]
        for p, layer in zip(align, matrices[1:]):
            value = product(product(value, p), layer)
        result[value[0][0]] += 1
    return result


def scalar_content(matrices, blocks):
    # interval[i][j] composes layers from cut i to cut j with all names aligned.
    end = len(matrices)
    intervals = {}
    for i in range(end):
        mat = identity(len(matrices[i]))
        for j in range(i+1, end+1):
            mat = product(mat, matrices[j-1])
            intervals[i, j] = mat
    ideals = []
    answer = 0
    for t, partition in enumerate(blocks, 1):
        for b in partition:
            root = b[-1]
            prefix = intervals[0, t][0]
            ideal = math.gcd(*(prefix[i] - prefix[root] for i in b))
            for s, a, prior in ideals:
                if s == t:
                    continue
                bridge = intervals[s, t]
                anchor = a[-1]
                mixed = math.gcd(*(bridge[j][i] - bridge[anchor][i] -
                                   bridge[j][root] + bridge[anchor][root]
                                   for j in a for i in b))
                ideal = math.gcd(ideal, prior * mixed)
            suffix = intervals[t, end]
            right = math.gcd(*(suffix[j][0] - suffix[root][0] for j in b))
            answer = math.gcd(answer, ideal * right)
            ideals.append((t, b, ideal))
    return intervals[0, end][0][0], answer


def check(mats, blocks):
    hist = exact_hist(mats, blocks)
    baseline, content = scalar_content(mats, blocks)
    assert baseline in hist
    observed = math.gcd(*(v - baseline for v in hist))
    assert observed == content
    return baseline, content, hist


def adversarial_family(n, cuts):
    u = tuple(int(i == 0) - int(i == 1) for i in range(n))
    v = (1,) * (n-1) + (1-n,)
    left = (tuple(n + vi for vi in v),)
    right = tuple((2 + ui,) for ui in u)
    middle = tuple(tuple(n + ui*vj for vj in v) for ui in u)
    return [left] + [middle] * (cuts-1) + [right], [[tuple(range(n))]] * cuts


def main():
    # All two named-token left and right populations in {0,1,2}, binary middle.
    rows = list(itertools.product(range(3), repeat=2))
    mids = list(itertools.product(itertools.product(range(2), repeat=2), repeat=2))
    block = [[(0, 1)], [(0, 1)]]
    counts = Counter()
    for row, mid, col in itertools.product(rows, mids, rows):
        _, g, _ = check([(row,), mid, tuple((v,) for v in col)], block)
        counts[g] += 1

    rng = random.Random(122920)
    random_cases = 140
    for _ in range(random_cases):
        cuts = rng.randint(1, 4)
        widths = [rng.randint(2, 4) for _ in range(cuts)]
        sizes = [1] + widths + [1]
        matrices = [tuple(tuple(rng.randrange(4) for _ in range(b)) for _ in range(a))
                    for a, b in zip(sizes, sizes[1:])]
        partitions = []
        for n in widths:
            labels = list(range(n))
            rng.shuffle(labels)
            if n == 4 or rng.randrange(2):
                split = rng.randrange(1, n)
                partitions.append([tuple(labels[:split]), tuple(labels[split:])])
            else:
                partitions.append([tuple(labels)])
        check(matrices, partitions)

    # A binary middle with one class and two endpoint multiplicities from simple token relations.
    binary = [((2, 1, 1),), ((1, 0, 0), (0, 1, 1), (0, 1, 1)), ((2,), (1,), (1,))]
    one = [[(0, 1, 2)]]
    base, g, hist_binary = check(binary, one*2)
    assert (base, g, hist_binary) == (8, 2, {8:20, 10:16})
    # One cut can have holes even though its affine difference lattice is Z.
    hole = check([((1, 1, 2),), ((1,), (3,), (4,))], one)
    assert sorted(hole[2]) == [9, 11, 12] and hole[1] == 1

    families = []
    for n, cuts in [(3, 1), (3, 2), (3, 3), (3, 4), (4, 2), (5, 2), (7, 7), (11, 8)]:
        mats, parts = adversarial_family(n, cuts)
        baseline, g = scalar_content(mats, parts)
        assert baseline == 2*n*n * (n*n)**(cuts-1) and g == n**cuts
        rec = {'capacity': n, 'cuts': cuts, 'baseline': baseline, 'content': g}
        if math.factorial(n)**cuts <= 15000:
            hist = exact_hist(mats, parts)
            assert sorted(hist) == [baseline-g, baseline, baseline+g]
            rec['alignment_counts'] = sorted(hist.items())
        families.append(rec)

    print(json.dumps({'exhaustive_binary_middle_cases': sum(counts.values()),
                      'content_histogram': sorted(counts.items()),
                      'additional_seeded_multiblock_cases': random_cases,
                      'binary_two_cut': sorted(hist_binary.items()),
                      'single_cut_with_gap': sorted(hole[2].items()),
                      'simultaneous_cut_family': families}, indent=2))


if __name__ == '__main__':
    main()
