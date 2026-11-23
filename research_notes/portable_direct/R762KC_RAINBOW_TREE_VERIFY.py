#!/usr/bin/env python3
"""R762KC: eight explicit rainbow trees prove universal Euler feasibility."""
from itertools import combinations, permutations
from math import comb
import json, random

AX=tuple(range(6))
P=tuple(combinations(AX,2)); P=tuple(v for v in P if v!=(0,1))
S=tuple(combinations(AX,3))
F=tuple((0,1,i) for i in range(2,6))
C=tuple(s for s in S if s not in F)
INDEX={v:i for i,v in enumerate(P)}
# Each table entry COLOR:PORT-PORT. Thirteen distinct colors form one spanning tree.
CERT={
 '023,024': '025:02-05 034:04-34 035:03-05 045:04-05 123:12-13 125:12-15 134:13-14 135:13-35 145:14-45 234:23-34 235:23-25 245:24-45 345:34-35',
 '023,045': '024:04-24 025:02-25 034:03-04 035:05-35 124:12-14 125:12-25 134:13-34 135:13-15 145:14-45 234:23-34 235:23-35 245:24-25 345:35-45',
 '023,123': '024:02-24 025:02-05 034:03-04 045:04-05 124:14-24 125:12-15 134:14-34 135:13-35 145:15-45 234:23-34 235:25-35 245:24-25 345:35-45',
 '023,124': '024:02-24 025:05-25 034:03-04 035:03-05 045:05-45 123:12-23 125:15-25 134:13-14 135:15-35 145:14-15 234:23-24 235:23-25 345:34-45',
 '023,145': '024:02-24 025:02-05 034:03-34 035:03-35 045:04-45 123:12-13 124:12-14 125:15-25 135:13-35 234:24-34 235:23-25 245:24-25 345:34-45',
 '023,234': '024:02-04 025:02-05 034:03-04 045:04-45 123:12-13 124:14-24 125:12-25 134:13-34 135:13-15 145:14-45 235:23-25 245:24-25 345:34-35',
 '023,245': '024:02-04 025:05-25 034:04-34 035:03-35 045:04-45 123:12-23 125:12-25 134:13-34 135:13-15 145:14-45 234:24-34 235:25-35 345:35-45',
 '234,235': '023:02-03 024:04-24 025:02-25 034:04-34 035:03-35 045:04-05 123:13-23 124:14-24 125:12-25 134:13-34 135:13-15 145:15-45 345:34-35',
}

def name(xs):return ''.join(map(str,xs))
def from_name(s):return tuple(map(int,s))
def allowed(s):
    v=tuple(t for t in combinations(s,2) if t in INDEX)
    return tuple(combinations(v,2))
def m(e):return (1<<INDEX[e[0]])^(1<<INDEX[e[1]])
def permute(t,g):return tuple(sorted(g[i] for i in t))
def perm_edge(e,g):return tuple(sorted((permute(e[0],g),permute(e[1],g))))

def parse_table(pair,entries):
    tree=[]
    for token in entries.split():
        c,ee=token.split(':');a,b=ee.split('-')
        tree.append((from_name(c), (from_name(a),from_name(b))))
    assert len(tree)==13 and len({c for c,_ in tree})==13
    assert all(c in C and c not in pair and e in allowed(c) for c,e in tree)
    # 13 edges on 14 vertices + connected => a tree.
    assert connected([e for _,e in tree])
    return tree

def connected(edge_list):
    g={x:set() for x in P}
    for a,b in edge_list:g[a].add(b);g[b].add(a)
    seen={P[0]};todo=[P[0]]
    while todo:
        v=todo.pop()
        for w in g[v]-seen:seen.add(w);todo.append(w)
    return len(seen)==14

def map_orbits():
    group=[(a,b)+tail for a,b in ((0,1),(1,0)) for tail in permutations((2,3,4,5))]
    mapping={};sizes=[]
    for k,entries in CERT.items():
        rep=tuple(from_name(x) for x in k.split(','))
        tree=parse_table(rep,entries)
        images=set()
        for g in group:
            image=tuple(sorted(permute(c,g) for c in rep))
            images.add(image)
            if image not in mapping:
                mapping[image]=[(permute(c,g),perm_edge(e,g)) for c,e in tree]
        sizes.append(len(images))
    assert len(mapping)==comb(16,2)==120
    assert sorted(sizes)==[6,6,6,6,24,24,24,24]
    return mapping,sizes

