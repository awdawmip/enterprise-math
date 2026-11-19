"""Exact Gaussian endpoint and finite Farey-budget tests (standard library)."""
from collections import Counter
from functools import lru_cache
from hashlib import sha256
from math import gcd, isqrt, log, log2
import json


def multiply(z, w):
    b, a = z
    d, c = w
    return b*d-a*c, b*c+a*d


def fold(z):
    b, a = sorted(map(abs, z), reverse=True)
    g = gcd(b, a)
    return b//g, a//g


def complement(z):
    b, a = z
    return fold((b+a, b-a))


def table(limit):
    least = list(range(limit+1))
    for p in range(2, isqrt(limit)+1):
        if least[p] == p:
            for k in range(p*p, limit+1, p):
                if least[k] == k:
                    least[k] = p
    return least


def quotient(z, w):
    b, a = multiply(z, (w[0], -w[1]))
    d = sum(x*x for x in w)
    if b % d or a % d:
        return None
    return b//d, a//d


def primes_of(n, least):
    while n > 1:
        p = least[n]
        yield p
        n //= p


def primitive_atoms(height):
    return [(b,a) for b in range(2,height+1) for a in range(1,b)
            if gcd(a,b) == 1]


def calculate(height):
    # The finite construction only needs primes dividing a member of the bulk.
    radius = (6*height+4)//5
    bulk = [z for z in primitive_atoms(radius) if 10*z[1] <= 9*z[0]]
    bare = primitive_atoms(height)
    s = len(bare)
    least = table(2*radius**2)
    primes = {p for b,a in bulk for p in primes_of(b*b+a*a, least) if p > 2} | {17}

    @lru_cache(None)
    def direction(p):
        for a in range(1,isqrt(p//2)+1):
            b = isqrt(p-a*a)
            if b*b+a*a == p:
                return b,a
        raise ValueError(p)

    anchors = {}
    for p in sorted(primes):
        z = direction(p)
        b,a = z
        if 20*a < b or 10*a > 9*b:
            z = fold(multiply(z,(4,1)))
        anchors[p] = z,complement(z)
    kit = {z for pair in anchors.values() for z in pair}
    assert len(kit) == 2*len(anchors) < s and len(set(bulk)|kit) >= s
    assert all(20*a >= b and a < b for b,a in kit)
    assert all(20*(b-a) >= b for b,a in kit)  # stays away from the diagonal
    free = [z for z in bulk if z not in kit][:s-len(kit)]
    assert len(free)+len(kit) == s

    @lru_cache(None)
    def coordinates(z):
        """Actually divide the Gaussian integer; its last unit records C8."""
        remaining = z
        counts = {}
        vb = 0
        n = sum(a*a for a in z)
        if n % 2 == 0:
            remaining = quotient(remaining,(1,1))
            assert remaining is not None
            vb = 1
            n //= 2
        # A rotated kit norm can exceed the sieve range by the fixed factor 17.
        if n % 17 == 0 and n >= len(least):
            factors = [17, *primes_of(n//17,least)]
        else:
            factors = list(primes_of(n,least))
        for p in factors:
            b,a = direction(p)
            for sign in (1,-1):
                q = quotient(remaining,(b,sign*a))
                if q is not None:
                    remaining = q
                    counts[p] = counts.get(p,0)+sign
                    break
            else:
                raise ArithmeticError((z,p))
        unit = [(1,0),(0,1),(-1,0),(0,-1)].index(remaining)
        return (2*unit+vb)%8, counts

    coeff = {z:8 for z in free}
    coeff.update({z:0 for z in kit})
    ledger = Counter()
    for z in free:
        for p,k in coordinates(z)[1].items():
            ledger[p] += 8*k
    for p in [v for v in sorted(primes) if v != 17]+[17]:
        first,other = anchors[p]
        row = coordinates(first)[1]
        assert abs(row[p]) == 1 and set(row) <= {p,17}
        correction = -ledger[p]*row[p]
        coeff[first] += correction
        for q,k in row.items():
            ledger[q] += correction*k
        assert ledger[p] == 0
    assert all(k == 0 for k in ledger.values())
    # Start a single diagonal turn, then add eight paired turns at a time.
    for z in anchors[17]:
        coeff[z] += 1
    for pair in anchors.values():
        minimum = min(coeff[z] for z in pair)
        increase = 8*max(0,(8-minimum)//8)
        for z in pair:
            coeff[z] += increase
    assert len(coeff) == s and min(coeff.values()) > 0
    torsion = 0
    result = Counter()
    for z,c in coeff.items():
        k,row = coordinates(z)
        torsion += c*k
        for p,m in row.items():
            result[p] += c*m
    assert (torsion-1)%8 == 0 and not any(result.values())
    witnesses = [(b,a) for b,a in bare if 8*height <= 10*b <= 9*height
                 and 5*height <= 10*a <= 6*height and least[a*a+b*b] == a*a+b*b]
    # Bare finite search for any second carrier below the stated threshold.
    short = primitive_atoms((10*height-1)//9)
    for z in witnesses:
        p = sum(v*v for v in z)
        assert [v for v in short if (v[0]**2+v[1]**2)%p == 0] == [z]
    if height == 30:
        # Independent endpoint verification by actual primitive integer powers.
        product = (1,0)
        for z,c in coeff.items():
            power = z
            while c:
                if c % 2:
                    u,v = multiply(product,power)
                    common = gcd(u,v)
                    product = u//common,v//common
                u,v = multiply(power,power)
                common = gcd(u,v)
                power = u//common,v//common
                c //= 2
        assert product == (1,1)
    def digest(value):
        return sha256(json.dumps(value,separators=(',',':')).encode()).hexdigest()
    return {
        "height":height,"support":s,"direct_integer_endpoint":([1,1] if height == 30 else None),"kit":len(kit),"auxiliary_radius":radius,
        "obstructing_prime_atoms":len(witnesses),"prime_rectangle_sha256":digest(witnesses),
        "sample_obstruction":witnesses[:3],"lower_excess_bits_approx":round(len(witnesses)*log2(10/9),6),
        "constructed_excess_bits_approx":round(sum(log2(b/height) for b,a in coeff)-
                                              sum(log2(b/height) for b,a in bare),6),
        "constructed_mu_approx":round(sum(log(10)/log(b/a) for b,a in coeff),6),
        "endpoint_torsion":torsion%8,"endpoint_nonzero_free_coordinates":0,
        "maximum_coefficient":max(coeff.values()),"maximum_denominator":max(b for b,a in coeff),
        "formula_sha256":digest([[*z,c] for z,c in sorted(coeff.items())]),
    }


def two_atom_record():
    # Only one primitive atom has denominator 2; the next cost is 3.
    # For the smallest pair, (2+i)(3+i)=5+5i is also a direct certificate.
    candidates = primitive_atoms(3)
    assert candidates == [(2,1),(3,1),(3,2)]
    assert multiply((2,1),(3,1)) == (5,5)
    return {"optimal_denominator_product":6,"support":[[2,1],[3,1]],"product":[5,5]}


if __name__ == "__main__":
    print(json.dumps({"two_atom":two_atom_record(),
                      "farey_fronts":[calculate(h) for h in (30,60,120,220)]},
                     indent=2,sort_keys=True))
