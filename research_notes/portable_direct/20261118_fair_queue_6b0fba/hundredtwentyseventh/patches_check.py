"""Verify all ambient embeddings of the finite collar catalogue and decode abstract samples."""
import argparse
import hashlib
from collections import Counter
from importlib.util import module_from_spec,spec_from_file_location
import json
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1]/"seventysixth"/"completion_check.py"
DIGEST = "82b672fa3179d66f5e0e4b337126485e45948da87e333035b9995a33c0533f9c"


def load(path):
    assert hashlib.sha256(path.read_bytes()).hexdigest()==DIGEST
    spec=spec_from_file_location("native_contact_core",path)
    core=module_from_spec(spec);spec.loader.exec_module(core)
    return core


class Template:
    def __init__(self,world,shape):
        self.S=tuple(sorted(shape))
        T=sorted(set().union(*(world(x) for x in shape))-set(shape))
        links={x:set(world(x))&set(T) for x in T}
        order=[max(T,key=lambda x:(len(links[x]),x))]
        while len(order)<len(T):
            used=set(order); y=max(set(T)-used,key=lambda x:(len(links[x]&used),len(links[x]),x))
            assert links[y]&used
            order.append(y)
        self.req=[[j for j in range(i) if order[j] in links[x]] for i,x in enumerate(order)]
        self.no=[[j for j in range(i) if order[j] not in links[x]] for i,x in enumerate(order)]
        self.deg=[len(links[x]) for x in order]
        self.ports=[[j for j,x in enumerate(order) if x in world(s)] for s in self.S]
        self.inner={(i,j) for i,x in enumerate(self.S) for j,y in enumerate(self.S) if y in world(x)}
        assert all(len(row)>4 for row in self.ports)

    def embeddings(self,neighbors,root,finite):
        if finite and len(neighbors(root))<self.deg[0]: return
        image=[root]
        def extend(i):
            if i==len(self.req):
                yield tuple(image);return
            pool=set.intersection(*(set(neighbors(image[j])) for j in self.req[i]))-set(image)
            for j in self.no[i]:
                pool-=neighbors(image[j])
            for y in pool:
                if finite and len(neighbors(y))<self.deg[i]: continue
                image.append(y);yield from extend(i+1);image.pop()
        yield from extend(1)

    def certify(self,world):
        count=0
        for phi in self.embeddings(world,(0,0,0),False):
            centers=[]
            for row in self.ports:
                matches=set.intersection(*(set(world(phi[j])) for j in row))-set(phi)
                assert len(matches)==1
                centers.append(matches.pop())
            assert len(set(centers))==len(self.S)
            assert all((y in world(x))==((i,j) in self.inner)
                       for i,x in enumerate(centers) for j,y in enumerate(centers))
            for x,row in zip(centers,self.ports):
                assert set(world(x))-set(centers)=={phi[j] for j in row}
            count+=1
        return count


def make_catalog(core,world):
    all_shapes=[list(sorted(core.connected_shapes(world,n))) for n in range(1,6)]
    dense=set()
    for a in all_shapes[-1]:
        old=set(a); e=core.edge_count(world,a)
        if e<7: continue
        for x in core.neighborhood(world,old)-old:
            if e+len(world(x)&old)>=12: dense.add(core.canonical(world,old|{x}))
    all_shapes.append(sorted(dense))
    menu=[]; report=[]
    for group in all_shapes:
        counts=[]
        for shape in group:
            motif=Template(world,shape)
            count=motif.certify(world)
            assert count>0
            counts.append(count); menu.append(motif)
        report.append(dict(templates=len(group),anchored_embeddings=sum(counts),counts=sorted(set(counts))))
    return menu,report


