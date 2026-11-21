#!/usr/bin/env python3
"""Exact source-labelled finite-state checker for PREFIX-979; Python 3 stdlib."""
from collections import Counter
import json

def source_dictionary(p):
    result = {}
    for i in range(p):
        for j in range(p):
            for s in (1, -1):
                c = (1 << i) - s * (1 << j)
                result.setdefault(c, []).append((i, j, s))
    return result

def mask_data(p, source):
    A = ((1 << p) - 1) ^ 1
    masks = {}
    for c, triples in source.items():
        P = M = 0
        for i, j, s in triples:
            if s == 1:
                P |= 1 << j
            else:
                M |= 1 << j
        masks[c] = (P & A, M & A)
    return masks

def predicted(P, M, Q, N):
    cross = (P & N) | (M & Q)
    return bool(cross or ((P & M) and (Q & N))), cross.bit_count()

def actual_graph(p, c, C, source):
    """Independent original (i,j,s) transition graph, no mask lookup."""
    m = 1 << (p - 1)
    graph = [[] for _ in range(2*m)]
    for phase, residual in enumerate((c, C)):
        for k in range(m):
            x = 2*k + 1
            for i, j, s in source[residual]:
                if j == 0:
                    continue
                if ((x >> j) & 1) != int(s == -1):
                    continue
                xx = x ^ (1 << j)
                graph[phase*m+k].append((1-phase)*m+(xx//2))
    return graph

def cyclic_and_longest(graph):
    color = [0]*len(graph)
    memo = [0]*len(graph)
    def visit(v):
        if color[v] == 1:
            raise ValueError('directed cycle')
        if color[v] == 2:
            return memo[v]
        color[v] = 1
        mx = 0
        for w in graph[v]:
            mx = max(mx, 1+visit(w))
        color[v] = 2
        memo[v] = mx
        return mx
    try:
        for v in range(len(graph)):
            visit(v)
    except ValueError:
        return True, None
    return False, max(memo[:len(graph)//2])

def enumerated_counts(p):
    src = source_dictionary(p)
    d = mask_data(p, src)
    counts = Counter()
    rank_hist = Counter()
    for c, (P,M) in d.items():
        for C, (Q,N) in d.items():
            persistent, cross_count = predicted(P,M,Q,N)
            mode = int(bool(P&M))+int(bool(Q&N))
            counts[(mode, bool(cross_count), persistent)] += 1
            rank_hist[cross_count] += 1
    return src, d, counts, rank_hist

def verify_small():
    checked = 0
    max_one_sided = 0
    for p in range(3,7):
        src, d, _, _ = enumerated_counts(p)
        for c, (P,M) in d.items():
            for C, (Q,N) in d.items():
                pred, cross_count = predicted(P,M,Q,N)
                actual, longest = cyclic_and_longest(actual_graph(p,c,C,src))
                assert actual == pred, (p,c,C,pred,actual)
                if cross_count == 0 and (bool(P&M) ^ bool(Q&N)):
                    assert not actual and longest <= 5, (p,c,C,longest)
                    max_one_sided = max(max_one_sided, longest)
                checked += 1
    return checked, max_one_sided

def verify_sharp_witness():
    p, x = 6, 41
    src = source_dictionary(p)
    history = []
    for c, j in ((6,1),(40,3),(6,1),(40,5),(6,1)):
        available = [(i,jj,s) for i,jj,s in src[c]
                     if jj == j and ((x>>jj)&1) == int(s==-1)]
        assert len(available) == 1, (x,c,j,available)
        history.append({'x':x,'residual':c,'port':j,'source':available[0]})
        x ^= 1 << j
    assert x == 3
    return history

def main():
    checked, max_one_sided = verify_small()
    assert max_one_sided <= 5
    history = verify_sharp_witness()
    _, d, counts, hist = enumerated_counts(19)
    assert len(d) == 499
    n = sum(bool(P&M) for P,M in d.values())
    assert n == 16
    total = sum(counts.values())
    cross = sum(v for (mode,J,inf),v in counts.items() if J)
    inf = sum(v for (mode,J,persist),v in counts.items() if persist)
    assert (total,cross,inf,counts[(2,False,True)]) == (249001,12642,12852,210)
    out = {'schema':'PREFIX979_R6_EXACT_INTEGER_V1',
           'model':'independent auxiliary BRC positive source-port observer, alternating c,C',
           'source_equation':'c=2**i-s*2**j; 0<=i,j<p, s=+1 or -1; odd x; ports j>=1',
           'p19':{'distinct_residues':len(d),'individual_persistent_residues':n,
                  'ordered_pairs':total,'J_nonempty_pairs':cross,
                  'persistent_pairs':inf,'finite_pairs':total-inf,
                  'J_empty_both_persistent':counts[(2,False,True)],
                  'J_histogram':dict(sorted(hist.items())),
                  'class_counts':{'mode_%s_J_%s_persistent_%s'%key:value
                                  for key,value in sorted(counts.items())}},
           'independent_full_source_graph':{
               'bit_widths':[3,4,5,6], 'ordered_pair_checks':checked,
               'method':'DFS cycle detection on original named (i,j,s) state graph; compare cross/reuse criterion',
               'max_one_sided_length_seen':max_one_sided},
           'sharp_five_step_witness_p6':history,
           'limitations':['Exhaustive p=19 pair enumeration, not full 19-bit state graph',
                          'No native X6/triadic update equivalence',
                          'No independent scientific peer review']}
    print(json.dumps(out, ensure_ascii=False, sort_keys=True, indent=2))

if __name__ == '__main__':
    main()
