"""Exact arithmetic for generalized Franel digit corrections. Python 3 standard library."""
import itertools
import json
import math
from collections import Counter
from functools import lru_cache


def valuation(n, p):
    a = 0
    while n % p == 0:
        n //= p
        a += 1
    return a


def binomial_power_table(limit, exponent, modulus):
    """Sum powers of the rows of Pascal's triangle, including zero carries."""
    row = [1]
    result = []
    for n in range(limit + 1):
        result.append(sum(pow(c, exponent, modulus) for c in row) % modulus)
        row = [1] + [(a + b) % modulus for a, b in zip(row, row[1:])] + [1]
    return result


def digit_model(p, exponent, s):
    modulus = p**s
    memory = p**(s - 1)
    values = binomial_power_table(modulus - 1, exponent, modulus)
    good = [b for b in range(p) if values[b] % p]
    @lru_cache(None)
    def update(h, b):
        numerator = values[p*h+b]
        denominator = values[h] * values[b] % modulus
        return (p*h+b) % memory, numerator*pow(denominator,-1,modulus) % modulus
    def evaluate(word):
        h, correction = 0, 1
        for b in word:
            h, multiplier = update(h, b)
            correction = correction*multiplier % modulus
        return h, correction
    return values, good, update, evaluate


def base_digits(n, p):
    digits = []
    while n:
        n, b = divmod(n, p)
        digits.append(b)
    return digits[::-1]


def fixed_histogram(p, exponent, s, length, ones, update):
    mod = p**s
    counts = Counter({(0, 0, 1): 1})
    for i in range(length):
        nxt = Counter()
        for (used, h, correction), paths in counts.items():
            for b in (0, 1):
                if not 0 <= ones-used-b <= length-i-1:
                    continue
                nh, factor = update(h, b)
                nxt[used+b, nh, correction*factor % mod] += paths
        counts = nxt
    hist = Counter()
    for (used, _, correction), paths in counts.items():
        assert used == ones
        hist[correction] += paths
    total = math.comb(length, ones)
    subgroup_size = p**max(0, s-1-valuation(exponent, p))
    assert sum(hist.values()) == total
    return dict(length=length, ones=ones, count=total, support=len(hist),
                group_size=subgroup_size, equal_to_digit_product=hist[1],
                least_count= min(hist.values()) if len(hist)==subgroup_size else 0,
                largest_count=max(hist.values()))


def test_branch(p, exponent, s):
    mod = p**s
    values, good, transition, evaluate = digit_model(p, exponent, s)
    a = valuation(exponent, p)
    u = 1 + a
    result = dict(p=p, exponent=exponent, precision=s, good=good)
    digits_tested = 0
    # Original exact integers, independent of the memory law.
    for n in range(401):
        word = base_digits(n, p)
        if not set(word).issubset(good):
            continue
        direct = sum(math.comb(n,k)**exponent for k in range(n+1)) % mod
        d = math.prod(values[b] for b in word)
        residue = evaluate(word)[1]
        assert residue*d % mod == direct
        assert (residue-1) % p**min(u,s)==0
        digits_tested += 1
    ac, bc = ([1,1,0]+[0]*(s-1), [1,0,1]+[0]*(s-1))
    left, right = evaluate(ac), evaluate(bc)
    assert left[0] == right[0] == 0
    switch = left[1]*pow(right[1],-1,mod) % mod
    order = p**max(s-u,0)
    assert pow(switch,order,mod)==1
    if order>1:
        assert pow(switch,order//p,mod)!=1
        assert (switch-1-p*exponent*pow(2,-1,mod)) % p**(u+1)==0
    result.update(direct_integer_good_inputs=digits_tested, switch=switch,
                  switch_order=order)
    if (p,exponent,s) in ((3,3,4),(5,3,3),(7,3,3),(3,9,4)):
        result["fixed_counts"] = [fixed_histogram(p,exponent,s,m,m//2,transition)
                                  for m in (12,32,60)]
    return result


def main():
    examples = [(3,3,s) for s in range(2,6)] + [(5,3,s) for s in range(2,5)]
    examples += [(7,3,3), (3,2,3), (3,9,4), (5,5,3), (7,14,3)]
    tests = [test_branch(*params) for params in examples]
    z = {n: sum(math.comb(n,k)**3 for k in range(n+1)) % 27 for n in (108,90)}
    assert z == {108:22,90:4}
    print(json.dumps(dict(branches=tests, cubic_mod27=z),indent=2))


if __name__ == "__main__":
    main()
