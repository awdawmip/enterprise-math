#!/usr/bin/env python3
"""PREFIX-814 exact finite regression: unpinning a named edge inserts its residual arcs.
Only integer arithmetic, exhaustive capacity/margin/source-table suites.
"""
from itertools import product
from collections import defaultdict
from math import gcd
import json

def adjacency(edges, cap, x, pinned, nverts):
    adj = [[] for _ in range(nverts)]
    for i,(u,v) in enumerate(edges):
        if i in pinned: continue
        if x[i]<cap[i]: adj[u].append(v)
        if x[i]>0: adj[v].append(u)
    return adj

def reach(adj):
    seen=[]
    for start in range(len(adj)):
        q=[start]; s={start}
        for u in q:
            for v in adj[u]:
                if v not in s: s.add(v); q.append(v)
        seen.append(s)
    return seen

def comps(adj):
    r=reach(adj); comp=[]; labels=[-1]*len(adj)
    for u in range(len(adj)):
        if labels[u]>=0:continue
        group=tuple(v for v in range(len(adj)) if v in r[u] and u in r[v]); idx=len(comp)
        for v in group:labels[v]=idx
        comp.append(group)
    return labels

def update_labels_insert(adj,u,v):
    """Single residual arc insertion via old condensation reachability."""
    before=comps(adj)
    if before[u]==before[v]:return before
    r=reach(adj)
    if u not in r[v]:return before
    groups=set(before[z] for z in r[v] if u in r[z])
    return [min(groups) if before[z] in groups else before[z] for z in range(len(adj))]

def equivalent(a,b):
    return all((a[i]==a[j])==(b[i]==b[j]) for i in range(len(a)) for j in range(len(a)))

def forest_gcd(edges,cap,x,pinned,nverts,w):
    adj=adjacency(edges,cap,x,pinned,nverts); lab=comps(adj)
    tree=[[] for _ in range(nverts)]
    par=list(range(nverts))
    def root(v):
        while par[v]!=v: par[v]=par[par[v]]; v=par[v]
        return v
    cycle=[]
    for i,(u,v) in enumerate(edges):
        if i in pinned or not cap[i] or lab[u]!=lab[v]:continue
        if root(u)!=root(v):
            par[root(u)]=root(v)
            tree[u].append((v,w[i]));tree[v].append((u,-w[i]))
        else:cycle.append((u,v,w[i]))
    p=[None]*nverts
    for start in range(nverts):
        if p[start] is not None:continue
        p[start]=0; q=[start]
        for u in q:
            for v,d in tree[u]:
                if p[v] is None:p[v]=p[u]+d;q.append(v)
    g=0
    for u,v,k in cycle:g=gcd(g,abs(k+p[u]-p[v]))
    return g

def tables_and_groups(edges, cap, nr, nc):
    groups=defaultdict(list)
    for x in product(*(range(k+1) for k in cap)):
        row=[0]*nr;col=[0]*nc
        for (u,v),val in zip(edges,x):row[u]+=val;col[v-nr]+=val
        groups[tuple(row+col)].append(x)
    return groups

