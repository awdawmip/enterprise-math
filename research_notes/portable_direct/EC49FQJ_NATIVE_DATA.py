#!/usr/bin/env python3
"""Frozen-source reconstruction for EC49FQJ. Python stdlib only."""
from pathlib import Path
import csv, hashlib, itertools
from collections import defaultdict
ROOTS=(3,5,6,7)
PIN="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
MASTER="cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"
CSV="a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f"

def load_native(master_path,csv_path):
    master=Path(master_path); csvfile=Path(csv_path)
    assert hashlib.sha256(master.read_bytes()).hexdigest()==MASTER
    assert hashlib.sha256(csvfile.read_bytes()).hexdigest()==CSV
    with master.open() as f:
        nk,nw,nconfigs=map(int,f.readline().split())
        assert (nk,nw,nconfigs)==(94,178850,38169)
        families=[]
        for _ in range(nk):
            masks=[0]*4
            for _ in range(int(f.readline())):
                label,word=f.readline().split()
                masks[ROOTS.index(bytes.fromhex(word)[0])] |= 1<<int(label)
            families.append(masks)
        configs=[tuple(map(int,f.readline().split())) for _ in range(nconfigs)]
    def domain(conf):
        result=[0]*24
        for fid in conf:
            for j,mask in enumerate(families[fid]):
                while mask:
                    one=mask&-mask
                    result[one.bit_length()-1]|=1<<j
                    mask^=one
        return tuple(result)
    target=domain(configs[16943])
    ids=[i for i,c in enumerate(configs) if domain(c)==target]
    assert len(ids)==310
    opts=[k for k in range(24) if target[k].bit_count()>1]
    alloc=list(itertools.product(*(tuple(r for j,r in enumerate(ROOTS) if target[k]>>j&1) for k in opts)))
    assert len(alloc)==144
    subsets={}
    for j,r in enumerate(ROOTS):
        ls=[k for k in opts if target[k]>>j&1]
        subsets[r]=sorted(sum(1<<k for k,b in zip(ls,bits) if b)
                          for bits in itertools.product((0,1),repeat=len(ls)))
    keys=[(r,s) for r in ROOTS for s in subsets[r]]
    assert len(keys)==84
    costs=defaultdict(dict);idset=set(ids)
    with csvfile.open() as f:
        for row in csv.DictReader(f):
            cid=int(row["config"])
            if cid in idset:
                key=(int(row["root"]),int(row["subset"]))
                assert key not in costs[cid]
                costs[cid][key]=int(row["cost"])
    assert len(costs)==310 and all(len(costs[cid])==84 for cid in ids)
    profiles={};reps=[];multiplicity=[]
    for cid in ids:
        prof=tuple(costs[cid][k] for k in keys)
        if prof not in profiles:
            profiles[prof]=len(profiles)
            reps.append(cid);multiplicity.append(0)
        multiplicity[profiles[prof]]+=1
    assert len(reps)==141 and sum(multiplicity)==310
    terminal=[]
    for assignment in alloc:
        masks={r:0 for r in ROOTS}
        for k,r in zip(opts,assignment): masks[r]|=1<<k
        terminal.append(tuple(sum(costs[cid][r,masks[r]] for r in ROOTS) for cid in reps))
    named=[tuple(costs[cid][key] for cid in reps) for key in keys]
    V=terminal+named
    assert len(V)==228
    return V,multiplicity,reps

def read_tree(tree,V,m):
    uR=uT=mR=mT=0
    for i in range(141):
        cur=tree;used=set()
        while "leaf" not in cur:
            q=cur["q"]
            assert 0<=q<228 and q not in used
            used.add(q)
            if q>=144: uR+=1;mR+=m[i]
            else: uT+=1;mT+=m[i]
            cur=cur["children"][str(V[q][i])]
        assert cur["leaf"]==i
    return (uR,uT,mR,mT)
