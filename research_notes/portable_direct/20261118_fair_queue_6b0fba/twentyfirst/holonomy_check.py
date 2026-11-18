"""Congruence lift of the signed (3,2,4) test. Only Python's standard library."""
from collections import Counter
from itertools import product
import json

I = (1, 0, 0, 1)
A0 = (1, 1, 0, 1)
B0 = (0, 1, 1, 0)


def mul(x, y, q):
    a, b, c, d = x
    e, f, g, h = y
    return ((a*e+b*g) % q, (a*f+b*h) % q, (c*e+d*g) % q, (c*f+d*h) % q)


def matrix_power(x, exponent, q):
    answer = I
    while exponent:
        if exponent % 2:
            answer = mul(answer, x, q)
        x = mul(x, x, q)
        exponent //= 2
    return answer


def inverse(x, q):
    a, b, c, d = x
    inv = pow(a*d-b*c, -1, q)
    return tuple(t*inv % q for t in (d, -b, -c, a))


def residue(x, q):
    return tuple(t % q for t in x)


def line_class(x, q):
    """Complete principal-kernel conjugacy signature for x == -I (mod 3)."""
    a, b, c, d = x
    t = (a+d)*((q+1)//2) % q
    vec = ((a-t) % q, b, c, (d-t) % q)
    depth = 1
    while depth < q and all(z % (depth*3) == 0 for z in vec):
        depth *= 3
    if depth == q:
        return (t, depth)
    a, b, c, d = (z//depth for z in vec)
    return (t, depth, a % 3, b % 3, c % 3, d % 3, (a*d-b*c) % (q//depth))


def lifts(x, q):
    return product(*(range(v % 3, q, 3) for v in x))


def bfs_orbits(q, signatures):
    generators = []
    for i in range(4):
        g = list(I)
        g[i] += 3
        generators.append((tuple(g), inverse(g, q)))
    unseen = set(signatures)
    visited_classes = set()
    while unseen:
        seed = min(unseen)
        sig = signatures[seed]
        assert sig not in visited_classes
        visited_classes.add(sig)
        unseen.remove(seed)
        stack = [seed]
        while stack:
            elt = stack.pop()
            for g, inv in generators:
                y = mul(mul(g, elt, q), inv, q)
                assert signatures[y] == sig
                if y in unseen:
                    unseen.remove(y)
                    stack.append(y)
    return len(visited_classes)


def census(n):
    q = 3**n
    scale = q//3
    p = mul(A0, B0, 3)
    minus = ((q-1), 0, 0, (q-1))
    fibers = Counter()
    for g in lifts(p, q):
        square = mul(g, g, q)
        fibers[mul(square, square, q)] += 1
    sizes, induced_sizes, induced_mass = Counter(), Counter(), Counter()
    signatures = {}
    for x in lifts(minus, q):
        sig = line_class(x, q)
        sizes[sig] += 1
        if n <= 3:
            signatures[x] = sig
        attainable = len(sig) == 2 or mul(sig[2:6], p, 3) == mul(p, sig[2:6], 3)
        assert (x in fibers) == attainable
        if attainable:
            induced_sizes[sig] += 1
            induced_mass[sig] += fibers[x]
    assert len(sizes) == scale*(13*scale-12)
    assert len(induced_sizes) == scale**2
    assert len(fibers) == scale*(scale**3+12)//13
    assert set(induced_mass.values()) == {scale**2}
    for sig, count in sizes.items():
        factor = sig[1]
        assert count == (1 if factor == q else (q//(3*factor))**2)
    result = {"n": n, "modulus": q, "induced_matrices": len(fibers),
              "all_twisted_matrices": scale**4, "induced_classes": len(induced_sizes),
              "all_twisted_classes": len(sizes), "product_lifts_per_induced_class": scale**2,
              "induced_matrix_fiber_histogram": dict(sorted(Counter(fibers.values()).items()))}
    if n <= 3:
        exact = bfs_orbits(q, signatures)
        assert exact == len(sizes)
        result["direct_conjugation_orbits"] = exact
    return result


def compose(word, q):
    out = I
    for a in word:
        out = mul(out, a, q)
    return out


def witnesses(q):
    p = mul(A0, B0, q)
    g = matrix_power(p, 3**(2*q.bit_length()), q)
    b = mul(inverse(A0, q), g, q)
    base = [A0, b]*4
    reference = compose(base, q)
    assert reference == (q-1, 0, 0, q-1)
    if q == 9:
        eta = tuple((a+3*v) % q for a, v in zip(I, b))
        inv = inverse(eta, q)
        def connect(pos):
            twists = [I]*8
            twists[pos-1], twists[7] = eta, inv
            return compose([mul(l, e, q) for l, e in zip(base, twists)], q)
        h1, h2 = connect(7), connect(6)
        assert h1 == reference != h2
        return {"A": A0, "B": b, "reference": reference, "eta": eta,
                "H_plus_edge7_minus_edge8": h1, "H_plus_edge6_minus_edge8": h2}
    x, y = (1, 3, 0, 1), (1, 0, 3, 1)
    xi, yi = inverse(x, q), inverse(y, q)
    def realize(word):
        corrected = word + [I]*(8-len(word))
        raw = []
        for i, theta in enumerate(corrected):
            suffix = compose(base[i+1:], q)
            raw.append(mul(mul(suffix, theta, q), inverse(suffix, q), q))
        hol = compose([mul(l, e, q) for l, e in zip(base, raw)], q)
        assert hol == mul(reference, compose(corrected, q), q)
        return hol
    h1, h2 = realize([x, xi, y, yi]), realize([x, y, xi, yi])
    comm = compose([x, y, xi, yi], q)
    assert comm == (10, 0, 0, 19)
    assert h1 == reference != h2 and residue(h1, 9) == residue(h2, 9)
    return {"A": A0, "B": b, "reference": reference, "commutator": comm,
            "H_cancelling_order": h1, "H_commutator_order": h2}


def main():
    group = {I}
    frontier = [I]
    while frontier:
        x = frontier.pop()
        for y in (A0, B0):
            z = mul(x, y, 3)
            if z not in group:
                group.add(z)
                frontier.append(z)
    p = mul(A0, B0, 3)
    assert len(group) == 48 and matrix_power(p, 4, 3) == (2, 0, 0, 2)
    assert matrix_power(A0, 3, 3) == I and matrix_power(B0, 2, 3) == I
    print(json.dumps({"marked_signed_image_order": len(group), "marked_product_mod3": p,
                      "census": [census(n) for n in (2, 3, 4)],
                      "mod9_witness": witnesses(9), "mod27_witness": witnesses(27)}, indent=2))


if __name__ == '__main__':
    main()
