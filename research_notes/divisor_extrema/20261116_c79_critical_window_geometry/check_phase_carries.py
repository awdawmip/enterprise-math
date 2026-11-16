"""Exact phase-limit polygon volumes and certified finite original bin counts."""
from collections import Counter
from fractions import Fraction as Q
import json
from math import comb, factorial
from critical_bins import block, full_width, bin_number, prepare, terminal


def clip(poly, a, b, c):
    """Keep a*x+b*y <= c in a circularly ordered convex polygon."""
    out = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        f, g = a*p[0]+b*p[1]-c, a*q[0]+b*q[1]-c
        if f <= 0:
            out.append(p)
        if (f < 0 < g) or (g < 0 < f):
            lam = f / (f-g)
            out.append((p[0] + lam*(q[0]-p[0]), p[1] + lam*(q[1]-p[1])))
    return out


def area(poly):
    return abs(sum((p[0]*q[1] - p[1]*q[0] for p, q in
                    zip(poly, poly[1:]+poly[:1])), Q(0))) / 2


def law(j, offset):
    unit = [(Q(0),Q(0)),(Q(1),Q(0)),(Q(1),Q(1)),(Q(0),Q(1))]
    out = {}
    for k in range(-2*j,2*j+1):
        lo = clip(unit,j-1,-j,offset-k)
        block_poly = clip(lo,1-j,j,k+1-offset)
        vol = area(block_poly)
        if vol:
            out[str(k)] = str(vol)
    assert sum(map(Q,out.values()))==1
    return out


def physical(c):
    p = ((c**9).bit_length()-1)//4
    prepare(c+2)
    terminal.cache_clear()
    aligned, shifted = Counter(), Counter()
    mixed_aligned, mixed_shifted = Counter(), Counter()
    prev_increments = {}
    for v in range(2,c+1):
        increments = {}
        for w in range(2,v+1):
            middle = block(v,w,3,terminal(w))
            vals = [full_width(c+j,v,middle) for j in range(3)]
            k0,k1,k2 = [bin_number(q,p,(0,1)) for q in vals]
            k2_shift = bin_number(vals[-1],p,(1,2))
            aligned[k2-2*k1+k0] += 1
            shifted[k2_shift-2*k1+k0] += 1
            inc0 = k1-k0
            inc1 = bin_number(vals[1],p,(2,5))-bin_number(vals[0],p,(1,3))
            increments[w] = inc0,inc1
            if w in prev_increments:
                old0, old1 = prev_increments[w]
                mixed_aligned[inc0-old0] += 1
                mixed_shifted[inc1-old1] += 1
        prev_increments = increments
    assert sum(mixed_aligned.values())==sum(mixed_shifted.values())==comb(c-1,2)
    assert sum(aligned.values()) == sum(shifted.values()) == comb(c,2)
    return {"c":c,"p":p,"templates":comb(c,2),
            "aligned":dict(sorted(aligned.items())),"shifted":dict(sorted(shifted.items())),
            "mixed_aligned":dict(sorted(mixed_aligned.items())),
            "mixed_shifted":dict(sorted(mixed_shifted.items()))}


def main():
    laws = {str(j):law(j,Q(0)) for j in range(2,7)}
    for j in range(2,7):
        assert laws[str(j)]["0"]==str(Q(1,j))
    shifted = law(2,Q(1,2))
    assert shifted == {"-1":"1/16","0":"7/16","1":"7/16","2":"1/16"}
    for i in range(8):
        assert sum((-1)**(i-j)*comb(i,j)*j**i for j in range(i+1)) == factorial(i)
    print(json.dumps({"aligned_limit":laws,"shifted_limit_j2":shifted,
                      "finite":[physical(c) for c in (32,64,128,256)]},indent=2))


if __name__=="__main__":
    main()
