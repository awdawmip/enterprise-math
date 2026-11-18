"""Fully expanded nested profile key on one pair; no color identifiers or graph library."""
from collections import Counter

GRAPHS = ("N??CA?_CCOH_HGCc?X?", "N??CA?_CCCL?EC@WOg?")


def graph6(text):
    n = ord(text[0])-63
    bits = "".join(f"{ord(x)-63:06b}" for x in text[1:])
    adj = [set() for _ in range(n)]
    i = 0
    for v in range(n):
        for u in range(v):
            if bits[i] == "1":
                adj[u].add(v)
                adj[v].add(u)
            i += 1
    return adj


def rooted_profile(adj, root):
    # One DFS from each root; both orientations are counted and divided by two.
    counts = [0]*(len(adj)-2)
    queue = [(root, frozenset((root,)))]
    while queue:
        tip, visited = queue.pop()
        for neighbor in adj[tip]:
            if neighbor not in visited:
                queue.append((neighbor, visited | {neighbor}))
            elif neighbor == root and len(visited) >= 3:
                counts[len(visited)-3] += 1
    assert all(x%2==0 for x in counts)
    return tuple(x//2 for x in counts)


def layers(adj):
    labels = [rooted_profile(adj,v) for v in range(len(adj))]
    for depth in range(4):
        yield Counter(labels)
        if depth < 3:
            labels = [(v,tuple(sorted(labels[x] for x in adj[i])))
                      for i,v in enumerate(labels)]


if __name__ == "__main__":
    for d,(left,right) in enumerate(zip(*(layers(graph6(g)) for g in GRAPHS))):
        equal = left == right
        print(d,equal,sum((left-right).values()),sum((right-left).values()))
        assert equal == (d < 3)
