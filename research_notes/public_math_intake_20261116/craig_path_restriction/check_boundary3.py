"""Exact finite checks for the conditional BRC comparison-moment boundary."""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, permutations
from math import comb, factorial, prod

from check_weighted import area, law_weight, load_signed_brc, words


def weights(m, mode):
    universe = tuple(words(m))
    assert len(universe) == load_signed_brc().shortest_path_multiplicity((m,m,0,0,0,0))
    if mode == 'early':
        # A half-and-half mixture of two explicit rational latent parameters.
        mass = Counter()
        for p in (F(1,5), F(2,3)):
            for a in range(m + 1):
                u = 'X'*a + 'Y'*m + 'X'*(m-a)
                mass[u] += comb(m,a)*p**a*(1-p)**(m-a)/2
        return mass
    a,b = (1,1) if mode == 'uniform' else (2,1)
    return {w: law_weight(w,a,b) for w in universe}


def falling(n,k):
    return prod(range(n-k+1,n+1))


@lru_cache(maxsize=None)
def matching_counts(word):
    """Count disjoint successful XY comparisons by adding each Y column."""
    m = word.count('Y')
    counts = [1]+[0]*m
    seen_x = 0
    for ch in word:
        if ch == 'X':
            seen_x += 1
        else:
            for j in range(min(m,seen_x),0,-1):
                counts[j] += (seen_x-j+1)*counts[j-1]
    return tuple(counts)


def brute_matchings(word, r):
    """Explicit source choices and bijections, for independent small-level checks."""
    xs = [k for k,a in enumerate(word) if a=='X']
    ys = [k for k,a in enumerate(word) if a=='Y']
    return sum(all(i<j for i,j in zip(x,y))
               for x in combinations(xs,r) for subset in combinations(ys,r)
               for y in permutations(subset))


def ruler_moments(law,k):
    return tuple(sum(weight*matching_counts(w)[r] for w,weight in law.items())
                 / (comb(k,r)**2*factorial(r)) for r in range(k+1))


@lru_cache(maxsize=None)
def partitions(r):
    """Restricted-growth strings encode partitions of the labelled pair indices."""
    if r == 1:
        return ((0,),)
    return tuple(p+(j,) for p in partitions(r-1) for j in range(max(p)+2))


@lru_cache(maxsize=None)
def match_event(word, px, py):
    bx,by = max(px)+1,max(py)+1
    xs,ys = ([j for j,s in enumerate(word) if s==c] for c in 'XY')
    n=len(xs)
    success = sum(all(X[i]<Y[j] for i,j in zip(px,py))
                  for X in permutations(xs,bx) for Y in permutations(ys,by))
    return F(success,falling(n,bx)*falling(n,by))


def verify():
    cases = 0
    for m in range(1,6):
        for w in words(m):
            counts = matching_counts(w)
            assert counts[1] == area(w)
            for r,count in enumerate(counts):
                assert brute_matchings(w,r) == count
                cases += 1
    polychecks=0
    for mode in ('uniform','biased','early'):
        laws = {m:weights(m,mode) for m in range(1,7)}
        moments = ruler_moments(laws[6],6)
        for m in range(1,7):
            assert ruler_moments(laws[m],m) == moments[:m+1]
        for r,h in enumerate(moments):
            expected = F(1,2)**r if mode == 'uniform' else (F(2,3)**r if mode=='biased'
                       else (F(1,5)**r+F(2,3)**r)/2)
            assert h == expected
        for r in range(1,4):
            modes = []
            for px in partitions(r):
                for py in partitions(r):
                    bx,by = max(px)+1,max(py)+1
                    m = max(bx,by)
                    success = sum(p*match_event(w,px,py) for w,p in laws[m].items())
                    modes.append((bx,by,success))
            for n in range(r,7):
                computed = sum(falling(n,bx)*falling(n,by)*s for bx,by,s in modes)/n**(2*r)
                direct = sum(p*F(area(w),n*n)**r for w,p in laws[n].items())
                assert computed == direct
                assert abs(direct - moments[r]) <= 1-F(falling(n,r),n**r)**2
                polychecks += 1
    print('Matching recurrence vs independent source selection and permutation:',cases)
    print('Fixed-level collision polynomials vs fine distribution moments:',polychecks)
    print('Boundary moments recovered exactly: 3 laws, all 6 levels; all tests passed.')


if __name__ == '__main__':
    verify()