def run():
    suites=[
      ('K22',2,2,[(i,2+j) for i in range(2) for j in range(2)],[range(3)]*4),
      ('K23',2,3,[(i,2+j) for i in range(2) for j in range(3)],[range(2)]*6),
      ('K33',3,3,[(i,3+j) for i in range(3) for j in range(3)],[range(2)]*9),
      ('PAR22',2,2,[(0,2),(0,2),(0,3),(1,2),(1,3)],[range(2)]*5),
      ('PAR3',1,1,[(0,1)]*3,[range(3)]*3),
    ]
    observers=lambda e:[tuple(i+1 for i in range(e)),tuple((-1)**i*(i*i+1) for i in range(e)),tuple(1 if i==0 else 0 for i in range(e))]
    overall=defaultdict(int);by_suite={}
    for name,nr,nc,edges,options in suites:
        c=defaultdict(int);n=nr+nc
        for cap in product(*options):
            c['configurations']+=1
            groups=tables_and_groups(edges,cap,nr,nc)
            for marg,tab in groups.items():
                c['margin_fibers']+=1;c['source_tables']+=len(tab)
                for x in tab:
                    for e in range(len(edges)):
                        if cap[e]==0:continue
                        c['unpin_cases']+=1
                        P={e}; current=adjacency(edges,cap,x,P,n); predicted=comps(current)
                        u,v=edges[e]
                        for a,b in ((u,v),(v,u)):
                            if (a==u and x[e]>=cap[e]) or (a==v and x[e]<=0):continue
                            updated=update_labels_insert(current,a,b)
                            current[a].append(b)
                            actual=comps(current)
                            assert equivalent(updated,actual),(name,cap,x,e,'SCC_INSERT')
                            predicted=updated
                            c['arc_insertion_checks']+=1
                        full=adjacency(edges,cap,x,set(),n)
                        assert equivalent(predicted,comps(full))
                        before=comps(adjacency(edges,cap,x,{e},n))
                        after=comps(full)
                        for i in range(n):
                            for j in range(n):
                                assert before[i]!=before[j] or after[i]==after[j]
                                c['partition_refinement_comparisons']+=1
                        for w in observers(len(edges)):
                            gfull=0;gpin=0
                            baseline=sum(q*v for q,v in zip(w,x))
                            for y in tab:
                                delta=sum(q*v for q,v in zip(w,y))-baseline
                                gfull=gcd(gfull,abs(delta))
                                if y[e]==x[e]:gpin=gcd(gpin,abs(delta))
                            algfull=forest_gcd(edges,cap,x,set(),n,w)
                            algpin=forest_gcd(edges,cap,x,{e},n,w)
                            assert (gfull,gpin)==(algfull,algpin),(name,cap,x,e,w,gfull,gpin,algfull,algpin)
                            assert gfull==0 and gpin==0 or gfull!=0 and gpin%gfull==0
                            c['observer_lattice_exact_checks']+=1
                        if not equivalent(before,after):c['scc_merge_cases']+=1
                        elif forest_gcd(edges,cap,x,{e},n,observers(len(edges))[0])!=forest_gcd(edges,cap,x,set(),n,observers(len(edges))[0]):
                            c['same_scc_lattice_changes']+=1
        by_suite[name]=dict(c)
        for k,v in c.items():overall[k]+=v
    ed=[(0,1)]*3;cap=(2,2,2);x=(1,1,1);w=(1,2,0)
    assert forest_gcd(ed,cap,x,{0},2,w)==2
    assert forest_gcd(ed,cap,x,set(),2,w)==1
    assert equivalent(comps(adjacency(ed,cap,x,{0},2)),comps(adjacency(ed,cap,x,set(),2)))
    ed=[(0,2),(0,3),(1,2),(1,3)];cap=(1,1,1,1);x=(1,0,0,1)
    assert len(set(comps(adjacency(ed,cap,x,{0},4))))==4
    assert len(set(comps(adjacency(ed,cap,x,set(),4))))==1
    ed=[(0,1)];cap=(2,);x=(1,)
    assert len(set(comps(adjacency(ed,cap,x,{0},2))))==2
    assert len(set(comps(adjacency(ed,cap,x,set(),2))))==1
    assert forest_gcd(ed,cap,x,set(),2,(1,))==0
    return {'schema':'PREFIX814_EXACT_UNPIN_REGRESSION_V1','integer_semantics':'Python arbitrary-precision integers; full exhaustive suites; no random samples','frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d','suites':by_suite,'totals':dict(overall),'witnesses':{'three_parallel_scc_unchanged_gcd_2_to_1':'PASS','two_by_two_scc_merge_four_to_one':'PASS','single_named_edge_reversal_no_new_table':'PASS'},'verdict':'ALL_EXACT_ASSERTIONS_PASSED'}

if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,sort_keys=True,indent=2))
