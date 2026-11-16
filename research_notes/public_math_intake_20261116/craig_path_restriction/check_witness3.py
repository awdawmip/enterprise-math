"""Forcing at level two and exact witnesses for finite-depth ambiguity.

Uses the pinned N_BRC branch count through check_weighted.load_signed_brc.
All computed probabilities and grid sums are integers or rational numbers.
"""
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from math import comb, factorial

from check_weighted import load_signed_brc

brc = load_signed_brc()


@lru_cache(None)
def words(n):
    paths = []
    for x_positions in combinations(range(2*n), n):
        x_positions = set(x_positions)
        paths.append(''.join('X' if i in x_positions else 'Y' for i in range(2*n)))
    assert len(paths) == brc.shortest_path_multiplicity((n,n,0,0,0,0))
    return tuple(paths)


@lru_cache(None)
def source_counts(word, k):
    xy = [[i for i,s in enumerate(word) if s == color] for color in 'XY']
    counts = Counter()
    for xs in combinations(xy[0], k):
        for ys in combinations(xy[1], k):
            retained = tuple(sorted(xs+ys))
            counts[''.join(word[i] for i in retained)] += 1
    return counts


def forcing_checks():
    checks = 0
    for n in range(2,7):
        local_gaps = []
        edge_masses = []
        for w in words(n):
            xs = ys = max_gap = area_sum = exact_sum = 0
            for s in w:
                old = xs-ys
                if s == 'X':
                    xs += 1
                else:
                    ys += 1
                    area_sum += xs
                new = xs-ys
                max_gap = max(max_gap, abs(new))
                exact_sum += old*old + old*new + new*new
            integral = Q(exact_sum,3*n**3)
            bins = source_counts(w, 2)
            d = Q(bins['XXYY']+bins['YYXX'], comb(n, 2)**2)
            assert integral == d-Q(1,3)+(1-d)/n
            assert Q(max_gap**3,n**3) <= Q(3,2)*integral
            assert abs(Q(area_sum,n*n) - Q(1,2)) <= Q(max_gap,n)
            local_gaps.append(integral)
            edge_masses.append(d)
            checks += 1
        assert sum(edge_masses)/len(edge_masses) == Q(1,3)
        assert sum(local_gaps)/len(local_gaps) == Q(2,3*n)
    return checks


def grid_prior(r, parity):
    return [(Q(j,r), Q(comb(r,j),2**(r-1))) for j in range(parity,r+1,2)]


def block_law(n, r, parity):
    result = {}
    for a in range(n+1):
        w = 'X'*a+'Y'*n+'X'*(n-a)
        result[w] = sum(mass * comb(n,a)*theta**a*(1-theta)**(n-a)
                        for theta,mass in grid_prior(r,parity))
    assert sum(result.values()) == 1
    return result


def filled_law(n, r, parity, uniform_share):
    sparse = block_law(n,r,parity)
    return {w: (1-uniform_share)*sparse.get(w,0) + uniform_share/len(words(n))
            for w in words(n)}


def verify_moment_pairs():
    projection_checks = compared_levels = 0
    for k in range(1,8):
        r = k+1
        for m in range(k+1):
            diff = sum((-1)**j*comb(r,j)*Q(j,r)**m for j in range(r+1))
            assert diff == 0
        delta = sum((-1)**j*comb(r,j)*Q(j,r)**r for j in range(r+1))
        assert delta == (-1)**r * Q(factorial(r), r**r)
        for n in range(1,k+1):
            assert block_law(n,r,0) == block_law(n,r,1)
            compared_levels += 1
        pos = block_law(r,r,0)
        neg = block_law(r,r,1)
        tv = sum(abs(mass-neg[w]) for w,mass in pos.items())/2
        assert tv == Q(factorial(r),r**r)
        # Polynomial identity for the exact character gap: the coefficient
        # comparison certifies (1-z)^r for the actual odd/even node supports.
        coefficients = [0]*(r+1)
        for parity in (0,1):
            for theta,mass in grid_prior(r,parity):
                coefficients[int(theta*r)] = (-1)**parity * mass
        poly = [Q(1)]
        for _ in range(r):
            poly = [u-v for u,v in zip(poly+[0],[0]+poly)]
        assert [c/2**(r-1) for c in poly] == coefficients
        for parity in (0,1):
            for n in range(2,5):
                law = filled_law(n,r,parity,Q(1,2))
                assert min(law.values()) > 0
                for m in range(1,n):
                    proj = Counter()
                    for w,mass in law.items():
                        for u,count in source_counts(w,m).items():
                            proj[u] += mass*Q(count,comb(n,m)**2)
                    assert dict(proj) == filled_law(m,r,parity,Q(1,2))
                    projection_checks += 1
    for side in (0,1):
        law = filled_law(2,3,side,Q(1,2))
        assert [law[w] for w in words(2)] == list(map(Q,['1/4','1/12','1/4','1/12','1/12','1/4']))
    return compared_levels, projection_checks


def edge_law(n, h):
    """Random early-X and late-Y counts; the middle names have uniform relative order."""
    masses = Counter()
    for early in range(n+1):
        for late in range(n+1):
            middle_x = n-early
            middle_y = n-late
            length = middle_x+middle_y
            prior = comb(n,early)*comb(n,late)*h**(early+late)*(1-h)**length
            if prior == 0:
                continue
            conditional = prior/comb(length,middle_x)
            for positions in combinations(range(length),middle_x):
                chosen = set(positions)
                middle = ''.join('X' if j in chosen else 'Y' for j in range(length))
                masses['X'*early + middle+'Y'*late] += conditional
    assert sum(masses.values()) == 1
    return masses


def frontier_checks():
    comparisons = 0
    for h in map(Q,['0','1/4','1/2','3/4','1']):
        low = edge_law(2,h)
        p = Q(1,2) + h - h*h/2
        d = Q(1,3)+2*h*h-4*h**3/3
        assert low['XXYY']+low['YYXX'] == d
        assert edge_law(1,h)['XY'] == p
        for n in range(1,6):
            fine = edge_law(n,h)
            assert set(fine) <= set(words(n))
            for k in range(1,n+1):
                out = Counter()
                for w,mass in fine.items():
                    for u, count in source_counts(w,k).items():
                        out[u] += mass*Q(count,comb(n,k)**2)
                assert out == edge_law(k,h)
                comparisons += 1
    return comparisons


if __name__ == '__main__':
    print('level-two forcing, discrete energy and order-area inequalities:', forcing_checks())
    print('matched full levels and projected full-support laws:', verify_moment_pairs())
    print('sharp boundary towers, exact projected laws:', frontier_checks())
