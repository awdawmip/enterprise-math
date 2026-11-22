#!/usr/bin/env python3
"""R762JR: exact witness construction for all forty one-inactive-Port rainbow-tree exceptions.
This validates the analytic bridge/parity lemma; no solver or network dependency.
Use --full to check all 40*C(17,5)=247520 compressed support inventories.
"""
from itertools import combinations
import argparse, json, hashlib
AXES=range(6)
PORTS=list(combinations(AXES,2)); PID={p:i for i,p in enumerate(PORTS)}
SUPPORTS=list(combinations(AXES,3)); SID={s:i for i,s in enumerate(SUPPORTS)}
TRIS=[tuple(PID[x] for x in combinations(s,2)) for s in SUPPORTS]
EDGES=[tuple(combinations(t,2)) for t in TRIS]
M=PID[(0,1)]; ACTIVE=set(range(15))-{M}
BRIDGES=[SID[(0,1,c)] for c in range(2,6)]
CORE=[SID[s] for s in combinations(range(2,6),3)]

def wing(a): return [SID[tuple(sorted((a,c,d)))] for c,d in combinations(range(2,6),2)]

def edge(s,p,q):
    e=tuple(sorted((PID[tuple(sorted(p))],PID[tuple(sorted(q))])))
    assert e in EDGES[s],(s,e,EDGES[s]);return e

def tree(root):
    Q=lambda c:(root,c)
    C=lambda c,d:(c,d)
    out={}
    pairs=[((2,3),Q(2),Q(3)),((2,4),Q(2),Q(4)),((2,5),Q(2),Q(5)),
           ((3,4),Q(3),C(3,4)),((3,5),Q(3),C(3,5)),((4,5),Q(4),C(4,5))]
    for (c,d),a,b in pairs:
        s=SID[tuple(sorted((root,c,d)))];out[s]=edge(s,a,b)
    corepairs=[((2,3,4),C(2,3),C(2,4)),
               ((2,3,5),C(2,3),C(2,5)),
               ((2,4,5),C(2,4),C(4,5))]
    for tri,a,b in corepairs:
        s=SID[tri];out[s]=edge(s,a,b)
    assert len(out)==9
    return out

def build(D):
    D=set(D)
    isA=D.issubset(set(wing(0)))
    assert isA or D.issubset(set(wing(1)))
    leaf=0 if isA else 1; root=1-leaf
    R=tree(root)
    other=set(range(20))-set(D)-set(BRIDGES)
    assert len(other)==13
    NON=[s for s in other if s not in R]
    assert len(NON)==4 and set(NON)-set(wing(leaf))==set(CORE)-set(R)
    # For every non-tree flexible color, any local triangle boundary is realizable.
    GEN=[(s,e) for s,e in sorted(R.items())]+[(s,e) for s in sorted(NON) for e in EDGES[s]]
    adj={p:[] for p in ACTIVE}
    for g,(s,(u,v)) in enumerate(GEN):
        adj[u].append((v,g));adj[v].append((u,g))
    components=[];par={};order=[];seen=set()
    for v in sorted(ACTIVE):
        if v in seen:continue
        cc=[];seen.add(v);queue=[v];par[v]=None
        for x in queue:
            cc.append(x);order.append(x)
            for y,g in adj[x]:
                if y not in seen:
                    seen.add(y);par[y]=(x,g);queue.append(y)
        components.append(cc)
    # a 13-edge fixed connectivity backbone: 9 root/core tree edges and 4 compulsory bridge edges.
    par2={p:p for p in ACTIVE}
    def find(p):
        while par2[p]!=p:p=par2[p]
        return p
    for a,b in list(R.values())+[(PID[(0,c)],PID[(1,c)]) for c in range(2,6)]:
        aa,bb=find(a),find(b)
        assert aa!=bb
        par2[aa]=bb
    assert len({find(p) for p in ACTIVE})==1
    missing=[c for c in components if len(c)==1]
    if missing:
        assert len(components)==2 and len(missing)==1
        x=missing[0][0]
        assert x in {PID[tuple(sorted((leaf,c)))] for c in range(2,6)}
        isolated=x
        assert all(x in TRIS[s] for s in D)
    else:
        assert len(components)==1
        isolated=None
    return dict(D=D,R=R,GEN=GEN,NON=NON,components=components,par=par,order=order,isolated=isolated)

