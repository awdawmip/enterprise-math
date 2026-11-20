"""Bound affine stabilizers using the proved exclusions on orders three, four and five."""
from collections import Counter, deque
from itertools import permutations, product
import json

def verify():
    basis = ((1,0,0),(0,1,0),(0,0,1))
    def matrix(perm, signs, unit):
        return tuple(tuple(unit * signs[i] * (perm[i] == j) % 5 for j in range(3)) for i in range(3))
    group = sorted({matrix(p, s, c) for p in permutations(range(3))
                    for s in product((1,-1), repeat=3) for c in (1,2)})
    ix = {m:i for i,m in enumerate(group)}
    def mul(a,b):
        return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3)) % 5 for j in range(3)) for i in range(3))
    op = [[ix[mul(a,b)] for b in group] for a in group]
    identity = ix[basis]
    inversion = ix[matrix((0,1,2),(1,1,1),4)]
    def order(a):
        p, k = a, 1
        while p != identity:
            p, k = op[p][a], k+1
        return k
    def count(use_cost_bound):
        allowed = {i for i in range(len(group)) if op[i][i] != inversion
                   and (not use_cost_bound or order(i) in (1, 2))}
        trivial = frozenset((identity,))
        pending, seen = deque([trivial]), {trivial}
        while pending:
            h = pending.popleft()
            for a in allowed - h:
                # The coset h*a must lie in every subgroup containing h and a.
                coset = {op[v][a] for v in h}
                if min(coset) != a or not coset <= allowed:
                    continue
                generators = tuple(h) + (a,)
                new, queue = set(h), deque(h)
                while queue:
                    u = queue.popleft()
                    for v in generators:
                        x = op[u][v]
                        if x not in new:
                            new.add(x)
                            if x not in allowed:
                                queue.clear()
                                break
                            queue.append(x)
                expanded = frozenset(new)
                if expanded <= allowed and expanded not in seen:
                    seen.add(expanded)
                    pending.append(expanded)
        return seen
    assert len(group) == 96
    all_eleven, cheap = count(False), count(True)
    cubes = [h for h in cheap if len(h) == 8]
    assert len(cubes) == 4
    def summary(groups):
        compatible = [h for h in groups if all(not (e <= h) for e in cubes)]
        return dict(sorted(Counter(map(len, compatible)).items()))
    reflection = ix[matrix((0,1,2),(-1,1,1),1)]
    inverse = {g:next(i for i in range(len(group)) if op[g][i]==identity) for g in range(len(group))}
    reflections = {op[g][op[reflection][inverse[g]]] for g in range(len(group))}
    assert len(reflections)==3
    # Every Klein subgroup and every single-axis reflection have independent cost exclusions.
    strict = [h for h in cheap if len(h)<=2 and h.isdisjoint(reflections)]
    return {'all_eleven':summary(all_eleven), 'strictly_below_11292':summary(strict)}

if __name__=='__main__':
    print(json.dumps(verify(), sort_keys=True, indent=2))
