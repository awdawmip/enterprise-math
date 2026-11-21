"""Exact finite three-copy common/independent one-probe class size. Standard library."""
import argparse, json
from packing import no_ten
from collections import Counter
from itertools import combinations, product
from pathlib import Path
P=list(product(range(5), repeat=3))
NUM=125
BUCKETS=[(12,20),(14,17),(0,9),(13,21),(15,18),(5,16),(23,24),(2,10),(3,11),(8,19),(4,21),(6,7),(1,22)]

INDEPENDENT16=[12, 3, 3, 3, 4, 2, 6, 8, 15, 10, 7, 1, 7, 7, 3, 0, 0, 0, 1, 1, 9, 1, 11, 13, 5, 1, 13, 8, 15, 4, 2, 7, 9, 12, 0, 13, 6, 13, 12, 13, 14, 13, 10, 12, 14, 3, 10, 11, 12, 5, 1, 11, 6, 10, 5, 3, 4, 9, 15, 0, 4, 8, 4, 4, 7, 6, 11, 14, 6, 6, 2, 4, 6, 13, 8, 2, 7, 9, 14, 12, 1, 6, 8, 14, 0, 2, 14, 9, 15, 10, 2, 7, 9, 15, 4, 3, 14, 11, 13, 5, 1, 12, 12, 10, 0, 3, 7, 5, 13, 11, 11, 6, 5, 11, 0, 8, 5, 14, 8, 4, 2, 9, 15, 9, 0]

INDEPENDENT14=[11, 3, 1, 9, 9, 6, 6, 13, 0, 6, 8, 3, 8, 8, 2, 12, 5, 10, 0, 2, 4, 9, 9, 0, 2, 11, 7, 6, 0, 2, 1, 4, 3, 3, 1, 9, 4, 6, 1, 8, 12, 7, 10, 1, 5, 13, 13, 6, 1, 13, 11, 4, 1, 12, 2, 9, 12, 12, 7, 12, 0, 0, 0, 12, 8, 9, 4, 10, 6, 5, 7, 3, 7, 12, 7, 5, 8, 1, 5, 2, 3, 8, 5, 11, 3, 9, 7, 5, 11, 0, 12, 8, 10, 6, 11, 4, 8, 5, 13, 11, 11, 1, 13, 0, 10, 2, 2, 2, 2, 10, 9, 7, 13, 10, 8, 12, 3, 13, 6, 5, 10, 10, 4, 4, 4]

INDEPENDENT13=[3, 10, 12, 2, 5, 2, 2, 2, 9, 4, 3, 1, 0, 0, 0, 3, 6, 11, 2, 7, 8, 8, 8, 2, 8, 12, 12, 11, 8, 12, 3, 5, 11, 9, 4, 0, 5, 11, 10, 2, 5, 6, 5, 5, 7, 1, 5, 1, 1, 1, 4, 4, 12, 4, 5, 3, 9, 9, 8, 9, 0, 1, 4, 8, 2, 10, 6, 4, 8, 7, 11, 11, 4, 11, 11, 7, 1, 12, 8, 5, 7, 1, 10, 9, 4, 0, 7, 7, 7, 2, 6, 1, 11, 6, 6, 7, 3, 3, 3, 3, 9, 0, 6, 8, 5, 3, 0, 6, 12, 4, 9, 1, 6, 12, 2, 9, 0, 11, 12, 7, 9, 0, 6, 12, 10]

def independent13(t):
    x,y,z=t;return INDEPENDENT13[25*x+5*y+z]

def independent14(t):
    x,y,z=t;return INDEPENDENT14[25*x+5*y+z]

def independent16(t):
    x,y,z=t;return INDEPENDENT16[25*x+5*y+z]

COMMON12=[9, 5, 9, 3, 1, 4, 4, 2, 10, 10, 2, 1, 11, 9, 7, 4, 4, 8, 10, 10, 0, 6, 2, 3, 7, 9, 2, 6, 1, 6, 3, 3, 5, 5, 6, 11, 1, 4, 3, 7, 3, 3, 8, 9, 2, 0, 1, 5, 5, 7, 1, 2, 0, 3, 0, 7, 7, 0, 9, 0, 5, 0, 4, 0, 5, 11, 0, 8, 0, 2, 10, 10, 4, 3, 6, 8, 8, 7, 7, 11, 1, 11, 1, 8, 8, 8, 8, 3, 11, 3, 2, 5, 7, 7, 9, 0, 6, 4, 8, 8, 2, 5, 10, 4, 4, 7, 7, 1, 2, 9, 6, 9, 3, 6, 3, 6, 5, 8, 6, 1, 0, 10, 9, 2, 11]

def common12(t):
    x,y,z=t;return COMMON12[25*x+5*y+z]

def common13(t):
    x,y,z=t;q=5*((y-x)%5)+(z-2*x)%5
    return next(i for i,s in enumerate(BUCKETS) if q in s)

