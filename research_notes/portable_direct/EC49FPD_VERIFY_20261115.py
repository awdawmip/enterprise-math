#!/usr/bin/env python3
"""EC49FPD: exact finite BRC equivalence and adaptive-depth verification.

Usage:
  python EC49FPD_VERIFY.py frozen_original_master.txt PROFILE.csv classes.json

The frozen input/profile CSV and full independent byte-Trie checks are included
in the separate SHA256-pinned evidence archive named in EC49FPD's paper.
This verifier uses exact integers throughout.
"""
import csv, hashlib, itertools, json, sys
from collections import defaultdict
from functools import lru_cache
from pathlib import Path

ROOTS=(3,5,6,7)
REPS=(16860,16864,16988,17022)
EXPECTED={
 16860:(1296,26180,31,1036,4,1018),
 16864:(1296,25872,39,704,3,2),
 16988:(1296,25872,39,704,3,2),
 17022:(1296,26180,31,1036,4,1020),
}
SOURCE_SHA256="cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"
PROFILE_SHA256="2e07ad0d935efd9824729feec6349c2af162e152cd9c8a2a93848fd4343eea93"

def source(path):
    assert hashlib.sha256(path.read_bytes()).hexdigest()==SOURCE_SHA256
    with path.open() as fh:
        nk,nw,nc=map(int,fh.readline().split())
        assert (nk,nw,nc)==(94,178850,38169)
        masks=[]
        for _ in range(nk):
            q=[0]*4
            for _ in range(int(fh.readline())):
                label,word=fh.readline().split()
                q[ROOTS.index(int(word[:2],16))] |= 1<<int(label)
            masks.append(tuple(q))
        cases=[tuple(map(int,fh.readline().split())) for _ in range(nc)]
    return masks,cases

def domain(case,masks):
    E=[0]*24
    for key in case:
        for j,m in enumerate(masks[key]):
            while m:
                b=m&-m
                E[b.bit_length()-1] |= 1<<j
                m^=b
    assert all(E)
    return tuple(E)

