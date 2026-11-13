"""Author-side exact test: a chart loop need not be the identity on X6
axis labels, although it preserves signed shortest-path BRC.  This is a
standalone recomputation of the selected live A6 chart consumer, not an
execution of the original import or a native admission.
"""
from collections import Counter
from itertools import combinations, product
from math import factorial

D = 6
AX = frozenset(range(D))
CHARTS = tuple(frozenset(s) for s in combinations(range(D), 3))
ID = tuple(range(D))


def compose(p, q):
    return tuple(p[q[i]] for i in range(D))


def even_lift(S, T):
    assert len(S & T) == 2
    a, b = next(iter(S - T)), next(iter(T - S))
    c, d = sorted(AX - (S | T))
    p = list(ID)
    p[a], p[b] = p[b], p[a]
    p[c], p[d] = p[d], p[c]
    return tuple(p)


def cycle_type(p):
    unseen = set(range(D))
    sizes = []
    while unseen:
        x = next(iter(unseen))
        orbit = []
        while x not in orbit:
            orbit.append(x)
            x = p[x]
        for a in orbit:
            unseen.discard(a)
        if len(orbit) > 1:
            sizes.append(len(orbit))
    return tuple(sorted(sizes))


def action(p, z):
    ans = [0] * D
    for i, v in enumerate(z):
        ans[p[i]] = v
    return tuple(ans)


def native_G(z):
    return sum(x*x for x in z)


def T(z):
    return sum(abs(x) for x in z)


def brc(z):
    return factorial(T(z)) // __import__('math').prod(factorial(abs(x)) for x in z)


def main():
    triangles = []
    for S, U, V in combinations(CHARTS, 3):
        if len(S & U) != 2 or len(U & V) != 2 or len(V & S) != 2:
            continue
        h = compose(even_lift(V, S), compose(even_lift(U, V), even_lift(S, U)))
        triangles.append((S, U, V, h))
    assert len(triangles) == 120
    types = Counter(cycle_type(t[3]) for t in triangles)
    assert types == {(): 60, (2, 2): 60}, types
    domain = tuple(product(range(-2, 3), repeat=6))
    assert len(domain) == 15625
    total = changed = fixed_curved = 0
    witness = None
    for S, U, V, h in triangles:
        for z in domain:
            w = action(h, z)
            assert native_G(z) == native_G(w)
            assert T(z) == T(w)
            assert brc(z) == brc(w)
            total += 1
            if w != z:
                changed += 1
                if witness is None:
                    witness = {'charts': tuple(tuple(sorted(x)) for x in (S, U, V, S)),
                               'axis_map': h, 'source': z, 'mapped': w,
                               'G': native_G(z), 'T': T(z), 'BRC': brc(z)}
            elif h != ID:
                fixed_curved += 1
    assert total == 1875000
    assert changed == 900000
    assert fixed_curved == 37500
    assert all(h == ID for S,U,V,h in triangles if cycle_type(h) == ())
    print('PASS_X6_LP28_CHART_A6_BRC_TYPED_HOLONOMY')
    print('triangle_classes', dict(types))
    print('native_vectors_per_triangle', len(domain))
    print('norm_length_brc_triplets_checked', total)
    print('coordinate_changed_by_nontrivial_holonomy', changed)
    print('coordinate_fixed_by_nontrivial_holonomy', fixed_curved)
    print('exact_first_witness', witness)


if __name__ == '__main__':
    main()
