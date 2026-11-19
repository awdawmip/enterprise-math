"""Complete rational chamber proof and finite source replays for the two hole intervals."""
import argparse
from collections import Counter
from functools import cache
from hashlib import sha256
from itertools import combinations
import json
from math import gcd
from pathlib import Path
import sys

PIN = '9a115cfd3f9333f6863bbca82fdda5ef7247ddebfbacc9140ac162698e5de1d3'


class Form(tuple):
    """Integer affine form on e,j,a,r, with constant last."""
    def __add__(self, other):
        return Form(x + y for x, y in zip(self, other))

    def __sub__(self, other):
        return Form(x - y for x, y in zip(self, other))

    def __mul__(self, scalar):
        return Form(x * scalar for x in self)


E, J, A, R, ONE = [Form(int(i == j) for i in range(5)) for j in range(5)]
ZERO = ONE * 0
CUTS = (A, A + J, A + E * 2 - J, A + E * 2, E * 3 + ONE)


@cache
def rationally_empty(rows):
    """Fourier-Motzkin feasibility for weak inequalities f>=0 over the rationals."""
    tight = {}
    for row in rows:
        divisor = gcd(*row[:-1])
        constant = row[-1]
        if divisor == 0:
            if constant < 0:
                return True
            continue
        normal = tuple(x // divisor for x in row[:-1])
        # Compare constants after division by the positive normalising divisor.
        if normal not in tight or constant * tight[normal][1] < tight[normal][0] * divisor:
            common = gcd(constant, divisor)
            tight[normal] = (constant // common, divisor // common)
    if not tight:
        return False
    rows = [tuple(den*x for x in normal) + (num,) for normal, (num, den) in tight.items()]
    dim = len(rows[0]) - 1

    def pair_count(i):
        return sum(row[i] > 0 for row in rows) * sum(row[i] < 0 for row in rows)

    i = min(range(dim), key=pair_count)
    positive = [row for row in rows if row[i] > 0]
    negative = [row for row in rows if row[i] < 0]
    shorter = [row[:i] + row[i+1:] for row in rows if row[i] == 0]
    for lower in positive:
        for upper in negative:
            shorter.append(tuple(lower[i]*upper[j] - upper[i]*lower[j]
                                 for j in range(dim+1) if j != i))
    return rationally_empty(tuple(sorted(set(shorter))))


def chambers(boundary=False):
    # The small-r range is proved by a direct interval matching bound in the text.
    domain = (J-ONE, E-J*6-ONE, A-J*2-ONE, E-J*4-A, E+ONE-A*2,
              R-E+J*4-ONE, E*2-J-R)
    cuts = CUTS
    if boundary:
        # Shorten the left interval by one, fixing a=2j+1 and e in {6j-1,6j}.
        domain = (J-ONE,E-J*6+ONE,J*6-E,A-J*2-ONE,J*2+ONE-A,
                  R-E+J*4-ONE*3,E*2-J-R)
        cuts = (A,A+J-ONE,A+E*2-J,A+E*2,E*3+ONE)
    states = [(domain, (), ())]
    stages = []
    for i, cut in enumerate(cuts):
        next_states = []
        for space, floors, order in states:
            for quotient in range(9):
                rem = cut - R*quotient
                new = space + (rem, R-rem-ONE)
                if rationally_empty(new):
                    continue
                earlier = [cuts[k]-R*floors[k] for k in order]
                for pos in range(i+1):
                    region = new
                    if pos:
                        region += (rem-earlier[pos-1],)
                    if pos < i:
                        region += (earlier[pos]-rem-ONE,)
                    if not rationally_empty(region):
                        sorted_ids = order[:pos] + (i,) + order[pos:]
                        next_states.append((region, floors+(quotient,), sorted_ids))
        states = next_states
        stages.append(len(states))

    formulas = Counter()
    for region, floors, order in states:
        boundaries = [ZERO]+[cuts[i]-R*floors[i] for i in order]+[R]
        total = ZERO
        for segment in range(6):
            passed = set(order[:segment])
            run = matching = 0
            for k in range(9):
                crosses = sum(k > f or (k == f and i in passed) for i,f in enumerate(floors))
                if crosses % 2 == 0:
                    run += 1
                else:
                    matching += run//2
                    run = 0
            matching += run//2
            total += (boundaries[segment+1] - boundaries[segment])*matching
        assert rationally_empty(region + (E-total,)), (floors, order, total)
        formulas[tuple(total)] += 1
    if not boundary:
        assert stages == [1, 2, 19, 31, 87] and len(formulas) == 30
    return {'chambers_by_inserted_cut':stages,'affine_matching_forms_e_j_a_r_constant':
            [list(form)+[count] for form, count in sorted(formulas.items())]}


def native(repo):
    source = repo/'src/enterprise_math/group_ring_span_erasures.py'
    assert sha256(source.read_bytes()).hexdigest() == PIN
    sys.path.insert(0,str(repo/'src'))
    from enterprise_math import group_ring_span_erasures as original
    assert Path(original.__file__).resolve() == source.resolve()
    return original


def expected(e, j, a):
    b = e+1-a
    return min(a,b) >= 2*j+1 and min(a,b) <= e-4*j


def support(e, j, a):
    H = 2*e-j
    return set(range(3*e+1)) - set(range(a, a+j)) - set(range(a+H, a+H+j))


def number_runs(e, j):
    if e <= 6*j:
        return 0
    return 2*(e-6*j) if e < 8*j else e-4*j


def exact_small_source(api):
    pairs = searches = surviving = 0
    for e in range(2,9):
        full = set(range(3*e+1))
        allowed = list(range(1,e-1))+list(range(2*e+2,3*e))
        for j in range(1,e):
            H = 2*e-j
            hits = set()
            for holes in combinations(allowed,2*j):
                support_ = full - set(holes)
                cert = api.certify_span_erasures(sorted(support_),H,3*e).certificate
                searches += 1
                if cert.minimum_deletions > e:
                    hits.add(tuple(holes))
            predicted = {tuple(sorted(full - support(e,j,a))) for a in range(1,e)
                         if expected(e,j,a)}
            assert hits == predicted and len(hits)==number_runs(e,j)
            pairs += 1
            surviving += len(hits)
    return {'parameter_pairs':pairs,'all_eligible_hole_sets':searches,'saturated_sets':surviving}


def source_boundaries(api):
    total = robust = 0
    examples = []
    for j in range(1,7):
        for e in sorted({6*j,6*j+1,7*j,8*j-1,8*j,10*j}):
            H = 2*e-j
            for a in sorted({j+2,2*j,2*j+1,e-4*j,e-4*j+1,(e+1)//2}):
                if not (j+2 <= a <= e-j-1):
                    continue
                s = support(e,j,a)
                cert = api.certify_span_erasures(sorted(s),H,3*e).certificate
                passes = cert.minimum_deletions > e
                assert passes == expected(e,j,a)
                total += 1
                robust += passes
                if j==4 and e in (24,25,31,32) and a in (9,(e+1)//2):
                    assert api.verify_span_erasure_certificate(cert)
                    examples.append([e,j,a,cert.minimum_deletions,
                                     cert.witness_period,cert.alias_period])
    boundary_examples = []
    for j in range(1,9):
        for e in (6*j-1,6*j):
            s = support(e,j,2*j+1)
            s.add(3*j)
            cert = api.certify_span_erasures(sorted(s),2*e-j,3*e).certificate
            assert cert.minimum_deletions == e+1 and 3*e+1-len(s)==2*j-1
            boundary_examples.append([j,e,len(s),cert.minimum_deletions])
    return {'next_best_examples':boundary_examples,'checked':total,'robust':robust,'examples_e_j_a_cut_period_alias':examples}


def legacy_examples(api):
    deleted = {4,5,6,7}
    marks = set(range(12)) - deleted
    def same(marks,r,s):
        return all(((a-b)%r==0) == ((a-b)%s==0) for a,b in combinations(marks,2))
    assert same(marks,4,8)
    marks = {0,3,6}
    assert same(marks,1,3) and not same(marks,1,2)
    assert api.minimum_erasure_span(6,4).minimum_span==12


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,default=Path('.'),help='enterprise-math checkout')
    args=ap.parse_args()
    api=native(args.repo)
    legacy_examples(api)
    result={'native_source_sha256':PIN,'source_exhaustion':exact_small_source(api),
            'threshold_cases':source_boundaries(api),'universal_proof':chambers(),'boundary_proof':chambers(True)}
    print(json.dumps(result,indent=2,sort_keys=True))
