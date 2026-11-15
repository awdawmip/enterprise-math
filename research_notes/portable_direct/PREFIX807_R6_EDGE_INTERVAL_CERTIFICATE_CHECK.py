#!/usr/bin/env python3
"""PREFIX-807 exact integer regression; standalone Python 3 standard library."""
from itertools import product
from collections import defaultdict
from pathlib import Path
import json

def margin(x,a,b):
    return (tuple(sum(x[i*b+j] for j in range(b)) for i in range(a)),
            tuple(sum(x[i*b+j] for i in range(a)) for j in range(b)))

def endpoint(x,k,a,b,e,up,frozen=()):
    n=a+b; i,j=divmod(e,b); s=a+j if up else i; t=i if up else a+j
    limit=k[e]-x[e] if up else x[e]
    cap=[[0]*n for _ in range(n)]
    for h in range(a*b):
        if h==e or h in frozen: continue
        u,v=divmod(h,b); cap[u][a+v]+=k[h]-x[h]; cap[a+v][u]+=x[h]
    old=[z[:] for z in cap]; sent=0
    while sent<limit:
        parent=[-1]*n; parent[s]=s; queue=[s]
        for u in queue:
            if parent[t]>=0: break
            for v in range(n):
                if parent[v]<0 and cap[u][v]>0: parent[v]=u;queue.append(v)
        if parent[t]<0: break
        flow=limit-sent; v=t
        while v!=s: u=parent[v];flow=min(flow,cap[u][v]);v=u
        v=t
        while v!=s: u=parent[v];cap[u][v]-=flow;cap[v][u]+=flow;v=u
        sent+=flow
    y=list(x)
    for h in range(a*b):
        if h==e:continue
        u,v=divmod(h,b);y[h]+=old[u][a+v]-cap[u][a+v]
    y[e]+=sent if up else -sent
    return sent,tuple(y)

def check(group,k,a,b,stats,frozen=()):
    x=group[0];m=margin(x,a,b)
    for e in range(a*b):
        if e in frozen:continue
        lo=min(t[e] for t in group);hi=max(t[e] for t in group)
        assert {t[e] for t in group}==set(range(lo,hi+1))
        delta_plus,yplus=endpoint(x,k,a,b,e,True,frozen)
        delta_minus,yminus=endpoint(x,k,a,b,e,False,frozen)
        assert (x[e]-delta_minus,x[e]+delta_plus)==(lo,hi)
        assert yplus[e]==hi and yminus[e]==lo
        assert margin(yplus,a,b)==m and margin(yminus,a,b)==m
        assert all(0<=v<=c for y in (yplus,yminus) for v,c in zip(y,k))
        assert all(yplus[f]==yminus[f]==x[f] for f in frozen)
        stats['integer_assertions']+=5
        if frozen: stats['one_frozen_edge_certificates']+=1
        else:
            stats['edge_interval_certificates']+=1
            stats['nondegenerate_edge_intervals' if hi>lo else 'forced_edge_intervals']+=1

def main():
    s={'schema':'EM_PREFIX807_EDGE_INTERVAL_EXACT_CERTIFICATE_V1',
       'frozen_scientific_input_commit':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
       'integer_assertions':0,'edge_interval_certificates':0,
       'forced_edge_intervals':0,'nondegenerate_edge_intervals':0,
       'one_frozen_edge_certificates':0,'families':[]}
    for a,b,cmax in ((2,2,2),(2,3,2),(3,3,1),(2,3,1)):
        fibers=0;tables=0;patterns=0
        for k in product(range(cmax+1),repeat=a*b):
            patterns+=1;groups=defaultdict(list)
            for x in product(*(range(c+1) for c in k)):
                groups[margin(x,a,b)].append(x)
            for group in groups.values():
                fibers+=1;tables+=len(group);check(group,k,a,b,s)
                if (a,b,cmax) in ((2,2,2),(2,3,1)):
                    for f in range(a*b):
                        byval=defaultdict(list)
                        for x in group:byval[x[f]].append(x)
                        for sub in byval.values():check(sub,k,a,b,s,(f,))
        s['families'].append({'rows':a,'cols':b,'max_edge_capacity':cmax,
                              'capacity_patterns':patterns,'distinct_margin_fibers':fibers,
                              'full_named_table_occurrences':tables})
    cap=(2,2,2,2);target=((2,2),(2,2))
    tables=[x for x in product(range(3),repeat=4) if margin(x,2,2)==target]
    assert sorted(x[0] for x in tables)==[0,1,2]
    hist=defaultdict(int)
    for x in tables:hist[2*x[0]]+=1
    assert dict(sorted(hist.items()))=={0:1,2:1,4:1}
    s['observation_gap_witness']={
        'capacities':cap,'row_demands':target[0],'column_demands':target[1],
        'named_selected_edge':[0,0],'full_named_tables':len(tables),
        'edge_support':[0,1,2],'signed_integer_observer':'2*x_00',
        'observer_histogram':{str(k):v for k,v in sorted(hist.items())}}
    s['status']='ALL_EXACT_CHECKS_PASS'
    p=Path(__file__).with_name('PREFIX807_R6_EDGE_INTERVAL_CERTIFICATE_RESULTS.json')
    p.write_text(json.dumps(s,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print(json.dumps(s,indent=2,ensure_ascii=False))

if __name__=='__main__':main()
