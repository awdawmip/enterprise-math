"""Exact finite reduction of the ordered positive-shear word model."""
from collections import Counter
from fractions import Fraction
from math import comb, gcd
import json


def group_data(m):
    d = gcd(m, 12)
    one = (1%m, 0, 0, 1%m)
    elements = [one]
    ids = {one: 0}
    chars = [0]
    neighbors = []
    for i, (a,b,c,e) in enumerate(elements):
        steps = []
        for mat, increment in [(((a+c)%m, (b+e)%m, c, e), 1),
                               ((a, b, (c+a)%m, (e+b)%m), -1)]:
            val = (chars[i]+increment)%d
            if mat not in ids:
                ids[mat] = len(elements)
                elements.append(mat)
                chars.append(val)
            j = ids[mat]
            assert chars[j] == val
            steps.append(j)
        neighbors.append(steps)
    # For each primitive first column there are m possible second columns.
    primitive = {(x,y) for x in range(m) for y in range(m) if gcd(x,y,m)==1}
    assert len(elements)==m*len(primitive)
    vector_fibers = Counter((chi, ((a+b)%m,(c+e)%m)) for (a,b,c,e),chi in zip(elements, chars))
    assert len(vector_fibers) == d*len(primitive)
    assert set(vector_fibers.values()) == {m//d}
    return chars, neighbors


def addpush(dest, hist, steps, j):
    for i, count in enumerate(hist):
        if count:
            dest[steps[i][j]] += count


def balanced_tests(m, nmax):
    labels, steps = group_data(m)
    size = len(labels)
    identity = [1] + [0]*(size-1)
    previous = [identity]
    first = None
    diagnostics = {}
    target_size = labels.count(0)
    for length in range(1, 2*nmax+1):
        lo = max(0,length-nmax)
        hi = min(length,nmax)
        prior_lo = max(0,length-1-nmax)
        layers = []
        for a in range(lo,hi+1):
            b = length-a
            hist = [0]*size
            if a:
                addpush(hist, previous[a-1-prior_lo], steps, 0)
            if b:
                addpush(hist, previous[a-prior_lo], steps, 1)
            layers.append(hist)
            if a==b:
                pop = sum(hist)
                assert pop == comb(2*a,a)
                assert all(v==0 or lab==0 for v,lab in zip(hist,labels))
                if first is None and sum(v>0 for v in hist)==target_size:
                    first = a
                if a in (4,8,12,nmax):
                    tv = Fraction(sum(abs(v*target_size-pop) for v,lab in zip(hist,labels) if lab==0),
                                  2*pop*target_size)
                    diagnostics[str(a)] = {'positive_matrices':sum(v>0 for v in hist),
                                           'total_variation_from_coset_uniform':str(tv)}
        previous = layers
    return {'modulus':m,'group_order':size,'abelianization_order':gcd(12,m),
            'stable_matrices_per_primitive_point':m//gcd(12,m),'first_positive_balanced_count_a_eq_b':first,
            'tested_to_a_eq_b':nmax,'balanced_examples':diagnostics}


def main():
    print(json.dumps({'exact_matrix_counts':[balanced_tests(m,24) for m in (2,3,4,5,6,7,8,9,10,11,12)]},indent=2))


if __name__=='__main__':
    main()
