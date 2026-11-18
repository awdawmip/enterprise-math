"""Exact small trees, simple Cell returns and joint colour refinement, standard library."""
from collections import Counter, defaultdict


import json


def canonical_tree(tree):
    def rooted(i, parent):
        return '(' + ''.join(sorted(rooted(j, i) for j in tree[i] if j != parent)) + ')'
    return min(rooted(r, -1) for r in range(len(tree)))


def tree_levels(limit):
    current = [[[]]]
    for size in range(1, limit + 1):
        yield current
        if size == limit:
            break
        next_level = {}
        for t in current:
            for v, row in enumerate(t):
                if len(row) < 3:
                    u = [adj[:] for adj in t] + [[v]]
                    u[v].append(size)
                    next_level[canonical_tree(u)] = u
        current = list(next_level.values())


def add_edge(graph, i, j):
    graph[i].append(j)
    graph[j].append(i)


def expand(tree, lengths=None, slots=None):
    if lengths is None:
        lengths = [3]*len(tree)
    if slots is None:
        slots = [list(range(len(row))) for row in tree]
    graph, ports = [], []
    for i, size in enumerate(lengths):
        offset = len(graph)
        graph.extend([] for _ in range(size))
        for p in range(size):
            add_edge(graph, offset+p, offset+(p+1) % size)
        ports.append(dict(zip(tree[i], (offset+j for j in slots[i]))))
    for i, row in enumerate(tree):
        for j in row:
            if j > i:
                add_edge(graph, ports[i][j], ports[j][i])
    return graph


def primitive_packet(graph):
    counts = [Counter() for _ in graph]
    for start in range(len(graph)):
        stack = [(start,)]
        while stack:
            path = stack.pop()
            for j in graph[path[-1]]:
                if j == start and len(path) >= 3 and path[1] < path[-1]:
                    for x in path:
                        counts[x][len(path)] += 1
                if j > start and j not in path:
                    stack.append(path+(j,))
    return Counter(tuple(sorted(row.items())) for row in counts)


def wl_history(graphs):
    """One shared palette per round. Stop at joint partition stabilization or full separation."""
    union, groups = [], []
    for g in graphs:
        start = len(union)
        groups.append(range(start, start+len(g)))
        union.extend([start+j for j in row] for row in g)
    colors, num = [0]*len(union), 1
    track = []
    while True:
        packets = [tuple(sorted(Counter(colors[i] for i in group).items())) for group in groups]
        track.append(len(set(packets)))
        if track[-1] == len(graphs):
            return track
        keys = [(colors[i], tuple(sorted(colors[j] for j in row))) for i, row in enumerate(union)]
        palette = {key: i for i, key in enumerate(sorted(set(keys)))}
        if len(palette) == num:
            return track
        colors = [palette[key] for key in keys]
        num = len(palette)


def tripod(arms):
    t = [[] for _ in range(sum(arms)+1)]
    top = 1
    for arm in arms:
        prev = 0
        for _ in range(arm):
            add_edge(t, prev, top)
            prev, top = top, top+1
    return t