def abstract_decode(menu,adj,d):
    # Boundary labels here are plain integers. No native coordinates are used.
    candidates={}
    for motif in menu:
        if len(motif.deg)>len(adj):continue
        for root in adj:
            for phi in motif.embeddings(adj.__getitem__,root,True):
                sig=tuple(frozenset(phi[j] for j in row) for row in motif.ports)
                if any(set.intersection(*(set(adj[y]) for y in port)) for port in sig):
                    continue
                key=frozenset(sig)
                inner=frozenset(frozenset((sig[i],sig[j])) for i,j in motif.inner if i<j)
                if key in candidates: assert candidates[key]==inner
                candidates[key]=inner
    columns={key:Counter(y for port in key for y in port) for key in candidates}
    counts=dict(d); answer=set(); edges=set(); pivots=[]
    while columns:
        entries={y:[] for y in adj}
        for c,mask in columns.items():
            for y,k in mask.items(): entries[y].append((c,k))
        y=next(y for y in sorted(adj) if len(entries[y])==1 and entries[y][0][1]==1)
        c=entries[y][0][0]; v=counts[y];pivots.append([y,v])
        if v not in (0,1): return candidates,pivots,None
        mask=columns.pop(c)
        if v:
            for y,k in mask.items():counts[y]-=k
            answer.update(c);edges.update(candidates[c])
    if any(counts.values()): return candidates,pivots,None
    return candidates,pivots,(answer,edges)


def genuine_example(core,w,menu,S):
    omega=set(S)|core.neighborhood(w,S)
    r=1
    while not omega.issubset(core.ball(w,core.ORIGIN,r)):r+=1
    whole=core.ball(w,core.ORIGIN,r+2)
    C=set(whole)-omega
    def connected(A):
        a=next(iter(A));seen={a};stack=[a]
        for z in stack:
            for b in w(z)&A-seen:
                seen.add(b);stack.append(b)
        return seen==A
    assert connected(C) and connected(omega) and (core.neighborhood(w,omega)-omega)<=C
    F={x for x in omega if w(x)&C};assert omega-F==S
    # Deliberately renumber before the abstract algorithm.
    coord=sorted(F,key=lambda x:hashlib.sha256(str(x).encode()).digest())
    lab={x:i for i,x in enumerate(coord)}
    adj={lab[x]:{lab[y] for y in w(x)&F} for x in F}
    d={lab[x]:12-len(w(x)&C)-len(adj[lab[x]]) for x in F}
    assert min(d.values())>0
    candidates,pivots,out=abstract_decode(menu,adj,d)
    signature={x:frozenset(lab[y] for y in w(x)&F) for x in S}
    expected=(set(signature.values()),{frozenset((signature[x],signature[y])) for x in S for y in w(x)&S})
    assert out==expected
    return dict(centers=sorted(S),connected_occupied=len(C),frontier=len(F),deficit=sum(d.values()),
                candidate_blocks=len(candidates),integer_pivots=len(pivots),restored_centers=len(out[0]),
                restored_internal_edges=len(out[1]))


def run(core):
    report={}
    for name in ('fcc','hcp'):
        w=getattr(core,name);menu,proof=make_catalog(core,w)
        # Use the full small dictionary on a dense six-point cavity, and the
        # appropriate subdictionary on two larger mixed-component examples.
        dense=set(menu[-1].S)
        sample=genuine_example(core,w,menu,dense)
        step=(1,1,0) if name=='fcc' else (1,0,0)
        sites=lambda ns:{tuple(j*v for v in step) for j in ns}
        mixed=genuine_example(core,w,[x for x in menu if len(x.S)<=3],sites([-4,-3,-2,1,2,5]))
        spread=genuine_example(core,w,menu[:1],sites([-6,-3,0,3,6]))
        # Actual singleton occupation has a cofinite hidden set. Its visible
        # twelve-point shell is a genuine ambient collar of an occupied center.
        S=set(w(core.ORIGIN));q={a:i for i,a in enumerate(sorted(S))}
        adj={q[a]:{q[b] for b in w(a)&S} for a in S}
        d={q[a]:12-1-len(w(a)&S) for a in S}
        cs,pivots,out=abstract_decode(menu,adj,d)
        assert out is None and len(cs)==1 and pivots[0][1]==7
        report[name]=dict(catalog=proof,dense_six_shape=sorted(dense),native_cavities=[sample,mixed,spread],
                          singleton_occupation_rejected_pivot=pivots[0][1])
    return dict(native_contact_sha256=DIGEST,worlds=report)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--native',type=Path,default=SOURCE);args=p.parse_args()
    print(json.dumps(run(load(args.native)),indent=2))