def families(costs,actions):
    # All distinct root profiles and their exact full-terminal cost vectors.
    roots=defaultdict(list); terminal=defaultdict(list); witnesses=[]
    for config,rootvec,t in costs:
        roots[rootvec].append(config)
        terminal[t].append(config)
        witnesses.append((rootvec,t))
    rp=sum(len(x)*(len(x)-1)//2 for x in roots.values())
    tp=sum(len(x)*(len(x)-1)//2 for x in terminal.values())
    assert tp>=rp
    return roots,terminal,rp,tp,witnesses

def adaptive_depth(vals):
    # Profile ids have fixed order, all complete allocations are candidate queries.
    n=len(vals); nq=len(vals[0]); full=(1<<n)-1
    pair_index={(i,j):1<<k for k,(i,j) in enumerate(itertools.combinations(range(n),2))}
    collision=[]
    for q in range(nq):
        c=0
        for (i,j),bit in pair_index.items():
            if vals[i][q]==vals[j][q]:c|=bit
        collision.append(c)
    def fibers(mask,q):
        out=defaultdict(int)
        while mask:
            b=mask&-mask; i=b.bit_length()-1; mask^=b
            out[vals[i][q]]|=b
        return tuple(out.values())
    @lru_cache(None)
    def one(mask):
        if mask.bit_count()<=1:return 0
        ids=[i for i in range(n) if (mask>>i)&1]
        pairs=0
        for i,j in itertools.combinations(ids,2):pairs|=pair_index[i,j]
        for q,c in enumerate(collision):
            if not c&pairs:return q
        return None
    @lru_cache(None)
    def two(mask):
        s=one(mask)
        if s is not None:return s
        for q in range(nq):
            if all(one(f) is not None for f in fibers(mask,q)):
                return q
        return None
    assert one(full) is None
    q=two(full)
    if q is not None:
        for f in fibers(full,q):
            z=one(f)
            assert z is not None
            assert all(t.bit_count()==1 for t in fibers(f,z))
        return (2,q)
    for q in range(nq):
        nexts=[two(f) for f in fibers(full,q)]
        if all(z is not None for z in nexts):
            for f,z in zip(fibers(full,q),nexts):
                for ff in fibers(f,z):
                    zz=one(ff)
                    assert zz is not None
                    assert all(t.bit_count()==1 for t in fibers(ff,zz))
            return (3,q)
    # Every 1/2/3-deep decision tree has now been excluded. Construct
    # and validate a depth-four tree by exact minimax partition recursion.
    all_partitions={}
    for q in range(nq):
        p=tuple(sorted(fibers(full,q)))
        if p not in all_partitions:all_partitions[p]=q
    actions=sorted(((q,p) for p,q in all_partitions.items()),
        key=lambda t:(max(z.bit_count() for z in t[1]),-len(t[1]),t[0]))
    @lru_cache(None)
    def construct(mask,d):
        if mask.bit_count()<=1:return {"leaf":(mask&-mask).bit_length()-1}
        if d==0:return None
        for q,p in actions:
            ff=[z for t in p if (z:=t&mask)]
            if len(ff)<=1:continue
            children=[]
            for z in ff:
                child=construct(z,d-1)
                if child is None:break
                children.append(child)
            if len(children)==len(ff):
                return {"query":q,"branches":{
                    str(vals[(z&-z).bit_length()-1][q]):child
                    for z,child in zip(ff,children)}}
        return None
    assert construct(full,3) is None
    tree=construct(full,4)
    assert tree is not None
    def walk(profile):
        node=tree;steps=0
        while "leaf" not in node:
            q=node["query"];steps+=1
            node=node["branches"][str(vals[profile][q])]
            assert steps<=4
        return node["leaf"],steps
    assert all(walk(i)[0]==i for i in range(n))
    assert max(walk(i)[1] for i in range(n))==4
    return 4,tree["query"]

def main(src,profile,manifest):
    masks,cases=source(src)
    memberships=defaultdict(list)
    for i,case in enumerate(cases):
        memberships[domain(case,masks)].append(i)
    assert len(memberships)==625
    selected={int(k):v for k,v in json.loads(manifest.read_text()).items()}
    assert tuple(selected)==REPS
    assert hashlib.sha256(profile.read_bytes()).hexdigest()==PROFILE_SHA256
    rows=defaultdict(dict)
    with profile.open() as f:
        for row in csv.DictReader(f):
            k,r,m,o,s,c=(int(row[x]) for x in
                         ("config","root","must","opt","subset","cost"))
            assert (r,s) not in rows[k]
            rows[k][r,s]=(m,o,c)
    assert set(rows)==set(i for v in selected.values() for i in v)
    totals=[0,0,0,0,0]
    for rep in REPS:
        ids=selected[rep]; E=domain(cases[rep],masks)
        assert ids==memberships[E] and len(ids)==77
        opt=[l for l,e in enumerate(E) if e.bit_count()>1]
        actions=list(itertools.product(
            *(tuple(ROOTS[j] for j in range(4) if (E[l]>>j)&1) for l in opt)))
        sub={}
        for j,r in enumerate(ROOTS):
            opts=[l for l in opt if E[l]&(1<<j)]
            sub[r]=[sum(1<<l for l,b in zip(opts,x) if b)
                    for x in itertools.product((0,1),repeat=len(opts))]
        nroot=sum(map(len,sub.values()))
        data=[]
        for id in ids:
            p=tuple(rows[id][r,s][2] for r in ROOTS for s in sub[r])
            assert len(rows[id])==nroot
            for j,r in enumerate(ROOTS):
                need=sum(1<<l for l,e in enumerate(E) if e==(1<<j))
                possible=sum(1<<l for l in opt if E[l]&(1<<j))
                assert all(rows[id][r,s][:2]==(need,possible) for s in sub[r])
            t=[]
            for a in actions:
                choice={r:0 for r in ROOTS}
                for l,r in zip(opt,a):choice[r]|=1<<l
                t.append(sum(rows[id][r,choice[r]][2] for r in ROOTS))
            data.append((id,p,tuple(t)))
        roots,term,rp,tp,_=families(data,actions)
        assert rp==tp
        unique={p:ts[0] for p,ts in roots.items()}
        by_id={id:t for id,p,t in data}
        vals=[by_id[k] for k in unique.values()]
        assert len({tuple(v) for v in vals})==len(vals)
        depth,first=adaptive_depth(vals)
        exp=EXPECTED[rep]
        assert (len(actions),len(ids)*nroot,len(roots),rp,depth,first)==exp, (rep,depth,first,exp)
        totals[0]+=len(ids); totals[1]+=len(ids)*nroot
        totals[2]+=len(ids)*len(actions); totals[3]+=len(ids)*(len(ids)-1)//2
        totals[4]+=rp
        print("PASS",rep,"profiles",len(roots),"adaptive_depth",depth,"first_query",first)
    assert tuple(totals)==(308,104104,399168,11704,3480)
    print("EC49FPD_EXACT_ALL_FOUR_PASS",totals)

if __name__=="__main__":
    assert len(sys.argv)==4, "expected FROZEN_SOURCE PROFILE_CSV CLASS_MEMBERSHIPS_JSON"
    main(*(Path(p) for p in sys.argv[1:]))
