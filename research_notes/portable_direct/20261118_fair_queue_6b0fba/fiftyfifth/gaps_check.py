"""Exact finite checks for the r-free multiwindow sieve. Standard Python only."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, gcd, prod
import json


def primes_to(limit):
    keep = [True] * (limit + 1)
    for divisor in range(2, limit + 1):
        if keep[divisor]:
            yield divisor
            for multiple in range(divisor * divisor, limit + 1, divisor):
                keep[multiple] = False


def surviving_masks(length, prime, power, step=1):
    modulus = prime ** power
    whole = (1 << length) - 1
    excluded = {}
    for j in range(1, length + 1):
        residue = -step*j % modulus
        excluded[residue] = excluded.get(residue, 0) | (1 << (j-1))
    counts = Counter(whole ^ mask for mask in excluded.values())
    if modulus > len(excluded):
        counts[whole] += modulus - len(excluded)
    return counts


def sieve_mass(primes, power, length, step=1):
    distribution = {(1 << length)-1: 1}
    for prime in primes:
        patterns = surviving_masks(length, prime, power, step)
        following = Counter()
        for current, count in distribution.items():
            for mask, weight in patterns.items():
                following[current & mask] += count * weight
        distribution = following
    return distribution


def direct_period(primes, power, length, step):
    powers = [p**power for p in primes]
    period = prod(powers)
    frequencies = Counter()
    for anchor in range(period):
        mask = 0
        for j in range(1, length+1):
            if all((anchor+step*j) % modulus for modulus in powers):
                mask |= 1 << (j-1)
        frequencies[mask] += 1
    return frequencies


def cost(first, middle, last, cap_left, cap_right):
    left = max(0, first + middle - cap_left)
    right = max(0, middle + last - cap_right)
    return max(left, right, left + right - middle)


def exhaustive_cost():
    cases = 0
    for counts in product(range(4), repeat=3):
        options = list(product(*(range(v+1) for v in counts)))
        for cap_left, cap_right in product(range(7), repeat=2):
            actual = min(sum(counts)-sum(y) for y in options
                         if y[0]+y[1] <= cap_left and y[1]+y[2] <= cap_right)
            assert actual == cost(*counts, cap_left, cap_right)
            cases += 1
    return cases


def decimal_bound(value, upward, places=12):
    scale = 10**places
    numerator = value.numerator * scale
    denominator = value.denominator
    integer = (numerator + (denominator-1 if upward else 0)) // denominator
    return f'{integer//scale}.{integer%scale:0{places}d}'


def density_bounds(power, m, cap, cutoff):
    """Three cells of m sites. The two windows overlap in the middle cell."""
    counts = sieve_mass(list(primes_to(cutoff)), power, 3*m)
    assert cutoff**power > 3*m
    denominator = sum(counts.values())
    good = 0
    tail_weights = Counter()
    cell_mask = (1 << m)-1
    for mask, count in counts.items():
        cells = [((mask >> (j*m)) & cell_mask).bit_count() for j in range(3)]
        t = cost(*cells, cap, cap)
        if t == 0:
            good += count
        else:
            tail_weights[t] += count*comb(sum(cells), t)
    small_factor = Fraction(1, (power-1)*cutoff**(power-1))
    low = Fraction(good, denominator)
    high = min(1, low + sum(Fraction(n, denominator)*small_factor**t
                            for t, n in tail_weights.items()))
    return {'r':power,'cell_length':m,'cap_each':cap,'prime_cutoff':cutoff,
            'lower':decimal_bound(low, False),'upper':decimal_bound(high, True)}


def progression_classes(power, prime, step):
    modulus = prime**power
    common = gcd(step,modulus)
    period = modulus//common
    hist = Counter()
    for a in range(modulus):
        roots = [j for j in range(period) if (a+step*j) % modulus == 0]
        assert len(roots) == (1 if a % common == 0 else 0)
        hist['whole' if period==1 and roots else 'one_residue' if roots else 'none'] += 1
    return dict(sorted(hist.items()))


def check_observer():
    cases=0
    for r in (2,3,4):
        field = list(range(501))
        for b in range(1,501):
            if field[b] != b:
                continue
            t=2
            while b*t**r <= 500:
                field[b*t**r] = b
                t += 1
        for length in range(1,420):
            base = len(set(field[1:length+1]))
            for shift in range(1,min(24, length//(2**r-1))+1):
                shifted = len(set(field[shift+1:shift+length+1]))
                assert shifted-base == sum(field[n]==n for n in range(length+1,length+shift+1))
                cases += 1
    return cases


def main():
    exact = []
    for r, primes, step in [(2,(2,3,5,7),1),(2,(2,3,5,7),2),
                            (2,(2,3,5,7),4),(3,(2,3,5),1)]:
        dist = sieve_mass(primes,r,6,step)
        assert dist == direct_period(primes,r,6,step)
        exact.append({'r':r, 'primes':primes,'step':step,'width':6,
                      'period':sum(dist.values()),'distinct_masks':len(dist),
                      'entirely_covered_residues':dist.get(0,0)})
    result={'finite_sieves_by_two_routes':exact,
            'overlap_cost_cases':exhaustive_cost(),
            'near_window_label_differences':check_observer(),
            'natural_density_outward_bounds':[
                density_bounds(r,2,cap,997) for r in (2,3) for cap in (0,1,2)],
            'p_divides_step':[
                 {'r':2,'p':2,'step':d,'anchor_counts':progression_classes(2,2,d)}
                 for d in (1,2,4)]}
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__=='__main__':
    main()
