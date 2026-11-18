"""Exact checks of root balls, projection fibres and common-factor lifts."""
from collections import Counter, defaultdict
from itertools import product
import json


def balls(p, k, A):
    """Disjoint cosets (residue, precision) modulo p**k."""
    A %= p**k
    if A == 0:
        return [(0, (k + 1) // 2)]
    a, u = 0, A
    while u % p == 0:
        a, u = a + 1, u // p
    if a % 2:
        return []
    b, c = a // 2, k - a
    if p == 2:
        if u % (2**min(c, 3)) != 1:
            return []
        if c <= 2:
            return [(2**b, b+1)]
        rho = 1
        for j in range(3, c):
            rho += (((u - rho*rho) // 2**j) % 2) * 2**(j-1)
        precision = k - b - 1
    else:
        rho = next((r for r in range(1, p) if (r*r-u) % p == 0), None)
        if rho is None:
            return []
        for j in range(1, c):
            digit = (u - rho*rho) // p**j * pow(2*rho, -1, p) % p
            rho += digit * p**j
        precision = k - b
    base = p**b * rho
    return [(base % p**precision, precision), (-base % p**precision, precision)]


def unit_square_count(p, h):
    if p == 2:
        return 2**max(0, h-3)
    return (p-1)*p**(h-1)//2


def fibre(p, ell, pieces, k, r):
    return sum(p**(ell - max(k, q)) for v, q in pieces if (r-v) % p**min(k, q) == 0)


def root_checks():
    layers = projections = square_classes = 0
    for p, max_level in ((2, 9), (3, 6), (5, 4), (7, 3)):
        all_roots = {}
        for k in range(1, max_level+1):
            mod = p**k
            grouped = defaultdict(list)
            for x in range(mod):
                grouped[(x*x) % mod].append(x)
            all_roots[k] = grouped
            labels = set()
            for A in range(mod):
                actual = grouped.get(A, [])
                predicted = sorted(x for v, q in balls(p, k, A) for x in range(v, mod, p**q))
                assert actual == predicted
                if A % p == 0:
                    labels.add(tuple(actual))
                # Independent unordered monic-factor count by actual pairs of roots.
                pairs = {tuple(sorted((r, -r % mod))) for r in actual}
                fixed = sum((2*r) % mod == 0 for r in actual)
                assert len(pairs) == (len(actual) + fixed)//2
                layers += 1
            if k >= 2:
                assert len(labels) == 2 + sum(unit_square_count(p, k-2*b) for b in range(1,(k-1)//2+1))
                square_classes += 1
        for ell in range(2, max_level+1):
            for A in range(p**ell):
                actual = all_roots[ell].get(A, [])
                parts = balls(p, ell, A)
                for k in range(1, ell):
                    mod = p**k
                    projected = Counter(x % mod for x in actual)
                    for r in all_roots[k].get(A % mod, []):
                        assert projected[r] == fibre(p, ell, parts, k, r)
                        projections += 1
    return {'constant_residue_layer_cases': layers, 'individual_projection_fibres': projections,
            'fixed_input_coarsest_class_counts': square_classes}


def mult(g, h, modulus):
    out = [0]*(len(g)+len(h)-1)
    for i,a in enumerate(g):
        for j,b in enumerate(h):
            out[i+j] = (out[i+j]+a*b) % modulus
    return out


def trim(f, p):
    f = [v % p for v in f]
    while f and f[-1] == 0:
        f.pop()
    return f


def rem(g, h, p):
    out = trim(g, p)
    while len(out) >= len(h):
        c = out[-1] * pow(h[-1], -1, p)
        off = len(out)-len(h)
        for j,b in enumerate(h):
            out[off+j] -= c*b
        out = trim(out, p)
    return out


def gcdpoly(g, h, p):
    a, b = list(g), list(h)
    while b:
        a, b = b, rem(a, b, p)
    return [(v*pow(a[-1], -1,p)) % p for v in a]


def factor_checks():
    count = 0
    for p in (2,3):
        for r,s in product((1,2), repeat=2):
            Xs, Ys = list(product(range(p), repeat=r)), list(product(range(p), repeat=s))
            for ga, ha in product(Xs,Ys):
                g, h = ga+(1,), ha+(1,)
                d = gcdpoly(g,h,p)
                base = mult(g,h,p**3)
                defect_counts = Counter()
                for x,y in product(Xs,Ys):
                    G = [u+p*p*v for u,v in zip(g,x)] + [1]
                    H = [u+p*p*v for u,v in zip(h,y)] + [1]
                    f = mult(G,H,p**3)
                    R = tuple(((v-u) % (p**3))//(p*p) for v,u in zip(f[:-1],base[:-1]))
                    defect_counts[R] += 1
                for R in product(range(p), repeat=r+s):
                    expected = 0 if rem(R,d,p) else p**(len(d)-1)
                    assert defect_counts[R] == expected
                    count += 1
    return count



def multiple_factor_checks():
    count = 0
    for p in (2,3):
        # The same literal multiplication also covers coincident factors in characteristic 2.
        for degrees in ((1,1,1),(1,1,2)):
            arrays = [list(product(range(p), repeat=d)) for d in degrees]
            for coefficients in product(*arrays):
                gs = [v+(1,) for v in coefficients]
                total = [1]
                for g in gs:
                    total = mult(total, g, p*p)
                omitted = []
                for i in range(len(gs)):
                    v = [1]
                    for j,g in enumerate(gs):
                        if i != j:
                            v = mult(v,g,p)
                    omitted.append(v)
                d = omitted[0]
                for v in omitted[1:]:
                    d = gcdpoly(d,v,p)
                seen = Counter()
                for changes in product(*arrays):
                    actual = [1]
                    for g,x in zip(gs, changes):
                        G = [a+p*b for a,b in zip(g,x)] + [1]
                        actual = mult(actual,G,p*p)
                    R = tuple(((v-u) % (p*p))//p for u,v in zip(total[:-1],actual[:-1]))
                    seen[R] += 1
                for R in product(range(p),repeat=sum(degrees)):
                    assert seen[R] == (0 if rem(R,d,p) else p**(len(d)-1))
                    count += 1
    return count


def second_digit_checks():
    records = {}
    for p,g in ((3,(1,0,1)),(5,(2,0,1))):
        base = mult(g,g,p**3)
        d = len(g)-1
        assert all(sum(a*r**i for i,a in enumerate(g)) % p for r in range(p))
        mod = p**3
        arrays = list(product(range(p), repeat=d))
        for C in arrays:
            f = list(base)
            for i, v in enumerate(C):
                f[i] = (f[i]+p*p*v) % mod
            actual = 0
            for changes in product(range(p*p),repeat=d):
                G = [v+p*w for v,w in zip(g,changes)] + [1]
                # Monic division over Z/p^3, no finite-field choice made.
                actual += not rem(f,G,mod)
            aliases = sum(not rem([v+(C[i] if i<d else 0) for i,v in enumerate(mult(A,A,p))],list(g),p)
                          for A in arrays)
            assert actual == p**d * aliases
            records[(p,C)] = actual
    return {'instances': len(records), 'mod125_counts_C_x_zero_minus_one':
            [records[(5,C)] for C in ((0,1),(0,0),(4,0))]}

if __name__ == '__main__':
    result = root_checks()
    result['labelled_two_factor_defect_cases'] = factor_checks()
    result['labelled_three_factor_defect_cases'] = multiple_factor_checks()
    result['repeated_irreducible_second_digit'] = second_digit_checks()
    result['mod125_at_p5'] = {str(A): sorted(x for v,q in balls(5,3,A) for x in range(v,125,5**q))
                              for A in (0,25,50)}
    result['x2_minus_25_mod625_to125'] = dict(Counter(x % 125 for v,q in balls(5,4,25)
                                                        for x in range(v,625,5**q)))
    print(json.dumps(result, indent=2))