def common_triples():
    edges=set()
    for d in (1,3):
        for p in P:
            by={}
            for i,t in enumerate(P):
                active=tuple(k for k in range(3) if (t[k]-p[k])%5 in (0,d))
                side=tuple(t[k] for k in active)
                by.setdefault(active,[]).append((i,side))
            for group in by.values():
                for (a,u),(b,v),(c,w) in combinations(group,3):
                    if u!=v and u!=w and v!=w:edges.add((a,b,c))
    return sorted(edges)

def independent_triples():
    # Any three distinguished binary answers contain an L in some two axes;
    # a remaining coordinate can be made to give a common receipt for any triple.
    cols=list(combinations(range(3),2));edges=[]
    for a,b,c in combinations(range(125),3):
        tr=P[a],P[b],P[c]
        for i,j in cols:
            if len({t[i] for t in tr})==len({t[j] for t in tr})==2 and len({(t[i],t[j]) for t in tr})==3:
                edges.append((a,b,c));break
    return edges

def solve(edges):
    bad=[[0]*NUM for _ in P]
    for a,b,c in edges:
        bad[a][b]|=1<<c;bad[b][a]|=1<<c
        bad[a][c]|=1<<b;bad[c][a]|=1<<b
        bad[b][c]|=1<<a;bad[c][b]|=1<<a
    # Translation symmetry guarantees that a maximum set contains vertex 0.
    # Combinations with two selected members forbid the third.
    # Initial rank candidates can be loose; coloring for pairs accelerates.
    best=1; witness=1;nodes=0
    def dfs(ch,can,forb,size):
        nonlocal best,witness,nodes
        if size+can.bit_count()<=best:return
        nodes+=1
        order=[];remaining=can;level=0
        while remaining:
            level+=1;cl=remaining
            while cl:
                low=cl&-cl;v=low.bit_length()-1;order.append((v,level))
                remaining^=low;cl&=remaining&forb[v]
        for v,lev in reversed(order):
            if size+lev<=best:return
            vert=1<<v;can^=vert;d=can&~forb[v]
            if size+1>best:best=size+1;witness=ch|vert
            if size+1+d.bit_count()<=best:continue
            nc={};r=d
            while r:
                rbit=r&-r;w=rbit.bit_length()-1;r^=rbit
                nc[w]=forb[w]|bad[v][w]
            dfs(ch|vert,d,nc,size+1)
    dfs(1,((1<<NUM)-1)^1,bad[0],1)
    W=[v for v in range(NUM) if witness>>v&1]
    assert len(W)==best and all(not (witness>>a & witness>>b & witness>>c & 1) for a,b,c in edges)
    return {'max_class':best,'witness':[P[v] for v in W], 'search_nodes':nodes, 'confusing_triples':len(edges),'messages_at_least':(NUM+best-1)//best}

def verify_code(mapping,steps):
    counts=Counter()
    for dt in steps:
        for p in P:
            classes={}
            for t in P:
                active=tuple(k for k in range(3) if (t[k]-p[k])%5 in (0,dt[k]))
                output=tuple(t[k] for k in active)
                classes.setdefault((mapping(t),active),[]).append(output)
            for (_,active),out in classes.items():
                distinct=set(out)
                assert len(distinct)<=2
                if len(distinct)==2:
                    u,v=distinct;i=next(i for i,(a,b) in enumerate(zip(u,v)) if a!=b)
                    assert {u[i],v[i]}=={p[active[i]],(p[active[i]]+dt[active[i]])%5}
                counts[len(distinct)-1]+=len(out)
    return {'joint_probe_counts':sorted(counts.items()),'cases':sum(counts.values()),'messages':len({mapping(t) for t in P})}

def run():
    e=common_triples();a=solve(e);pack=no_ten(e);b=solve(independent_triples());enc=verify_code(common13,[(1,1,1),(3,3,3)]);enc['modulo_quotient_buckets']=BUCKETS;com12=verify_code(common12,[(1,1,1),(3,3,3)]);com12['table_xyz']=COMMON12;assert com12['messages']==12;ind=verify_code(independent16,product((1,3),repeat=3));ind['table_xyz']=INDEPENDENT16;small=verify_code(independent14,product((1,3),repeat=3));assert small['messages']==14;small['table_xyz']=INDEPENDENT14;best=verify_code(independent13,product((1,3),repeat=3));assert best['messages']==13;best['table_xyz']=INDEPENDENT13
    assert a['max_class']==13 and b['max_class']==10 and enc['cases']==31250 and enc['messages']==13 and ind['cases']==125000 and ind['messages']==16
    return {'scope':'three old five-cycle histories; one shared supplemental vertex query; finite choice among physically observed receipts; no kernel cost attributed to this checker','common':a,'common_partition_lower_bound':pack,'independent':b,'common_attainment':enc,'common_smaller_attainment':com12,'independent_attainment':ind,'independent_smaller_attainment':small,'independent_exact_attainment':best,'common_and_independent_bits_for_budget_0_1_2_3':[7,4,2,0]}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path);opts=ap.parse_args()
    s=json.dumps(run(),indent=2,ensure_ascii=False)+'\n'
    if opts.out:opts.out.write_text(s)
    else:print(s,end='')
