"""Combinatorial certification of exact suffix languages, independent of gate arithmetic."""
from collections import defaultdict
from math import gcd
import json


def classes(order, depth, cut):
    """Build exact extension languages from binary-word concatenation."""
    high, low = 1 << cut, 1 << (depth - cut)
    by_target = [defaultdict(set) for _ in range(order)]
    for j in range(high):
        for ell in range(low):
            d = (j * low + ell) % order
            by_target[d][j].add(ell)
    return by_target


def check():
    cuts = fibers = 0
    all_depth_tests = 0
    for depth in range(0, 11):
        for order in range(1, 33):
            peak = [0] * order
            for i in range(depth + 1):
                high, low = 1 << i, 1 << (depth - i)
                g = gcd(low,order)
                width = min(high,order // g,low // g)
                for d, target in enumerate(classes(order,depth,i)):
                    count = ((1 << depth) + order - 1 - d) // order
                    langs = {frozenset(s) for s in target.values()}
                    assert len(langs) == min(width,count)
                    peak[d] = max(peak[d],len(langs))
                    all_depth_tests += 1
                    if 1 << depth >= order**2:
                        assert len(langs) == width
                    assert sum(map(len,langs)) == len(set().union(*langs))
                    fibers += int((1 << depth) >= order**2)
                cuts += int((1 << depth) >= order**2)
            v = (order & -order).bit_length() - 1
            for d, value in enumerate(peak):
                count = ((1 << depth) + order - 1 - d) // order
                assert value == min(count,order >> v,1 << (max(depth-v,0)//2))
    samples = []
    for n in [12,15,24,40,48,64,72,96]:
        t = 2 * n
        widths = [min(1 << i, n // gcd(1 << (t-i),n),
                      (1 << (t-i)) // gcd(1 << (t-i),n)) for i in range(t+1)]
        odd = n // (n & -n)
        assert max(widths) == odd
        samples.append(dict(mersenne_bit_length=n, max_width=odd, layers_at_max=widths.count(odd)))
    lower_examples = []
    for k in range(1, 8):
        r = 3**k
        i = r.bit_length() - 1
        lower_examples.append(dict(N=3*r, depth=i, distinct_prefixes=1 << i,
                              probability_mass_of_all_histories="1"))
    return dict(all_depth_tests=all_depth_tests,saturated_cuts=cuts, single_target_fibers=fibers, mersenne_examples=samples,
                lower_bound_parameters=lower_examples)


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
