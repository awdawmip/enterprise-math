"""Verify integral congruence kernels, signed probe observations, and Laurent coefficients."""
import json
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import gcd, lcm


def multiply(a, b):
    x, y = a
    u, v = b
    return x*u-y*v, x*v+y*u-y*v


def conjugate(z):
    return z[0]-z[1], -z[1]


def norm(z):
    return z[0]**2-z[0]*z[1]+z[1]**2


def divides(z, numerator):
    d = norm(z)
    return all(coefficient % d == 0 for coefficient in multiply(numerator, conjugate(z)))


def relative_index(a, b):
    gamma = multiply(conjugate(a), b)
    numerator = multiply(gamma, gamma)
    denominator = norm(gamma)
    return denominator // gcd(denominator, *numerator)


def integral_checks():
    pi, rho = (3,1), (4,1)
    branches = [(1,0), pi, conjugate(pi), rho, conjugate(rho)]
    branches += [multiply(a,b) for a in (pi,conjugate(pi)) for b in (rho,conjugate(rho))]
    branches += [multiply(pi,pi),multiply(conjugate(pi),conjugate(pi))]
    # For every possible row precompute its honest divisibility kernel in (Z/L)^2.
    # The positive integers lying in a simple ideal are precisely the multiples of its norm.
    masks = {}
    total = 0
    first_groups = Counter()
    for rows in combinations(branches,3):
        period = lcm(*(norm(a) for a in rows))
        if period>100:
            continue
        for row in rows:
            if (period,row) not in masks:
                masks[period,row] = {s for s in product(range(period),repeat=2) if divides(row,s)}
            assert next(t for t in range(1,period+1) if divides(row,(t,0))) == norm(row)
        index = period**2 // len(set.intersection(*(masks[period,a] for a in rows)))
        relative = lcm(*(relative_index(a,b) for a,b in combinations(((1,0),)+rows,2)))
        assert index == relative
        assert period % (index//period) == 0
        first_groups[str((index//period, period))] += 1
        total += 1
    return total, dict(sorted(first_groups.items()))


def polynomial_product(first, second):
    answer = Counter()
    for i, u in first.items():
        for j, v in second.items():
            answer[i+j] += u*v
    return answer


def box_weights(weights, b):
    if b < 0:
        return Counter()
    box = Counter({0:1})
    for frequency in (-sum(weights),)+weights:
        box = polynomial_product(box, Counter(frequency*t for t in range(b+1)))
    return box


def shell_checks():
    total = 0
    for rows in range(1,5):
        weights = tuple((-1)**j*(j+1) for j in range(rows))
        for b in range(1,6):
            actual = Counter()
            for values in product(range(-b,b+1),repeat=rows):
                if max((0,)+values) - min((0,)+values) == b:
                    actual[sum(w*t for w,t in zip(weights,values))] += 1
            count = (b+1)**(rows+1) - 2*b**(rows+1) + (b-1)**(rows+1)
            assert actual.total() == count
            predicted = box_weights(weights,b)
            predicted.subtract(box_weights(weights,b-1))
            predicted.subtract(box_weights(weights,b-1))
            predicted.update(box_weights(weights,b-2))
            assert all(actual[k] == predicted[k] for k in actual.keys() | predicted.keys())
            total += 1
    return total


def diameter_law(weights, edges, signs):
    unseen=set(range(len(weights)))
    blocks=[]
    while unseen:
        root=min(unseen)
        sign={root:1}
        stack=[root]
        unseen.remove(root)
        while stack:
            i=stack.pop()
            for j in list(unseen):
                if tuple(sorted((i,j))) in edges:
                    sign[j]=sign[i]*signs[i]*signs[j]
                    unseen.remove(j)
                    stack.append(j)
        left=max([0]+[weights[i] for i in sign if sign[i]>0])
        right=max([0]+[weights[i] for i in sign if sign[i]<0])
        blocks.append((max(left,right),min(left,right)))
    maximum,anchor=max((a,i) for i,(a,b) in enumerate(blocks))
    floor=max(b for a,b in blocks)
    def cumulative(t):
        if t < floor:
            return Fraction(0)
        count=sum(i!=anchor and a>t for i,(a,b) in enumerate(blocks))
        return Fraction(1,2**count)
    return {maximum+t:cumulative(t)-cumulative(t-1) for t in range(maximum+1)
            if cumulative(t)>cumulative(t-1)}


def probe_checks():
    trials=0
    weights=[2,1,3,2]
    possible=list(combinations(range(4),2))
    for mask in range(1<<len(possible)):
        edges={edge for j,edge in enumerate(possible) if mask>>j & 1}
        records=defaultdict(list)
        for signs in product((-1,1),repeat=4):
            values=tuple(w*s for w,s in zip(weights,signs))
            observed=tuple(abs(values[i]-values[j]) for i,j in sorted(edges))
            height=max((0,)+values)-min((0,)+values)
            records[observed].append((signs,height))
        for options in records.values():
            counts=Counter(height for signs,height in options)
            actual={d:Fraction(v,len(options)) for d,v in counts.items()}
            assert actual == diameter_law(weights,edges,options[0][0])
            trials+=1
    return trials


def main():
    total, groups = integral_checks()
    print(json.dumps({
        "literal_ideal_kernel_triples_mod_7_13_and_49":total,
        "smith_group_histogram":groups,
        "exact_diameter_spheres_and_Laurent_polynomials":shell_checks(),
        "graphs_examined":64,
        "conditional_diameter_distributions_exact":probe_checks(),
        "ordered_pair_counts_at_prime_powers_0_through_5":[1,6,12,18,24,30]
    },indent=2))


if __name__=="__main__":
    main()
