"""Sharp support sizes for labelled equality observations after adversarial erasures."""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb, isqrt
import json


def optimum_holes(c):
    if c < 3:
        return 0
    t, d = divmod(c, 3)
    return 2*t-(d != 2)


def construction(e,c):
    A, H = 3*e+c, 2*e+c
    h = optimum_holes(c)
    t = c//3
    omit = {e+i if i<t else H-i for i in range(1,h+1)}
    return omit, (1<<(A+1))-1 - sum(1<<x for x in omit)


def adjacent_matching(mask,r):
    # Lower endpoints of all edges of length r. Repeatedly take the leftmost
    # edge of each run, discarding its neighbour to avoid overlapping pairs.
    edges = mask & (mask>>r)
    total = 0
    while edges:
        starts = edges & ~(edges<<r)
        total += starts.bit_count()
        edges &= ~(starts | (starts<<r))
    return total


def primes(n):
    return [p for p in range(2,n+1) if all(p%j for j in range(2,isqrt(p)+1))]


def comparison_cut(S,r,p):
    by_residue = defaultdict(Counter)
    for x in S:
        by_residue[x%r][(x//r)%p] += 1
    return sum(sum(c.values())-max(c.values()) for c in by_residue.values())


def direct_robust(S,e,H,A):
    ps = primes(A)
    for r in range(1,H+1):
        for p in ps:
            if p>2 and p*r>A:
                break
            if comparison_cut(S,r,p)<=e:
                return False
    return True


def small_full_enumeration(e,c):
    H, A = 2*e+c, 3*e+c
    central = list(range(e+1,H))
    full = set(range(A+1))
    layers=[1]
    previous = {()}
    for h in range(1,len(central)+1):
        survivors = set()
        for previous_holes in previous:
            for x in central:
                if previous_holes and x<=previous_holes[-1]:
                    continue
                new = previous_holes+(x,)
                if direct_robust(full-set(new),e,H,A):
                    survivors.add(new)
        if not survivors:
            break
        layers.append(len(survivors))
        previous = survivors
    assert len(layers)-1 == optimum_holes(c)
    return layers


def raw_all_layout_counts(e,c):
    # Construct each full-dataset refinement test. Use the fact that removing
    # h points can lower any one cut by at most h, regardless of geometry.
    A,H = 3*e+c,2*e+c
    tests = []
    for r in range(1,H+1):
        for p in primes(max(2,A//r)):
            blocks=[]
            for a in range(r):
                fine=[sum(1<<x for x in range(j,A+1,p*r))
                      for j in range(a,min(A+1,a+p*r),r)]
                blocks.append((sum(fine),fine))
            baseline=sum(group.bit_count()-max(m.bit_count() for m in parts)
                         for group,parts in blocks)
            tests.append((baseline,blocks))
    tests.sort(key=lambda pair:pair[0])
    counts=Counter()
    def visit(after, mask, n_holes):
        for base,blocks in tests:
            if base>e+n_holes:
                break
            cost=sum((group&mask).bit_count()-max((m&mask).bit_count() for m in parts)
                     for group,parts in blocks)
            if cost<=e:
                return
        counts[n_holes]+=1
        for x in range(after,H):
            visit(x+1,mask^(1<<x),n_holes+1)
    visit(e+1,(1<<(A+1))-1,0)
    return [counts[k] for k in range(max(counts)+1)]


def compressed_layouts(c):
    # The polynomial basis coefficient for z freely chosen deep holes.
    h = optimum_holes(c)
    objective = []
    for total in range(h+1):
        by_z = [0]*(total+1)
        for z in range(total+1):
            for selected in combinations(range(2*(c-1)),total-z):
                left = {i+1 for i in selected if i<c-1}
                right = {i-c+2 for i in selected if i>=c-1}
                if any(sum(i<=m for i in left)+sum(i<=m for i in right)>m
                       for m in range(1,total)):
                    continue
                for k in range(1,total+1):
                    a = max(0,min(k-1,c-2*k))
                    L, R = {i for i in left if i>a}, {i for i in right if i>a}
                    pairs = sum(c-k-i in R for i in L)
                    if z+len(L)+len(R)-pairs>max(k-1,c-2*k):
                        break
                else:
                    by_z[z] += 1
        objective.append(by_z)
    return objective


def trace_layer(coeff,deep):
    return sum(a*comb(deep,j) for j,a in enumerate(coeff) if j<=deep)


def exhaustive_deletions(S,e,H,A):
    for discard in combinations(sorted(S),e):
        remaining = sorted(S-set(discard))
        seen = {}
        for r in range(1,A+2):
            pattern = tuple((y-x)%r==0 for x,y in combinations(remaining,2))
            label = min(r,H+1)
            if pattern in seen and seen[pattern]!=label:
                return False
            seen[pattern]=label
    return True


def main():
    instances=ranks=0
    examples=[]
    for e in range(1,66):
        for c in range(e):
            omitted, mask=construction(e,c)
            H=2*e+c
            matches=[adjacent_matching(mask,r) for r in range(1,H+1)]
            assert min(matches)==e+1 and len(omitted)==optimum_holes(c)
            instances+=1
            ranks+=H
            if (e,c) in {(4,3),(6,5),(8,7),(9,8),(20,19),(60,30)}:
                examples.append({'e':e,'H':H,'A':3*e+c,'holes':sorted(omitted),
                                 'points':mask.bit_count(),'worst_adjacent_matching':min(matches)})
    native_direct = {}
    for e in range(3,9):
        for c in range(1,e):
            native_direct[f'{e},{c}']=small_full_enumeration(e,c)
    verified_counts = {
        3:[1,11],4:[1,15],5:[1,19,34],6:[1,23,252,38],
        7:[1,27,350,621],8:[1,31,464,1539,450],
    }
    polynomials={}
    for c in range(3,12):
        layers=compressed_layouts(c)
        counts=[trace_layer(a,2*c+1) for a in layers]
        if c in verified_counts:
            assert counts==verified_counts[c]==raw_all_layout_counts(3*c,c)
        polynomials[c]={'e_3c_all_counts':counts,'optimal_binomial_coefficients':layers[-1]}
    e,c=4,3
    holes,mask=construction(e,c)
    assert exhaustive_deletions(set(range(3*e+c+1))-holes,e,2*e+c,3*e+c)
    original=set(range(12))-{4,5,6,7}
    def pattern(S,r):
        return tuple((x-y)%r==0 for x,y in combinations(sorted(S),2))
    assert pattern(original,4)==pattern(original,8)
    assert pattern({0,3,6},1)==pattern({0,3,6},3)!=pattern({0,3,6},2)
    return {
        'source':'RTASK-POWER-HIGH-ERASURE-SPARSE-20260927',
        'one_sided_regime':'H=2e+c, 0<=c<e',
        'matching_parameter_pairs':instances,'matching_ranks':ranks,
        'examples':examples,
        'all_robust_supports_by_hole_count_independent_prime_refinement':native_direct,
        'binomial_basis_in_e_minus_c_plus_1':polynomials,
        'unrestricted_gcd_crosscheck_at_3c':'c=3 through 8, independent direct reference counts',
        'individual_known_deletion_sets_e4_c3':comb(15,4),
        'original_counterexamples_checked':2,
    }


if __name__ == '__main__':
    print(json.dumps(main(),ensure_ascii=False,indent=2))
