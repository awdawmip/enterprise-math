#!/usr/bin/env python3
"""R762JZ: exact exhaustive all-active (M=empty) 42-event construction.
Use --start N --end N to run reproducible chunks of 43 singleton orbits.
Only Python 3.10+ standard library; integer/GF(2) calculations throughout.
"""
import argparse, itertools as it, json, hashlib
A=range(6)
P=list(it.combinations(A,2)); S=list(it.combinations(A,3))
pidx={p:i for i,p in enumerate(P)}; sidx={s:i for i,s in enumerate(S)}
tri=[tuple(pidx[p] for p in it.combinations(s,2)) for s in S]
side=[list(it.combinations(v,2)) for v in tri]

def comps(edges,n=15):
    par=list(range(n))
    def root(x):
        while par[x]!=x:
            par[x]=par[par[x]];x=par[x]
        return x
    for a,b in edges:
        a,b=root(a),root(b)
        if a!=b:par[a]=b
    roots=[root(i) for i in range(n)]
    keys={r:i for i,r in enumerate(sorted(set(roots)))}
    return [keys[x] for x in roots]

def xor(edges,lab=None):
    if lab is None:lab=list(range(15))
    v=0
    for a,b in edges:v^=(1<<lab[a])^(1<<lab[b])
    return v

def singles(D):
    rem=set(range(20))-set(D)
    groups=comps(e for k in rem for e in side[k]); n=max(groups)+1
    ans=[]
    for choice in it.product(*(side[k] for k in D)):
        root=comps(((groups[a],groups[b]) for a,b in choice),n)
        if len(set(root))==1:ans.append(choice)
    return ans

def build(D,T,sc):
    td=set(T); dd=set(D); doubles=sorted(set(range(20))-td-dd)
    q=comps(e for k in T for e in side[k]);
    reachable={0:()}
    for k in doubles:
        nxt={}
        for mask,seq in reachable.items():
            for i,e in enumerate(side[k]):
                value=mask^xor((e,),q)
                if value not in nxt:nxt[value]=seq+(i,)
        reachable=nxt
    for choice in sc:
        miss=reachable.get(xor(choice,q))
        if miss is None:continue
        edges={k:[] for k in range(20)}
        for k,e in zip(D,choice):edges[k]=[e]
        for k,i in zip(doubles,miss):edges[k]=[e for j,e in enumerate(side[k]) if j!=i]
        for k in T:edges[k]=side[k][:]
        residual=xor(e for v in edges.values() for e in v)
        # Reduce the residual into boundaries of the triple-color side generators.
        generators=[(k,e) for k in T for e in side[k]]
        pivots={}
        for j,(_,e) in enumerate(generators):
            v=xor((e,));rep=1<<j
            for bit in sorted(pivots,reverse=True):
                if v>>bit&1:
                    w,r=pivots[bit];v^=w;rep^=r
            if v:pivots[v.bit_length()-1]=(v,rep)
        exp=0;v=residual
        for bit in sorted(pivots,reverse=True):
            if v>>bit&1:
                w,r=pivots[bit];v^=w;exp^=r
        assert v==0
        per={k:0 for k in T}
        for j,(k,e) in enumerate(generators):
            if exp>>j&1:per[k]^=xor((e,))
        for k in T:
            if per[k]==0:continue
            match=[e for e in side[k] if xor((e,))==per[k]]
            assert len(match)==1
            spare=next(e for e in side[k] if e!=match[0])
            edges[k]=[match[0],spare,spare]
        check(D,T,edges)
        return edges
    raise AssertionError(('no construction',D,T))

def check(D,T,edges):
    # Independent event/property checker, rather than trusting the parity builder.
    deg=[0]*15; adj=[set() for _ in P]; total=0
    for k, s in enumerate(S):
        allowed={tuple(sorted(e)) for e in it.combinations((pidx[p] for p in it.combinations(s,2)),2)}
        require=1 if k in D else (3 if k in T else 2)
        assert len(edges[k])==require
        for a,b in edges[k]:
            assert a!=b and tuple(sorted((a,b))) in allowed
            deg[a]+=1;deg[b]+=1;adj[a].add(b);adj[b].add(a);total+=1
    assert total==42 and all(v>0 and v%2==0 for v in deg)
    seen={0}; stack=[0]
    while stack:
        for v in adj[stack.pop()]:
            if v not in seen:seen.add(v);stack.append(v)
    assert len(seen)==15

def orbits():
    maps=[tuple(sidx[tuple(sorted(p[i] for i in s))] for s in S)
          for p in it.permutations(A)]
    unseen=set(it.combinations(range(20),5)); out=[]
    while unseen:
        d=min(unseen)
        orb={tuple(sorted(m[i] for i in d)) for m in maps}
        assert orb<=unseen
        out.append((d,len(orb)));unseen-=orb
    assert len(out)==43 and sum(n for d,n in out)==15504
    return out

def run(start,end):
    classes=orbits();assert 0<=start<=end<=43
    report=[]; digest=hashlib.sha256()
    for i in range(start,end):
        D,n=classes[i]; choices=singles(D); successful=0
        for T in it.combinations(tuple(j for j in range(20) if j not in D),7):
            E=build(D,T,choices)
            raw=json.dumps([D,T,[E[k] for k in range(20)]],separators=(',',':')).encode()
            digest.update(len(raw).to_bytes(4,'big')+raw);successful+=1
        assert successful==6435
        report.append({'orbit':i,'D':D,'orbit_size':n,'T_passed':successful,'single_connect_choices':len(choices)})
    obj={'schema':'R762JZ_M0_REPRO_V1','start':start,'end':end,'orbits':report,
         'checked':sum(r['T_passed'] for r in report),
         'labeled_42_targets':sum(r['orbit_size']*r['T_passed'] for r in report),
         'framed_witness_sha256':digest.hexdigest()}
    with open(f'R762JZ_REPRO_{start}_{end}.json','w') as f:json.dump(obj,f,indent=2)
    print(json.dumps({k:v for k,v in obj.items() if k!='orbits'},sort_keys=True))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--start',type=int,default=0);p.add_argument('--end',type=int,default=43);a=p.parse_args();run(a.start,a.end)
