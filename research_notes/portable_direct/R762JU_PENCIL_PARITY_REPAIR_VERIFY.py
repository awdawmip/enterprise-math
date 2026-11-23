#!/usr/bin/env python3
"""R762JU: exact constructive audit of the 4-singleton pencil lemma in the
42-event section; pure Python stdlib, no numerical solver. The stronger
all-n>=2 theorem is proved by the general construction in the companion note.
"""
from itertools import combinations
from collections import defaultdict
import json

A=range(6)
PORTS=tuple(combinations(A,2))
COLORS=tuple(combinations(A,3))
AB=(0,1)
D=tuple(c for c in COLORS if set(AB).issubset(c))
assert len(D)==4

def p(x):return tuple(int(z) for z in x)
def s(x):return tuple(int(z) for z in x)
def cert(rows):
    out=[]
    tokens=rows.split()
    assert len(tokens)%3==0
    for i in range(0,len(tokens),3):
        color,u,v=tokens[i:i+3];out.append((s(color),p(u),p(v)))
    return tuple(out)

RAINBOW={
0:cert('034 04 34  135 13 35  234 23 34  235 23 35  023 03 23  035 03 05  134 13 14  245 25 45  025 05 25  124 12 24  145 15 45  123 12 23  024 02 04'),
1:cert('035 03 35  025 05 25  135 13 35  034 03 04  045 04 45  145 15 45  345 34 35  124 12 14'),
2:cert('124 12 14  024 02 04  034 04 34  135 15 35')
}
PARITY_TREE={
0:cert('023 02 03  024 02 04  025 02 05  023 02 23  024 02 24  025 02 25  034 03 34  035 03 35  045 04 45  123 23 12  123 23 13  124 24 14  125 25 15'),
1:cert('024 02 04  025 02 05  024 02 24  025 02 25  034 04 03  034 04 34  045 04 45  035 05 35  124 24 12  124 24 14  125 25 15  134 34 13'),
2:cert('024 02 04  025 02 05  024 02 24  025 02 25  034 04 03  034 04 34  035 05 35  124 24 12  124 24 14  125 25 15  134 34 13')
}

def setup(m):
    M=tuple(((2,3),(4,5))[:m]);V=set(PORTS)-set(M)
    forced={};flex={}
    for c in COLORS:
        pts=tuple(z for z in combinations(c,2) if z in V)
        assert len(pts) in (2,3)
        (forced if len(pts)==2 else flex)[c]=pts
    q={v:v for v in V}
    def root(v):
        while q[v]!=v:
            q[v]=q[q[v]];v=q[v]
        return v
    def join(a,b):
        a,b=root(a),root(b)
        if a!=b:q[b]=a
    for pts in forced.values():join(*pts)
    groups=defaultdict(set)
    for v in V:groups[root(v)].add(v)
    comp={v:root(v) for v in V}
    assert comp[AB]==AB
    assert len(groups)==(15,10,6)[m]
    assert all(c in flex for c in D)
    W=V-{AB}
    for rows,distinct,expected in ((RAINBOW[m],True,len(groups)-2),
                                    (PARITY_TREE[m],False,len(W)-1)):
        assert len(rows)==expected
        if distinct:assert len({c for c,u,v in rows})==len(rows)
        tree={x:x for x in ((set(groups)-{AB}) if distinct else W)}
        def tr(x):
            while tree[x]!=x:
                tree[x]=tree[tree[x]];x=tree[x]
            return x
        for c,u,v in rows:
            assert c in flex and c not in D
            assert set((u,v)).issubset(flex[c])
            x,y=(comp[u],comp[v]) if distinct else (u,v)
            assert x in tree and y in tree and tr(x)!=tr(y)
            tree[tr(x)]=tr(y)
        assert len({tr(x) for x in tree})==1
    return M,V,forced,flex,W

def xor_parity(edges):
    out=set()
    for a,b in edges:
        for v in (a,b):
            if v in out:out.remove(v)
            else:out.add(v)
    return out

