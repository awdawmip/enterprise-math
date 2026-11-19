"""Finite checks on the P11 marked curve and exact distributions in its five-division tower."""
import json
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd, isqrt


P, Q = 233, 119
H = (194089, 69872040)
A, B = -(P**2 + Q**2), (P * Q)**2
DISCRIMINANT = 16 * P**4 * Q**4 * (P**2 - Q**2)**2
C4 = 16 * (A**2 - 3 * B)
PRIME = 5


def valuation(n, p):
    assert n > 0
    exponent = 0
    while n % p == 0:
        exponent += 1
        n //= p
    return exponent


def add(left, right, p):
    if left is None:
        return right
    if right is None:
        return left
    x, y = left
    u, v = right
    if x == u:
        if (y + v) % p == 0:
            return None
        slope = (3*x*x + 2*A*x + B) * pow(2*y, -1, p)
    else:
        slope = (v-y) * pow(u-x, -1, p)
    z = (slope*slope - A - x - u) % p
    return z, (slope*(x-z) - y) % p


def multiply(n, point, p):
    result = None
    while n:
        if n % 2:
            result = add(result, point, p)
        point = add(point, point, p)
        n //= 2
    return result


def look_at_prime(p):
    assert all(p % j for j in range(2, isqrt(p)+1))
    assert DISCRIMINANT % p and p != PRIME
    roots = {}
    for y in range(p):
        roots.setdefault(y*y % p, []).append(y)
    points = [None]
    for x in range(p):
        points.extend((x,y) for y in roots.get(x*(x-P*P)*(x-Q*Q) % p, []))
    order = len(points)
    h = tuple(c % p for c in H)
    assert h in points and multiply(order, h, p) is None
    multiples = [multiply(5, v, p) for v in points]
    torsion = multiples.count(None)
    preimages = multiples.count(h)
    j = 0
    reduced = multiply(order // (5**valuation(order,5)), h, p)
    while reduced is not None:
        reduced = multiply(5, reduced, p)
        j += 1
    result = dict(p=p, group_order=order, trace=p+1-order, H=h,
                  five_torsion=torsion, rational_five_preimages=preimages,
                  v5_order_H=j, trace_discriminant_mod5=((p+1-order)**2-4*p)%5)
    if order % 5 == 0:
        result["order_over_5_times_H"] = multiply(order//5,h,p)
    return result


def matrix_type(a, b, c, d, modulus):
    # Size of the kernel over Z/m by Smith form over Z, truncated at m.
    # gcd with m also handles the zero matrix.
    g = gcd(gcd(a,b), gcd(c,d))
    first = gcd(g, modulus)
    second = modulus if g == 0 else gcd((a*d-b*c)//g, modulus)
    return valuation(first,5), valuation(second,5)


def smith_prob(a,b):
    if (a,b)==(0,0):
        return Fraction(365,480)
    if a==0:
        return Fraction(19,20*5**b)
    if a==b:
        return Fraction(1,5**(4*a))
    return Fraction(6,5**(1+3*a+b))


def truncated_type_probs(level):
    # Sum the geometric tails in the infinite formula after capping both exponents.
    q = 5
    out = {}
    for a in range(level):
        for b in range(a,level):
            out[a,b] = smith_prob(a,b)
        out[a,level] = smith_prob(a,level)*Fraction(q,q-1)
    out[level,level] = Fraction(1,480*q**(4*(level-1)))
    assert sum(out.values()) == 1
    return out


def local_level(level):
    r = 5**level
    pairs = list(product(range(r),repeat=2))
    counts = Counter()
    affine_direct = Counter()
    for a,b,c,d in product(range(r),repeat=4):
        if ((1-a)*(1-d)-b*c) % 5 == 0:
            continue
        indices = matrix_type(a,b,c,d,r)
        counts[indices] += 1
        if level == 1:
            histogram = Counter(((a*x+b*y)%r,(c*x+d*y)%r) for x,y in pairs)
            affine_direct[0] += r*r-len(histogram)
            affine_direct.update(histogram.values())
    total = sum(counts.values())
    assert total==480*625**(level-1)
    assert {key:Fraction(val,total) for key,val in counts.items()}==truncated_type_probs(level)
    affine = Counter()
    for (a,b), num in counts.items():
        size = 5**(a+b)
        good = r*r//size
        affine[size] += num*good
        affine[0] += num*(r*r-good)
    if level==1:
        assert affine==affine_direct
    return dict(level=level, modulus=r, linear_matrices=total,
                affine_group_order=total*r*r,
                smith_counts={f"{a},{b}":num for (a,b),num in sorted(counts.items())},
                affine_fixed_points=dict(sorted(affine.items())),
                preimage_exists=str(1-Fraction(affine[0],total*r*r)))


def odd_saturation():
    """All possible integral preimages in H + 2E(Q), using integer bounds only."""
    from math import isqrt
    A, B, Hx = 233**2, 119**2, 194089
    assert 2*(A-B)**2 > A*A
    common_bound = 4*(A*B*(A-B))**4
    limit = Hx*(2*common_bound)**3
    low, high = 0, 1 << ((limit.bit_length()+8)//9)
    while low+1 < high:
        middle = (low+high)//2
        if middle**9 <= limit:
            low = middle
        else:
            high = middle
    assert low**9 <= limit < (low+1)**9
    kmax = isqrt(low//3961)
    mod, classes, sieve = 1, [0], []
    for p in (2, 3, 5, 7, 11, 13, 17, 19):
        squares = {i*i % p for i in range(p)}
        first = {1398*z % p for z in squares}
        second = {102*z % p for z in squares}
        allowed = {i for i in range(p) if (3961*i*i-A) % p in first
                   and (3961*i*i-B) % p in second}
        classes = [i for r in classes for i in range(r, mod*p, mod) if i % p in allowed]
        mod *= p
        sieve.append([p, mod, len(classes)])
    candidates, points = 0, []
    for r in classes:
        for k in range(r, kmax+1, mod):
            x = 3961*k*k
            if x < A:
                continue
            candidates += 1
            b, rem1 = divmod(x-A,1398)
            c, rem2 = divmod(x-B,102)
            if rem1 == rem2 == 0 and isqrt(b)**2 == b and isqrt(c)**2 == c:
                points.append([k, x, isqrt(b), isqrt(c)])
    assert points == [[7,Hx,10,42]]
    sharp_bound = 4*(A*B*(A-B))**2
    sharp_limit = Hx*(2*sharp_bound)**3
    # Independently certify the proposed integer ninth root by adjacent powers.
    sharp_x = 7610639897
    assert sharp_x**9 <= sharp_limit < (sharp_x+1)**9
    small_k = isqrt(sharp_x//3961)
    assert small_k == 1386
    direct = []
    for k in range(1,small_k+1):
        x = 3961*k*k
        if x <= A:
            continue
        b, r_b = divmod(x-A, 1398)
        c, r_c = divmod(x-B, 102)
        if r_b == r_c == 0 and isqrt(b)**2 == b and isqrt(c)**2 == c:
            direct.append([k, x, isqrt(b), isqrt(c)])
    assert direct == points
    return dict(second_gcd_bound=str(sharp_bound), second_x_max=sharp_x,
                second_k_max=small_k, all_direct_candidates=direct,
                duplication_gcd_bound=str(common_bound), numerator_upper_bound=low,
                k_bound=kmax, sieve=sieve,
                congruence_survivors=candidates, all_candidates=points)


def main():
    assert H[1]**2==H[0]*(H[0]-P*P)*(H[0]-Q*Q)
    curves = [look_at_prime(p) for p in (13,23,29,31,37,373,1831,2687,3499)]
    assert curves[0]["trace_discriminant_mod5"]==2
    assert curves[4]["order_over_5_times_H"]==(36,5) and curves[4]["rational_five_preimages"]==0
    assert [(row["five_torsion"],row["v5_order_H"]) for row in curves[5:]]==[(5,2),(25,1),(5,1),(5,0)]
    local = [local_level(i) for i in (1,2)]
    probability = (365+114*Fraction(1,6)+Fraction(1,31))/480
    assert probability==Fraction(2381,2976)
    joint = probability * Fraction(139,2912)
    assert joint==Fraction(330959,8666112)
    result = dict(odd_saturation=odd_saturation(), curve=dict(P=P,Q=Q,H=H), good_prime_certificates=curves,
                  multiplicative={p:dict(discriminant_valuation=valuation(DISCRIMINANT,p),
                                         c4_mod_p=C4%p) for p in (7,233)},
                  finite_full_affine_levels=local,
                  limiting_density_order_coprime_to_five=str(probability),
                  limiting_density_order_coprime_to_thirty=str(joint),
                  rank_two_given_group_order_v5_eq_2=str(smith_prob(1,1)/(smith_prob(0,2)+smith_prob(1,1))))
    assert DISCRIMINANT%5 and all(row["c4_mod_p"] and row["discriminant_valuation"]==4
                                  for row in result["multiplicative"].values())
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
