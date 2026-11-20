"""Exact BRC signed-word meet-in-middle certificate for R762GP.
Run with Python 3 standard library; expected endpoint table is asserted.
"""
from collections import defaultdict
from itertools import combinations, permutations

E = tuple(combinations(range(4), 2))
S = [tuple(E.index(tuple(sorted((v, u)))) for u in range(4) if u != v)
     for v in range(4)]
I = tuple(range(6))
P = [p for p in permutations(I) if sum(p[a] > p[b] for a in I
                                   for b in range(a + 1, 6)) % 2 == 0]
PI = {p: i for i, p in enumerate(P)}
def mul(a, b): return tuple(a[b[i]] for i in I)
def cyc(star):
    q = list(I); a, b, c = star; q[a], q[b], q[c] = b, c, a
    return tuple(q)
G = [cyc(s) for s in S]
N = [tuple(g.index(i) for i in I) for g in G]
B = 65; POW = [B**i for i in I]; SIZE = B**6; D = sum(POW)
origin = PI[I]*SIZE + 25*D
arcs = [[] for _ in P]; reverse = [[] for _ in P]
for pi, p in enumerate(P):
    for v in E[p[0]]:
        for sign in (-1, 1):
            qi = PI[mul(p, G[v] if sign == 1 else N[v])]
            delta = sign * sum(POW[p[j]] for j in S[v])
            arcs[pi].append((qi, delta))
            reverse[qi].append((pi, -delta))
    assert len(arcs[pi]) == 4

def advance(current, graph):
    result = defaultdict(int)
    for state, count in current.items():
        pi, xcode = divmod(state, SIZE)
        for qi, delta in graph[pi]:
            result[qi*SIZE + xcode + delta] += count
    return result

F = {origin: 1}; R = {origin: 1}
expected = {
  2:{0:4}, 4:{0:28}, 6:{0:224}, 8:{0:1884},
  10:{0:16256}, 12:{-6:8,0:142616,6:8},
  14:{-6:324,0:1267096,6:324},
  16:{-6:7936,-4:1,-1:1,0:11376408,1:1,4:1,6:7936}}
for half in range(1, 9):
    F = advance(F, arcs); R = advance(R, reverse)
    count = {k:sum(mult*R.get(state-k*D, 0) for state,mult in F.items())
             for k in range(-half, half+1)}
    count = {k:v for k,v in count.items() if v}
    assert count == expected[2*half], (half, count)
    print(2*half, count, 'half-states', len(F), len(R))

def check(word, k):
    x = [0]*6; p = I; ports = []
    for v,s in word:
        e = E[p[0]]; assert v in e
        ports.append(''.join(map(str,e)))
        for j in S[v]: x[p[j]] += s
        p = mul(p, G[v] if s == 1 else N[v])
    assert x == [k]*6 and p == I
    return ports

positive = [(0,1),(2,1),(0,1),(2,-1),(2,-1),(1,-1),(3,-1),(1,-1),
            (2,1),(0,1),(1,1),(3,1),(0,1),(1,1),(2,-1),(1,-1)]
negative = [(1,-1),(3,-1),(1,-1),(3,1),(3,1),(0,1),(2,1),(0,1),
            (3,-1),(1,-1),(0,-1),(2,-1),(1,-1),(0,-1),(3,1),(0,1)]
print('positive ports', check(positive, 1))
print('negative ports', check(negative, -1))
print('PASS: L(+D)=L(-D)=16; each C_16=1')
