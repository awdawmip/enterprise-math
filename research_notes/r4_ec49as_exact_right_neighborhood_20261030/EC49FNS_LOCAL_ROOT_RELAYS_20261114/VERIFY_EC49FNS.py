#!/usr/bin/env python3
"""EC49FNS: exact first-neutral shortest detour census, no native optimizer rerun."""
import base64, collections, hashlib, itertools, json, lzma
from pathlib import Path

HERE=Path(__file__).resolve().parent
raw=lzma.decompress(base64.b64decode((HERE/'EDGE_VECTOR_EC49FNP.u8x11.xz.b64').read_text().strip(),validate=True))
assert len(raw)==11000 and hashlib.sha256(raw).hexdigest()=='4d6540181b8c25a324aa701f551602ed53156be46b70170f1c104230c6443e9b'
keys=[frozenset(raw[i*11:i*11+7]) for i in range(1000)]
sigs=[tuple(raw[i*11+7:i*11+10]) for i in range(1000)]
assert len(set(keys))==1000 and all(len(k)==7 for k in keys)
index={k:i for i,k in enumerate(keys)}
buckets=collections.defaultdict(set)
for i,k in enumerate(keys):
    for core in itertools.combinations(sorted(k),6):buckets[core].add(i)
adj=[set() for _ in keys];edges=set()
for bucket in buckets.values():
    for i,j in itertools.combinations(sorted(bucket),2):
        edges.add((i,j))
        if sigs[i]==sigs[j]:adj[i].add(j);adj[j].add(i)
assert len(edges)==27942 and sum(map(len,adj))==23148
pairs=[(32275,32703),(32276,32719),(32315,32353),(32318,32353),
       (32703,32951),(32703,32953),(32719,32961),(32719,32963)]
counts=[];first_edges=set();reports=[]
for A,B in pairs:
    a,b=A-32000,B-32000
    r=len(keys[a]-keys[b])
    assert r in (2,3) and sigs[a]==sigs[b]
    # Exhaustively exclude every monotone r-step Johnson geodesic.
    for deletes in itertools.permutations(sorted(keys[a]-keys[b])):
        for inserts in itertools.permutations(sorted(keys[b]-keys[a])):
            cur=keys[a]
            for remove,add in zip(deletes,inserts):
                cur=(cur-{remove})|{add}
                v=index.get(cur)
                if v is None or sigs[v]!=sigs[a]:break
            else:raise AssertionError('shortest stable Johnson geodesic unexpectedly exists')
    routes=[]
    def rec(path,zeros):
        u=path[-1]
        if len(path)==r+2:
            if u==b and zeros==1:routes.append(tuple(path))
            return
        for v in sorted(adj[u]):
            if v in path:continue
            d0=len(keys[u]-keys[b]);d1=len(keys[v]-keys[b])
            if d1>d0 or d1<d0-1:continue
            neutral=(d1==d0)
            if zeros+neutral>1:continue
            rec(path+[v],zeros+neutral)
    rec([a],0)
    assert routes
    for route in routes:
        changes=[len(keys[route[t]]-keys[b])-len(keys[route[t+1]]-keys[b])
                 for t in range(len(route)-1)]
        assert changes.count(0)==1 and changes.count(1)==r and changes.index(0)==0
        u,v=route[0],route[1]
        removed=next(iter(keys[u]-keys[v]));added=next(iter(keys[v]-keys[u]))
        assert removed not in keys[b] and added not in keys[b]
        first_edges.add((u+32000,v+32000))
    counts.append(len(routes))
    reports.append({'endpoints':[A,B],'johnson_distance':r,'stable_detours':len(routes),
                    'first_neutral':True,'example':[v+32000 for v in routes[0]],
                    'signature':sigs[a]})
assert counts==[1,2,39,39,1,1,2,2] and sum(counts)==87
assert len(first_edges)==84
(HERE/'FIRST_NEUTRAL_EDGES_EC49FNS.txt').write_text(
    ''.join(f'{a} {b}\n' for a,b in sorted(first_edges)))
print(json.dumps({'schema':'EC49FNS_NEUTRAL_RELAY_V1',
 'frozen_science_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
 'vector_sha256':hashlib.sha256(raw).hexdigest(),
 'defect_pairs':8,'shortest_detours':87,'distinct_first_neutral_edges':84,
 'all_first_neutral':True,'all_swap_non_target_for_non_target':True,
 'path_counts':reports,'mathematical_admission':'NOT_REVIEWED'},
 ensure_ascii=False,sort_keys=True,indent=2))