def local_edges(pts,n,target,designated=None):
    """Realize a triangle boundary, preserving a designated side's endpoint link."""
    target=frozenset(target)
    assert len(pts)==3 and n in (2,3)
    sides=tuple(combinations(pts,2))
    assert not target or (len(target)==2 and target in map(frozenset,sides))
    if designated is None:designated=sides[0]
    u,v=designated;w=next(x for x in pts if x not in designated)
    if n==2:
        if not target:return [designated,designated]
        if target==frozenset((u,v)):return [(u,w),(v,w)]
        if target==frozenset((u,w)):return [(u,v),(v,w)]
        return [(u,v),(u,w)]
    if not target:return [(u,v),(u,w),(v,w)]
    return [tuple(sorted(target)),designated,designated]

def construct(m,triples,prepared=None):
    M,V,forced,flex,W=prepared if prepared is not None else setup(m)
    triples=set(triples)
    assert len(triples)==6 and triples.isdisjoint(D)
    n={c:(1 if c in D else 3 if c in triples else 2) for c in COLORS}
    by_color={c:[] for c in COLORS}
    for idx,c in enumerate(D):
        pts=flex[c]
        if idx<2:
            v=next(v for v in pts if v!=AB)
            by_color[c]=[(AB,v)]
        else:
            by_color[c]=[tuple(v for v in pts if v!=AB)]
    for c,(u,v) in forced.items():by_color[c]=[(u,v)]*n[c]
    base=[e for c in COLORS if c in D or c in forced for e in by_color[c]]
    need=xor_parity(base)
    assert AB not in need and len(need)%2==0
    adj=defaultdict(list)
    for c,u,v in PARITY_TREE[m]:
        adj[u].append((v,c));adj[v].append((u,c))
    root=next(iter(W));parent={root:None};parcolor={};order=[root]
    for u in order:
        for v,c in adj[u]:
            if v not in parent:
                parent[v]=u;parcolor[v]=c;order.append(v)
    assert len(order)==len(W)
    requests={c:set() for c in flex if c not in D}
    for v in reversed(order[1:]):
        if v in need:
            u=parent[v];c=parcolor[v]
            requests[c].symmetric_difference_update((u,v))
            need.symmetric_difference_update((u,v))
    assert not need
    chosen={c:tuple(sorted((u,v))) for c,u,v in RAINBOW[m]}
    for c,pts in flex.items():
        if c not in D:
            by_color[c]=local_edges(pts,n[c],requests[c],chosen.get(c))
    assert all(len(by_color[c])==n[c] for c in COLORS)
    all_edges=[e for c in COLORS for e in by_color[c]]
    assert len(all_edges)==42
    deg=defaultdict(int);adj=defaultdict(set)
    for u,v in all_edges:
        assert u!=v and u in V and v in V
        deg[u]+=1;deg[v]+=1;adj[u].add(v);adj[v].add(u)
    assert all(deg[v]>0 and deg[v]%2==0 for v in V)
    q=[AB];seen={AB}
    for u in q:
        for v in adj[u]:
            if v not in seen:seen.add(v);q.append(v)
    assert seen==V
    return by_color

def run():
    out={"schema":"R762JU_EXACT_CONSTRUCTIVE_CHECK_V1",
         "pencil_colors":["".join(map(str,c)) for c in D],
         "model":"composite Port-Euler; no native P000 lift","cases":[]}
    for m in range(3):
        prepared=setup(m)
        M,V,forced,flex,W=prepared
        choices=tuple(c for c in COLORS if c not in D)
        count=0
        for triple in combinations(choices,6):
            construct(m,triple,prepared);count+=1
        assert count==8008
        out["cases"].append({
            "inactive_ports":m,"representative_missing_ports":["".join(map(str,x)) for x in M],
            "port_count":len(V),"forced_components":(15,10,6)[m],
            "rainbow_edges":len(RAINBOW[m]),"parity_tree_edges":len(PARITY_TREE[m]),
            "inventories_exactly_checked":count,"status":"PASS"})
    out["total_exact_42_event_realizations_checked"]=sum(r["inventories_exactly_checked"] for r in out["cases"])
    print(json.dumps(out,indent=2,ensure_ascii=False))
if __name__=="__main__":run()
