#!/usr/bin/env python3
"""EC49FAH: independent BFS per-depth color cover, signed LCP and witness audit."""
import collections,contextlib,io,itertools,json,runpy,sys
from pathlib import Path
P=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()): m=runpy.run_path(str(P/'VERIFY_EC49FAH_COMPACT.py'))
F=m['fam'];G=m['G'];mat=m['mat'];lookup=m['lookup'];rows=m['rows'];T2=m['T2'];T4=m['T4']

def cover_bfs(masks,full):
    q=collections.deque([0]);dist={0:0}
    while q:
        x=q.popleft()
        if x==full:return dist[x]
        for mask in masks:
            y=x|mask
            if y not in dist:dist[y]=dist[x]+1;q.append(y)
    raise AssertionError(('incomplete colors',full))

bfs_checks=0
for (hs,k),(q,L,pids) in G.items():
    D=collections.defaultdict(dict);off=0
    for h in hs:
        t=4 if k[0]+k[1]-h-1>=1 else 2
        for depth,mm in F[h,k,t].items():
            for pid,mask in mm.items(): D[depth][pid]=D[depth].get(pid,0)|(mask<<off)
        off+=t
    for d in range(1,L+1):
        assert cover_bfs(D[d].values(),(1<<off)-1)==q[d],(hs,k,d)
        bfs_checks+=1
assert bfs_checks==3964

prefixes={f:{d:set(mm) for d,mm in v.items()} for f,v in F.items()}
lcp_checked=0
for f,g in itertools.combinations(sorted(F),2):
    value=mat[lookup[f[0],f[1]]][5+lookup[g[0],g[1]]]
    p=prefixes[f];q=prefixes[g]
    assert value==0 or not p[value].isdisjoint(q[value]),(f,g,value)
    assert value+1 not in p or value+1 not in q or p[value+1].isdisjoint(q[value+1]),(f,g,value)
    lcp_checked+=1
assert lcp_checked==9316

wpath=Path(sys.argv[1]) if len(sys.argv)>1 else P.parent/'EC49FAB_H8_M5_FOUR_EXPLICIT_76_WITNESSES/EC49FAB_EXPLICIT_76_WITNESSES.json'
witnesses=json.loads(wpath.read_text())
index={' '.join(map(str,v)):gr for v,gr in rows};rechecked=[]
for w in witnesses:
    gr=index[w['schedule_row']];chosen=w['selected_paths']
    by_h=collections.defaultdict(list)
    for p in chosen:by_h[p['h']].append(p)
    for h in range(2,9):
        k=next(k for hs,k in gr if h in hs)
        t=4 if k[0]+k[1]-h-1>=1 else 2
        assert len(by_h[h])==t
        assert set(p['signature'] for p in by_h[h])==set(T4 if t==4 else T2)
    edge_total=0
    for d in range(1,max(x[1] for x in (G[g] for g in gr))+1):
        allp={tuple(x['signed_primitive_steps'][:d]) for x in chosen if len(x['signed_primitive_steps'])>=d}
        edge_total+=len(allp)
        for hs,k in gr:
            sub={tuple(x['signed_primitive_steps'][:d]) for x in chosen if x['h'] in hs and len(x['signed_primitive_steps'])>=d}
            assert len(sub)>=G[hs,k][0].get(d,0),(w['rank'],hs,k,d)
    assert edge_total==76,(w['rank'],edge_total)
    rechecked.append({'rank':w['rank'],'exact_native_prefix_edges':76,'all_observers':True,'local_cover_bound':True})
assert sorted(x['rank'] for x in rechecked)==[1512,1513,2200,2203]
report={'id':'EC49FAH_INDEPENDENT_AUDIT','status':'PASS','bfs_local_cover_checks':bfs_checks,'word_family_pair_lcp_checks':lcp_checked,'witnesses':rechecked}
(P/'EC49FAH_INDEPENDENT_AUDIT_COMPACT.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
