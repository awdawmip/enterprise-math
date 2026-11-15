#!/usr/bin/env python3
"""EC49FPC: exact finite BRC equivalence and adaptive-depth verification.

Usage:
  python EC49FPC_VERIFY.py frozen_original_master.txt PROFILE.csv classes.json

The frozen input/profile CSV and full independent byte-Trie checks are included
in the separate SHA256-pinned evidence archive named in EC49FPC's paper.
This verifier uses exact integers throughout.
"""
import csv, hashlib, itertools, json, sys
from collections import defaultdict
from functools import lru_cache
from pathlib import Path

ROOTS=(3,5,6,7)
REPS=(14316,14320,16777,16781,16987,16989,17017,17027)
EXPECTED={
 14316:(864,24568,29,991,2,11),
 14320:(864,24568,29,991,2,20),
 16777:(432,12136,34,781,2,132),
 16781:(432,11840,40,562,3,0),
 16987:(432,11840,40,562,3,0),
 16989:(864,24568,36,668,3,2),
 17017:(432,12136,34,781,2,254),
 17027:(864,24568,36,668,3,2),
}
SOURCE_SHA256="cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"
PROFILE_SHA256="3f8d43c2234e80d9699157352bfe9f7f87166985310fd4fe66e1c78f851e252c"

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
    return (4,None)  # lower bound only when no three-deep tree found

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
        assert ids==memberships[E] and len(ids)==74
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
    assert tuple(totals)==(592,146224,383616,21608,6004)
    print("EC49FPC_EXACT_ALL_EIGHT_PASS",totals)

if __name__=="__main__":
    assert len(sys.argv)==4, "expected FROZEN_SOURCE PROFILE_CSV CLASS_MEMBERSHIPS_JSON"
    main(*(Path(p) for p in sys.argv[1:]))