def realize(s,n,boundary_edge):
    assert n>=1 and boundary_edge in allowed(s)
    if len(allowed(s))==1:return [boundary_edge]*n
    options=allowed(s)
    if n==1:return [boundary_edge]
    others=[e for e in options if e!=boundary_edge]
    base=others if n%2==0 else [boundary_edge,others[0],others[0]]
    return list(base)+[options[0]]*(n-len(base))

def construct(counts,pair,tree):
    assert all(counts[c]>=1 for c in S)
    assert set(pair)<=set(C) and all(counts[c]>=2 for c in C if c not in pair)
    # Each tree color offers two boundary edges whose XOR is the chosen tree edge.
    base={};alt={}
    for c,e in tree:
        x,y=[q for q in allowed(c) if q!=e]
        base[c]=x;alt[c]=y
        assert m(x)^m(y)==m(e)
    for c in C:
        if c not in pair and c not in base:base[c]=allowed(c)[0]
    for c in pair:base[c]=allowed(c)[0]
    residue=0
    for c in F:
        if counts[c]%2:residue^=m(allowed(c)[0])
    for c in C:residue^=m(base[c])
    # Tree boundary map: peel leaf parity toward root PORTS[0].
    adjacency={v:[] for v in P}
    for c,(a,b) in tree:
        adjacency[a].append((b,c));adjacency[b].append((a,c))
    parent={P[0]:None};todo=[P[0]];order=[]
    while todo:
        v=todo.pop();order.append(v)
        for w,c in adjacency[v]:
            if w not in parent:parent[w]=(v,c);todo.append(w)
    assert len(order)==14
    for v in reversed(order[1:]):
        parent_vertex,color=parent[v]
        if residue & (1<<INDEX[v]):
            base[color]=alt[color]
            residue^=m(next(e for c,e in tree if c==color))
    assert residue==0
    events=[]
    for c in S:
        edge=allowed(c)[0] if c in F else base[c]
        es=realize(c,counts[c],edge)
        assert len(es)==counts[c]
        events.extend(es)
    deg={v:0 for v in P}
    for a,b in events:deg[a]+=1;deg[b]+=1
    assert all(deg[v]>0 and deg[v]%2==0 for v in P)
    assert connected(events)
    return events

def main():
    mapping,sizes=map_orbits()
    rng=random.Random(762003)
    tested=0;profiles=0
    for pair,tree in mapping.items():
        rest=tuple(c for c in C if c not in pair)
        extremes=(rest[:6],rest[-6:])
        for forced_triple in F:
            for six_triples in extremes:
                counts={c:(3 if c==forced_triple else 1) for c in F}
                counts.update({c:1 if c in pair else 3 if c in six_triples else 2 for c in C})
                assert sum(counts.values())==42
                assert len(construct(counts,pair,tree))==42
                tested+=1
        # Extra theorem: arbitrary multiplicities, not just 42-event histograms.
        for i in range(4):
            counts={c:rng.randint(1,8) for c in F}
            counts.update({c:rng.randint(1,8) if c in pair else rng.randint(2,8) for c in C})
            assert len(construct(counts,pair,tree))==sum(counts.values())
            profiles+=1
    evidence={
        'schema':'ENTERPRISE_MATH_R762KC_RAINBOW_TREE_V1',
        'model':'unsigned composite Port-Euler; inactive pair Port 01',
        'frozen_science':'p000_reality_foundation.json@a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'finite_combinatorial_certificates':len(CERT),
        'stabilizer_order':48,'pair_orbit_sizes':sorted(sizes),
        'covered_nonforced_exceptional_pairs':len(mapping),
        'tree_edges_per_certificate':13,'active_ports':14,
        'exact_42_event_regressions':tested,
        'arbitrary_multiplicity_regressions':profiles,
        'deduced_labeled_d3t1_42_event_inventories':4*comb(16,2)*comb(14,6),
        'deduced_marked_44_to_42_inventories':5*4*comb(16,2)*comb(14,6),
        'failures':0,'review':'NOT_REVIEWED'
    }
    print(json.dumps(evidence,sort_keys=True,ensure_ascii=False))

if __name__=='__main__':main()