def construct(plan,extra):
    D=plan['D'];R=plan['R'];GEN=plan['GEN'];NON=plan['NON']
    extra=set(extra)
    assert len(extra)==5 and not(extra&D)
    counts=[1 if s in D else (3 if s in extra else 2) for s in range(20)]
    assert sum(counts)==42
    out=[[0]*3 for _ in range(20)]
    b=[0]*15
    def add(s,idx,count):
        out[s][idx]+=count
        u,v=EDGES[s][idx];b[u]^=count%2;b[v]^=count%2
    # Four compulsory bridge labels have exactly two active ports, so their edges are forced.
    for s in BRIDGES:
        k=next(k for k,(u,v) in enumerate(EDGES[s]) if u in ACTIVE and v in ACTIVE)
        add(s,k,counts[s])
    # For exceptional wing colors, singles may be oriented to repair the isolated leaf port.
    for s in sorted(D):
        k=next(k for k,(u,v) in enumerate(EDGES[s]) if plan['isolated'] not in (u,v)) if plan['isolated'] is not None else 0
        add(s,k,1)
    iso=plan['isolated']
    if iso is not None and b[iso]:
        s=min(D)
        k=next(k for k,(u,v) in enumerate(EDGES[s]) if iso in (u,v))
        old=out[s].index(1);out[s][old]=0
        u,v=EDGES[s][old];b[u]^=1;b[v]^=1
        add(s,k,1)
    # Forest path decomposition of b over tree-designated flexible edge generators and
    # all edges of the four remaining flexible color triangles.
    for cc in plan['components']:
        assert sum(b[v] for v in cc)%2==0
    selected=[0]*len(GEN)
    for v in reversed(plan['order']):
        t=plan['par'][v]
        if t is not None and b[v]:
            parent,g=t;selected[g]^=1;b[parent]^=1;b[v]^=1
    assert all(b[v]==0 for v in ACTIVE)
    target={s:[0]*15 for s in R.keys()|set(NON)}
    for (s,(u,v)),z in zip(GEN,selected):
        if z:target[s][u]^=1;target[s][v]^=1
    for s in sorted(target):
        c=counts[s];bit=target[s]
        assert c in (2,3)
        for x in range(15):
            if x not in TRIS[s]:assert bit[x]==0
        ones=[x for x in TRIS[s] if bit[x]]
        assert len(ones) in (0,2)
        if len(ones)==2:
            k=EDGES[s].index(tuple(sorted(ones)))
            if c==2:
                for idx in range(3):
                    if idx!=k:out[s][idx]=1
            else:out[s][k]=3
        else:
            if c==2:
                k=EDGES[s].index(R[s]) if s in R else 0
                out[s][k]=2
            else:out[s]=[1,1,1]
    # Independent integer certificate check.
    assert all(sum(row)==cnt for row,cnt in zip(out,counts))
    deg=[0]*15;adj=[set() for _ in range(15)]
    for s,row in enumerate(out):
        for (u,v),n in zip(EDGES[s],row):
            if n:
                deg[u]+=n;deg[v]+=n;adj[u].add(v);adj[v].add(u)
    assert deg[M]==0
    assert all(deg[v]>0 and deg[v]%2==0 for v in ACTIVE)
    seen={min(ACTIVE)};q=[min(ACTIVE)]
    for u in q:
        for v in adj[u]:
            if v not in seen:seen.add(v);q.append(v)
    assert seen==ACTIVE
    return bytes(x for row in out for x in row)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--full',action='store_true')
    args=parser.parse_args()
    summary={'star_isolated_patterns':0,'connected_flexible_patterns':0,'patterns':0,'certificates':0,'inventories_per_pattern':0}
    digest=hashlib.sha256()
    for leaf in (0,1):
        for D in combinations(wing(leaf),3):
            plan=build(D);summary['patterns']+=1
            if plan['isolated'] is not None:summary['star_isolated_patterns']+=1
            else:summary['connected_flexible_patterns']+=1
            rest=sorted(set(range(20))-set(D))
            if args.full:inventories=combinations(rest,5)
            else:
                # Exactly represent every possible parity of the four forced bridge supports.
                def samples():
                    for mask in range(16):
                        forced={BRIDGES[i] for i in range(4) if mask & (1<<i)}
                        other=[s for s in rest if s not in BRIDGES]
                        yield tuple(sorted(forced|set(other[:5-len(forced)])))
                inventories=samples()
            ct=0
            for extra in inventories:
                witness=construct(plan,extra)
                digest.update(bytes(D));digest.update(bytes(extra));digest.update(witness)
                ct+=1
            summary['inventories_per_pattern']=ct
            summary['certificates']+=ct
    assert summary['patterns']==40
    assert summary['star_isolated_patterns']==8
    assert summary['connected_flexible_patterns']==32
    assert summary['certificates']==(247520 if args.full else 640)
    summary.update(status='PASS',scope='one inactive Port, all 40 exceptional color patterns',full_inventory_enumeration=args.full,witness_stream_sha256=digest.hexdigest(),model='six-axis composite Port-Euler; P000 lift not claimed')
    print(json.dumps(summary,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