def counts_polya(k, cutoff):
    """Compute the dihedral cycle-index series for planted, vertex-, edge- and free trees."""
    one = [1]+[0]*cutoff
    def multiply(a, b):
        return [sum(a[i]*b[m-i] for i in range(m+1)) for m in range(cutoff+1)]
    def product_of(factors):
        result = one
        for a in factors:
            result = multiply(result, a)
        return result
    def subst(a, d):
        return [a[i//d] if i % d == 0 else 0 for i in range(cutoff+1)]
    def rotation(n):
        return [(i+n) % k for i in range(k)]
    def reflection(n):
        return [(n-i) % k for i in range(k)]
    def cycles(perm, omit=None):
        left = set(range(len(perm))) - ({omit} if omit is not None else set())
        lens = []
        while left:
            j = min(left)
            length = 0
            while j in left:
                left.remove(j)
                j = perm[j]
                length += 1
            lens.append(length)
        return lens
    stabs = [cycles(g, 0) for g in [rotation(0), reflection(0)]]
    bouquet = [cycles(g) for n in range(k) for g in [rotation(n), reflection(n)]]
    def necklace(p, types, index):
        p = [p[0]+1] + p[1:]
        numerator = sum(product_of([subst(p, j) for j in lengths])[index] for lengths in types)
        assert numerator % len(types) == 0
        return numerator // len(types)
    plant = [0]*(cutoff+1)
    for n in range(1, cutoff+1):
        plant[n] = necklace(plant, stabs, n-1)
    pair, double = multiply(plant, plant), subst(plant, 2)
    free = [0]
    for n in range(1, cutoff+1):
        assert (pair[n] - double[n]) % 2 == 0
        free.append(necklace(plant, bouquet, n-1) - (pair[n]-double[n])//2)
    return free[1:]


def direct_dihedral(k, maximum):
    """List explicit port words up to plant reflection / free centre re-rooting."""
    planted = defaultdict(set)
    free_counts = []
    def words(arity, total):
        if arity == 0:
            if total == 0:
                yield ()
            return
        for m in range(total+1):
            for item in (planted[m] if m else ['.']):
                for rest in words(arity-1, total-m):
                    yield (item,) + rest
    def code(seq):
        return '(' + ''.join(seq) + ')'
    def free_code(word):
        """Minimum over all re-rootings of this embedded polygon tree."""
        def read(codeword):
            if codeword == '.':
                return None
            children, start, depth = [], 1, 0
            for i in range(1, len(codeword)-1):
                depth += (codeword[i]=='(') - (codeword[i]==')')
                if depth == 0:
                    children.append(read(codeword[start:i+1]))
                    start = i+1
            return children
        nodes = []
        def add(parent, entries, isroot=False):
            idx = len(nodes)
            nodes.append([] if isroot else [parent])
            for child in entries:
                nxt = None if child is None else add(idx, child)
                nodes[idx].append(nxt)
            assert len(nodes[idx]) == k
            return idx
        add(None, list(map(read, word)), True)
        def from_port(v, parent):
            ports = nodes[v]
            if parent is not None:
                i = ports.index(parent)
                others = ports[i+1:]+ports[:i]
            else:
                others = ports
            seq = tuple('.' if child is None else from_port(child, v) for child in others)
            if parent is not None:
                return code(min(seq, seq[::-1]))
            return min(code(s[i:]+s[:i]) for s in [seq, seq[::-1]] for i in range(k))
        return min(from_port(v, None) for v in range(len(nodes)))
    for n in range(1, maximum+1):
        planted[n] = {code(min(w, w[::-1])) for w in words(k-1, n-1)}
        free_counts.append(len({free_code(w) for w in words(k, n-1)}))
    return free_counts


def main():
    census = {}
    for m, models in enumerate(tree_levels(12), 1):
        graphs = [expand(t) for t in models]
        if m <= 8:
            for graph in graphs:
                assert primitive_packet(graph) == {((3, 1),): 3*m}
        trace = wl_history(graphs)
        assert trace[-1] == len(models)
        census[m] = {'tree_types': len(models), 'distinct_packets_by_round': trace}
    pure = {}
    for k in range(3, 8):
        predicted = counts_polya(k, 12)
        direct = direct_dihedral(k, 5)
        assert direct == predicted[:5] and predicted[2] == k//2
        pure[k] = {'sizes_1_to_12': predicted, 'reference_enumeration_sizes_1_to_5': direct}
    assert pure[3]['sizes_1_to_12'] == [x['tree_types'] for x in census.values()]
    deep = []
    for L in [2, 3, 5, 9, 17, 33]:
        trees = [tripod(a) for a in [(L, L, 3*L), (L, 2*L, 2*L)]]
        assert canonical_tree(trees[0]) != canonical_tree(trees[1])
        history = wl_history([expand(t) for t in trees])
        assert history[-1] == 2
        last_equal = len(history)-2
        radius_bound = (L-3)//2
        assert last_equal >= radius_bound
        deep.append({'L': L, 'cells': 3*(5*L+1), 'first_distinguishing_round': len(history)-1})
    mixed = expand([[1], [0]], [3, 5])
    add0, add1 = 0, 3
    mixed[add0].remove(add1)
    mixed[add1].remove(add0)
    mixed.extend([[], []])
    for i, j in [(add0, 8), (8, 9), (9, add1)]:
        add_edge(mixed, i, j)
    packet = primitive_packet(mixed)
    assert packet == {((3, 1),): 3, ((5, 1),): 5, (): 2}
    print(json.dumps({'triangle_fibres': census, 'uniform_cycle_dihedral_fibres': pure,
                      'same_size_tripod_witnesses': deep, 'mixed_example': 
                      {'lengths': [3, 5], 'zero_return_roots': packet[()]}}, indent=2))


if __name__ == '__main__':
    main()
