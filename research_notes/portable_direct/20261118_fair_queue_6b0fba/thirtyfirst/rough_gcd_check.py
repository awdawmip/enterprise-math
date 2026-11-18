"""Windowed prime-product GCD. Python 3 and python-flint 0.9.0, exact arithmetic."""
import json
from math import comb, gcd, isqrt, prod

from flint import fmpq, fmpq_poly, fmpz, fmpz_mat, fmpz_mod_poly_ctx


def product_tree(polys):
    layers = [polys]
    while len(polys) > 1:
        polys = [polys[i]*polys[i+1] if i+1 < len(polys) else polys[i]
                 for i in range(0, len(polys), 2)]
        layers.append(polys)
    return layers


def consecutive(left, right, modulus):
    """Product on (left,right] by monic multipoint evaluation over a composite ring."""
    length = right-left
    if length == 0:
        return 1 % modulus
    b = isqrt(length)
    ring = fmpz_mod_poly_ctx(modulus)
    g = product_tree([ring([j, 1]) for j in range(1, b+1)])[-1][0]
    blocks = length//b
    nodes = product_tree([ring([-left-i*b, 1]) for i in range(blocks)])
    remainders = [g % nodes[-1][0]]
    for layer in reversed(nodes[:-1]):
        remainders = [remainders[i//2] % node for i, node in enumerate(layer)]
    value = 1
    for r in remainders:
        value = value*int(r[0]) % modulus
    for n in range(left+blocks*b+1, right+1):
        value = value*n % modulus
    return value


def descend(d, x, y):
    target, leaves = 1, []
    while d > 1 and gcd(d, consecutive(x, y, d)) > 1:
        left, right = x, y
        while right-left > 1:
            mid = (left+right)//2
            if gcd(d, consecutive(left, mid, d)) > 1:
                right = mid
            else:
                left = mid
        p = gcd(d, right)
        leaves.append([right, p])
        if x < p <= y:
            target *= p
        while d % p == 0:
            d //= p
    return target, leaves


def integer_roots(coefficients, left, right):
    """Sturm at half-integers, retaining integer candidates in [left,right]."""
    poly = fmpq_poly(coefficients)
    if poly.degree() <= 0:
        return []
    poly = poly // poly.gcd(poly.derivative())
    chain = [poly, poly.derivative()]
    while chain[-1].degree() > 0:
        r = -(chain[-2] % chain[-1])
        chain.append(r / abs(r.leading_coefficient()))
    def variation(edge):
        z = fmpq(2*edge-1, 2)
        signs = [1 if v>0 else -1 for f in chain if (v := f(z))]
        return sum(a != b for a,b in zip(signs, signs[1:]))
    roots = []
    def visit(a,b,va,vb):
        if va <= vb:
            return
        if b == a+1:
            if poly(a) == 0:
                roots.append(a)
            return
        mid = (a+b)//2
        vm = variation(mid)
        visit(a,mid,va,vm)
        visit(mid,b,vm,vb)
    visit(left,right+1,variation(left),variation(right+1))
    return roots


def parameters(d, lower, dimension=None):
    n = dimension or max(2, d.bit_length())
    m = max((i for i in range(1,n) if d**i <= lower**n), default=1)
    quotient = lower**(2*m*n) // d**(m*(m+1))
    radius = int(fmpz(quotient).root(n*(n-1))) // 4
    return n, m, radius


def lattice_window(d, x, y, dimension=None):
    if d <= x:
        return 1, {"blocks": 0}
    lower = x+1
    n, m, radius = parameters(d, lower, dimension)
    if radius < 1:
        return prod(v for v in range(lower,y+1) if d%v == 0), {"direct_fallback":True}
    hits = []
    blocks = 0
    for c in range(lower, y+1, radius+1):
        b = min(radius,y-c)
        if b == 0:
            if d%c == 0:
                hits.append(c)
            blocks += 1
            continue
        rows = []
        for i in range(n):
            power, shift = min(i,m), max(0,i-m)
            scalar = d**max(0,m-i)
            row = [0]*n
            for j in range(power+1):
                k = shift+j
                row[k] = scalar*comb(power,j)*c**(power-j)*b**k
            rows.append(row)
        basis = fmpz_mat(rows)
        reduced, transform = basis.lll(transform=True,gram="exact")
        assert transform*basis == reduced
        v = [int(reduced[0,j]) for j in range(n)]
        assert n*sum(t*t for t in v) < lower**(2*m)
        assert any(v) and all(a % b**j == 0 for j,a in enumerate(v))
        for offset in integer_roots([a//b**j for j,a in enumerate(v)],0,b):
            if d%(c+offset)==0:
                hits.append(c+offset)
        blocks += 1
    return prod(hits), dict(n=n,m=m,radius=radius,blocks=blocks,hits=hits)


def prime(n):
    return n>1 and all(n%i for i in range(2,isqrt(n)+1))


def main():
    arithmetic = 0
    for d in (16,27,35,49,77,121,125,1001):
        for x in (0,1,5,26,101):
            direct = 1
            for h in range(65):
                if h:
                    direct = direct*(x+h) % d
                assert consecutive(x,x+h,d) == direct % d
                arithmetic += 1
    tests = 0
    for B in (3,4,5):
        ps = [v for v in range(B*B+1,B**3+9) if prime(v)]
        for d,factors in [(1,[]),(ps[0]**3,[ps[0]]),(ps[0]*ps[-1],[ps[0],ps[-1]]),
                          (ps[1]**2*ps[2],[ps[1],ps[2]])]:
            for x in range(B*B,B**3,3):
                for y in {x+1,min(B**3,x+B),B**3}:
                    target = prod(p for p in factors if x < p <= y)
                    assert descend(d,x,y)[0] == target
                    tests += 1
    B = 16
    p, q = 3001, 3023
    assert prime(p) and prime(q)
    d = p*q
    x,y = 2840,3160
    assert B**3//2 <= x and B*B < y-x <= B**2*isqrt(B)
    examples = []
    for a,b,expected in [(x,y,d),(x,p-1,1),(p-1,p,p),(p,q,q),(q,y,1)]:
        result, cert = lattice_window(d,a,b,dimension=10)
        assert result == expected == descend(d,a,b)[0]
        examples.append(dict(x=a,y=b,gcd=result,certificate=cert))
    assert integer_roots([1,-2,1],0,5)==[1]
    # Multiple hits outside the prime interval, with a repeated prime in d.
    false_d = 101**2 * 103
    false_result, trace = descend(false_d, 200, 206)
    assert false_result == 1 and sorted(p for _,p in trace)==[101,103]
    print(json.dumps(dict(composite_ring_products=arithmetic, direct_prime_window_cases=tests,
                          false_hits=dict(d=false_d,x=200,y=206,leaves=trace,answer=false_result),
                          lattice_examples=dict(B=B,d=d,rows=examples)),indent=2))


if __name__ == "__main__":
    main()
