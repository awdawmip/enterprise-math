"""Verify the simultaneous near-full-class packing restrictions from the endpoint semantics."""
from collections import Counter
from itertools import permutations, product
from pathlib import Path
import subprocess

from cyclic11 import P, class_cost, index, observations, setbits
from six13 import enumerate_classes, is_legal

FULL = (1 << 125) - 1

def image(mask, action):
    return sum(1 << action[i] for i in setbits(mask))

def shifted(p, d):
    return index(tuple((x+y) % 5 for x,y in zip(p,d)))

def linear_actions():
    return [tuple(index(tuple(a*s*p[j] % 5 for j,s in zip(perm,sg))) for p in P)
            for perm in permutations(range(3)) for sg in product((1,-1),repeat=3) for a in (1,2)]

def inventory(actions, bad, costs):
    A = {0}
    for h,k in product((1,-1),repeat=2):
        A.update((index((0,2*h%5,k%5)),index((h%5,0,2*k%5)),index((2*h%5,k%5,0))))
    base = sum(1 << i for i in A)
    shapes = {image(base,t) for t in actions}
    parents = sorted({sum(1 << shifted(P[i],d) for i in setbits(s)) for s in shapes for d in P})
    # Previous all-class enumeration proves there are exactly 250 13-point classes,
    # 250 cost-1104 12-classes, and 3000 cost-1116 12-classes.
    assert len(parents) == 250 and all(is_legal(p,bad) for p in parents)
    families = {1104:set(),1116:set()}
    centers = []
    for row in parents:
        one = []
        for i in setbits(row):
            reduced = row ^ (1<<i)
            cost = class_cost(list(setbits(reduced)),costs)
            families[cost].add(reduced)
            if cost == 1104: one.append(i)
        assert len(one) == 1
        centers.append(one[0])
    assert [len(x) for x in families.values()] == [250,3000]
    return parents, centers

def normalize(parents, centers, actions):
    base = parents[0]
    ix = {p:i for i,p in enumerate(parents)}
    maps = []
    stabilizer = []
    for i,p in enumerate(parents):
        first = None
        for t in actions:
            d = tuple((x-y)%5 for x,y in zip(P[centers[0]],P[t[centers[i]]]))
            both = tuple(shifted(P[j], d) for j in t)
            if image(p,both) == base:
                ids = [ix[image(m,both)] for m in parents]
                if i == 0: stabilizer.append(ids)
                if first is None: first = ids
                if i: break
        assert first
        maps.append(first)
    def key(packed):
        return min(tuple(sorted(st[maps[i][j]] for j in packed))
                   for i in packed for st in stabilizer)
    return key

def residuals(rows):
    double = 0; seen = 0
    for m in rows:
        double |= m & seen
        seen |= m
    def search(j,selected):
        if j == len(rows):
            yield FULL ^ selected
            return
        m = rows[j]
        # Every eight-parent representative has union defect eight. Disjointness
        # therefore forces all omissions onto shared points.
        for i in setbits(m & double):
            reduced = m ^ (1 << i)
            if not selected & reduced:
                yield from search(j+1, selected | reduced)
    assert 13 * len(rows) - seen.bit_count() == 8
    return set(search(0,0))

def three_cover(R,bad):
    # Take a largest class in a putative cover, then a largest remaining one.
    # Include the empty class so that this tests "at most three".
    n = R.bit_count()
    for x in enumerate_classes(R,(n+2)//3,bad):
        rem = R ^ x
        if is_legal(rem,bad): return True
        for y in enumerate_classes(rem,(rem.bit_count()+1)//2,bad):
            if is_legal(rem ^ y,bad): return True
    return False

def verify(directory):
    bad, costs = observations()
    actions = linear_actions()
    parents, centers = inventory(actions,bad,costs)
    path = directory / "parents.txt"
    path.write_text("".join(f"{p % (1<<64)} {p >> 64} {c}\n" for p,c in zip(parents,centers)))
    reports = {}
    based = []
    for k in (7,8,9):
        result = subprocess.check_output([str(directory/"parent_packing"),str(k),str(path)],text=True)
        support = []
        for line in result.splitlines():
            u = line.split()
            if u[0] == 'support': support.append(list(map(int,u[1:])))
            elif u[0] == 'counts': candidate, feasible = map(int,u[1:])
            else: based.append(list(map(int,u)))
        reports[k] = dict(candidate_parents=candidate, feasible_parents=feasible, types=support)
    assert reports[7]['types'] == [[0,5],[0,6],[0,7],[1,6]]
    assert reports[8]['types'] == [[0,8]]
    assert reports[9]['types'] == []
    key = normalize(parents,centers,actions)
    representatives = {key(p) for p in based}
    trials = []
    for example in representatives:
        R = residuals([parents[i] for i in example])
        assert len(R)==1
        space=next(iter(R))
        trials.append([space.bit_count(), three_cover(space,bad)])
    assert trials==[[29,False]]*4
    return dict(parent_packing=reports,eight_parent_orbits=len(representatives),three_label_completions=0)
