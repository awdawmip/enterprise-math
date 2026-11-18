"""Finite checks of the exclusive-seed size calculus and block inverse. Python 3.8+."""
from collections import Counter
from itertools import product
from math import comb, gcd, prod
import json


def positive_residue(x, modulus):
    return (x - 1) % modulus + 1


def size_audit(periods):
    L = prod(periods)
    weights = [L // a for a in periods]
    apery = [
        sum(w * (residue * pow(w, -1, a) % a) for w, a in zip(weights, periods))
        for residue in range(L)
    ]
    bound = (len(periods) + 1) * L
    representable = [False] * (bound + 1)
    representable[0] = True
    for D in range(1, bound + 1):
        representable[D] = any(D >= w and representable[D - w] for w in weights)
        assert representable[D] == (D >= apery[D % L])
    bad_positive = []
    bad_background = []
    comparisons = 0
    for D in range(bound + 1):
        lowest = [w * positive_residue(D * pow(w, -1, a), a)
                  for w, a in zip(weights, periods)]
        q = (D - sum(lowest)) // L
        predicted = comb(q + len(periods), len(periods)) if q >= 0 else 0
        counted = 0
        for ns in product(*(range(w, D + 1, w) for w in weights)):
            leftover = D - sum(ns)
            if leftover < 0:
                continue
            comparisons += 1
            legal = leftover % L == 0
            assert legal == all((D - n) % a == 0 for n, a in zip(ns, periods))
            counted += legal
        assert counted == predicted
        if not counted:
            bad_positive.append(D)
        if q < 1:
            bad_background.append(D)
    F = max(apery) - L
    assert F == (len(periods) - 1) * L - sum(weights)
    assert max(bad_positive) == (len(periods) - 1) * L
    assert max(bad_background) == len(periods) * L
    return dict(periods=periods, frobenius=F, D_checked_through=bound,
                size_vector_comparisons=comparisons, largest_impossible=max(bad_positive),
                largest_impossible_with_background=max(bad_background))


def common_rotations():
    # An entry records copy identity and both inactive labels; -1 denotes active.
    sites = ([(0, -1, b) for b in range(3)] +
             [(c, a, -1) for c in (1, 2) for a in range(2)] +
             [(3, a, b) for a in range(2) for b in range(3)])
    inverse = {s: j for j, s in enumerate(sites)}
    rotations = []
    for t in range(6):
        row = []
        for c, a, b in sites:
            moved = (c, (a + t) % 2 if a >= 0 else -1, (b + t) % 3 if b >= 0 else -1)
            row.append(inverse[moved])
        rotations.append(row)
    return sites, rotations


def fiber_orders(a, b):
    entries = []
    for i, j in product(range(a), range(b)):
        mult = 1 + int((i, j) in ((0, 0), (1, 1))) - int((i, j) in ((0, 1), (1, 0)))
        entries += [(i, j)] * mult
    seen_a, seen_b = Counter(), Counter()
    orders = []
    for i, j in entries:
        orders.append(((seen_a[j] - i) % a, (seen_b[i] - j) % b))
        seen_a[j] += 1
        seen_b[i] += 1
    assert list(seen_a.values()) == [a] * b and list(seen_b.values()) == [b] * a
    return entries, orders


def histogram(counts, space):
    h = Counter(counts.values())
    if len(counts) < space:
        h[0] = space - len(counts)
    return h


def crt_weights(moduli):
    M = prod(moduli)
    return [M // n * pow(M // n, -1, n) for n in moduli]


def fiber_experiment(seed, fault, x, k, sites, rotations):
    D = len(sites)
    a, b, low, a_blocks, other, n = [(2, 17, 23, 3, 3, 3), (3, 19, 31, 4, 2, 4)][seed]
    A = a_blocks * a
    perm = [(7 * z + 3) % low for z in range(low)]
    domain = []
    for t in range(a_blocks):
        domain.append(perm[t * a:(t + 1) * a])
    domain.append(perm[A:])
    inv = {point: (block, y) for block in domain for y, point in enumerate(block)}
    e, rho = fiber_orders(a, b)
    if fault != 'none':
        u, v = rho[0]
        rho[0] = ((u + int('a' in fault)) % a, (v + int('b' in fault)) % b)
    left = Counter((j, (i + u) % a) for (i, j), (u, v) in zip(e, rho))
    right = Counter((i, (j + v) % b) for (i, j), (u, v) in zip(e, rho))
    h_a, h_b = histogram(left, a*b), histogram(right, a*b)
    moduli = [low, a, b, other, D]
    weights = crt_weights(moduli)
    ordinary, seed_targets, useful, seed_useful = Counter(), Counter(), Counter(), Counter()
    for l in range(low):
        source_low = (k - l) % low
        block, y = inv[source_low]
        on_a = len(block) == a
        ci, cj = (y, 0) if on_a else (0, y)
        for (i, j), (u, v) in zip(e, rho):
            hbase = l * weights[0] + u * weights[1] + v * weights[2]
            ordinary_c = ((ci + i) % a, (cj + j) % b)
            high = block[(y + x - hbase) % len(block)]
            ordinary[ordinary_c + (high,)] += 1
            useful[ordinary_c] += 1
            for tau in range(D):
                h = hbase + tau * weights[4]
                clock = x - h
                sp = sites[(x - tau) % D]
                moved = rotations[clock % 6][(x - tau) % D]
                z = (5 * moved + 2) % D
                if sp[1 + seed] < 0:
                    c = ordinary_c
                    target_high = block[(y + clock) % len(block)]
                else:
                    c = ((sp[1 + seed] + i) % a, j)
                    target_high = source_low
                seed_targets[c + (target_high, z)] += 1
                seed_useful[c] += 1
    assert set(useful.values()) == {low} and set(seed_useful.values()) == {low * D}
    h_ord = histogram(ordinary, low * a * b)
    h_seed = histogram(seed_targets, D * low * a * b)
    for r in set(h_a) | set(h_b) | set(h_ord) | set(h_seed):
        assert h_ord[r] == A*h_a[r] + (low-A)*h_b[r]
        assert h_seed[r] == ((D-n)*low+n*A)*h_a[r] + n*(low-A)*h_b[r]
    return {'seed': seed + 1, 'fault': fault, 'ordinary_histogram': dict(h_ord),
            'seed_histogram': dict(h_seed), 'ordinary_c_multiplicity': low,
            'seed_c_multiplicity': low * D}


def max_matching(edges):
    adj = {}
    for l, r in edges:
        adj.setdefault(l, []).append(r)
    taken = {}
    def extend(l, seen):
        for r in adj[l]:
            if r in seen:
                continue
            seen.add(r)
            if r not in taken or extend(taken[r], seen):
                taken[r] = l
                return True
        return False
    return sum(extend(l, set()) for l in adj)


def repair_instance():
    from itertools import combinations
    shifts = list(product(range(2), range(3)))
    edges = [((j, (i + int((i, j) == (1, 0))) % 2),
              (i, (j + 2 * int((i, j) == (0, 2))) % 3)) for i, j in shifts]
    def paired(sub):
        return all(len({edges[t][s] for t in sub}) == len(sub) for s in range(2))
    exhaustive = max(r for r in range(7) if any(paired(t) for t in combinations(range(6), r)))
    assert exhaustive == max_matching(edges) == 4
    return {'entries': 6, 'left_holes': 6-len({e[0] for e in edges}),
            'right_holes': 6-len({e[1] for e in edges}), 'minimum_joint_edits': 6-exhaustive}


def main():
    sites, rotations = common_rotations()
    R = rotations[1]
    assert all(R[s] != s for s in range(13))
    lam = lambda s: (5 * s + 2) % 13
    assert not any(all(lam(R[s]) == (u * lam(s) + v) % 13 for s in range(13))
                   for u in range(1, 13) for v in range(13))
    rows = []
    for seed, fault in product(range(2), ('none', 'a', 'b', 'ab')):
        row = fiber_experiment(seed, fault, -5, 18, sites, rotations)
        assert row == fiber_experiment(seed, fault, 9, 7, sites, rotations)
        rows.append(row)
    noncoprime = []
    for periods in ((2, 2), (4, 6), (4, 6, 9)):
        L = prod(periods)
        lcm = 1
        for a in periods:
            lcm = lcm * a // gcd(lcm, a)
        counts = Counter(sum((L//a)*t for a,t in zip(periods,ts)) % L
                         for ts in product(*(range(a) for a in periods)))
        assert set(counts) == set(range(0,L,L//lcm))
        assert set(counts.values()) == {L//lcm}
        noncoprime.append(dict(periods=periods, image_size=lcm, residue_multiplicity=L//lcm))
    shear_checks = 0
    for r in (23, 31):
        for clock, k, high, h in product((-52, -1, 0, 38), range(r), range(r), (-1003, -1, 0, 1, 2221)):
            initial = clock + (k-clock) % r + r*high
            shifted = clock+h + ((k+h) % r - clock-h) % r + r*high
            assert (initial+h-shifted) % (r*r) == 0
            shear_checks += 1
    p = 211
    h = (p*p-1)//6
    assert gcd(2,2)==2 and all((6-n) % 2 == 0 for n in (2,2)) and (6-2-2)%4 != 0
    res = {
        'source_example': {'p': p, 'D': p**4, 'sector_size': p*p, 'least_active_sizes': [3,4],
                           'feasible_size_vectors': h*h, 'minimal_labeled_region_pairs': comb(p*p,3)*comb(p*p,4)},
        'semigroup_checks': [size_audit(x) for x in ((2,3), (2,5), (3,4), (2,3,5), (3,4,5))],
        'shear_translations_checked': shear_checks, 'noncoprime_images': noncoprime,
        'noncoprime_counterexample': {'periods': [2,2], 'D': 6, 'active_sizes': [2,2]},
        'reduced_model': {'horizontal_group': 'Z/13', 'bases_x_low': [[-5,18],[9,7]], 'same_z_both_seeds': True,
                          'lambda_s': '(5*s+2) mod 13', 'rotation_cycles': [2,2,3,6],
                          'seed_a_b_low':[ [2,17,23], [3,19,31]], 'histograms': rows},
        'minimal_joint_repair': repair_instance()
    }
    print(json.dumps(res, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
