"""R762IR: exact constructive 54-to-46 Port-Euler witness, standard Python 3."""
from itertools import combinations
from collections import deque

P = list(combinations(range(6), 2))
S = list(combinations(range(6), 3))
pi = {p: i for i, p in enumerate(P)}
TRI = [tuple(pi[p] for p in combinations(s, 2)) for s in S]
EDGES = [((a,b),(a,c),(b,c)) for a,b,c in TRI]

def partition(triples):
    parent = list(range(15))
    def root(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for i in triples:
        a,b,c = TRI[i]
        parent[root(a)] = root(b)
        parent[root(b)] = root(c)
    return tuple(root(x) == root(y) for x in range(15) for y in range(x))

def boundary(edges):
    mask = 0
    for a,b in edges:
        mask ^= (1<<a) ^ (1<<b)
    return mask

def realize(s, mask):
    options = EDGES[s]
    if mask == 0:
        return list(options)
    edge = next(e for e in options if ((1<<e[0]) ^ (1<<e[1])) == mask)
    other = next(e for e in options if e != edge)
    return [edge, other, other]

def validate(H, target):
    assert len(H) == 20
    degrees = [0]*15
    parent = list(range(15))
    def root(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for s,edges in enumerate(H):
        assert len(edges) == target[s]
        assert all(e in EDGES[s] for e in edges)
        for a,b in edges:
            degrees[a] += 1
            degrees[b] += 1
            parent[root(a)] = root(b)
    assert all(d > 0 and d%2 == 0 for d in degrees)
    assert len({root(i) for i in range(15)}) == 1
    return sum(len(e) for e in H)

def reduce_once(H):
    n = [len(e) for e in H]
    strong = [s for s in range(20) if n[s] == 3]
    assert len(strong) >= 11
    original = partition(strong)
    j = next(s for s in strong
             if partition([i for i in strong if i != s]) == original)
    picked = EDGES[j][0]
    delta = boundary(H[j]) ^ boundary([picked])
    ans = [list(x) for x in H]
    ans[j] = [picked]
    if delta:
        ends = [x for x in range(15) if delta>>x & 1]
        assert len(ends) == 2
        adj = {x: [] for x in range(15)}
        for s in strong:
            if s == j:
                continue
            for a,b in EDGES[s]:
                adj[a].append((b,s,a,b))
                adj[b].append((a,s,a,b))
        q = deque([ends[0]])
        prev = {ends[0]: None}
        while q and ends[1] not in prev:
            a = q.popleft()
            for b,s,x,y in adj[a]:
                if b not in prev:
                    prev[b] = (a,s,x,y)
                    q.append(b)
        assert ends[1] in prev
        toggles = {s: 0 for s in strong if s != j}
        at = ends[1]
        while prev[at] is not None:
            prior,s,a,b = prev[at]
            toggles[s] ^= (1<<a) ^ (1<<b)
            at = prior
        for s in toggles:
            ans[s] = realize(s, boundary(H[s]) ^ toggles[s])
    validate(ans, [len(x) for x in ans])
    return j, ans

def main():
    doubles = (0,1,2,4,5,7)
    H = [list(EDGES[s]) if s not in doubles
         else [EDGES[s][0]]*2 for s in range(20)]
    assert validate(H, [3 if s not in doubles else 2 for s in range(20)]) == 54
    chosen = []
    while sum(len(edges)==3 for edges in H) > 10:
        j,H = reduce_once(H)
        chosen.append(j)
    assert validate(H, [len(x) for x in H]) == 46
    assert len(chosen) == 4
    print("PASS R762IR: n3=14,n2=6; 54->46, deleted pairs at supports", chosen)
    print("Support triple indices:", [S[j] for j in chosen])
    print("Final multiplicities:", [len(x) for x in H])

if __name__ == "__main__":
    main()
