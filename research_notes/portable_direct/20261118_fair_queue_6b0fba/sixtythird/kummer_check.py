"""Exact finite-field and finite affine checks on the marked P11 curve (standard library)."""
import json
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import gcd, isqrt, prod

ROOTS = (0, 233**2, 119**2)
CURVE_A = -sum(ROOTS)
CURVE_B = ROOTS[1]*ROOTS[2]
H = (194089, 69872040)
BAD = 6*233*119*(233**2-119**2)
RADICANDS = (-1, 627, 17*233, 6*233)


def primes_to(n):
    bits = bytearray([1])*(n+1)
    bits[:2] = bytes(2)
    for j in range(2, isqrt(n)+1):
        if bits[j]:
            bits[j*j::j] = bytes((n-j*j)//j+1)
    return [j for j in range(2, n+1) if bits[j]]


def add(p, u, v):
    if u is None:
        return v
    if v is None:
        return u
    x, y = u
    z, w = v
    if x == z:
        if (w+y) % p == 0:
            return None
        slope = (3*x*x + 2*CURVE_A*x + CURVE_B)*pow(2*y, -1, p) % p
    else:
        slope = (w-y)*pow(z-x, -1, p) % p
    h = (slope*slope - CURVE_A - x - z) % p
    return h, (slope*(x-h)-y) % p


def mul(p, n, u):
    out = None
    while n:
        if n & 1:
            out = add(p, u, out)
        u = add(p, u, u)
        n //= 2
    return out


def neg(p, u):
    return None if u is None else (u[0], -u[1] % p)


def hasse_multiple(p, u):
    radius = isqrt(4*p)
    start, stop = p+1-radius, p+1+radius
    side = isqrt(stop-start)+1
    baby = {}
    v = None
    for j in range(side):
        baby.setdefault(v,j)
        v = add(p,v,u)
    giant_step = neg(p,v)
    v = neg(p,mul(p,start,u))
    for i in range((stop-start)//side+1):
        if v in baby:
            n = start+i*side+baby[v]
            if n <= stop:
                assert mul(p,n,u) is None
                return n
        v = add(p,v,giant_step)
    raise ArithmeticError("No multiple in Hasse interval")


def order_valuations(p, u):
    multiple = hasse_multiple(p,u)
    valuations = []
    for ell in (2,3):
        n = multiple
        while n % ell == 0:
            n //= ell
        v = mul(p,n,u)
        j = 0
        while v is not None:
            v = mul(p,ell,v)
            j += 1
        valuations.append(j)
    return tuple(valuations)


def symbols(p):
    return tuple(1 if pow(z % p,(p-1)//2,p) == 1 else -1 for z in RADICANDS)


def small_check(p, u, signs, want_j):
    squares = {a*a % p:a for a in range((p+1)//2)}
    points = [None]
    for x in range(p):
        y2 = prod((x-e) for e in ROOTS) % p
        if y2 in squares:
            y = squares[y2]
            points.append((x,y))
            if y:
                points.append((x,-y % p))
    doubles = Counter(add(p,v,v) for v in points)
    a,b,c,d = signs
    n4 = sum(n for v,n in doubles.items() if v is None or v[1] == 0)
    assert n4 == (16 if a == b == 1 else 8)
    expected = (a,b,a*b)
    assert [doubles[(e%p,0)] for e in ROOTS] == [4*int(s==1) for s in expected]
    assert doubles[u] == 4*int(c==d==1)
    v = None
    for n in range(1,len(points)+1):
        v = add(p,v,u)
        if v is None:
            js = []
            for ell in (2,3):
                j = 0
                while n % ell == 0:
                    n //= ell
                    j += 1
                js.append(j)
            assert want_j == tuple(js)
            break
    else:
        raise AssertionError("No point order found")
    return len(points)


def square_class(n):
    d, out = 2, -1 if n<0 else 1
    n = abs(n)
    while d*d <= n:
        odd = False
        while n % d == 0:
            odd = not odd
            n //= d
        if odd:
            out *= d
        d += 1
    return out*n


def rank_by_det():
    counts = defaultdict(Counter)
    for a,b,c,d in product(range(3), repeat=4):
        det = (a*d-b*c) % 3
        if det:
            rank = 2 if ((1-a)*(1-d)-b*c) % 3 else int((a,b,c,d)!=(1,0,0,1))
            counts[det][rank] += 1
    tails = {}
    for det, hist in sorted(counts.items()):
        tail = (hist[1]*Fraction(3,4)+hist[0]*Fraction(12,13))/sum(hist.values())
        tails[det] = str(tail)
    assert tails == {1:'15/52', 2:'3/8'}
    finite = {}
    for e in (1,2):
        m = 3**e
        points = list(product(range(m),repeat=2))
        sizes, hits = Counter(), defaultdict(Counter)
        for a,b,c,d in product(range(m),repeat=4):
            det = (a*d-b*c)%3
            if det == 0:
                continue
            image = {(((1-a)*x-b*y)%m, (-c*x+(1-d)*y)%m) for x,y in points}
            sizes[det] += len(points)
            for k in range(e+1):
                hits[det][k] += sum(((3**k*x)%m,(3**k*y)%m) not in image for x,y in points)
        f = lambda n: Fraction(1,4)+Fraction(3,4*9**n)
        def failure(n,k):
            if n<=k:
                return Fraction(0)
            g = failure(n-1,k-1) if k else 1-(1-failure(n-1,0))/9
            return (32*((1-f(n-k))/3**k)+g)/81
        for det in (1,2):
            for k in range(e):
                g = failure(e-1,k-1) if k else 1-(1-failure(e-1,0))/9
                expectation = (counts[det][1]*(1-f(e-k))/3**k+counts[det][0]*g)/24
                assert Fraction(hits[det][k],sizes[det]) == expectation
        finite[e] = {det:{"pairs":sizes[det], "fail_count_by_k":dict(hits[det])} for det in (1,2)}
    return {"rank_counts_for_I_minus_A":dict(counts), "tail_coefficients":tails,"finite_images":finite}


def sample(limit):
    joint = defaultdict(Counter)
    by_cell = defaultdict(Counter)
    by_det = defaultdict(Counter)
    point_tests = []
    for p in primes_to(limit):
        if BAD % p == 0:
            continue
        u = H[0] % p, H[1] % p
        signs = symbols(p)
        j2,j = order_valuations(p,u)
        joint[j2][j] += 1
        key = ''.join('+' if s==1 else '-' for s in signs)
        by_cell[key][j] += 1
        by_det[p%3][j] += 1
        if p <= 1200:
            point_tests.append(small_check(p,u,signs,(j2,j)))
    assert len(by_cell) == 16
    return {"upper_inclusive":limit, "good_primes":sum(sum(v.values()) for v in by_det.values()),
            "small_primes_full_curve_count":len(point_tests), "small_curve_points_checked":sum(point_tests),
            "joint_v2_rows_v3_columns":dict(joint), "v3_point_order_by_p_mod_3":dict(by_det), "v3_point_order_by_four_legendre_signs":dict(by_cell)}


def filtered_frobenius():
    rows = [
        (709,(76,87),(195,232),(94,174)),
        (1613,(306,643),(996,481),(217,795)),
        (1801,(712,496),(828,136),(338,1494)),
        (4441,(1081,1386),(241,1430),(23,276)),
        (4001,(562,3942),(605,277),(396,148))]
    generators = {0}
    certificate = []
    for p,u,v,w in rows:
        assert p in primes_to(p) and gcd(p,BAD)==1
        for x,y in (u,v,w):
            assert (y*y-prod((x-e) for e in ROOTS)) % p == 0
        n = 8 if p==4001 else 4
        assert mul(p,n//2,u)==(0,0) and mul(p,n//2,v)==(ROOTS[1]%p,0)
        assert mul(p,n,w)==(H[0]%p,H[1]%p)
        residues = [pow((z[0]-e)%p,(p-1)//2,p) for z in (u,v) for e in ROOTS[:2]]
        assert all(s in (1,p-1) for s in residues)
        bits = [int(s==p-1) for s in residues]
        code = sum(v<<i for i,v in enumerate(bits))
        if n==4:
            generators |= {a^code for a in generators}
        else:
            assert p%3==2
        certificate.append({"p":p, "level_split":n, "U":u, "V":v, "W":w, "next_bits":bits, "code":code})
    assert len(generators)==16
    assert [x["code"] for x in certificate[:4]]==[12,5,14,15]
    a,b,c,d=certificate[2]["next_bits"]
    assert (a*d-b*c)%2==1
    return certificate


@lru_cache(None)
def random_matrix_failure(n, k, restricted):
    if n<=k:
        return Fraction(0)
    if k==0:
        zero_fail = 1-(1-random_matrix_failure(n-1,0,False))/4
    else:
        zero_fail = random_matrix_failure(n-1,k-1,False)
    rank_one_fail = sum(Fraction(1,2**j)*(1-Fraction(1,2**(j-k))) for j in range(k+1,n))
    rank_one_fail += Fraction(1,2**(n-1))*(1-Fraction(1,2**(n-k)))
    return (3*rank_one_fail+zero_fail)/4 if restricted else (9*rank_one_fail+zero_fail)/16


def finite_two_adic():
    results = []
    for n in (1,2,3,4):
        mod=2**n
        vv=list(product(range(mod),repeat=2))
        size=0
        failures=Counter()
        for a,b,c,d in product(range(mod//2),repeat=4):
            if c%2 or d%2:
                continue
            image={((2*a*x+2*b*y)%mod,(2*c*x+2*d*y)%mod) for x,y in vv}
            size += len(vv)
            for k in range(n+1):
                failures[k] += sum((((2**k*x)%mod,(2**k*y)%mod) not in image) for x,y in vv)
        assert size==(4 if n==1 else 64**(n-1))
        for k in range(n+1):
            if k:
                expected=random_matrix_failure(n-1,k-1,True)
            else:
                expected=1-(1-random_matrix_failure(n-1,0,True))/4
            assert Fraction(failures[k],size)==expected
        results.append({"n":n, "affine_pairs":size,"number_failing_by_k":dict(failures)})
    return results


def main():
    roots = [(7,17*233),(10,6*233),(42,102)]
    assert [H[0]-v for v in ROOTS] == [u*u*v for u,v in roots]
    assert H[1]**2 == prod(H[0]-e for e in ROOTS)
    span = {square_class(prod(z for z,on in zip(RADICANDS,mask) if on)) for mask in product((0,1),repeat=4)}
    assert len(span)==16 and -3 not in span
    return {"curve":{"roots":ROOTS,"point":H,"low_squareclass_span":sorted(span)},
            "two_adic_generators":filtered_frobenius(), "finite_2_affine":finite_two_adic(),
            "affine_3":rank_by_det(), "curve_sample":sample(100_000)}


if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
